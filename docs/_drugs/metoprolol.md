---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker (beta-blocker) that is already marketed in South Africa as Lopresor tablets, and it is used as an antihypertensive.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **2 publications**, neither of which studies metoprolol for this condition. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the SAHPRA registration record supplied has no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, metoprolol is a beta-1 selective blocker. Beta-1 blockade lowers renin release from the kidney and reduces cardiac output, so a link to renin-driven hypertension is plausible.

Renovascular hypertension is driven largely by activation of the renin-angiotensin system when the kidney is under-perfused. The malignant form is a severe, rapidly progressive variant. Because metoprolol already lowers blood pressure and renin activity, the model's prediction is biologically reasonable.

This is a mechanistic argument only. No trial or on-topic publication supports metoprolol in this condition. Malignant hypertension is also a much more acute and severe state than routine hypertension, so efficacy in ordinary hypertension cannot simply be assumed to carry over.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15231398](https://pubmed.ncbi.nlm.nih.gov/15231398/) | 2004 | Review/Commentary | Survey of Ophthalmology | Case of a 26-year-old woman with hypertensive optic neuropathy caused by renal artery stenosis from Takayasu's arteritis. Metoprolol is not studied. |
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Cohort | Medicine | Chromogranin A as a diagnostic marker for pheochromocytoma in the differential diagnosis of hypertension. Metoprolol is not studied. |

Both papers are only loosely related to the topic. They concern the causes and diagnosis of secondary hypertension, not treatment with metoprolol.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H/5.2/72 | Lopresor | Tablet (oral) | Not stated in the available record |

The Evidence Pack does not include Essential Medicines List (EML) status for metoprolol, so it is not reported here.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no on-topic literature. The mechanism is plausible but unverified. The SAHPRA package insert warnings and contraindications have not been reviewed, so the safety screening cannot proceed.

Other high-scoring predictions for metoprolol do not change this assessment:
- Post-myocardial-infarction subtypes are already covered by its established use, so they are not true repurposing.
- Pulmonary hypertension and chronic pulmonary heart disease carry a caution. The metoprolol COPD trial (BLOCK-COPD, NCT02587351) was terminated for futility and showed a harm signal for severe exacerbations.

**To proceed, the following is needed:**
- The SAHPRA package insert (Professional Information) for Lopresor, to obtain warnings, contraindications and the approved indication text. This is the blocking item.
- Mechanism of action data from DrugBank.
- Searches for disease-specific evidence in malignant and renovascular hypertension, including trials and case series.
- Clinical review of whether an oral beta-blocker has a role in an acute hypertensive emergency and in renal artery stenosis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

