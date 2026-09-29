---
layout: default
title: Dimethicone
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Dimethicone
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

# Dimethicone: From Unspecified Original Indication to Insomnia

## One-Sentence Summary

Dimethicone is an inert, topically applied silicone polymer. The Evidence Pack does not record an approved indication for it in South Africa.
The TxGNN model predicts it may be effective for **insomnia**, but this rests on a model score alone. There is **1 clinical trial** on record, graded not relevant to sleep, and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dimethicone is a silicone polymer that is applied topically and is chemically inert. It has negligible systemic absorption and no known central nervous system or sleep-related activity.

No plausible mechanistic link to insomnia was identified. The high TxGNN score of 0.94 is most likely a knowledge-graph artefact rather than a real pharmacological signal.

The same pattern appears in the other predictions for this drug. Nine cataract subtypes and severe nonproliferative diabetic retinopathy score 92–93%, many with identical scores. This suggests one correlated graph signal rather than independent findings.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | Not applicable | Completed | 74 | Oral supplement plus topical product for skin health (redness, sensitivity, reactive skin). It has no sleep outcomes, so it was graded not relevant to insomnia. |

No SANCTR, PACTR or ICTRP trials were found.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E1691 (OM) | Propan gel s | Suspension | Not stated in the record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical or literature evidence (L5). There is no plausible mechanism for a topical, non-absorbed silicone in insomnia, and the only trial on record is unrelated to sleep. The score most likely reflects a knowledge-graph artefact.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which currently blocks safety screening
- Mechanism of action data, for example from DrugBank
- The approved indication and route of use for the registered product
- Any credible mechanistic or clinical evidence linking dimethicone to sleep outcomes. Without it, this candidate should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

