---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 470
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-29
monitor_inn: "VERAPAMIL"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Verapamil: Obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker, originally used for hypertension, atrial fibrillation, angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**,
but **no clinical trials and no publications** currently support this prediction, and the mechanism argues against benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 4 of 4) |
| Number of SAHPRA Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, verapamil is an L-type calcium channel blocker that slows atrioventricular (AV) nodal conduction. Its efficacy in hypertension and supraventricular and ventricular arrhythmias is established.

The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence: bundle branch block is a conduction disorder, and verapamil is already linked to conduction-related conditions such as atrial fibrillation and ventricular tachycardia. This is a statistical association, not a mechanistic one.

Mechanistically, the prediction is hard to support. Verapamil slows conduction rather than improving it, so benefit in bundle branch block is implausible and it may be harmful. The disease term is also flagged as obsolete, which further weakens the prediction. Knowledge graph contraindication edges list atrioventricular block and heart failure among the conditions where verapamil should be avoided.

**Other predicted indications (all Hold):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant hypertensive renal disease | 0.9927 | L5 | No trials or literature; standard care uses other agents |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9926 | L5 | Only indirect preclinical evidence; calcium channel blockers may worsen gas exchange |
| Pulmonary hypertension with unclear multifactorial mechanism | 0.9926 | L5 | No evidence; empirical use not supported |
| Braddock syndrome | 0.9915 | L5 | No mechanistic link; likely a network artifact |
| Periodic paralysis with transient compartment-like syndrome | 0.9908 | L5 | Loose ion-channel connection only; safety uncertain |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

## South Africa Market Information

Verapamil is marketed in South Africa with 4 valid single-ingredient registrations. The approved indication text was not available in the data compiled for this report. Essential Medicines List (EML) status was not available either.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/7.1.4/161 | Verapamil 40 Oethmaan | Tablet | Not available |
| 31/7.1/0637 | Verahexal 240 SR | Sustained-release tablet | Not available |
| 31/7.1.3/0631 | Tarka | Sustained-release capsule | Not available |
| A39/7.1.3/0508 | Tarka 180mg/2mg | Sustained-release tablet | Not available |

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** Associations include atrioventricular block, heart failure, hypotensive disorder, hypertrophic cardiomyopathy, aortic stenosis, ventricular tachycardia, kidney disease, liver disease, myasthenia gravis, neuromuscular junction disease, neutropenia, agranulocytosis and angioedema (several forms). These are graph associations and must be confirmed against the approved Professional Information.
- **Drug Interactions:** 100 interactions were identified; the most relevant listed:
  - **Major:** Loperamide
  - **Moderate:** Clarithromycin, Cimetidine, Aprepitant, Bupropion, Metformin, Canagliflozin, Acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide) and calcium salts (carbonate, chloride, citrate, acetate, phosphate)
  - **Minor:** Morphine

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9962 TxGNN score is not backed by any clinical trial or publication. Verapamil slows cardiac conduction, so benefit in bundle branch block is mechanistically implausible and potentially harmful. The target disease term is also obsolete. None of the other six predictions has clinical evidence either.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA Professional Information (warnings, contraindications and approved indications), currently a blocking gap
- Detailed mechanism of action data from DrugBank
- Re-mapping the obsolete disease term to a current diagnosis, or selecting a better-supported candidate (the pulmonary hypertension prediction has some preclinical rationale, but calcium channel blockers are not recommended in that setting)
- A clinical safety review of conduction effects before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

