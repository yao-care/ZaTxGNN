"""ZA 依成分重建證據包的許可證紀錄（2026-11-05，用戶核准；做法比照母 repo br_rebuild_by_ingredient_20261031.py）。

原本的許可證紀錄來自 scripts/download_mpr_data.py：只依約 200 個常見藥名查 MPR（Medicine Price Registry），
再經 DrugBank 對照、每藥最多 20 筆，所以常只收到部分註冊號（diazepam 只收到 1 張已註銷的 Benzopin 2，
頁面就寫成 Not marketed；SAHPRA 全量裡含 diazepam 的註冊有 37 張，22 張 Registered）。另外 MPR 的成分欄有錯植
（Valheft 80 是 valsartan 產品，成分欄多列了 donepezil），錯的產品被收進別的藥。

來源（全程不用 AI）：
- SAHPRA medapps 匯出全量（data/raw/sahpra_status.json，scripts/license_adapter.py 下載）：註冊號、產品名、成分全文、狀態。
  舊制藥品（Old Medicine）以申請號（例 G2963）當號碼。這是主要來源：成分以 SAHPRA 成分全文為準。
- MPR API 依每個成分查（https://medicineprices.org.za/api/v2/search?q=<成分>，快取 data/raw/mpr_by_ingredient/）：
  補產品名、劑型（SAHPRA 沒有劑型欄），以及 SAHPRA 匯出沒收到的註冊號（匯出依註冊日期篩選，沒有日期的品項不在檔內）。
  MPR 的號碼在 SAHPRA 全量裡、但 SAHPRA 成分全文不含本藥 → 判定為 MPR 成分欄錯植，剔除。

做法：
1. 本藥成分名（terms）：INN 去掉鹽類字尾（amlodipine besylate → amlodipine；鹽類頁依成分計，與現行頁面一致）
   ＋南非常用名（acetaminophen → paracetamol 等，SYN）；d-／l-／dl- 前綴去掉；無機鹽（calcium acetate）整個名稱就是成分。
   單一元素／離子頁（calcium、copper…）依成分查會吃進所有鹽類，不重建，只清理（剔除非註冊號、錯植，更新狀態）。
2. SAHPRA 成分全文以整詞出現本藥成分名的註冊全收（ethinyl estradiol 不算 estradiol）；同號多列任一列不是 Canceled 即有效。
3. 狀態：Canceled → cancelled；Registered／Registrered／Old Medicine → valid；SAHPRA 沒有的 MPR 號碼狀態空白、視為有效（同 license_adapter）。
   2026-11-06（用戶決定）：MPR 號碼先做寫法統一再對 SAHPRA（規則見 _sig／same_product／build_alias 上方註解；對到的一律改寫成
   SAHPRA 匯出的寫法、取 SAHPRA 狀態）；統一後仍查不到的照樣算有效，但標 status_unconfirmed，頁面加註「not confirmed by SAHPRA」
   （許可證表狀態格、概覽狀態列、張數列，見 scripts/sync_license_pages.py 與 tools/txgnn/.claude/check_drug_page.py 的 UNCONFIRMED_ST）。
4. 剔除：不是註冊號的列（ITN 調配營養液的「EXCLUSION UNDER SECTION 36 & SECTION 14」「ARTICLE 21B N/A」等）；
   MPR 錯植（見上）；人工清單 MISMATCH（SAHPRA 沒有的號碼，附理由）。剔除的列存進 tfda.excluded_records（附原因），不刪資料。
5. 張數依全量：records 收全部（不截 20 筆），total_matches＝不重複號碼數。排序：有效在前、MPR 有價格登錄（市面上買得到）在前、
   單方在前。頁面表格只列前 N 筆（scripts/sync_license_pages.py）。
6. 停損：原有紀錄（剔除錯植與非註冊號後、且號碼在 SAHPRA 全量裡）一半以上不在新結果裡 → 成分名可能對錯，不改、列出來。

用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--dry-run] [--report out.tsv] [頁 ...]
"""
import difflib
import json
import re
import sys
import time
import unicodedata
from collections import Counter
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
CACHE = ROOT / "data/raw/mpr_by_ingredient"
SAHPRA = ROOT / "data/raw/sahpra_status.json"
MPR_URL = "https://medicineprices.org.za/api/v2/search"
SOURCE = "SAHPRA medapps export (ingredients, status) + MPR by ingredient (2026-11-05 rebuild)"

# INN（DrugBank 寫法）→ 南非 SAHPRA／MPR 成分欄的寫法（只收同一個成分的別名）
SYN = {
    "acetaminophen": ["paracetamol"], "chlorpheniramine": ["chlorphenamine"], "epinephrine": ["adrenaline"],
    "norepinephrine": ["noradrenaline"], "ascorbic acid": ["vitamin c"], "thiamine": ["vitamin b1"],
    "riboflavin": ["vitamin b2", "riboflavine"], "pyridoxine": ["vitamin b6"], "cyanocobalamin": ["vitamin b12"],
    "cholecalciferol": ["vitamin d3"], "ergocalciferol": ["vitamin d2"], "vitamin a": ["retinol"],
    "tocopherol": ["vitamin e"], "alpha tocopherol": ["vitamin e", "tocopherol"], "lidocaine": ["lignocaine"],
    "dicyclomine": ["dicycloverine"], "guaifenesin": ["guaiphenesin"], "sulfamethoxazole": ["sulphamethoxazole"],
    "furosemide": ["frusemide"], "nitroglycerin": ["glyceryl trinitrate"], "glyceryl trinitrate": ["nitroglycerin"],
    "acetylsalicylic acid": ["aspirin"], "mepyramine": ["pyrilamine"], "estradiol": ["oestradiol"],
    "ethinylestradiol": ["ethinyl estradiol", "ethinyloestradiol", "ethinyl oestradiol"], "cefalexin": ["cephalexin"],
    "cephalexin": ["cefalexin"], "amoxicillin": ["amoxycillin"], "sulfadoxine": ["sulphadoxine"],
    "sulfadiazine": ["sulphadiazine"], "levothyroxine": ["thyroxine"], "rifampicin": ["rifampin"],
    "dextropropoxyphene": ["propoxyphene"],
}
# 前面接這些字時不算本藥（ethinyl estradiol 不是 estradiol；perindopril arginine 的 arginine 是鹽）
NOT_PRECEDED = {"estradiol": r"ethinyl\s+$", "oestradiol": r"ethinyl\s+$", "alanine": r"(beta|phenyl)\s*$",
                "arginine": r"perindopril\s+(l\s+)?$", "lysine": r"(ibuprofen|aspirin|acetylsalicylic acid|ketoprofen|clonixin)\s+(l\s+)?$"}
