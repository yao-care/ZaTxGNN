"""ZA（SAHPRA medapps）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：SAHPRA medapps 匯出（免登入、免 token）：
https://medapps.sahpra.org.za:6006/DateSearch/ExportData?s1=1900/01/01 00:00:00&s2=<今年底>（依註冊日期區間；xlsx）。
欄位：Registration Number（＝證據包 license_id，例 41/2.5/0460）、Status（Registered／Canceled／Old Medicine，原檔另有拼錯的 Registrered）。
站上原本的來源是 MPR 價格登錄（status 空白）；這裡改用 SAHPRA 官方註冊資料。
寫回：status＝Status 原文（拼錯的 Registrered 照原文保留）；license_status：Canceled→cancelled，其他→valid
（reviewer 的註銷字樣是 cancel，Canceled 少一個 l 也會中；另寫 license_status 以免依賴拼字）。新檔沒有的註冊號保留原狀態。
"""
import io
import time

import openpyxl
import requests

RAW_FILE = "raw/sahpra_status.json"
# 匯出依註冊日期篩選：舊制藥品（Old Medicine，代碼如 G1831、C795 (OM)）沒有註冊號、沒有註冊日期的品項都不在匯出檔，
# 2026-10-30 實測證據包 1,148 張只對得上 76.3%。涵蓋門檻設 70%（低於代表來源真的變了），其餘保留原狀態。
COVER_MIN = 0.70


def fetch():
    end = time.strftime("%Y") + "/12/31 00:00:00"
    url = "https://medapps.sahpra.org.za:6006/DateSearch/ExportData"
    for attempt in range(4):
        try:
            r = requests.get(url, params={"s1": "1900/01/01 00:00:00", "s2": end}, timeout=600)
            r.raise_for_status()
            if r.content[:2] != b"PK":
                raise RuntimeError("回傳的不是 xlsx")
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(20 * (attempt + 1))
    ws = openpyxl.load_workbook(io.BytesIO(r.content), read_only=True).active
    ws.reset_dimensions()
    rows = ws.iter_rows(values_only=True)
    head = [str(x or "").strip() for x in next(rows)]
    if "Registration Number" not in head or "Status" not in head:
        raise RuntimeError(f"欄位改變：{head}")
    out = []
    for row in rows:
        rec = dict(zip(head, row))
        k = str(rec.get("Registration Number") or "").strip()
        if k and k != "Old Medicine":
            out.append({"reg": k, "status": str(rec.get("Status") or "").strip()})
    return out


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    idx = {}
    for r in new:
        # 同一註冊號多列時，任一列不是 Canceled 即視為仍註冊
        if r["status"] and (r["reg"] not in idx or idx[r["reg"]] == "Canceled"):
            idx[r["reg"]] = r["status"]
    return idx


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    cls = "cancelled" if new.lower().startswith("cancel") else "valid"
    if rec.get("status") == new and rec.get("license_status") == cls:
        return False
    if not rec.get("status") and cls == "valid" and rec.get("license_status") in (None, "valid"):
        return False  # 原本空白（reviewer 視為有效）、現在仍註冊：意義不變
    rec["status"], rec["license_status"] = new, cls
    return True
