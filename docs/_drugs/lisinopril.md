---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lisinopril: predicted new indication Posterolateral myocardial infarction . Most meaningful new candidate:… (evidence level L5). Approved use: Hypertension, myocardial infarction"
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Lisinopril: From Hypertension and Myocardial Infarction to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used for hypertension and myocardial infarction.
The TxGNN model's top-ranked prediction is **posterolateral myocardial infarction**, but this is a subtype of an already-approved indication and not a true repurposing signal. The only new indication with direct clinical publications is **chronic pulmonary heart disease** (2 small clinical studies, no registered clinical trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; no approved indication text is available in the SAHPRA records) |
| Predicted New Indication | Posterolateral myocardial infarction (top-ranked; a subtype of the existing MI indication). Most meaningful new candidate: chronic pulmonary heart disease |
| TxGNN Prediction Score | 99.90% (posterolateral myocardial infarction); 99.68% (chronic pulmonary heart disease) |
| Evidence Level | L4 (top-ranked prediction); L3 for chronic pulmonary heart disease |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold (top-ranked prediction); research question for chronic pulmonary heart disease |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lisinopril is an ACE inhibitor, and its efficacy in hypertension and myocardial infarction is established. By blocking the renin-angiotensin system (RAS), it reduces afterload and limits adverse cardiac remodelling.

**Top-ranked predictions (MI subtypes).** Posterolateral, posteroinferior and septal myocardial infarction are anatomical subtypes of myocardial infarction, which lisinopril already treats. The high scores reflect the known parent indication, not a new repurposing opportunity. The same applies to malignant renovascular hypertension and malignant hypertensive renal disease, which fall within the approved hypertension indication.

**Chronic pulmonary heart disease.** This is the most interesting candidate. RAS activity contributes to pulmonary vascular tone and remodelling, and lowering right-ventricular afterload is mechanistically plausible. Two Russian-language clinical studies report that lisinopril attenuated pulmonary hypertension and improved right-ventricular function. They appear small and likely uncontrolled, so confirmatory controlled trials are needed.

**Pulmonary hypertension (lung disease/hypoxia).** The link is plausible but weak. The 15 publications retrieved are mostly preclinical or off-topic (fish physiology, retinopathy of prematurity, skeletal muscle). One rat study suggests endothelin, not angiotensin II, drives the hypoxic pulmonary artery response. ACE inhibitors are not established therapy for this indication.

**Other predictions** (pulmonary hypertension with unclear mechanism, Braddock syndrome, a rare COL4A1-related syndrome) are model predictions only, with no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

Literature for the most relevant indication, chronic pulmonary heart disease. Study types are from preliminary classification and design could not be confirmed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (likely small/uncontrolled) | Kardiologiia | Lisinopril 10 mg/day attenuated pulmonary hypertension and improved right-ventricular systolic function and diastolic filling in heart failure with ischaemic heart disease and COPD |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (likely small/uncontrolled) | Problemy tuberkuleza i boleznei legkikh | Lisinopril in chronic cor pulmonale (no abstract available) |
| [26895877](https://pubmed.ncbi.nlm.nih.gov/26895877/) | 2016 | Review/Commentary | European Journal of Pediatrics | Discusses ACE inhibitor use in paediatric chronic heart failure despite limited data |
| [20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/) | 2010 | Case report (safety) | Am J Health-Syst Pharm | Severe bradycardia and hypotension with concomitant tizanidine and lisinopril |

Other indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | ACE inhibitor plus coenzyme Q10 as adjunctive treatment in ventricular septal rupture after late-onset MI (indirect evidence for septal MI) |
| [10456287](https://pubmed.ncbi.nlm.nih.gov/10456287/) | 1999 | Preclinical | Fundam Clin Pharmacol | In rat pulmonary arteries, endothelin rather than angiotensin II drives the hypoxic contractile response (weakens the rationale for hypoxic pulmonary hypertension) |

---

## South Africa Market Information

All 9 registrations are valid, single-ingredient entries in tablet form (oral). Approved indication text is not available in the data compiled for this report. Several products are lisinopril/hydrochlorothiazide combinations, judging by their names (for example, the "co" and "Lisoretic" products). Essential Medicines List status could not be determined from the available data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 33/7.1.3/0513 | Adco-zetomax | Tablet | Not available |
| 37/7.1.3/0392 | Austell-lisinopril | Tablet | Not available |
| 41/7.1.3/1050 | Lisinozide 10 Mg | Tablet | Not available |
| 37/7.1.3/0160 | Adco-zetomax co 10/12.5 | Tablet | Not available |
| 36/7.1.3/0114 | Simayla Lisinopril 20 | Tablet | Not available |

Four further registrations are not listed here: Lisoretic 20/12.5, Lisoretic 10/12.5, Zestozide 20, and Lisinopril co unicorn 10mg/12.5mg.

---

## Safety Considerations

**Contraindications and conditions of concern (from the knowledge graph, not label text):** angioedema (including hereditary and ACE-inhibitor-induced), kidney disease, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, aortic stenosis, hypotensive disorders, systemic lupus erythematosus and connective tissue disease, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, neutropenia and agranulocytosis, hyperparathyroidism and bone disease.

**Drug Interactions** (100 interactions identified; selected examples):
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel preparations (picosulfuric acid, polyethylene glycol with electrolytes)

**Additional cautions from the evidence:**
- Bilateral renal artery stenosis or a solitary kidney: ACE inhibitors can precipitate acute kidney injury.
- Renal function and potassium monitoring is required.
- A published case report describes severe hypotension and bradycardia when tizanidine is combined with lisinopril.
- Rare ACE-inhibitor-induced small bowel angioedema has been reported and can be hard to diagnose.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predictions (MI subtypes, malignant hypertension variants) are already covered by lisinopril's existing indications, so they are not new repurposing opportunities.
- Chronic pulmonary heart disease is the only genuinely new candidate with direct clinical publications, but those are small, probably uncontrolled studies with no registered trials. It is best handled as a research question and not a Go decision.
- Pulmonary hypertension due to lung disease or hypoxia has weak and partly contradictory mechanistic support.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for official warnings, contraindications and approved indications
- Mechanism of action data
- Full-text review of PMID 17047621 and 14524095 to confirm design, sample size and outcomes
- A controlled trial of lisinopril in chronic pulmonary heart disease, with renal function, potassium and blood pressure monitoring
- Confirmation of Essential Medicines List status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

