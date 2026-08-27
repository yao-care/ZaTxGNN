---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Ramipril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ramipril: From ACE Inhibitor Therapy (Hypertension) to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Ramipril (DrugBank DB00178) is a well-established angiotensin-converting enzyme (ACE) inhibitor; specific SAHPRA-registered indication text is not available in this evidence pack because the product is currently **not marketed** in South Africa. The TxGNN model's top-ranked prediction is **pulmonary hypertension with unclear multifactorial mechanism**, but this candidate is currently supported by **zero clinical trials and zero publications** — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from SAHPRA registry data (product not marketed); as an ACE inhibitor, ramipril's globally established indications are hypertension, heart failure and cardiovascular risk reduction |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ramipril is flagged as a data gap in this evidence pack. Based on generally known pharmacology, ramipril is an ACE inhibitor that suppresses the renin-angiotensin-aldosterone system (RAAS), and its efficacy in hypertension and cardiovascular risk reduction is well established.

However, for this specific top-ranked candidate — pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) — the evidence pack's own repurposing rationale is explicit: *"TxGNN gives a high score but there is no trial or literature support, and the mechanism of this indication itself is not clearly defined, so no concrete pharmacological hypothesis can be established."* In other words, because this WHO Group 5 category is defined by heterogeneous and unclear mechanisms, RAAS inhibition cannot currently be mapped to a specific pathophysiological rationale for this indication.

By contrast, other TxGNN-predicted indications for ramipril in this evidence pack (not detailed further below, since this report follows the top-ranked candidate) have much clearer mechanistic links — for example, malignant renovascular hypertension (RAAS-driven, direct ACEI mechanism) and cerebral artery occlusion (supported by a completed Phase 2 trial and human cohort data). These may warrant separate evaluation if a viable repurposing candidate is the goal (see Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Ramipril has **0 SAHPRA registrations** in this evidence pack, and market status is recorded as **Not Marketed**. No product licences, dosage forms, or approved indication text are currently available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: Retrieval of PI-based warnings/contraindications is flagged in this evidence pack as a Blocking data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension with unclear multifactorial mechanism) has no supporting clinical trials or literature and no established mechanistic hypothesis — evidence level L5. Combined with the product's Not Marketed status in South Africa (0 registrations) and a Blocking data gap on safety/PI data, there is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/SAHPRA Professional Information (PI) warnings, precautions and contraindications (DG001, Blocking)
- Confirmed mechanism of action via DrugBank API (DG002, High)
- Dedicated clinical or preclinical studies of ramipril specifically in WHO Group 5 pulmonary hypertension
- If the goal is to identify a viable repurposing candidate for ramipril generally, consider prioritising other predictions in this evidence pack with stronger evidence — notably **cerebral artery occlusion** (rank 10, evidence level L2, one completed Phase 2 trial plus a human cohort study and multiple animal studies) and **malignant renovascular hypertension** (rank 3, L4, strong direct RAAS mechanistic link) — over the current top-ranked but evidence-free candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

