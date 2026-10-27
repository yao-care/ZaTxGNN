---
layout: default
title: Calcium Ascorbate
parent: Model Prediction Only (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Calcium Ascorbate: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the SAHPRA registration data"
monitor_inn: "Calcium ascorbate"
predicted_indications: ["insomnia (disease)", "diabetic cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "mature cataract", "immature cataract", "tetanic cataract", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy"]
---

# Calcium Ascorbate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Calcium Ascorbate: From an Unspecified Original Indication to Insomnia
{: .text-alpha }

## One-Sentence Summary

Calcium ascorbate is a buffered form of vitamin C (ascorbic acid). The SAHPRA registration data compiled for this report do not state an approved indication for it.
The TxGNN model predicts it may be useful for **insomnia** (score 95.1%), but there are currently **0 clinical trials** and **0 publications** supporting this prediction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 95.15% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

**Other predictions in the top 10:** The remaining nine predictions have similar scores (93.9% to 94.3%). Eight concern ophthalmic conditions (cataract subtypes) and one concerns diabetic retinopathy. None has clinical trial or literature support.

| Rank | Predicted Indication | Score | Evidence Level | Suggested Handling |
|------|------|------|------|------|
| 2 | Diabetic cataract | 94.26% | L5 | Research question |
| 3 | Type 2 diabetes-associated cataract | 94.21% | L5 | Research question (overlaps with rank 2) |
| 4 | Craniostenosis cataract | 94.21% | L5 | Hold |
| 5 | Mature cataract | 94.21% | L5 | Hold |
| 6 | Immature cataract | 94.21% | L5 | Research question |
| 7 | Tetanic cataract | 94.21% | L5 | Hold |
| 8 | Cortical cataract | 94.08% | L5 | Research question |
| 9 | Nuclear senile cataract | 94.08% | L5 | Research question |
| 10 | Diabetic retinopathy | 93.87% | L5 | Research question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ascorbate is an antioxidant, but nothing in the data compiled for this report links it to sleep regulation. Ascorbate is not an established treatment for insomnia, so the high TxGNN score (95.1%) is a knowledge-graph prediction without a verified mechanistic basis. It should not be read as evidence of efficacy.

The eye-related predictions (ranks 2 to 10) have a more plausible, though still unverified, rationale. Ascorbate is concentrated in the aqueous humour and lens. Oxidative stress, polyol pathway activity and glycation damage contribute to diabetic cataract, age-related cataract and diabetic microvascular disease. This gives a biological basis for hypothesis generation only.

Several cataract predictions are likely artefacts of ontology propagation from the general cataract node:
- **Craniostenosis cataract:** a syndromic cataract of genetic or developmental origin, unlikely to respond to an antioxidant.
- **Mature cataract:** established lens opacity is not expected to be reversed by antioxidants, and management is surgical.
- **Tetanic cataract:** associated with hypocalcaemia. The calcium in calcium ascorbate is minimal and is not a therapeutic route for correcting it.
- **Type 2 diabetes-associated cataract:** overlaps with diabetic cataract and adds no independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| P/7.1.4/281 | Nitrolingual | Inhaler | Not stated in the data compiled |
| C769 (ACT 101/1965) | Ilvico | Syrup | Not stated in the data compiled |
| C770 (ACT 101/1965) | Ilvico | Tablet | Not stated in the data compiled |

All three registrations are valid single-ingredient entries. No Essential Medicines List (EML) status was available in the data compiled. The Nitrolingual entry should be verified against the SAHPRA register, because that product name is not usually associated with calcium ascorbate.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on a model score alone, with no trials, no literature, no mechanistic link and no safety data. The ophthalmic predictions have a plausible antioxidant rationale but are also unsupported by evidence, so they are better treated as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert for warnings, contraindications and approved indications (this is a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic literature search on vitamin C for insomnia, cataract and diabetic retinopathy, including existing observational and interventional studies
- A trial registry search (ClinicalTrials.gov, SANCTR, PACTR) for the same conditions
- Confirmation of the product-to-ingredient mapping for the three SAHPRA registrations
- Route and formulation compatibility assessment for any shortlisted indication (for example, whether an oral or ophthalmic route is needed)
- If any ophthalmic indication is pursued, prioritise diabetic cataract and early-stage (immature, cortical, nuclear) cataract, and de-prioritise craniostenosis, mature and tetanic cataract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

