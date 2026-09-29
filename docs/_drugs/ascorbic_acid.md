---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: Repurposing Prediction for Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ascorbic acid (vitamin C) is marketed in South Africa across 20 SAHPRA registrations, but the source data does not record an original indication.
The TxGNN model ranks **non-syndromic esophageal malformation** as its top prediction (score 99.96%).
No clinical trials or publications support this prediction, and no plausible mechanism links ascorbic acid to a congenital structural malformation. It is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.96% (model rank 398) |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ascorbic acid in this dataset. Ascorbic acid is an antioxidant and a cofactor in collagen synthesis. Neither role explains how it could prevent or treat a congenital malformation of the esophagus, which is a structural defect arising during embryonic development.

The evidence review found no trials or literature linking the two, so the high score is unlikely to reflect real biology. It probably comes from the way the knowledge graph connects nodes. The similarity between the original and new indication could not be assessed because the original indication is missing from the data.

Other predictions for this drug have more supporting material. They are noted in the conclusion below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Twenty registrations exist in total. The dosage forms include oral tablets, capsules and effervescent tablets, as well as sachets, syrups, infusions and TPN products. Five main registrations are shown below. The approved indication text was not provided for these products.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| B/2.8/1329 | Paracetacod | Tablet |
| C1009 | Fluend | Capsule |
| 35/5.8/0152 | Flutex effervescent | Effervescent tablet |
| H0689 (ACT 101/1965) | Autrin | Capsule |
| Y/5.8/308 | Demazin Flu | Effervescent tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanism, so it is Level L5 and not actionable. It should not advance to safety screening.

**Other predictions with more supporting data:**
- **Vitamin deficiency disorder (L3):** This is probably an established use missing from the original-indication field, rather than true repurposing. Confirm the labelled indications first.
- **Perinatal disease (L2):** Completed Phase 3 trials exist, but they mostly test vitamin combinations. Large published vitamin C+E preeclampsia trials have reported no benefit and possible harm, so results must be checked before any advancement.
- **Injury (L3):** Several Phase 2 trials are registered, but none has completed with results in this data.
- **Esophageal disease (L4):** Evidence is mixed. Rat studies show enhanced esophageal carcinogenesis when ascorbic acid is combined with nitrite, and case reports describe esophagitis or strictures linked to ascorbic acid tablets (PMIDs 17953708, 131047, 3606243). This is a safety signal for any esophageal use.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap): download and parse the PI PDF.
- Mechanism of action data (DrugBank).
- The original and labelled indications, including Essential Medicines List (EML) status, to separate true repurposing from established use.
- Independent evidence review before any further work on the esophageal malformation prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

