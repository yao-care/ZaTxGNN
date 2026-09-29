---
layout: default
title: Sodium Acetate
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
---

# Sodium Acetate
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

# Sodium Acetate: From Electrolyte and Fluid Replacement to Congenital Prothrombin Deficiency

## One-Sentence Summary

Sodium acetate is an electrolyte and alkalinizing agent. In South Africa it is registered as an ingredient in infusion, dialysis and injectable products. The TxGNN model predicts it may be useful for **congenital prothrombin deficiency**, but **0 clinical trials** and **0 publications** support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (products are infusion, dialysis and injectable fluids) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium acetate acts as a source of sodium and of bicarbonate-equivalent base (acetate is metabolised to bicarbonate). It is used in fluid replacement and dialysis solutions.

The pack finds no plausible mechanistic link to congenital prothrombin deficiency. This is an inherited coagulation disorder caused by low or dysfunctional factor II. Sodium acetate has no known role in the coagulation cascade or in prothrombin synthesis. The high score (0.9998) most likely reflects the structure of the knowledge graph rather than a drug-specific signal. It should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

## Other Predicted Indications (Context Only)

The other nine top-10 predictions are also unsupported. Some retrieved records look relevant but are not:

| Rank | Predicted Indication | Score | Evidence Level | What the Retrieved Records Show |
|------|------|------|------|------|
| 2 | Epiglottitis | 99.77% | L5 | No trials or publications. No antimicrobial rationale. |
| 3 | Urinary tract infection | 99.69% | L5 | Two trials ([NCT04302467](https://clinicaltrials.gov/study/NCT04302467), [NCT01808261](https://clinicaltrials.gov/study/NCT01808261)) and one preclinical paper ([PMID 34792197](https://pubmed.ncbi.nlm.nih.gov/34792197/)). None tests sodium acetate against UTI. |
| 4 | Sclerosing cholangitis | 99.61% | L5 | No records. |
| 5 | Gonococcal urethritis | 99.57% | L5 | No records. |
| 6 | Ureaplasma urethritis | 99.57% | L5 | No records. Its score is identical to rank 5, which suggests a shared graph neighbourhood rather than a drug-specific signal. |
| 7 | Dyspepsia | 99.56% | L4 | Six papers on gastric emptying and SCFA physiology. They likely reflect diagnostic-tracer use, not therapy. |
| 8 | Uterine inflammatory disease | 99.48% | L5 | One Phase 2 trial ([NCT00604825](https://clinicaltrials.gov/study/NCT00604825)) with no demonstrated sodium acetate link. Two papers on corticosteroids and montelukast. |
| 9 | Gastroparesis | 99.47% | L4 | Two trials and three papers. Sodium 13C-acetate is a standard gastric emptying breath-test tracer, so it was likely a measurement tool, not the treatment. |
| 10 | Xanthogranulomatous pyelonephritis | 99.46% | L5 | No records. |

For dyspepsia and gastroparesis, the literature hits most likely come from the diagnostic use of 13C-acetate. They should not be counted as therapeutic evidence.

## South Africa Market Information

Twenty registrations are on record. The five main ones are listed below. Approved indication text is not stated in the registration records, and EML inclusion status was not confirmed in the data supplied.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal Pd4 W/1.1% Amin Acid (2.5L) | Solution | Not stated in record |
| Reg. No. Y/6.1/415 | Dopamine HCl Fresenius 5ml 200mg/5ml | Injection | Not stated in record |
| Reg. No. D/24/208 | Sabax Ringer-Lactate 500ml | Solution | Not stated in record |
| Reg. No. D/24/208 | Sabax Ringer-Lactate (1000ml) | Infusion | Not stated in record |
| Reg. No. D/24/208 | Ringer-Lactate 200ml AFB2328 | Infusion | Not stated in record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug-drug interaction records were found for this ingredient.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical or literature support and no plausible mechanism. Across all ten predictions, no study tests sodium acetate as a therapy, and some of the retrieved literature is confounded by the diagnostic use of 13C-acetate. Evidence stays at L5 for the top prediction.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to test any link to coagulation
- Review of the full records of the trials retrieved for other indications, to confirm whether acetate was only a diagnostic marker
- Approved indication text for the local registrations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

