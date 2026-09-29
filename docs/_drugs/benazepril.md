---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 5
---

# Benazepril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Benazepril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Benazepril is an ACE inhibitor. Its original indication is not recorded in the supplied registration data, but it is a known blood pressure drug. The TxGNN model predicts it may be useful for **malignant renovascular hypertension**. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration record (general pharmacology: hypertension) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied dataset. Benazepril is an ACE inhibitor, and this class blocks the renin-angiotensin-aldosterone system (RAAS). The reasoning below therefore comes from general pharmacology, not from the supplied data.

Renovascular hypertension is driven largely by renin release from an under-perfused kidney. Blocking RAAS is biologically plausible in this setting, so the prediction is not unreasonable. However, the TxGNN score is a computational prediction only, and no trial or publication was found to confirm it.

Two safety concerns matter for this indication:
- ACE inhibitors can reduce kidney function in patients with bilateral renal artery stenosis.
- This risk would need careful review before any further step.

The other predictions are weaker:
- **Malignant hypertensive renal disease** has an identical score (99.65%). It is likely a closely related graph node, so it is not independent support.
- **Pulmonary hypertension** (two forms) has a score of 99.60%. The 20 retrieved publications are generic hypoxia literature, and none of the ten titles shown mentions benazepril, ACE inhibitors, or pulmonary hypertension treatment.
- **Braddock syndrome** (99.44%) has no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR entries were not supplied).

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/7.1.3/0121 | Cibadrex 10 10mg/12.5mg | Tablet (oral) | Not stated in the registry record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature (L5, model prediction only). Safety information from the SAHPRA package insert has not been reviewed, and this blocks further screening. There is also a known renal safety concern for ACE inhibitors in renovascular disease.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), downloaded and reviewed
- Mechanism of action data, for example from DrugBank
- A targeted search for benazepril or ACE inhibitor studies in renovascular hypertension
- A review of renal risk in patients with bilateral renal artery stenosis
- Confirmation of the approved indication text for the registered product

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

