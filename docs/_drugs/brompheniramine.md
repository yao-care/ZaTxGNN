---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 2
---

# Brompheniramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Brompheniramine: From Antihistamine Use to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation H1 antihistamine, marketed in South Africa as Ilvico syrup and tablets. The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score and drug-class reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (first-generation H1 antihistamine) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Based on known information, brompheniramine belongs to the first-generation H1-receptor antagonist class. Its effect on allergic conditions is well recognised at class level, and mechanistically it may be applicable to allergic urticaria.

In allergic urticaria, mast cells release histamine, which produces the typical itchy wheal-and-flare reaction. Blocking the H1 receptor is a biologically coherent way to reduce these symptoms. The high TxGNN score probably reflects this drug-class relationship.

Two cautions apply:
- The mechanism link is a class-level inference. It has not been verified against a drug-specific record.
- Brompheniramine is already marketed, so this may be an existing class use rather than true repurposing. That should be checked against the SAHPRA-approved label.

A second prediction, **cold urticaria** (score 99.55%), has the same weaknesses. Cold exposure triggers mast cell degranulation and histamine release, so H1 blockade is plausible. However, no trial or publication supports brompheniramine in this condition, and the score likely reflects general antihistamine–urticaria associations. It is rated Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR records were not supplied for this candidate).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C769 (ACT 101/1965) | Ilvico | Syrup | Not listed in the supplied record |
| C770 (ACT 101/1965) | Ilvico | Tablet | Not listed in the supplied record |

Essential Medicines List (EML) inclusion status was not supplied and should be confirmed separately.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial or publication supports it (L5). The mechanism, the original indication and the safety profile are all missing from the record. The drug is already marketed and may already be used for allergic conditions, so it is unclear whether this is new.

**To proceed, the following is needed:**
- The SAHPRA package insert, to confirm the approved indications (including whether allergic urticaria is already covered), warnings and contraindications
- Mechanism of action data for brompheniramine, for example from DrugBank
- A literature and trial search specific to brompheniramine in allergic urticaria and cold urticaria
- A route compatibility check for the predicted indication against the syrup and tablet forms
- Confirmation of Essential Medicines List (EML) status

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

