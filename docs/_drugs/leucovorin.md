---
layout: default
title: Leucovorin
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Leucovorin
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

# Leucovorin: From Methotrexate Rescue / 5-FU Chemotherapy Adjunct to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (calcium folinate) is a reduced folate traditionally used as rescue therapy after high-dose methotrexate and as a biomodulator to enhance 5-fluorouracil chemotherapy. The TxGNN model predicts it may be effective for **Primary Hyperoxaluria**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale argues against biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (data gap); clinically known as methotrexate-toxicity rescue and 5-FU chemotherapy biomodulator |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Leucovorin in this evidence pack (data gap DG002). Based on generally known pharmacology, Leucovorin is a reduced folate (5-formyltetrahydrofolate) that bypasses dihydrofolate reductase inhibition — it is used clinically to rescue normal cells from methotrexate toxicity and to potentiate 5-fluorouracil's inhibition of thymidylate synthase in colorectal cancer regimens. Its efficacy in these established uses is well documented; mechanistically, its activity is confined to one-carbon (folate) metabolism.

Primary hyperoxaluria, however, is caused by inherited deficiencies in hepatic glyoxylate-metabolising enzymes (AGT, GRHPR, or HOGA1), leading to excess oxalate production. The established adjunct therapy for this condition is pyridoxine (vitamin B6), not folate supplementation. There is no known regulatory link between folate/one-carbon metabolism and the glyoxylate-to-oxalate pathway.

Consequently, although the TxGNN score for this pairing is high (99.41%), the model-generated mechanistic rationale explicitly states there is **no direct mechanistic link** and that the high score likely reflects a knowledge-graph embedding artifact rather than a biologically grounded hypothesis. This prediction should be treated as a research signal only, not a basis for clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Leucovorin is currently **not registered or marketed** in South Africa — the evidence pack records 0 SAHPRA registrations and no license entries. No product-level market information is available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this evidence pack flags TFDA label warnings/contraindications (DG001) and DDI data as blocking/unresolved data gaps — a formal PI-based safety review has not yet been completed for this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (primary hyperoxaluria) has no clinical trial or literature support (Evidence Level L5), and the model's own rationale argues the mechanistic link is absent rather than merely indirect — this looks like a false-positive signal rather than a genuine repurposing lead. The drug is also not currently marketed in South Africa, and core safety data (label warnings, contraindications, MOA) are marked as blocking data gaps, so no safety pre-screening (S1) is possible yet.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved package insert warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action data via DrugBank (DG002, High)
- Independent pharmacological review of whether folate metabolism has any plausible interaction with oxalate biosynthesis before pursuing primary hyperoxaluria further
- If repurposing work continues, consider deprioritizing this indication in favor of candidates further down this same drug's prediction list that already show partial evidence — e.g. primary amyloidosis (L3, one Phase 1 trial, "Research Question" stage) and focal myositis (L4, 10 literature records, "Research Question" stage) — though both require disentangling Leucovorin's role as a chemotherapy adjunct/MTX-rescue agent from any direct disease-modifying effect before they can be considered credible leads
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

