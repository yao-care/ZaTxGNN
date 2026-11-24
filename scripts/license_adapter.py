"""ZA（SAHPRA medapps）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：SAHPRA medapps 匯出（免登入、免 token）：
https://medapps.sahpra.org.za:6006/DateSearch/ExportData?s1=1900/01/01 00:00:00&s2=<今年底>（依註冊日期區間；xlsx）。
欄位：Applicant Name、Product Name、API、Registration Number（＝證據包 license_id，例 41/2.5/0460）、Application Number、
Registration Date、Expiry Date、Ingredients（成分全文，例「EACH TABLET CONTAINS METFORMIN HYDROCHLORIDE 500,0 mg」）、
Therapeutic Area、Status（Registered／Canceled／Old Medicine，原檔另有拼錯的 Registrered）。
站上原本的來源是 MPR 價格登錄（status 空白）；這裡改用 SAHPRA 官方註冊資料。
寫回：status＝Status 原文（拼錯的 Registrered 照原文保留）；license_status：Canceled→cancelled，其他→valid
（reviewer 的註銷字樣是 cancel，Canceled 少一個 l 也會中；另寫 license_status 以免依賴拼字）。新檔沒有的註冊號保留原狀態。
2026-11-06（用戶決定）：每週更新也做號碼寫法統一——證據包裡標 status_unconfirmed（只在 MPR 有）的號碼，用依成分重建的同一套規則
（scripts/rebuild_licenses_by_ingredient.py 的 _sig／same_product／build_alias：SAHPRA 只有一個號碼化成同一序列、品名或成分吻合、一對一）
對 SAHPRA；對到的號碼改成 SAHPRA 匯出的寫法、取 SAHPRA 狀態。狀態有變的藥，許可證表依重建的排序重排（sync_tables）。
2026-11-06（用戶決定）：對回 SAHPRA 後，同一個藥的證據包裡若本來就有那個 SAHPRA 號碼，兩筆當場合併成一筆（merge_records），
規則用依成分重建同一支程式的 merge_same_number（保留哪一筆、產品名／劑型／in_mpr／nappi 怎麼取都跟重建以號碼為鍵合併的做法相同）；
只合併同一個藥裡、號碼正規化後相同的紀錄（2026-11-06 用戶決定：clean_only／kept_old 的證據包也合併，重建同步改）。
合併過的藥也走 sync_tables 重排許可證表，張數、狀態列照現有流程重算。
2026-11-05：raw 檔另存產品名、成分全文、申請者、藥理分類、註冊日期（給 scripts/rebuild_licenses_by_ingredient.py 依成分重建用）；
舊制藥品（Registration Number 欄是「Old Medicine」）改用 Application Number（例 G2963）當號碼收進來，狀態 Old Medicine＝有效。
2026-11-17（用戶要求查證 791 張只在 MPR 有、SAHPRA 查不到的號碼）：fetch() 另下載衛生部現行一期 MPR（Database of Medicine Prices，
https://www.health.gov.za/nhi-pee/ 上日期最新的 xlsx）。SAHPRA 匯出（含寫法統一 R1–R10）沒有、而現行 MPR 也不列（號碼不在檔內），
或現行 MPR 該號每一列的 Status 都是 Discontinued（原檔另有拼錯的 Discountinued）的號碼，preprocess 標 license_status＝cancelled
＋mpr_not_current（第一次發現日）＋mpr_status（"discontinued"／"not listed"）＋mpr_edition（MPR 那一期的日期），status 改成
「Not on SAHPRA register; discontinued in MPR (Database of Medicine Prices, <日期>)」或「Not on SAHPRA register or current MPR (…)」
（頁面許可證表照這個寫，不寫 SAHPRA 撤銷；原 status 存 status_before_mpr_not_current），拿掉 status_unconfirmed；之後 SAHPRA 查得到
或 MPR 又列為現行就還原。MPR 下載失敗、少於 MPR_MIN 個號碼、或 SAHPRA 匯出不是這次下載的，都不做新判定。
confirmed_absent() 讓排程把這些列成「主管機關現行清單確認已不列」。現行 MPR 仍列（沒有 Discontinued）的號碼照舊算有效、標 not confirmed：
MPR 是價格登錄，不是註冊登錄（2026-10-01 那期仍列 2010 年就撤市的 sibutramine 產品、價格照年度調整），不能當成仍註冊的證據，也不能推定撤銷。
2026-11-18（用戶決定）：MPR 仍列、SAHPRA 不列的號碼裡，有官方撤市依據的收在 ZA_WITHDRAWN（人工確認表，每筆附依據網址、日期、摘要）：
preprocess 對表內號碼（SAHPRA 匯出含寫法統一查不到時）標 license_status＝cancelled＋za_withdrawn（第一次標記日）＋za_withdrawn_basis，
status 改「Withdrawn from the South African market (<年>; <依據>); not on SAHPRA register」（原值存 status_before_za_withdrawn），拿掉
status_unconfirmed；頁面許可證表寫「Withdrawn from the South African market (<年>); not on SAHPRA register」，不寫 SAHPRA 撤銷
（依據是撤市，沒有取得 SAHPRA／MCC 撤銷註冊的官方文件）。表不依賴下載，依成分重建把號碼重設成 status_unconfirmed 後，下一次 preprocess 會再標回；
SAHPRA 匯出查得到就不套（照 SAHPRA 狀態）。confirmed_absent() 對表內號碼回真。
本機（雲端連不到 medapps 6006 埠）試跑：環境變數 ZA_SAHPRA_RAW=<sahpra_status.json> 讀已下載的 SAHPRA 匯出，MPR 照常下載。
"""
import importlib.util
import io
import json
import re
import time
from pathlib import Path

