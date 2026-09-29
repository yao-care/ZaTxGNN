---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Cardiovascular Beta-Blocker to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a beta-blocker with additional alpha-1 blocking activity and is currently marketed in South Africa as an oral tablet. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**. There are currently **0 clinical trials** and **0 publications** in the Evidence Pack supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration record |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general pharmacology, carvedilol is a non-selective beta-blocker with alpha-1 blockade and vasodilatory activity, which is consistent with blood pressure lowering. Renovascular disease is driven largely by activation of the renin-angiotensin system. Beta-blockade reduces renin release, so a mechanistic link is plausible. This is a hypothesis only. The registration record has no original indication text, so the link rests on general pharmacology rather than on the supplied data.

The five predictions for this drug are not independent. Malignant renovascular hypertension and malignant hypertensive renal disease have identical scores (99.55%), and the two pulmonary hypertension entries also share one score (99.54%). This points to a shared disease-class signal rather than separate lines of evidence. The pulmonary hypertension predictions are mechanistically uncertain:
- Beta-blockade may reduce cardiac output and right-ventricular reserve.
- In patients with underlying lung disease, non-selective beta-blockade raises a bronchoconstriction concern.

Braddock syndrome (99.37%) has no clear mechanistic link. It most likely reflects graph proximity to cardiovascular phenotypes and should be treated as hypothesis-generating only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/7.1.3/0281 | Carvedilol unicorn | Tablet (oral) | Not stated in the record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug interaction query returned no results, which reflects missing data rather than an absence of interactions. For the pulmonary hypertension predictions, the risks of reduced cardiac output and bronchoconstriction would need review before any further consideration.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or publications, and the mechanistic link is plausible but unverified. The identical scores across paired predictions suggest overlapping rather than independent signals.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which blocks the safety screening step
- Mechanism of action data from DrugBank
- A systematic search of trials and literature for carvedilol in renovascular and malignant hypertension
- A dedicated safety review for the pulmonary hypertension and lung disease predictions
- Confirmation of the original registered indication for this product

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

