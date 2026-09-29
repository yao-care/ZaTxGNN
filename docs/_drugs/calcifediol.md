---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Calcifediol: From an Unrecorded Original Indication to Vitamin D Deficiency

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D) is the main circulating vitamin D metabolite. It is registered in South Africa in oral capsule products, but the record does not state an approved indication.
The TxGNN model predicts it may be effective for **"obsolete vitamin D deficiency"**, an outdated ontology term. This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data |
| Predicted New Indication | Obsolete vitamin D deficiency (outdated ontology term) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Calcifediol is 25-hydroxyvitamin D, the circulating form of vitamin D that the body measures to judge vitamin D status. It is the intermediate produced by liver hydroxylation of vitamin D and is later converted to active calcitriol in the kidney. On that basis, a link to vitamin D deficiency is biologically plausible.

However, the predicted disease name is an obsolete ontology term, and no trials or publications are attached to it. The score of 99.99% reflects how the model ranks drug-disease links. It is not clinical evidence. The entry should be mapped to a current vitamin D deficiency concept, and evidence re-collected, before any real assessment.

Other predictions for calcifediol have more literature but still no direct trials:
- **Vitamin D-dependent rickets (L4):** the most promising rationale applies only to type 1B (25-hydroxylase deficiency), where calcifediol directly bypasses the missing enzyme step. The two registered trials are non-phased and address general vitamin D insufficiency or magnesium-related vitamin D resistance, not this disease.
- **Hereditary hypophosphatemic rickets (L4) and renal tubular acidosis (L4):** the evidence is indirect (physiology studies, animal models, old case reports). Calcifediol would not correct the primary defect in either condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2466 | Complenatal Ff | Capsule | Not recorded |
| H2466 | Complenatal Ff | Capsule | Not recorded (duplicate entry of the same registration) |
| H2062 (ACT 101) | Filibon | Capsule | Not recorded |

All registered products are oral capsules. Manufacturer and approved indication text are blank in the source data, so the original indication could not be confirmed.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The package insert warnings and contraindications have not been retrieved. This is flagged as a blocking gap for safety screening. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is an obsolete disease term with no trials, no literature and only model-level support (L5). Safety information is missing, and the original indication cannot be confirmed from the registration data.

**To proceed, the following is needed:**
- Map "obsolete vitamin D deficiency" to a current vitamin D deficiency concept and re-run the evidence collection.
- Obtain the SAHPRA package inserts (warnings, contraindications, interactions, approved indications) for H2466 and H2062.
- Obtain mechanism of action data from DrugBank (DB00146).
- Confirm the calcifediol content and dose in each registered product, including whether these are multi-ingredient products.
- Optionally, scope a separate feasibility review of vitamin D-dependent rickets type 1B, the only alternative prediction with a clear mechanistic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

