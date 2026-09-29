---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 1
---

# Diltiazem
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

# Diltiazem: From Cardiovascular Use to Susceptibility to Ischemic Stroke (Obsolete Term)

## One-Sentence Summary

Diltiazem is a non-dihydropyridine calcium channel blocker that is marketed in South Africa, but the registration records supplied do not state its approved indication.
The TxGNN model predicts it may be relevant to **"obsolete susceptibility to ischemic stroke"**, a retired ontology label for stroke predisposition.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (diltiazem is a calcium channel blocker used in cardiovascular disease) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% (model rank 4,529) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Diltiazem is a non-dihydropyridine L-type calcium channel blocker. It is established cardiovascular therapy, and mechanistically it may be relevant to stroke risk.

A plausible link to ischemic stroke would run through three effects:
- Lowering blood pressure.
- Cerebral vasodilation.
- Heart rate and rhythm control, which could reduce cardioembolic risk.

This reasoning is a hypothesis. The mechanism cannot be checked against source data because no original indications or MOA were supplied.

The predicted disease label is also a problem. "Obsolete susceptibility to ischemic stroke" is a retired ontology term. It describes a risk factor or predisposition, not a treatable clinical indication. The prediction should be remapped to a current stroke or stroke-prevention term before any evidence review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/7.1/0298 | Sandoz Diltiazem HCl 60 | Tablet (oral) | Not stated in data supplied |
| Reg. No. 28/7.1/0579 | Tilazem 180 CR | Slow-release capsule/tablet (SRC) | Not stated in data supplied |
| Reg. No. 30/7.1/0183 | Adco-Zildem SR | Slow-release capsule/tablet (SRC) | Not stated in data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug-drug interaction query returned no records. This is most likely a gap in the dataset and should not be read as evidence of safety.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high TxGNN score, which is a computational prediction and not clinical evidence (L5). The predicted disease is an obsolete term for a risk state rather than a treatable indication, and no trials or publications were found.

**To proceed, the following is needed:**
- Remap the predicted disease to a current stroke or stroke-prevention term, then re-run the evidence search.
- Obtain the SAHPRA package inserts to confirm approved indications, warnings and contraindications. This is a blocking gap for safety screening.
- Retrieve mechanism of action data from DrugBank to support the mechanistic-link analysis.
- Run a proper drug-drug interaction query, since the current empty result is likely a data gap.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

