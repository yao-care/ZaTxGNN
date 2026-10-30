---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "immature cataract", "tetanic cataract", "mature cataract", "cortical cataract", "craniostenosis cataract", "nuclear senile cataract", "diabetes mellitus type 2 associated cataract", "diabetic cataract"]
last_modified_at: 2026-10-30
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not stated in the licence records (the registered products are parent…"
---

# Methionine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methionine: From Parenteral Nutrition Components to Acne (Disease)
{: .text-alpha }

## One-Sentence Summary

Methionine is an essential sulphur-containing amino acid. In South Africa it is registered only as an ingredient of parenteral nutrition and dialysis solutions, and no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **acne (disease)**, but there are **0 clinical trials** and only **2 publications**, neither of which tests methionine as a treatment.
This is a model prediction only (evidence level L5) and the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (the registered products are parenteral nutrition and peritoneal dialysis solutions; no indication text is available) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 9 of 10) |
| Number of SAHPRA Registrations | 10 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methionine is an essential amino acid that supplies sulphur and methyl groups. It is a precursor of homocysteine and, through the transsulfuration pathway, of cysteine and glutathione.

The two papers retrieved for acne both concern homocysteine, not methionine treatment. One reports raised plasma homocysteine in patients on isotretinoin for cystic acne. The other is a case report of an MTHFR mutation in a neonate, where neonatal acne was one of several skin findings. Methionine sits on the same metabolic pathway, so the link is biologically adjacent. However, supplementation could raise homocysteine, which argues against benefit rather than for it.

The TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases. It is not biological evidence that methionine treats acne.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Plasma homocysteine was elevated in patients taking isotretinoin for cystic acne. This describes a side-effect marker, not methionine efficacy. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Neonate with a novel MTHFR mutation, encephalopathy, hair loss and marfanoid features; neonatal acne was one of several skin findings. |

Neither paper studies methionine as an acne therapy.

---

## South Africa Market Information

All 10 registrations are valid single-entry records. No approved indication text is available for any of them. The data compiled for this report do not show Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated |

Five further registrations are on file: Numeta G13E, Numeta G16E, Smofkabiven, Nutriflex Omega Specialized and Nutriflex lipid special 625ml. These products are mostly multi-component nutrition and dialysis preparations, so their licences do not describe a stand-alone methionine product.

---

## Safety Considerations

**Contraindication relations recorded in the knowledge graph** (these come from the TxGNN knowledge graph, not from label text):
- Cardiovascular: hypertension, hypertensive disorder, heart disease, cardiovascular disease, hyperlipidaemia, familial hyperlipidaemia, digitalis poisoning, ventricular fibrillation
- Renal: kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hypercalcaemia, humoral hypercalcaemia of malignancy, phosphorus metabolism disease, sarcoidosis, phenylketonuria and other disorders of phenylalanine metabolism

**Drug interactions** (DDInter, 5 recorded):
- Moderate: activated charcoal
- Minor: ephedrine, pseudoephedrine, mexiletine, flecainide

Label-based warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is based on the model alone (L5). There are no clinical trials, and the two publications address homocysteine rather than methionine treatment of acne.
- Methionine supplementation could raise homocysteine, and the knowledge graph records several cardiovascular and renal contraindication relations. Together these argue against moving forward without supporting data.

**To proceed, the following is needed:**
- Studies that test methionine, or a related sulphur amino acid, directly in acne
- Mechanism of action data for methionine
- Approved indication text and safety sections from the SAHPRA Professional Information for the registered products
- A review of homocysteine effects and the cardiovascular and renal risks in the intended population

---

## Other Predicted Indications (for reference)

All other predictions are also at evidence level L5 or lower in practical value, except where noted.

| Predicted Indication | TxGNN Score | Evidence Level | Notes |
|------|------|------|------|
| Severe nonproliferative diabetic retinopathy | 1.0000 | L5 | No trials or literature |
| Immature, tetanic, craniostenosis and diabetes type 2 associated cataract | 1.0000 | L5 | No trials or literature |
| Mature cataract | 1.0000 | L5 | One in vitro crystallin study; no methionine therapy data |
| Cortical cataract | 1.0000 | L5 | Mechanistic and observational papers on lens oxidation only |
| Nuclear senile cataract | 1.0000 | L5 | Lens protein oxidation models; no methionine therapy data |
| Diabetic cataract | 1.0000 | L5 | See below |

For diabetic cataract, the supporting literature is the most relevant of all the predictions. Two studies show that methionine sulfoxide reductase B1 protects human lens epithelial cells from high-glucose and peroxynitrite damage, and a review links homocysteine to eye disease. However, all of it is preclinical or observational and none tests methionine itself, so the evidence level stays at L5. It is the most reasonable research question among these predictions, but not a basis for a treatment decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

