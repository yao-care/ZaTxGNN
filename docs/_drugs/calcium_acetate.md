---
layout: default
title: Calcium Acetate
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 2
---

# Calcium Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Calcium Acetate: From Phosphate Binding to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium acetate is a calcium-containing phosphate binder. The SAHPRA registration data supplied here do not state its approved indication.
The TxGNN model predicts it may be useful for **calcium-alkali syndrome**, but there are **0 relevant clinical trials** and **0 publications** behind this prediction.
The prediction is most likely a knowledge-graph artefact, because calcium acetate is a potential cause of this condition rather than a treatment for it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data provided (generally used as a phosphate binder) |
| Predicted New Indication | Calcium-alkali syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Calcium acetate is a calcium-containing phosphate binder, which lowers serum phosphate by binding dietary phosphate in the gut.

On review, the prediction does not look reasonable. Calcium-alkali syndrome (hypercalcaemia, metabolic alkalosis and acute kidney injury) is caused by excess calcium and alkali intake. A calcium-containing product such as calcium acetate is therefore a potential cause or aggravator of the condition, not a plausible treatment. The very high score (99.90%) probably reflects a drug-disease association in the knowledge graph, such as an adverse or causal link, rather than a therapeutic one. No therapeutic mechanism is supported, and repurposing would carry a safety risk.

The second-ranked prediction, **primary bone dysplasia with defective bone mineralisation** (score 99.88%), has no trials or literature either. Calcium is relevant to mineralisation, but lowering phosphate could be harmful in disorders where phosphate is already deficient, such as hypophosphatasia or hypophosphatemic rickets. This group of rare diseases is heterogeneous, so no single mechanism can be assumed. It needs expert review before any further work.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03591471](https://clinicaltrials.gov/study/NCT03591471) | Phase 1/2 | Unknown | 500 | Multistep traditional Chinese medicine treatment (glycosides of *Tripterygium wilfordii*) for Henoch-Schönlein purpura nephritis in children. **Not relevant:** it does not address calcium-alkali syndrome, and nothing shows calcium acetate was tested in it (relevance grade C). |

No SANCTR or PACTR trials were identified.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/24/0102 | Phosphosorb 660 | Tablet (oral) | Not stated in the data provided |
| Reg. No. 45/24/0919 | Osvaren | Film-coated tablet (Fct) | Not stated in the data provided |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no relevant trials or publications. Calcium acetate is a possible cause of calcium-alkali syndrome, so using it as a treatment would be a safety concern. The second-ranked prediction is also unsupported and may be harmful in some mineralisation disorders.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI), to confirm the approved indication, warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data (e.g. from DrugBank) to allow a mechanistic-link analysis.
- Review of the knowledge-graph edge to confirm whether the association is causal or adverse rather than therapeutic.
- For the second prediction, expert review of the specific bone mineralisation disorders involved, before any further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

