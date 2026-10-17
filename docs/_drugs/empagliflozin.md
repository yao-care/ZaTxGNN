---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Empagliflozin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin was originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the registration records compiled for this report carry no approved-indication text, so this comes from the TxGNN knowledge graph) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Empagliflozin is known to be an SGLT2 inhibitor that lowers renal glucose reabsorption, and its efficacy in type 2 diabetes mellitus is established.

The data compiled for this report do not support a mechanistic link to focal stiff limb syndrome. This is a rare disorder of the stiff-person spectrum, often associated with GAD65 or glycine receptor autoimmunity that impairs inhibitory neurotransmission. No established biological connection between SGLT2 inhibition and this pathology is evident.

Two further points weaken the prediction:
- The second-ranked prediction, classic stiff person syndrome, has an identical score (99.06%). This suggests the model is propagating a shared disease-node signal rather than drug-specific evidence.
- The third-ranked prediction, opsismodysplasia (score 99.03%), is a rare skeletal dysplasia caused by INPPL1 (SHIP2) mutations. SHIP2 is involved in insulin/PI3K signalling, so there is a thematic overlap with a diabetes drug. Empagliflozin does not act on this pathway, so this is hypothesis-generating only, and use in a paediatric skeletal disorder would raise unassessed safety concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/21.2/1380 | Jardiance | Tablet | Not available in the compiled data |
| Reg. No. 48/21.2/0411 | Jardiance | Tablet | Not available in the compiled data |
| Reg. No. 49/21.2/0915 | Synjardy 5/500 Mg | Tablet | Not available in the compiled data |

All three registrations are currently valid, and all are oral tablets. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 interacting drugs, mostly of Moderate severity, with a few Minor. Examples from the data compiled for this report:
- **Moderate**: phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, fosinopril, furosemide
- **Minor**: topical hydrocortisone, topical alclometasone

Only the first 20 entries were available for review. Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications, and the full interaction profile. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications. The identical scores for related stiff-person conditions suggest a shared-node artefact, and no plausible mechanistic link to SGLT2 inhibition is evident.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for safety screening
- Independent preclinical or mechanistic evidence linking SGLT2 inhibition to stiff-person-spectrum or related pathology
- A literature and trial registry search (including SANCTR and PACTR) to confirm no relevant studies exist
- Safety assessment for the target population, including paediatric considerations if opsismodysplasia is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

