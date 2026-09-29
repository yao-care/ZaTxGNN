---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 5
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Quinapril: From ACE-Inhibitor Antihypertensive Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Quinapril is an ACE inhibitor marketed in South Africa, mostly in fixed-dose tablets. The supplied SAHPRA records do not state its approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
**No clinical trials and no relevant publications** currently support this prediction, so it rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA records |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, quinapril is an ACE inhibitor. Renovascular hypertension is driven largely by the renin-angiotensin system, so ACE inhibition is mechanistically plausible for this condition. This reasoning comes from general knowledge, not from evidence in the supplied data.

The predicted indication is a severe form of hypertension, and it overlaps with quinapril's known antihypertensive use. It may therefore not be true repurposing, but an extension within the same therapeutic area. The very high score (99.86%) is a computational output and not clinical evidence. It also matches the score of the "malignant hypertensive renal disease" prediction, which suggests both come from the same hypertension-related area of the knowledge graph.

Safety caution: ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis, a common cause of renovascular hypertension. This would need careful evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

## Other Predicted Indications

All have evidence level L5 and a recommendation of Hold. None has clinical trial support.

| Predicted Indication | TxGNN Score | Evidence Notes |
|------|------|------|
| Malignant hypertensive renal disease | 99.86% | No trials or literature. Angiotensin II involvement in renal injury makes the link plausible. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.85% | 20 publications were retrieved, but the 10 provided are general hypoxia-biology papers (brain ageing, cancer, keloid, multiple sclerosis, altitude). None mention quinapril, ACE inhibitors or pulmonary hypertension treatment, and the other 10 were not assessed. The link appears to be a keyword match on "hypoxia" only. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.85% | No trials or literature, and no drug-specific rationale. |
| Braddock syndrome | 99.79% | Ultra-rare syndrome with no trials or literature and no clear mechanistic link. ACE inhibitors carry fetal toxicity warnings. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 43/7.1.3/1044 | Biquretic 10/12,5 Mg | Tablet |
| Reg. No. 41/7.1.3/0212 | Quinace Co 10/12,5 | Tablet |
| Reg. No. 43/7.1.3/1046 | Kwinco 10/12,5 Mg | Tablet |
| Reg. No. 38/5.2/0106 | Bisoprolol Hexal | Tablet |
| Reg. No. 27/7.1.3/0165 | Accuretic 10/12.5 | Tablet |

Approved indication text was not available for any registration. The "10/12.5" strengths suggest quinapril 10 mg combined with hydrochlorothiazide 12.5 mg, but this should be confirmed against the Professional Information. "Bisoprolol Hexal" appears to be a bisoprolol product, so its link to quinapril should be verified. Essential Medicines List status was not assessed.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Cautions from the prediction rationale: ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis. Renal function and potassium monitoring would be key in any future evaluation. Fetal toxicity would need careful risk assessment in reproductive-age patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has evidence level L5, with no clinical trials and no relevant literature. The predicted indication also overlaps with quinapril's existing antihypertensive use, so the value as repurposing is unclear. The SAHPRA safety data is not yet available, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) for the registered quinapril products
- Mechanism of action data (for example from DrugBank)
- A check of whether malignant renovascular hypertension is already covered by current quinapril labelling
- A targeted literature search on ACE inhibitors in renovascular hypertension, since the retrieved papers were not relevant
- A renal safety plan for patients with renal artery stenosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

