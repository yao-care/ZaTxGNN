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
2026-11-05：raw 檔另存產品名、成分全文、申請者、藥理分類、註冊日期（給 scripts/rebuild_licenses_by_ingredient.py 依成分重建用）；
舊制藥品（Registration Number 欄是「Old Medicine」）改用 Application Number（例 G2963）當號碼收進來，狀態 Old Medicine＝有效。
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


def fetch():
    return parse(download())


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


ROOT = Path(__file__).resolve().parents[1]
# 每週更新允許改的非表格行：許可證表下程式產生的「Showing N of M」（重排後總數變了要跟著改）與它前後的空行
PAGE_NOTE = r"^Showing \d+ of \d+ registrations \(valid registrations first\)\.$"
_ALIAS = {}  # {MPR 號碼 key: SAHPRA 匯出寫法}（status_index 時依新資料建）
_KEY = None


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
            if r.get("in_mpr") or not r.get("status"):
                rows.append((str(r.get("license_id") or ""), r.get("brand_name_en") or "", str(r.get("ingredients") or "").split(";")))
    for f in sorted((ROOT / "data/raw/mpr_by_ingredient").glob("*.json")):
        for x in json.loads(f.read_text(encoding="utf-8")):
            rows.append((str(x.get("regno") or ""), x.get("name") or "", [i.get("name") or "" for i in x.get("ingredients") or []]))
    alias, _ = rb.build_alias(S, rows)
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


def record_id(rec):
    """證據包一筆的號碼；只在 MPR 有（status_unconfirmed）的，照寫法統一規則換成 SAHPRA 匯出的寫法"""
    k = str(rec.get("license_id") or "").strip()
    if rec.get("status_unconfirmed") and _ALIAS:
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


def sync_tables(site_root, bundles):
    """狀態有變的藥：許可證表依重建的排序重排、號碼照證據包、「Showing N of M」跟著改（scripts/sync_license_pages.py 的 resync_tables）"""
    slp = _load("sync_license_pages", Path(site_root) / "scripts/sync_license_pages.py")
    return slp.resync_tables(bundles)


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