import openpyxl
import requests

RAW_FILE = "raw/sahpra_status.json"
# 匯出依註冊日期篩選：沒有註冊日期的品項不在匯出檔，2026-10-30 實測證據包 1,148 張只對得上 76.3%。
# 涵蓋門檻設 70%（低於代表來源真的變了），其餘保留原狀態。
COVER_MIN = 0.70
URL = "https://medapps.sahpra.org.za:6006/DateSearch/ExportData"


def download():
    end = time.strftime("%Y") + "/12/31 00:00:00"
    for attempt in range(4):
        try:
            r = requests.get(URL, params={"s1": "1900/01/01 00:00:00", "s2": end}, timeout=600)
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("回傳的不是 xlsx")
            return r.content
        except Exception:
            if attempt == 3:
                raise
            time.sleep(20 * (attempt + 1))


def parse(content):
    ws = openpyxl.load_workbook(io.BytesIO(content), read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    if "Registration Number" not in head or "Status" not in head:
        raise RuntimeError(f"欄位改變：{head}")
    out = []
    for row in rows:
        rec = dict(zip(head, row))
        g = lambda k: str(rec.get(k) or "").strip()  # noqa: E731
        k = g("Registration Number")
        old = k == "Old Medicine"
        if old:
            k = g("Application Number")  # 舊制藥品沒有註冊號，用申請號（例 G2963、F1016）
        if k:
            out.append({"reg": k, "status": g("Status"), "name": g("Product Name"), "ingredients": g("Ingredients"),
                        "applicant": g("Applicant Name"), "area": g("Therapeutic Area"), "reg_date": g("Registration Date"),
                        "old_medicine": old})
    return out


MPR_PAGE = "https://www.health.gov.za/nhi-pee/"
MPR_MIN = 8000          # 現行 MPR 不重複註冊號少於這個數＝下載或格式有問題，不判定（2026-10-01 那期 13,734 個產品列）
MPR_ROWS: dict = {}     # {號碼 key: [該號每一列的 Status]}（fetch() 填；空的就不判定）
MPR_INFO: dict = {}     # {"url":…, "date": "YYYY-MM-DD"}
_MON = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
_DISC = re.compile(r"disc\w*tinu", re.I)


def _mpr_links(html):
    """nhi-pee 頁上每一期 MPR（Database of Medicine Prices）的 xlsx 連結 → [(日期, 網址)]，日期取自檔名"""
    out = []
    for u in set(re.findall(r'href="([^"]*Database[_-]?Of[_-]?Medicine[_-]?Prices[^"]*\.xlsx)"', html, re.I)):
        m = re.search(r"(\d{1,2})[_ -]*([A-Za-z]{3})[A-Za-z]*[_ -]*(\d{4})", u.rsplit("/", 1)[-1])
        if m and m.group(2).lower() in _MON:
            out.append((f"{m.group(3)}-{_MON[m.group(2).lower()]:02d}-{int(m.group(1)):02d}", requests.compat.urljoin(MPR_PAGE, u)))
    return sorted(out)


def _fetch_mpr():
    """現行一期 MPR：{號碼 key: [Status…]}；任何失敗回 {}（就不做「不在 SAHPRA／MPR 現行」判定）"""
    MPR_ROWS.clear(); MPR_INFO.clear()
    try:
        hd = {"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"}
        links = _mpr_links(requests.get(MPR_PAGE, timeout=120, headers=hd).text)
        date, url = links[-1]
        r = requests.get(url, timeout=600, headers=hd); r.raise_for_status()
        if r.content[:2] != b"PK":
            raise RuntimeError("回傳的不是 xlsx")
        rb = _load("rebuild_licenses_by_ingredient", ROOT / "scripts/rebuild_licenses_by_ingredient.py")
        rows = {}
        for ws in openpyxl.load_workbook(io.BytesIO(r.content), read_only=True).worksheets:
            ws.reset_dimensions()
            started = False
            for row in ws.iter_rows(values_only=True):
                row = list(row) + [None] * 22
                if not started:  # 表頭那一列：第 3 欄是「MCC\SAHPRA Medicine Registration No」
                    started = bool(row[2]) and "reg" in str(row[2]).lower() and "status" in [str(x or "").strip().lower() for x in row]
                    continue
                if row[2]:  # 第 3 欄註冊號、第 20 欄 Status；成分續行（註冊號空白）不算
                    rows.setdefault(rb.key(row[2]), []).append(str(row[19] or "").strip())
        if len(rows) < MPR_MIN:
            raise RuntimeError(f"只解析出 {len(rows)} 個註冊號")
        MPR_ROWS.update(rows); MPR_INFO.update(url=url, date=date)
    except Exception as e:
        print(f"MPR（Database of Medicine Prices）下載失敗，不判定 SAHPRA 與現行 MPR 都不列的號碼：{e}")


_FRESH = False  # 這次的 SAHPRA 匯出是 fetch() 拿到的（status_index 收到的就是它）才判定


def fetch():
    import os
    global _FRESH
    if os.environ.get("ZA_SAHPRA_RAW"):  # 本機試跑：雲端連不到 medapps 6006 埠，讀已下載的匯出
        new = json.loads(Path(os.environ["ZA_SAHPRA_RAW"]).read_text(encoding="utf-8"))
    else:
        new = parse(download())
    _fetch_mpr()
    _FRESH = True
    return new


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


ROOT = Path(__file__).resolve().parents[1]
# 每週更新允許改的非表格行：許可證表下程式產生的「Showing N of M」（重排後總數變了要跟著改）與它前後的空行
# 2026-11-24 第四輪：整頁沒有市場段落的公開頁由 sync_license_pages.add_section 補段落，放行補的標題行與程式區塊標記
PAGE_NOTE = r"^(Showing \d+ of \d+ registrations \(valid registrations first\)\.|## South Africa Market Information|<!-- licenses:(begin|end) -->)$"
_ALIAS = {}  # {MPR 號碼 key: SAHPRA 匯出寫法}（status_index 時依新資料建）
_KEY = None
_RB = _S = _RK = None  # 依成分重建的程式、新資料的 SAHPRA 全量、重建的 rk（合併同號紀錄用）


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def _build_alias(new):
    """號碼寫法統一：規則與依成分重建相同（用同一支程式的 build_alias）；MPR 列取自證據包紀錄與 data/raw/mpr_by_ingredient 快取"""
    rb = _load("rebuild_licenses_by_ingredient", ROOT / "scripts/rebuild_licenses_by_ingredient.py")
    S = rb.load_sahpra(new)
    rows = []
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        t = json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}
        for r in (t.get("records") or []) + (t.get("excluded_records") or []):
            # 2026-11-17：SAHPRA 自己以前匯出的號碼、現在匯出改了寫法的（例 590209＝59/8.2/0209）也收進來比對（R8）
            if r.get("in_mpr") or not r.get("status") or rb.key(r.get("license_id")) not in S:
                rows.append((str(r.get("license_id") or ""), r.get("brand_name_en") or "", str(r.get("ingredients") or "").split(";")))
    for f in sorted((ROOT / "data/raw/mpr_by_ingredient").glob("*.json")):
        for x in json.loads(f.read_text(encoding="utf-8")):
            rows.append((str(x.get("regno") or ""), x.get("name") or "", [i.get("name") or "" for i in x.get("ingredients") or []]))
    alias, _ = rb.build_alias(S, rows)
    global _RB, _S, _RK
    _RB, _S, _RK = rb, S, rb.make_rk(S, alias)[0]
    return {a: S[k]["reg"] for a, (k, _) in alias.items()}, rb.key


