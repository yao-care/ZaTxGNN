---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Metformin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely used oral antidiabetic drug, originally indicated for **type 2 diabetes mellitus**.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome** (score 99.4%),
but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Metformin is a biguanide whose efficacy in type 2 diabetes is well established. It is generally understood to act by reducing hepatic glucose production and improving insulin sensitivity, but this comes from general knowledge, not from the data compiled here.

Focal stiff limb syndrome is a rare condition within the stiff-person spectrum, thought to involve impaired GABAergic inhibition and, in many cases, autoimmune or neurological mechanisms. No plausible pathway from metformin's metabolic effects to this pathology can be established from the available evidence.

The related prediction, classic stiff person syndrome, received an identical score (99.45%). It may reflect a knowledge-graph association through diabetes, as stiff person syndrome often co-occurs with type 1 diabetes (shared GAD autoimmunity). This is a hypothesis about why the model made the prediction, not evidence of efficacy.

**Other predicted indications (all L5, Hold, no trials or literature):**

| Rank | Predicted Indication | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 99.45% | Possible link via shared diabetes/GAD autoimmunity; no therapeutic rationale |
| 3 | Opsismodysplasia | 99.40% | Speculative link via insulin/PI3K signalling (INPPL1/SHIP2); benefit unlikely for a congenital structural disease |
| 4 | Thiamine-responsive dysfunction syndrome | 99.40% | Defect is thiamine transport; standard treatment is thiamine supplementation |
| 5 | Drug-induced localized lipodystrophy | 99.06% | Plausible insulin-sensitising rationale, but localized injection-related lipodystrophy is a different process |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Metformin is marketed in South Africa with 16 valid SAHPRA registrations (all single-entity records, none cancelled). The approved indication text was not available for these registrations. Essential Medicines List (EML) status was not available in the data compiled for this report. Five main registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/21.2/0071 | Gluconorm | Tablet | Not available |
| Reg. No. 33/21.2/0204 | Mylan metformin | Tablet | Not available |
| Reg. No. 35/21.2/0093 | Metformin 500 Biotech | Tablet | Not available |
| Reg. No. A39/21.2/0027 | Glucophage XR | Sustained-release tablet (SRT) | Not available |
| Reg. No. 52/21.2/0090 | Metformin XR 500 mg Accord | Tablet | Not available |

The remaining registrations include fixed-dose combinations with other antidiabetic agents (for example Janumet, Synjardy, Xigduo XR and Amaryl Combi).

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** The knowledge graph links metformin to liver failure, liver disease, kidney disease, congestive heart failure, pancreatitis, gallbladder disease, pyoureter, adrenocortical insufficiency, thymus gland disease, and a range of pituitary deficiency and hypogonadotropic hypogonadism conditions. These should be verified against the approved label.
- **Drug Interactions:** 100 interactions were identified in total; the 20 reviewed include:
  - **Major:** Acetazolamide, ethanol
  - **Moderate:** Dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acetohexamide
  - **Minor:** Acarbose, topical hydrocortisone, topical alclometasone

SAHPRA-approved Professional Information (PI) warnings and contraindications were not available, so please consult the PI before any clinical consideration. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no supportable mechanistic link to focal stiff limb syndrome (Evidence Level L5). The most plausible explanation for the high score is a diabetes-related knowledge-graph association rather than a therapeutic effect.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for metformin (for example from DrugBank)
- A systematic literature search for metformin in stiff-person spectrum disorders
- Preclinical or mechanistic evidence linking metformin to GABAergic or autoimmune pathways in this condition
- Review of the major interactions (acetazolamide, ethanol) and the listed contraindications for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

