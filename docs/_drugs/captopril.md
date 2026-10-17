---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 98
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Captopril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder, hypertension, diabetic nephropathy"
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Captopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Captopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Captopril is an ACE inhibitor originally used for hypertensive disorders, hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 registered clinical trials** and only **18 publications** (almost all diagnostic, case reports or reviews, with no therapeutic trials) behind this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, diabetic nephropathy (from the knowledge-graph indication list; the SAHPRA registrations contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 (preclinical/mechanistic support only; no clinical trials) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold (treat as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, captopril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven by activation of the renin-angiotensin system (RAS) when renal perfusion falls. Blocking ACE is therefore biologically coherent. One 1984 clinical report describes captopril use in hypertension with a stable and a malignant course.

Caution is needed. This prediction is largely an extension of the existing hypertension indication rather than a true novel repurposing. Captopril is also widely used as a *diagnostic* tool (captopril renography and captopril-stimulated renin testing), and much of the retrieved literature reflects that use, not treatment. In bilateral renal artery stenosis, ACE inhibitors carry a known risk of acute renal failure.

Other predicted indications were also ranked. Malignant hypertensive renal disease (score 99.28%) has one diagnostic case report only. Pulmonary hypertension of unclear multifactorial mechanism (99.15%) has no literature. Pulmonary hypertension due to lung disease/hypoxia (99.15%) has only off-target preclinical literature. These are all rated L5 / Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Of the 18 publications retrieved for the lead prediction, none is a randomised trial. The most relevant are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Clinical report | Biulleten' Vsesoiuznogo kardiologicheskogo nauchnogo tsentra AMN SSSR | Use of captopril in hypertension with a stable and malignant course (no abstract available) |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Review | Endocrinol Metab Clin North Am | Renin-secreting tumours; blood pressure falls on converting-enzyme inhibitor treatment |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Review | Japanese Journal of Medicine | Pathophysiology and outcome of hypertension, including diagnostic tests for renovascular hypertension |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Clinical study | Clinical Science | Rise in plasma renin after ACE blockade (including captopril) identified renovascular hypertension in 43 of 44 untreated patients (diagnostic) |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Case report and review | Clinical Nephrology | Two cases of renovascular hypertension in neurofibromatosis; captopril used for renin testing |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Case series | Pediatric Nephrology | 27 children with neurofibromatosis type 1 assessed for renovascular disease and hypertension (captopril test) |
| [3326101](https://pubmed.ncbi.nlm.nih.gov/3326101/) | 1987 | Clinical report | Journal of UOEH | Efficacy of captopril in refractory hypertension in childhood |
| [6315275](https://pubmed.ncbi.nlm.nih.gov/6315275/) | 1983 | Review | Clin Exp Hypertens A | Acute and chronic renal effects of captopril and other converting enzyme inhibitors in hypertension |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Case report | Clinical Nuclear Medicine | False-positive captopril renogram in malignant hypertension without renal artery stenosis (diagnostic) |
| [7955304](https://pubmed.ncbi.nlm.nih.gov/7955304/) | 1994 | Review | Cleveland Clinic Journal of Medicine | Noninvasive screening for renovascular disease (diagnostic) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31/7.1/0658 | Bio-captopril | Tablet | Not available in the data compiled |
| 31/7.1.3/0478 | Captoretic Hs | Tablet | Not available in the data compiled |
| Y/7.1.3/379 | Capozide | Tablet | Not available in the data compiled |

All three registrations are valid and recorded as single-ingredient products. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindication and disease-risk signals (from the knowledge graph, not label text):**
- Renal and hepatic: kidney disease, liver disease, hepatic coma/encephalopathy, pancreatitis, gallbladder disease
- Angioedema: including hereditary, acquired and RAS-blocker-induced angioedema
- Haematological/immune: neutropenia, agranulocytosis, systemic lupus erythematosus, connective tissue disease
- Cardiovascular: aortic stenosis and aortic valve disease, hypotensive disorders
- Metabolic/other: potassium deficiency, diabetes mellitus and diabetic ketoacidosis, hyperuricaemia, hyperparathyroidism, bone disease

These come from knowledge-graph relationships and should be confirmed against the approved label.

**Drug interactions:** The interaction screen returned 100 entries. Those listed were mostly Moderate, with two Minor.
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Glucose-lowering agents: metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide
- Others (Moderate): acetylsalicylic acid, morphine, bupropion, dronabinol
- Minor: aluminium hydroxide, calcium carbonate

**Indication-specific risk:** In bilateral renal artery stenosis, ACE inhibitors carry a known risk of acute renal failure.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.28%) is not backed by therapeutic clinical data. There are no registered trials, and the literature is mainly diagnostic use, case reports and reviews. The prediction largely extends captopril's existing hypertension indication, and the renal safety risk in renovascular disease is significant. The evidence is at the research-question stage.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications), which is currently a blocking gap
- Detailed mechanism-of-action data
- Therapeutic studies (prospective or controlled) of captopril in malignant or renovascular hypertension
- A renal safety plan (renal function and potassium monitoring, exclusion of bilateral renal artery stenosis)
- Review of how this differs from the existing hypertension indication, to confirm whether it represents new value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

