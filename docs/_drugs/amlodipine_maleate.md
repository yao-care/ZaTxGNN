---
layout: default
title: Amlodipine Maleate
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 0
---

# Amlodipine Maleate
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

# Amlodipine Maleate: Drug Repurposing Evaluation

---

## One-Sentence Summary

Amlodipine maleate is a specific salt form of the dihydropyridine calcium channel blocker amlodipine, used in the management of hypertension and angina pectoris in other markets. No TxGNN repurposing predictions were generated for this compound in the current Evidence Pack, and the maleate salt formulation holds no SAHPRA registrations on record. This report therefore functions as an initial data gap assessment rather than a full repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Cannot be determined — no predictions available |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why a Full Prediction Rationale Cannot Be Provided

No TxGNN repurposing prediction was produced for this compound, so no new indication rationale can be evaluated at this time.

Detailed mechanism of action data is also absent from this Evidence Pack. Although amlodipine maleate is a recognised salt form of a widely used active moiety, the DrugBank ID was not linked in the submission — despite the query log confirming a **successful DrugBank search returning 1 result** (`query_date: 2026-03-26`, `result_count: 1`). This disconnect between a successful query and an empty `drugbank_id` field suggests a data extraction or mapping failure in the pipeline, rather than an absence of DrugBank coverage.

Until the DrugBank ID is resolved and original indication data is populated, the TxGNN model cannot be run, and no mechanistic reasoning can be formally assessed.

> **Note on salt form:** Amlodipine besylate is the salt form most commonly registered globally, including in South Africa. If this evaluation is intended to cover the active moiety (amlodipine) across all salt forms, SAHPRA registration data for the besylate formulation should be retrieved separately and may substantially change the market status assessment.

---

## South Africa Market Information

No SAHPRA registrations were found for **amlodipine maleate** specifically.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | No registered products found | — | — |

> Amlodipine besylate products are widely available in South Africa. If coverage of the active moiety is intended, a separate regulatory search using the maleate and besylate salt forms together is recommended.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated, and three blocking data gaps — original indications, mechanism of action, and safety information — remain unresolved. A meaningful repurposing evaluation cannot proceed until these are addressed.

**To proceed, the following is needed:**

- **Resolve the DrugBank ID linkage** — the query returned 1 result but no ID was captured; re-extract and verify the DrugBank ID (likely `DB00381` for amlodipine)
- **Retrieve MOA data** from DrugBank API once the ID is confirmed
- **Populate original indication(s)** from SAHPRA PI or DrugBank approved indications
- **Clarify the evaluation scope** — determine whether the target is the maleate salt specifically, or the amlodipine active moiety (covering besylate and all other registered salts)
- **Re-run the TxGNN prediction pipeline** once DrugBank ID and indication data are available
- **Obtain SAHPRA PI** for amlodipine-containing products to address the blocking safety data gap (DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

