---
layout: default
title: Calcium Acetate
parent: Model Prediction Only (L5)
nav_order: 90
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

# Calcium Acetate: From Hypercalcaemia and Phosphorus Metabolism Disorders to Calcium-Alkali Syndrome

## One-Sentence Summary

Calcium acetate is a calcium salt, originally used for conditions of calcium and phosphorus imbalance (hypercalcaemia disease, nephrocalcinosis, phosphorus metabolism disease) and cardiac arrest.
The TxGNN model predicts it may be effective for **calcium-alkali syndrome**, but **no clinical trials and no publications** support this prediction.
The predicted link most likely reflects a causal relationship (the drug can cause the condition) rather than a therapeutic one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcaemia disease, nephrocalcinosis, phosphorus metabolism disease, cardiac arrest (from the TxGNN knowledge graph; no approved indication text is available for the SAHPRA registrations) |
| Predicted New Indication | Calcium-alkali syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, calcium acetate is a calcium salt, and its calcium content is what makes it relevant to disorders of calcium and phosphorus balance.

On closer examination, the prediction appears **not to be a valid therapeutic opportunity**. Calcium-alkali syndrome (hypercalcaemia, metabolic alkalosis and acute kidney injury) is a recognised result of excess calcium intake combined with absorbable alkali. The model's association most likely captures this causal or adverse-effect relationship, not a treatment effect. Using a calcium salt to treat a condition it can cause would be inappropriate and potentially harmful.

The second-ranked prediction, **primary bone dysplasia with defective bone mineralization** (score 99.88%), is also speculative. Calcium provides a mineral substrate for bone, but defective mineralization in these disorders usually has genetic or phosphate-metabolism causes. In some of them, calcium or phosphate supplementation may be ineffective or may worsen hypercalcaemia or ectopic calcification. It also has no supporting trials or literature, and no mechanism data are available to assess it.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/24/0102 | Phosphosorb 660 | Tablet (oral) | Not available in the data compiled for this report |
| Reg. No. 45/24/0919 | Osvaren | Film-coated tablet | Not available in the data compiled for this report |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

---

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links calcium acetate to contraindication with the following conditions:
- **Renal:** kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, acute urate nephropathy, nephrolithiasis, nephrolithiasis susceptibility caused by SLC26A1, pyoureter
- **Calcium and parathyroid:** hypercalcaemia disease, humoral hypercalcaemia of malignancy, hyperparathyroidism, osteitis fibrosa, nephrocalcinosis, sarcoidosis
- **Cardiac:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
- **Other:** phosphorus metabolism disease, diarrhoeal disease

Some of these overlap with the drug's original indication list (for example hypercalcaemia and phosphorus metabolism disease), so these edges should be interpreted with caution and verified against the approved Professional Information.

**Drug Interactions:** 83 interactions were identified. The main ones are:
- **Major:** dolutegravir, bictegravir (reduced absorption of integrase inhibitors is a concern, relevant in South Africa given widespread HIV treatment)
- **Moderate:**
  - Tetracyclines and quinolones: doxycycline, tetracycline, gemifloxacin
  - Bisphosphonates: alendronic acid, risedronic acid, ibandronate
  - Calcium channel blockers: nifedipine, amlodipine
  - Beta-blockers: acebutolol, atenolol, betaxolol, bisoprolol
  - Thiazide diuretics: hydrochlorothiazide, bendroflumethiazide, benzthiazide
  - Vitamin D analogues: calcipotriol (topical), calcitriol (topical)
  - Antiviral: baloxavir marboxil

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and precautions. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials or publications behind it. The calcium-alkali syndrome prediction most likely reflects a drug-caused condition, so it should not be pursued as a treatment. The bone mineralization prediction is speculative and carries potential harm.

**To proceed, the following is needed:**
- Mechanism of action data (currently unavailable)
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the two registered products
- A formal literature review and a disease-subtype-specific assessment for primary bone dysplasia with defective mineralization
- Confirmation that the calcium-alkali syndrome association is causal and not therapeutic, after which it should be removed from the candidate list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

