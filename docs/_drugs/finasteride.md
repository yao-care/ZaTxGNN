---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 231
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Finasteride: From Androgen-Dependent Conditions to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is an oral 5-alpha reductase inhibitor. It is established for androgen-dependent hair conditions such as androgenetic alopecia.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** with a very high score, but there are **0 clinical trials** and **0 publications** for this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data; established use is androgen-dependent hair conditions |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the Evidence Pack. Finasteride is known to inhibit type II 5-alpha reductase and lower dihydrotestosterone (DHT), which reduces androgen-dependent hair growth.

The link to the predicted indication is weak. Ambras syndrome is a congenital hypertrichosis that is not androgen-driven. It is usually attributed to chromosomal rearrangements affecting TRPS1 regulation, so lowering DHT is not expected to address its cause. The very high TxGNN score reflects graph-based association, not clinical or mechanistic support. It should be read as a hypothesis-generating signal only.

### Other predictions for finasteride

| Predicted Disease | Score | Evidence Level | Assessment |
|------|------|------|------|
| Hypertrichosis (disease) | 99.99% | L4 | Hypertrichosis is non-androgen-dependent hair excess, so DHT suppression is not expected to help. Evidence is indirect. |
| Malformation syndrome with odontal and/or periodontal component | 99.99% | L5 | No plausible mechanistic link. |
| Syndrome with a Dandy-Walker malformation as major feature | 99.99% | L5 | Likely a knowledge-graph artefact. No trials or literature. |
| Isolated genetic hair shaft abnormality | 99.99% | L5 | Structural shaft defects are generally not androgen-driven. Any follicle-biology link is speculative. |
| Familial isolated trichomegaly | 99.15% | L5 | No established androgen-dependent mechanism. It has the lowest score of the six predictions. |

## Clinical Trial Evidence

Currently no related clinical trials are registered for Ambras type hypertrichosis universalis congenita.

For the closely related prediction "hypertrichosis", one trial was retrieved. It was graded low relevance (C):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04293822](https://clinicaltrials.gov/study/NCT04293822) | Phase 4 | Unknown | 60 | Topical cetirizine gel vs minoxidil 5% gel in androgenetic alopecia. It does not involve finasteride and studies hair loss, not hypertrichosis. |

## Literature Evidence

Currently no related literature is available for Ambras type hypertrichosis universalis congenita.

For the related "hypertrichosis" prediction, only general reviews were retrieved. None demonstrates finasteride efficacy in hypertrichosis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Treatment options for androgenetic alopecia, hirsutism and hypertrichosis |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | Hypertrichosis is non-androgen-dependent and usually iatrogenic or metabolic. Hormone monitoring is not warranted. |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Finasteride for male pattern hair loss and laser hair removal for hypertrichosis and hirsutism |

The 20 publications retrieved for the periodontal/odontal malformation prediction are general periodontitis papers that do not mention finasteride. They reflect keyword matching on the disease term and are not drug-specific evidence.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 48/21.12/0594 | Finasteride 1 Unicorn | Tablet |
| Reg. No. 43/21.12/0055 | Profina | Tablet |
| Reg. No. 27/21.12/0069 | Proscar | Tablet |

All three registrations are oral tablets. The approved indication text was not available in the registration data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and the mechanistic link is weak. Ambras syndrome is not androgen-driven, so DHT suppression is unlikely to help. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications, so that safety screening can begin
- Mechanism-of-action data from DrugBank
- A specific biological rationale linking 5-alpha reductase inhibition to the predicted condition, for example from preclinical or case-level data
- Expert dermatology or genetics review before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

