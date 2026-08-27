---
layout: default
title: Fosinopril
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 5
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril (DrugBank DB00492) is an ACE inhibitor; the evidence pack does not contain a confirmed original indication text, but ACE inhibitors are conventionally used to treat hypertension and related cardiovascular/renal conditions. The TxGNN model predicts potential efficacy for **Malignant Renovascular Hypertension**, but currently **no clinical trials** and **no published literature** support this specific prediction — it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (Fosinopril is pharmacologically classified as an ACE inhibitor; no confirmed indication text was returned) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, fosinopril is an ACE inhibitor, working by suppressing the renin-angiotensin system to lower angiotensin II levels, reduce vascular resistance, and lower blood pressure.

Mechanistically, ACE inhibitors as a class are plausible candidates for hypertension-related renal conditions. However, malignant renovascular hypertension is frequently associated with bilateral renal artery stenosis — a setting in which ACE inhibitors are a recognised class-level risk factor for acute kidney function deterioration and are often listed as a warning or contraindication. This is an important mechanistic caution rather than a supporting rationale: the predicted benefit (blood pressure and renin-angiotensin control) and a known class-specific harm (risk of acute renal impairment in bilateral stenosis) apply to the same population.

No clinical trials or literature specific to fosinopril in this indication were identified, so this mechanistic reasoning has not been empirically validated for this specific disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registrations are recorded for this drug in the evidence pack (0 licenses; market status: Not Marketed). No product/dosage-form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: TFDA-equivalent label warnings/contraindications for this drug are flagged in the source data as a **Blocking** data gap — a formal safety review (including bilateral renal artery stenosis contraindication status) cannot be completed until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score (L5 evidence) with zero clinical trials or literature, and the mechanistic pathway carries a known class-level renal safety concern (bilateral renal artery stenosis) directly relevant to this indication. The drug is also not currently marketed in South Africa.

**To proceed, the following is needed:**
- Official product label / Professional Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank
- Targeted literature/clinical trial search specific to fosinopril and renovascular hypertension or hypertensive renal disease
- Assessment of renal artery stenosis status as an exclusion criterion before any further evaluation
- Confirmation of a route to market (SAHPRA registration) if this indication is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

