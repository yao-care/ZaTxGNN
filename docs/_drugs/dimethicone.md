---
layout: default
title: Dimethicone
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dimethicone: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the registration data"
monitor_inn: "Dimethicone"
predicted_indications: ["insomnia (disease)", "mature cataract", "tetanic cataract", "craniostenosis cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "severe nonproliferative diabetic retinopathy"]
---

# Dimethicone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dimethicone: From an Unspecified Original Indication to Insomnia

## One-Sentence Summary

Dimethicone is a silicone polymer registered in South Africa as a single-ingredient product. The registration data compiled for this report do not state an approved indication. The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials and no publications** currently support this direction. The prediction is a computational output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Dimethicone is generally understood to be a non-absorbed, chemically inert silicone polymer. It is used as an antifoaming agent (simethicone-type) and as a topical emollient or barrier. It has no known central nervous system activity and no recognised sleep-related pharmacology.

Based on this, the prediction does **not** appear to be mechanistically reasonable. The high TxGNN score reflects a knowledge-graph association with no supporting biological rationale. A similarity analysis between the original and predicted indications has not been performed, and route compatibility has not been assessed.

**Other predicted indications** (all L5, all Hold, none with trials or literature):

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Mature cataract | 92.71% | No pharmacological link to reversing lens opacity. Cataract is treated surgically. |
| Tetanic cataract | 92.71% | Secondary to hypocalcaemia or hypoparathyroidism. Dimethicone does not act on calcium metabolism. |
| Craniostenosis cataract | 92.71% | Rare syndromic condition. No relevant target. Likely propagated from other cataract nodes. |
| Immature cataract | 92.71% | No documented antioxidant or anti-aggregation activity. |
| Type 2 diabetes-associated cataract | 92.71% | Dimethicone does not act on polyol, oxidative or glycation pathways. |
| Cortical cataract | 92.68% | Does not address ionic or osmotic disturbance of lens fibres. |
| Nuclear senile cataract | 92.68% | No known antioxidant or anti-aggregation activity. |
| Senile cataract | 92.40% | No approved drug therapy exists. Dimethicone's only ophthalmic relevance is as a physical surgical material. |
| Severe non-proliferative diabetic retinopathy | 92.16% | Not targeted at VEGF, microvascular damage or inflammation. Related silicone oil is a surgical tamponade, not a treatment for severe NPDR. |

The cataract predictions probably reflect graph proximity to eye-related terms rather than a therapeutic mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E1691 (OM) | Propan gel s | Suspension | Not stated in the registration data |

No Essential Medicines List (EML) status was available in the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interactions were found in the data compiled for this report, and no drug-disease contraindications were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no publications and no plausible mechanism. Dimethicone is an inert, non-absorbed silicone with no known CNS activity. The registration data compiled for this report also lack an approved indication and safety information, so the evaluation cannot progress beyond the initial screening stage.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), which is currently a blocking gap
- Mechanism of action data from DrugBank
- A credible biological rationale for sleep-related or ocular effects, supported by preclinical or clinical studies
- Assessment of route compatibility and of similarity to the original indication
- Consideration of whether the other predictions (cataract, diabetic retinopathy) are worth pursuing, given that dimethicone's ophthalmic role is limited to a surgical adjunct
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

