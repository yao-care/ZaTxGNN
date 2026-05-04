---
layout: default
title: Cinchocaine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 0
---

# Cinchocaine Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cinchocaine Hydrochloride: Drug Repurposing Evaluation — Insufficient Data for Full Assessment

## One-Sentence Summary

Cinchocaine Hydrochloride (also known as dibucaine) is a long-acting amide-type local anaesthetic, typically used topically for anorectal conditions such as haemorrhoidal pain and pruritus.
The TxGNN model was **unable to generate repurposing predictions** for this drug because a DrugBank ID and mechanism of action data were not available in the current Evidence Pack.
A meaningful repurposing evaluation cannot proceed until the two identified critical data gaps (DG001, DG002) are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anaesthesia; topical use for haemorrhoidal and anorectal conditions (from general pharmacological knowledge — not confirmed in this Evidence Pack) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A — pipeline did not complete |
| Evidence Level | L5 — No model predictions or studies available |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN repurposing pipeline requires a valid **DrugBank ID** to anchor the drug within the knowledge graph and retrieve mechanism of action data. For Cinchocaine Hydrochloride, this identifier was not resolved (`drugbank_id: null` in the Evidence Pack), despite a successful DrugBank query in the system log (Query ID 1, 2026-03-26).

> **Likely cause:** The query may have matched on a synonym or salt form without returning a resolvable DrugBank accession number. Cinchocaine is also marketed under the INN **dibucaine** — a targeted search using this alternative name may resolve the mapping.

Until the DrugBank ID is confirmed and the MOA is retrieved, the knowledge graph cannot place this drug within the disease–drug network, and no indication predictions can be scored.

---

## South Africa Market Information

Cinchocaine Hydrochloride currently has **no SAHPRA-registered products** in South Africa and is classified as **not marketed**.

> **Note for reviewers:** Cinchocaine is commonly used in multi-ingredient combination products (e.g., cinchocaine + hydrocortisone for haemorrhoidal conditions, or cinchocaine + prednisolone in suppository/ointment forms) that are registered in other jurisdictions. A targeted SAHPRA search covering combination products containing cinchocaine is recommended to confirm whether any such products hold South African registration.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the online MedSafety portal (https://www.sahpra.org.za).

> **Critical Notice:** Both safety data gaps in this Evidence Pack are unresolved:
> - **DG001 (Blocking):** SAHPRA-approved warnings and contraindications were not retrieved. This prevents completion of the mandatory Safety Screening Step 1 (S1). No clinical repurposing evaluation can begin until this is resolved.
> - **DDI data:** The drug interaction query returned no results (`query_status: not_found`). This may reflect an unresolved drug identifier rather than a true absence of interactions — cinchocaine is known to interact with other sodium channel-blocking agents and certain antiarrhythmics.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Cinchocaine Hydrochloride is missing foundational data required to run the TxGNN pipeline — specifically the DrugBank ID and mechanism of action. Without these, no repurposing candidates were predicted, and the safety screening process cannot be initiated. There is no evidence base to evaluate at this time.

**To proceed, the following is needed:**

- [ ] **\[Blocking — DG001\]** Retrieve the SAHPRA-approved Professional Information (PI) PDF from the SAHPRA product database and extract key warnings, contraindications, and special population precautions
- [ ] **\[High — DG002\]** Re-query DrugBank using the alternative INN **dibucaine** (and variant spellings: cinchocaine, cincocaína) to obtain a confirmed DrugBank accession ID and mechanism of action
- [ ] Once DrugBank ID is confirmed, re-run the TxGNN prediction pipeline to generate ranked repurposing candidates
- [ ] Conduct a SAHPRA product search for **combination products** containing cinchocaine (e.g., with hydrocortisone, prednisolone) to accurately characterise South African market presence
- [ ] Re-run drug interaction query using the confirmed DrugBank ID to populate DDI data

---

*This report is generated for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before application. Data sourced from TxGNN Evidence Pack version v4, data cutoff 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

