---
layout: default
title: Pramocaine
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Pramocaine
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

# Pramocaine: From Topical Anaesthesia to Papillary Conjunctivitis

## One-Sentence Summary

> Pramocaine (pramoxine) is a topical local anaesthetic conventionally used to relieve itching and irritation of the skin and mucosa (e.g. haemorrhoids, insect bites, combined otitis externa preparations).
> The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Topical relief of pruritus/irritation (formal approved-indication text not available — see Data Gap DG001) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the information that is available, pramocaine is a surface-acting local anaesthetic that blocks sodium-channel conduction at sensory nerve endings, an effect exploited clinically for symptomatic relief of itching and irritation rather than for treating an underlying inflammatory process.

Papillary conjunctivitis is primarily an allergic/mechanical inflammatory condition of the conjunctiva. Pramocaine's anaesthetic action could theoretically provide symptomatic relief of ocular itching and discomfort, but it has no known anti-inflammatory or anti-allergic activity and therefore would not address the underlying disease mechanism. No ocular formulation, ocular safety data, or corneal-toxicity data for pramocaine are present in this evidence pack.

It is also worth noting that this candidate was one of ten TxGNN-predicted indications for pramocaine, spanning unrelated conditions (e.g. acne keloidalis, neonatal dermatomyositis, interstitial lung disease). All ten carry similarly high TxGNN scores (97.8–99.2%) but **zero supporting trials or literature**, and all are independently rated L5/Hold. This pattern is more consistent with knowledge-graph proximity (pramocaine sitting near "dermatology/symptom-relief" nodes) than with a specific, mechanistically grounded signal for papillary conjunctivitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## South Africa Market Information

Pramocaine currently has **0 SAHPRA registrations** and is **not marketed** in South Africa. No product, dosage form, or approved-indication data is available for this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/manufacturer labelling warnings and contraindications are flagged as a blocking data gap — DG001 — and must be obtained before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5) with no clinical trial or literature support, a mechanistically weak and non-specific rationale (symptom relief only, not disease-modifying), no ocular safety data, and no current SAHPRA registration or market presence in South Africa.

**To proceed, the following is needed:**
- TFDA/manufacturer Professional Information (warnings, contraindications) — blocking gap (DG001)
- Mechanism of action data from DrugBank or primary literature (DG002)
- Any preclinical or case-level evidence specific to ocular/conjunctival use of pramocaine
- Confirmation of whether an ocular-appropriate formulation exists, given all current uses are topical/otic
- A regulatory pathway assessment, since the drug is not currently registered in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

