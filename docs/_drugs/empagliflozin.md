---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 210
evidence_level: L5
indication_count: 3
monitor_inn: "EMPAGLIFLOZIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
last_modified_at: 2026-10-29
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
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

## Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor, recorded in the knowledge graph for type 2 diabetes mellitus. The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but **no clinical trials and no publications** were found in the data compiled for this report. The prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 3 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

Two other predictions have identical evidence status (no trials, no literature, L5, Hold):
- **Focal stiff limb syndrome**: score 0.9906
- **Opsismodysplasia**: score 0.9903

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Empagliflozin is generally known as an SGLT2 inhibitor that lowers blood glucose by increasing urinary glucose excretion. This is background knowledge, not something verified in the data compiled here.

Stiff person syndrome is an autoimmune neurological disorder, typically linked to anti-GAD65 antibodies and impaired GABAergic signalling. SGLT2 inhibition does not target these pathways. The only conceivable link is indirect, through the overlap of diabetes and autoimmunity, and this is speculative. No mechanistic link is supported by the data.

The score for focal stiff limb syndrome is identical to that of classic stiff person syndrome. This suggests both scores come from the shared disease-ontology neighbourhood rather than from independent evidence.

For opsismodysplasia, a rare skeletal dysplasia caused by INPPL1 (SHIP2) mutations, there is a speculative connection to insulin/PI3K signalling. Empagliflozin has no established action on SHIP2 or skeletal development. SGLT2 inhibitors also raise a theoretical concern for bone and mineral metabolism in growing children.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/21.2/1380 | Jardiance | Tablet | Not stated in the available records |
| Reg. No. 48/21.2/0411 | Jardiance | Tablet | Not stated in the available records |
| Reg. No. 49/21.2/0915 | Synjardy 5/500 Mg | Tablet | Not stated in the available records |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report. All three registrations are valid and oral tablets. The Synjardy registration is listed in the records as a single-ingredient entry, but the product name suggests a fixed-dose combination. It should therefore not be used to describe empagliflozin alone.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records, and 20 are shown in the data compiled. Most are rated Moderate, and a few are Minor. Examples of Moderate interactions:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Cardiovascular and diuretic agents: acebutolol, nifedipine, fosinopril, furosemide, acetazolamide
  - Hormones and corticosteroids: ethinylestradiol, hydrocortisone
  - Others: ethanol, fosamprenavir, fosphenytoin, fostamatinib, fostemsavir, gemifloxacin
- **Minor interactions**: topical hydrocortisone and topical alclometasone.

Warning and contraindication text from the SAHPRA-approved Professional Information (PI) was not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no clinical trials, no publications and no plausible mechanistic link. The same holds for the two other predicted diseases.

**To proceed, the following is needed:**
- Retrieve the SAHPRA Professional Information (indications, warnings, contraindications), which is currently a blocking gap for safety screening
- Obtain mechanism of action data
- Run a systematic literature and trial registry search (including SANCTR and PACTR) for empagliflozin in stiff person spectrum disorders
- Test the mechanistic hypothesis preclinically before any clinical consideration
- For opsismodysplasia, assess paediatric bone and mineral safety separately
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

