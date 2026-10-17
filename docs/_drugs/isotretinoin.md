---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 279
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Isotretinoin: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "ISOTRETINOIN"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Isotretinoin
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

# Isotretinoin: From Hypertensive Disorder to Malignant Renovascular Hypertension

## One-Sentence Summary

According to the knowledge graph used for this prediction, isotretinoin's original indication is hypertensive disorder or hypertension. This does not match its known clinical use as a retinoid for severe acne. The TxGNN model predicts it may be effective for **malignant renovascular hypertension** (and, with an identical score, malignant hypertensive renal disease). **No clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; no approved indication text is recorded in the SAHPRA registration data) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The prediction therefore cannot be supported by a documented mechanistic link.

The original indications listed (hypertensive disorder, hypertension) are not consistent with isotretinoin's known clinical use, which is severe acne. This suggests the knowledge-graph indication edges may be unreliable for this drug, and the prediction should be read with caution.

Retinoids have been explored in preclinical settings for effects on renin expression, vascular remodelling and renal fibrosis. This is speculative and has not been shown for malignant renovascular hypertension. Isotretinoin is also associated with lipid elevations and rare reports of blood pressure or vascular effects, so an antihypertensive benefit is not established. The same score (99.01%) for the second predicted indication, malignant hypertensive renal disease, suggests a shared graph-neighbourhood signal rather than indication-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43/13.4.2/0746 | Oratane 5Mg | Capsule (oral) | Not recorded in the data compiled |
| 29/13.12/0027 | Isotrex | Gel (topical) | Not recorded in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug–disease contraindication edges, not label text):

- **Hepatic, renal and pancreatic:** liver disease, kidney disease, pancreatitis, gallbladder disease, pyoureter
- **Psychiatric:** anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency disease, hyperuricaemia
- **Haematological:** neutropenia, agranulocytosis
- **Immune, inflammatory and bone:** systemic lupus erythematosus (including paediatric), inflammatory bowel disease, osteoporosis (including postmenopausal)
- **Angioedema:** acquired, hereditary (including C1-inhibitor deficiency), non-histaminic and RAAS-blocker-induced forms
- **Haemodynamic:** hypotensive disorder

Several of these (kidney disease, diabetes, hypotension) overlap with the population in which a hypertensive indication would be considered.

**Drug interactions:** 98 interactions are recorded. Major interactions include:

- **Tetracyclines:** doxycycline, minocycline, tetracycline
- **Vitamin A**

Moderate interactions include:

- **Corticosteroids:** betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone
- **Anticoagulants:** warfarin, dicoumarol
- **Others:** ethanol, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor, topical abametapir

Other concerns to weigh, which are not drawn from label data compiled for this report: isotretinoin's known teratogenicity, hepatotoxicity and dyslipidaemia are significant in patients with compromised renal and cardiovascular status.

Warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone, with no clinical trials or literature, no mechanism data, and original indications that conflict with the drug's known use. The safety profile, including teratogenicity, is a poor fit for the target population.

**To proceed, the following is needed:**
- Verification of the original indication data, which appears inconsistent with the drug's known use
- Mechanism of action data and a plausible pharmacological link to renovascular or malignant hypertension
- Preclinical or clinical evidence for the predicted indications
- SAHPRA package insert warnings and contraindications, which block safety screening
- A safety assessment for patients with hypertensive renal disease, covering renal function, lipids, liver function and the interactions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

