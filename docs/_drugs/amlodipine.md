---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amlodipine: predicted new indication Brain stem infarction (evidence level L5). Approved use: Hypertension"
monitor_inn: "AMLODIPINE"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a calcium channel blocker, originally used to treat hypertension, stroke-related conditions and Prinzmetal angina.
The TxGNN model's top-ranked prediction is **brain stem infarction**, but this prediction has **no clinical trials and no publications** behind it.
The best-supported repurposing direction in the data is **intracerebral haemorrhage** (secondary prevention), with **4 clinical trials** and **10 publications**, including a completed Phase 3 RCT of a triple-pill combination that contains amlodipine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (SAHPRA indication text is not available in the data compiled for this report; original indications are taken from the knowledge graph: hypertensive disorder, stroke disorder, cerebral infarction, Prinzmetal angina) |
| Predicted New Indication | Brain stem infarction (rank 1); intracerebral haemorrhage (rank 10) is the best-supported prediction |
| TxGNN Prediction Score | 99.94% (brain stem infarction); 99.79% (intracerebral haemorrhage) |
| Evidence Level | L5 for brain stem infarction; L1 for intracerebral haemorrhage (combination therapy, not amlodipine alone) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold for brain stem infarction; Proceed with Guardrails for intracerebral haemorrhage |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Amlodipine is a dihydropyridine calcium channel blocker. It relaxes vascular smooth muscle, lowers blood pressure and may protect the cerebral vasculature. Its efficacy in hypertension is established, and it is already linked to stroke and cerebral infarction indications.

**Brain stem infarction** overlaps closely with the existing cerebral infarction and stroke indications. The high TxGNN score probably reflects network proximity to these approved uses. There is no trial or literature evidence specific to brain stem infarction.

**Intracerebral haemorrhage (ICH)** is a different situation. Intensive blood pressure control is central to preventing recurrent stroke after ICH. Amlodipine is one of three low-dose agents in the TRIDENT triple-pill regimen. This is a population extension of the approved hypertension and stroke indications rather than a wholly new use. The benefit cannot be attributed to amlodipine alone.

Other predictions in the list (pulmonary hypertension variants, malignant hypertensive renal disease, malignant renovascular hypertension, cerebral artery occlusion, MRI-defined brain infarct, Braddock syndrome, ABri amyloidosis) are either model predictions only or supported by preclinical or anecdotal data. For hypoxic lung disease, vasodilators can worsen ventilation-perfusion mismatch, and amlodipine-related hypoxia has been reported (PMID 36856509).

---

## Clinical Trial Evidence

The rank 1 prediction (brain stem infarction) has no registered trials. The trials below relate to intracerebral haemorrhage (rank 10).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT: double-blind RCT of a low-dose triple antihypertensive pill (including amlodipine) versus standard care for preventing recurrent stroke after ICH |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | NA | Recruiting | 140 | Triple antihypertensive medication after ICH for blood pressure control (TRICH score); early and small |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; no usable data |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; no usable data |

