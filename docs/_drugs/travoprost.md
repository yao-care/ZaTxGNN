---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2α (FP receptor) agonist used to lower intraocular pressure in open-angle glaucoma and ocular hypertension (based on the drug-class information embedded in the trial evidence within this pack; formal original-indication and MOA records are not yet available). The TxGNN model's top-ranked prediction for this drug is **Visceral Calciphylaxis**, but **no clinical trials and no literature** currently support this link, and the model's own generated rationale states there is no known biological basis for it — this is a pure graph-inference artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / ocular hypertension (inferred from trial evidence in this pack; not confirmed by a formal indication record) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Travoprost is not available in this evidence pack. Based on the information embedded in the supporting trial records, Travoprost belongs to the prostaglandin analogue (FP receptor agonist) class, and its efficacy in lowering intraocular pressure via the uveoscleral outflow pathway is well established for glaucoma and ocular hypertension.

Visceral calciphylaxis is a vascular calcification disorder affecting deep tissue and organ vasculature — a pathology that is mechanistically unrelated to FP-receptor-mediated aqueous humor outflow. The evidence pack's own repurposing rationale is explicit on this point: *"no known mechanism links FP receptor agonism to vascular calcification pathology; the high TxGNN score appears to lack biological grounding and reflects only a graph-relational inference."*

In other words, this is a case where the model's numerical confidence (99.9998%) is not corroborated by any mechanistic plausibility or independent evidence. High TxGNN scores alone should not be interpreted as clinical validity — this candidate illustrates why supporting evidence (trials, literature, MOA) must always be checked before advancing a prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Travoprost currently has no SAHPRA registrations and is not marketed in South Africa (0 licenses on file). No product/registration data is available for review.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Visceral Calciphylaxis) is evidence level L5 — a model-only inference with zero clinical trials, zero literature, and an explicitly stated lack of mechanistic plausibility. Combined with the drug's non-marketed status in South Africa and outstanding MOA/safety data gaps, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action record for Travoprost (DrugBank query is flagged as a blocking data gap)
- SAHPRA-approved PI warnings, contraindications, and drug interaction data
- Independent biological rationale or preclinical data connecting FP receptor agonism to vascular calcification, before further trial/literature search is warranted
- Note for prioritization: within the same prediction batch, rank 5 ("vascular disease") reached decision stage S1 with 15 clinical trials and 20 publications, though the evidence pack flags that evidence as largely glaucoma-specific and mismatched to the "vascular disease" label — this may be a more productive candidate to re-evaluate with corrected search terms before Visceral Calciphylaxis is revisited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

