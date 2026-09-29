---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

# Ergocalciferol: From Vitamin D Deficiency to Familial Isolated Hypoparathyroidism (Impaired PTH Secretion)

## One-Sentence Summary

Ergocalciferol (vitamin D2) is a vitamin D supplement. The SAHPRA registration data supplied here does not state an approved indication.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**.
This is a **model prediction only, with 0 clinical trials and 0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.85% (model rank 1138) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 (2 distinct registration numbers; see the market section) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ergocalciferol is a vitamin D analogue (vitamin D2). Vitamin D analogues are used in hypoparathyroidism generally, so a model trained on drug-disease relationships could plausibly link the two.

The mechanistic fit is weak, however. Ergocalciferol is a prohormone. It must be hydroxylated in the liver and then in the kidney (1-alpha-hydroxylation) to become active, and the kidney step depends on parathyroid hormone (PTH). When PTH secretion is impaired, activation is likely to be poor. Already-activated analogues such as calcitriol or alfacalcidol are a better fit. No trials or publications were retrieved for this familial form, so the high score is not backed by disease-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were retrieved either.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not listed in the data supplied |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not listed in the data supplied |

- Gericomplex appears twice under the same registration number, so there are only 2 distinct registrations.
- Spiriva Respimat is a tiotropium inhaler. Its link to ergocalciferol looks like a data-mapping error and should be verified against the SAHPRA register.
- Essential Medicines List (EML) status is not available in the data supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or literature. Ergocalciferol also depends on PTH-driven activation, which makes it a poor mechanistic fit for a disease of impaired PTH secretion.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Verification of the registrations, in particular the Spiriva Respimat link
- Disease-specific evidence, or a direct comparison against calcitriol or alfacalcidol
- A hypercalcaemia and renal monitoring plan if any use were considered

For context, other predicted indications in this Evidence Pack have more supporting literature (renal osteodystrophy and hypophosphatemic rickets, both L3). They may be better candidates for further review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

