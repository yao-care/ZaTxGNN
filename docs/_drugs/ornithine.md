---
layout: default
title: Ornithine
parent: Model Prediction Only (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ornithine: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report"
---

# Ornithine
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

# Ornithine: From an Unspecified Original Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

Ornithine is an amino acid that is currently registered in South Africa as a component of parenteral nutrition infusions (Numeta G13E and Numeta G16E). The TxGNN model predicts it may be effective for **congenital prothrombin deficiency** (score 97.5%), but **no clinical trials and no publications** support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 97.52% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ornithine in the data compiled for this report. Ornithine is a naturally occurring amino acid involved in the urea cycle and a precursor of polyamines, and it is supplied here as part of parenteral nutrition products.

Congenital prothrombin deficiency is a coagulation factor II disorder. No identifiable mechanistic link was found between ornithine and prothrombin synthesis or function. The high TxGNN score is a model prediction with no supporting trials or literature, so the prediction should be treated as a hypothesis with no demonstrated rationale.

For context, the other predictions generated for this drug have similarly weak support:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Vitamin deficiency disorder | 96.2% | L4 | Literature describes ornithine as a metabolite affected by vitamin B6 and A status, not as a treatment |
| Biotin metabolic disease | 95.7% | L4 | Only indirect links (biomarker or intermediate role); standard care is biotin supplementation |
| Atypical coarctation of aorta | 95.4% | L5 | No evidence; structural defect treated surgically or by intervention |
| Aortic malformation | 94.2% | L4 | Polyamine pathway association only; not evidence of benefit |
| Acne, seborrhoeic conditions, others | 91–92% | L5 | No supporting evidence |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not stated in the data compiled |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion | Not stated in the data compiled |

Both registrations are valid single-ingredient entries, and both are injectable (infusion) forms only. Essential Medicines List status could not be determined from the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from label text): exanthem and dermatitis.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interaction information, as none of these were available in the data compiled. No drug interaction records were found. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no relevant literature, and no plausible mechanistic link between ornithine and prothrombin. Safety information from the PI is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (PI) for warnings, contraindications and approved indications
- Mechanism of action data for ornithine (for example, from DrugBank)
- Any mechanistic or preclinical evidence linking ornithine to prothrombin synthesis or function
- Confirmation of the original approved indications and route compatibility, since only infusion forms are registered
- If the project continues, consider whether other predicted indications with at least some indirect literature (such as the vitamin-dependent metabolic conditions) merit a closer review, while recognising that these too are only L4 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

