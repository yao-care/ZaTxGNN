"""本站（ZaTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是 SAHPRA 註冊（medapps 匯出），另以 MPR 價格登錄補 SAHPRA 匯出查不到的有效註冊（狀態加註「status not confirmed by SAHPRA」）。
"""
import gzip
import importlib.util
import json
import re
from pathlib import Path

SITE = "ZaTxGNN"
CODE = "za"
BUNDLE_KEY = "tfda"  # 證據包裡本站市場資料的鍵（收集器沿用的欄位名）

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["Evidence Level"]          # Quick Overview 與其他預測表的證據等級欄名
HEADER_LABEL = r"Evidence Level"           # 頁首「Evidence Level: **Lx**」
WITHDRAWN = r"Withdrawn\b"                 # 重審撤回後總覽格的開頭
# 頁首規則：2026-11-12 實測 354 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 5 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"evidence level (L[1-5]|N/A)", re.I)


def desc_level_text(level):
    return "known uses only" if level == "N/A" else f"evidence level {level}"


DISCLAIMER_RE = re.compile(r"^## Disclaimer\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "Review correction", "annotate": "Review note", "rereview": "Pending re-review",
              "rereview_result": "Re-review result"},
    "action": {"correct": "Corrected", "annotate": "Annotated", "rereview": "Marked for re-review",
               "section": "Added a sourced section", "rereview_result": "Re-review completed",
               "header_level": "Header evidence level recomputed from the Quick Overview",
               "description_level": "Page description evidence level set to the header level"},
    "verdict": {"maintain": "Maintained", "downgrade": "Downgraded", "upgrade": "Upgraded", "withdraw": "Withdrawn"},
    "log_head": "## Review Log",
    "log_cols": "| Review date | Item | Action | Source |",
    "head": "> **{label} ({date})**: ",
    "originally": "Originally stated: \"{claim}\"",
    "source": "Source: {src}.",
    "decision": "Decision recommendation: {note}",
    "level_same": "evidence level {o} unchanged",
    "level_change": "evidence level {o} → {n}",
    "table_updated": " The {labels} on this page were updated to the re-review result; the original values are listed in the Review Log below.",
    "rereviewed": "Marked for re-review → re-reviewed (see the re-review result)",
    "hdr": "Header evidence level recomputed from the Quick Overview ({o} → {n})",
    "hdr_withdraw": "Main prediction withdrawn on re-review; header evidence level recomputed ({o} → {n})",
    "listed_under": ", now listed under \"{t}\"",
    "rr": "Re-review: {v}, {c}",
    "tu": "; {l}: \"{a}\" → \"{b}\"",
    "desc": "Page description: \"evidence level {o}\" changed to \"{n}\" (follows the header level; other text unchanged, original kept in the record)",
    "revised": " (revised {d}; earlier version kept in the record)",
    "superseded": "Superseded by the program-generated registration table (was: {a})",
    "regen": "No longer present after the report was regenerated ({d}: {n}; was: {a})",
    "prog": "No longer present after a program fix ({d}: {n}; was: {a})",
    "wd": "Review withdrawn ({d}: {n}; was: {a})",
    "intro": ("Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine "
              "register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and "
              "conclusions were not rewritten."),
    "intro_levels": ("Below is the review log for this page; the header evidence level follows the Quick Overview. "
                     "Model predictions, the overview table, and conclusions were not rewritten."),
    "intro_rr": ("Below is the review log for this page. Corrections are limited to basic factual statements and model prediction text "
                 "was not rewritten; evidence levels and decisions were changed only by a re-review result (downgrade, upgrade, or "
                 "withdrawal), with the original values listed below."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
MARKET_SEC = re.compile(r"^## South Africa Market Information\s*$")
# SAHPRA 註冊號（2026-11-12 依證據包實測的格式：「28/2.6/0351」「A40/7.1.3/0123」「A/20.2.8/123」「G1032」）
ID_RE = re.compile(r"\b(?:[A-Z]?\d{1,2}/\d{1,2}(?:\.\d+){0,3}/\d{3,4}|[A-Z]/\d{1,2}(?:\.\d+){0,3}/\d{3,4}|[A-Z]\d{3,5})\b")


def own_ids(tf):
    return sorted({str(r.get("license_id") or "").strip() for r in tf.get("records") or [] if r.get("license_id")})


def _slt():
    p = Path(__file__).resolve().parents[3] / "scripts" / "sync_license_pages.py"
    s = importlib.util.spec_from_file_location("za_sync_license_pages", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def program_block_problems(sec_lines, entry):
    """程式區塊（licenses:begin／end）＝依快照重算的結果（scripts/sync_license_pages.py 的 table_block 與 SHOW 規則）"""
    S = _slt()
    has_b, has_e = S.BEGIN in sec_lines, S.END in sec_lines
    hd = S.HEAD.split("\n")
    if has_b != has_e:
        return ["程式區塊標記不成對"]
    if not has_b:
        if any(l.strip() == hd[0] for l in sec_lines) or any(l.strip() == S.NONE_LINE for l in sec_lines):
            return ["程式表沒有程式區塊標記（跑 python3 scripts/sync_license_pages.py --mark-existing）"]
        return []
    i, j = sec_lines.index(S.BEGIN), sec_lines.index(S.END)
    blk = [x for x in sec_lines[i + 1:j] if x.strip()]
    rows, total = entry.get("rows") or [], entry.get("total") or 0
    if not rows:
        return [] if blk == [S.NONE_LINE] else ["程式區塊應為「查無 SAHPRA 註冊」一句"]
    tb = [x for x in blk if x.startswith("|")]
    show = [x.strip() for x in blk if not x.startswith("|")]
    n = len(tb) - 2
    if tb[:2] != hd:
        return ["程式區塊的表頭不是程式表頭"]
    if tb[2:] != rows[:n]:
        k = next((k for k, (x, y) in enumerate(zip(tb[2:], rows)) if x != y), min(n, len(rows)))
        return [f"程式表第 {k + 1} 列跟快照重算的結果不同（程式表被手改或資料已更新：跑 scripts/sync_license_pages.py）"]
    if not (min(5, total) <= n <= 20):
        return [f"程式表列數 {n} 不在 {min(5, total)}–20 之間"]
    want = [S.SHOW.format(n=n, m=total)] if total > n else []
    if show != want:
        return [f"程式區塊的 SHOW 句應為「{want[0] if want else '（無）'}」"]
    return []


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs；排程狀態格、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["34c7b025c", "a65297c2e", "abd20429a", "c97d21c2a", "d5c6364b6", "c920fe120", "368499a76", "e5e744898", "ac2b62c83", "3f897ce6f"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["6e50eb14c", "cc149b87e", "70f906ec0", "3ae0be411", "76eb6991a", "076267129", "c1dab5440", "04d991afa", "19ca4dd0c"]
SOURCES = [{"title": "SAHPRA medicine register (medapps export)", "url": "https://medapps.sahpra.org.za:6006/DateSearch/ExportData"},
           {"title": "SAHPRA", "url": "https://www.sahpra.org.za/"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9(*"\[])|\n')
PROGRAM_LINES = [re.compile(r"^Showing \d+ of \d+ registrations \(valid registrations first\)\.$"),
                 re.compile(r"^No SAHPRA registration was found in the data compiled for this report\.$")]
NUMW = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|both|all)"
LIC = r"(?:licen[cs]es?|registrations?|authori[sz]ations?|products?|records?)"
CLASSIFY = [
    ("tw", re.compile(r"Taiwan|TFDA", re.I)),
    ("cancel", re.compile(r"cancel|withdrawn|revoked|lapsed|no (?:valid|active|current|SAHPRA)|not (?:currently )?(?:registered|marketed|valid|active)|Section 21", re.I)),
    ("count", re.compile(rf"\b{NUMW}\b[^.;]{{0,40}}\b{LIC}|\b{LIC}\b[^.;]{{0,30}}\b{NUMW}\b|\bvalid\b", re.I)),
    ("combo", re.compile(r"single[- ]ingredient|combination|combo|multi-ingredient", re.I)),  # 只有單方／複方說法、沒有張數或狀態時才歸這類
]
SUMMARY = "Removed: \"{text}\""
REGEN_NOTE = "the report was regenerated in 2026-11 and no longer contains this statement"


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA", reason):
        return "tw"
    if re.search(r"開場白|自述", reason):
        return "leak"
    if re.search(r"延續|失去指涉|指代", reason):
        return "dep"
    if re.search(r"單方|複方", reason):
        return "combo"
    if re.search(r"註銷|查無|未上市|Section 21|沒有有效", reason):
        return "cancel"
    if re.search(r"張|有效|總數", reason):
        return "count"
    return None


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    n, v = fc["total"], fc.get("valid") or 0
    return (f" The SAHPRA data list {n} registration{'s' if n != 1 else ''} for this drug, {v} valid; the Quick Overview and the table "
            "under South Africa Market Information show the current figures.")


def note_for(kind, date, fc):
    d = f"SAHPRA registration data as of {date}"
    if kind == "tw":
        return "Removed: leftover template text about Taiwan's TFDA, which does not apply to this South African page."
    if kind == "leak":
        return "Removed: leftover text from the model's notes about its input data, not part of the report."
    if kind == "dep":
        return f"Removed: it continued a sentence that was removed for contradicting the {d}, and would not make sense on its own."
    if kind == "combo":
        return f"Removed: it described the products as single-ingredient or combination products in a way that did not match the {d}." + _fig(fc)
    if kind == "cancel":
        return f"Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the {d}." + _fig(fc)
    if kind == "count":
        return f"Removed: the number or status of registrations stated here did not match the {d}, after registrations were matched by ingredient." + _fig(fc)
    return f"Removed: it conflicted with the {d}, after registrations were matched by ingredient." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["Original Indication"]
ORIG_NONE_RE = re.compile(r"^\s*(not (recorded|available|listed)|none|n/a|no (approved )?indication)", re.I)
ORIG_SPLIT_RE = re.compile(r"[;,/()]+|\band\b|\bor\b", re.I)

# 產生程式許可證表的本站程式（build_license_snapshot 讀它的 rows_of；sync_notes_to_docs 用它的 carry_block）
PROGRAM_SCRIPT = "sync_license_pages.py"
