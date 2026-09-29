---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Vitamin A
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Vitamin A: From Vitamin Supplementation to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A is an essential fat-soluble vitamin, and in South Africa it is registered as a component of parenteral nutrition, multivitamin and prenatal products.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but the retrieved evidence does not support this: **0 publications** and **5 clinical trials**, none of which tests vitamin A for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records. The registered products are vitamin and nutritional supplements, so "vitamin supplementation" is inferred from product type. |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Vitamin A (retinol) is known to act through retinoid receptors to support vision, epithelial integrity, immunity and cell differentiation.

There is no credible mechanistic link to this predicted indication. Prothrombin synthesis and function depend on vitamin K, through gamma-carboxylation of clotting factors, and not on vitamin A. The very high TxGNN score (99.97%) is not supported by any retrieved trial or publication. It most likely reflects a knowledge-graph artefact, such as shared "vitamin" or nutrient-deficiency neighbours, and should not be read as a real efficacy signal.

## Clinical Trial Evidence

All five retrieved trials were graded "C" (weak relevance). None tests vitamin A, and none studies congenital prothrombin deficiency.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Observational study of bone loss in haemophilia. No vitamin A intervention. |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Retrospective characterisation of adult inborn errors of metabolism in Switzerland. No vitamin A intervention. |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | Prothrombin complex concentrate (Beriplex P/N) for acquired factor II/VII/IX/X deficiency due to oral anticoagulation. Does not test vitamin A. |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Randomised, double-blind trial in decompensated cirrhosis. The tested vitamin cannot be confirmed as vitamin A, and the condition does not match. |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Dietary supplement combination and endothelial function in mild-to-moderate hypertension. Unrelated condition. |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Sixteen registrations contain vitamin A. Five are shown below. Approved indication text was not recorded in the registration data, and Essential Medicines List (EML) status could not be checked from the available data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Z/22.1/236 | Vitalipid Novum Adult 10 ml | Infusion | Not recorded |
| 30/22.1/0201 | Vitalipid Novum Infant 10 ml | Infusion | Not recorded |
| A/21.8.1/743 | Menoflush | Tablet | Not recorded |
| H2466 | Complenatal FF | Capsule | Not recorded |
| L/24/329 | Dextrose 20% in water 500 ml | Infusion | Not recorded |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

General caution from the wider evidence pack: excess vitamin A is teratogenic, so any antenatal use needs care. Some prospective studies also link high vitamin A intake to increased fracture risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trial or publication and no plausible mechanism, since prothrombin depends on vitamin K. The high model score is most likely a knowledge-graph artefact.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications for the registered vitamin A products
- Mechanism of action data, for example from DrugBank
- Any experimental or clinical evidence of a vitamin A effect on prothrombin or coagulation
- Resources are better directed to other predicted indications with more support. Perinatal disease has systematic reviews of vitamin A in very low birth weight infants, though this is already an established use. Radiation- or chemically-induced disorder has RCT evidence for topical retinoids in photoaging, but this evidence does not extend to radiation or chemical injury. Both are graded L2 and still need manual verification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

