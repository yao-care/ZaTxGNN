"""依成分重建後，把藥物頁的許可證內容對齊新事實（2026-11-05，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles；工作目錄（scripts/txgnn_ws.sh）已跑
dump_license_facts_20261021.py（事實）與 license_table_sync 的 sync_market_rows（概覽表狀態列、張數列）。
本支做兩件事：
1. 許可證表：「## South Africa Market Information」段落裡原有的表，換成程式產生的表（Licence／Product／Dosage form／Status，
   有效在前、單方在前），列數＝原表列數與 min(5, 總數) 取大（最多 20）；總數多於列數時表後加一句「Showing N of M registrations」。
   段落裡沒有表的頁不新增；新資料沒有任何註冊時拿掉表，改一句「No SAHPRA registration was found in the data compiled for this report.」
2. 刪句：正文（表格、標題、概覽表除外）跟新事實矛盾的句子整句刪除，不改寫（前例 DE、In 的 ONLY_CANCEL 做法）：
   M3／M3a／M3b／M3c（check_drug_page 的規則，含 2026-11-05 擴充）、張數精確不符（COUNT_*）、
   點名的產品狀態與新資料相反（NAMED_STATUS）、人工清單 scripts/license_sentence_fixes.json（附理由，例：LLM 開場白外洩）。
   刪完整行空掉的行拿掉，連續空行併成一行。刪掉的句子逐句寫進 --log（頁、規則、原句、依據）。
用法（repo 根目錄）：python3 scripts/sync_license_pages.py --ws <工作目錄> [--dry-run] [--log out.tsv] [頁 ...]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "ZaTxGNN"
SEC = "## South Africa Market Information"
HEAD = "| Licence | Product | Dosage form | Status |\n|------|------|------|------|"
LAB = {"valid": "Valid", "cancelled": "Cancelled", "not_marketed": "Approved, not marketed"}
NONE_LINE = "No SAHPRA registration was found in the data compiled for this report."
SHOW = "Showing {n} of {m} registrations (valid registrations first)."
ABBR = [("Reg. No.", "Reg․ No․"), ("e.g.", "e․g․"), ("i.e.", "i․e․"), ("vs.", "vs․"),
        ("No.", "No․"), ("et al.", "et al․"), ("approx.", "approx․"), ("Vit.", "Vit․"), ("St.", "St․")]
QUAL = re.compile(r"\b(further|other|remaining|additional|more|main|following|first|listed|shown|showing|these|those|another)\b", re.I)
QUAL_PRE = re.compile(r"\b(further|other|remaining|additional|more|another|first|these|those)\s+$", re.I)
NUMW = r"(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty)"
TOTAL_CNT = re.compile(r"\b" + NUMW + r"\b((?:[\s-]+(?!of\b|and\b|are\b|is\b|were\b|was\b)[\w-]+){0,3}?)[\s-]+(registrations?|licen[cs]es?|registration records)\b", re.I)
CANC_CNT = re.compile(r"\b" + NUMW + r"\b((?:[\s-]+(?!of\b|and\b)[\w-]+){0,3}?)\s+(are|is|were|was|have been|has been)\s+cancel+ed\b|\b" + NUMW + r"\s+cancel+ed\b", re.I)


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def split_sentences(line):
    t = line
    for a, b in ABBR:
        t = t.replace(a, b)
    parts = re.split(r"(?<=[.!?])(\s+)(?=[*\"'(\[A-Z0-9])", t)
    out = []  # [(句子, 後面的空白)]
    for i in range(0, len(parts), 2):
        s = parts[i]
        for a, b in ABBR:
            s = s.replace(b, a)
        out.append((s, parts[i + 1] if i + 1 < len(parts) else ""))
    return out


def norm(x):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", str(x or "").lower()).split())


def _n(x):
    w = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
         "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20}
    return int(x) if x.isdigit() else w.get(x.lower())


IN_TOTAL = re.compile(r"\b" + NUMW + r"\s+in total\b", re.I)
REST = re.compile(r"\b(?:other|remaining|further|additional|more)\s+" + NUMW + r"\s+(?=are\b|include|exist|is\b|registrations?|licen|products?|entries)|"
                  r"\b" + NUMW + r"\s+(?:other|remaining|further|additional|more)\s+(?=[\w-]*\s*(registrations?|licen|products?|syrup|valid|entries))", re.I)
ONLY = re.compile(r"\b(the|this|its) only (valid |local |registered |current )?(registration|product|licen[cs]e|entry|record)\b|"
                  r"\bonly (one|1|a single) (valid |registered |local )?(registration|product|licen[cs]e)\b|\b(the|this) single registration\b|"
                  r"\bthe registered product (is|was)\b|\bthe registered dosage form is\b|\bonly (one|1) registration\b", re.I)
BOTH = re.compile(r"\b(both|neither)\s+(of the\s+)?([\w-]+\s+){0,2}?(registrations?|licen[cs]es?|records|entries|products|registered products)\b", re.I)
KIND_SINGLE = re.compile(r"\b(recorded|classif\w+|listed|label\w*|classed)\s+(them\s+)?(in the (records|data|source data)\s+)?as\s+(a\s+)?single[- ](ingredient|entity|entry)", re.I)
ALL_SINGLE = re.compile(r"\ball\b[^.;]{0,40}\bsingle[- ](ingredient|entity|entry)", re.I)
GONE_CTX = re.compile(r"registration|registered|licen[cs]e|record|entr(y|ies)|listed|products?\b|named", re.I)
# 緊接在被刪句後面、以指代詞開頭的句子：前句刪掉後就斷了（「This should…」「They are…」「It should not…」）
DEPENDENT = re.compile(r"^\W*(It|Its|This|These|They|Their|Those|Others|As noted above|See the note above|The last entry|"
                       r"Without these|Under these|Until local registration)\b")


def verdict(ck, s, fc, recs, counts=True, rest=None, gone=()):
    """這句跟新事實矛盾就回傳 (規則, 依據)；不矛盾回 None。counts＝是否查張數精確不符（只在市場資訊段與概覽段查）"""
    ms, v, n, c = fc.get("market_status"), fc.get("valid") or 0, fc.get("total"), fc.get("cancelled") or 0
    basis = f"新事實：{ms}，有效 {v}／共 {n if n is not None else '?'}（註銷 {c}）"
    if re.search(r"trial|SANCTR|PACTR|ICTRP|NCT\d|stud(y|ies)", s, re.I) and not re.search(r"SAHPRA|licen[cs]e", s, re.I):
        return None
    if v > 0 and (ck.ALL_CANCEL.search(s) or ck.NOT_MKT_CLAIM.search(s) or ((ck.NOT_MKT_LOOSE.search(s) or ck.ONLY_CANCEL.search(s))
                                                                          and not ck.POS_VALID.search(s))) \
            and not (ck.still_valid_ok(s) and not ck.NOT_MKT_CLAIM.search(s)):
        return "M3", basis
    if ms in ("Cancelled only", "Not marketed") and (ck.marketed_word("en") in s or ck.MKT_CLAIM_EXTRA.search(s)) and not ck.mv2.NEG.search(s):
        return "M3", basis
    sub = ck.m3x("en", s, fc)
    if sub:
        return sub, basis
    if counts and not fc.get("partial") and n is not None:
        for m in ck.VALID_COUNT.finditer(s):
            k = _n(m.group(1) or m.group(5))
            pre = s[max(0, m.start() - 14):m.start()]
            if k is None or ck.AT_LEAST.search(pre) or QUAL.search(m.group(2) or "") or QUAL_PRE.search(pre):
                continue
            if m.group(1) and re.search(r"\bof (the )?$", pre, re.I):
                continue
            if k != v:
                return "COUNT_VALID", basis + f"；句中有效 {k}"
        for m in TOTAL_CNT.finditer(s):
            k = _n(m.group(1))
            pre = s[max(0, m.start() - 14):m.start()]
            if k is None or ck.AT_LEAST.search(pre) or QUAL.search(m.group(2) or "") or QUAL_PRE.search(pre) or \
                    re.search(r"\b(showing|shows|lists?|are|section)\s+$", pre, re.I):
                continue
            if re.search(r"\b(single|combination|oral|topical|injectable|parenteral|tablet|cream|infusion)\b", m.group(2) or "", re.I) and k < n:
                continue  # 「2 single-ingredient registrations」只是子集
            if k != n:
                return "COUNT_TOTAL", basis + f"；句中總數 {k}"
        for m in CANC_CNT.finditer(s):
            k = _n(m.group(1) or m.group(4))
            if k is None or QUAL.search(m.group(2) or "") or QUAL_PRE.search(s[max(0, m.start() - 14):m.start()]):
                continue
            if k != c:
                return "COUNT_CANCELLED", basis + f"；句中註銷 {k}"
    if counts and n is not None:
        m = IN_TOTAL.search(s)
        if m and _n(m.group(1)) not in (None, n):
            return "COUNT_TOTAL", basis + f"；句中總數 {m.group(1)}"
        for m in REST.finditer(s):
            k = _n(m.group(1) or m.group(2))
            if rest is not None and k is not None and k != rest and not re.search(r"prediction|indication", s, re.I):
                return "COUNT_TOTAL", basis + f"；句中「其餘 {k}」，表格以外實為 {rest}"
        if n != 2 and BOTH.search(s) and not re.search(r"off-label|indicat|approved for", s, re.I):
            return "COUNT_TOTAL", basis + "；句中寫兩張（both／neither）"
        if KIND_SINGLE.search(s):
            low = f" {norm(s)} "
            named = [r for r in recs if len(norm(r.get("brand_name_en")).split()[0] if norm(r.get("brand_name_en")) else "") >= 5
                     and f" {norm(r.get('brand_name_en')).split()[0]} " in low]
            pool = named or [r for r in recs if r.get("license_status", "valid") == "valid"]
            if any(r.get("kind") == "combo" for r in pool):
                return "COMPOSITION", basis + "；新紀錄（SAHPRA 成分全文）把這些產品記為複方，句中說資料把它們記成單方"
        if n > 1 and ONLY.search(s):
            return "COUNT_TOTAL", basis + "；句中寫只有一張／一個產品"
        if ALL_SINGLE.search(s) and any(r.get("kind") == "combo" for r in recs if r.get("license_status", "valid") == "valid" and not r.get("excluded_reason")):
            return "COMPOSITION", basis + "；新紀錄裡有複方，句中寫全部是單方"
    if counts and gone and GONE_CTX.search(s):
        low = f" {norm(s)} "
        for nm, reg in gone:
            if (len(nm) >= 5 and f" {nm} " in low) or (reg and reg in s):
                return "STALE_ENTRY", basis + f"；句中點名的 {reg} {nm} 已從本藥剔除（SAHPRA 成分不含本藥或非註冊號）"
    # 點名的產品：句子說有效、但該產品已註銷（或反過來）
    pos = re.search(r"\b(valid|are registered|is registered|remains? on the market)\b", s, re.I) and not re.search(r"cancel|withdrawn|revoked", s, re.I)
    neg = re.search(r"cancel+ed|revoked|withdrawn", s, re.I) and not re.search(r"\bvalid\b", s, re.I)
    if (pos or neg) and re.search(r"registration|licen[cs]e|registered|\bproducts?\b", s, re.I):
        low = norm(s)
        for r in recs:
            nm = norm(r.get("brand_name_en"))
            reg = str(r.get("license_id") or "")
            hit = (len(nm) >= 5 and f" {nm} " in f" {low} ") or (reg and reg in s)
            if not hit:
                continue
            st = r.get("license_status") or "valid"
            if pos and st == "cancelled":
                return "NAMED_STATUS", basis + f"；{reg} {r.get('brand_name_en')} 在 SAHPRA 已註銷"
            if neg and st == "valid" and r.get("status"):
                return "NAMED_STATUS", basis + f"；{reg} {r.get('brand_name_en')} 在 SAHPRA 仍為 {r.get('status')}"
    return None


def table_block(recs, nrows):
    seen, rows = set(), []
    for r in recs:
        k = r.get("license_id")
        if not k or k in seen:
            continue
        seen.add(k)
        rows.append(f"| {k} | {str(r.get('brand_name_en') or '').replace('|', '/').strip()[:70]} | "
                    f"{str(r.get('dosage_form') or '').replace('|', '/').strip() or 'Not recorded'} | {LAB.get(r.get('license_status') or 'valid', 'Valid')} |")
    return HEAD.split("\n") + rows[:nrows], len(rows)


def process(ck, page, fc, bundle, manual):
    raw = page.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw[:500]
    t = raw.replace("\r\n", "\n")
    if "layout: id_redirect" in t[:3000] or 'http-equiv="refresh"' in t[:3000]:
        return None, [], False
    fm_end = t.index("\n---", 4) + 4 if t.startswith("---") else 0
    lines = t.split("\n")
    start = t[:fm_end].count("\n") + 1
    recs = (bundle.get("tfda") or {}).get("records") or []
    excl = (bundle.get("tfda") or {}).get("excluded_records") or []
    log = []
    nrows, rest = None, None
    if SEC in lines:
        a0 = lines.index(SEC) + 1
        b0 = next((k for k in range(a0, len(lines)) if lines[k].startswith("## ")), len(lines))
        tb0 = [k for k in range(a0, b0) if lines[k].startswith("|")]
        total0 = len({r.get("license_id") for r in recs if r.get("license_id")})
        if tb0 and total0:
            y0 = tb0[0]
            while y0 + 1 < b0 and lines[y0 + 1].startswith("|"):
                y0 += 1
            nrows = min(20, max(y0 - tb0[0] - 1, min(5, total0)))
            rest = max(0, total0 - nrows)
    keep_ids = {r.get("license_id") for r in recs}
    gone = [(norm(re.sub(r"\(.*?\)", "", str(e.get("brand_name_en") or ""))), str(e.get("license_id") or "")) for e in excl
            if e.get("license_id") not in keep_ids]
    sec = ""
    for i in range(start, len(lines)):
        l = lines[i]
        if l.startswith("## "):
            sec = l.strip()
        if not l.strip() or l.startswith(("|", "#", "{:", "<", "---")):
            continue
        sents = split_sentences(l)
        keep, changed = [], False
        prev_deleted = False
        for s, sp in sents:
            core = s.strip()
            why = None
            if prev_deleted and DEPENDENT.search(re.sub(r"^\s*([-*>]\s*)+", "", core)) \
                    and not re.search(r"Essential Medicines List|\bEML\b|This report", core):
                why = ("DEPENDENT", "緊接在被刪句後、以指代詞開頭；前句刪除後失去指涉對象（不改寫，一併刪除）")
            for m in manual.get(page.stem, []):
                if not why and m["sentence"] in core:
                    why = ("MANUAL", m["reason"])
            if not why and re.search(r"[A-Za-z]{3}", core):
                why = verdict(ck, re.sub(r"^\s*[-*]\s+", "", core), fc, recs, counts=sec in (SEC, "## Quick Overview"), rest=rest, gone=gone)
            if why:
                log.append((page.stem, why[0], core, why[1]))
                changed = True
                prev_deleted = True
                continue
            prev_deleted = False
            keep.append((s, sp))
        if changed:
            new = "".join(s + sp for s, sp in keep).rstrip()
            bullet = re.match(r"^(\s*[-*]\s+|\s*\d+\.\s+|>\s*)", l)
            if not re.sub(r"^\s*([-*]|\d+\.|>)\s*", "", new).strip(" *_>"):
                new = None
            elif bullet and not new.lstrip().startswith(bullet.group(1).strip()):
                new = bullet.group(1) + new.lstrip()
            lines[i] = new
    lines = [l for l in lines if l is not None]
    # 許可證表
    if SEC in lines:
        a = lines.index(SEC) + 1
        b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        if tb:
            x, y = tb[0], tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            old_rows = max(0, y - x - 1)
            total = len({r.get("license_id") for r in recs if r.get("license_id")})
            if total:
                nrows = nrows or min(20, max(old_rows, min(5, total)))
                new_tb, total = table_block(recs, nrows)
                sec_text = "\n".join(lines[a:b])
                note = []
                lines_after = [l for l in lines[y + 1:b] if not l.startswith("Showing ") or "(valid registrations first)" not in l]
                if total > nrows and not re.search(r"\bShowing \d+ of \d+", "\n".join(lines_after)):
                    note = ["", SHOW.format(n=nrows, m=total)]
                lines = lines[:x] + new_tb + note + lines_after + lines[b:]
            else:
                lines = lines[:x] + [NONE_LINE] + lines[y + 1:]
            # 表格前要空行（kramdown）
            k = next(k for k in range(a, len(lines)) if lines[k].startswith("|") or lines[k] == NONE_LINE)
            if lines[k - 1].strip():
                lines.insert(k, "")
    t2 = "\n".join(lines)
    t2 = re.sub(r"\n{3,}", "\n\n", t2)
    return (t2 if t2 != t else None), log, crlf


def main(argv):
    ws = Path(argv[argv.index("--ws") + 1])
    dry = "--dry-run" in argv
    logf = argv[argv.index("--log") + 1] if "--log" in argv else None
    skip = {ws.as_posix(), logf}
    only = {a for a in argv if not a.startswith("--") and a not in skip}
    ck = _load("ck", ws / ".claude/check_drug_page.py")
    facts = json.loads((ws / ".claude/cache/license_facts" / f"{SITE}.json").read_text(encoding="utf-8"))
    mf = ROOT / "scripts/license_sentence_fixes.json"
    manual = json.loads(mf.read_text(encoding="utf-8")) if mf.exists() else {}
    all_log, n = [], 0
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        key = page.stem if page.stem in facts else page.stem.replace("-", "_")
        bf = ROOT / "data/bundles" / key / "drug_bundle.json"
        if key not in facts or not bf.exists():
            continue
        res = process(ck, page, facts[key], json.loads(bf.read_text(encoding="utf-8")), manual)
        if res[0] is None and not res[1]:
            continue
        new, log, crlf = res
        all_log += log
        if new is not None:
            n += 1
            if not dry:
                page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    if logf:
        Path(logf).write_text("頁\t規則\t原句\t依據\n" + "\n".join("\t".join(x) for x in all_log) + "\n", encoding="utf-8")
    print(f"改頁 {n}；刪句 {len(all_log)}")


if __name__ == "__main__":
    main(sys.argv[1:])
