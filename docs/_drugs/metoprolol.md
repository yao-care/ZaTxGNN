---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 6
monitor_inn: "METOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-29
description: "Metoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Metoprolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker whose relations recorded in the knowledge graph include hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** directly study this condition, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; the local registration record contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, metoprolol blocks beta-1 adrenergic receptors. This lowers heart rate, cardiac output and renin release. The association of the drug with hypertension in the TxGNN model (deep learning) may reflect similarities the model learned between related diseases, not biological evidence.

Malignant hypertensive renal disease is kidney injury caused by severely uncontrolled blood pressure. Its score of 0.9991 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. A high score of this kind is not independent clinical evidence.

Malignant hypertension is usually managed with rapid, titratable intravenous agents, not oral metoprolol. This weakens the practical case for the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H/5.2/72 | Lopresor | Tablet (oral) | Not stated in the registration record |

This is a single-ingredient product, currently valid. Essential Medicines List status is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication-type relations recorded in the knowledge graph** (these are graph relations, not label text) include:
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, gout, hyperuricaemia, potassium deficiency, hypercalcaemia, hyperparathyroidism
- Liver and pancreas: liver disease, hepatic encephalopathy, pancreatitis, gallbladder disease
- Neuromuscular: myasthenia gravis
- Other: phaeochromocytoma, hypotensive disorder, systemic lupus erythematosus, psoriasis, anuria

**Drug interactions** (DDInter, 100 recorded in total; examples):
- Moderate: epinephrine, bupropion, morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, and several corticosteroids and anticholinergics
- Minor: acetylsalicylic acid, magnesium oxide

For label-based warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Other Predicted Indications (for context)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension (lung disease/hypoxia) | 0.9991 | L5 | No mechanistic rationale; theoretical risk of worsening right heart function. The retrieved publications do not address this use. |
| Pulmonary hypertension, unclear multifactorial mechanism | 0.9991 | L5 | Prediction only, no studies |
| Braddock syndrome | 0.9989 | L5 | No mechanistic link or studies |
| Chronic pulmonary heart disease | 0.9940 | L5 | Trials and publications concern heart failure with COPD, not this disease (see below) |
| Trichotillomania | 0.9905 | L5 | No mechanistic link or studies |

Rank 5 (chronic pulmonary heart disease) has related studies, but none directly studies the disease itself. They address metoprolol in heart failure with COPD, including the terminated Phase 3 BLOCK-COPD trial (NCT02587351), where metoprolol did not reduce COPD exacerbations, and the not-yet-recruiting Phase 4 trial NCT06825728. The rationale text assigned L3, but under the evidence ceiling rule it is L5. These studies are useful mainly as safety context for beta-blockers in chronic lung disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no supporting trials or publications, and its score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Oral metoprolol is not a standard approach for malignant hypertension. Safety data from the SAHPRA label is also missing.

**To proceed, the following is needed:**
- A review of the SAHPRA Professional Information for warnings and contraindications (this step is currently blocking)
- Mechanism of action data from DrugBank
- A literature and trial search specific to malignant hypertensive renal disease
- Clinical expert review of whether oral beta-blockade has any role beyond conventional management of malignant hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

