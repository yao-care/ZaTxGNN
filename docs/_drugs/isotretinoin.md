---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Dermatological Use (Original Indication Not Recorded) to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is a retinoid registered in South Africa as an oral capsule (Oratane 5Mg) and a topical gel (Isotrex), but the registration data do not state its approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension** and **malignant hypertensive renal disease**.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data provided |
| Predicted New Indication | Malignant renovascular hypertension (a second prediction, malignant hypertensive renal disease, has the same score) |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and the original indication is not recorded in the data provided. Isotretinoin is a retinoid, and this is the only mechanistic starting point available.

A speculative link exists through retinoid signalling. Preclinical work has reported that retinoic acid can modulate renin expression and renal inflammation or fibrosis. That could in theory touch the renin-angiotensin system, which is central to renovascular hypertension. **This link was not verified against the provided data. It does not show that isotretinoin lowers blood pressure or protects the kidney.**

The two predicted diseases have identical scores (99.01%, ranks 4772 and 4773). They probably come from the same overlapping disease neighbourhood in the knowledge graph, so they should be read as one weak signal, not two independent ones.

## Clinical Trial Evidence

Currently no related clinical trials registered. No ClinicalTrials.gov, ICTRP, SANCTR or PACTR entries were found for either predicted indication.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/13.4.2/0746 | Oratane 5Mg | Capsule (oral) | Not stated in the data provided |
| Reg. No. 29/13.12/0027 | Isotrex | Gel (topical) | Not stated in the data provided |

Essential Medicines List (EML) status was not included in the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Isotretinoin is known to be teratogenic and can cause dyslipidaemia, so hepatic and lipid monitoring would be a concern. No data were provided on its use in renovascular disease or severe renal impairment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score. There are no trials or publications, and the mechanism and original indication are not documented. The known safety profile (teratogenicity, lipid effects) is a further reason for caution in a severely ill hypertensive population.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (indications, warnings, contraindications), which currently blocks safety screening
- Mechanism of action data, for example from DrugBank
- A systematic literature search on retinoids and renin, renal fibrosis or hypertension, followed by preclinical validation
- A safety assessment for patients with severe hypertension and renal impairment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

