---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Levodopa
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine-replacement medicine, used mainly for Parkinson's disease and marketed in South Africa in several combination products.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The high score is a graph-based prediction only, with no mechanistic rationale identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (standard use of levodopa products; the SAHPRA indication text was not captured in the source data) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Levodopa is known to act as a dopamine precursor, and its efficacy in parkinsonism is well established.

Rasmussen encephalitis is an immune-mediated inflammatory disease that affects one brain hemisphere. Dopamine replacement has no established role in it, so this prediction has **no clear mechanistic link**. No trials or publications were retrieved for this pairing. The high TxGNN score most likely reflects patterns in the knowledge graph rather than a biologically supported new use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications With More Evidence

The same Evidence Pack contains other predictions with more support than the top-ranked one. All are symptomatic (dopaminergic) rationales, not disease modification.

| Predicted Indication | TxGNN Score | Evidence Level | Key Points |
|------|------|------|------|
| PLA2G6-associated neurodegeneration | 98.75% | L3 | Case series and reviews report levodopa-responsive parkinsonism, but the response is often partial and wanes over time. Several retrieved papers concern other NBIA genes and are only indirectly relevant. |
| Lewy body dementia | 97.25% | L4 | Reviews and consensus reports discuss levodopa for motor features. There is no direct levodopa RCT, and dopaminergic therapy may worsen hallucinations. |
| Multiple system atrophy, parkinsonian type | 97.02% | L4 | Reviews and case reports show modest, non-sustained benefit. One Phase 1/2 trial ([NCT06831500](https://clinicaltrials.gov/study/NCT06831500), recruiting) examines the carbidopa/levodopa ratio on orthostatic hypotension. Its intervention needs verification. |
| Progressive supranuclear palsy-corticobasal syndrome | 97.58% | L4 | Only reviews and non-interventional or device studies. Response is usually poor or transient. |
| Paralysis agitans, juvenile, of Hunt | 98.03% | L5 | Biologically plausible, but likely a synonym or ontology overlap with Parkinson's disease. Needs manual disease-term review. |

The remaining predictions (myelitis, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency, X-linked intellectual disability-ataxia-apraxia syndrome) have no mechanistic link or only indirect evidence.

## South Africa Market Information

Six SAHPRA registrations were found. The five main ones are listed below; approved indication text was not available in the source data.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 32/5.4.1/0081 | Teva carbi-levo 25/100 | Tablet |
| Reg. No. 31/5.4.1/0194 | Madopar HBS 100mg/25mg | Capsule |
| Reg. No. 45/5.4.1/0765 | Lecardop 25/100 | Tablet |
| Reg. No. R/3.1/50 | Panamor AT | Tablet |
| Reg. No. 8/5.4.1/0138 | Stalevo 100/25 | Tablet |

All available products are oral (tablet or capsule).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) has no trials, no literature and no plausible mechanism. It is a model output only (L5) and should not be pursued.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Manual review of the disease-term mapping, especially for "paralysis agitans, juvenile, of Hunt"
- If the team wants to advance a levodopa candidate, consider PLA2G6-associated neurodegeneration, Lewy body dementia or MSA-P as research questions instead. Each needs prospective evidence beyond case series and reviews.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

