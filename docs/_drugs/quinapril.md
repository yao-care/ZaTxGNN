---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 398
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Quinapril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder). The SAHPRA licence records comp…"
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Quinapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Quinapril: From Hypertension to Malignant Renovascular Hypertension
{: .text-alpha }

## One-Sentence Summary

Quinapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The SAHPRA licence records compiled for this report contain no approved indication text, so this is taken from the knowledge-graph indication data. |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, quinapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension.

Malignant renovascular hypertension is strongly dependent on the renin-angiotensin-aldosterone system (RAAS), so RAAS blockade is plausible. The high TxGNN score most likely reflects similarity to the already approved hypertension indication rather than any new evidence.

An important caution applies: ACE inhibitors carry a known risk of acute decline in renal function in bilateral renal artery stenosis or a solitary kidney. This is precisely the setting of renovascular hypertension, so the approach would need careful specialist supervision.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.86% | L5 | Hold. RAAS blockade may reduce intraglomerular pressure and proteinuria, but there is no direct clinical evidence. |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.85% | L4 | Research question. Animal data only. |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.85% | L5 | Hold. Loose mechanistic rationale only. |
| 5 | Braddock syndrome | 99.79% | L5 | Hold. No clear mechanistic link found. |

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension, and none for the other predicted indications.

## Literature Evidence

Currently no related literature is available for malignant renovascular hypertension.

For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), two preclinical papers were identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Preclinical animal study | Circulation | Inhibiting tissue ACE with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodeling |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Preclinical animal study | J Cardiovasc Pharmacol | Quinapril preserved left ventricular function and energy metabolism in rats after myocardial infarction (only indirectly relevant) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/7.1.3/1044 | Biquretic 10/12,5 Mg | Tablet | Not available |
| Reg. No. 41/7.1.3/0212 | Quinace Co 10/12,5 | Tablet | Not available |
| Reg. No. 43/7.1.3/1046 | Kwinco 10/12,5 Mg | Tablet | Not available |
| Reg. No. 38/5.2/0106 | Bisoprolol Hexal | Tablet | Not available |
| Reg. No. 27/7.1.3/0165 | Accuretic 10/12.5 | Tablet | Not available |

All five registrations are valid and oral tablets. The product names with "10/12,5" suggest quinapril/hydrochlorothiazide combinations, but the data compiled for this report classify them as single-ingredient products. Please verify against the SAHPRA Professional Information. The Essential Medicines List (EML) status could not be determined from the available data.

## Safety Considerations

**Contraindication and disease-risk signals (from knowledge-graph drug-disease edges, not label text):**
Conditions linked to quinapril include kidney disease, anuria, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, angioedema (including hereditary and ACE inhibitor/RAAS-blocker-induced forms), systemic lupus erythematosus and other connective tissue disease, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, gout, neutropenia and agranulocytosis, hypotensive disorders, hyperparathyroidism, bone and cartilage disease, and neonatal jaundice. These are graph-derived signals and must be confirmed against the approved label.

**Drug Interactions:** The interaction query returned 100 records, of which 20 were reviewed here (most rated Moderate).
- **Major:** Potassium citrate (risk of hyperkalaemia)
- **Moderate (examples):** Metformin, acetylsalicylic acid, dapagliflozin, canagliflozin, chlorpropamide, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), tetracycline, doxycycline, morphine, bupropion

For authoritative warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a plausible RAAS mechanism, with no trials or publications for malignant renovascular hypertension. The renal risks of ACE inhibitors in renovascular disease add further reason for caution.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to complete the safety review (warnings and contraindications are currently missing)
- Detailed mechanism of action data
- Clinical evidence specific to malignant renovascular hypertension, such as a literature search or registered trials
- A renal safety plan for patients with bilateral renal artery stenosis or a solitary kidney (monitoring of creatinine, eGFR and potassium)
- Approved indication text for the SAHPRA registrations, and confirmation of whether the combination products contain quinapril
- Separate review of the pulmonary hypertension prediction, which currently has animal data only and is a research question rather than a candidate for clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

