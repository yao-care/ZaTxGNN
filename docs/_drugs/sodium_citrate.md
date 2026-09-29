---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Sodium Citrate
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

# Sodium Citrate: From an Unspecified Registered Indication to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate is registered in South Africa, mainly in oral tablets and syrups, but the registration records supplied do not state its approved indication.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration records |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium citrate's original mechanism could not be retrieved, and the registration records give no approved indication. Without either, the link between its established use and papillary conjunctivitis cannot be assessed.

No plausible mechanism for this prediction is documented in the supplied data. The high TxGNN score (99.95%) reflects a pattern in the knowledge graph, not evidence that the drug works in this condition.

Route of administration is also a concern. All registered sodium citrate products found are oral (tablets) or syrups and solutions. Conjunctivitis would normally need an ophthalmic formulation, and none is registered.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Sodium citrate has 16 SAHPRA registrations. The five below are the main ones. Several product names suggest codeine-containing combination products, so sodium citrate may be one component among several. The records supplied do not include approved indication text or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 43/2.6.5/0042 | Rispevon | Tablet |
| Reg. No. Y/2.8/306 | Paincodein | Tablet |
| Reg. No. G/10.1/1112 | Broncleer & cod unboxed | Syrup |
| Reg. No. G998 (OM) | Tussilinct cough | Syrup |
| Reg. No. G1053 (ACT 101 OF 1965) | Phenorant with codeine | Syrup |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, no documented mechanism and no ophthalmic product registered. Safety information from the package inserts is also missing.

Other predicted indications are similarly weak. Only "stomach disease" has any supporting material (L4), and that is limited to in vitro gastric cancer cell studies, with no clinical evidence.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, downloaded from the SAHPRA website
- Mechanism of action data (for example, from the DrugBank API)
- The approved indication for each registered product, to establish the original use
- Evidence that a suitable ophthalmic formulation and route is feasible
- Any clinical or preclinical study of sodium citrate in papillary conjunctivitis

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

