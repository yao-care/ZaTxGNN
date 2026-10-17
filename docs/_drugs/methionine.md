---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: No approved indication text is recorded in the SAHPRA registrations (…"
monitor_inn: "Methionine"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetes mellitus type 2 associated cataract", "immature cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "craniostenosis cataract", "tetanic cataract", "diabetic cataract"]
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

# Methionine: From Parenteral Nutrition Component to Acne (Disease)

## One-Sentence Summary

Methionine is an essential sulfur-containing amino acid. In South Africa it is registered only as an ingredient of multi-component amino acid products, such as peritoneal dialysis solutions and parenteral nutrition infusions.
The TxGNN model predicts it may be effective for **acne (disease)**, with a very high score, but **no clinical trials** and only **2 indirect publications** support this direction.
The evidence is model-driven, so the recommendation is to **hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is recorded in the SAHPRA registrations (nutritional or amino acid supply as a component of infusion products) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.9996% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, methionine is an essential amino acid that is part of amino acid and parenteral nutrition products. It is central to the methionine-homocysteine cycle. No established link has been shown between this role and acne.

The two publications retrieved are indirect and do not support a therapeutic benefit:

- One cohort study (PMID 11277950) found raised plasma homocysteine in patients taking isotretinoin for cystic acne. This touches the methionine-homocysteine axis but does not show that methionine treats acne.
- One case report (PMID 39357918) describes a neonate with an MTHFR mutation, encephalopathy and neonatal acne. It is not relevant to treating acne.

Methionine supplementation can raise homocysteine, which would be an unfavourable direction. The very high TxGNN score therefore cannot be taken as evidence of benefit.

Other predicted indications are also supported only by the model or by indirect preclinical work. The most notable is **diabetic cataract** (TxGNN score 99.999%, evidence level L4). Its evidence centres on methionine sulfoxide reductase B1 (MsrB1), which repairs oxidised methionine in lens epithelial cells. This supports a mechanistic research question about methionine sulfoxide reductase pathways, not a methionine therapy. Several cataract subtypes and severe non-proliferative diabetic retinopathy were also predicted, with no clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Elevated plasma homocysteine in patients on isotretinoin for cystic acne. Relates to the methionine-homocysteine axis but does not show benefit of methionine. |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Rep | Novel MTHFR mutation in a neonate with encephalopathy, hair loss, marfanoid features and neonatal acne. Not relevant to acne treatment. |

---

## South Africa Market Information

Methionine is registered only as a component of multi-ingredient infusion products. No approved indication text is available in the data compiled for this report. Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not recorded |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not recorded |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not recorded |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not recorded |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not recorded |

A further 5 registrations are not shown here: Adco-ipratropium (ni201), Numeta G16E, Smofkabiven, Nutriflex Omega Specialized and Nutriflex lipid special 625ml. All 10 registrations are valid single-entity entries.

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
The TxGNN knowledge graph links methionine with the following conditions as possible contraindications. These are model-derived and must be confirmed against the product label.

- Cardiovascular: hypertension, hypertensive disorder, heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
- Renal: kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure, nephrolithiasis (including SLC26A1-related susceptibility), nephrocalcinosis, acute urate nephropathy, pyoureter
- Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia, familial hyperlipidaemia, phosphorus metabolism disease, phenylketonuria, disorder of phenylalanine metabolism
- Calcium-related: hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis

**Drug interactions (5 recorded, DDInter):**

| Interacting Drug | Severity |
|------|------|
| Activated charcoal | Moderate |
| Ephedrine | Minor |
| Pseudoephedrine | Minor |
| Mexiletine | Minor |
| Flecainide | Minor |

**Additional consideration:** Methionine supplementation can raise homocysteine, which is itself implicated in vascular and ocular disease.

For warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI) of the relevant product. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no clinical trials, and the two publications are indirect, with no evidence that methionine treats acne. Possible homocysteine elevation points in an unfavourable direction.

**To proceed, the following is needed:**
- Mechanism of action data for methionine and a defined mechanistic link to acne pathophysiology
- Evidence from preclinical or clinical studies testing methionine directly in acne
- Review of the SAHPRA package inserts for warnings and contraindications of the relevant products
- Assessment of route and formulation feasibility, since methionine is currently marketed only in infusion products
- If the eye indications are pursued, reframe diabetic cataract as a mechanistic research question on methionine sulfoxide reductase pathways, not as a methionine therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

