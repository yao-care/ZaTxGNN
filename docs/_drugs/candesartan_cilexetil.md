---
layout: default
title: Candesartan Cilexetil
parent: Moderate Evidence (L3-L4)
nav_order: 97
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-15
description: "Candesartan Cilexetil: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder). The SAHPRA registration records…"
monitor_inn: "CANDESARTAN CILEXETIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Candesartan Cilexetil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The SAHPRA registration records compiled for this report contain no approved-indication text, so this is taken from the knowledge-graph indication data. |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, candesartan is an angiotensin II type 1 receptor blocker (ARB). Its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-related kidney disease.

Malignant hypertensive renal disease (kidney injury from severely elevated blood pressure) involves activation of the renin-angiotensin-aldosterone system (RAAS). Blocking this pathway is therefore plausible. However, this indication is closely related to the already-approved hypertension indication rather than a distinct repurposing target. The high TxGNN score is a model prediction only.

Important clinical caveats:
- Acute malignant hypertension is generally managed with intravenous agents, not oral ARBs.
- ARBs carry renal risks, including hyperkalaemia and acute kidney injury, particularly in volume-depleted or renovascular states.

**Other predicted indications (all Hold):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant renovascular hypertension | 99.68% | L4 | RAAS-driven, so mechanistically relevant, but ARBs are contraindicated or require great caution in bilateral renal artery stenosis or stenosis in a solitary kidney (risk of acute renal failure). |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.67% | L5 | Angiotensin II may contribute to pulmonary vascular remodelling, but ARBs have no established efficacy in pulmonary hypertension. |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | L5 | Plausible but unproven link; systemic vasodilation may worsen ventilation-perfusion matching. |
| 5 | Braddock syndrome | 99.56% | L5 | No clear mechanistic link; the score likely reflects a network artefact, and the disease annotation should be verified. |

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction (malignant hypertensive renal disease). No SANCTR or PACTR entries were identified in the data compiled for this report.

## Literature Evidence

Currently no related literature available for the lead prediction.

For rank 4 (pulmonary hypertension owing to lung disease and/or hypoxia), two publications were retrieved, but neither provides clinical support:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Preclinical (mouse) | Frontiers in Immunology | Candesartan cilexetil, an anti-inflammatory compound, improved neurological outcomes in a mouse model of neonatal hypoxia-induced seizures. It is not a pulmonary hypertension study. |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Preclinical (rat) | Evid Based Complement Alternat Med | Hachimijiogan (a herbal formula, not candesartan) was studied in a remnant kidney model with involvement of HIF-1α, compared with an ARB. It does not support the predicted indication. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/7.1.3/0412 | Aterwin | Tablet | Not available in the data compiled |
| Reg. No. 44/7.1.3/0555 | Candepres plus 16mg/12.5mg | Tablet | Not available in the data compiled |
| Reg. No. 35/7.1.3/0098 | Atacand plus 16mg/12.5mg | Tablet | Not available in the data compiled |
| Reg. No. 45/7.1.3/0394 | Mylacand plus 16mg/12.5mg | Tablet | Not available in the data compiled |

All four registrations are valid and oral tablets. Essential Medicines List (EML) status was not available in the data compiled for this report. The product names suggest that three of the four are candesartan/hydrochlorothiazide (16 mg/12.5 mg) combinations, although they are recorded as single-ingredient entries.

## Safety Considerations

**Contraindications / conditions flagged in the knowledge graph** (derived from drug-disease contraindication links, not from label text):
- Renal and urinary: anuria, impaired renal function, renal artery obstruction, nephrocalcinosis
- Hepatic: liver disease, hepatic coma, hepatic encephalopathy, neonatal jaundice, gallbladder disease, pancreatitis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, phosphorus metabolism disease, hyperuricaemia, gout, hyperparathyroidism, osteitis fibrosa
- Other: hypotensive disorder, systemic lupus erythematosus (including paediatric)

Several of these probably reflect the hydrochlorothiazide component of the combination products. Renal artery obstruction and impaired renal function are directly relevant to the predicted renal and renovascular indications.

No drug-interaction data were found. For warnings and label contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and class-level mechanistic reasoning (evidence level L4). No clinical trials or relevant publications exist. The indication largely overlaps with the approved hypertension use, and there are renal safety concerns, especially in renovascular disease.

**To proceed, the following is needed:**
- Clinical or observational data on candesartan in hypertensive nephropathy or malignant hypertension
- Mechanism of action data (DrugBank)
- SAHPRA Professional Information (warnings, contraindications and approved indications) to complete safety screening
- Drug-interaction data
- Renal and potassium monitoring plan for any proposed use
- Verification of the Braddock syndrome annotation if that prediction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

