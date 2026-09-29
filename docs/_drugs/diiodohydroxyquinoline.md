---
layout: default
title: Diiodohydroxyquinoline
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
---

# Diiodohydroxyquinoline
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

# Diiodohydroxyquinoline: From Anti-amoebic Use to Osteoradionecrosis

## One-Sentence Summary

Diiodohydroxyquinoline is a halogenated hydroxyquinoline, historically used as an anti-amoebic agent. The TxGNN model predicts it may be effective for **osteoradionecrosis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model prediction only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data (anti-amoebic agent) |
| Predicted New Indication | Osteoradionecrosis |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Diiodohydroxyquinoline is an anti-amoebic agent, and its use in amoebiasis is described in older clinical literature. No plausible mechanistic link to osteoradionecrosis can be stated from the available data.

The model score is high, but it reflects the drug's position in a knowledge graph, not proof of a biological effect. Osteoradionecrosis is a late radiation injury of bone, and the link to an anti-amoebic drug is unexplained. The registered South African product is a topical cream, and route compatibility with this predicted condition has not been assessed.

**Other predictions in the pack** (all Hold):

| Rank | Predicted Indication | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Radiodermatitis | 96.29% | L5 |
| 3 | Pneumonitis | 95.65% | L4 |
| 4 | Aspiration pneumonia | 90.99% | L5 |
| 5 | Type 2 diabetic nephropathy | 90.57% | L5 |
| 6 | Byssinosis | 88.17% | L5 |
| 7 | Mitochondrial oxidative phosphorylation disorder (nuclear DNA anomalies) | 87.30% | L5 |
| 8 | Mixed mineral dust pneumoconiosis | 82.82% | L5 |
| 9 | Baritosis | 82.67% | L5 |
| 10 | Slate pneumoconiosis | 82.67% | L5 |

Baritosis and slate pneumoconiosis have identical scores. This suggests a shared graph-neighbourhood artefact, not two independent signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

No SANCTR or PACTR entries were provided.

---

## Literature Evidence

Currently no related literature available for osteoradionecrosis.

For the rank 3 prediction (pneumonitis), the only relevant item is an in vitro study. The other three citations retrieved are historical amoebiasis or cytomegalovirus (CMV) case reports and do not support that indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32473310](https://pubmed.ncbi.nlm.nih.gov/32473310/) | 2020 | In vitro screening | Pharmacological Research | Identified diiodohydroxyquinoline as a potential anti-SARS-CoV-2 agent in a two-tier drug screen. This is indirect preclinical evidence for viral pneumonia, not for radiation pneumonitis. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. G1781 (Act 101) | Viocort | Cream | Not listed in the available data |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Halogenated hydroxyquinolines carry a known neurotoxicity signal (subacute myelo-optic neuropathy, SMON). This needs review before any repurposing, especially for predictions involving neurologically vulnerable populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions rest on model scores alone. For osteoradionecrosis there are no trials or publications, and the mechanism of action and SAHPRA safety data are missing. The safety review cannot begin without the package insert.

**To proceed, the following is needed:**
- SAHPRA package insert for Viocort (warnings, contraindications, approved indication). This is a blocking gap.
- Mechanism of action data from DrugBank
- A targeted literature search for osteoradionecrosis and radiodermatitis, followed by a review of the neurotoxicity signal
- An assessment of route compatibility between the topical cream and the predicted conditions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

