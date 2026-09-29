---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Ibuprofen
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

# Ibuprofen: From Pain and Inflammation to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID) that blocks COX enzymes to relieve pain, fever and inflammation.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and inflammation (general NSAID use; the supplied SAHPRA records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ibuprofen is a non-selective COX inhibitor, and its efficacy for pain and inflammation is well established.

Acromesomelic dysplasia, Hunter-Thompson type is a genetic skeletal dysplasia caused by loss of function of CDMP1/GDF5. It affects limb growth. There is no established mechanistic link between COX inhibition and this pathway. Ibuprofen gives only symptomatic analgesic and anti-inflammatory effects, so a disease-modifying role is not plausible.

The very high score (0.997, model rank 1783) reflects a graph-based association. No trial or literature supports it, and the score should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Ibuprofen has 19 SAHPRA registrations. Dosage forms include oral tablets, capsules and suspensions. The approved indication text was not available for the registrations below. The first five are listed as the main examples.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| R/3.1/186 | Adco-ibuprofen | Tablet |
| 49/2.7/0178 | Nurofen For Children Strawberry 4% M/V | Suspension |
| 36/5.8/0207 | Sinutab 3-way | Tablet |
| 33/2.8/0430 | Ibucod | Tablet |
| A39/2.8/0229 | Ibumol grape | Suspension |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence (Level L5), and no plausible mechanistic link to a CDMP1/GDF5-driven skeletal dysplasia. The other nine predicted indications (ranks 2–10) are also model-only, with no supporting evidence, and are also on Hold.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and a mechanistic rationale specific to GDF5/BMP signalling
- Preclinical evidence (cell or animal models) showing a disease-relevant effect
- SAHPRA package insert warnings and contraindications for a safety screen, particularly for use in children with skeletal disorders
- A systematic literature and trial registry search, including SANCTR and PACTR, to confirm that no evidence exists

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