def status_index(new):
    global _ALIAS, _KEY
    _ALIAS, _KEY = _build_alias(new)
    idx = {}
    for r in new:
        # 同一註冊號多列時，任一列不是 Canceled 即視為仍註冊
        if r["status"] and (r["reg"] not in idx or idx[r["reg"]] == "Canceled"):
            idx[r["reg"]] = r["status"]
    return idx


# 2026-11-18 人工確認表：MPR 仍列、SAHPRA 不列、有官方撤市依據的號碼（號碼照證據包寫法）。找不到官方依據的（Ciplatrim 10／15
# 41/11.3/0312–0313、Leantil 10／15 41/11.3/0180、0153：MCC 只說會對學名藥「take appropriate action」，沒有找到後續官方文件）不收。
_SIB = {"year": 2010, "date": "2010-10-13", "authority": "MCC",
        "url": "https://www.sanews.gov.za/south-africa/ectiva-reductil-sa-shelves",
        "summary": "SAnews (GCIS), 13 Oct 2010: Abbott Laboratories agreed with the Medicines Control Council to withdraw Ectiva and "
                   "Reductil (sibutramine) from the South African market after the SCOUT cardiovascular outcome results.",
        "also": "https://www.bizcommunity.com/Article/196/398/53194.html (Abbott notice: voluntary withdrawal of Reductil after discussions with the MCC)"}