SALT = re.compile(r"\b(hydrochloride|hcl|hydrobromide|besylate|besilate|maleate|mesylate|mesilate|tartrate|bitartrate|fumarate|succinate|"
                  r"citrate|acetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|"
                  r"monohydrate|dihydrate|trihydrate|tetrahydrate|hexahydrate|hemihydrate|anhydrous|sodium|potassium|calcium|magnesium|"
                  r"disodium|cilexetil|axetil|dihydrochloride|bromide)\b")
INORGANIC = re.compile(r"^(calcium|copper|cupric|magnesium|zinc|iron|ferrous|ferric|potassium|sodium|chromium|chromic|selenium|manganese|"
                       r"aluminium|aluminum|ammonium|lithium|silver|bismuth|barium|strontium)\b")
HYDRATE = re.compile(r"\b(monohydrate|dihydrate|trihydrate|tetrahydrate|hexahydrate|hemihydrate|anhydrous)\b")
NO_REBUILD = re.compile(r"^(calcium|copper|magnesium|zinc|iron|iodine|potassium|sodium|chromium|selenium|manganese|fluoride|chloride|"
                        r"phosphorus|phosphate|water|glucose|d glucose|dextrose|oxygen|nitrogen)$")
# 單一元素頁裡，SAHPRA 成分全文寫法不會跟其他藥的鹽類混淆的，照常依成分重建（其他元素頁只清理）
ELEMENT_TERMS = {"selenium": ["selenium", "selenite", "selenate"], "nitrogen": ["nitrogen"]}
# 人工核對是 MPR 成分欄錯植、或註冊身分對不上的產品（(號碼, 本藥成分名) → 理由）；號碼依寫法統一後比對
# 「*X」＝這個產品的真正成分是 X：本藥不是 X 就是錯植
MISMATCH = {
    ("A.682", "*pyrimethamine"): "Daraprim 是 pyrimethamine 產品，MPR 成分欄另列 clindamycin 屬錯植",
    ("P/7.1.4/281", "*glyceryl trinitrate"): "Nitrolingual 是 glyceryl trinitrate 舌下噴劑，MPR 成分欄另列 paracetamol、chlorphenamine、calcium ascorbate 等屬錯植",
    ("T/2.2/207", "*midazolam"): "Dormicum 是 midazolam 產品，MPR 成分欄另列 naproxen 屬錯植",
    ("L/2.5/188", "*valproic acid"): "Epilim EC 500 是 valproate 產品，MPR 成分欄另列 promethazine、ephedrine 等屬錯植",
    ("D/26/174", "*bleomycin"): "Blenoxane 是 bleomycin 產品，MPR 成分欄另列 promethazine 屬錯植",
    ("H1786 (ACT 101/1965)", "*acetazolamide"): "Diamox Tablets 250 mg 是 acetazolamide 產品，MPR 成分欄另列 triamterene 屬錯植（SAHPRA 匯出查無此號）",
    ("37/34/0243", "cycloserine"): "Nutrineal PD4 是腹膜透析胺基酸液，不含 cycloserine（MPR 成分欄誤植；SAHPRA 成分全文被截斷，無法自動排除）",
    # 2026-11-06（用戶決定剔除）：號碼寫法統一後對到的 SAHPRA 產品跟 MPR 品名或本藥對不上
    ("BV329", "morphine"): "MPR 品名 Opium Camphorated Tinct，但號碼 BV329 補零後是 SAHPRA BV0329 EXTRACT OF MALT AND COD LIVER OIL（麥芽魚肝油，"
                           "不同產品）；這張註冊的身分無法確認，不列入 morphine",
    ("BV362", "morphine"): "MPR 品名 Gees Linctus（即 Squill Opiate Linctus），號碼補零後是 SAHPRA BV0362 SQUILL OPIATE LINCTUS（舊制藥品）；"
                           "SAHPRA 成分全文是 oxymel of squill、camphorated opium tincture、tolu syrup，不是以 morphine 登記的製劑，不列入 morphine",
    ("T/30.3/704", "calcium"): "MPR 品名 Stabilised Human Serum-5% Protein Solution，號碼補零後是 SAHPRA T/30.3/0704 STABILISED HUMAN SERUM"
                               "（人血清蛋白，已註銷）；MPR 成分欄列的 calcium、potassium 是血清本身含的電解質，不是 calcium 製劑",
    ("G0894", "sulfamethoxazole"): "MPR Cocc.Co.Syrup（G 894）對回 SAHPRA G0894 ADCO-COCILLANA COMPOUND SYRUP（見 MANUAL_ROWS）；SAHPRA 成分只有 "
                                   "cocillana liquid extract、menthol、tinctura scillae，MPR 成分欄的 sulfamethoxazole（劑量寫 200 ml）是誤植，不列入 sulfamethoxazole"
                                   "（SAHPRA 成分全文含 extract 字樣，自動判定不採用，故列人工清單）",
    ("T/30.3/704", "potassium"): "MPR 品名 Stabilised Human Serum-5% Protein Solution，號碼補零後是 SAHPRA T/30.3/0704 STABILISED HUMAN SERUM"
                                 "（人血清蛋白，已註銷）；MPR 成分欄列的 calcium、potassium 是血清本身含的電解質，不是 potassium 製劑",
}


