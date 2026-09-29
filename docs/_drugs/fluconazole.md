---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Fluconazole
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

# Fluconazole: From Antifungal Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an oral azole antifungal, marketed in South Africa as capsules.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (fluconazole is an antifungal) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Fluconazole is an azole antifungal that inhibits fungal CYP51, an enzyme in ergosterol synthesis. Its efficacy in fungal infections is established.

The mechanistic link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is most often viral (adenoviral) or immune-mediated, so an antifungal has no clear rationale. The high score is more likely a knowledge-graph association than a real pharmacological signal. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were identified in the Evidence Pack.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/20.2.2/0534 | Mycorest | Capsule | Not provided in source data |
| A38/20.2.2/0559 | Ralmient | Capsule | Not provided in source data |
| A38/20.2.2/0558 | Ralmient | Capsule | Not provided in source data |

All three registered products are oral capsules. No topical or ophthalmic formulation is registered. This matters because the predicted indication is an ocular surface disease. Essential Medicines List (EML) status was not included in the Evidence Pack and has not been verified.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, and no plausible antifungal mechanism for a mainly viral or immune-mediated eye condition. No ophthalmic formulation is registered locally.

Among the other model predictions, only *Plasmodium falciparum* malaria has any supporting evidence, and it is limited to in vitro work (L4). It is best treated as a research question, and achievable drug concentrations would need to be checked against the in vitro activity.

**To proceed, the following is needed:**
- SAHPRA-approved PI (warnings, contraindications, approved indications)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking fluconazole to punctate epithelial keratoconjunctivitis
- An assessment of route and formulation feasibility (oral only at present)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

