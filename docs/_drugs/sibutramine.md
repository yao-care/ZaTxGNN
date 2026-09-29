---
layout: default
title: Sibutramine
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 4
---

# Sibutramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Sibutramine: From Obesity to Hypervitaminosis

## One-Sentence Summary

Sibutramine is generally described as a serotonin-norepinephrine reuptake inhibitor used for obesity. The SAHPRA record supplied here does not state an approved indication.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record (generally known as an anti-obesity agent) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sibutramine is generally described as a serotonin-norepinephrine reuptake inhibitor used for weight management. No pathway connects this action to vitamin excess, and I could not identify a plausible mechanistic link to hypervitaminosis.

The very high score (99.98%) is a model output only. Knowledge-graph topology or ontology artifacts may explain it, so it should not be read as biological support.

The three other predictions in the pack have the same weakness (all L5, no trials, no publications, decision Hold):
- **Proximal 16p11.2 microdeletion syndrome** (99.98%): only an indirect symptom-level link is conceivable, because the deletion is associated with obesity. Sibutramine's cardiovascular and neuropsychiatric risks would need specific consideration in this population.
- **Obsolete hypertelorism (disease)** (99.97%): an obsolete ontology term for a structural craniofacial feature, with no expected response to a monoamine reuptake inhibitor. It should be mapped to a current ontology entry before further assessment.
- **Frontorhiny** (99.95%): a rare craniofacial malformation with no pharmacological rationale, likely a graph-structure artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/11.3/0313 | Ciplatrim 15 | Capsule (oral) | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records, which does not mean no interactions exist.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

Sibutramine was withdrawn in several major markets over cardiovascular risk. The pack lists it as Marketed in South Africa, so its current registration status should be verified independently with SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature and no identifiable mechanistic link. The drug also carries known cardiovascular safety concerns, and its South African market status needs checking.

**To proceed, the following is needed:**
- Confirm the current SAHPRA registration status of Ciplatrim 15 and obtain the approved PI (warnings, contraindications, approved indication)
- Obtain mechanism of action data (e.g. from DrugBank)
- Present a plausible biological rationale for hypervitaminosis, or treat the prediction as a knowledge-graph artifact
- Complete a safety screening, focused on cardiovascular risk, before any further evaluation
- Map obsolete ontology terms (e.g. hypertelorism) to current entries if those predictions are pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

