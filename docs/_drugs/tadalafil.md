---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From Pulmonary Arterial Hypertension to Kyphoscoliotic Heart Disease

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor internationally approved for erectile dysfunction, benign prostatic hyperplasia, and pulmonary arterial hypertension (PAH, marketed as Adcirca), but it currently holds **no SAHPRA registration** in South Africa.
Of 10 TxGNN-predicted indications reviewed for this candidate, only **Kyphoscoliotic Heart Disease** shows a plausible mechanistic link to tadalafil's known PAH indication — the other nine, including the highest-scoring signal, are flagged as likely model noise with no supporting mechanism.
No clinical trials or published literature currently support tadalafil use specifically in kyphoscoliotic heart disease, placing this candidate at an early, hypothesis-generating stage.

> **Note on candidate selection:** This evidence pack scored 10 candidate indications by raw TxGNN rank. Nine of them — including the top-ranked "Ambras type hypertrichosis universalis congenita" (score 99.98%) — were annotated by the source rationale as mechanistically implausible or contradicted by existing evidence (e.g., PDE5 inhibitors are known to *trigger* migraine-like headache as an adverse effect, not treat migraine). Only Kyphoscoliotic Heart Disease (rank 7, score 99.43%) carries a credible mechanistic rationale, so it is presented here as the lead candidate. The screened-out signals are summarized at the end of this report for transparency.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in South Africa. Internationally approved for erectile dysfunction, BPH, and pulmonary arterial hypertension (PAH) |
| Predicted New Indication | Kyphoscoliotic Heart Disease |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate has not been retrieved from DrugBank (data gap). Based on known information, tadalafil is a phosphodiesterase type 5 (PDE5) inhibitor that promotes vasodilation, particularly in pulmonary vasculature, and has an internationally approved indication for pulmonary arterial hypertension (Adcirca).

Kyphoscoliosis — spinal curvature affecting the thorax — can cause restrictive lung disease that progresses to secondary pulmonary hypertension and cor pulmonale ("kyphoscoliotic heart disease"). Because this downstream pathophysiology overlaps with the pulmonary hemodynamic abnormality that tadalafil is already approved to treat, there is an indirect mechanistic rationale for exploring tadalafil in this population.

However, this rationale is theoretical: it rests on overlap with an already-approved indication (PAH) rather than any tadalafil-specific study in kyphoscoliosis-associated heart disease. No trials or publications targeting this specific population currently exist.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Tadalafil is currently **not registered with SAHPRA** (market status: not marketed; 0 licenses on file). No South African product, dosage form, or approved indication text is available to summarize.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: since tadalafil has no current SAHPRA registration, no local PI exists yet; the international Adcirca/Cialis PI can serve as an interim reference pending local registration.)*

## Other TxGNN Signals Screened Out (Not Pursued)

For transparency, the remaining 9 predicted indications in this evidence pack were reviewed and are **not recommended for further evaluation**:

| Disease | Score | Reason for Hold |
|---------|-------|------------------|
| Ambras type hypertrichosis universalis congenita | 99.98% | Rare chromosomal rearrangement disorder; no known mechanistic link to PDE5 inhibition |
| Hypertrichosis (disease) | 99.98% | Speculative vasodilation-hair-growth analogy only; no evidence |
| Malformation syndrome (odontal/periodontal) | 99.97% | Developmental anomaly; no plausible PDE5 mechanism |
| Syndrome with Dandy-Walker malformation | 99.97% | Congenital posterior fossa malformation; no pharmacological relevance |
| Isolated genetic hair shaft abnormality | 99.96% | Structural genetic defect; no mechanistic link |
| Familial isolated trichomegaly | 99.65% | Associated with prostaglandin analogues, not PDE5 inhibitors |
| Migraine with brainstem aura | 99.08% | PDE5-induced vasodilation is a known *cause* of headache, not a treatment |
| Migraine disorder | 98.91% | Literature identified (PMID 17059442) documents tadalafil-*induced* migraine aura — evidence contradicts, not supports, this indication |
| Hypotrichosis simplex of the scalp | 98.71% | Speculative scalp-perfusion analogy to minoxidil; no supporting data |

These illustrate a known limitation of raw TxGNN ranking: high prediction scores do not guarantee mechanistic or clinical plausibility, and in the migraine case the literature signal actively runs counter to the therapeutic hypothesis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Tadalafil has no SAHPRA registration in South Africa, which blocks even a preliminary safety assessment (per data gap DG001). The lead candidate indication (kyphoscoliotic heart disease) is supported only by indirect mechanistic reasoning (L4) with no clinical trials or direct literature evidence, and the remaining nine TxGNN signals in this evidence pack are not clinically credible.

**To proceed, the following is needed:**
- Detailed mechanism of action data from DrugBank (currently a data gap)
- SAHPRA Professional Information / warnings and contraindications, or a regulatory pathway assessment for South African registration
- Preclinical or proof-of-concept clinical evidence specifically in kyphoscoliosis-associated pulmonary hypertension/cor pulmonale
- Re-screening of TxGNN output using mechanistic plausibility filters before further candidates from this "multi" batch are advanced
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

