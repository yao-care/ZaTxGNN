---
layout: default
title: Calcium Acetate
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 2
monitor_inn: "CALCIUM ACETATE"
predicted_indications: ["calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization"]
last_modified_at: 2026-10-29
description: "Calcium Acetate: predicted new indication calcium-alkali syndrome (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Calcium Acetate: Calcium salt phosphate binder → calcium-alkali syndrome
{: .text-alpha }

## One-Sentence Summary

Calcium acetate is a calcium salt used to manage calcium and phosphate balance. The TxGNN model predicts it for **calcium-alkali syndrome**, with a score of 0.9990. No clinical trials or publications were found to support this prediction, and the condition is recognised as being caused by excess calcium intake, so this is more likely a safety signal than a treatment opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | calcium-alkali syndrome |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Calcium acetate is a calcium salt that binds dietary phosphate in the gut and supplies calcium.

Calcium-alkali syndrome is characterised by hypercalcaemia, metabolic alkalosis and acute kidney injury. It is classically caused by excess calcium intake together with absorbable alkali. The high model score most likely reflects this causal or adverse-effect relationship rather than a therapeutic one. Because the drug can contribute to the condition, using it as a treatment would be inappropriate. This prediction is therefore not a valid repurposing candidate on the current information.

A second prediction in the data, primary bone dysplasia with defective bone mineralization, has no supporting studies either and is not assessed further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/24/0102 | Phosphosorb 660 | Tablet | Not recorded in the local data |
| Reg. No. 45/24/0919 | Osvaren | Fct | Not recorded in the local data |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status is not available in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions:** 83 interactions were recorded. Major interactions include:
  - Dolutegravir
  - Bictegravir

  Moderate interactions include:
  - Tetracyclines (doxycycline, tetracycline)
  - Quinolones (gemifloxacin)
  - Bisphosphonates (alendronic acid, risedronic acid, ibandronate)
  - Calcium channel blockers (nifedipine, amlodipine)
  - Beta-blockers (acebutolol, atenolol, betaxolol, bisoprolol)
  - Thiazide diuretics (hydrochlorothiazide, bendroflumethiazide, benzthiazide)
  - Topical vitamin D analogues (calcipotriol, calcitriol)
  - Baloxavir marboxil
- **Conditions of concern in the compiled data:** Compiled drug-disease data flag caution in kidney disease (including chronic and end-stage renal failure), nephrolithiasis, hypercalcaemia (including humoral hypercalcaemia of malignancy), hyperparathyroidism, sarcoidosis, heart and cardiovascular disease, digitalis poisoning and ventricular fibrillation. These are not taken from label text.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has a high model score but no supporting trials or publications (evidence level L5). Calcium-alkali syndrome is a recognised consequence of excess calcium, so treatment use would be contraindicated.

**To proceed, the following is needed:**
- Confirmation that the model association reflects an adverse-effect relationship rather than a therapeutic one
- Retrieval of the SAHPRA Professional Information for warnings and contraindications
- Mechanism of action data
- A systematic literature review before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

