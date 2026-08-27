---
layout: default
title: Linezolid
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Linezolid
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

# Linezolid: From Gram-Positive Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Linezolid is an oxazolidinone antibiotic originally developed for serious Gram-positive bacterial infections (e.g., MRSA, vancomycin-resistant *Enterococcus*). The TxGNN model predicts a possible new application in **Polyclonal Hyperviscosity Syndrome**, but this signal currently comes from the knowledge-graph model alone — **no clinical trials** and **no published literature** support this specific indication in the evidence pack.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (general pharmacological knowledge; the evidence pack contains no license or indication text for this field) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 92.45% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Linezolid is an oxazolidinone-class antibacterial agent that inhibits bacterial protein synthesis by binding the 23S ribosomal RNA of the 50S subunit; its efficacy against Gram-positive organisms (including MRSA and VRE) is well established clinically.

Polyclonal hyperviscosity syndrome is a hematological/immunological condition driven by elevated circulating immunoglobulins, sometimes seen in the context of chronic infection or immune dysregulation. There is no established pharmacological pathway linking an antibacterial protein-synthesis inhibitor to a reduction in serum viscosity, and the evidence pack's own mechanistic-link and similarity-to-original-indication fields are both marked "pending" — meaning this rationale has not yet been analysed by the pipeline.

Given the absence of a documented mechanistic link, along with zero supporting trials or literature, this prediction should be treated as an exploratory knowledge-graph association rather than a biologically substantiated hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## South Africa Market Information

No SAHPRA-equivalent registration records are available for this drug — the underlying regulatory data shows 0 licenses and a market status of **Not Marketed**.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: the evidence pack flags PI warnings/contraindications as a **Blocking** data gap (DG001) — this prevents the candidate from entering initial safety assessment (S1) until PI data is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (92.45%), this is an L5, model-only prediction with no clinical trials, no literature, and no documented mechanistic rationale connecting an antibacterial agent to a hyperviscosity syndrome. The drug is also not currently marketed locally (0 registrations), and both MOA (DG002, High severity) and PI safety data (DG001, Blocking severity) are missing.

**To proceed, the following is needed:**
- SAHPRA-approved PI (warnings, contraindications) — currently a Blocking gap
- Mechanism of action data via DrugBank query (DG002)
- A documented mechanistic or clinical rationale linking linezolid to polyclonal hyperviscosity syndrome
- At minimum, preclinical or case-level evidence before further evaluation
- Confirmation of local market/registration intent if this candidate is to be pursued in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

