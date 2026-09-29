---
layout: default
title: Labetalol
parent: Moderate Evidence (L3-L4)
nav_order: 282
evidence_level: L4
indication_count: 4
---

# Labetalol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Labetalol: From Severe Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is an oral blocker of alpha-1 and beta receptors, already used for severe hypertension and hypertensive emergencies.
The TxGNN model predicts it may be useful for **malignant renovascular hypertension**.
The supporting evidence is weak: **no clinical trials** and **2 indirect case-report publications**, neither of which tests labetalol in renovascular disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration record (the pack describes labetalol as used for severe hypertension and hypertensive emergencies) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Labetalol combines alpha-1 blockade with non-selective beta blockade, and it is already used in hypertensive emergencies. Lowering blood pressure is therefore mechanistically plausible in malignant hypertension.

Renovascular hypertension, however, is driven mainly by activation of the renin-angiotensin system. No direct data show that labetalol works or is safe in this setting, for example in bilateral renal artery stenosis or where the kidney depends on perfusion pressure. The high score (0.991) most likely reflects the drug's general antihypertensive class effect rather than a disease-specific mechanism.

The model also ranked three related conditions highly, but none has usable support:
- **Malignant hypertensive renal disease** (99.08%): prediction only, with no trials or literature. It is closely related to the lead prediction, so it probably reflects the same graph signal. Effects on GFR and renal perfusion have not been assessed.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.08%): no evidence. Benefit from systemic antihypertensive action cannot be assumed, and beta blockade may blunt right ventricular compensation.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.08%): the 20 retrieved papers are general hypoxia biology (neurodegeneration, cancer, altitude) and do not study labetalol. Non-selective beta-2 blockade could also worsen bronchospasm in chronic lung disease.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR entries were not found in the Evidence Pack).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | Malignant hypertension in a young man after hallucinogen use, with drug-induced arteritis in the renal vessels. Blood pressure was controlled initially with minoxidil and labetalol, and the arteritis responded to prednisone. |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case report | BMC Nephrol | Hyponatraemic hypertensive syndrome (renovascular hypertension with hyponatraemia) presenting as malignant hypertension in an 18-month-old child. Labetalol is not evaluated. |

Both papers are indirect. Neither tests labetalol in renovascular hypertension.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. J/7.1.3/52 | Trandate | Tablet (oral) | Not stated in the registration record |

Essential Medicines List (EML) inclusion status is not available in the Evidence Pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Theoretical concerns for the predicted indications, from the mechanistic analysis and not from label data:
- Renal perfusion may be compromised in renovascular disease.
- Non-selective beta-2 blockade may worsen bronchospasm in chronic lung disease.
- Beta blockade may impair right ventricular compensation in pulmonary hypertension.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and two indirect case reports. There are no trials, and the drug's mechanism does not directly address the renin-driven pathophysiology of renovascular hypertension. Renal perfusion is also a safety concern. The Evidence Pack lacks safety data from the SAHPRA package insert, which blocks progression to safety screening. Suitable as a research question only.

**To proceed, the following is needed:**
- Warnings and contraindications from the SAHPRA package insert (blocking)
- Mechanism of action data, for example from DrugBank
- Labetalol-specific evidence in renovascular or malignant hypertensive renal disease, including effects on renal function
- Clarification of the approved indication text for Reg. No. J/7.1.3/52
- Drug interaction data, as the query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

