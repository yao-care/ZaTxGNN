---
layout: default
title: Phenyltoloxamine
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Phenyltoloxamine
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

# Phenyltoloxamine: From Antihistamine Combination Products to Allergic Urticaria

## One-Sentence Summary

Phenyltoloxamine is a first-generation H1 antihistamine, sold in South Africa as an ingredient in combination oral tablets such as Sinutab and Suncodin. The TxGNN model predicts it may be useful for **allergic urticaria**. There are currently **0 clinical trials** and **0 publications** for this drug-disease pair, so the prediction rests on class-level reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration data supplied |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 96.24% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this drug. Phenyltoloxamine belongs to the first-generation H1 antihistamines, and H1 receptor blockade is the standard way to control the itch and wheals of urticaria. The mechanistic fit is therefore high.

This also means the result is more likely a rediscovery of an antihistamine class effect than a true repurposing finding. No phenyltoloxamine-specific data were supplied for urticaria. First-generation agents are sedating and anticholinergic, which is a disadvantage against non-sedating alternatives.

The other top-ranked predictions vary in plausibility:
- **Cold urticaria** (score 93.2%) has a good mechanistic fit, but no specific evidence was supplied.
- **Nasal cavity disease**, **pharyngitis** and **acute laryngopharyngitis** could see symptomatic relief only.
- **Anorectal stricture**, **anal polyp** and **proctitis** have no plausible antihistamine mechanism and are probably knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria. No SANCTR or PACTR entries were supplied.

For context, one trial is linked to a different prediction, pharyngitis (rank 6). It is [NCT00378144](https://clinicaltrials.gov/study/NCT00378144), a completed Phase 4 community pharmacy study (n=469) of a Sinutab product for nasal congestion and headache in the common cold. The supplied data do not show that phenyltoloxamine is in the studied product or that its effect can be separated from other ingredients, so it does not support the allergic urticaria prediction.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Six registrations are reported, but only five entries were supplied, and Reg. No. F/5.8/279 appears twice. All are oral tablets. No approved indication text was supplied, and no Essential Medicines List (EML) status was provided.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| F/5.8/279 | Sinutab With Codeine | Tablet | Not listed |
| B697 (ACT 101 1965) | Suncodin Tablets | Tablet | Not listed |
| F/5.8/275 | Sinutab | Tablet | Not listed |
| Y/5.8/264 | Adco-sinal co | Tablet | Not listed |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible but is supported only by the model score and class-level reasoning. There are no trials or publications, and the safety data needed for screening are missing. First-generation sedating agents are also unlikely to offer an advantage over established non-sedating antihistamines for urticaria.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Confirmation of which registered products actually contain phenyltoloxamine, and their approved indications
- A targeted literature search for phenyltoloxamine in urticaria
- A comparison against non-sedating second-generation antihistamines to define any added value

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

