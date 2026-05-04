---
layout: default
title: D-Biotin
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 0
---

# D-Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# D-BIOTIN: Drug Repurposing Evaluation Report

## One-Sentence Summary

D-Biotin (Vitamin B7/Vitamin H) is a water-soluble B-complex vitamin essential for carboxylase enzyme activity and fatty acid metabolism. The TxGNN model did not generate any predicted new indications for this compound, and no original approved indications were identified in the regulatory dataset. **There is currently insufficient data to support a repurposing evaluation.**

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None identified in regulatory records |
| Predicted New Indication | None — no TxGNN predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (No predictions or supporting studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

> Currently, detailed mechanism of action data is not available. D-Biotin (also known as Vitamin B7 or Vitamin H) is a water-soluble vitamin that serves as a coenzyme for carboxylase enzymes involved in gluconeogenesis, fatty acid synthesis, and amino acid catabolism. It is commonly available as a dietary supplement rather than a registered pharmaceutical product.

The TxGNN model did not generate any repurposing predictions for D-Biotin. This may be due to one or more of the following factors:

1. **Absence from the knowledge graph**: D-Biotin may not have a mapped DrugBank ID within the TxGNN knowledge graph (the DrugBank ID field is null in this evidence pack), meaning the model could not establish drug–disease relationship edges for prediction.
2. **Nutritional supplement classification**: As a vitamin, D-Biotin may not be represented as a therapeutic drug node in the TxGNN disease–drug interaction network.
3. **Limited therapeutic drug–disease signal**: Without approved therapeutic indications in regulatory databases, the model lacks a starting signal from which to infer novel indications.

## Clinical Trial Evidence

Currently no related clinical trials registered (no predicted indication to evaluate).

## Literature Evidence

Currently no related literature available (no predicted indication to evaluate).

## South Africa Market Information

D-Biotin has no SAHPRA registrations on record. It may be available as an over-the-counter dietary supplement or as a component of multivitamin formulations, but no scheduled pharmaceutical products were identified in the regulatory dataset.

## Safety Considerations

> Please refer to the SAHPRA-approved Professional Information (PI) for safety information, if applicable. Report adverse drug reactions to SAHPRA.
>
> **Note for healthcare professionals:** High-dose biotin supplementation (≥5 mg/day) is known to interfere with streptavidin-biotin immunoassays, potentially causing falsely elevated or falsely decreased results in laboratory tests including troponin, TSH, and other hormone assays. Clinicians should enquire about biotin supplementation before interpreting affected laboratory results.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not produce any repurposing predictions for D-Biotin. The compound lacks a DrugBank ID mapping in this dataset, has no registered pharmaceutical products with SAHPRA, and has no approved therapeutic indications on record. Without a predicted indication, there is no candidate to evaluate.

**To proceed, the following is needed:**
- Confirm DrugBank ID mapping (query DrugBank for "Biotin" / DB00121) and re-run the TxGNN prediction pipeline with a valid drug node
- Clarify the regulatory context — determine whether D-Biotin is being evaluated as a high-dose therapeutic agent (e.g., for multiple sclerosis, as studied in MD1003/Qizenday) or as a nutritional supplement
- Obtain mechanism of action data from DrugBank to enable mechanistic relevance analysis
- If a specific repurposing hypothesis exists, manually search ClinicalTrials.gov, PACTR, and PubMed for supporting evidence before re-evaluation

---

*This report was generated on 2026-04-05 based on Evidence Pack v4 (candidate ID: TW-UNKNOWN-multi). Results are for research reference only and do not constitute medical advice. Any drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

