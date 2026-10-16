---
layout: default
title: Amiloride
parent: Moderate Evidence (L3-L4)
nav_order: 25
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-15
description: "Amiloride: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertension and congestive heart failure"
---

# Amiloride
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Amiloride: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic, originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **no registered clinical trials** and only **1 indirect publication** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (no approved indication text is recorded in the SAHPRA registrations compiled for this report; the original indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amiloride is generally known to block the epithelial sodium channel (ENaC). It is already used for hypertension and heart failure, and it may be applicable to related hypertensive conditions.

The relationship to the new indication is weak, however. Malignant renovascular hypertension is mainly driven by activation of the renin-angiotensin system, not by sodium-channel or mineralocorticoid mechanisms. The only linked paper (a 2003 review on mineralocorticoid hypertension) offers indirect support. The very high TxGNN score most likely reflects the closeness of this condition to the known hypertension indication in the knowledge graph, rather than new biology.

Other predictions in the same list were also assessed:
- **Malignant hypertensive renal disease** (score 99.82%, L5): prediction only, with no trials or literature. Hyperkalaemia risk in renal impairment is a major concern.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.81%, L4): there is a plausible preclinical rationale. Hypoxia downregulates ENaC in alveolar epithelium, and ASIC1 in smooth muscle is implicated in hypoxic pulmonary hypertension. There are no clinical trials, and most of the 20 retrieved papers are off-target.
- **Chronic pulmonary heart disease** (score 99.68%, L3): amiloride is already used as adjunctive therapy in heart failure, but the supporting studies address general or left-sided heart failure, so the evidence is indirect.
- **Pulmonary hypertension with unclear multifactorial mechanism and Braddock syndrome**: prediction only (L5), with no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Overview of investigating mineralocorticoid hypertension (primary aldosteronism, hypokalaemia, low renin). Only indirect support for the predicted indication. |

For context, the literature linked to the other predicted indications includes:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Clinical study (double-blind crossover) | Cardiovasc Drugs Ther | Amiloride improved haemodynamics in 11 chronic heart failure patients on digoxin (chronic pulmonary heart disease). |
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT | Lancet | Captopril alone vs frusemide plus amiloride in mild heart failure (14 patients); 4 patients on captopril alone deteriorated. |
| [25398716](https://pubmed.ncbi.nlm.nih.gov/25398716/) | 2015 | Preclinical review | Exp Physiol | Smooth muscle ASIC1 is implicated in hypoxic pulmonary hypertension. |
| [9376126](https://pubmed.ncbi.nlm.nih.gov/9376126/) | 1997 | Preclinical | Am J Respir Cell Mol Biol | Hypoxia reduced amiloride-sensitive sodium channel activity in rat alveolar cells. |
| [15219007](https://pubmed.ncbi.nlm.nih.gov/15219007/) | 2004 | Cohort/physiological | Eur Respir J | High altitude impairs nasal sodium transport in HAPE-prone subjects. |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case report | Am J Med Sci | Severe hyperkalaemia in an elderly heart failure patient on trimethoprim-sulfamethoxazole (safety signal). |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. Q/18.1/168 | Sandoz Co-Amilozide | Tablet | Not recorded |
| Reg. No. V/18.1/260 | Adco-retic 50mg/5mg | Tablet | Not recorded |
| Reg. No. L/18.1/396 | Amiloretic | Tablet | Not recorded |
| Reg. No. U/18.1/0040 | Amiloretic hs 25mg/2.5mg | Tablet | Not recorded |

All four registrations are valid oral tablets. Essential Medicines List (EML) status is not covered by the data compiled for this report.

## Safety Considerations

- **Contraindications / cautions (from knowledge graph associations, not label text)**: kidney disease, anuria, diabetic nephropathy, liver disease, hepatic coma/encephalopathy, pancreatitis, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, gout and hyperuricaemia, acidosis (including lactic acidosis), potassium deficiency disease, hyperparathyroidism, systemic lupus erythematosus, and neonatal jaundice. These should be verified against the SAHPRA-approved Professional Information.
- **Hyperkalaemia**: a recognised concern with potassium-sparing diuretics, particularly in renal impairment, in elderly patients, and with interacting drugs (see the trimethoprim-sulfamethoxazole case report above).
- **Drug interactions**: 100 interactions were identified. The ones listed are mostly Moderate:
  - Corticosteroids: hydrocortisone, betamethasone, budesonide, dexamethasone
  - Antidiabetic agents: metformin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide
  - Laxatives: bisacodyl, castor oil, glycerin, lactitol, lactulose
  - Others: bupropion, dronabinol
  - Minor: doxycycline, amoxicillin, cimetidine

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone. There are no clinical trials, the single linked paper is an indirect review, and the proposed mechanism does not match the renin-driven biology of malignant renovascular hypertension. Hyperkalaemia and renal risks add to the concern. Of the related predictions, pulmonary hypertension due to lung disease or hypoxia (preclinical rationale) and chronic pulmonary heart disease (indirect heart-failure data) merit further research questions.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) for amiloride
- The SAHPRA package insert warnings and contraindications, and the approved indication text for each registration
- Direct clinical or mechanistic evidence in malignant renovascular hypertension (or in the more promising hypoxic pulmonary hypertension and cor pulmonale indications)
- A potassium and renal function monitoring plan for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

