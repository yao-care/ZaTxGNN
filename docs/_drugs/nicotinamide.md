---
layout: default
title: Nicotinamide
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nicotinamide: predicted new indication Elevated plasma zinc (evidence level L5). Approved use: Acne, pellagra, beriberi"
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

# Nicotinamide: From Acne to Werner Syndrome

## One-Sentence Summary

Nicotinamide (vitamin B3) is originally used for acne, pellagra and beriberi.
The TxGNN model predicts it may be effective for **elevated plasma zinc** (the top-ranked prediction, score 97.8%), but this prediction has **no supporting clinical trials and no relevant publications**.
The best-supported prediction in the data compiled for this report is **Werner syndrome** (rank 4), which has **1 randomised trial of a related compound (nicotinamide riboside)** and several mechanistic studies. This is discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, pellagra, beriberi (from the TxGNN knowledge graph; SAHPRA indication text is not available in the data compiled for this report) |
| Predicted New Indication | Elevated plasma zinc (rank 1); Werner syndrome is the best-supported alternative (rank 4) |
| TxGNN Prediction Score | 97.83% (elevated plasma zinc); 88.61% (Werner syndrome) |
| Evidence Level | L5 (elevated plasma zinc); L2 (Werner syndrome, indirect) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold (elevated plasma zinc); Werner syndrome is a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, nicotinamide is an NAD+ precursor and a form of vitamin B3. It is used in conditions linked to B3 deficiency (pellagra) and in acne, where it has anti-inflammatory activity.

**Elevated plasma zinc (rank 1):** No clear mechanistic link to nicotinamide has been established. The two retrieved papers concern hyperinsulinaemia, magnesium and vitamin D in COVID-19, and antioxidant enzymes in hypertensive rat kidney. Neither addresses plasma zinc. The high score is a model prediction only and lacks clinical support.

**Werner syndrome (rank 4):** This is a more plausible candidate. Werner syndrome is a rare premature-ageing disease caused by WRN gene mutations. Patients show depleted NAD+, including in mitochondria, with impaired mitophagy. Preclinical work showed that NAD+ augmentation restored mitophagy and limited accelerated ageing. A 2025 double-blind crossover trial of **nicotinamide riboside** in Werner syndrome patients provides clinical support. Nicotinamide riboside is a related NAD+ precursor, not nicotinamide itself, so the evidence for this drug is indirect.

Other lower-ranked predictions are largely unsupported. Mitochondrial oxidative phosphorylation disorders are biologically plausible but have only indirect review-level evidence. PAPA syndrome likely reflects the shared acne association. Dyspepsia has no credible link, and GI upset is a known adverse effect of high-dose niacin-family compounds.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No registered trial appears for the top prediction or for Werner syndrome in the data compiled for this report.

---

## Literature Evidence

