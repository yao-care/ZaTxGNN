---
layout: default
title: Dl-Alpha-Tocopherol
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
monitor_inn: "DL-alpha-Tocopherol"
predicted_indications: ["mature cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "immature cataract", "diabetic cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "antithrombin deficiency type 2"]
last_modified_at: 2026-10-29
description: "Dl-Alpha-Tocopherol: predicted new indication Mature cataract (evidence level L5). Approved use: Not stated in the SAHPRA licence data compiled for this report"
---

# Dl-Alpha-Tocopherol
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

## DL-alpha-Tocopherol: From Vitamin E Supplementation (Cernevit Infusion) to Mature Cataract
{: .text-alpha }

## One-Sentence Summary

DL-alpha-Tocopherol is a form of vitamin E, a lipid-soluble antioxidant. In South Africa it is registered only as a component of a multivitamin infusion product (Cernevit).
The TxGNN model predicts it may be effective for **mature cataract**, but the data compiled for this report contain **0 clinical trials** and **0 publications** that directly study this disease.
The prediction is therefore supported by the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA licence data compiled for this report |
| Predicted New Indication | Mature cataract |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, tocopherol is a lipid-soluble, chain-breaking antioxidant that protects lipids in cell membranes from oxidative damage.

Oxidative damage to lens proteins and lipids is a recognised contributor to lens opacity, so an antioxidant rationale is biologically plausible. However, a mature cataract is an advanced, structurally established opacity, and antioxidants are not expected to reverse it. At most, antioxidant therapy might slow early-stage progression.

The other predicted indications have similarly high scores (0.9997 to 0.9998) from the TxGNN model (deep learning). These scores may reflect similarities the model learned between related diseases in the broader "cataract" group, not biological evidence. Some have a plausible oxidative-stress link (diabetes-associated, nuclear senile, cortical, senile and immature cataract). Others have no clear link, including craniostenosis cataract, tetanic cataract and antithrombin deficiency type 2. These are likely model artefacts rather than disease-specific signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publication directly studies mature cataract. The only publication linked to the related prediction "diabetic cataract" is listed below for transparency. It is an animal study of a non-cataract oxidative-stress model, not clinical evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12770645](https://pubmed.ncbi.nlm.nih.gov/12770645/) | 2003 | Animal study (rat) | The Journal of Nutritional Biochemistry | Vitamin E (dl-alpha-tocopherol acetate) supplementation was examined for protection against carbon tetrachloride-induced oxidative stress in rats. It did not study cataract or diabetes. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/22.1/0508 | Cernevit | Infusion | Not stated in the data compiled for this report |

Cernevit is a multi-ingredient vitamin product. Its licence does not describe how tocopherol alone is approved or marketed. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trial or publication directly studies mature cataract (Evidence Level L5). Mature cataract is an advanced structural opacity that an antioxidant is not expected to reverse. Safety data from the SAHPRA package insert are also missing.

**To proceed, the following is needed:**
- A literature review of published observational and randomised antioxidant (vitamin E) supplementation studies in cataract, particularly age-related and early-stage forms, which are more biologically plausible targets than mature cataract
- The SAHPRA Professional Information (warnings and contraindications), and confirmation of the approved indication for Cernevit
- Mechanism of action data (for example from DrugBank)
- Assessment of route compatibility, since the only local product is an intravenous infusion and no ocular or oral single-ingredient route has been evaluated
- Re-evaluation of the prediction for earlier-stage cataract types, as these are better candidates than mature cataract
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

