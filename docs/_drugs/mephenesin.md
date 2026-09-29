---
layout: default
title: Mephenesin
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Mephenesin
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

# Mephenesin: From Centrally Acting Muscle Relaxant to Metastatic Melanoma

## One-Sentence Summary

Mephenesin is generally described as a centrally acting muscle relaxant and is registered in South Africa as an oral tablet.
The TxGNN model predicts it may be effective for **metastatic melanoma**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Metastatic melanoma |
| TxGNN Prediction Score | 96.26% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

The registration record does not state an approved indication.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mephenesin is generally described as a centrally acting muscle relaxant, and the supplied data documents no link between this drug and melanoma biology. The high score (0.963) is a model output only.

The other top-ranked predictions suggest the score reflects knowledge-graph structure rather than drug-specific biology:

- **Melanoma cluster:** Non-cutaneous, epithelioid cell and eyelid melanoma score 0.954–0.957. These are likely driven by proximity to other melanoma nodes in the graph, not independent evidence.
- **Cataract cluster:** Five cataract subtypes share an identical score (0.9547), which points to a shared graph node or neighbourhood effect rather than a disease-specific signal.
- **Choroideremia:** This is a monogenic inherited retinal degeneration (CHM gene), and no plausible link to a muscle relaxant is documented.

The predictions should therefore be treated as hypotheses to screen, not as findings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 56/2.8/0309 | Pynspas | Tablet |

Route of administration: oral only. Essential Medicines List (EML) status is not available in the supplied data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (Evidence Level L5). There are no trials or publications, no mechanism of action data, and no safety data from the package insert. The clustered and identical scores across related diseases suggest graph artefacts rather than real signal. Safety screening cannot start until the PI has been reviewed.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), to enable safety screening
- Mechanism of action data (for example from DrugBank) to test whether any biological link to melanoma exists
- A systematic PubMed and trial-registry search (ClinicalTrials.gov, SANCTR, PACTR) for mephenesin in melanoma
- Preclinical or in vitro evidence, since none exists yet
- A route-compatibility assessment once a plausible indication is identified

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

