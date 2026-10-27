---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Triamterene: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension and congestive heart failure"
monitor_inn: "TRIAMTERENE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Triamterene
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

## Triamterene: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but currently there are **0 clinical trials** and **0 publications** directly supporting this prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the SAHPRA registration carries no indication text, so these come from the TxGNN knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron. This increases sodium excretion, lowers blood volume and reduces blood pressure. Its efficacy in hypertension and congestive heart failure is established.

The link to malignant renovascular hypertension is weak. This condition is driven mainly by activation of the renin-angiotensin system and usually needs RAAS blockade and revascularisation. Diuretic monotherapy is not a rational primary strategy. The high TxGNN score most likely reflects closeness in the knowledge graph to the approved hypertension indication, not independent evidence.

Other predictions in the same list show a similar pattern:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Malignant hypertensive renal disease | 99.89% | Largely a restatement of the hypertension indication. Hyperkalaemia risk in renal impairment is a major concern. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.88% | No evidence of effect on pulmonary vascular remodelling. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.88% | Only generic diuretic volume reduction. No supporting data. |
| Braddock syndrome | 99.84% | No plausible mechanistic link. |
| Chronic pulmonary heart disease (cor pulmonale) | 99.75% | Indirect support only, through the approved heart failure use. Rated L4 (research question). |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

---

## Literature Evidence

No literature was retrieved for the top predicted indication. Two publications were retrieved for lower-ranked predictions, and both are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Small randomised crossover study (classified as review) | Dtsch Med Wochenschr | 16 heart failure patients received hydrochlorothiazide + triamterene or digitalis. Addresses chronic heart failure in general, not cor pulmonale specifically. |
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Clinical haemodynamic study (design unconfirmed) | Fortschr Med | 12 heart failure patients on a verapamil/triamterene/hydrochlorothiazide combination for 4 weeks. Blood pressure and heart rate fell. |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Pulmonary oedema after a triamterene-hydrochlorothiazide tablet, thought to be due to the hydrochlorothiazide component. This is an adverse event report, not evidence of efficacy. |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Preclinical (animal) | J Physiol | Electrical potential across rat colon mucosa. No clinical relevance. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| U/18.1/72 | Renezide | Tablet (oral) | Not stated in the data compiled for this report |

Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease links in the knowledge graph, not from SAHPRA label text, and must be checked against the approved Professional Information):

- **Renal and urinary:** kidney disease, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Hepatic:** liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis
- **Metabolic:** diabetes mellitus (type 1 and 2), diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia, hyperparathyroidism, acidosis (including lactic acidosis), phosphorus metabolism disease
- **Other:** systemic lupus erythematosus, folic acid deficiency anaemia, neonatal jaundice

**Drug Interactions** (100 interactions were identified; examples are shown):

- **Major:** Potassium citrate (risk of hyperkalaemia)
- **Moderate:** Metformin, bupropion, morphine, dapagliflozin, canagliflozin, dronabinol, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- **Minor:** Famotidine, ranitidine, cimetidine, doxycycline, minocycline

Potassium monitoring is essential, particularly in renal impairment and when other potassium-raising agents are co-prescribed.

Please also refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, as this label information was not available for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model scoring (L5), with no clinical trials or directly relevant literature. The mechanism does not fit malignant renovascular hypertension, which is driven by the renin-angiotensin system. Hyperkalaemia and renal safety concerns further limit use in hypertensive kidney disease. Of the predictions, only chronic pulmonary heart disease has any indirect support (L4), as a research question.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or mechanistic studies specific to renovascular or malignant hypertension
- A potassium and renal safety assessment for patients with hypertensive kidney disease
- If any prediction is pursued, a focused review of diuretic use in cor pulmonale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

