---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Dutasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha reductase inhibitor. The registration data supplied lists no approved indication, but the drug is generally used for androgen-driven conditions such as benign prostatic hyperplasia, and this should be confirmed against the SAHPRA Professional Information (PI).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, with **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model-only and the mechanistic link is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (benign prostatic hyperplasia is the usual use; confirm against the PI) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dutasteride inhibits 5-alpha reductase types 1 and 2 and lowers dihydrotestosterone (DHT). Detailed mechanism-of-action data from DrugBank is not available in this pack, so the description above comes from the pack's mechanistic assessment.

Ambras syndrome is a congenital condition caused by chromosomal rearrangements affecting TRPS1 regulation at 8q22. It is not primarily androgen-driven, so lowering DHT has no clear reason to help. The very high TxGNN score reflects a pattern in the knowledge graph. It may simply capture the drug's known association with hair-related conditions, possibly in the opposite direction (reducing hair growth rather than increasing it). Without clinical evidence, the score should not be read as support for efficacy.

### Other Predictions Reviewed

None of the other top-10 predictions has supporting trial evidence. All are rated "Hold".

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Hypertrichosis | 99.997% | L5 | Indirect link only. Hypertrichosis is largely androgen-independent. |
| 3 | Malformation syndrome with odontal/periodontal component | 99.997% | L5 | No credible link. The 20 retrieved papers concern periodontitis in general and none evaluates dutasteride. |
| 4 | Syndrome with Dandy-Walker malformation | 99.996% | L5 | No plausible link. Likely a graph artefact. |
| 5 | Isolated genetic hair shaft abnormality | 99.996% | L5 | Structural defect not driven by DHT. |
| 6 | Hypotrichosis simplex of the scalp | 99.771% | L5 | Genetic, not DHT-mediated. Cannot extrapolate from androgenetic alopecia. |
| 7 | Congenital hypotrichosis milia | 99.753% | L5 | No known androgen-dependent mechanism. |
| 8 | Diffuse alopecia areata | 99.675% | L4 | Autoimmune. The one retrieved paper is a review of androgenetic alopecia in women and is a disease mismatch. |
| 9 | Migraine with brainstem aura | 99.667% | L5 | Speculative link through neurosteroids. |
| 10 | Familial isolated trichomegaly | 99.565% | L5 | Mechanism not established as androgen-dependent. |

## Clinical Trial Evidence

Currently no related clinical trials registered. No ClinicalTrials.gov, SANCTR, PACTR or ICTRP trials were retrieved for this prediction.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 55/21.12/0032 | Swifsul | Capsule | Not stated in the data |
| Reg. No. 44/21.12/0850 | Duodart 0.5mg/0.4mg | Capsule (oral) | Not stated in the data |

The Essential Medicines List (EML) status was not provided. Approved indication text should be taken from the SAHPRA package inserts.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or drug-specific literature. The biological link between DHT suppression and Ambras syndrome is weak. All ten predicted indications are also on hold.

**To proceed, the following is needed:**
- SAHPRA package insert data (approved indications, warnings, contraindications), because the missing safety data blocks safety screening
- Mechanism-of-action data from DrugBank
- Disease-specific preclinical or clinical evidence linking 5-alpha reductase inhibition to the predicted condition
- A review of whether the model score reflects the opposite direction of effect (hair reduction rather than growth)
- A route-compatibility assessment against the predicted indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

