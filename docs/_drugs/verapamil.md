---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 466
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Verapamil: From Cardiovascular Calcium Channel Blocker to Bundle Branch Block (Obsolete Term)

## One-Sentence Summary

Verapamil is an L-type calcium channel blocker registered in South Africa in cardiovascular product categories, but the supplied registration data do not state its approved indications.
The TxGNN model predicts it may be useful for **obsolete bundle branch block**, with **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model output only, and the disease term is flagged "obsolete" in the ontology, so the high score is probably a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 (4 unique registration numbers) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank field. Verapamil is generally understood to be an L-type calcium channel blocker that slows atrioventricular (AV) nodal conduction.

That mechanism is usually a safety concern in conduction disease, not a therapeutic rationale. Slowing conduction in a patient who already has a conduction defect, such as a bundle branch block, could worsen the problem. No mechanistic link to a benefit in this condition can be established from the data provided.

The ontology flags the disease term as "obsolete". The 99.62% score (graph rank 2357) is therefore likely an artifact of how the knowledge graph maps the term. The term mapping should be verified before any further review.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR, PACTR or ICTRP records were retrieved either.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/7.1.4/161 | Verapamil 40 Oethmaan | Tablet | Not stated in supplied data |
| 31/7.1/0637 | Verahexal 240 SR | Sustained-release tablet | Not stated in supplied data |
| 31/7.1.3/0631 | Tarka | Sustained-release (Src) | Not stated in supplied data |
| A39/7.1.3/0508 | Tarka 180mg/2mg | Sustained-release tablet | Not stated in supplied data |

- The Tarka 180mg/2mg registration (A39/7.1.3/0508) appears twice in the source data and is shown once here.
- Tarka appears to be a fixed-dose combination product containing verapamil. Confirm its composition against the PI.
- Essential Medicines List (EML) status was not included in the data supplied.

## Safety Considerations

- **Conduction disease:** Verapamil slows AV nodal conduction. This is a potential safety concern, not a benefit, in conduction disorders such as bundle branch block.

No warnings, contraindications or drug interaction records were available in the supplied data. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials or literature. The target disease term is obsolete, and verapamil's known conduction-slowing effect argues against a therapeutic role.

**Other predicted indications (for context):**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Malignant renovascular hypertension | 99.27% | L4 | Plausible vasodilation link, but the 2 retrieved papers are indirect and do not test verapamil. Suggested as a research question. |
| Malignant hypertensive renal disease | 99.27% | L5 | Same score as the renovascular entry, suggesting a shared ontology parent. No evidence. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.26% | L5 | The 20 retrieved papers are generic hypoxia literature, not verapamil-specific. Calcium channel blockers may worsen ventilation-perfusion matching in hypoxic lung disease. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.26% | L5 | No evidence. Calcium channel blockers are generally limited to vasoreactive subsets. |
| Braddock syndrome | 99.15% | L5 | No mechanistic link identified. |
| Periodic paralysis with transient compartment-like syndrome | 99.08% | L5 | Ion channel involvement is conceivable, but there is no verapamil-specific evidence. |

**To proceed, the following is needed:**
- Verification of the "obsolete bundle branch block" term mapping in the knowledge graph
- SAHPRA package insert warnings, contraindications and approved indications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature review of calcium channel blockers in renovascular hypertension, the only prediction with any (indirect) literature

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

