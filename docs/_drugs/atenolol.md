---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Atenolol: From Beta-Blocker Therapy to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-1 selective blocker marketed in South Africa in several oral tablet products. The TxGNN model predicts it may be useful for **posterolateral myocardial infarction (MI)**, but **no clinical trials and no publications** were found for this specific indication. The prediction rests on model output and biological plausibility alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration records supplied |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the supplied rationale, atenolol is a beta-1 selective blocker. It lowers heart rate, myocardial contractility and myocardial oxygen demand. It is registered here as a cardiovascular tablet, alone and in two products that appear to be fixed-dose combinations.

Reducing oxygen demand is a biologically sensible goal in a heart muscle injured by MI. The same logic applies to other MI locations, and the model gave near-identical scores to related MI subtypes (posteroinferior, septal). This is a plausibility argument, not evidence of benefit. Nothing supplied shows atenolol improves outcomes in posterolateral MI specifically. The model score also cannot say whether the benefit outweighs the risks in this setting.

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication. No SANCTR or PACTR entries were supplied either.

## Literature Evidence

Currently no related literature available for this indication.

## Evidence for Other Predicted Indications

The pack lists eight further predictions. Only three have any supporting material, and all of it is indirect.

| Predicted Indication | Score | Evidence Level | Supporting Material | Assessment |
|------|------|------|------|------|
| Posteroinferior MI | 99.87% | L4 | [PMID 3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) (1985, Rev Med Interne): single-blind crossover trial of atenolol vs diltiazem in 23 patients with residual ischaemia after posteroinferior or anterior MI | Small, dated, and it studies exercise-induced ischaemia rather than MI outcomes |
| Malignant renovascular hypertension | 99.85% | L4 | [PMID 18454714](https://pubmed.ncbi.nlm.nih.gov/18454714/) (2008, Nefrologia): case report of a teenager with type 1 neurofibromatosis, aortic coarctation and renal artery stenosis | Cannot support efficacy. The pack's rationale text mislabels this patient as having type 1 diabetes. |
| Chronic pulmonary heart disease | 99.04% | L4 | [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) (REDUCE-SWEDEHEART, Phase 4, 5,000 patients, active not recruiting), plus mostly indirect papers on beta-blockers in COPD and hypertension | The trial covers post-MI beta-blocker discontinuation, not this disease, and does not name atenolol. It is a tangential match (grade C). |

The remaining predictions (malignant hypertensive renal disease, two forms of pulmonary hypertension, septal MI, Braddock syndrome) are prediction only. For pulmonary hypertension, the pack notes that negative inotropy could harm right ventricular function.

## South Africa Market Information

Six registrations are recorded, and five were supplied in detail. The approved indication text is empty in all supplied records, and the Essential Medicines List status is not in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/5.2/0005 | Gulf atenolol | Tablet | Not stated in supplied record |
| Reg. No. A38/5.2/0502 | Tenopress | Tablet | Not stated in supplied record |
| Reg. No. 32/5.2/0670 | B-block | Tablet | Not stated in supplied record |
| Reg. No. Y/7.1.3/24 | Sandoz Co-Tenidone 50/12.5 | Tablet | Not stated in supplied record |
| Reg. No. S/7.1.3/201 | Tenoret 50 50mg/12.5mg | Tablet | Not stated in supplied record |

All products are oral tablets, so no route-of-administration barrier is evident. This is provisional, because route compatibility has not been assessed for the predicted indication.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The evidence pack raises two indication-specific cautions for the wider prediction set. Beta-blockers need care in bilateral renal artery stenosis. Negative inotropy may harm right ventricular function in pulmonary hypertension. Neither applies directly to posterolateral MI. A drug interaction query returned no results, which is not the same as no interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.87% TxGNN score is high, but it is the only support for posterolateral MI. There are no trials or publications (L5), and the SAHPRA package insert safety data have not been reviewed. That safety gap blocks progression to safety screening.

**To proceed, the following is needed:**
- Download and parse the SAHPRA package inserts to capture approved indications, warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Run a targeted search for atenolol in MI, including contemporary trials, and confirm whether the 1985 crossover study has any relevance to MI outcomes
- Review post-MI beta-blocker evidence, including REDUCE-SWEDEHEART results once available, for direct bearing on atenolol
- Confirm whether the predicted indication is distinct from the approved cardiovascular indications

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

