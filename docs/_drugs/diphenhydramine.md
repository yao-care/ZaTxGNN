---
layout: default
title: Diphenhydramine
parent: Model Prediction Only (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Diphenhydramine
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

# Diphenhydramine: From Allergic Conditions (H1 Antihistamine Use) to Rosacea Conjunctivitis

## One-Sentence Summary

Diphenhydramine is a first-generation H1 antihistamine, widely used for allergic conditions such as rhinitis and urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis** (score 99.20%), but **no clinical trials and no publications** were retrieved for this specific direction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data (general use: allergic conditions) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Diphenhydramine is known as an H1 receptor inverse agonist with anticholinergic activity. Its efficacy in histamine-driven allergic symptoms is established, and blocking H1 receptors could plausibly relieve histamine-driven ocular itch.

The mechanistic fit is only partial, however. Rosacea-associated ocular disease is mainly inflammatory. It involves meibomian gland dysfunction, *Demodex* mites and innate immune activation, rather than histamine release. H1 blockade may therefore ease itch at most, and is unlikely to treat the underlying disease. The prediction is not supported by any retrieved trial or publication.

## South Africa Market Information

Twenty registrations are on file. The first five are shown below. The register data supplied contain no approved indication text.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 28/2.8/0729 | Tylenol Nightpain | Tablet |
| Reg. No. M/10.1/248 | Flemex | Syrup |
| Reg. No. 30/7.1/0183 | Adco-Zildem SR | Sustained-release capsule (SRC) |
| Reg. No. 43/2.6.5/0042 | Rispevon | Tablet |
| Reg. No. 28/10.1/0249 | Expectalin with Cod | Syrup |

Some product names (for example Adco-Zildem SR and Rispevon) do not obviously contain diphenhydramine. The ingredient-to-registration mapping should be verified against the SAHPRA register before any use. No Essential Medicines List (EML) status was available.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, and the mechanistic link is weak because rosacea ocular disease is mainly inflammatory. The available data support no efficacy claim in this indication.

**To proceed, the following is needed:**
- Retrieve the SAHPRA Professional Information (PI) for safety, warnings and contraindications.
- Obtain mechanism of action (MOA) data from DrugBank.
- Confirm the registered indications and verify the ingredient-to-registration mapping.
- Carry out a targeted search for ocular rosacea and blepharitis studies involving antihistamines.
- Consider prioritising other predictions in this pack. Rhinitis (rank 2, L1) and allergic urticaria (rank 3, L2) have far stronger evidence. Both are established uses rather than novel repurposing, with sedation and anticholinergic effects as the main guardrails.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

