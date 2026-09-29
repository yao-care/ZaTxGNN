---
layout: default
title: Zinc Gluconate
parent: Model Prediction Only (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Zinc Gluconate
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

# Zinc Gluconate: Predicted New Indication of Anemia of Prematurity (Hold)

## One-Sentence Summary

Zinc gluconate is a zinc salt marketed in South Africa within several registered products, but the registration data provided contain no approved indication text.
The TxGNN model predicts it may be useful for **anemia of prematurity** with a very high score, but **no clinical trials and no publications** were found to support this.
This is a model prediction only, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc gluconate is a zinc salt, and the registrations found do not state an approved indication. The pack therefore offers no established pathway linking it to anemia of prematurity.

The TxGNN score is high (99.94%), but a high score reflects patterns in the knowledge graph. It is not clinical proof. No trials or literature were retrieved for this indication, and route and formulation suitability for preterm infants has not been assessed. The prediction should be treated as a hypothesis to test, not as a finding.

**Other predictions in the pack (for context only):**
- **Injury** (score 99.89%, L4) has the most supporting material. It is mostly preclinical work, plus a review of zinc and steroid treatment for traumatic anosmia (PMID 25715353). The trials retrieved are indirect, being zinc-containing combinations in COVID-19 or non-zinc interventions for olfactory loss. This remains a research question, not an actionable indication.
- The other eight predicted indications (ranks 3-10) are L4-L5 and rated Hold. They are mostly broad ontology categories or rare conditions, and the literature hits are largely keyword matches unrelated to zinc gluconate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 52/24/0031 | Nutryelt | Infusion |
| Reg. No. G2667 (ACT 101/1965) | Gericomplex | Capsule |
| Reg. No. 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler |

- Approved indication text is not available for any registration in the pack.
- Gericomplex appears twice under the same registration number, so there are 3 distinct products for 4 listed licenses.
- Spiriva Respimat is not normally a zinc product. Please verify this registration against the SAHPRA record, as it may be a data-matching error.
- Essential Medicines List (EML) status was not provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, anemia of prematurity, has a high model score but no trials, no literature and no mechanistic support in the pack. Safety data are also missing, so the candidate cannot move forward.

**To proceed, the following is needed:**
- SAHPRA package insert data (warnings, contraindications, approved indications), which is a blocking gap
- Mechanism of action data, for example from DrugBank
- A targeted search for zinc use and safety in preterm infants and anemia of prematurity
- Assessment of whether any registered zinc product has a suitable route, dose and formulation for neonates
- Verification of the Spiriva Respimat registration match
- Consideration of whether the "injury" prediction (L4) is a better-defined research question, once a specific injury type is chosen

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

