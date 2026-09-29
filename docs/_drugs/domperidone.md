---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 193
evidence_level: L5
indication_count: 1
---

# Domperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Domperidone: From Prokinetic/Antiemetic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist, generally used as a prokinetic and antiemetic.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. It is a model-derived association only, with no credible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record; generally used as a prokinetic and antiemetic |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% (model rank 4550) |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Domperidone is known as a peripheral dopamine D2/D3 receptor antagonist. Its established effects are on gastrointestinal motility and nausea/vomiting.

NSIAD is caused by gain-of-function mutations in *AVPR2* (the vasopressin V2 receptor). These produce constitutive antidiuresis while circulating vasopressin (AVP) is suppressed. Domperidone has no known action on the V2 receptor or the aquaporin-2 pathway, so the two conditions share no obvious pharmacological link.

The high TxGNN score is a knowledge-graph association only. No trial or publication supports it, and the record lacks both original-indication data and MOA data, so the prediction cannot be cross-checked against curated pharmacology. On current information, the prediction is **not** mechanistically well supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/5.7.2/0563 | Domperidone Cipla | Orally disintegrating tablet (ODT) | Not stated in the record |

## Safety Considerations

- **Cardiac risk (from the evidence pack's assessment)**: Domperidone carries a risk of QT prolongation and arrhythmia. Electrolyte disturbance such as hyponatremia, which can occur in NSIAD, could compound this risk.
- **Drug Interactions**: The interaction query returned no records. This does not mean there are no interactions.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and interaction details. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link to V2 receptor-driven antidiuresis. The known QT and arrhythmia risk, together with possible electrolyte disturbance in NSIAD, adds a safety concern with no offsetting efficacy signal.

**To proceed, the following is needed:**
- A credible mechanistic rationale linking dopamine D2/D3 antagonism to the AVPR2/aquaporin-2 pathway, supported by preclinical data
- Mechanism of action data for domperidone (e.g. from DrugBank)
- Original indication text and safety sections (warnings, contraindications) from the SAHPRA-approved PI
- Any published case reports or preclinical studies in NSIAD, none of which are currently identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

