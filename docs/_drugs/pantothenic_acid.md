---
layout: default
title: Pantothenic Acid
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Pantothenic Acid
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

# Pantothenic Acid: From Ascorbic Acid Deficiency (Scurvy) to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (vitamin B5) is a coenzyme A precursor. The knowledge graph lists its original indications as ascorbic acid deficiency and scurvy.
The TxGNN model's top prediction is **congenital prothrombin deficiency**, but there are **0 clinical trials** and **0 publications** supporting it. This is a computational prediction only, with no identified mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency, scurvy (from the knowledge graph; the SAHPRA registrations carry no indication text) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pantothenic acid is a precursor of coenzyme A, a cofactor in lipid and energy metabolism. It is used as a nutritional supplement, including in parenteral nutrition products.

For the top-ranked prediction, **no plausible mechanistic link was identified**. Congenital prothrombin deficiency is a genetic coagulation factor disorder (F2 gene). Pantothenic acid does not act on prothrombin synthesis or function. The high score is a computational artefact of the knowledge graph, not a pharmacologically grounded signal.

Other predictions are weak, though a few have some indirect support:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 1 | Congenital prothrombin deficiency | 99.96% | L5 | No mechanistic link, no studies |
| 2 | Ochronosis disorder | 99.78% | L5 | Caused by homogentisate dioxygenase deficiency, with no link to CoA biosynthesis |
| 3 | Glycerol metabolism disease | 99.77% | L5 | Loosely plausible biochemistry, but the retrieved papers are metabolomics profiling only |
| 4 | Folic acid deficiency anaemia | 99.60% | L4 | Indirect historical and animal evidence; folic acid replacement is standard therapy |
| 5 | Uterine inflammatory disease | 99.14% | L4 | One 2026 mouse study; no human data |
| 6–10 | Xanthogranulomatous pyelonephritis, urinary tract infection, Ureaplasma urethritis, gonococcal urethritis, Keshan disease | 98.9–99.1% | L5 | No plausible mechanism or relevant evidence |

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

**Contraindications (knowledge graph associations, not label text):** the TxGNN knowledge graph links pantothenic acid with the following conditions as contraindications. These should be verified against the SAHPRA-approved Professional Information (PI):
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

