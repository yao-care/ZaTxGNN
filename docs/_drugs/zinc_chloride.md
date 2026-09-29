---
layout: default
title: Zinc Chloride
parent: Model Prediction Only (L5)
nav_order: 474
evidence_level: L5
indication_count: 3
---

# Zinc Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Zinc Chloride: From Parenteral Trace Element Supplementation to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Zinc chloride is a trace element salt, and its registered South African products appear to be parenteral nutrition and trace element preparations. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data. Product names (Peditrace, Addaven, TPN products) suggest parenteral trace element supplementation, but this is inferred rather than registered wording |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zinc chloride is a zinc source used in trace element and nutrition formulations, and mechanistically it may be relevant to the eye because zinc is a cofactor for antioxidant enzymes such as SOD1.

The link to diabetic retinopathy is a hypothesis only: zinc might modulate oxidative stress in the diabetic retina. Nothing in the supplied data confirms this. The similarity between the original and predicted indications has not been assessed. A high model score is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

The registration data do not include approved indication text, so that column is omitted. Only 5 of the 10 registrations were supplied.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Y/6.1/415 | Dopamine HCl Fresenius 5 ml 200 mg/5 ml | Injection |
| 29/24/0462 | Peditrace 10 ml | Infusion |
| 49/24/0996 | Addaven | Infusion |
| ARTICLE 21B N/A | ITN 3007M 2500 ml | TPN |
| EXCLUSION UNDER SECTION 36 & SECTION 14 | ITN 55A 600 ml | TPN |

- The dopamine product is an unexpected match for a zinc salt. Verify it against its ingredient list.
- The last two entries carry no standard registration number. They appear to be special-access or exclusion entries.
- All listed forms are parenteral, so no ocular or topical product is registered.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature and no verified mechanism. Safety information is also missing, which blocks safety screening.

**Other predictions in the pack:**
- **Sjögren syndrome** (score 99.18%) has no trials or literature.
- **Dry eye syndrome** (score 99.18%) is the only prediction with trials, rated L4 and worth a research question. Both trials are small, completed and indirect, and no results were supplied:
  - [NCT02951910](https://clinicaltrials.gov/study/NCT02951910) is a Phase 4 trial (n=20) of zinc-hyaluronate, which is a different compound from zinc chloride.
  - [NCT01541891](https://clinicaltrials.gov/study/NCT01541891) is a Phase 2 trial (n=30) of PRO-148 versus Systane. Its composition is unconfirmed.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications. This is a blocking gap.
- Mechanism of action data, for example from DrugBank.
- A targeted literature and trial search for zinc in diabetic retinopathy.
- Confirmation of the original registered indication and of the dopamine product's link to zinc chloride.
- An assessment of route compatibility, since all registered products are parenteral and the predicted indications are ocular.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

