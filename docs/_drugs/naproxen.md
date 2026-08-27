---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 4
---

# Naproxen
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

# Naproxen: From [Indication Not Recorded] to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen (DrugBank DB00788) is a widely used NSAID; this evidence pack does not record its original approved indication or mechanism of action in structured form.
The TxGNN model's top prediction is **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal disorder, with a raw score of 99.35% — but **zero clinical trials and zero publications** support this direction, and the evidence pack's own mechanistic analysis flags the prediction as a likely statistical artifact rather than a genuine pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (Naproxen is a well-established NSAID for pain, inflammation and fever; no structured indication text was supplied here) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% (rank 3482 in model output) |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on known information, Naproxen is a propionic-acid NSAID that acts as a non-selective COX-1/COX-2 inhibitor, reducing prostaglandin synthesis to relieve pain and inflammation.

Brachydactyly-syndactyly syndrome, by contrast, is a congenital skeletal malformation disorder driven primarily by GDF5/BMP signalling pathway mutations — a developmental/structural condition, not an inflammatory or prostaglandin-mediated one. There is no known causal mechanism connecting COX inhibition to this developmental pathway.

The evidence pack's own repurposing rationale is explicit on this point: it assesses the high TxGNN score as most likely arising from knowledge-graph embedding proximity among rare skeletal-disease nodes (phenotype co-occurrence in the graph), rather than a real pharmacological relationship. This assessment is reinforced by the fact that all four of Naproxen's top predicted indications in this batch (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrome) are rare congenital skeletal/developmental syndromes clustered tightly around a ~0.99 score band, with no differentiating trial or literature support for any of them — a pattern consistent with a batch clustering artifact rather than four independent genuine signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Naproxen is currently **not marketed** in South Africa under this evidence pack (0 SAHPRA registrations recorded). No product/registration data is available to summarize.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this evidence pack flags TFDA/SAHPRA label warnings and contraindications as a Blocking data gap — this must be resolved before any safety assessment can be considered complete.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support, no plausible mechanistic link between COX inhibition and a congenital skeletal-developmental disorder, and the evidence pack's own analysis attributes the high score to a knowledge-graph clustering artifact rather than genuine biology. This pattern repeats across all four of Naproxen's top-ranked predictions in this batch, further weakening confidence in the signal.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (PI) — safety warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action and original approved indication(s) from DrugBank or SAHPRA registration data
- Independent biological/mechanistic rationale connecting NSAID pharmacology to GDF5/BMP-driven skeletal dysplasias, if this candidate is to be pursued further
- Given the artifact pattern identified across the whole batch, consider deprioritizing this candidate in favor of higher-scoring, mechanistically plausible predictions for Naproxen, if any exist outside this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

