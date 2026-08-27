---
layout: default
title: Mesterolone
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Mesterolone
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

Using the drug-repurposing evaluation report template you supplied, here is the report generated from the Evidence Pack.

---

# Mesterolone: From Androgen Replacement Therapy to Gout

## One-Sentence Summary

Mesterolone is an orally active androgen, publicly known for use in conditions such as male hypogonadism and oligospermia; however, no original-indication or MOA record exists in this evidence pack, and the drug is not currently registered in South Africa. The TxGNN model's top prediction is **Gout**, with a prediction score of **98.20%**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own repurposing rationale flags a mechanistic contradiction — androgens are known to raise serum uric acid, a recognised risk factor for gout, rather than lower it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (no licences on file). Publicly, Mesterolone is known as an androgen used for male hypogonadism/oligospermia — cited as general background, not as a sourced field |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.20% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Mesterolone is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Mesterolone is an androgen/anabolic steroid, and its established uses relate to androgen deficiency states rather than urate metabolism or joint disease.

The repurposing rationale attached to this prediction is explicitly cautionary rather than supportive: androgens are known to raise, not lower, serum uric acid, which is the opposite of the direction needed to treat gout. This suggests the high TxGNN score (98.20%) most likely reflects knowledge-graph co-occurrence or embedding similarity rather than genuine pharmacological plausibility.

Because there are no clinical trials, no registered ICTRP trials, and no literature hits for the Mesterolone–gout pairing, there is currently no independent evidence — clinical or mechanistic — that corroborates the model's prediction. This candidate should be read as a hypothesis-generating signal only, not as an actionable repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Mesterolone is not currently registered with SAHPRA (0 registrations on file), so no market/product information is available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical trial or literature support (0/0), sits at the lowest evidence tier (L5), and the drug's own mechanistic rationale points against biological plausibility (androgens raise, rather than lower, serum uric acid). Combined with a Blocking data gap on safety/labelling and the drug's absence from the South African market, there is no basis to proceed beyond monitoring at this time.

**To proceed, the following is needed:**
- SAHPRA/manufacturer Professional Information (PI) — warnings, precautions and contraindications (currently a Blocking data gap)
- Confirmed mechanism of action data via DrugBank (currently a High-severity data gap)
- Independent mechanistic or preclinical evidence addressing the androgen–urate–gout relationship before any further evaluation stage is considered
- Monitoring of the other nine TxGNN-predicted indications for this drug, all of which are similarly rated L5/Hold and lack corroborating trial or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