# 人工核對的 MPR 列（2026-11-06，用戶看完逐筆查證後決定）：同一個 MPR 號碼依產品名分開處理（MISMATCH 只能依號碼＋本藥成分）。
# mpr＝MPR 號碼（依 key() 比對）、name＝MPR 產品名（norm() 後相同，或以它開頭）；
# to＝這一列其實是 SAHPRA 的哪個號碼（對回後取 SAHPRA 狀態、號碼寫法與產品名）；exclude＝剔除理由（任何藥都不收這一列）。
# 依據：MPR https://medicineprices.org.za/api/v2/search?q=<詞>；SAHPRA medapps 匯出（data/raw/sahpra_status.json，
# https://medapps.sahpra.org.za:6006/DateSearch/ExportData）；SAHPRA PI/PIL 公開庫（https://pi-pil-repository.sahpra.org.za/）查無這些舊制藥品的仿單。
MANUAL_ROWS = [
    {"mpr": "C777", "name": "colcleer paediatric",
     "exclude": "MPR 號碼 C777 補零後是 SAHPRA C0777 ASALEN PAEDIATRIC SYRUP（Adcock Ingram，已註銷，成分只有 chlorpheniramine maleate、"
                "phenylephrine HCl）；MPR 的 Colcleer paediatric 含 paracetamol 75 mg/5ml、caffeine，不是 C0777 登記的配方，SAHPRA 也沒有 Colcleer 糖漿"
                "（只有 C0810 COLCLEER TABLETS）。不是 SAHPRA 可查證的註冊，剔除（就算視為同一產品，SAHPRA 也是 Canceled）。"
                "依據 https://medicineprices.org.za/api/v2/search?q=colcleer ；SAHPRA 匯出 C0777、C0810"},
    {"mpr": "C661", "name": "corbar linctus",
     "exclude": "MPR 把 Corbar linctus 200 ml（NAPPI 716073013）寫成 C661，同一產品 100 ml（NAPPI 716073005）寫的是 G1032；"
                "C661 補零後是 SAHPRA C0661 CORENZA C（發泡錠，不同產品）。Corbar linctus 的註冊是 SAHPRA G1032 CORBAR LINCTUS（已註銷，"
                "成分與含量逐項相符），已由 G1032 那一列代表，這一列剔除、不重複計算。依據 https://medicineprices.org.za/api/v2/search?q=corbar ；"
                "SAHPRA 匯出 G1032、C0661"},
    {"mpr": "C661", "name": "corenza c", "to": "C0661",
     "why": "MPR Corenza c（NAPPI 716170019／716170020）＝SAHPRA C0661 CORENZA C（Adcock Ingram，Old Medicine）：補零後號碼相同、"
            "品名相同、aspirin 500 mg、ascorbic acid 500 mg、moroxydine 100 mg、phenylephrine、chlorpheniramine 2 mg 相符。"
            "MPR 20 錠包裝多列的 thiamine 不在 SAHPRA 配方，依 SAHPRA 成分不算 thiamine。依據 https://medicineprices.org.za/api/v2/search?q=corenza ；SAHPRA 匯出 C0661"},
    {"mpr": "G894", "name": "cocc co syrup", "to": "G0894",
     "why": "MPR Cocc.Co.Syrup（Cocillana Compound Syrup，NAPPI 715007007）＝SAHPRA G0894 ADCO-COCILLANA COMPOUND SYRUP（已註銷）："
            "補零後號碼相同，MPR 列的 cocillana、squill、menthol 正好是 G0894 的全部成分；MPR 另列的 sulfamethoxazole（劑量寫 200 ml）"
            "不在 SAHPRA 配方，判斷是 MPR 誤植，依 SAHPRA 成分不算 sulfamethoxazole。依據 https://medicineprices.org.za/api/v2/search?q=cocillana ；SAHPRA 匯出 G0894、G0896"},
    {"mpr": "E512", "name": "anugesic", "to": "E0512",
     "why": "MPR Anugesic 栓劑（NAPPI 704075008）＝SAHPRA E0512 ANUSOL PAIN RELIEF SUPPOSITORIES（MDI Healthcare，Old Medicine）："
            "MPR 自己把同品牌軟膏寫成「Anusol pain relief (was anugesic)」（T/11.8/65＝SAHPRA T/11.8/0065 ANUSOL PAIN RELIEF OINTMENT），"
            "補零後號碼相同、劑型相同，MPR 列的 8 個成分都在 SAHPRA 配方（bismuth subiodide＝bismuth iodide oxide、pramocaine＝pramoxine）。"
            "依據 https://medicineprices.org.za/api/v2/search?q=anugesic ；SAHPRA 匯出 E0512、T/11.8/0065"},
]


def manual(raw, name):
    """MANUAL_ROWS 裡對到這一列（MPR 號碼＋產品名）的那一筆；沒有回傳 None"""
    k, n = key(raw), norm(name)
    for m in MANUAL_ROWS:
        if key(m["mpr"]) == k and n and (n == m["name"] or n.startswith(m["name"] + " ")):
            return m
    return None


def record_order(r):
    """證據包紀錄與頁面許可證表的排序（重建與每週更新共用）：有效在前、MPR 有價格登錄在前、單方在前、號碼"""
    return (r.get("license_status", "valid") != "valid", not r.get("in_mpr"), r.get("kind") != "single", str(r.get("license_id") or ""))


