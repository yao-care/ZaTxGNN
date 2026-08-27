---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From Undocumented Original Indication to Hypotrichosis Simplex of the Scalp (Predicted)

## One-Sentence Summary

Spironolactone's originally registered indication is not documented in the current dataset, and detailed mechanism-of-action data is also missing. The TxGNN model predicts potential activity in **Hypotrichosis Simplex of the Scalp**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it rests on the model score alone, and the evidence pack's own mechanistic review raises significant doubts about biological plausibility.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no indications or market registrations on file) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why Is This Prediction Reasonable?

Detailed mechanism-of-action data for spironolactone is not currently available in this dataset, and no original indication is on file to compare against. What can be said, based on the supporting rationale accompanying this prediction, is that spironolactone is a mineralocorticoid receptor antagonist, and its only well-established dermatological use is antiandrogenic (blocking the androgen receptor and lowering testosterone/DHT), applied in androgenetic (androgen-dependent) alopecia.

Hypotrichosis simplex of the scalp, however, is an autosomal hereditary disorder associated with keratinocyte-related gene mutations (e.g. CDSN) that cause a structural follicular developmental defect — it is not driven by androgen signaling. This means the pharmacological pathway that would justify repurposing (androgen suppression) does not map onto the pathology of the predicted disease.

The most likely explanation is that TxGNN scored this pairing based on superficial phenotypic similarity within the knowledge graph — both conditions fall under "hair loss/thinning" — rather than a genuine mechanistic relationship. The same concern applies to the second-ranked prediction, congenital hypotrichosis milia (score 99.04%), which is also a congenital structural disorder unrelated to androgen pathways. Both predictions should be treated as hypothesis-generating signals only, not as evidence of therapeutic potential.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Spironolactone is not currently marketed and has no registrations on file for this product line (0 registrations recorded).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-only prediction with no clinical trial or literature support, and the evidence pack's own mechanistic review flags a biological mismatch between spironolactone's antiandrogenic mode of action and the genetic/structural pathology of both predicted indications. Combined with the absence of local market registration and blocking safety data gaps, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation for spironolactone
- Preclinical or mechanistic studies directly testing mineralocorticoid/androgen receptor pathways in structural (non-androgenic) hair follicle disorders, to resolve the plausibility concern raised above
- Confirmation of original registered indication(s), for comparison against the predicted use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

