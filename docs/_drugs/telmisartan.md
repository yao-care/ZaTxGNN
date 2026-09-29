---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker (ARB) marketed in South Africa, mainly used for hypertension.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **0 clinical trials** and **0 publications** currently support this specific prediction.
Two other predicted indications, cerebral artery occlusion and intracerebral haemorrhage, have more supporting evidence and are summarised below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (general drug class knowledge; the SAHPRA registration extract contains no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Telmisartan belongs to the ARB class, which blocks the angiotensin II type 1 (AT1) receptor. Its efficacy in hypertension is well established.

Prinzmetal (vasospastic) angina is driven by coronary artery spasm. AT1 blockade could plausibly reduce vasoconstrictor tone, which is the basis for the prediction. This is a theoretical argument only. No drug-specific or disease-specific data were retrieved, and the high TxGNN score is not evidence on its own.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

---

## Other Predicted Indications With Evidence

The top-ranked prediction has the least support. Two lower-ranked predictions have more, though both remain well short of L1.

| Predicted Indication | TxGNN Score | Evidence Level | Key Evidence |
|------|------|------|------|
| Cerebral artery occlusion | 99.95% | L4 | Consistent rodent stroke-model data (smaller infarct, less oxidative stress and inflammation, PPARγ-related effects). Clinical support is indirect. [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) (Phase 4, completed, n=1228) is a telmisartan cardiovascular prevention trial, but its cerebrovascular relevance is unverified. |
| Intracerebral haemorrhage | 99.93% | L3 | [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) (TRIDENT, Phase 3, completed, n=1671) tests a telmisartan-containing triple-pill regimen for recurrent stroke prevention. Efficacy results were not retrieved, and the effect cannot be attributed to telmisartan alone. Other TRIDENT sub-studies ([NCT03783754](https://clinicaltrials.gov/study/NCT03783754), [NCT03785067](https://clinicaltrials.gov/study/NCT03785067)) were terminated with 4 and 1 participants and are uninformative. Supporting literature: the TRIDENT design paper ([PMID 34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/)) and the PRoFESS post-hoc analysis ([PMID 24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/)). |

The other seven predictions (brain stem infarction, ABri amyloidosis, three pulmonary or malignant hypertension entries, malignant hypertensive renal disease and Braddock syndrome) have no supporting evidence. The 20 publications retrieved for pulmonary hypertension owing to lung disease and/or hypoxia are generic hypoxia papers unrelated to telmisartan and were disregarded.

---

## South Africa Market Information

Five of the 17 registrations are shown. Indication text was not captured in the registration extract. The Essential Medicines List (EML) status is not available in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/7.1.3/0726 | Telmisartan 40 Unicorn | Tablet | Not stated in extract |
| Reg. No. 47/7.1.3/1120 | Tesminol 40 Mg | Tablet | Not stated in extract |
| Reg. No. 46/7.1.3/0938 | Telpres 40 | Film-coated tablet | Not stated in extract |
| Reg. No. 46/7.1.3/0928 | Tremistan Plus 80/12.5 Mg | Film-coated tablet | Not stated in extract |
| Reg. No. 50/7.1.3/0511 | Stytem 80/5 | Tablet | Not stated in extract |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One point from the prediction notes: ARBs carry a renal-safety concern in renovascular disease (for example bilateral renal artery stenosis). Any evaluation in malignant renovascular hypertension or hypertensive renal disease would need a renal safety review first.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) rests on model output alone, with no trials or publications. The better-supported directions, cerebral artery occlusion (preclinical) and intracerebral haemorrhage (indirect evidence from a combination-therapy trial), are more useful research questions than Prinzmetal angina.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings, contraindications and approved indication text
- Detailed mechanism of action data
- Any telmisartan-specific clinical evidence for vasospastic angina
- For the stroke-related predictions, TRIDENT efficacy results and a telmisartan-specific stroke trial
- A renal safety review before any evaluation in renovascular or hypertensive renal disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

