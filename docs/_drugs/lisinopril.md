---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From an ACE Inhibitor to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an oral ACE inhibitor marketed in South Africa. The approved indication text was not captured in this Evidence Pack.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but **no clinical trials and no publications** currently support this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Lisinopril is an ACE inhibitor. ACE inhibition lowers angiotensin II, which is thought to limit ventricular remodelling after a heart attack. That makes the mechanistic fit plausible.

The approved indication text was not captured, so the relationship between the original and predicted indications cannot be assessed here. Any label-level use in acute myocardial infarction should be checked against the SAHPRA-approved label before this row is finalised.

The second-ranked prediction, posteroinferior myocardial infarction, has an identical score. This suggests the two are duplicate ontology nodes rather than independent signals, so the high score should not be read as two separate lines of support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 33/7.1.3/0513 | Adco-zetomax | Tablet |
| Reg. No. 37/7.1.3/0392 | Austell-lisinopril | Tablet |
| Reg. No. 41/7.1.3/1050 | Lisinozide 10 Mg | Tablet |
| Reg. No. 37/7.1.3/0160 | Adco-zetomax co 10/12.5 | Tablet |
| Reg. No. 36/7.1.3/0114 | Simayla Lisinopril 20 | Tablet |

Showing 5 of 9 registrations. Oral tablet is the only dosage form recorded. Approved indication text and Essential Medicines List status are not available in the pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug interaction query returned no records. This should not be read as an absence of interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials or publications for this indication (L5), and the pack has no safety data from the SAHPRA PI. The mechanism is plausible, but a model score alone is not enough to advance.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications) to complete safety screening and confirm whether acute MI use is already on-label
- Mechanism of action data, for example from DrugBank
- A targeted trial and literature search for lisinopril in acute myocardial infarction, including post-MI remodelling
- Confirmation of whether the posterolateral and posteroinferior MI entries are duplicate ontology nodes
- For context, the pack's tenth-ranked prediction, chronic pulmonary heart disease, has the most supporting material (L3, two lisinopril-specific publications whose designs still need verification). It may be a better candidate for follow-up.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

