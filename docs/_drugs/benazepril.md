---
layout: default
title: Benazepril
parent: Moderate Evidence (L3-L4)
nav_order: 60
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-15
description: "Benazepril: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertension (hypertensive disorder). The SAHPRA registration text is…"
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Benazepril
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction.
The prediction rests on model-based proximity to the approved indication, not on clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The SAHPRA registration text is empty, so this comes from the knowledge graph indication data |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Benazepril is a member of the ACE inhibitor class. Its efficacy in hypertension is established, and by class pharmacology it lowers blood pressure by blocking the renin-angiotensin system.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so the mechanistic rationale is strong. However, this is essentially an extension of the approved hypertension indication to a severe subtype, not a truly new therapeutic area.

There is an important safety caveat. ACE inhibitors carry a known risk of acute renal failure in bilateral renal artery stenosis or a solitary kidney, which is exactly the setting in which renovascular hypertension occurs. This needs careful evaluation before any use.

### Other predicted indications (all prediction-only)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 99.65% | L4 | Indirect link, based on class-level renoprotective evidence for ACE inhibitors, not benazepril-specific data |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.60% | L5 | Weak rationale. ACE inhibitors have not shown reliable benefit in pulmonary hypertension, and vasodilators may worsen ventilation-perfusion matching in hypoxic lung disease |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.60% | L5 | Only a weak theoretical link via pulmonary vascular remodelling |
| 5 | Braddock syndrome | 99.44% | L5 | No clear mechanistic connection can be established |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports the lead prediction. For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), three preclinical papers were retrieved. They concern traditional Chinese medicine formulas in renal fibrosis, chronic renal failure, and myocardial fibrosis, and do not involve benazepril or pulmonary hypertension, so they offer no direct support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38803876](https://pubmed.ncbi.nlm.nih.gov/38803876/) | 2024 | Preclinical | Heliyon | Modified Zhenwu Tang and oxidative stress and hypoxic responses in a chronic renal failure model |
| [31007700](https://pubmed.ncbi.nlm.nih.gov/31007700/) | 2019 | Preclinical | Evid Based Complement Alternat Med | Danggui Shaoyao San and hypoxia and autophagy in rat renal fibrosis |
| [31317035](https://pubmed.ncbi.nlm.nih.gov/31317035/) | 2019 | Preclinical | BioMed Res Int | Tongxinluo and endothelial-to-mesenchymal transition in rat post-infarction myocardial fibrosis |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28/7.1.3/0121 | Cibadrex 10 (10 mg/12.5 mg) | Tablet (oral) | Not available in the compiled data |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

Safety data from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

**Knowledge graph contraindication signals** (from drug-disease contraindication edges, not label text, so they must be verified against the PI):
- **Hepatic and biliary:** liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis, neonatal jaundice
- **Renal and urinary:** kidney disease, anuria, pyoureter
- **Angioedema:** angioedema (including acquired, hereditary, and RAAS-blocker-induced forms)
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperuricaemia, hyperparathyroidism, osteitis fibrosa
- **Haematological:** neutropenia, agranulocytosis
- **Other:** hypotensive disorder, systemic lupus erythematosus (including paediatric), connective tissue disease, bone disease, cartilage disease

**Drug interactions:** The interaction query returned 100 records. The 20 listed in the compiled data are all of Moderate severity and mostly involve glucose-lowering agents:
- **Insulins** (human, aspart, degludec, detemir, glargine, glulisine, lispro, and others)
- **Sulfonylureas** (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide)
- **Other antidiabetic agents:** alogliptin, dapagliflozin, exenatide
- **Others:** hydrocortisone, glycerin

Co-prescription with antidiabetic agents warrants glucose monitoring.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for malignant renovascular hypertension is plausible, but no trials or literature support it. The high TxGNN score reflects proximity to the approved hypertension indication in the knowledge graph. The known renal risk of ACE inhibitors in renal artery stenosis adds a safety concern, and the other four predicted indications have weak or no mechanistic support.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking data gap that prevents safety screening)
- Detailed mechanism of action data
- Targeted literature review of ACE inhibitor use in renovascular hypertension, including renal function safety in bilateral renal artery stenosis or a solitary kidney
- Review of whether the single registration (Cibadrex 10, whose name suggests a benazepril/hydrochlorothiazide combination, though the compiled data lists it as a single-ingredient product) and its approved indication text support the proposed use
- A monitoring plan for renal function, potassium, and blood pressure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

