---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue, originally used to control blood glucose in type 1 and type 2 diabetes mellitus and to manage diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are **no clinical trials and no publications** supporting this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 and type 2 diabetes mellitus, diabetic ketoacidosis (the SAHPRA registration entry carries no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting human insulin analogue. Its efficacy in lowering blood glucose in diabetes is well established. It acts as a replacement hormone rather than an immune-modulating drug.

The only plausible link to autoimmune oophoritis is the overlap of autoimmune endocrine conditions with type 1 diabetes (autoimmune polyendocrine syndromes). Insulin lispro has no known immunomodulatory action on ovarian autoimmunity. The high score most likely reflects network proximity to autoimmune endocrine disease in the knowledge graph, not a therapeutic mechanism. The prediction should be treated as unverified.

### Other Predicted Indications (All Hold)

None of the other predictions have supporting clinical trials. They are summarised below.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Thiamine-responsive dysfunction syndrome | 99.37% | L5 | Diabetes is a feature of the disease. Insulin only manages this symptom, and thiamine is the disease-directed therapy. |
| 3 | Classic stiff person syndrome | 99.36% | L5 | Association with anti-GAD65 autoimmunity and comorbid type 1 diabetes. Insulin does not treat the neurological disease. |
| 4 | Focal stiff limb syndrome | 99.36% | L5 | Same reasoning as stiff person syndrome. |
| 5 | Opsismodysplasia | 99.34% | L5 | A speculative pathway link (INPPL1/SHIP2 in insulin signalling). No evidence, and hypoglycaemia risk is not justified. |
| 6 | Drug-induced localized lipodystrophy | 99.09% | L5 | Insulin causes this as an injection-site adverse effect. Likely a false-positive signal. |
| 7 | Pancreatic agenesis | 99.09% | L4 | Insulin replacement is rational and already standard care. It is not a novel repurposing. |
| 8 | Centrifugal lipodystrophy | 99.04% | L5 | A localized paediatric skin and fat disorder. Insulin has no demonstrated role. |
| 9 | Pressure-induced localized lipoatrophy | 99.03% | L5 | Mechanical in origin. Injection-site lipoatrophy is an insulin adverse effect. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for autoimmune oophoritis, and none for the other predicted indications.

---

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

One general review was supplied for the rank 7 prediction (pancreatic agenesis). It is indirect and not specific to that condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Reviews the increasing use of insulin therapy in type 2 diabetes and practical aspects of starting it |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/21.1/0785 | Humalog vial 10ml | Injection | Not recorded in the data compiled for this report |

Insulin lispro is available only as an injectable product in South Africa. The data compiled for this report do not show its Essential Medicines List (EML) status.

---

## Safety Considerations

**Drug Interactions:** The interaction query returned 100 records. The main ones from the first 20 reviewed are listed below.

- **Moderate:** phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, doxycycline, epinephrine, levonorgestrel, hydrocortisone, albiglutide, salbutamol, ethanol, hydrochlorothiazide, alogliptin, metformin, estradiol, alpelisib, ethinylestradiol
- **Minor:** topical hydrocortisone, topical alclometasone

Many of these affect blood glucose, so glucose monitoring is important when they are combined with insulin.

**Other Safety Notes:** Injection-site lipodystrophy and lipoatrophy are known adverse effects of insulin, including lispro. Hypoglycaemia is the main risk of giving insulin to patients without diabetes.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis rests only on a model score. There are no trials or publications, and no plausible therapeutic mechanism. The other predictions are either existing diabetes management, adverse-effect associations, or speculative.

**To proceed, the following is needed:**
- Mechanism of action data, and any evidence that insulin lispro affects ovarian autoimmunity
- Preclinical or clinical studies in autoimmune oophoritis
- The SAHPRA Professional Information (warnings and contraindications), which is currently missing
- A hypoglycaemia risk assessment for use in non-diabetic patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

