---
layout: default
title: Dextropropoxyphene
parent: Model Prediction Only (L5)
nav_order: 171
evidence_level: L5
indication_count: 1
---

# Dextropropoxyphene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Dextropropoxyphene: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Dextropropoxyphene is a weak opioid analgesic, generally used for mild to moderate pain (the registration records supplied contain no indication text).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction, and the proposed mechanism is doubtful.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration records; generally used as an opioid analgesic for mild to moderate pain |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% (model rank 3015) |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Dextropropoxyphene is generally known as a weak mu-opioid agonist, but no mechanism data was supplied to confirm this.

NSIAD is caused by gain-of-function variants in *AVPR2* (rarely *GNAS*). These variants make the vasopressin V2 receptor signal constantly, even without vasopressin, so the kidneys retain too much water. A treatment would need to reduce V2 receptor-mediated water reabsorption. No such pathway is documented for dextropropoxyphene.

The prediction is therefore hard to justify on mechanistic grounds. Mu-opioid activity is more often linked to increased ADH release or water retention, so the predicted effect may run opposite to a benefit. The high score (99.46%) reflects a knowledge-graph association only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. E/2.9/97 | Doxyfene | Capsule | Not provided in the registration record |
| Reg. No. B1334 (OM) | Lentogesic | Capsule | Not provided in the registration record |

Both products are oral capsules. Essential Medicines List (EML) status could not be determined from the data supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Dextropropoxyphene has been withdrawn in several jurisdictions because of cardiotoxicity (QT prolongation and arrhythmia risk) and toxicity in overdose. The "Marketed" status in this report should be checked against the drug's current regulatory position in South Africa.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or publications. The proposed mechanism is doubtful, and the drug's cardiotoxicity history makes further investigation unattractive without a strong reason.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI) for both registered products, to obtain the approved indications, warnings and contraindications
- Confirmation of the current SAHPRA regulatory status of dextropropoxyphene
- Mechanism of action data (for example from DrugBank), and evidence that the drug can reduce V2 receptor-mediated water reabsorption
- A safety review, particularly of QT prolongation and arrhythmia risk, before any repurposing work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

