---
layout: default
title: Nicotinamide
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Nicotinamide
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

# Nicotinamide: From Vitamin B Supplementation to Elevated Plasma Zinc

## One-Sentence Summary

Nicotinamide (vitamin B3) is registered in South Africa mainly in vitamin B-complex and multivitamin products, and the registry records no formal indication text for it. The TxGNN model predicts it may be useful for **elevated plasma zinc**, but the **10 clinical trials** and **2 publications** retrieved do not test nicotinamide for this condition. The prediction is model-only and unsupported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registry data. Registered products are vitamin B-complex and multivitamin preparations |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 97.83% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nicotinamide is the amide form of vitamin B3 and a precursor of NAD+ through the salvage pathway. It is used as a nutritional supplement in vitamin B-complex products.

No clear mechanistic link between nicotinamide and lowering plasma zinc was found. The high TxGNN score is not supported by the retrieved evidence. The trials and papers concern nutrition, obesity or zinc deficiency, not elevated zinc treated with nicotinamide. This prediction should be treated as a model output only.

---

## Clinical Trial Evidence

All 10 trials retrieved were graded C (low relevance). None tests nicotinamide for elevated plasma zinc. No SANCTR or PACTR records were identified.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06975241](https://clinicaltrials.gov/study/NCT06975241) | Phase 4 | Recruiting | 64 | EPA-to-DHA conversion rates by sex and genotype in healthy adults. Not related to nicotinamide or zinc |
| [NCT06457412](https://clinicaltrials.gov/study/NCT06457412) | N/A | Recruiting | 200 | Lifestyle programme for childhood obesity |
| [NCT04413604](https://clinicaltrials.gov/study/NCT04413604) | N/A | Terminated | 29 | Vitamin D, zinc and iron status in children given young children's milk |
| [NCT04612088](https://clinicaltrials.gov/study/NCT04612088) | N/A | Unknown | 34 | Behavioural intervention for multivitamin adherence after bariatric surgery |
| [NCT06317883](https://clinicaltrials.gov/study/NCT06317883) | N/A | Active, not recruiting | 1508 | Observational study of childhood obesity risk factors |
| [NCT03866837](https://clinicaltrials.gov/study/NCT03866837) | N/A | Completed | 288 | Prebiotic GOS and lactoferrin with iron supplements in Kenyan infants |
| [NCT04641663](https://clinicaltrials.gov/study/NCT04641663) | N/A | Unknown | 70 | Tolerability of a multi-ingredient supplement in older adults |
| [NCT02989311](https://clinicaltrials.gov/study/NCT02989311) | N/A | Completed | 23 | Iron absorption from a micronutrient powder in African infants |
| [NCT06081114](https://clinicaltrials.gov/study/NCT06081114) | N/A | Active, not recruiting | 643 | Micronutrient dose-response in women in Bangladesh (deficiency, not excess) |
| [NCT02428647](https://clinicaltrials.gov/study/NCT02428647) | N/A | Completed | 3433 | Preventive vs therapeutic zinc supplementation in Lao children (zinc deficiency) |

---

## Literature Evidence

Neither publication evaluates nicotinamide for elevated plasma zinc.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32938758](https://pubmed.ncbi.nlm.nih.gov/32938758/) | 2020 | Review | Open Heart | Hyperinsulinaemia, magnesium, vitamin D and thrombosis in COVID-19. Only tangentially related |
| [15361776](https://pubmed.ncbi.nlm.nih.gov/15361776/) | 2004 | Preclinical (animal) | J Hypertens | Antioxidant enzymes in the kidneys of hypertensive rats on an antioxidant-rich diet. Mentions NADPH oxidase only, not nicotinamide therapy |

---

## South Africa Market Information

Showing 5 of 20 registrations. The registry data does not state approved indications or manufacturers, and Essential Medicines List status is not available in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2611 (Act 101/1965) | Becoplex Ido vial 10ml | Injection | Not stated in registry data |
| H2412 (Act 101/1965) | A-Lennon Vitamin B Co ampoule 2ml | Injection | Not stated in registry data |
| H2975 (Act 101/1965) | Vitamin B Co 10ml | Injection | Not stated in registry data |
| U/2.6/218 | Restin | Capsule | Not stated in registry data |
| U/22.1.4/200 | Soluvit Novum 10ml vials | Injection | Not stated in registry data |

Other registered forms include infusion, TPN and inhaler presentations.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug-interaction records were found for nicotinamide in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 97.83% TxGNN score is not backed by any trial or publication testing nicotinamide for elevated plasma zinc. All 10 trials are unrelated, and the evidence is model prediction only (L5).

**To proceed, the following is needed:**
- A plausible mechanism linking nicotinamide to plasma zinc, plus the mechanism of action data from DrugBank
- SAHPRA Professional Information (warnings and contraindications), needed before any safety screening
- Confirmation of the approved indications for each registered product
- Any clinical or biochemical study of nicotinamide and zinc handling

**Other predictions to note:**
Of the ten predicted indications, **Werner syndrome** (rank 4) has the strongest support (L4, "Research Question"). It has preclinical NAD+ data and a 2025 double-blind crossover trial of nicotinamide riboside (PMID 40459998). Nicotinamide riboside is a related NAD+ precursor, not nicotinamide itself, and the trial design was inferred from the title and should be confirmed. It would be the better candidate for follow-up, once nicotinamide-specific efficacy and safety data are obtained.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

