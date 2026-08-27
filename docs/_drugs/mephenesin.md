---
layout: default
title: Mephenesin
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Mephenesin
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

# Mephenesin: From Muscle Spasm to Metastatic Melanoma

## One-Sentence Summary

> Mephenesin is a centrally-acting skeletal muscle relaxant; its original approved indication is not recorded in this evidence pack (no SAHPRA licenses exist, as the drug is not marketed in South Africa).
> The TxGNN model predicts it may be effective for **Metastatic Melanoma**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no independent verification.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no SAHPRA license data). Mephenesin is generically known as a centrally-acting skeletal muscle relaxant used for muscle spasm/spasticity. |
| Predicted New Indication | Metastatic Melanoma |
| TxGNN Prediction Score | 96.26% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Mephenesin is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacological information, Mephenesin is a centrally-acting muscle relaxant whose established action is inhibition of polysynaptic spinal reflexes — a mechanism used to relieve muscle spasm and spasticity. There is no known biological pathway connecting this action to melanoma pathogenesis (e.g., BRAF/MEK signalling, melanocyte proliferation control), and the absence of confirmed MOA data means neither support for, nor exclusion of, a mechanistic link can be established.

It is also notable that this candidate is not an isolated signal: ranks 2, 3, and 10 in the same prediction set (non-cutaneous melanoma, epithelioid cell melanoma, eyelid melanoma) are all melanoma-family diseases with very similar scores, and ranks 5–9 (multiple cataract subtypes) share an *identical* score of 95.47%. This pattern is consistent with TxGNN producing correlated outputs across clustered disease nodes in the knowledge graph, rather than independent, disease-specific biological evidence for each entry. Combined with the complete absence of clinical trials, registry entries, or publications for Mephenesin in melanoma, this prediction should be treated as a hypothesis-generating statistical association only, not as evidence of therapeutic plausibility.

Given the lack of original indication data, original MOA data, and any corroborating trial or literature evidence, there is currently no basis to argue the mechanism "may be applicable" to metastatic melanoma beyond the model's statistical output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registrations were found for Mephenesin. The evidence pack confirms a market status of "Not Marketed" with 0 total licenses, so no product/dosage-form information is currently available for the South African market.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: Key warnings, contraindications, and drug-interaction data were queried but are not currently available. Retrieval of the TFDA/SAHPRA product label is flagged as a Blocking data gap — it is required before this candidate can proceed to any safety-stage evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has Evidence Level L5 (model prediction only) — zero clinical trials, zero registry entries, and zero publications support a Mephenesin–melanoma link, the drug's mechanism of action is undocumented, and it is not currently marketed in South Africa. There is no basis to advance beyond initial screening at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Mephenesin (currently a High-severity data gap)
- SAHPRA/TFDA-approved Professional Information, including warnings and contraindications (currently a Blocking data gap)
- Original approved indication and regulatory history for Mephenesin
- Preclinical or mechanistic studies exploring any plausible link between centrally-acting muscle relaxants and melanoma biology
- Ongoing monitoring for new clinical trial registrations or literature, given the current complete absence of supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

