---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 314
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely used oral glucose-lowering medicine, originally used for type 2 diabetes.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes (the SAHPRA indication text was not supplied in the data) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Metformin is generally understood to activate AMPK, inhibit mitochondrial complex I and improve insulin sensitivity. Its efficacy in type 2 diabetes is well established.

Focal stiff limb syndrome is a localised variant of the stiff person syndrome spectrum. It is largely autoimmune (often anti-GAD65) and involves impaired GABAergic inhibition. No direct mechanism links metformin to this pathology. The high score most likely reflects shared graph neighbours, such as diabetes or autoimmunity associations, rather than a validated pathway. The model gave an identical score (99.45%) to classic stiff person syndrome, which points to a shared graph-derived signal.

The other predictions are also weak, and none has trial or literature support:
- **Classic stiff person syndrome:** it often co-occurs with type 1 diabetes, which may explain the association with a diabetes drug.
- **Opsismodysplasia:** there is a speculative overlap in PI3K/AKT/mTOR signalling, and metformin's effect on skeletal growth in children would need separate safety assessment.
- **Thiamine-responsive dysfunction syndrome:** the link is probably the diabetic phenotype, and thiamine and insulin remain the standard approaches.
- **Drug-induced localised lipodystrophy:** systemic insulin sensitisation is a different problem from treating local adipose changes.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR and PACTR entries were not supplied).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Metformin has 16 SAHPRA registrations. The five main ones are listed below. Approved indication text and Essential Medicines List (EML) status were not included in the supplied data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/21.2/0071 | Gluconorm | Tablet | Not listed in supplied data |
| Reg. No. 33/21.2/0204 | Mylan Metformin | Tablet | Not listed in supplied data |
| Reg. No. 35/21.2/0093 | Metformin 500 Biotech | Tablet | Not listed in supplied data |
| Reg. No. A39/21.2/0027 | Glucophage XR | Extended-release tablet | Not listed in supplied data |
| Reg. No. 52/21.2/0090 | Metformin XR 500 mg Accord | Tablet | Not listed in supplied data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or publications, and no plausible mechanistic pathway linking metformin to the GABAergic and autoimmune pathology of focal stiff limb syndrome. The likely explanation is a diabetes or autoimmunity association in the knowledge graph.

**To proceed, the following is needed:**
- Mechanism of action data for metformin (for example from DrugBank), to test any link to GABAergic or autoimmune pathways
- Preclinical or clinical evidence for metformin in stiff person syndrome spectrum disorders
- SAHPRA Professional Information (warnings, contraindications and interactions), which is required before any safety screening
- Confirmation of the registered indications and EML status for the South African products
- Trial registry searches (SANCTR, PACTR, ClinicalTrials.gov) for any relevant studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

