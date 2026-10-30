---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 9
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
last_modified_at: 2026-10-30
description: "Ramipril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L4). Approved use: Hypertension and stroke-related conditions"
---

# Ramipril
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

## Ramipril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia
{: .text-alpha }

## One-Sentence Summary

Ramipril is an ACE inhibitor. The TxGNN model (deep learning) predicts it may be useful for **pulmonary hypertension owing to lung disease and/or hypoxia** (score 0.9993). This score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence. **No clinical trials** and only **one directly relevant animal study** (from 1996) currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and stroke-related conditions (relations recorded in the knowledge graph; South African licence records contain no indication text) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 7) |
| Number of SAHPRA Registrations | 7 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ramipril is known as an ACE inhibitor. By reducing angiotensin II, it may lessen vasoconstriction and vascular remodelling, which are processes thought to contribute to hypoxic pulmonary vasoconstriction.

The strongest supporting study is a 1996 rat experiment (PMID 9200213). In it, ramipril given during three weeks of chronic hypoxia was associated with lower baseline perfusion pressure in the pulmonary vessels. This directly studies hypoxic pulmonary hypertension, but only in animals and it is now dated. The other retrieved papers concern myocardial infarction, kidney capillaries, radiation-induced brain necrosis and similar topics, so they support the prediction only indirectly.

The link between systemic hypertension and pulmonary hypertension is a shared renin-angiotensin pathway. This is a plausible hypothesis, not demonstrated clinical benefit in people.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (animal) | Physiological Research | In rats exposed to chronic hypoxia, ramipril lowered baseline pulmonary perfusion pressure and attenuated hypoxia-induced changes in pulmonary vessels |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | Preclinical (animal) | Am J Physiol Regul Integr Comp Physiol | Renin-angiotensin system and heart muscle tolerance to hypoxia-reoxygenation; indirect relevance |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | Preclinical / human tissue | European Heart Journal | ACE2 expression increases after myocardial infarction; indirect relevance |
| [19380417](https://pubmed.ncbi.nlm.nih.gov/19380417/) | 2009 | Preclinical (animal) | Cardiovascular Research | ACE inhibition promoted endothelial progenitor cells and new vessel growth in cardiac pressure overload; indirect relevance |
| [24907870](https://pubmed.ncbi.nlm.nih.gov/24907870/) | 2014 | Preclinical (animal) | Basic Research in Cardiology | Soluble guanylyl cyclase activation versus ACE inhibition after myocardial infarction; indirect relevance |

---

## South Africa Market Information

All 7 registrations are valid. The records contain no approved-indication text. Note that 4 of the 7 are combination-type products (ramipril with hydrochlorothiazide or other agents, judging by product names); their licences do not describe how single-ingredient ramipril is approved. Essential Medicines List status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| W/7.1.3/232 | Ramiwin 1.25 Mg | Capsule | Not stated in the records |
| A39/7.1.3/0242 | Austell-ramipril | Capsule | Not stated in the records |
| A39/7.1.3/0239 | Austell-Ramipril 1.25Mg | Capsule | Not stated in the records |
| 31/7.1/0677 | Tri-plen 2.5mg/2.5mg | Tablet | Not stated in the records |
| 44/7.1/0612 | Co Ramiwin 2.5/12.5 Mg | Tablet | Not stated in the records |

---

## Safety Considerations

**Relations recorded in the knowledge graph (not label text).** The knowledge graph records contraindication relations with the following conditions: kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, neutropenia, agranulocytosis, hereditary angioedema, hypotensive disorder, connective tissue disease, scleroderma and systemic sclerosis, renal artery obstruction, and bone and cartilage diseases.

**Drug interactions.** The interaction check returned 100 entries in total; the main ones listed are:
- **Major:** potassium citrate and potassium bicarbonate (risk of raised potassium)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, morphine, bupropion, and several diabetes medicines (metformin, glimepiride, chlorpropamide, alogliptin, and the gliflozins canagliflozin, dapagliflozin and empagliflozin)

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct support is a single dated rat study, with no registered clinical trials. Evidence therefore sits at an early, preclinical stage, and the safety and label information for South Africa has not yet been reviewed.

**To proceed, the following is needed:**
- Review of the SAHPRA package insert for warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Contemporary preclinical confirmation, followed by a registered clinical study in pulmonary hypertension due to lung disease or hypoxia
- Safety assessment in this population, given that low blood pressure and kidney disease are recorded as contraindication relations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

