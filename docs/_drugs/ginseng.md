---
layout: default
title: Ginseng
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
monitor_inn: "Ginseng"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy", "amenorrhea (disease)", "immature cataract", "diabetes mellitus type 2 associated cataract"]
last_modified_at: 2026-10-29
description: "Ginseng: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not stated in the registration records"
---

# Ginseng
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

## Ginseng: From an Unspecified Registered Indication to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Ginseng is a herbal ingredient with two registrations in South Africa, but the registration records do not state an approved indication.
The TxGNN model predicts it may be useful for **drug-induced osteoporosis**, with a very high model score.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Ginseng's active constituents, the ginsenosides, have been proposed in the wider scientific literature to influence bone remodelling. However, none of the data compiled for this report supports that idea for drug-induced osteoporosis. No original indication could be confirmed from the local registration records, so the link between an existing use and this new one cannot be assessed.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not clinical proof. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not stated in the registration record |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not stated in the registration record |

Both registrations are currently valid and are recorded as single-ingredient products. The second record is a branded inhaler that is not normally associated with ginseng. The ingredient mapping for these two records should be verified before relying on them.

## Safety Considerations

- **Drug Interactions:** 83 interactions were identified. The 20 listed in the data compiled for this report are all rated **Moderate**. They cluster in two groups:
  - **Glucose-lowering medicines:** acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide, dulaglutide, semaglutide, lixisenatide, and several insulins (aspart, degludec, detemir, glargine, glulisine). The practical concern is additive blood-glucose lowering, so glucose monitoring is advisable.
  - **Acetylsalicylic acid.**

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis has no supporting trials or publications, so the evidence level is L5. No approved indication or mechanism data could be confirmed to support it.

**To proceed, the following is needed:**
- Preclinical or clinical studies that directly examine ginseng or ginsenosides in drug-induced (for example glucocorticoid-induced) osteoporosis
- Mechanism of action data for the registered products
- Verification of which active ingredients the two SAHPRA registrations actually contain, and their approved indications
- Warnings and contraindications from the SAHPRA Professional Information
- A review of interaction risk, particularly with glucose-lowering medicines and aspirin, in the likely patient population

**Note on other predictions for this drug:** Among the other predicted indications, **diabetic retinopathy** has the most supporting literature (20 records). These are mostly preclinical and review studies, plus one 2026 randomised, double-blind clinical trial of Korean red ginseng (PMID 42395017). This trial is not specific to severe non-proliferative disease. It is a more promising research question than osteoporosis, though still without registered trials or confirmed clinical benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

