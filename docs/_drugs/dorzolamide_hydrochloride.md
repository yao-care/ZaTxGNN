---
layout: default
title: Dorzolamide Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 0
---

# Dorzolamide Hydrochloride
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

# Dorzolamide Hydrochloride: Repurposing Evaluation — No Predicted Indications Available

---

## One-Sentence Summary

Dorzolamide hydrochloride is a carbonic anhydrase inhibitor conventionally used as a topical ophthalmic agent to reduce elevated intraocular pressure in glaucoma and ocular hypertension. The current Evidence Pack contains **no TxGNN-predicted new indications** for this drug, and two critical data gaps — missing mechanism of action data and absent SAHPRA registration records — prevent a complete repurposing evaluation. No decision on repurposing can be made until the prediction pipeline is re-run with complete drug identity data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack (known pharmacological use: glaucoma / ocular hypertension) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no predictions generated; evaluation cannot proceed |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The TxGNN model requires a resolved DrugBank ID and at least one mapped original indication to generate repurposing candidates via the knowledge graph. For this drug record, **both fields are absent**:

- `drugbank_id` is null — the drug has not been linked to a DrugBank node, so no graph traversal can occur.
- `original_indications` is empty — the indication anchor required for similarity-based prediction is missing.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, dorzolamide hydrochloride is a sulfonamide-derived **carbonic anhydrase inhibitor** targeting isoenzymes CA-II and CA-IV in the ciliary epithelium. By blocking bicarbonate secretion, it reduces aqueous humour production and lowers intraocular pressure. Its established efficacy in open-angle glaucoma and ocular hypertension is well documented, but until this information is formally captured in the pipeline's structured data, the model cannot reason about mechanistic overlap with candidate diseases.

Before a repurposing hypothesis can be assessed, the data gaps listed below must be resolved and the TxGNN pipeline re-run.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete: no TxGNN-predicted indications exist, the DrugBank ID is unresolved, original indications are not recorded, and there are zero SAHPRA registrations on file. A repurposing evaluation cannot be meaningfully completed or acted upon under these conditions.

**To proceed, the following is needed:**

- **Resolve DrugBank ID** for dorzolamide hydrochloride (search term: "dorzolamide") to enable knowledge graph traversal — this is the highest-priority unblocking step
- **Record structured original indication(s)** (e.g., "open-angle glaucoma", "ocular hypertension") to provide a disease anchor for TxGNN
- **Re-run the TxGNN prediction pipeline** once the above two items are complete, to generate candidate indications and confidence scores
- **Obtain SAHPRA-approved PI or equivalent prescribing information** to populate safety warnings and contraindications *(Data Gap DG001 — Blocking severity)*
- **Retrieve mechanism of action data from DrugBank API** to support mechanistic rationale analysis *(Data Gap DG002 — High severity)*
- **Verify South Africa regulatory pathway**: if the drug is not currently registered with SAHPRA, determine whether a Section 21 authorisation or new registration application would be required before any clinical repurposing study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

