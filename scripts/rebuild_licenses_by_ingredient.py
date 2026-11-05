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
# SAHPRA 匯出沒有的號碼、但人工核對是 MPR 成分欄錯植的產品（(號碼, 本藥成分名) → 理由）
# 「*X」＝這個產品的真正成分是 X：本藥不是 X 就是錯植
MISMATCH = {
    ("A.682", "*pyrimethamine"): "Daraprim 是 pyrimethamine 產品，MPR 成分欄另列 clindamycin 屬錯植",
    ("P/7.1.4/281", "*glyceryl trinitrate"): "Nitrolingual 是 glyceryl trinitrate 舌下噴劑，MPR 成分欄另列 paracetamol、chlorphenamine、calcium ascorbate 等屬錯植",
    ("T/2.2/207", "*midazolam"): "Dormicum 是 midazolam 產品，MPR 成分欄另列 naproxen 屬錯植",
    ("L/2.5/188", "*valproic acid"): "Epilim EC 500 是 valproate 產品，MPR 成分欄另列 promethazine、ephedrine 等屬錯植",
    ("D/26/174", "*bleomycin"): "Blenoxane 是 bleomycin 產品，MPR 成分欄另列 promethazine 屬錯植",
}


def norm(x):
    x = unicodedata.normalize("NFKD", str(x or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", x).split())


def key(k):
    """號碼正規化：去空白、去「(ACT 101/1965)」「(OM)」註記"""
    k = re.sub(r"\((ACT|OM)[^)]*\)", "", str(k or ""), flags=re.I)
    return re.sub(r"\s+", "", k).upper()


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


def derive_terms(inn, recs):
    base = base_name(inn)
    terms = {base} | set(SYN.get(base, [])) | set(SYN.get(inn, []))
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


def load_sahpra():
    by = {}
    for r in json.loads(SAHPRA.read_text(encoding="utf-8")):
        if str(r.get("ingredients") or "").strip().lower() in ("none", "null", "n/a"):
            r = {**r, "ingredients": ""}
        k = key(r["reg"])
        cur = by.get(k)
        if cur is None:
            by[k] = {**r, "_ing": norm(r.get("ingredients")), "_rows": 1, "_trunc": truncated(r.get("ingredients"))}
        else:
            cur["_rows"] += 1
            cur["_ing"] += " | " + norm(r.get("ingredients"))
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
        terms = ELEMENT_TERMS.get(inn) or derive_terms(inn, old)
        excluded = []

        def check(k):
            """回傳剔除理由或 None"""
            if not is_reg(k):
                return "不是註冊號（ITN 調配營養液的豁免條款、IMPORT PERMIT 等）"
            s = S.get(key(k))
            if s and s.get("_ing") and not s.get("_trunc") and not GROUP.search(s["_ing"]) and not any(mentions(s["_ing"], tm) for tm in terms):
                return f"SAHPRA 成分全文不含本藥（{s.get('name')}：{str(s.get('ingredients'))[:80]}），MPR 成分欄錯植"
            for (mk, tm), why in MISMATCH.items():
                if key(mk) == key(k) and (tm[1:] not in terms if tm.startswith("*") else tm in terms):
                    return why
            return None

        def apply_status(r):
            s = S.get(key(r.get("license_id")))
            if s and s.get("status"):
                r["status"], r["license_status"] = s["status"], "cancelled" if s["status"].lower().startswith("cancel") else "valid"
            return r

        def note_excluded(r, why):
            if key(r.get("license_id")) not in {key(e.get("license_id")) for e in excluded}:
                excluded.append({**r, "excluded_reason": why})

        if NO_REBUILD.match(inn) and inn not in ELEMENT_TERMS:
            recs = []
            for r in old:
                why = check(r.get("license_id"))
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
                    k = key(x.get("regno"))
                    name = (x.get("name") or "").strip()
                    if k in new:
                        new[k].update({"brand_name_en": name or new[k]["brand_name_en"], "brand_name_zh": name or new[k]["brand_name_zh"],
                                       "dosage_form": x.get("dosage_form") or new[k]["dosage_form"], "in_mpr": True,
                                       "nappi_code": x.get("nappi_code") or ""})
                        continue
                    rec = {"license_id": str(x.get("regno") or "").strip(), "brand_name_zh": name, "brand_name_en": name,
                           "ingredients": "; ".join(i.strip() for i in ings if i.strip()), "indication": "",
                           "dosage_form": x.get("dosage_form") or "", "manufacturer": "", "license_holder": "", "approval_date": "",
                           "expiry_date": "", "kind": "combo" if len([i for i in ings if i.strip()]) > 1 else "single",
                           "status": "", "license_status": "valid", "in_mpr": True, "nappi_code": x.get("nappi_code") or "",
                           "source": SOURCE}
                    why = check(rec["license_id"])
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
                    new[k] = rec
            for r in old:  # 原有紀錄被剔除的，記下原因
                why = check(r.get("license_id"))
                if why:
                    note_excluded(r, why)
            old_ok = {key(r.get("license_id")) for r in old if not check(r.get("license_id")) and key(r.get("license_id")) in S}
            cover = len(old_ok & set(new)) / max(1, len(old_ok))
            if not new or (old_ok and cover < 0.5):
                recs = [apply_status(r) for r in old if not check(r.get("license_id"))]
                action, note = "kept_old", f"新結果只涵蓋原有紀錄 {cover:.0%}（新 {len(new)} 筆），疑似成分名對錯，保留原紀錄（只清理）"
            else:
                recs = sorted(new.values(), key=lambda r: (r["license_status"] != "valid", not r.get("in_mpr"), r["kind"] != "single",
                                                           r["license_id"]))
                action, note = "rebuilt", f"原有紀錄涵蓋 {cover:.0%}"
        exrows += [tuple(" ".join(str(x).split()) for x in (pg, e.get("license_id"), e.get("brand_name_en"), str(e.get("ingredients"))[:120],
                                                            e["excluded_reason"])) for e in excluded]
        nv = sum(1 for r in recs if r.get("license_status", "valid") == "valid")
        rows.append((pg, inn, "|".join(terms), action, len(old), old_valid, len(recs), nv, len(recs) - nv, len(excluded), note))
        if not dry:
            t.update({"records": recs, "total_matches": len({key(r['license_id']) for r in recs}), "found": bool(recs),
                      "query_terms": terms, "excluded_records": excluded, "rebuilt": action})
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("\n".join("\t".join(map(str, r)) for r in rows) + "\n", encoding="utf-8")
        Path(rep).with_suffix(".excluded.tsv").write_text("\n".join("\t".join(r) for r in exrows) + "\n", encoding="utf-8")
    c = Counter(r[3] for r in rows[1:])
    print(f"{len(rows) - 1} 個證據包：{dict(c)}；剔除 {sum(int(r[9]) for r in rows[1:])} 列")


if __name__ == "__main__":
    main(sys.argv[1:])
