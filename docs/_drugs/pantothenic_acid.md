---
layout: default
title: Pantothenic Acid
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
monitor_inn: "Pantothenic acid"
predicted_indications: ["congenital prothrombin deficiency", "ochronosis disorder", "glycerol metabolism disease", "folic acid deficiency anemia", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urinary tract infection (disease)", "gonococcal urethritis", "Ureaplasma urethritis"]
description: "Pantothenic Acid: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Pantothenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pantothenic Acid: Congenital prothrombin deficiency
{: .text-alpha }

## One-Sentence Summary

Pantothenic acid (vitamin B5) is a coenzyme A precursor. Its original indications are listed as ascorbic acid deficiency and scurvy.
The TxGNN model's top prediction is **congenital prothrombin deficiency**, but there are **0 clinical trials** and **0 publications** supporting it. This is a computational prediction only, with no identified mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 3 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pantothenic acid is a precursor of coenzyme A, a cofactor in lipid and energy metabolism. It is used as a nutritional supplement, including in parenteral nutrition products.

For the top-ranked prediction, **no plausible mechanistic link was identified**. Congenital prothrombin deficiency is a genetic coagulation factor disorder (F2 gene). Pantothenic acid does not act on prothrombin synthesis or function. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions are weak, though a few have some indirect support:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 1 | Congenital prothrombin deficiency | 0.9996 | L5 | No mechanistic link, no studies |
| 2 | Ochronosis disorder | 0.9978 | L5 | Caused by homogentisate dioxygenase deficiency, with no link to CoA biosynthesis |
| 3 | Glycerol metabolism disease | 0.9977 | L5 | Loosely plausible biochemistry, but the retrieved papers are metabolomics profiling only |
| 4 | Folic acid deficiency anaemia | 0.9960 | L4 | Indirect historical and animal evidence; folic acid replacement is standard therapy |
| 5 | Uterine inflammatory disease | 0.9914 | L5 | One 2026 mouse study; no human data |
| 6–10 | Xanthogranulomatous pyelonephritis, urinary tract infection, Ureaplasma urethritis, gonococcal urethritis, Keshan disease | 98.9–0.9910 | L5 | No plausible mechanism or relevant evidence |

The two most credible research directions are **folic acid deficiency anaemia** (B-vitamin interrelationships) and **uterine inflammatory disease** (preclinical anti-inflammatory signal). Both remain hypothesis-level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency or any of the other nine predicted indications.

---

## Literature Evidence

No literature was retrieved for congenital prothrombin deficiency. The most relevant publications for the other predicted indications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41223999](https://pubmed.ncbi.nlm.nih.gov/41223999/) | 2026 | Preclinical (mouse) | Mucosal Immunology | Pantothenic acid alleviated vagotomy-induced endometrial injury (uterine inflammatory disease) |
| [3724048](https://pubmed.ncbi.nlm.nih.gov/3724048/) | 1986 | Review | Laboratory Animal Science | Review of nutritional deficiency anaemias in nonhuman primates, including pantothenic acid and folic acid (folic acid deficiency anaemia) |
| [21021037](https://pubmed.ncbi.nlm.nih.gov/21021037/) | 1946 | Historical report | Nutrition Reviews | Anaemia and granulocytopenia in relation to pantothenic acid and folic acid deficiencies (folic acid deficiency anaemia) |
| [21929634](https://pubmed.ncbi.nlm.nih.gov/21929634/) | 2011 | Review | Maternal & Child Nutrition | Fortified foods in pregnancy and lactation and nutritional status (folic acid deficiency anaemia; indirect) |

The five papers retrieved for glycerol metabolism disease are metabolomics, microbiome or biomarker profiling studies (including rat, mouse, dairy cow and human plasma/faecal studies). None tests pantothenic acid as a treatment. The two papers retrieved for urinary tract infection are off-topic (a transporter deficiency report and a zoledronic acid case report). They are not used as evidence.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| U/22.1.4/200 | Soluvit novum 10ml vials | Injection | Not stated in the data compiled |
| L/24/329 | Dextrose 20% in water 500ml | Infusion | Not stated in the data compiled |
| Exclusion under Section 36 & Section 14 | ITN neonatal TPN 150ml | TPN | Not stated in the data compiled |

All three registrations are valid single-ingredient entries, and all are injectable or parenteral products. The data compiled for this report do not include Essential Medicines List (EML) status.

---

## Safety Considerations

**Contraindications (TxGNN model associations, not label text):** the TxGNN model (deep learning) links pantothenic acid with the following conditions as contraindications. This may reflect similarities the model learned between related diseases, not biological evidence. These should be verified against the SAHPRA-approved Professional Information (PI):
- Kidney disease
- Pyoureter
- Sickle cell anaemia
- Hereditary persistence of fetal haemoglobin
- Primary hyperoxaluria
- Hereditary haemochromatosis
- Haemosiderosis
- Iron metabolism disease
- Wilson disease

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interactions. No drug interaction records were found. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, congenital prothrombin deficiency, rests on a high TxGNN score alone. There are no trials or publications, and pantothenic acid has no known effect on prothrombin synthesis or function. The evidence level is L5, and the marketed products are nutritional or parenteral formulations with no related approved indication.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable) and a biological rationale for the prothrombin link
- SAHPRA PI warnings and contraindications, to reconcile with the knowledge-graph contraindications
- If a lead is wanted, redirect effort to the better-supported hypotheses: folic acid deficiency anaemia (controlled human data) and uterine inflammatory disease (further preclinical validation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

