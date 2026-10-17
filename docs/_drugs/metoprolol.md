---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 322
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metoprolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, acute coronary syndrome, myocardial infarction"
monitor_inn: "METOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "trichotillomania"]
---

# Metoprolol
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

# Metoprolol: From Hypertension and Myocardial Infarction to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker, originally used for hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are **0 clinical trials** and only **1 publication** (a diagnostic study unrelated to metoprolol treatment) for this prediction.
The top-ranked prediction is essentially a subtype of an existing indication, so it is not true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, acute coronary syndrome, myocardial infarction (the SAHPRA licence record contains no indication text; these indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, metoprolol is a cardioselective beta-1 blocker. It lowers heart rate and cardiac output and reduces renin release from the kidney. Renin release is the pathway that drives renovascular hypertension, so the prediction is mechanistically plausible.

Malignant renovascular hypertension is a severe form of the hypertension that metoprolol is already used for, so this is better seen as a subtype of an existing indication than as a new use. The high score probably reflects close links to hypertension nodes in the knowledge graph. The only publication retrieved (PMID 1988765) is about chromogranin A as a diagnostic marker for pheochromocytoma and says nothing about treating this condition with metoprolol. Malignant hypertension is generally managed acutely with intravenous agents, and beta-blockers are not first-line.

### Other predictions reviewed

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 99.91% | L5 | No trials or literature; overlaps with hypertension |
| 3 | Pulmonary hypertension owing to lung disease/hypoxia | 99.91% | L4 | Only indirect, off-topic literature; beta-blockade is a theoretical concern in pulmonary hypertension |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 99.91% | L5 | No evidence; right ventricular function concern |
| 5 | Braddock syndrome | 99.89% | L5 | No evidence or plausible mechanism |
| 6 | Posterolateral myocardial infarction | 99.84% | L4 | Subtype of existing indication; small old haemodynamic studies |
| 7 | Posteroinferior myocardial infarction | 99.84% | L5 | Subtype of existing indication; no subtype evidence |
| 8 | Septal myocardial infarction | 99.80% | L3 | Subtype of existing indication; small clinical studies on remodelling |
| 9 | Chronic pulmonary heart disease | 99.40% | L3 | Most evidence available, mainly on safety in COPD |
| 10 | Trichotillomania | 99.05% | L5 | No evidence or mechanistic rationale |

The best-supported entry is chronic pulmonary heart disease (rank 9), which has 4 registered trials and about 20 publications. The evidence addresses metoprolol in patients with heart failure and COPD, not right heart disease directly.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction (malignant renovascular hypertension). The trials below relate to the best-supported prediction, chronic pulmonary heart disease (rank 9).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol doses in heart failure with reduced ejection fraction and COPD; outcomes are all-cause death and re-hospitalisation (planned completion 2028) |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | Randomised, placebo-controlled trial of metoprolol to prevent COPD exacerbations; stopped early, so conclusions are limited |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | Carvedilol vs metoprolol respiratory effects in heart failure; no participants enrolled, so no data |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | Terminated | 14 | Post-COVID exertional dyspnoea with tachycardia; loosely related |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

## Literature Evidence

Publications for the top-ranked prediction: only one (PMID 1988765), which is not relevant to metoprolol treatment. The table below lists the most relevant publications for the best-supported prediction (chronic pulmonary heart disease), in order of priority.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | BICS trial of bisoprolol in COPD at high risk of exacerbation; notes that the earlier metoprolol trial did not reduce exacerbations and increased those needing hospital admission |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction (not specific to pulmonary heart disease) |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised crossover | J Am Coll Cardiol | Switching between beta-1 selective and non-selective beta-blockers in chronic heart failure with COPD |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Secondary analysis of RCT | Ann Am Thorac Soc | BLOCK COPD analysis of chronotropic index and COPD exacerbations on metoprolol |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in older patients with heart failure, COPD, diabetes and renal failure |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | Eur J Heart Fail | Danish cohort of beta-blocker use in heart failure with COPD |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Carvedilol, bisoprolol and metoprolol in coexisting heart failure and COPD (Taiwan database) |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Review | Expert Rev Respir Med | Practical recommendations for beta-blockers in COPD |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Clinical study | Heart Vessels | Metoprolol appeared safe in coronary artery disease patients with COPD |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Clinical physiological study | Clin Cardiol | Oral metoprolol in 6 patients with reversible airways obstruction |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H/5.2/72 | Lopresor | Tablet (oral) | Not available in the data compiled for this report |

One valid single-ingredient registration is on record. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are drug-disease links, not text from the approved label). They include:
- Cardiovascular and metabolic: hypotensive disorder, diabetes mellitus, diabetic ketoacidosis, gout, anuria
- Neuromuscular: myasthenia gravis and other neuromuscular junction diseases
- Endocrine: phaeochromocytoma
- Hepatic: liver disease, hepatic coma and encephalopathy
- Others: psoriasis, systemic lupus erythematosus, pancreatitis, gallbladder disease, anxiety and related disorders

**Drug interactions:** 100 interactions were found in the DDInter database; the 20 listed in the data compiled for this report are mostly Moderate. Examples:
- Moderate: epinephrine, bupropion, morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, glycopyrronium)
- Minor: acetylsalicylic acid, magnesium oxide

**Population-specific signal:** In COPD, the BLOCK-COPD metoprolol trial reported more exacerbations requiring hospitalisation (as noted in PMID 38762800). Beta-blockers also carry a theoretical risk in pulmonary hypertension because of reduced right ventricular reserve.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, malignant renovascular hypertension, has no trials and no relevant literature, and it is a subtype of hypertension, which metoprolol already treats. Acute management of malignant hypertension normally relies on intravenous agents, so there is no clear new role for oral metoprolol. The most evidence-supported prediction (chronic pulmonary heart disease, L3) is a research question, not a ready repurposing candidate, because existing data concern COPD safety and show a hospitalisation signal.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings, contraindications, approved indications), as the safety screening cannot be completed without it
- Mechanism of action data from DrugBank
- For malignant renovascular hypertension: a targeted literature review of beta-blocker use in renin-mediated hypertension, and a comparison with current guideline-recommended agents
- For chronic pulmonary heart disease: results of NCT06825728 and a review of right ventricular outcomes
- Confirmation of EML status and of the Lopresor approved indications in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

