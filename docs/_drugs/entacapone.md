---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease Adjunct Therapy to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT inhibitor, marketed in South Africa as part of the Stalevo levodopa/carbidopa/entacapone tablets. The registry data supplied did not record an original indication, so its use as a levodopa adjunct in Parkinson's disease comes from general pharmacology.
The TxGNN model predicts it may be useful for **PLA2G6-associated neurodegeneration**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data supplied (generally known as a levodopa adjunct in Parkinson's disease) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Entacapone is generally known as a peripheral COMT inhibitor that prolongs the effect of levodopa. It is an established adjunct in Parkinson's disease.

PLA2G6-associated neurodegeneration can include dystonia-parkinsonism, so a dopaminergic rationale is conceivable. However, the underlying defect lies in phospholipid metabolism and iron/synuclein pathology, which COMT inhibition does not address. The prediction most likely reflects proximity to Parkinson's disease in the knowledge graph rather than a demonstrated mechanism. The link cannot be checked against known pharmacology until the original indication and mechanism data are completed.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Other Predicted Indications (Top 10)

Nine other candidates were predicted. Only two have any registered study or literature, and none has direct evidence of benefit.

| Rank | Predicted Indication | Score | Evidence Level | Notes |
|------|------|------|------|------|
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L5 | Early-onset parkinsonism. Mechanistic plausibility is higher than for most other candidates, but no juvenile-specific evidence exists. |
| 7 | Lewy body dementia | 99.25% | L4 | Indirect preclinical support only ([PMID 23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/), in vitro antiparkinsonian agents and oligomer formation). The one registered trial ([NCT04246437](https://clinicaltrials.gov/study/NCT04246437), Phase 1, recruiting, n=40) is an F-DOPA imaging study in autonomic failure, not a test of entacapone. Dopaminergic side effects such as psychosis and hallucinations are a particular concern in this population. |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L5 | Poor levodopa response makes the rationale weak. The one registered study ([NCT02994719](https://clinicaltrials.gov/study/NCT02994719), N/A phase, recruiting, n=120) is a gait analysis with no entacapone intervention. |
| 2, 3, 5, 6, 8, 9 | Rasmussen encephalitis, myelitis, transaldolase deficiency, lethal infantile mitochondrial myopathy, fructose-1,6-bisphosphatase deficiency, perisylvian polymicrogyria syndrome | 99.06–99.73% | L5 | No plausible mechanistic path from COMT inhibition and no evidence found. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 8/5.4.1/0138 | Stalevo 100/25 | Tablet | Not stated in the registry data supplied |
| Reg. No. 38/5.4.1/0137 | Stalevo 150/37.5 | Tablet | Not stated in the registry data supplied |

Both products are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a model score alone, with no trials or literature. The stated mechanism (COMT inhibition) does not address the disease pathology. The SAHPRA safety data is missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is a blocking gap
- Mechanism of action and original indication data (for example from DrugBank) to test the mechanistic link
- Clinical or preclinical evidence specific to PLA2G6-associated neurodegeneration
- If pursuing a better-supported candidate, a dedicated safety and evidence review for early-onset parkinsonism or Lewy body dementia, including psychiatric risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