**Elevated plasma zinc (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32938758](https://pubmed.ncbi.nlm.nih.gov/32938758/) | 2020 | Review | Open Heart | Hyperinsulinaemia, magnesium, vitamin D and thrombosis in COVID-19; does not address plasma zinc |
| [15361776](https://pubmed.ncbi.nlm.nih.gov/15361776/) | 2004 | Preclinical (animal) | J Hypertens | Antioxidant enzymes in the kidney of hypertensive rats; not relevant to plasma zinc |

**Werner syndrome (rank 4, best-supported prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40459998](https://pubmed.ncbi.nlm.nih.gov/40459998/) | 2025 | RCT | Aging Cell | Double-blind randomised crossover placebo-controlled trial of nicotinamide riboside in Werner syndrome patients (related compound, not nicotinamide) |
| [31754102](https://pubmed.ncbi.nlm.nih.gov/31754102/) | 2019 | Preclinical (mechanistic) | Nat Commun | NAD+ augmentation restored mitophagy and limited accelerated ageing in Werner syndrome models |
| [40179319](https://pubmed.ncbi.nlm.nih.gov/40179319/) | 2025 | Preclinical (cell) | Aging | Mitochondrial NAD+ is decreased in WRN-deficient cells, linked to dysfunctional proliferation |
| [34201700](https://pubmed.ncbi.nlm.nih.gov/34201700/) | 2021 | Review | Int J Mol Sci | DNA damage-induced neurodegeneration in accelerated ageing diseases, including Werner syndrome |
| [42701765](https://pubmed.ncbi.nlm.nih.gov/42701765/) | 2026 | Review | Aging Med | Mechanisms of biological ageing guiding translational research, including Werner syndrome |
| [38184705](https://pubmed.ncbi.nlm.nih.gov/38184705/) | 2024 | Preclinical (cell) | Cell Biosci | WRN loss accelerates abnormal adipocyte metabolism |

**Other predictions:** Literature for dyspepsia (rank 7) is off-target (gastric cancer cells, a betaine glucuronate combination in NASH, silkworm hypervitaminosis, a genetic variant study and two 1960s reports). Literature for mitochondrial OXPHOS disorders (rank 8) consists of reviews and a zygote transcriptomics study. Neither shows a nicotinamide benefit. No literature was found for the remaining predictions (ranks 2, 3, 5, 6, 9, 10).

---

## South Africa Market Information

All 11 registrations are valid single-ingredient entries. Approved indication text is not available in the data compiled for this report, and Essential Medicines List status could not be determined from it. The first 5 registrations are shown.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2611 (ACT 101/1965) | Becoplex ido vial 10ml | Injection | Not available |
| H2412 (ACT 101/1965) | A-lennon vitamin b co ampoule 2ml | Injection | Not available |
| H2975 (ACT 101/1965) | Vitamin b co 10ml | Injection | Not available |
| U/2.6/218 | Restin | Capsule | Not available |
| U/22.1.4/200 | Soluvit novum 10ml vials pds000010 | Injection | Not available |

Other registrations include infusion, TPN and capsule products (for example Cernevit and Gericomplex). One entry appears under Spiriva respimat inhaler, which looks unusual for nicotinamide and should be verified against SAHPRA records.

---

## Safety Considerations

**Contraindication signals (knowledge-graph associations, not label text):** Associated conditions include kidney disease, liver disease, gallbladder disease, peptic ulcer disease, diabetes mellitus, diabetic ketoacidosis, gout, blood coagulation disease, hemophilia, acute coronary syndrome, hypotensive disorder, thyroid gland disease, rhabdomyolysis, sickle cell anaemia, Wilson disease, hereditary hemochromatosis and other iron metabolism disorders. These need verification against the approved Professional Information (PI).

**Drug interactions:** 64 interactions were recorded. Most listed are Moderate and include:
- Antidiabetic agents: metformin, acarbose, pioglitazone, chlorpropamide, DPP-4 inhibitors (alogliptin, linagliptin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin) and GLP-1 agonists (albiglutide, dulaglutide). Glycaemic monitoring is advisable.
- Oncology agents: asparaginase products, brentuximab vedotin, clofarabine, methotrexate.
- Others: efavirenz, cannabidiol, and carbamazepine (Minor).

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and labelled contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (elevated plasma zinc and most other predictions). **Werner syndrome: Research Question.**

**Rationale:**
- The top-ranked prediction, elevated plasma zinc, is supported only by the model score, with no plausible mechanism and no relevant evidence. Werner syndrome has a credible NAD+-depletion rationale and a small 2025 randomised trial, but that trial used nicotinamide riboside, not nicotinamide, and the disease is very rare.

**To proceed, the following is needed:**
- Full review of the 2025 Werner syndrome trial (PMID 40459998), including dose, outcomes and safety, to judge whether it extends to nicotinamide.
- Mechanism of action data for nicotinamide from DrugBank.
- SAHPRA package insert warnings and contraindications, which are currently missing and block safety screening.
- Verification of the SAHPRA indications and the Spiriva-linked entry.
- Review of the diabetes-related interactions and the kidney, liver and peptic ulcer signals for any target population.
- Registered trials or a prospective study for any prioritised indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

