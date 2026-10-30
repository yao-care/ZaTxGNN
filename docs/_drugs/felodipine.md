---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
monitor_inn: "FELODIPINE"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-30
description: "Felodipine: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension / hypertensive disorder"
---

# Felodipine
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

## Felodipine: From Hypertension to Pulmonary Hypertension with Unclear Multifactorial Mechanism
{: .text-alpha }

## One-Sentence Summary

Felodipine is a calcium channel blocker whose known use, as recorded in the knowledge graph, is hypertension.
The TxGNN model predicts it may be useful for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials and no publications** directly support this prediction, so the evidence rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (relation recorded in the knowledge graph; the local registration contains no indication text) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed (licences cancelled: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 0) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Felodipine belongs to the dihydropyridine class of L-type calcium channel blockers, which relax vascular smooth muscle and lower vascular resistance. This is the basis of its use in hypertension.

In theory, the same vasodilation could extend to the pulmonary circulation. However, calcium channel blockers help only a small vasoreactive subset of patients with pulmonary arterial hypertension, and the predicted condition here is poorly defined. The high score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

### Other predictions reviewed

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9991 | L5 | Eight preclinical papers (rat, dog and human ex vivo tissue) on hypoxia or anoxia. None studies pulmonary hypertension itself. Vasodilators may worsen ventilation-perfusion matching in lung disease. |
| Malignant hypertensive renal disease | 0.9990 | L5 | No trials or literature. It is largely an extension of the existing hypertension use. |
| Braddock syndrome | 0.9988 | L5 | No clear mechanistic rationale and no studies. |
| Chronic pulmonary heart disease | 0.9919 | L5 | Three older haemodynamic studies or reviews, none of which directly studies chronic pulmonary heart disease as a clinical outcome (see below). |

For chronic pulmonary heart disease, a 1988 study in 11 patients with severe COPD found that felodipine infusion reduced pulmonary vascular resistance by 18% and improved ventricular ejection fractions. This is a short haemodynamic observation in a related condition (COPD), not a study of cor pulmonale outcomes, so the evidence level stays at L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly addresses the top predicted indication. The nearest publications are listed below for context. They concern related conditions or mechanisms only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2838319](https://pubmed.ncbi.nlm.nih.gov/2838319/) | 1988 | Clinical haemodynamic study | Eur Respir J | In 11 patients with severe COPD, felodipine infusion lowered pulmonary vascular resistance by 18% and systemic vascular resistance by 33%, and raised cardiac output |
| [2487551](https://pubmed.ncbi.nlm.nih.gov/2487551/) | 1989 | Clinical haemodynamic study | Cardiovasc Drugs Ther | Acute haemodynamic and regional blood flow effects of felodipine in severe congestive heart failure |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonists in hypertension and supraventricular arrhythmias |
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | Preclinical (rat renal tubules) | Pflugers Arch | Felodipine protected against hypoxic injury through a calcium-independent mechanism |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | Preclinical (human atrial muscle, ex vivo) | Int J Cardiol | Felodipine pretreatment protected against hypoxia-reoxygenation dysfunction |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | Preclinical (rat) | Stroke | Dihydropyridines depressed the anoxia-induced rise in cerebral blood flow |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31/7.1/0677 | Tri-plen 2.5mg/2.5mg | Tablet | Not stated in the data compiled |

This single registration is valid, but it is a combination-type product name (2.5 mg/2.5 mg) listed as a single-ingredient record. It should not be used to describe how felodipine alone is approved. Essential Medicines List status is not stated in the data compiled.

## Safety Considerations

No approved label warnings or contraindications are available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

- **Knowledge-graph contraindication relations** (not label text; verify against the PI): kidney disease, liver disease, gallbladder disease, angioedema (including hereditary and ACE/RAAS-blocker-induced forms), neutropenia and agranulocytosis, aortic stenosis, hypotensive disorder, hypertrophic cardiomyopathy, renal artery obstruction, myocardial infarction, coronary artery disease and atherosclerosis, among others.
- **Drug interactions** (100 recorded; examples from DDInter):
  - Major: dolasetron.
  - Moderate: clarithromycin, cimetidine, aprepitant, bupropion, systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), morphine, acetylsalicylic acid, magnesium sulfate, and SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin).
- **Disease-specific concern:** in hypoxic lung disease, vasodilators can worsen ventilation-perfusion matching.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No clinical trial or publication studies pulmonary hypertension of unclear multifactorial mechanism, so the evidence level is L5. Calcium channel blockers benefit only a small vasoreactive subset of patients, and safety data from the label are missing.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings, contraindications, approved indication), as the registered product is a combination-type listing
- Mechanism of action data
- A clearer definition of the target pulmonary hypertension subgroup, such as vasoreactive pulmonary arterial hypertension
- Controlled clinical evidence in pulmonary hypertension, including haemodynamic safety in patients with hypoxic lung disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

