---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

> Ofloxacin is a fluoroquinolone-class antibacterial (DNA gyrase/topoisomerase inhibitor) with a long history of use against bacterial infections.
> The TxGNN model's top-ranked prediction for this drug is **Polyclonal Hyperviscosity Syndrome**, with a prediction score of **99.91%**,
> but currently **0 clinical trials** and **0 publications** support this specific direction — this is a model-score-only prediction with no mechanistic or empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack — no SAHPRA license/indication text on file (drug not currently marketed in South Africa) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned for this candidate. Based on the drug's known pharmacology, ofloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV, disrupting bacterial DNA replication.

There is no known or plausible pharmacological pathway connecting this antibacterial mechanism to polyclonal hyperviscosity syndrome, which results from excess circulating plasma proteins (e.g., paraproteinemias, autoimmune conditions) rather than any process ofloxacin's mechanism would affect. This prediction is generated purely from the TxGNN knowledge-graph model's scoring and has no supporting clinical trial or literature evidence in the evidence pack.

Notably, several **lower-ranked** predictions for this drug carry meaningfully stronger evidence: *monoclonal gammopathy* (rank 6, evidence level L3, 20 supporting publications including a Phase 3 RCT on levofloxacin infection-prophylaxis in myeloma) and *septicemic plague* (rank 8, evidence level L3, 20 supporting publications including FDA Animal Rule approvals for class-related fluoroquinolones). These are class-effect / infection-prevention rationales rather than direct treatment of the named disease, but they are substantially better supported than this top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Ofloxacin currently has **0 SAHPRA registrations** on file and is marked as **not marketed** in South Africa. No product/registration records are available to list.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (polyclonal hyperviscosity syndrome) has no mechanistic plausibility, no clinical trials, and no literature support — it is an L5, model-score-only signal that does not meet the threshold for further evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) and original approved indication data for ofloxacin (currently unavailable — DG002/High severity gap)
- SAHPRA-approved Professional Information (PI) covering warnings and contraindications (currently unavailable — DG001/Blocking gap)
- If pursuing repurposing for this drug at all, consider redirecting evaluation toward the higher-evidence candidates identified above (monoclonal gammopathy — infection prophylaxis in myeloma; septicemic plague — class-effect antimicrobial activity against *Yersinia pestis*) rather than the top TxGNN-score-only candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

