---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ramipril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertension"
monitor_inn: "RAMIPRIL"
predicted_indications: ["malignant hypertensive renal disease", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis"]
---

# Ramipril
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

# Ramipril: From Hypertension to Pulmonary Hypertension (Hypoxia-Related)

## One-Sentence Summary

Ramipril is an ACE inhibitor originally used for hypertension and for reducing stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension**. The top-ranked prediction has no supporting studies, so this report focuses on the second-ranked prediction, **pulmonary hypertension owing to lung disease and/or hypoxia**, which has **no clinical trials** and **only one directly relevant preclinical publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the SAHPRA registration data compiled for this report contain no approved indication text; the original indications come from the TxGNN knowledge graph: hypertensive disorder, stroke and cerebrovascular disorders) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia (rank 2; rank 1 is pulmonary hypertension with unclear multifactorial mechanism) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 (preclinical evidence only; rank 1 is L5) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 7 |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Ramipril is a well-known ACE inhibitor: it blocks the conversion of angiotensin I to angiotensin II, which lowers vascular tone and can reduce vascular remodelling. This is general pharmacology, not drawn from the compiled data.

The link to pulmonary hypertension is plausible. Angiotensin II signalling could influence pulmonary vascular tone and remodelling under chronic hypoxia. One rat study (PMID 9200213) found that ramipril given during three weeks of hypoxia lowered baseline perfusion pressure in isolated lungs and attenuated the effects of chronic hypoxia on the pulmonary vessels.

This is a mechanistic hypothesis supported by a single animal study. Most of the other retrieved papers are off-topic or tangential (myocardial infarction, renal capillaries, radiation brain necrosis, an unrelated Cushing's disease case report), and no human data exist for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Only publications relevant to the predicted indication are listed; the other retrieved papers were off-topic.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (rat) | Physiological Research | Ramipril 10 mg/kg daily during 3 weeks of hypoxia attenuated the effects of chronic hypoxia on pulmonary vessels and lowered baseline perfusion pressure in isolated lungs |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclinical/Translational | European Heart Journal | ACE2 expression rises after myocardial infarction in rats and humans; indirect relevance to the renin-angiotensin system and hypoxia |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclinical (transgenic rat) | Am J Physiol Regul Integr Comp Physiol | Renin-angiotensin system and cardiac function during hypoxia-reoxygenation; indirect relevance |

---

## South Africa Market Information

All seven registrations are valid single-ingredient entries. No approved indication text is available in the data compiled for this report. Essential Medicines List (EML) status is not stated in the data and should be confirmed.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| W/7.1.3/232 | Ramiwin 1.25 Mg | Capsule | Not available in compiled data |
| A39/7.1.3/0242 | Austell-ramipril | Capsule | Not available in compiled data |
| A39/7.1.3/0239 | Austell-Ramipril 1.25Mg | Capsule | Not available in compiled data |
| 31/7.1/0677 | Tri-plen 2.5mg/2.5mg | Tablet | Not available in compiled data |
| 44/7.1/0612 | Co Ramiwin 2.5/12.5 Mg | Tablet | Not available in compiled data |

Two further registrations (44/7.1/0613 Co Ramiwin 5/12.5 Mg and 43/7.1/1129 Tritace Plus 5/25 Mg, both tablets) are also valid. All products are oral.

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), neutropenia, agranulocytosis, hereditary angioedema, hypotensive disorders, connective tissue disease, scleroderma/systemic sclerosis, bone and cartilage disease, renal artery obstruction and pyoureter. These should be verified against the PI.

**Drug interactions (100 recorded; examples from the first 20 shown):**
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aspirin, morphine, bupropion, and glucose-lowering agents (metformin, glimepiride, chlorpropamide, alogliptin, canagliflozin, dapagliflozin, empagliflozin)

---

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The prediction score is very high, but the only support is a single 1996 rat study. There are no clinical trials or human data. Other predictions fare no better: most (e.g. malignant renovascular hypertension, malignant hypertensive renal disease, brain stem infarction) are L5 with no evidence. Intracerebral haemorrhage and cerebral artery occlusion reach L4 but with preclinical data only, and those for cerebral artery occlusion are mixed. Blood pressure lowering by ramipril could also be a concern in patients with pulmonary hypertension.

**To proceed, the following is needed:**
- Obtain the SAHPRA PI (warnings, contraindications and approved indications), which is a blocking data gap
- Detailed mechanism of action data
- Confirmatory preclinical work in modern pulmonary hypertension models, followed by a small human haemodynamic study if results are positive
- A safety assessment covering hypotension, renal function and hyperkalaemia in pulmonary hypertension patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

