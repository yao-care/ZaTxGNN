---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a peripherally-acting COMT inhibitor used as adjunct therapy to levodopa/carbidopa in Parkinson's disease. The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**, but this prediction is currently **model-only — no clinical trials or literature support it**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) — inferred from narrative text within this evidence pack; not confirmed by an official label field |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for entacapone is not confirmed within this evidence pack — it is flagged as a High-severity data gap (DG002). Based on information referenced elsewhere in the pack, entacapone is understood to be a peripheral, reversible COMT (catechol-O-methyltransferase) inhibitor, approved as adjunct therapy to levodopa/carbidopa in Parkinson's disease, where it prolongs the central availability of levodopa.

PLA2G6-associated neurodegeneration (PLAN) belongs to the NBIA (Neurodegeneration with Brain Iron Accumulation) disease spectrum, characterized by iron deposition and progressive neurodegeneration. Some patients present with parkinsonian features, giving a theoretical overlap with the dopamine pathway that entacapone acts on.

However, the model's own rationale explicitly notes there is no clinical or literature evidence tying entacapone to PLAN — the theoretical overlap in symptomatology is not the same as mechanistic validation. This should be treated as a low-confidence signal, possibly model noise, rather than a supported hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Entacapone currently has **0 SAHPRA registrations** on file and is **not marketed** in South Africa per this evidence pack. No product/dosage-form data is available.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (PLA2G6-associated neurodegeneration) has a high TxGNN score but zero supporting clinical trials or literature (Evidence Level L5) — it is a pure model output, not a validated repurposing signal.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings/contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety screening can occur.
- Confirmed mechanism-of-action data (DG002) to properly assess mechanistic plausibility.
- Preclinical or mechanistic studies specifically linking COMT inhibition to PLAN pathology.
- Given the complete absence of route/dosage data, route compatibility for this rare pediatric-onset condition would also need to be established.

**Note:** Among the 10 TxGNN candidates in this evidence pack, two other predictions — *Lewy body dementia* (rank 7) and *paralysis agitans, juvenile, of Hunt* (rank 4) — reached Evidence Level L4 / decision stage S1 ("Research Question"), each supported by at least indirect clinical-trial or literature context tied to dopaminergic pathways. These may warrant separate evaluation as more promising candidates than the top-ranked-by-score prediction covered here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