_DPP = {"year": 2011, "date": "2011-05-03", "authority": "MCC",
        "url": "https://www.gov.za/news/media-statements/withdrawal-dextropropoxyphene-containing-medicines-south-african-market-03",
        "summary": "MCC media statement, 3 May 2011: the MCC resolved at its 14-15 April 2011 meeting to withdraw all dextropropoxyphene-"
                   "containing medicines (named: Distalgesic, Doloxene, Doloxene Co-65, Doxyfene, Lentogesic, Synap Forte) from the "
                   "South African market due to cardiac safety risks, with a three-month transition period."}
ZA_WITHDRAWN = {
    "33/11.3/0025": dict(_SIB, product="Reductil 10"),
    "33/11.3/0026": dict(_SIB, product="Reductil 15"),
    "33/11.3/0027": dict(_SIB, product="Ectiva 10 mg"),
    "33/11.3/0028": dict(_SIB, product="Ectiva 15 mg"),
    "E/2.8/0090": dict(_DPP, product="Distalgesic"),
    "B0586 (ACT 101)": dict(_DPP, product="Doloxene Plain"),
    "B0584 (ACT 101)": dict(_DPP, product="Doloxene Co-65"),
    "B1334(ACT 101/1965) OM*": dict(_DPP, product="Lentogesic (paracetamol + dextropropoxyphene)"),
}


