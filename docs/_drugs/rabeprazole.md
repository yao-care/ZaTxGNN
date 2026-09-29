---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Rabeprazole
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

# Rabeprazole: From Acid-Related Gastric Disorders to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) that suppresses stomach acid, and it is registered in South Africa as Pariet and Ulcopraz 10. The registration data supplied do not state the approved indication, so "acid-related disorders" is inferred from the drug class. The TxGNN model predicts it may be useful for **Smouldering Systemic Mastocytosis**, but this is a **model prediction only, with 0 clinical trials and 0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Rabeprazole is a PPI. It inhibits the gastric H+/K+-ATPase (the "proton pump") and strongly suppresses acid secretion, which is why it heals acid-related ulcers and treats reflux disease. That efficacy is well established, but it is a different disease area from mastocytosis.

The link to smouldering systemic mastocytosis is weak. A symptomatic rationale is conceivable, because acid suppression is sometimes used for gastric symptoms driven by mast-cell mediators. That would be symptom control, not treatment of the underlying disease. No data in the Evidence Pack supports even this idea.

The score most likely reflects proximity to other mastocytosis nodes in the knowledge graph, not a rabeprazole-specific mechanism. **The high score should not be read as clinical support.** The second-ranked prediction, lymphadenopathic mastocytosis with eosinophilia (score 99.35%), has the same limitation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/11.4.3/0206 | Pariet | Tablet | — |
| Reg. No. 56/11.4.3/0623.621 | Ulcopraz 10 | Tablet | — |

Only the oral route (tablet) is registered. The approved indication text was not supplied, so the labelled uses should be confirmed against the SAHPRA Professional Information (PI).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mastocytosis prediction has no trials, no literature and no established mechanism (L5), so the score alone cannot justify clinical use. The only rationale is symptomatic gastric acid suppression, which is not disease modification.

Two other predictions for this drug (active peptic ulcer disease and gastric ulcer) have L1 evidence and a "Proceed with Guardrails" recommendation. Both are established acid-peptic uses, not true repurposing. The label should be checked before they are presented as new.

**To proceed, the following is needed:**
- The SAHPRA package insert, to confirm the approved indications, warnings and contraindications (currently blocking).
- Mechanism of action data from DrugBank.
- Any clinical evidence for rabeprazole or PPIs in mastocytosis, including a search of SANCTR and PACTR. Neither registry has been searched, and no SANCTR or PACTR identifiers were supplied.
- A clear definition of the intended use (symptom control versus disease modification) and the target population.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

