---
layout: default
title: Tretinoin
parent: 僅模型預測 (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Tretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tretinoin: From Undocumented Original Indication to Rheumatoid Nodulosis (Low-Confidence Signal)

## One-Sentence Summary

This evidence pack does not record tretinoin's original approved indication or mechanism of action (both flagged as data gaps). The TxGNN model's top-ranked prediction for this drug is **Rheumatoid Nodulosis**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a model score with no corroborating evidence, and the drug's known retinoid-related adverse effects (arthralgia/musculoskeletal symptoms) point in the opposite direction of the hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap — DrugBank/SAHPRA licence data not yet retrieved) |
| Predicted New Indication | Rheumatoid Nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field (data gap DG002). However, the pack's own rationale text for other candidates confirms tretinoin is all-trans retinoic acid (ATRA), a RAR/RXR nuclear receptor ligand — a well-characterised class independent of this gap.

For the top-ranked prediction, the evidence pack itself argues **against** biological plausibility rather than for it: there is no direct mechanistic pathway linking retinoic acid signalling to rheumatoid nodule formation, and retinoid-class drugs are already known to cause arthralgia and musculoskeletal adverse effects — the opposite of a therapeutic effect on a joint/nodule-related condition. The pack's own annotation concludes the high TxGNN score likely reflects a spurious association from "cartilage/joint" node proximity in the knowledge graph rather than a genuine drug–disease relationship.

Because no clinical trial or literature evidence exists for this specific pairing, there is no basis to support the prediction beyond the raw model score.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

No SAHPRA registrations are recorded for tretinoin in this evidence pack (`total_licenses: 0`, market status: Not marketed). Registration and Essential Medicines List status cannot be assessed until this data gap (DG001, blocking) is resolved via SAHPRA licence lookup.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug interaction data are all marked as data gaps in this pack — none could be verified.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Rheumatoid Nodulosis) has zero clinical trials, zero literature, and a mechanistic rationale that actively contradicts the hypothesis. This does not meet even a minimal bar to advance past model-score-only status (L5/S0).

**Note on other candidates in this batch:** Two lower-ranked predictions in this pack have at least some literature support and were staged further (S1, "Research Question"): **Osteoarthritis** (rank 7, 20 PubMed records, though directionally mixed — some show retinoic acid as disease-modifying, others show it as OA-inducing) and **Quinquaud's folliculitis decalvans** (rank 10, 1 case report on a related but non-identical condition). If prioritising within this drug's candidate set, these two warrant review ahead of rheumatoid nodulosis.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — resolve blocking data gap DG001
- Confirmed mechanism of action from DrugBank — resolve high-severity gap DG002
- Confirmed original approved indication(s) for tretinoin
- If pursuing the OA or folliculitis decalvans signals instead: mechanistic studies resolving the conflicting direction of retinoic acid's effect on cartilage/joint tissue
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

