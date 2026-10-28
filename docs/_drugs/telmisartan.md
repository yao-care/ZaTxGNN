---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Telmisartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Telmisartan: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker (ARB) originally used to treat hypertension and to reduce stroke and cerebrovascular risk.
The TxGNN model's top-ranked prediction is **Prinzmetal angina**, but **no clinical trials and no publications** were found for it, so this is a model prediction only.
The best-supported candidate among the top ten is **intracerebral hemorrhage**, which has **1 completed Phase 3 trial (a combination pill)** and **12 publications**. Because the trial intervention is a combination, its results cannot be attributed to telmisartan alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed (valid licences: 17 of 17) |
| Number of SAHPRA Registrations | 17 (valid: 17) |
| Recommended Decision | Hold |

**Other top-ranked predictions with evidence (for context):**

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Cerebral artery occlusion | 0.9995 | L2 | Research question |
| Intracerebral hemorrhage | 0.9993 | L5 | Research question |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9993 | L5 | Hold |

The remaining predictions (brain stem infarction, ABri amyloidosis, pulmonary hypertension with unclear multifactorial mechanism, malignant renovascular hypertension, malignant hypertensive renal disease, Braddock syndrome) have no trials or literature and sit at L5 (Hold).

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, telmisartan blocks the angiotensin II type 1 (AT1) receptor, and preclinical studies also describe partial PPARγ agonism. Its efficacy in hypertension and cardiovascular risk reduction is established.

For **Prinzmetal angina** (coronary vasospasm), a plausible link exists through ARB-mediated vasodilation and endothelial effects. However, nothing in the data compiled for this report supports it, so it should be regarded as a hypothesis only.

The cerebrovascular predictions are more coherent. Telmisartan's original indications already include stroke-related conditions, so **cerebral artery occlusion** and **intracerebral hemorrhage** are largely extensions of an existing indication area rather than independent repurposing discoveries. Animal studies of cerebral ischaemia report reduced infarct volume, oxidative stress and inflammation, with a proposed PPARγ-mediated neuroprotective pathway. In intracerebral hemorrhage, the benefit is likely driven mainly by blood pressure lowering, with possible added anti-inflammatory effects.

---

## Clinical Trial Evidence

No trials are registered for Prinzmetal angina. Currently no related clinical trials registered for the top-ranked prediction.

For the better-supported predictions:

**Intracerebral hemorrhage**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: low-dose triple-pill BP-lowering strategy vs standard care for preventing recurrent stroke after ICH. Combination pill, not telmisartan alone |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; too small to interpret |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study (memory decline); too small to interpret |

**Cerebral artery occlusion**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1228 | Open-label (PROBE) trial of telmisartan vs ordinary therapy in high-risk hypertensive patients, looking at biomarkers and cardiovascular events; outcomes not provided |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; uninformative |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; uninformative |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

No publications were found for Prinzmetal angina. Currently no related literature available for the top-ranked prediction.

**Intracerebral hemorrhage (selected)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT report | N Engl J Med | Triple low-dose antihypertensive single pill after ICH (TRIDENT); results not verifiable from the data available here |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial protocol | Int J Stroke | TRIDENT rationale and design |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | RCT secondary analysis | Int J Stroke | Ischaemic and haemorrhagic stroke recurrence by race-ethnic group in PRoFESS |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical | J Pharmacol Exp Ther | AT1 blockade with telmisartan reduced apoptosis, inflammation and oxidative stress in rat ICH |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical | Neurol Res | Telmisartan reduced oxidative stress and vasospasm after subarachnoid haemorrhage in animals |

**Cerebral artery occlusion (selected)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Preclinical | J Neurotrauma | Telmisartan reduced infarct volume and peri-infarct cPLA2 in rat MCAO |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Preclinical | J Stroke Cerebrovasc Dis | PPARγ activation by telmisartan inhibited Egr-1 and reduced brain injury |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Preclinical | Pharmacol Biochem Behav | Non-hypotensive telmisartan plus nimodipine gave synergistic neuroprotection |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Preclinical | PLoS One | Telmisartan, ramipril and their combination in rat stroke models |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Preclinical | Toxicol Rep | Telmisartan attenuated cerebral ischaemia-reperfusion neurotoxicity via Nrf2/HO-1 |

For cerebral artery occlusion, all retrieved studies are animal studies. For pulmonary hypertension owing to lung disease and/or hypoxia, the literature is indirect (mouse intermittent-hypoxia models and high-altitude blood pressure studies) and does not evaluate pulmonary hypertension in humans.

---

## South Africa Market Information

Telmisartan is marketed in South Africa with 17 valid registrations (all valid, none cancelled). Approved indication text and manufacturer details were not available in the data compiled for this report. Essential Medicines List (EML) status could not be determined from the available data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/7.1.3/0726 | Telmisartan 40 Unicorn | Tablet | Not available |
| Reg. No. 47/7.1.3/1120 | Tesminol 40 Mg | Tablet | Not available |
| Reg. No. 46/7.1.3/0938 | Telpres 40 | Film-coated tablet | Not available |
| Reg. No. 46/7.1.3/0939 | Telpres 80 | Film-coated tablet | Not available |
| Reg. No. 46/7.1.3/0928 | Tremistan Plus 80/12.5 Mg | Film-coated tablet | Not available |

The remaining 12 registrations include fixed-dose combinations with hydrochlorothiazide or amlodipine (e.g. Telpres Plus, Stytem, Co-pritor, Co-Telza, Amtelip, Ticarda Plus).

---

## Safety Considerations

**Contraindications / conditions of concern.** No label-based warnings or contraindications were available. The knowledge graph links telmisartan to caution or contraindication in the following conditions, which are not label text and should be checked against the SAHPRA-approved Professional Information (PI):
- Hepatic: liver failure, liver disease, hepatic coma and encephalopathy, cholestasis (including familial and benign recurrent forms), gallbladder disease, pancreatitis
- Renal: kidney disease, anuria, renal artery obstruction, nephrocalcinosis
- Metabolic: potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, gout, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disorders
- Other: hypotensive disorder, systemic lupus erythematosus (including paediatric), neonatal jaundice, pyoureter

Several of these likely reflect the hydrochlorothiazide-containing combination products. Renal artery stenosis is particularly relevant to the renovascular hypertension predictions.

**Drug interactions.** The interaction screen returned 100 interactions in total; examples from the first 20 are listed:
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulin (human, aspart), exenatide, bupropion, morphine, dronabinol, and bowel-preparation agents (sodium sulfate, picosulfuric acid, polyethylene glycol with electrolytes)

Refer to the SAHPRA-approved PI for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, Prinzmetal angina)

**Rationale:**
- Prinzmetal angina is supported by a model score alone, with no trials or literature (L5). Cerebral artery occlusion and intracerebral hemorrhage are better supported (L2) but are largely extensions of telmisartan's existing stroke-related indication. The Phase 3 TRIDENT trial tested a triple-pill combination, so benefit cannot be attributed to telmisartan, and the animal data have not been confirmed in humans.
- These two cerebrovascular candidates may be pursued as research questions rather than as new indications.

**To proceed, the following is needed:**
- SAHPRA PI warnings and contraindications, which is a blocking gap for safety screening
- Detailed mechanism of action data
- Verification of the TRIDENT results (NCT02699645, PMID 42019018) and whether they support telmisartan-containing therapy
- For Prinzmetal angina, any clinical or mechanistic evidence
- Approved indication text and EML status for the South African registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

