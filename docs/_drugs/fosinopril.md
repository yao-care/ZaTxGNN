---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 239
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: From Hypertension (Registered Product) to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril is an ACE inhibitor marketed in South Africa, but the Evidence Pack does not record an approved indication text for the local product.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but currently there are **0 clinical trials** and **0 relevant publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (the SAHPRA registration has no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fosinopril is an ACE inhibitor (angiotensin-converting enzyme inhibitor). Renovascular hypertension is driven by activation of the renin-angiotensin-aldosterone system (RAAS), so blocking this pathway is biologically plausible.

The same reasoning applies to the second-ranked prediction, malignant hypertensive renal disease, where RAAS blockade is relevant to hypertensive kidney injury. However, both predictions have exactly the same TxGNN score (99.87%). This suggests they share a neighbourhood in the knowledge graph rather than representing two independent lines of support.

Safety is the key concern. ACE inhibitors can precipitate renal failure in patients with bilateral renal artery stenosis or a solitary kidney, which is the very population in renovascular hypertension. Any follow-up would need to address renal function and hyperkalaemia risk.

The other predictions are much weaker:
- **Pulmonary hypertension (unclear multifactorial mechanism):** No clear mechanistic rationale. ACE inhibition is not an established therapy for pulmonary hypertension, and systemic vasodilation carries a risk of hypotension.
- **Pulmonary hypertension owing to lung disease and/or hypoxia:** The 20 retrieved records are general hypoxia papers found by keyword matching. None of the titles shown mention fosinopril, ACE inhibitors or pulmonary hypertension, so they are not counted as supporting evidence. Vasodilators can worsen ventilation-perfusion matching in hypoxic lung disease.
- **Braddock syndrome:** No mechanistic link to ACE inhibition could be identified. The high score likely reflects graph proximity rather than a validated pharmacological rationale.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/7.1.3/0416 | Monozide | Tablet (oral) | Not recorded in the supplied data |

Essential Medicines List (EML) inclusion status is not available in the supplied data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (Evidence Level L5), with no registered clinical trials and no relevant literature. The SAHPRA safety information has not been obtained, and the renal risks of ACE inhibitors in renovascular disease are significant. The pulmonary hypertension and Braddock syndrome predictions have no supportable mechanism.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) for Monozide, including warnings, contraindications and the approved indication (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature search specific to ACE inhibitors in renovascular hypertension and malignant hypertension, with attention to renal outcomes
- Safety assessment for renal artery stenosis, solitary kidney, renal function and hyperkalaemia
- Confirmation of whether the combination product (Monozide) contains other active ingredients, since the registration details are limited

Please report adverse drug reactions to SAHPRA.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

