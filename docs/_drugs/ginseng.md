---
layout: default
title: Ginseng
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Ginseng
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

# Ginseng: From a Marketed Herbal Ingredient to Drug-Induced Osteoporosis

## One-Sentence Summary

Ginseng is a herbal ingredient found in products registered in South Africa, but no approved indication is recorded in the available licence data.
The TxGNN model predicts it may be useful for **drug-induced osteoporosis**, and only **1 clinical trial** (with no published results in the pack) and **0 publications** currently relate to this prediction.
The prediction has no direct clinical support and remains model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA licence data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 (2 distinct products) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ginseng is a traditional herbal medicine, and it is not clear which approved use the model is extending from. Any mechanistic link to bone health is therefore hypothetical.

The one related trial notes that ginseng extract improved bone density and bone-related biomarkers in animal models of induced osteoporosis. This is the only biological rationale in the pack. It is preclinical, it concerns osteoporosis generally, and it does not address drug-induced (for example glucocorticoid-induced) bone loss.

The very high score (99.95%) should not be read as evidence of efficacy. It reflects a knowledge-graph signal, and no supporting literature was retrieved.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02763280](https://clinicaltrials.gov/study/NCT02763280) | Not applicable | Completed | 90 | 12-week randomised, double-blind, placebo-controlled trial of ginseng extract on bone metabolism in menopausal women (2015–2016). No results are included in the pack. |

This trial studies menopausal bone metabolism, not drug-induced osteoporosis. It is short, and it appears to use biomarker endpoints. At best it is indirect evidence. No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not stated in the register extract |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not stated in the register extract |

Gericomplex appears twice in the data, so there are 2 distinct products. Spiriva Respimat is an inhaled respiratory product, and its link to ginseng looks like a data-matching artefact. Please verify it against the SAHPRA register before relying on it.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no ginseng-specific clinical or literature support for drug-induced osteoporosis. The only trial is short, indirect and has no reported results. Without a mechanism or safety data, it cannot move forward.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which are needed for safety screening
- Mechanism of action data (for example from DrugBank)
- Clarification of the SAHPRA record, including the approved indications and the Spiriva Respimat match
- Results and full endpoints from NCT02763280, and a targeted literature search on ginseng and glucocorticoid-induced bone loss

**Other predicted indications:** Among the other predicted indications, diabetic retinopathy (rank 7) has the largest body of literature. It is mostly network pharmacology and preclinical work, plus multi-herb formula studies, and no ginseng-only human trial. It is best treated as a research question rather than a candidate for recommendation. Most of the remaining predictions (cataract subtypes, hemorrhagic disease of the newborn) have no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

