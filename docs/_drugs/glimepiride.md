---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Glimepiride: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea, a class of oral glucose-lowering medicines used for type 2 diabetes. The TxGNN model predicts it may be effective for **classic stiff person syndrome** with a very high score. However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model alone and the likely explanation is a graph-association artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (based on the drug class; the SAHPRA registration data provided do not state an indication) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.75% (model rank 1730) |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data. Glimepiride blocks ATP-sensitive potassium (K-ATP) channels on pancreatic beta cells, which stimulates insulin release. Its established use is in type 2 diabetes.

**No direct mechanistic link was identified.** Stiff person syndrome is a rare autoimmune disorder of the central nervous system, often associated with anti-GAD65 antibodies. The high score most likely reflects the comorbidity of autoimmune diabetes with stiff person syndrome in the knowledge graph. It does not appear to reflect a therapeutic mechanism. Because no original mechanism data were available, an independent mechanistic check was not possible.

The same reasoning applies to the closely related prediction, **focal stiff limb syndrome** (score 99.75%). The other predictions are also not supported by evidence:

| Predicted Indication | Score | Assessment |
|------|------|------|
| Opsismodysplasia | 99.74% | Weak, speculative link only. The disease involves INPPL1 (SHIP2), a regulator of insulin/PI3K signalling, but nothing supports benefit in a skeletal dysplasia. |
| Thiamine-responsive dysfunction syndrome | 99.73% | Indirect at most. Diabetes is a feature of this syndrome, so any use would be symptomatic diabetes management, not treatment of the underlying disease. |
| Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic) | 99.56–99.62% | No mechanistic rationale. A sulfonylurea would not restore lost fat tissue, and the scores likely reflect graph proximity to diabetes. |
| Pancreatic agenesis | 99.55% | Mechanistically contradictory. Glimepiride needs existing beta cells to work, and insulin replacement is the logical therapy. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for classic stiff person syndrome. The only paper retrieved across all predictions concerns endosonographic imaging of suspected insulinomas (PMID [12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/), 2003). It was linked to the pancreatic agenesis prediction and is unrelated to glimepiride or its treatment.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 41/21.2/0656 | Accord glimepiride | Tablet |
| Reg. No. A39/21.2/0023 | Glimepiride 1 oethmaan | Tablet |
| Reg. No. 43/21.2/0005 | Amaryl Combi 2/500 | Tablet |

All three products are oral tablets. Approved indication text and Essential Medicines List (EML) status were not included in the data provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug interaction records were found for this drug in the data provided.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and no plausible mechanism links K-ATP channel blockade to stiff person syndrome. The high score most likely reflects shared graph neighbours (diabetes and autoimmunity). The same applies to the other predicted indications. Safety review also cannot proceed until the SAHPRA package insert data are obtained.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for glimepiride (e.g. via the DrugBank API)
- Any independent clinical or preclinical evidence for stiff person syndrome; none was retrieved
- Approved indication text for the three SAHPRA registrations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

