---
layout: default
title: Cupric Chloride
parent: Model Prediction Only (L5)
nav_order: 153
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-29
monitor_inn: "Cupric Chloride"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "thrombocytopenia due to immune destruction"]
description: "Cupric Chloride: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Cupric Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cupric Chloride: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Cupric chloride is a source of copper, an essential trace element, and is registered in South Africa as a single-ingredient infusion product (Addaven).
The TxGNN model predicts it may be relevant to **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

Two other predictions were also generated, both L5 and Hold: pseudo-von Willebrand disease (0.9925) and thrombocytopenia due to immune destruction (0.9902).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cupric chloride supplies copper, an essential trace element and cofactor for enzymes such as lysyl oxidase and ceruloplasmin. The original indication could not be confirmed from the registration record.

The review found **no established mechanistic link** between cupric chloride and platelet granule release or signalling defects. The high score (0.9929) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same applies to the other two predictions:
- **Pseudo-von Willebrand disease:** this condition arises from gain-of-function mutations in GP1BA that increase platelet GPIb-alpha affinity for von Willebrand factor (VWF). Copper has no known action on this interaction.
- **Immune thrombocytopenia:** this involves autoantibody-mediated platelet destruction. Copper deficiency can cause cytopenias (mainly anaemia and neutropenia, occasionally thrombocytopenia), but that is a nutritional deficiency effect, not immune-mediated destruction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 49/24/0996 | Addaven | Infusion | Not recorded in the data compiled for this report |

Addaven is a valid, single-ingredient injectable registration. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from label text): Wilson disease, iron metabolism disease, hereditary haemochromatosis. These are plausible given copper handling and metal-overload physiology, but must be verified against the product label.
- **Drug interactions:** no interactions were found in the queried database.

For full warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no literature and no plausible mechanism for any of the three predicted platelet or bleeding-related conditions. The label safety information and the original indication are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI), to confirm the approved indication, warnings and contraindications
- Mechanism of action data for cupric chloride
- A literature search for any link between copper status and platelet function or platelet disorders
- Evidence that a plausible mechanism exists before any clinical investigation is considered
- Review of the knowledge-graph contraindications (Wilson disease, iron metabolism disorders, haemochromatosis) against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

