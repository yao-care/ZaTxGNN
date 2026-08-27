---
layout: default
title: Dutasteride
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

Using the txgnn-pipeline skill confirmed no additional formatting rules apply beyond the report template already provided — proceeding to generate the report directly from the Evidence Pack.

---

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a dual 5α-reductase inhibitor, internationally used to treat **benign prostatic hyperplasia (BPH)** by lowering dihydrotestosterone (DHT) levels. The TxGNN model's highest-scoring candidate indication is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth disorder, but this prediction is currently supported by **zero clinical trials and zero published literature**, and the model's own rationale flags the underlying mechanism as a poor biological fit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registry (Dutasteride is not currently marketed in South Africa); internationally approved for benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (drugbank field flagged as a data gap). Based on what is embedded in the evidence pack's own repurposing rationale, Dutasteride acts as a dual 5α-reductase inhibitor that lowers DHT — the mechanism underlying its efficacy in androgen-driven conditions such as BPH and androgenetic alopecia.

Ambras type hypertrichosis universalis congenita, however, is a rare congenital disorder caused by a chromosomal rearrangement at 8q24, producing generalised excess hair growth through a developmental pathway that is **not androgen-dependent**. The evidence pack's own mechanistic assessment explicitly notes this mismatch: even though "reducing hair growth" might superficially seem relevant to a hypertrichosis diagnosis, the disease's actual biology does not run through the DHT/5α-reductase axis that Dutasteride targets, so there is no established pharmacological basis for benefit.

A further caution: this candidate's TxGNN score (99.998%) sits at overall model rank 50, and eight of the ten candidates in this evidence pack cluster in a similarly narrow, near-ceiling score band (99.56%–99.998%, ranks 50–2604) with no supporting trials or literature. This pattern is consistent with score saturation/embedding-proximity noise rather than a strong, discriminative therapeutic signal, and should be weighted accordingly when interpreting the ranking.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Dutasteride currently holds **no SAHPRA product registrations** and is recorded as **not marketed** in South Africa in this evidence pack (0 licenses on file). No product-level dosage form or approved-indication data is therefore available from the local registry.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: this evidence pack flags SAHPRA/local warning and contraindication data as a **Blocking** data gap (DG001) — meaning a preliminary safety screen (S1) cannot be completed until this information is obtained.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The candidate indication is supported only by TxGNN's model score (Evidence Level L5) — there are no clinical trials and no literature of any kind.
- The evidence pack's own mechanistic analysis indicates the drug's DHT-lowering action does not plausibly address the non-androgen-dependent, chromosomally driven pathology of Ambras type hypertrichosis.
- A **Blocking** data gap (missing SAHPRA/TFDA warnings and contraindications) prevents even an initial safety assessment (S1) from being started.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, precautions, contraindications) — currently a **Blocking** gap (DG001)
- Confirmed mechanism-of-action data from DrugBank/primary sources — currently a **High**-severity gap (DG002)
- Preclinical or mechanistic evidence directly linking the 5α-reductase/DHT pathway to Ambras type hypertrichosis pathophysiology
- Clarification of whether pharmacological suppression of hair growth is even a clinically desired outcome for this congenital condition, as the current rationale itself is conditional ("if needed")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

