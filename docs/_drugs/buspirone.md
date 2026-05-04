---
layout: default
title: Buspirone
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 0
---

# Buspirone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Buspirone: Repurposing Potential — No TxGNN Predictions Currently Available

---

## One-Sentence Summary

Buspirone is a non-benzodiazepine anxiolytic approved internationally for the treatment of Generalised Anxiety Disorder (GAD). The current Evidence Pack contains **no TxGNN model predictions** for this drug, and Buspirone is **not registered with SAHPRA** for the South African market. A complete repurposing evaluation cannot be conducted until prediction data, mechanism of action details, and full safety documentation have been retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Generalised Anxiety Disorder (GAD) — based on international registration; no SAHPRA-approved indication available |
| Predicted New Indication | No TxGNN predictions available |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (No predictions generated; model output pending) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN predictions are currently present in this Evidence Pack, so a formal mechanistic rationale for a specific repurposing direction cannot be presented at this stage.

Detailed mechanism of action data was not returned in this Evidence Pack. Based on established pharmacology, Buspirone is a partial agonist at serotonin 5-HT1A receptors and has moderate affinity for dopamine D2, D3, and D4 receptors — a profile that is mechanistically distinct from benzodiazepines and has historically generated research interest in areas beyond anxiety management, including adjunctive treatment of major depressive disorder, augmentation in ADHD, and reduction of agitation in neurodegenerative conditions.

These directions remain speculative in this context. Once TxGNN KG and deep learning predictions are generated for DB00490, a full mechanistic evaluation linking the original indication (anxiety) to any predicted new indication can be completed.

---

## South Africa Market Information

Buspirone is currently **not registered with SAHPRA** and holds no approved product listings in South Africa. No registration records are available in this Evidence Pack.

> **Note for prescribers:** Buspirone is widely available as a generic medicine in the United States, European Union, and multiple other jurisdictions. If a compelling clinical need exists, the **Section 21 Authorisation** pathway (unregistered medicines) under the Medicines and Related Substances Act (Act 101 of 1965, as amended) may be applicable. Application is made through SAHPRA and requires documented motivation by the treating clinician.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the [MedSafety online portal](https://www.sahpra.org.za/adverse-drug-reactions/).

> **Important:** As Buspirone is currently unregistered in South Africa, no SAHPRA-approved PI exists. Until local registration is obtained, prescribers should consult internationally recognised product information, such as the **US FDA prescribing information** or the **EMA Summary of Product Characteristics (SmPC)**, for complete guidance on warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Buspirone is not registered in South Africa, the TxGNN pipeline has not yet generated any repurposing predictions for this drug, and critical safety and mechanism-of-action data are absent. There is insufficient evidence to evaluate any specific repurposing direction at this time.

**To proceed, the following is needed:**

- **Run TxGNN predictions:** Execute the KG and deep learning prediction models for Buspirone (DB00490) to generate ranked repurposing candidates and associated evidence bundles
- **Retrieve MOA data (DG002 — High priority):** Query DrugBank API for full mechanism of action, pharmacodynamics, and pharmacokinetic parameters
- **Retrieve safety data (DG001 — Blocking):** Download and parse the FDA prescribing information or DrugBank safety profile to populate key warnings, contraindications, and drug-drug interactions
- **Assess SAHPRA registration pathway:** Determine whether a full registration application or Section 21 unregistered medicine authorisation is appropriate, based on clinical demand and evidence available
- **Re-run the Evidence Pack pipeline:** Once the above data gaps are resolved, regenerate the Evidence Pack (target version ≥ v5) to produce a complete repurposing evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

