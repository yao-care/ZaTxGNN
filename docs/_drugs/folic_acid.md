---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 239
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "FOLIC ACID"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Folic Acid: From Vitamin Deficiency and Folate-Deficiency Anaemia to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (vitamin B9) is originally used to treat vitamin deficiency disorders and anaemias, particularly folic acid deficiency anaemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but there are **no registered clinical trials** and the **20 publications** retrieved are mostly general reviews on vitamins, none of which directly test folic acid in this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anaemia; iron deficiency anaemia; hypochromic and microcytic anaemia (SAHPRA registrations contain no indication text) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only; the supporting literature is indirect and does not test folic acid in this condition) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Folic acid is a water-soluble B vitamin that serves as a cofactor in one-carbon metabolism (including DNA synthesis and homocysteine-to-methionine conversion). Its efficacy in folate-deficiency anaemia is well established.

Folic acid and biotin (vitamin B7) are both water-soluble B vitamins, and vitamin-responsive disorders are often discussed together in the literature (for example, a review covering cobalamin, folate, biotin, B1 and E). This shared grouping is likely what drives the high prediction score.

However, the link is weak. Folic acid cannot replace biotin as a carboxylase cofactor. No direct mechanism is established by which folic acid would correct a primary biotin metabolic defect such as biotinidase deficiency or holocarboxylase synthetase deficiency. The score most likely reflects proximity in the vitamin/metabolic network rather than a validated therapeutic mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Of the 20 publications retrieved, none is an RCT. Most are narrative reviews or general vitamin studies. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Covers vitamin-responsive disorders (cobalamin, folate, biotin, B1, E). Folate and B12 deficiency present with megaloblastic anaemia and neurological signs, and rare inborn errors of vitamin metabolism are described. |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Vitamin B12 deficiency and the nervous system. Notes B12 and biotin share metabolic pathways (succinyl-CoA synthesis), and B12 and folate share methionine synthesis. |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Reviews vitamins in inborn metabolic errors and vitamin-dependent syndromes, which may need pharmacological rather than nutritional doses. |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Arch Biochem Biophys | Micronutrient deficiencies (including B12, folic acid, B6) may damage DNA, supporting optimal micronutrient intake. |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clin Dermatol | Overview of B vitamins in cellular metabolism and erythrocyte synthesis. |
| [39828265](https://pubmed.ncbi.nlm.nih.gov/39828265/) | 2025 | Umbrella review | Asia Pac J Clin Nutr | Water-soluble vitamins and glycaemic control in type 2 diabetes. Indirect to the predicted indication. |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Combined biotin and folic acid deficiency induced in rats on a purified diet with phthalylsulfathiazole. |

These publications address vitamins in general. None demonstrates that folic acid treats biotin metabolic disease.

---

## South Africa Market Information

All 11 registrations are valid single-ingredient entries. No approved-indication text is recorded for any of them. The five main ones are listed below. Essential Medicines List (EML) status was not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A40/22.2/0592 | Gulf folic acid | Tablet | Not recorded |
| H0689 (ACT 101/1965) | Autrin | Capsule | Not recorded |
| H2466 | Complenatal FF | Capsule | Not recorded |
| H2062 (ACT 101) | Filibon | Capsule | Not recorded |
| 36/22.1/0508 | Cernevit | Infusion | Not recorded |

The remaining six include Soluvit Novum (injection), Gericomplex (capsule), Linctifed wet cough (syrup), Dextrose 20% in water (infusion), ITN neonatal TPN, and Spiriva Respimat (inhaler). Several of these entries look like multivitamin or parenteral nutrition products, and some (Linctifed, Spiriva) are unlikely to contain folic acid as a relevant active ingredient. The registration mapping should be verified against the SAHPRA register.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not from label text):** The TxGNN knowledge graph links folic acid to contraindication relationships with several conditions, including:
- Haematological: sickle cell anaemia, haemolytic anaemia, hereditary haemochromatosis, haemosiderosis
- Renal and metabolic: kidney disease, nephrolithiasis, nephrocalcinosis, primary hyperoxaluria, hypercalcaemia, hyperparathyroidism, diabetic ketoacidosis, diabetes mellitus
- Gastrointestinal: peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, diarrhoeal disease, constipation
- Other: bipolar disorder, sarcoidosis, Wilson disease

These graph edges may be noisy or reflect other compounds, and should not be read as label contraindications. Verify them against the approved Professional Information.

**Drug Interactions:** The interaction check returned 100 entries. The main ones with a graded severity are:
- Pancrelipase: Moderate
- Sulfasalazine: Minor

Many other entries have no severity grade, including pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, mesalazine, prednisone and simvastatin.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model score and general vitamin-group proximity. There are no registered trials, and no publication tests folic acid in biotin metabolic disorders. Folic acid does not substitute for biotin as a cofactor, and the label safety data needed for screening is missing.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data to assess a plausible link
- Targeted evidence on folic acid in biotinidase or holocarboxylase synthetase deficiency, or biotin-related metabolic disease
- Clarification of whether the prediction reflects a real therapeutic opportunity or a network artefact
- Verification of the SAHPRA product-to-active-ingredient mapping and approved indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

