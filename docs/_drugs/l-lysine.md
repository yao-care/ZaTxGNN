---
layout: default
title: L-Lysine
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# L-Lysine
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

# L-Lysine: From Unregistered Indication to Gastroparesis (Predicted)

## One-Sentence Summary

> L-Lysine has no registered original indication in the available data and is not currently marketed in South Africa.
> The TxGNN model predicts a possible link to **Gastroparesis**, with a very high prediction score (99.77%),
> but this is supported by **0 clinical trials** and only **1 literature citation**, which itself appears unrelated to L-Lysine's known biology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved/registered indication on file |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for L-Lysine is currently not available. Based on the evidence collected, the TxGNN model assigns a very high prediction score (99.77%, global rank 1,612) linking L-Lysine to gastroparesis. However, the single literature record retrieved for this pairing does not describe any lysine-related mechanism at all — it discusses delivery of mesenchymal stem cells via a gelatin-alginate hydrogel to the stomach as a regenerative therapy for gastroparesis, a topic and mechanism unrelated to L-Lysine itself. This is most likely a keyword co-occurrence artefact rather than genuine supporting evidence.

L-Lysine also has no registered original indication in this evidence pack, and it is not registered with SAHPRA (0 licenses). Without a defined original indication or a documented mechanism of action, no plausible pharmacological bridge between L-Lysine and gastroparesis can currently be established from the available data. The high TxGNN score should therefore be interpreted as a computational signal only, not as evidence of clinical plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical | Bioengineering (Basel, Switzerland) | Describes delivery of mesenchymal stem cells via gelatin-alginate hydrogel to the stomach lumen to regenerate interstitial cells of Cajal/enteric neurons in gastroparesis. Does not investigate L-Lysine and is likely a keyword-match artefact rather than direct evidence for this drug-disease pair. |

## South Africa Market Information

Currently no SAHPRA registrations on file for L-Lysine.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial support and the sole literature citation does not actually relate to L-Lysine's pharmacology — evidence level is L5 (model prediction only). Combined with the absence of MOA data and zero SAHPRA registrations, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Documented mechanism of action for L-Lysine (DrugBank or equivalent) — currently a High-severity data gap
- PI-level safety warnings/contraindications from the relevant regulatory authority — currently a Blocking data gap
- A targeted, verified literature/trial search specifically for "L-Lysine AND gastroparesis" to confirm whether the one retrieved citation is relevant or a false match
- As a secondary note: candidate #6 in this evidence pack ("vitamin deficiency disorder," evidence level L4, 3 clinical trials) has comparatively stronger supporting evidence than the top-ranked gastroparesis prediction and may warrant separate review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

