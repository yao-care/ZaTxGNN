---
layout: default
title: Diphenylpyraline Hydrochloride
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 0
---

# Diphenylpyraline Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

# Diphenylpyraline Hydrochloride: Evaluation Incomplete — No Predictions Generated

## One-Sentence Summary

Diphenylpyraline hydrochloride is a first-generation H1 antihistamine (piperidine class) historically used for allergic rhinitis, urticaria, and pruritus, though no SAHPRA-registered indication text was available in this Evidence Pack.
The TxGNN model **did not generate any repurposing predictions** for this compound — most likely because the DrugBank ID could not be resolved, blocking knowledge graph linkage.
As a result, **no new indications, clinical trials, or supporting literature** are available for evaluation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrievable — no SAHPRA registrations on file |
| Predicted New Indication | None — TxGNN pipeline returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (pipeline did not complete) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline could not complete because the DrugBank ID for Diphenylpyraline Hydrochloride was not resolved, preventing knowledge graph traversal. Without a valid prediction, there is no repurposing candidate to evaluate.

**To proceed, the following is needed:**

- **[Blocking]** Resolve DrugBank ID: Search DrugBank for "diphenylpyraline" (DB00679 is a candidate — verify and populate `drugbank_id`)
- **[Blocking]** Re-run TxGNN prediction pipeline after DrugBank ID is confirmed
- **[High]** Retrieve mechanism of action (MOA) via DrugBank API to support mechanistic rationale once predictions are available
- **[High]** Download and parse any available professional information (PI) or package insert to populate safety warnings and contraindications
- Verify whether any SAHPRA registration exists under alternative brand names (e.g., Lergobine, Histryl) and update `licenses` accordingly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

