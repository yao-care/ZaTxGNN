---
layout: default
title: Quinapril
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Quinapril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

> Quinapril is an ACE inhibitor internationally used for essential hypertension and heart failure; it is **not currently registered or marketed in South Africa** (0 SAHPRA registrations).
> The TxGNN model predicts a possible link to **Malignant Renovascular Hypertension**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the drug's own rationale flags a known safety concern rather than a validated new-use hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from SAHPRA registry data (drug not marketed); internationally, quinapril (ACE inhibitor) is indicated for hypertension |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, quinapril belongs to the **ACE inhibitor (ACEi) class**, which lowers systemic blood pressure by suppressing the renin-angiotensin-aldosterone system (RAAS). Its efficacy in essential hypertension is well established internationally.

Mechanistically, the model's link between quinapril and malignant renovascular hypertension is plausible on the surface — both involve severe elevation of blood pressure mediated by RAAS activity. However, malignant renovascular hypertension is frequently caused by **bilateral (or solitary-kidney) renal artery stenosis**. In this setting, ACE inhibition dilates the efferent glomerular arteriole and can cause an abrupt drop in glomerular filtration pressure, precipitating acute kidney injury. This is a **recognized safety hazard requiring careful exclusion of renal artery stenosis**, not a novel therapeutic opportunity — the high TxGNN score reflects embedding proximity between "ACE inhibitor" and "hypertension/renal" nodes in the knowledge graph rather than a validated efficacy signal.

No clinical trial or literature evidence currently exists to support (or further characterize the risk of) this specific use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note:** This evidence pack flags a Blocking-severity data gap — SAHPRA label warnings/contraindications for quinapril are not yet available, which prevents a full initial safety assessment (S1 stage) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Quinapril is not currently marketed or registered in South Africa (0 SAHPRA licenses), and label-level safety data (warnings/contraindications) is unavailable — a blocking gap for initial safety review.
- There is no clinical trial or published literature evidence for use in malignant renovascular hypertension, and the underlying mechanistic rationale itself identifies a known ACE-inhibitor safety hazard (risk of acute kidney injury in renal artery stenosis) rather than a novel efficacy signal.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) / label warnings and contraindications for quinapril
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Any preclinical or case-level evidence specifically addressing quinapril use in confirmed vs. excluded renal artery stenosis
- A formal safety opinion before this candidate can advance past S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

