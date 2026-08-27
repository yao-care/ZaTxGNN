---
layout: default
title: Nicotine
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Nicotine
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

# Nicotine: From Smoking Cessation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Nicotine is best known as the active agent in nicotine replacement therapy (NRT) products used to support smoking cessation. The TxGNN model's top-ranked prediction suggests a possible link to **exercise-induced malignant hyperthermia**, but this direction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal with no independent mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation / nicotine replacement therapy (general knowledge; no formal registration record in this evidence pack) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 83.91% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, nicotine is a nicotinic acetylcholine receptor (nAChR) agonist, historically used in NRT products to reduce withdrawal symptoms during smoking cessation, and its efficacy for that original use is well established.

Malignant hyperthermia, by contrast, is a life-threatening pharmacogenetic disorder of skeletal muscle, driven primarily by mutations in the RYR1 ryanodine receptor calcium channel and typically triggered by volatile anaesthetics or succinylcholine. This pathway is mechanistically distinct from the cholinergic (nAChR) pathway through which nicotine acts.

The evidence pack's own rationale for this prediction is explicit that no established mechanistic link exists between nicotine and exercise-induced malignant hyperthermia. This prediction should therefore be treated as an unvalidated model signal rather than a mechanistically grounded hypothesis, consistent with its L5 evidence level and Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Nicotine has no SAHPRA-registered products recorded in this evidence pack (market status: Not marketed; total registrations: 0).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (exercise-induced malignant hyperthermia) has no supporting clinical trials, no supporting literature, and no plausible mechanistic link — it reflects a model-only signal (L5) that the evidence pack itself flags as mechanistically unsupported. Nicotine is also not currently marketed in South Africa (0 SAHPRA registrations), which is an independent barrier to any near-term development pathway.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for nicotine from DrugBank/PI sources
- Preclinical or in vitro evidence connecting nAChR signalling to RYR1-mediated malignant hyperthermia pathophysiology, if such a link is to be pursued at all
- SAHPRA Professional Information (PI) for warnings, contraindications, and drug interactions
- A regulatory pathway assessment given nicotine's current "Not marketed" status in South Africa

**Additional observation:** Among the other candidates in this evidence pack, **blepharospasm** (rank 5) shows materially stronger real-world signal — two published pilot clinical studies of nicotine nasal spray in blepharospasm (evidence level L3, decision stage S1) — despite mixed efficacy results in those small studies. If further evaluation is warranted, this candidate merits separate assessment rather than the top TxGNN-ranked indication reported above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

