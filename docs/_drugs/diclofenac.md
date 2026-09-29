---
layout: default
title: Diclofenac
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From NSAID Pain and Inflammation Use to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a nonsteroidal anti-inflammatory drug (NSAID) widely marketed in South Africa for pain and inflammation. The TxGNN model ranks **hypotrichosis simplex of the scalp** as its top new-indication prediction, but there are **0 clinical trials** and **0 publications** behind it. The link is a graph-based prediction only and is not credible mechanistically.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data supplied (diclofenac is generally used as an NSAID for pain and inflammation) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Diclofenac is an NSAID and is generally understood to work by inhibiting cyclooxygenase (COX), which lowers prostaglandin-driven pain and inflammation.

The predicted disease is a monogenic hair-follicle disorder (for example, CDSN, APCDD1 or RPL21 variants). COX inhibition does not address these underlying defects. **No credible mechanistic link was identified**, and the high score reflects a knowledge-graph association, not clinical or biological support. This prediction should not be regarded as reasonable without new evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypotrichosis simplex of the scalp.

## Literature Evidence

Currently no related literature available for hypotrichosis simplex of the scalp.

## Other Predicted Candidates (Context)

Nine other candidates were predicted. Only juvenile idiopathic arthritis (JIA) has any linked evidence, and it is indirect.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 9 | Juvenile idiopathic arthritis | 99.25% | L4 | NSAIDs are a recognised symptomatic option in JIA, but there is no diclofenac-specific trial or literature. NSAIDs are not disease-modifying. |
| 8 | Diffuse alopecia areata | 99.57% | L5 | Nominal plausibility (autoimmune inflammation), but established treatments act on immune pathways, not COX. |
| 3 | Pseudoachondroplasia | 99.66% | L5 | NSAIDs might relieve joint pain, but there is no evidence of disease modification. |
| 7 | Myosclerosis | 99.60% | L5 | At most a symptomatic link, which is speculative. |
| 2, 4, 5, 6, 10 | Hunter-Thompson acromesomelic dysplasia, brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, congenital hypotrichosis milia, WHIM syndrome | 99.15–99.67% | L5 | No credible mechanistic link. |

Trials linked to JIA (both indirectly relevant, grade C):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05871086](https://clinicaltrials.gov/study/NCT05871086) | Phase 2/3 | Unknown | 60 | Coenzyme Q10 supplementation in JIA. Diclofenac is not the intervention. |
| [NCT00688545](https://clinicaltrials.gov/study/NCT00688545) | N/A (observational) | Terminated | 275 | Safety registry of celecoxib and non-selective NSAIDs in JIA. Diclofenac data are not confirmed. |

## South Africa Market Information

Diclofenac has 14 SAHPRA registrations. Registered dosage forms include tablet, sachet, suppository, injection, capsule and gel. Approved indication text was not available in the data supplied.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| A38/3.1/0651 | K-fenak otc | Tablet |
| R/3.1/0050 | Panamor At-50 | Tablet |
| A39/3.1/0588 | Cataflam | Sachet |
| U/3.1/181 | Adco-diclofenac | Tablet |
| 27/3.1/0121 | Panamor supp | Suppository |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials or literature, and the pack identifies no credible mechanistic link between COX inhibition and a monogenic hair-follicle disorder. Only JIA has any indirect signal, and there NSAIDs would be symptomatic, not disease-modifying.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (safety screening cannot proceed without them)
- Mechanism of action data (for example, from DrugBank)
- Diclofenac-specific studies in the predicted indication. For JIA, a targeted literature review of diclofenac use would be the most logical starting point.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

