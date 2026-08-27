---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension/Heart Failure to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor whose original approved indications are not on record in this evidence pack (the drug is currently **not marketed in South Africa**), but it is internationally established as standard therapy for hypertension, heart failure, and post-myocardial-infarction care. The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on class-level mechanistic reasoning rather than direct evidence for this specific anatomical subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record for South Africa (drug not marketed); internationally recognised ACE-inhibitor indications include hypertension and heart failure |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for lisinopril in this evidence pack. Based on the information available, lisinopril belongs to the ACE inhibitor (ACEi) drug class. Per the model's own rationale notes, ACE inhibitors are already a standard drug class used after acute myocardial infarction — they reduce mortality and inhibit adverse ventricular remodelling — and are also foundational therapy for hypertension.

Posterolateral myocardial infarction is simply an anatomically defined subtype of MI. Since ACEi therapy is already guideline-recommended for essentially all post-MI patients regardless of infarct territory, the mechanistic plausibility of benefit in this subtype is high. However, this TxGNN prediction is a **class-level extrapolation** rather than a subtype-specific finding: no clinical trial or published study in this dataset specifically evaluates lisinopril in posterolateral MI, likely because dedicated trials stratified by infarct location are uncommon — post-MI ACEi use is generally studied and applied without anatomical stratification.

Because the mechanism transfers logically from "MI in general" to "MI, posterolateral subtype," the biological rationale is reasonable, but it has not been independently tested or confirmed for this specific presentation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Lisinopril is not currently marketed in South Africa. No SAHPRA registrations were found in this evidence pack (total registrations: 0).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (posterolateral myocardial infarction) has only mechanism-level (L4) support — no clinical trials or literature address this anatomical MI subtype directly — and the drug is not currently marketed in South Africa, so there is no local regulatory pathway to build on. Notably, a related but different candidate in this evidence pack (chronic pulmonary heart disease, rank 9) has some direct — though small, dated, non-RCT — lisinopril-specific literature and may warrant separate, lower-priority follow-up.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI data (currently a Blocking data gap)
- Confirmed mechanism of action (MOA) documentation from DrugBank or equivalent source
- Direct clinical trial or observational evidence specific to posterolateral (or general post-MI anatomic subtype) use of lisinopril
- Assessment of whether SAHPRA registration/market entry is planned or feasible for this product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

