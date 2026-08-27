---
layout: default
title: Sibutramine
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 4
---

# Sibutramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Sibutramine: From Unknown Original Indication to Hypervitaminosis

## One-Sentence Summary

The original indication and mechanism of action for sibutramine (DrugBank DB01105) are not available in the current evidence pack. The TxGNN model predicts a possible link to **Hypervitaminosis**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic-rationale text flags it as a likely false-positive knowledge-graph artifact rather than a real pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no license or indication text on record) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sibutramine is not currently available in this evidence pack, and no original indication is on record, so a mechanistic comparison between the original and predicted indications cannot be constructed.

More importantly, the model's own rationale for this candidate argues against a genuine pharmacological link: hypervitaminosis results from excess intake of fat- or water-soluble vitamins, a metabolic pathway with no known overlap with monoamine reuptake inhibition (the general drug class sibutramine belongs to). The rationale text explicitly attributes the high TxGNN score to indirect node proximity in the knowledge graph — likely both drug and disease sharing connections to obesity/metabolic-comorbidity nodes — rather than a true mechanism-based association. The same pattern holds for the other three ranked candidates (proximal 16p11.2 microdeletion syndrome, obsolete hypertelorism, frontorhiny), all of which are described in their own rationale text as biologically implausible or referencing an obsolete disease term.

Taken together, this candidate set should be treated as a signal of possible embedding noise rather than a genuine repurposing hypothesis, pending independent mechanistic or literature confirmation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Safety data for sibutramine (key warnings, contraindications, drug interactions) is not currently available in this evidence pack. This is flagged as a **blocking data gap** — without the TFDA/SAHPRA-equivalent Professional Information (PI) warnings and contraindications, this candidate cannot proceed to a safety pre-screen (S1). Please refer to the SAHPRA-approved Professional Information (PI) for safety information once available, and report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence for any of the four predicted indications, no mechanism-of-action data, and no original-indication data to anchor a biological rationale. The model's own mechanistic notes suggest this top prediction (and the other ranked candidates) likely reflect knowledge-graph node proximity rather than real pharmacology, and a blocking data gap prevents even an initial safety screen.

**To proceed, the following is needed:**
- Sibutramine mechanism of action (MOA) data (DrugBank query, per DG002)
- TFDA/SAHPRA-equivalent product warnings and contraindications (per DG001, blocking)
- Independent literature or preclinical evidence specifically linking sibutramine to hypervitaminosis before further evaluation is warranted
- Reassessment of whether this candidate should remain in the pipeline, given the mechanistic implausibility noted in the model's own rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

