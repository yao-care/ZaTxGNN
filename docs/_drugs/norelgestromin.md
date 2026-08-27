---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 1
---

# Norelgestromin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

> Norelgestromin is the active metabolite of norgestimate, a third-generation progestin used as the hormonal component of transdermal contraceptive patches (e.g. Ortho Evra/Xulane).
> The TxGNN model predicts it may be effective for **amenorrhea (disease)**, but this direction is **not currently supported by any clinical trials or published literature**, and the underlying pharmacology raises a directionality concern (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded for South Africa; based on known pharmacology, norelgestromin is used as the progestin component of a transdermal contraceptive patch (no SAHPRA registration on file) |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for norelgestromin is not currently available in this evidence pack. Based on known pharmacology, norelgestromin is the active metabolite of norgestimate, a third-generation progestin. Clinically it is used as the hormonal component of transdermal contraceptive patches, where it suppresses ovulation and alters cervical mucus and endometrial development to prevent pregnancy.

This predicted association with amenorrhea should be interpreted with caution. Continuous progestin exposure is well known to *induce* amenorrhea — either as a recognized side effect of hormonal contraception, or as an intentional therapeutic effect in conditions such as endometriosis or menstrual suppression regimens. This is the **opposite direction** from "treating" amenorrhea as a disorder. It is possible the TxGNN model has captured a genuine drug–disease association in its knowledge graph (e.g. a "causes/associated with" edge) but the model output here should be reviewed to confirm it does not represent a misread of relationship direction (causes vs. treats).

Because the original indication and mechanism-of-action fields are both unavailable, and no clinical trial or literature evidence currently exists for this specific prediction, confidence in the biological plausibility of this candidate is low.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Norelgestromin is not marketed in South Africa — no SAHPRA registrations are on file (0 licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has only model-prediction-level evidence (L5) with no supporting clinical trials or literature, no SAHPRA market presence, and a mechanistic rationale that plausibly points in the opposite therapeutic direction (progestin exposure is more commonly associated with *causing* amenorrhea than treating it). The evidence base does not currently support advancing this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for norelgestromin
- Clarification of whether the TxGNN knowledge graph edge represents a "causes" vs. "treats" relationship
- At least preliminary clinical or case-level evidence supporting a therapeutic (not causative) role in amenorrhea
- SAHPRA-approved Professional Information (PI), including warnings, contraindications, and drug interaction data, once/if this drug is considered for South African registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

