---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus (also type 1 diabetes mellitus and diabetic…"
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Insulin Glargine: From Type 2 Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin, originally used to treat type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are **no clinical trials and no publications** supporting this prediction. It is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (also type 1 diabetes mellitus and diabetic ketoacidosis) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Insulin glargine is a long-acting insulin analogue, and its efficacy in diabetes mellitus is well established. It has no known immunomodulatory mechanism that would be relevant to autoimmune oophoritis.

The most plausible explanation for the prediction is co-occurrence. Autoimmune oophoritis is often seen in polyglandular autoimmune syndromes, which can include type 1 diabetes. This is an association with the original indication, not evidence that insulin glargine treats the ovarian condition. The high score (99.88%) is a knowledge-graph prediction only and should not be read as evidence of efficacy.

**Other top-ranked predictions show the same pattern:**
- **Thiamine-responsive dysfunction syndrome** (99.61%): diabetes is a shared feature. Insulin would only treat the hyperglycaemia, while the primary treatment is thiamine.
- **Focal stiff limb syndrome and classic stiff person syndrome** (99.60%): both are linked to anti-GAD autoimmunity and type 1 diabetes. Insulin would only treat coexisting diabetes.
- **Opsismodysplasia** (99.59%): there is a speculative link through insulin/PI3K signalling (INPPL1/SHIP2), with no clinical support.
- **Pancreatic agenesis** (99.43%): insulin replacement is standard care for the resulting diabetes. This is the same mechanism as the original indication, not a novel repurposing. It is the only prediction with any literature (L4), and that literature is indirect.
- **Lipodystrophy and lipoatrophy conditions** (ranks 7–10, 99.34–99.42%): localized lipodystrophy is a known adverse effect of injected insulin, so these predictions are likely knowledge-graph artefacts. Insulin glargine should not be considered for them.

## Clinical Trial Evidence

Currently no related clinical trials registered for autoimmune oophoritis.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For reference, the only literature retrieved among the top-ten predictions relates to pancreatic agenesis (rank 6). It is indirect and does not study insulin glargine in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Practical aspects of starting insulin therapy in type 2 diabetes |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes associated with endocrine diseases and the impact of new treatments |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Cohort (veterinary) | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 49/21.1/1230 | Toujeo pen 1.5ml | Injection | Not available in the data compiled for this report |
| Reg. No. 51/21.1/0729 | Endulin Select | Solution | Not available in the data compiled for this report |
| Reg. No. 41/21.1/0363 | Optisulin cartridge 3ml | Injection | Not available in the data compiled for this report |

All three registrations are valid single-ingredient products. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs, mostly of moderate severity. Examples from the listed results:
- **Antidiabetic agents (additive glucose-lowering effect):** metformin, pioglitazone, alogliptin, albiglutide
- **Beta-agonists and sympathomimetics:** salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
- **Beta-blocker:** acebutolol
- **Diuretics and others:** hydrochlorothiazide, acetazolamide, doxycycline, alpelisib, ethanol
- **Hormones and corticosteroids:** estradiol, ethinylestradiol, hydrocortisone (moderate); topical hydrocortisone and topical alclometasone (minor)

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis rests only on a knowledge-graph score. There are no trials or publications, and no plausible mechanism by which insulin glargine would treat the condition. None of the other top-ten predictions offers a genuine repurposing opportunity either. Several reflect shared diabetes comorbidity, and the lipodystrophy-related ones reflect adverse effects of the drug.

**To proceed, the following is needed:**
- Mechanism of action data for insulin glargine
- Review of the SAHPRA Professional Information for warnings and contraindications (a blocking gap for safety screening)
- Systematic literature review on insulin or glucose control in autoimmune oophoritis and polyglandular autoimmune syndromes
- Clinical rationale showing a benefit beyond managing coexisting diabetes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