def _wd(lid):
    """人工確認表的那一筆（SAHPRA 匯出含寫法統一查得到的不套）；不在表內回 None"""
    lid = str(lid or "").strip()
    hit = ZA_WITHDRAWN.get(lid)
    if hit is None and _KEY:
        k = _KEY(lid)
        hit = next((v for x, v in ZA_WITHDRAWN.items() if _KEY(x) == k), None)
    if hit is None:
        return None
    if _S is not None and _KEY and (_KEY(lid) in _S or _KEY(lid) in _ALIAS):
        return None
    return hit


def _wd_status_text(w):
    return f"Withdrawn from the South African market ({w['year']}; {w['authority']}, {w['url']}); not on SAHPRA register"


def mpr_state(lid):
    """SAHPRA 匯出（含寫法統一）沒有的號碼在現行 MPR 的情形："discontinued"（每一列都是 Discontinued）、"not listed"（不在檔內）、
    "listed"（仍列為現行）；SAHPRA 有、或資料不齊（MPR／SAHPRA 沒下載成功）回 None"""
    if not (_FRESH and MPR_ROWS and _S is not None and _KEY):
        return None
    k = _KEY(lid)
    if k in _S or k in _ALIAS:
        return None
    st = MPR_ROWS.get(k)
    if st is None:
        return "not listed"
    return "discontinued" if all(_DISC.search(x) for x in st) else "listed"


def confirmed_absent(lid):
    """給 license_refresh：SAHPRA 匯出沒有、現行 MPR 也不列為現行（不在檔內或已 Discontinued）＝確認不是現行註冊"""
    return _wd(lid) is not None or mpr_state(lid) in ("discontinued", "not listed")


def _mpr_status_text(state):
    d = MPR_INFO.get("date", "")
    return (f"Not on SAHPRA register; discontinued in MPR (Database of Medicine Prices, {d})" if state == "discontinued"
            else f"Not on SAHPRA register or current MPR (Database of Medicine Prices, {d})")


def preprocess(bundle):
    """SAHPRA 匯出與現行 MPR 都不列為現行的號碼標 cancelled（mpr_not_current＝第一次發現日）；又列為現行（或 SAHPRA 查得到）就還原。有改回 True"""
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:  # 人工確認表（不依賴下載）
        w = _wd(r.get("license_id"))
        if w is None:
            if r.get("za_withdrawn"):  # 移出人工確認表或 SAHPRA 查得到了：回到只在 MPR 有（SAHPRA 有的由 update() 接著改成 SAHPRA 狀態）
                r["status"] = r.pop("status_before_za_withdrawn", "")
                for x in ("za_withdrawn", "za_withdrawn_basis"):
                    r.pop(x, None)
                r["license_status"] = "valid"
                r["status_unconfirmed"] = True
                ch = True
            continue
        txt = _wd_status_text(w)
        if not r.get("za_withdrawn"):
            r["za_withdrawn"] = today
            r["status_before_za_withdrawn"] = r.get("status") or ""
        if r.get("status") != txt or r.get("license_status") != "cancelled" or r.get("za_withdrawn_basis") != w or "status_unconfirmed" in r:
            r.update(status=txt, license_status="cancelled", za_withdrawn_basis=w)
            r.pop("status_unconfirmed", None)
            ch = True
    if not (_FRESH and MPR_ROWS and _S is not None):
        return ch
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if r.get("za_withdrawn") and _wd(lid) is not None:
            continue
        if not (r.get("status_unconfirmed") or r.get("mpr_not_current")):
            continue  # 只看只在 MPR 有的號碼（SAHPRA 有的照 SAHPRA 狀態）
        state = mpr_state(lid)
        if state in ("discontinued", "not listed"):
            txt = _mpr_status_text(state)
            if not r.get("mpr_not_current"):
                r["mpr_not_current"] = today
                r["status_before_mpr_not_current"] = r.get("status") or ""
            if r.get("status") != txt or r.get("license_status") != "cancelled" or r.get("mpr_status") != state:
                r.update(status=txt, license_status="cancelled", mpr_status=state, mpr_edition=MPR_INFO.get("date"))
                r.pop("status_unconfirmed", None)
                ch = True
        elif r.get("mpr_not_current") and (state == "listed" or _KEY(lid) in _S or _KEY(lid) in _ALIAS):
            # MPR 又列為現行：回到「只在 MPR 有、狀態未經 SAHPRA 確認」；SAHPRA 查得到的由 update() 接著改成 SAHPRA 狀態
            r["status"] = r.pop("status_before_mpr_not_current", "")
            for x in ("mpr_not_current", "mpr_status", "mpr_edition"):
                r.pop(x, None)
            r["license_status"] = "valid"
            r["status_unconfirmed"] = True
            ch = True
    return ch


