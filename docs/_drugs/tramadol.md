---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Unspecified Indication to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol's original approved indication is not recorded in this evidence pack, and no formal mechanism-of-action (MOA) entry is available. The TxGNN model's top-ranked prediction — **acromesomelic dysplasia, Hunter-Thompson type** — has **0 clinical trials** and **0 publications** supporting it, and the evidence pack's own mechanistic review flags this specific pairing as the *least* biologically plausible of the ten candidates returned, most likely reflecting model noise rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

A formal mechanism-of-action record is not available for tramadol in this evidence pack. However, the pack's own rationale for a lower-ranked candidate (rank 7, juvenile idiopathic arthritis) does describe tramadol's pharmacology: it is a **μ-opioid receptor agonist combined with norepinephrine/serotonin reuptake inhibition**, producing central analgesic effects.

Acromesomelic dysplasia, Hunter-Thompson type is a structural genetic disorder caused by GDF5 gene defects, affecting skeletal development. There is no pathophysiological pathway connecting a centrally-acting analgesic/monoaminergic mechanism to a congenital skeletal malformation — the two are mechanistically unrelated.

Notably, the evidence pack's own analysis is explicit about this: it states that this top-ranked pairing is "the highest TxGNN score but the lowest biological plausibility," and recommends treating it as a **reference case for model-noise calibration** rather than a genuine repurposing candidate. By comparison, several mid-ranked candidates in this batch — such as juvenile idiopathic arthritis (rank 7) — have a more coherent rationale (symptomatic pain control in an inflammatory joint condition), though even those are explicitly noted as non-disease-modifying, unsupported by any trial or literature evidence, and carry known pediatric opioid safety concerns (an FDA black-box warning for tramadol in children under 12 and post-tonsillectomy/adenoidectomy adolescents is referenced in that rationale). None of the ten candidates in this batch have any clinical trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only candidate with zero supporting clinical trials or literature, and the evidence pack's own rationale identifies it as the least biologically plausible pairing in the batch (likely model noise). Separately, a Blocking data gap (missing SAHPRA/TFDA label warnings and contraindications) means the candidate cannot yet enter safety screening (S1) regardless of the indication question.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) for tramadol — currently a Blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source
- If a repurposing signal is still worth pursuing, re-examine mechanistically coherent candidates (e.g., symptomatic pain control in juvenile idiopathic arthritis) rather than the top TxGNN score, and actively search for trial/literature evidence on those
- Clarification of regulatory pathway, since tramadol currently has zero SAHPRA registrations (Not Marketed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

