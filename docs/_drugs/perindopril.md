---
layout: default
title: Perindopril
parent: Model Prediction Only (L5)
nav_order: 366
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder). Approved indication text is not…"
monitor_inn: "PERINDOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Perindopril
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

# Perindopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but there are currently **0 clinical trials** and only **1 publication** (not directly relevant) supporting this direction. The prediction rests on model inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). Approved indication text is not available in the SAHPRA registration data compiled for this report |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 (preclinical or mechanistic reasoning only; no relevant clinical studies) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, perindopril is an ACE inhibitor. It blocks the renin-angiotensin-aldosterone system (RAAS), lowering blood pressure and reducing pressure within the kidney's filtering units (intraglomerular pressure). This is biologically plausible for hypertensive kidney injury.

Malignant hypertensive renal disease is a severe form of hypertension, which is already perindopril's established indication. The high TxGNN score (99.77%) largely reflects this closeness to the approved indication rather than independent evidence. The single publication retrieved (functional state of a solitary kidney after nephrectomy for renal cancer) does not study perindopril or malignant hypertensive nephropathy.

Other predictions in the list are weaker:
- **Malignant renovascular hypertension** (99.77%, L5): ACE inhibition is mechanistically relevant, but ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis or stenosis of a solitary kidney. No trials or literature were found.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.75%, L4): Animal studies in hypoxic rats (e.g. PMID 11282121 and PMID 10602319) give a preclinical signal. Most other retrieved papers are irrelevant keyword matches.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.75%, L5) and **Braddock syndrome** (99.66%, L5): no supporting evidence and no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication. No SANCTR or PACTR entries were identified in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Other (not drug-specific) | Urologiia | Renal function of a solitary kidney after nephrectomy for renal cancer; does not address perindopril or malignant hypertensive nephropathy |

For the pulmonary hypertension prediction (rank 3), the most relevant item is preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Animal study | Eur J Pharmacol | In hypoxic rats, amlodipine plus perindopril fully prevented pulmonary artery medial thickening, versus partial effect with amlodipine alone |
| [10602319](https://pubmed.ncbi.nlm.nih.gov/10602319/) | 1999 | Animal study | Br J Pharmacol | Perindopril reduced pulmonary artery pressure by 18% in hypoxic pulmonary hypertensive rats |

## South Africa Market Information

Perindopril is marketed in South Africa. Approved indication text is not available for any of the registrations. Essential Medicines List (EML) status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34/7.1.3/0480 | Vectoryl | Tablet | Not available |
| 37/7.1.3/0021 | Perindopril unicorn | Tablet | Not available |
| 41/7.1.3/0652 | Spec-perindopril | Tablet | Not available |
| 44/7.1.3/0503 | Ciplasyl plus 4mg/1.25mg | Tablet | Not available |
| 55/7.1.3/0812 | Teprilam 10/10 | Tablet | Not available |

Four further registrations are valid: Cosyrel 5/5 (film-coated tablet), Pearinda, Preterax 2mg/0.625mg, and Spec-perindopril plus 4mg/1.25mg (all tablets).

## Safety Considerations

**Contraindication-related disease associations** (from a knowledge graph, not label text): kidney disease, liver disease, gallbladder disease, angioedema (including acquired, hereditary, and RAAS-blocker-induced forms), neutropenia, agranulocytosis, hypotensive disorder, connective tissue disease, bone disease, cartilage disease, renal artery obstruction, and pyoureter.

Two points deserve emphasis for the predicted indications:
- Renal artery obstruction and kidney disease appear on this list, which is directly relevant to renal and renovascular predictions.
- ACE-inhibitor angioedema can be life-threatening. Case reports describe late-onset airway angioedema with perindopril (PMID 37678466) and a case needing ECMO (PMID 40365500).

**Drug interactions** (100 recorded; examples):
- **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, saxagliptin, chlorpropamide, acetylsalicylic acid, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, morphine, bupropion, dronabinol, picosulfuric acid, polyethylene glycol with electrolytes

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score reflects proximity to the existing hypertension indication, not independent evidence. No relevant clinical trials exist, and the only retrieved publication does not address perindopril in this condition. Renal safety concerns (renal artery obstruction, kidney disease) add caution.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings, contraindications and approved indication text, which is currently a blocking gap for safety screening
- Detailed mechanism of action data (e.g. from DrugBank)
- Clinical studies or guideline evidence on ACE inhibitors in malignant hypertensive nephropathy
- A renal safety monitoring plan (renal function, potassium) for patients with severe hypertension and renal impairment
- Clarification of whether this is a distinct new indication or already covered within the approved hypertension indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