def record_id(rec):
    """證據包一筆的號碼；SAHPRA 匯出沒有的號碼（多是只在 MPR 有、status_unconfirmed 的），照寫法統一規則換成 SAHPRA 匯出的寫法"""
    k = str(rec.get("license_id") or "").strip()
    if _ALIAS:  # _ALIAS 只收 SAHPRA 匯出沒有的號碼，SAHPRA 原有的號碼不受影響
        return _ALIAS.get(_KEY(k), k)
    return k


def update(rec, new):
    cls = "cancelled" if new.lower().startswith("cancel") else "valid"
    tgt = record_id(rec)
    moved = tgt != str(rec.get("license_id") or "").strip()
    if moved:  # 寫法統一後對到 SAHPRA：號碼改成 SAHPRA 的寫法（頁面許可證表由 sync_tables 跟著改）
        rec["license_id"] = tgt
    if rec.get("status") == new and rec.get("license_status") == cls and not moved:
        return False
    if not rec.get("status") and cls == "valid" and rec.get("license_status") in (None, "valid") and not rec.get("status_unconfirmed"):
        return False  # 原本空白（reviewer 視為有效）、現在仍註冊：意義不變
    rec["status"], rec["license_status"] = new, cls
    rec.pop("status_unconfirmed", None)  # SAHPRA 查得到了：不再是「狀態未經 SAHPRA 確認」
    return True


def merge_records(b):
    """寫法統一後同號的紀錄合併成一筆（license_refresh 在逐筆更新狀態前呼叫；合併後那一筆接著照常更新狀態）。
    規則見 scripts/rebuild_licenses_by_ingredient.py 的 merge_same_number。回傳 ["<SAHPRA 號碼> 合併同號紀錄 N 筆成 1 筆"]"""
    if _RB is None:
        return []
    return [f"{reg} 合併同號紀錄 {n} 筆成 1 筆" for reg, n in _RB.merge_same_number(b.get("tfda") or {}, _S, _RK)]


def sync_tables(site_root, bundles):
    """狀態有變的藥：許可證表依重建的排序重排、號碼照證據包、「Showing N of M」跟著改（scripts/sync_license_pages.py 的 resync_tables）"""
    slp = _load("sync_license_pages", Path(site_root) / "scripts/sync_license_pages.py")
    # 2026-11-17：preprocess 標的「SAHPRA 與現行 MPR 都不列為現行」不在 license_refresh 傳來的清單裡（它只傳狀態更新與合併的藥），
    # 而概覽同步把表格狀態格寫成通用的 Cancelled；有這種紀錄的藥一律重排，狀態格照 sync_license_pages.label 寫 MPR 的情形
    extra = [f.parent.name for f in sorted((Path(site_root) / "data/bundles").glob("*/drug_bundle.json"))
             if '"mpr_not_current"' in (t := f.read_text(encoding="utf-8")) or '"za_withdrawn"' in t]
    return slp.resync_tables(sorted(set(bundles) | set(extra)))


if __name__ == "__main__":
    # 單獨下載（依成分重建的 workflow 用）：python3 scripts/license_adapter.py data/raw/sahpra_status.json
    import json
    import sys
    from pathlib import Path
    dst = Path(sys.argv[1])
    old = json.loads(dst.read_text(encoding="utf-8")) if dst.exists() else None
    new = fetch()
    prob = validate(new, old)
    if prob:
        sys.exit("SAHPRA 匯出檢查沒過：" + "；".join(prob))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(new, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"SAHPRA 匯出 {len(new)} 筆 → {dst}")
