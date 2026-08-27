---
layout: default
title: Latanoprostene Bunod
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Glaucoma (Drug Class Inference) to Visceral Calciphylaxis

## One-Sentence Summary

> Latanoprostene bunod belongs to the prostaglandin F2α agonist / nitric oxide (NO) donor class used to lower intraocular pressure, though this evidence pack's own original-indication and mechanism-of-action fields are unconfirmed (data gap).
> The TxGNN model's top-ranked prediction for this drug is **Visceral Calciphylaxis**, with a prediction score of **99.76%**,
> but currently **0 clinical trials** and **0 publications** support this specific prediction — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in this dataset — `original_indications` is empty and `original_moa` is unrecorded; drug-class evidence elsewhere in this pack (see below) points to glaucoma / ocular hypertension |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug in the current dataset (`original_moa` is unrecorded, and no `original_indications` are listed). This is flagged in the evidence pack itself as a **Blocking**-severity data gap (DG001, missing SAHPRA/TFDA-equivalent label warnings) and a **High**-severity gap (DG002, missing MOA), meaning safety and mechanistic assessment cannot yet proceed formally.

That said, other entries in this same evidence pack independently identify latanoprostene bunod's known pharmacological class as a prostaglandin F2α receptor agonist combined with an NO donor, acting via the trabecular meshwork and uveoscleral outflow pathways to lower intraocular pressure — i.e., a glaucoma/ocular hypertension therapeutic class. This is useful context but should be treated as unconfirmed until the formal indication/MOA fields are populated.

For the top-ranked prediction, **visceral calciphylaxis**, the evidence pack's own mechanistic rationale states there is **no known link** between this drug's prostaglandin/NO pathway and the calcium-phosphate dysregulation and microvascular thrombosis underlying calciphylaxis. The score (99.76%, TxGNN rank 1675) reflects a purely computational association with no supporting trials or literature. By contrast, a lower-ranked candidate in this same pack — **vascular disease** (rank 6, score 99.53%) — does have a plausible mechanistic rationale (NO-mediated vasodilation) and is backed by two completed clinical trials and one review article, though these measure microvascular blood-flow surrogate endpoints rather than disease treatment outcomes. This candidate may warrant separate follow-up evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: retrieval of the product's official warnings/contraindications is an outstanding **Blocking** data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can be completed for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (visceral calciphylaxis) has no supporting clinical trials or literature (Evidence Level L5, decision stage S0) and no established mechanistic link per this pack's own analysis.
- A Blocking-severity data gap (missing SAHPRA/label safety warnings) currently prevents any safety pre-assessment for this drug, regardless of indication.
- The drug is not currently marketed or registered in South Africa (0 SAHPRA licenses).

**To proceed, the following is needed:**
- Retrieve SAHPRA-approved Professional Information (PI) — warnings, contraindications, drug interactions (resolves DG001, Blocking)
- Confirm mechanism of action and original approved indication via DrugBank or manufacturer labeling (resolves DG002, High)
- If pursuing repurposing evaluation further, prioritize re-scoping toward the **vascular disease** candidate (rank 6), which has actual trial and literature support, rather than the top TxGNN-ranked but evidence-free candidate
- Manually verify whether "primary hereditary glaucoma" (rank 2) reflects a genuine registry gap in the original-indication data, since this drug's known class is glaucoma therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