def norm(x):
    x = unicodedata.normalize("NFKD", str(x or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", x).split())


def key(k):
    """號碼正規化：去空白、去「(ACT 101/1965)」「(OM)」「(O/M)」註記（舊制藥品依 1965 年第 101 號法令登記的註記，不是號碼的一部分）"""
    k = re.sub(r"\((ACT|OM|O/M)\b[^)]*\)", "", str(k or ""), flags=re.I)
    # 號碼後面的舊制註記，MPR 有各種寫法：「ACT 101 OF 1965」「(ACT101/1965)」「(ACT 101/1965」「(OLD MEDICNE)」
    k = re.sub(r"\s*\(?\s*(ACT\s*101|OLD\s+MEDIC\w*)[^)]*\)?\s*$", "", k, flags=re.I)
    return re.sub(r"\s+", "", k).upper()


# ---- 號碼寫法統一（2026-11-06，用戶決定；只用在比對，頁面與證據包一律寫 SAHPRA 匯出的原寫法）----
# MPR 價格登錄的註冊號是人工鍵入，跟 SAHPRA 匯出常差在寫法。下列差異都不改變號碼本身（字首字母＋數字段的順序與數值）：
#   R1 舊制註記：「(OM)」「(O/M)」「(ACT 101 1965)」等是登記依據的註記（key() 去掉）
#   R2 空白：「G 894」「B 1492」（key() 去掉）
#   R3 數字段前導零：27/3.1/321 ＝ 27/3.1/0321、舊制申請號 A557 ＝ A0557（SAHPRA 匯出本身兩種寫法都有，例 27/20.2.2/201、31/7.5/0447）
#   R4 小數逗號：藥理分類 3,1 ＝ 3.1（南非以逗號作小數點，SAHPRA 匯出含量也寫 40,0 mg）
#   R5 分隔符號：分類段後多打的點或斜線（20.2.2./、11.4.3//）、年份或分類後的點應為斜線（45.20.2.8/0111 ＝ 45/20.2.8/0111、
#      44/10.2.2.0890 ＝ 44/10.2.2/0890）、字首字母後少斜線或多點（L13.4.1/66 ＝ L/13.4.1/66、A.39/… ＝ A39/…、G.524 ＝ G0524）
#   R6 子號：最後一段後的「.326」（SAHPRA 用來標示複製註冊的原號，例 54/7.5/0330.326 ＝ 54/7.5/0330）；只在完整寫法對不到時才試
# 比對方式：兩邊都化成「字首字母＋數字段數值序列」（R3–R5 只影響這個序列以外的部分），只有下列條件全部成立才當成同一張註冊：
#   (1) SAHPRA 全量裡只有一個號碼化成這個序列（SAHPRA 自己有兩個號碼撞在一起的，例 A809／A0809 是兩個不同產品，一律不比對）；
#   (2) 產品相符：MPR 產品名第一個字（去掉 Adco 等廠牌字、劑型字）出現在 SAHPRA 產品名，或 MPR 列的成分全部出現在 SAHPRA 成分全文；
#   (3) 一對一：全部 MPR 資料裡化成同一個 SAHPRA 號碼的寫法，產品都相符（rebuild 時逐筆檢查 (2)）。
# 不符合的不改，照原號碼留在「只有 MPR」那一類。
def _sig(k, drop_sub=False):
    k = key(k)
    if drop_sub:
        k = re.sub(r"(?<=/\d{4})\.\d{3}$", "", k)
    m = re.fullmatch(r"([A-Z]{0,2})[./]?(\d[\d.,/]*)", k)
    if not m:
        return None
    nums = [x for x in re.split(r"[./,]+", m.group(2)) if x]
    return (m.group(1), tuple(int(x) for x in nums)) if nums else None


# 劑型、規格等不能區分產品的字（廠牌字不在這裡：Adco-Simvastatin 與 Simvastatin Sandoz 是不同產品）
GENERIC_W = {"tablets", "tablet", "tabs", "tab", "tabl", "capsules", "capsule", "caps", "syrup", "cream", "ointment", "injection", "inj",
             "solution", "suspension", "drops", "gel", "lotion", "mg", "ml", "mcg", "the", "and", "for", "with", "sr", "xl", "cr", "forte",
             "plus", "co", "dt", "ec", "oral", "eye", "ear", "nasal", "spray", "powder", "sachets", "vials", "vial", "infusion",
             "elixir", "linctus", "mixture", "paediatric", "pediatric", "lozenges", "ampoules", "ampoule", "amp", "pfs", "new", "formula"}
ING_SKIP = {"alcohol", "water", "purified water", "ethanol", "sucrose", "glucose", "sorbitol"}


def same_product(name, ings, s):
    """MPR 那一列（產品名、成分）跟 SAHPRA 那一列是不是同一個產品（只用在號碼寫法統一）。回傳依據（"name"／"ingredients"）或 None。
    產品名：產品名裡不是成分名的字（品牌、廠牌）取第一個，要出現在 SAHPRA 產品名；
    成分：MPR 列的成分（去掉酒精、水等溶劑）全部出現在 SAHPRA 成分全文（同號產品改名時，例 Flemlite／FLUSIN MUCOUS COUGH）"""
    sn = " " + norm(s.get("name")) + " "
    il = [norm(i) for i in ings if norm(i) and norm(i) not in ING_SKIP]
    ing_words = {w for i in il for w in i.split()}
    words = [w for w in norm(name).split() if len(w) >= 3 and not w.isdigit() and w not in GENERIC_W]
    brand = [w for w in words if w not in ing_words]
    if brand and _word_hit(brand[0], sn):
        return "name"
    if il and all(mentions(s.get("_ing") or "", base_name(i)) or f" {base_name(i)} " in sn for i in il):
        return "ingredients"
    return None


def _word_hit(w, sn):
    """產品名的一個字出現在 SAHPRA 產品名：整字、連寫（Dis-Chem／DISCHEM）、拼字相近（Valduo／VALDOU，前 3 字母相同、相似度 ≥0.8）"""
    if f" {w} " in sn:
        return True
    if len(w) >= 5 and w in sn.replace(" ", ""):
        return True
    return len(w) >= 5 and any(len(x) >= 5 and x[:3] == w[:3] and difflib.SequenceMatcher(None, w, x).ratio() >= 0.8 for x in sn.split())


def resolve(raw, name, ings, S, SIG):
    """MPR 一列的號碼 → (SAHPRA 號碼 key, 依據)；對不到或不符合條件回傳 (None, 原因)"""
    if key(raw) in S:
        return key(raw), "exact"
    for drop in (False, True):
        g = _sig(raw, drop)
        if not g:
            return None, "not a registration number"
        cands = SIG.get(g) or set()
        if len(cands) > 1:
            return None, "SAHPRA 有多個號碼化成同一序列：" + "、".join(sorted(cands))
        if len(cands) == 1:
            k = next(iter(cands))
            why = same_product(name, ings, S[k])
            return (k, why) if why else (None, f"產品不符：MPR {name}／SAHPRA {S[k].get('name')}")
    return None, "SAHPRA 沒有"


def build_alias(S, rows):
    """{MPR 號碼 key: (SAHPRA 號碼 key, 依據)}；rows＝[(原號碼, 產品名, [成分])]，全部 MPR 列（快取＋證據包原有紀錄）。
    一對一：同一個 MPR 號碼的每一列都要對到同一個 SAHPRA 號碼（MPR 自己把一個號碼給了兩個產品的，例 C661 Corbar／Corenza，不比對）；
    SAHPRA 號碼本身也出現在 MPR 時，那些列也要跟 SAHPRA 是同一個產品，否則對到它的別種寫法全部不比對。
    回傳 (alias, 報告列)"""
    from collections import defaultdict
    SIG = defaultdict(set)
    for k in S:
        g = _sig(k)
        if g:
            SIG[g].add(k)
    by = defaultdict(list)
    for raw, name, ings in rows:
        if is_reg(raw):
            by[key(raw)].append((raw, name, ings))
    alias, rep = {}, []
    for k, rs in by.items():
        if k in S:
            continue
        got = [resolve(r, n, i, S, SIG) for r, n, i in rs]
        ks = {g[0] for g in got}
        if len(ks) == 1 and None not in ks:
            alias[k] = (ks.pop(), sorted({g[1] for g in got}))
        elif any(g[0] for g in got):
            rep.append((rs[0][0], "", "不比對：同一號碼的 MPR 列結果不一致（" + "；".join(sorted({f'{n}→{g[0] or g[1]}' for (_, n, _), g in zip(rs, got)})) + "）"))
    for k in {v[0] for v in alias.values()}:
        exact = by.get(k) or []
        if exact and not all(same_product(n, i, S[k]) for _, n, i in exact):
            for a in [a for a, v in alias.items() if v[0] == k]:
                rep.append((by[a][0][0], S[k]["reg"], f"不比對：SAHPRA 號碼 {S[k]['reg']} 在 MPR 另有不同產品（{exact[0][1]}）"))
                del alias[a]
    for a, (k, why) in sorted(alias.items()):
        rep.append((by[a][0][0], S[k]["reg"], "比對：" + "＋".join(why) + f"（MPR {by[a][0][1]}／SAHPRA {S[k].get('name')}，{S[k].get('status')}）"))
    return alias, rep


_RX = {}


def has(text, term):
    if term not in text:
        return False
    rx = _RX.get(term) or _RX.setdefault(term, re.compile(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"))
    pre = NOT_PRECEDED.get(term)
    for m in rx.finditer(text):
        if not pre or not re.search(pre, text[:m.start()]):
            return True
    return False


def is_reg(k):
    k = str(k or "").strip()
    return bool(k) and bool(re.search(r"\d", k)) and not re.search(r"EXCLUSION|ARTICLE|SECTION|N/A|^NA$", k, re.I)


def base_name(inn):
    inn = re.sub(r"^(dl|d|l)( alpha)? (?=[a-z]{4})", "", inn)
    if INORGANIC.match(inn):  # 無機鹽（calcium acetate、zinc gluconate）：整個名稱就是成分，只去水合物字樣
        return " ".join(HYDRATE.sub(" ", inn).split()) or inn
    return " ".join(SALT.sub(" ", inn).split()) or inn


def variant(a, b):
    """拼字變體：前面的詞相同，最後一個詞前 4 字相同且相似度 ≥0.88（tacrolimo／tacrolimus；vitamin a ≠ vitamin e）"""
    x, y = a.split(), b.split()
    if len(x) != len(y) or x[:-1] != y[:-1] or len(x[-1]) < 5 or len(y[-1]) < 5 or x[-1][:4] != y[-1][:4]:
        return False
    return difflib.SequenceMatcher(None, x[-1], y[-1]).ratio() >= 0.88 and abs(len(x[-1]) - len(y[-1])) <= 3


def derive_terms(inn, recs, bundle=None):
    base = base_name(inn)
    terms = {base} | set(SYN.get(base, [])) | set(SYN.get(inn, []))
    # 上次重建用過的成分名照樣沿用（2026-11-06）：拼字變體是從「重建前」的 MPR 紀錄學來的（例 MPR 誤拼 Triprodlidine），
    # 重建後紀錄改用 SAHPRA 成分全文，再重建一次就學不到，MPR 那幾列會掉出來（產品名、劑型、in_mpr 跟著變）
    terms |= {norm(x) for x in ((bundle or {}).get("tfda") or {}).get("query_terms") or [] if norm(x)}
    seen = Counter(norm(x) for r in recs for x in set(re.split(r";", r.get("ingredients") or "")) if norm(x))
    for c in seen:  # 原有紀錄裡跟 INN 相近的寫法（拼字變體）
        cb = base_name(c)
        if cb and cb not in terms and variant(cb, base):
            terms.add(cb)
    return sorted(t for t in terms if len(t) >= 4)


def mpr(term, session):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (re.sub(r"[^a-z0-9]+", "_", term) + ".json")
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    for attempt in range(4):
        try:
            r = session.get(MPR_URL, params={"q": term}, timeout=60)
            r.raise_for_status()
            data = r.json()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(5 * (attempt + 1))
    f.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    time.sleep(0.5)
    return data


UNITS = {"mg", "g", "mcg", "ml", "iu", "kg", "l", "mmol", "u"}


def tidy(name):
    """SAHPRA 產品名是全大寫：每個字首字大寫，單位小寫"""
    return " ".join(w.lower() if w.lower() in UNITS else (w.capitalize() if w.isalpha() and w.isupper() else w) for w in str(name or "").split())


def n_ingredients(text):
    lines = [l for l in re.split(r"[\r\n]+", text) if l.strip() and not re.search(r"\bCONTAINS?\b\s*:?\s*$", l, re.I)]
    if len(lines) > 1:
        return len(lines)
    return max(1, len(re.findall(r"\d[\d,.]*\s*(mg|g|mcg|µg|ml|iu|%|units?|mmol)\b", text, re.I)))


def form_of(text):
    m = re.search(r"EACH\s+(?:[\d,.]+\s*\w+\s+)?([A-Za-z][A-Za-z /-]{2,40}?)\s+CONTAINS", str(text or ""), re.I)
    return m.group(1).strip().lower() if m else ""


# SAHPRA 成分全文只寫類別名（AMINO ACID SOLUTION WITH ELECTROLYTES）時，不能當「不含本藥」的證據
GROUP = re.compile(r"amino acid|vitamins|trace element|electrolyte|multivitamin|minerals|lipid emulsion|herbal|extract")


def truncated(text):
    """SAHPRA 成分全文多成分時常被截斷（最後一行只有成分名、沒有含量）；截斷的全文不能當「不含本藥」的證據"""
    lines = [l for l in re.split(r"[\r\n]+", str(text or "")) if l.strip()]
    return bool(lines) and not re.search(r"\d", lines[-1])


def mentions(s_ing, term):
    """寬鬆比對（只用在判定 MPR 錯植時）：整詞、字首（fusidic → sodium fusidate）、拼字相近（pantroprazole）"""
    if has(s_ing, term):
        return True
    w0 = term.split()[0]
    if len(w0) >= 4 and w0[:max(4, min(5, len(w0) - 2))] in s_ing:
        return True
    return any(difflib.SequenceMatcher(None, w, w0).ratio() >= 0.85 for w in set(s_ing.split()) if abs(len(w) - len(w0)) <= 3)


COMBO_MARK = re.compile(r"\b(co|plus|compound|comp|forte co|with|duo|combi)\b|^co-|\d\s*/\s*\d|\+", re.I)


def load_vocab():
    """DrugBank 藥名（單字、≥6 字母）：MPR 產品名含別的藥名時判定錯植"""
    import csv
    f = ROOT / "data/external/drugbank_vocab.csv"
    if not f.exists():
        return set()
    with open(f, encoding="utf-8-sig", newline="") as fh:
        return {n for n in (norm(r.get("drug_name")) for r in csv.DictReader(fh)) if n.isalpha() and len(n) >= 6}


def load_sahpra(data=None):
    """{號碼 key: SAHPRA 一列}；data＝已讀進來的匯出（每週更新用），沒給就讀 data/raw/sahpra_status.json"""
    by = {}
    for r in (data if data is not None else json.loads(SAHPRA.read_text(encoding="utf-8"))):
        if str(r.get("ingredients") or "").strip().lower() in ("none", "null", "n/a"):
            r = {**r, "ingredients": ""}
        k = key(r["reg"])
        cur = by.get(k)
        if cur is None:
            by[k] = {**r, "_ing": norm(r.get("ingredients")), "_rows": 1, "_trunc": truncated(r.get("ingredients"))}
        else:
            cur["_rows"] += 1
            if norm(r.get("ingredients")):  # 空白的成分欄（原檔寫 None）不併進來，否則「不含本藥」會誤判
                cur["_ing"] = (cur["_ing"] + " | " if cur["_ing"] else "") + norm(r.get("ingredients"))
            cur["_trunc"] = cur["_trunc"] or truncated(r.get("ingredients"))
            if cur["status"] == "Canceled" and r["status"] != "Canceled":
                cur.update({x: r[x] for x in ("status", "name", "applicant") if r.get(x)})
    return by


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = {a for a in argv if not a.startswith("--") and a != rep}
    S = load_sahpra()
    VOCAB = load_vocab()
    if not any(v.get("ingredients") for v in S.values()):
        sys.exit("sahpra_status.json 沒有成分欄（先用新版 scripts/license_adapter.py 重新下載）")
    sess = requests.Session()
    sess.headers["User-Agent"] = "ZaTxGNN-license-rebuild (+https://zatxgnn.yao.care)"
    # 號碼寫法統一（2026-11-06）：先把各藥要查的 MPR 都取齊（有快取就不重抓），再用全部 MPR 列建對照表
    mrows = []
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        b = json.loads(f.read_text(encoding="utf-8"))
        old = (b.get("tfda") or {}).get("records") or []
        inn = norm(b.get("drug", {}).get("inn") or f.parent.name.replace("_", " "))
        for term in ([] if NO_REBUILD.match(inn) and inn not in ELEMENT_TERMS else (ELEMENT_TERMS.get(inn) or derive_terms(inn, old, b))):
            mpr(term, sess)
        for r in old + ((b.get("tfda") or {}).get("excluded_records") or []):
            if r.get("in_mpr") or not r.get("status"):  # MPR 來的列（SAHPRA 來的列用不到）
                mrows.append((str(r.get("license_id") or ""), r.get("brand_name_en") or "", str(r.get("ingredients") or "").split(";")))
    for f in sorted(CACHE.glob("*.json")):
        for x in json.loads(f.read_text(encoding="utf-8")):
            mrows.append((str(x.get("regno") or ""), x.get("name") or "", [i.get("name") or "" for i in x.get("ingredients") or []]))
    ALIAS, alias_rep = build_alias(S, mrows)

    def rk(raw, name=None):
        """比對用的號碼：SAHPRA 有的用 SAHPRA 的 key（含寫法統一、MANUAL_ROWS 人工對照），沒有的用原號碼的 key"""
        m = manual(raw, name) if name is not None else None
        if m and m.get("to") and key(m["to"]) in S:
            return key(m["to"])
        k = key(raw)
        return k if k in S else ALIAS.get(k, (k,))[0]

    def official(raw, name=None):
        """頁面與證據包寫的號碼：SAHPRA 有的一律用 SAHPRA 匯出的寫法（讀者可以直接拿去 SAHPRA 查），沒有的照 MPR 原寫法"""
        k = rk(raw, name)
        return S[k]["reg"] if k in S else str(raw or "").strip()
    rows = [("bundle", "inn", "terms", "action", "old_n", "old_valid", "new_n", "new_valid", "new_cancelled", "excluded", "note")]
    exrows = [("bundle", "license_id", "product", "ingredients", "reason")]
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        pg = f.parent.name
        if only and pg not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.setdefault("tfda", {})
        old = t.get("records") or []
        inn = norm(b.get("drug", {}).get("inn") or pg.replace("_", " "))
        old_valid = sum(1 for r in old if (r.get("license_status") or "valid") == "valid")
        terms = ELEMENT_TERMS.get(inn) or derive_terms(inn, old, b)
        excluded = []

        def check(k, name=None):
            """回傳剔除理由或 None（name＝MPR 產品名，給 MANUAL_ROWS 用）"""
            m = manual(k, name) if name is not None else None
            if m and m.get("exclude"):
                return m["exclude"]
            if not is_reg(k):
                return "不是註冊號（ITN 調配營養液的豁免條款、IMPORT PERMIT 等）"
            for (mk, tm), why in MISMATCH.items():  # 人工清單先判（理由較具體）
                if (key(mk) == key(k) or rk(mk) == rk(k, name)) and (tm[1:] not in terms if tm.startswith("*") else tm in terms):
                    return why
            s = S.get(rk(k, name))
            # SAHPRA 產品名就是本藥（COLCHICINE HOUDE 的成分全文只列 probenecid）時，成分全文不完整，不當成錯植的證據
            if s and s.get("_ing") and not s.get("_trunc") and not GROUP.search(s["_ing"]) and not any(mentions(s["_ing"], tm) for tm in terms) \
                    and not any(has(norm(s.get("name")), tm) for tm in terms):
                return f"SAHPRA 成分全文不含本藥（{s.get('name')}：{str(s.get('ingredients'))[:80]}），MPR 成分欄錯植"
            return None

        def apply_status(r):
            s = S.get(rk(r.get("license_id"), r.get("brand_name_en") or ""))
            if s:
                r["license_id"] = s["reg"]
                r.pop("status_unconfirmed", None)
                if s.get("status"):
                    r["status"], r["license_status"] = s["status"], "cancelled" if s["status"].lower().startswith("cancel") else "valid"
            elif not r.get("status") and r.get("license_status", "valid") == "valid":
                r["status_unconfirmed"] = True  # 只在 MPR 有、SAHPRA 匯出（含寫法統一）查不到：照用戶決定算有效，頁面加註
            return r

        def note_excluded(r, why):
            if rk(r.get("license_id")) not in {rk(e.get("license_id")) for e in excluded}:
                excluded.append({**r, "excluded_reason": why})

        if NO_REBUILD.match(inn) and inn not in ELEMENT_TERMS:
            recs = []
            for r in old:
                why = check(r.get("license_id"), r.get("brand_name_en") or "")
                if why:
                    note_excluded(r, why)
                else:
                    recs.append(apply_status(r))
            action, note = "clean_only", "單一元素／離子頁，不依成分重建"
        else:
            new = {}
            for k, s in S.items():  # 1) SAHPRA 全量依成分
                if any(has(s["_ing"], tm) for tm in terms):
                    st = s.get("status") or ""
                    new[k] = {"license_id": s["reg"], "brand_name_zh": tidy(s.get("name")), "brand_name_en": tidy(s.get("name")),
                              "ingredients": " ".join(str(s.get("ingredients") or "").split()), "indication": "",
                              "dosage_form": form_of(s.get("ingredients")), "manufacturer": s.get("applicant") or "",
                              "license_holder": s.get("applicant") or "", "approval_date": s.get("reg_date") or "", "expiry_date": "",
                              "kind": "combo" if n_ingredients(s.get("ingredients") or "") > 1 else "single",
                              "status": st, "license_status": "cancelled" if st.lower().startswith("cancel") else "valid",
                              "therapeutic_area": s.get("area") or "", "old_medicine": bool(s.get("old_medicine")),
                              "in_mpr": False, "source": SOURCE}
            for term in terms:  # 2) MPR 依成分：補產品名、劑型；補 SAHPRA 匯出沒有的號碼
                for x in mpr(term, sess):
                    ings = [i.get("name") or "" for i in x.get("ingredients") or []]
                    if not any(has(norm(i), tm) for i in ings for tm in terms):
                        continue
                    name = (x.get("name") or "").strip()
                    mr = manual(x.get("regno"), name)
                    k = rk(x.get("regno"), name)
                    if k in new:
                        if mr and mr.get("to"):  # 人工對照：產品名用 SAHPRA 的（MPR 品名是舊名或縮寫）
                            new[k].update({"dosage_form": x.get("dosage_form") or new[k]["dosage_form"], "in_mpr": True,
                                           "nappi_code": x.get("nappi_code") or ""})
                            continue
                        new[k].update({"brand_name_en": name or new[k]["brand_name_en"], "brand_name_zh": name or new[k]["brand_name_zh"],
                                       "dosage_form": x.get("dosage_form") or new[k]["dosage_form"], "in_mpr": True,
                                       "nappi_code": x.get("nappi_code") or ""})
                        continue
                    if mr and mr.get("to") and k in S:
                        name = tidy(S[k].get("name")) or name
                    rec = {"license_id": official(x.get("regno"), x.get("name") or ""), "brand_name_zh": name, "brand_name_en": name,
                           "ingredients": "; ".join(i.strip() for i in ings if i.strip()), "indication": "",
                           "dosage_form": x.get("dosage_form") or "", "manufacturer": "", "license_holder": "", "approval_date": "",
                           "expiry_date": "", "kind": "combo" if len([i for i in ings if i.strip()]) > 1 else "single",
                           "status": "", "license_status": "valid", "in_mpr": True, "nappi_code": x.get("nappi_code") or "",
                           "source": SOURCE}
                    why = check(x.get("regno"), x.get("name") or "") if mr else check(rec["license_id"])
                    nm = norm(name)
                    if not why and k not in S:  # SAHPRA 匯出查無此號：只能靠 MPR，成分欄要有產品名佐證
                        # 「公司名＋藥名」型的學名藥名稱（Medpro-Ciprofloxacin）含別的藥名 → 錯植；第一個字是品牌（Dantron），不算
                        other = [w for w in nm.split()[1:] if w in VOCAB and not any(w in tm or tm.split()[0] in w for tm in terms)]
                        named = any(tm.split()[0][:5] in nm for tm in terms)
                        if rec["kind"] == "single" and other and not named and not COMBO_MARK.search(name):
                            why = f"產品名是別的藥（{other[0]}），SAHPRA 匯出查無此號，MPR 成分欄錯植"
                    if why:
                        note_excluded(rec, why)
                        continue
                    s = S.get(k)
                    if s:  # SAHPRA 有這個號碼（成分全文寫法不同或被截斷）：狀態、申請者以 SAHPRA 為準
                        st = s.get("status") or ""
                        rec.update({"status": st, "license_status": "cancelled" if st.lower().startswith("cancel") else "valid",
                                    "manufacturer": s.get("applicant") or "", "license_holder": s.get("applicant") or "",
                                    "approval_date": s.get("reg_date") or "", "therapeutic_area": s.get("area") or "",
                                    "old_medicine": bool(s.get("old_medicine"))})
                    else:
                        rec["status_unconfirmed"] = True  # SAHPRA 匯出（含寫法統一）查不到：照用戶決定算有效，頁面加註
                    new[k] = rec
            for r in old:  # 原有紀錄被剔除的，記下原因
                why = check(r.get("license_id"), r.get("brand_name_en") or "")
                if why:
                    note_excluded(r, why)
            old_ok = {rk(r.get("license_id"), r.get("brand_name_en") or "") for r in old
                      if not check(r.get("license_id"), r.get("brand_name_en") or "") and rk(r.get("license_id"), r.get("brand_name_en") or "") in S}
            cover = len(old_ok & set(new)) / max(1, len(old_ok))
            if not new or (old_ok and cover < 0.5):
                recs = [apply_status(r) for r in old if not check(r.get("license_id"), r.get("brand_name_en") or "")]
                action, note = "kept_old", f"新結果只涵蓋原有紀錄 {cover:.0%}（新 {len(new)} 筆），疑似成分名對錯，保留原紀錄（只清理）"
            else:
                recs = sorted(new.values(), key=record_order)
                action, note = "rebuilt", f"原有紀錄涵蓋 {cover:.0%}"
        exrows += [tuple(" ".join(str(x).split()) for x in (pg, e.get("license_id"), e.get("brand_name_en"), str(e.get("ingredients"))[:120],
                                                            e["excluded_reason"])) for e in excluded]
        nv = sum(1 for r in recs if r.get("license_status", "valid") == "valid")
        rows.append((pg, inn, "|".join(terms), action, len(old), old_valid, len(recs), nv, len(recs) - nv, len(excluded), note))
        if not dry:
            t.update({"records": recs, "total_matches": len({rk(r['license_id']) for r in recs}), "found": bool(recs),
                      "query_terms": terms, "excluded_records": excluded, "rebuilt": action})
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("\n".join("\t".join(map(str, r)) for r in rows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".excluded.tsv").write_text("\n".join("\t".join(r) for r in exrows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".alias.tsv").write_text("MPR 號碼\tSAHPRA 號碼\t結果\n" + "\n".join("\t".join(" ".join(str(x).split()) for x in r) for r in alias_rep) + "\n", encoding="utf-8")
    c = Counter(r[3] for r in rows[1:])
    print(f"號碼寫法統一 {len(ALIAS)} 個 MPR 號碼對到 SAHPRA；{len(rows) - 1} 個證據包：{dict(c)}；剔除 {sum(int(r[9]) for r in rows[1:])} 列")


if __name__ == "__main__":
    main(sys.argv[1:])