Of the trials found for cerebral artery occlusion (rank 6), NCT00805311 (Phase 4, carotid endarterectomy versus medical treatment, terminated, n=400) does not test amlodipine specifically.

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | Three low-dose antihypertensives in a single pill after ICH, assessed for blood pressure lowering and recurrent stroke risk (only the background is available in the data; outcomes need to be confirmed from the full text) |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design/rationale | Int J Stroke | TRIDENT rationale, design and progress |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonists in hypertension: lower systemic vascular resistance |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with haemorrhagic stroke (safety signal) |
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical (animal) | J Neurosci Res | Amlodipine plus atorvastatin were neuroprotective after transient MCAO in rats |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical (animal) | Am J Hypertens | Amlodipine reduced stroke size in ApoE-deficient mice |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Preclinical (animal) | Brain Res | Calcium channel blockers with antioxidative effects reduced neuronal damage after focal ischaemia in rats |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Preclinical (animal) | Brain Res | Synergistic neuroprotection with amlodipine plus atorvastatin after stroke in rats |
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Preclinical (animal) | Eur J Pharmacol | Amlodipine attenuated pulmonary vascular remodelling in hypoxic rats |
| [10759437](https://pubmed.ncbi.nlm.nih.gov/10759437/) | 2000 | Crossover trial | Eur Respir J | Amlodipine versus placebo on respiratory and pulmonary vascular responses to hypoxia in 14 mountaineers |

Literature specific to brain stem infarction was not found.

---

## South Africa Market Information

Amlodipine has 20 valid SAHPRA registrations, all marketed. Approved indication text is not available in the data compiled for this report. Essential Medicines List (EML) status is also not available in the data. Many entries are fixed-dose combinations (for example with valsartan, atorvastatin, perindopril or telmisartan), although the data classifies them as single-ingredient. The five main registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38/7.1/0183 | Amloc | Tablet | Please refer to the Professional Information (PI) |
| A39/7.1/0532 | Amlodac | Tablet | Please refer to the PI |
| A39/7.1/0545 | Austell-amlodipine | Tablet | Please refer to the PI |
| 41/7.1.3/0291 | Exforge 5mg/160mg | Tablet | Please refer to the PI |
| A39/7.0/0326 | Caduet 5mg/10mg | Tablet | Please refer to the PI |

---

## Safety Considerations

SAHPRA package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for definitive safety information. Report adverse drug reactions to SAHPRA.

The following signals come from the knowledge graph and the retrieved literature, not from label text:

- **Conditions flagged in the knowledge graph as contraindication-related:** liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, hypothyroidism, angioedema (including hereditary and RAAS-blocker-induced forms), systemic lupus erythematosus, myopathy and muscle disease, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, hypotensive disorder, and hyperparathyroidism. These should be verified against the PI before use.
- **Angioedema:** a case report links amlodipine to angioedema (PMID 19299323).
- **Overdose:** amlodipine overdose has been associated with hypotension and non-cardiogenic pulmonary oedema with alveolar haemorrhage (PMID 35261597).
- **Hypoxia:** a case report describes hypoxia during one-lung ventilation attributed to inhibition of hypoxic pulmonary vasoconstriction (PMID 36856509).
- **Drug interactions:** 100 interactions were found (all those listed are Moderate severity). The main ones include corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), aprepitant, acetylsalicylic acid, bupropion, calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate, phosphate and others), canagliflozin, dapagliflozin, clarithromycin and clotrimazole.

---

## Conclusion and Next Steps

**Decision: Hold** for brain stem infarction (the top-ranked prediction).
**Decision: Proceed with Guardrails** for intracerebral haemorrhage (secondary prevention, as part of a triple-pill combination).

**Rationale:**
- Brain stem infarction is supported only by the model score and its proximity to existing stroke and cerebral infarction indications. There are no trials or publications, so it remains at L5.
- For intracerebral haemorrhage, a completed Phase 3 RCT (TRIDENT, n=1,671) supports a triple low-dose pill that includes amlodipine. The benefit applies to the combination, not to amlodipine alone, and it is a population extension of the existing hypertension and stroke uses. Only one completed Phase 3 trial supports this, so the L1 grade (which requires at least two completed Phase 3 RCTs) should be regarded as provisional.

**To proceed, the following is needed:**
- Full-text confirmation of the TRIDENT outcomes (PMID 42019018), including the effect on recurrent stroke and the safety profile.
- SAHPRA package insert warnings, contraindications and approved indication text for all registered amlodipine products.
- Mechanism of action data from DrugBank.
- Assessment of whether the triple-pill combination is available or registered in South Africa, or whether the regimen can be reproduced with registered components.
- Safety monitoring plan covering hypotension and angioedema, with limitation to the post-ICH setting rather than acute-phase use.
- For brain stem infarction and other lower-ranked predictions, prospective or observational data would be needed before reconsidering the Hold decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

