---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 377
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Not recorded in the local data"
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pioglitazone: Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitising drug originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pioglitazone is generally known as a PPAR-gamma agonist (a thiazolidinedione) that improves insulin sensitivity. Its efficacy in type 2 diabetes is established.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in *INPPL1* (SHIP2), a phosphoinositide phosphatase that modulates PI3K/insulin signalling. A theoretical link to insulin signalling therefore exists. However, there is no demonstrated effect of pioglitazone on this pathway in skeletal development. The high score (0.9959) reflects model output only and is not backed by trials or literature. At present the link should be regarded as speculative.

Other top-ranked predictions show the same pattern: all are L5 with no trials. They include:
- focal stiff limb syndrome and classic stiff person syndrome (score 0.9950)
- thiamine-responsive dysfunction syndrome (0.9948)
- several localised lipodystrophies (99.18–0.9930)
- pancreatic agenesis (0.9918)

Many of these scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a therapeutic mechanism. The lipodystrophy predictions have a plausible PPAR-gamma adipogenesis rationale, but it is unproven for localised forms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

For context, the seventh-ranked or lower-ranked prediction (pancreatic agenesis) retrieved seven articles, but these concern pioglitazone and other thiazolidinediones in type 2 diabetes and do not address that condition. They are therefore not evidence for any predicted new indication.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A40/21.2/0149 | Cipla-pioglitazone | Tablet | Not stated in the data compiled |
| 46/21.2/0257 | Pioglitazone Hydrochloride Tablets Macleods 15 Mg | Tablet | Not stated in the data compiled |

Both registrations are valid single-ingredient oral products. Essential Medicines List (EML) status could not be determined from the data compiled.

## Safety Considerations

- **Contraindications (associations, not label text):** Pioglitazone is associated with contraindication in congestive heart failure, kidney disease, liver disease and gallbladder disease. It is also linked to pituitary hormone deficiencies and hypogonadotropic hypogonadism (including Kallmann syndrome), adrenocortical insufficiency (Addison disease), thymus gland disease and infectious disease. These associations should be verified against the approved label.
- **Drug Interactions:** 100 interactions were identified (DDInter). Examples at **Moderate** level include phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol, hydrocortisone, acetazolamide, hydrochlorothiazide, ethanol, abiraterone and alpelisib. Examples at **Minor** level include nifedipine, ethinylestradiol and topical corticosteroids.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) have not been retrieved. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or literature for opsismodysplasia, and the mechanistic link is speculative. Safety data from the PI are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Download and review the SAHPRA PI for warnings and contraindications (blocking gap)
- Mechanism of action data (for example from DrugBank)
- Preclinical evidence on whether pioglitazone affects SHIP2/INPPL1-related signalling or skeletal development
- A literature search specific to opsismodysplasia and other candidate indications
- Consideration of lipodystrophy-related predictions as a more biologically plausible area for further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

