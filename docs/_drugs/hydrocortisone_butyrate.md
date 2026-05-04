---
layout: default
title: Hydrocortisone Butyrate
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 0
---

# Hydrocortisone Butyrate
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

# Hydrocortisone Butyrate: Evaluation Report — No Repurposing Predictions Available

---

## One-Sentence Summary

Hydrocortisone butyrate (DB14540) is a corticosteroid compound currently not registered with SAHPRA in South Africa.
The TxGNN model has **not generated any repurposing predictions** for this drug at this time — the evidence pack contains **no predicted indications, no clinical trial evidence, and no supporting literature**.
This report documents the outstanding data gaps and recommends a **Hold** decision pending data completion.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current evidence pack |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — No predictions or supporting evidence available |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The current evidence pack for hydrocortisone butyrate (DB14540) is incomplete in two critical areas that prevent the TxGNN pipeline from generating repurposing candidates:

**1. No original indication data on record.**
The SAHPRA regulatory data returns zero licences and no approved indication text. Without a documented therapeutic starting point, the model lacks the anchoring context required to rank and surface plausible new indications.

**2. Mechanism of action (MOA) unavailable.**
A DrugBank query was successfully executed (query log entry 1, 2026-03-26), returning one result record; however, no MOA data was captured in the output. MOA is classified as a **High-severity** data gap (DG002) because mechanistic rationale is central to assessing the biological plausibility of any repurposing prediction.

> **Note for reviewers:** Hydrocortisone butyrate is broadly recognised in pharmacological literature as a medium-potency topical glucocorticoid used for inflammatory dermatoses; however, this background knowledge is not formally structured within the current evidence pack and cannot substitute for the required data fields in the TxGNN evaluation workflow.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Hydrocortisone butyrate is **not currently registered with SAHPRA** and holds no South African product licences. No Essential Medicines List (EML) inclusion applies.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions have been generated, and all critical evaluation fields — original indication, mechanism of action, and safety information — are absent from the current evidence pack. There is no evidentiary basis on which to assess or recommend a repurposing pathway at this stage.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve SAHPRA-approved Professional Information (PI) to populate warnings and contraindications; without this, the safety screening step (S1) cannot be initiated
- **[High — DG002]** Query the DrugBank API directly for DB14540 to extract MOA, drug categories, and toxicity data; confirm whether the returned record contains populated pharmacology fields
- **Verify TxGNN node coverage:** Confirm that hydrocortisone butyrate (DB14540) is present as a valid drug node in the TxGNN knowledge graph (`data/node.csv`); if absent, the prediction pipeline will silently return zero results
- **Document original approved indications:** Register at least one structured indication (e.g., topical inflammatory skin conditions such as eczema or psoriasis) to enable the model to compute disease-similarity scores
- **Re-run the full prediction pipeline** once the above gaps are resolved, then regenerate this evidence pack at version ≥ v5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

