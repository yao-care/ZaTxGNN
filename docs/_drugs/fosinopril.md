---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 241
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Fosinopril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder). The SAHPRA registration record…"
monitor_inn: "FOSINOPRIL"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Fosinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Fosinopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but this is a computational prediction only: **0 clinical trials** and **0 publications** were found for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The SAHPRA registration record contains no indication text, so this comes from the knowledge graph |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fosinopril is an ACE inhibitor, its use in hypertension is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system (RAS), so blocking this pathway is biologically plausible. The predicted indication is also very close to the approved hypertension indication. It is better seen as a subtype of the existing use than as true repurposing.

There is an important safety caveat. ACE inhibitors can cause an acute decline in kidney function in patients with bilateral renal artery stenosis or a solitary kidney, which are the very patients in whom renovascular hypertension occurs. The high score (0.9987) is a computational output and is not backed by trial or literature evidence in the data compiled for this report.

### Other Predicted Indications (All L5, All Hold)

| Rank | Predicted Indication | Score | Comment |
|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 99.87% | RAS blockade is plausible for reducing intraglomerular pressure and proteinuria. Malignant hypertension is an emergency, where agent choice, pace of blood pressure reduction, and renal function and potassium monitoring matter. It is also a subtype of the approved indication. |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.87% | Theoretical rationale only. ACE inhibitors have not shown reliable benefit in pulmonary hypertension and guidelines do not recommend them for it. Systemic hypotension is a risk. |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.87% | Theoretical link only. The two retrieved publications do not support efficacy (see below). |
| 5 | Braddock syndrome | 99.81% | Very rare condition with no evident mechanistic link to ACE inhibition. The score likely reflects network-level associations. It would need a fresh mechanistic and phenotype review. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked indication (malignant renovascular hypertension). Two publications were retrieved for the rank 4 prediction. Neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report (adverse event) | Revue des maladies respiratoires | Two patients treated with enalapril and fosinopril for hypertension developed hypoxic eosinophilic pneumonia with sub-acute respiratory failure. They improved after the ACE inhibitor was stopped. This is a possible pulmonary safety signal. |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinical/bioinformatics | Experimental and Therapeutic Medicine | Gene expression analysis of mouse mesangial cells in a diabetic nephropathy context. Not relevant to pulmonary hypertension. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31/7.1.3/0416 | Monozide | Tablet (oral) | Not available in the registration record |

Only one registration is on record (single-ingredient, valid). Essential Medicines List status could not be determined from the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (derived from drug-disease network edges, not from approved label text, so they must be checked against the SAHPRA Professional Information):
- **Angioedema:** including hereditary, acquired, and RAAS-blocker-induced forms
- **Kidney and liver:** kidney disease, liver disease, hepatic coma and encephalopathy, pyoureter
- **Cardiovascular:** aortic stenosis and aortic valve disease, hypotensive disorders
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperparathyroidism, osteitis fibrosa, hyperuricaemia
- **Haematological:** neutropenia, agranulocytosis
- **Other:** pancreatitis, gallbladder disease, systemic lupus erythematosus (including paediatric), connective tissue disease, bone disease

**Drug interactions** (DDInter; 100 interactions found, the first 20 returned):
- **Major:** potassium bicarbonate and potassium citrate, because of the risk of hyperkalaemia
- **Moderate:**
  - Corticosteroids: hydrocortisone, betamethasone, budesonide, triamcinolone, dexamethasone
  - Antidiabetic agents: alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, metformin
  - Others: acetylsalicylic acid, bupropion, morphine, dronabinol, picosulfuric acid, polyethylene glycol with electrolytes

Please also refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or supporting literature. The top-ranked indications are subtypes of the already approved hypertension use, so they add little as true repurposing. The one relevant literature signal (pulmonary) points toward harm, and the renal risk in renovascular disease is a significant concern.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Clinical evidence for ACE inhibitors in renovascular and malignant hypertension, with attention to renal artery stenosis and solitary kidney populations
- A monitoring plan for renal function, potassium and blood pressure
- For the pulmonary hypertension and Braddock syndrome predictions, a fresh mechanistic and phenotype review before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

