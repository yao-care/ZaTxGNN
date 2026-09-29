---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 420
evidence_level: L5
indication_count: 7
---

# Sodium Fluoride
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

# Sodium Fluoride: From Nutritional Trace-Element Supplementation to Epiglottitis

## One-Sentence Summary

Sodium fluoride is registered in South Africa as a component of trace-element infusions and a prenatal capsule. No approved indication text is recorded for it.
The TxGNN model predicts it may be effective for **epiglottitis**, but this is a model prediction only.
There are **0 clinical trials** and **0 publications** for this indication, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record (registered products are trace-element infusions and a prenatal capsule) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium fluoride is a component of trace-element and prenatal supplement products. No original indication is recorded, so a mechanistic link to epiglottitis cannot be established.

The only plausible rationale is speculative. In vitro, fluoride inhibits bacterial enolase and glycolysis, which is antibacterial. This has not been shown at clinically safe systemic concentrations. Epiglottitis is usually caused by *Haemophilus influenzae* type b or other pathogens, and effective antibiotics and vaccination already exist.

The high score (99.92%, model rank 718) reflects the knowledge-graph model only. The same pattern appears for the other top predictions: urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease and xanthogranulomatous pyelonephritis. All are infection or inflammation related, with scores above 99.8% and no trials or literature. Gonococcal and Ureaplasma urethritis have identical scores, which suggests a shared graph-neighbourhood artefact rather than a disease-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for epiglottitis.

For the rank 7 prediction (laryngitis), five publications were retrieved, but they are only indirectly related:
- One 1975 in vitro study of diphtheria toxin modulation.
- One animal study of dietary fluorine toxicity in broilers.
- Three case reports of 18F-NaF PET/CT uptake in laryngeal or thyroid cartilage.

The PET reports reflect the diagnostic radiotracer use of 18F-NaF, not treatment. None of this supports a repurposing claim.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/24/0462 | Peditrace 10ml pdp100010 | Infusion | Not stated in the registration record |
| Reg. No. 49/24/0996 | Addaven | Infusion | Not stated in the registration record |
| Reg. No. 52/24/0031 | Nutryelt | Infusion | Not stated in the registration record |
| Reg. No. H2466 | Complenatal Ff | Capsule | Not stated in the registration record |

Of the 17 registrations, the first 5 records are shown; the H2466 entry appears twice and is listed once. EML inclusion status is not available in the data provided. No registered dosage form is an inhaled or otherwise airway-directed product suited to epiglottitis, and route compatibility has not been assessed.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (Evidence Level L5). There are no trials or publications for epiglottitis, and no mechanism is documented. Effective standard treatments exist, so there is no clinical need to justify moving forward on this evidence.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI) for warnings and contraindications, which blocks any safety screening.
- Mechanism of action data, for example from DrugBank.
- The original approved indication, and a comparison of it with the predicted indication.
- In vitro activity against epiglottitis pathogens at safe concentrations, and a review of fluoride systemic toxicity, including renal handling.
- A route and formulation compatibility assessment.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

