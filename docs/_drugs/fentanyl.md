---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Fentanyl
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

Using the report template's literal field-extraction rules (predicted_indications[0] = rank 1, "nephrogenic syndrome of inappropriate antidiuresis") since that candidate's own rationale explicitly states it has zero supporting evidence — I'm reporting that honestly rather than substituting a better-evidenced candidate, and adding a supplementary table so the two candidates with real evidence aren't lost.

# Fentanyl: From Severe Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Fentanyl is a potent synthetic opioid used for severe pain management and anesthesia. The TxGNN model's top-ranked prediction for this drug is **Nephrogenic Syndrome of Inappropriate Antidiuresis**, but this ranking is based on the model score alone — **0 clinical trials** and **0 publications** currently support it, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe pain management / anesthesia (opioid analgesic) — SAHPRA-specific approved indication text not available; this evidence pack contains no registered South African license for fentanyl |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for fentanyl in this evidence pack. Based on general pharmacological knowledge, fentanyl is a full μ-opioid receptor agonist used for severe pain and anesthesia; however, the evidence pack itself provides no validated mechanistic pathway connecting opioid receptor agonism to Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD), a rare renal tubular disorder involving the vasopressin V2 receptor.

The repurposing rationale supplied with this candidate is explicit on this point: *"無任何臨床試驗或文獻佐證，亦無已知機轉關聯，純屬 TxGNN 模型預測分數"* — there is no clinical trial or literature support, and no known mechanistic relationship. This candidate reflects a raw knowledge-graph prediction score (rank 3012 in the model's output), not a clinically or mechanistically substantiated hypothesis.

Given the absence of any supporting evidence and the lack of biological plausibility documented in this pack, this candidate does not currently warrant further investment relative to other candidates in the same evidence pack (see supplementary table below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Fentanyl currently has **0 SAHPRA registrations** on file in this evidence pack, and market status is recorded as **Not Marketed**. No product-level registration details (registration number, product name, dosage form, approved indication) are available to tabulate.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: this evidence pack flags TFDA/SAHPRA label warnings and contraindications as a **Blocking** data gap (DG001) — safety data for fentanyl could not be retrieved, which by itself prevents this candidate from entering initial safety screening (S1), independent of the efficacy evidence gap above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level L5 — this candidate is a model score with no supporting clinical trials, no supporting literature, and no identified mechanistic link. Combined with a Blocking safety data gap (PI warnings/contraindications unavailable) and fentanyl's status as an unmarketed, high-risk controlled opioid in this market, there is no basis to advance this indication.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking gap
- Mechanism of action data for fentanyl (DrugBank query pending)
- Any mechanistic or preclinical rationale connecting opioid agonism to NSIAD, or reclassification of this candidate as low-priority given the total absence of evidence

---

## Other Candidate Indications in This Evidence Pack

This evidence pack (TW-DB00813-multi) scored 10 predicted indications for fentanyl. Two candidates have meaningfully stronger evidence than the top-ranked one above and may warrant separate evaluation:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|------------------|-----------------|
| 1 | Nephrogenic syndrome of inappropriate antidiuresis | 99.46% | L5 | S0 | Hold |
| 2 | Tourette syndrome | 99.05% | L5 | S0 | Hold |
| 3 | Trichotillomania | 98.87% | L4 | S0 | Hold |
| **4** | **Myofascial pain syndrome** | 98.09% | **L3** | **S2** | **Proceed with Guardrails** |
| 5 | Manic bipolar affective disorder | 97.73% | L5 | S0 | Hold |
| 6 | Migraine with brainstem aura | 97.71% | L4 | S0 | Hold |
| 7 | Methemoglobinemia | 97.22% | L5 | S0 | Hold |
| 8 | Myositis fibrosa | 97.04% | L5 | S0 | Hold |
| 9 | Idiopathic granulomatous myositis | 97.04% | L5 | S0 | Hold |
| **10** | **Tendinitis** | 97.04% | **L3** | **S2** | **Proceed with Guardrails** |

Myofascial pain syndrome (1 Phase 3 RCT, NCT00343733, n=120) and tendinitis (multiple RCTs on fentanyl patches/PCA in shoulder and tendon surgery) both reflect fentanyl's existing, well-established analgesic use extended to musculoskeletal pain settings — not a novel mechanistic hypothesis. If this repurposing effort is intended to identify actionable candidates, these two are better starting points than the top-ranked NSIAD prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

