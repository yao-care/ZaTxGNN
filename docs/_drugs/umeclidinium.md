---
layout: default
title: Umeclidinium
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Umeclidinium
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

# Umeclidinium: From an Inhaled Long-Acting Muscarinic Antagonist to Migraine Disorder

## One-Sentence Summary

Umeclidinium is an inhaled long-acting muscarinic antagonist (LAMA) and is registered in South Africa as a component of a triple-combination inhaler.
The TxGNN model predicts it may be relevant to **migraine disorder**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 96.4% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Umeclidinium is an inhaled LAMA with low systemic exposure. Muscarinic signalling has a speculative role in trigeminovascular and cortical processes, which is the only conceptual link to migraine.

There is no data showing that inhaled dosing reaches relevant central nervous system targets, so the link is weak. The prediction is best read as a knowledge-graph association, not a mechanism-backed hypothesis.

The other high-scoring predictions do not look stronger:
- **Migraine with brainstem aura (95.8%)** is likely a neighbour effect from the general migraine node.
- **Open-angle glaucoma (93.3%) and primary hereditary glaucoma (92.9%)** run in the opposite direction to the safety profile. Anticholinergics carry a labelled warning for worsening narrow-angle glaucoma.
- **Gastroduodenitis, peptic ulcer disease and common cold** have a conceptual antimuscarinic link, but inhaled dosing gives minimal systemic or nasal exposure.
- **Nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata and allergic urticaria** have no plausible muscarinic link and are probably graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The only article retrieved for any top-10 prediction is a COPD annual review (PMID [29583021](https://pubmed.ncbi.nlm.nih.gov/29583021/), 2018). It was retrieved for the common cold prediction and does not test umeclidinium in that condition.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 52/21.5.1/0177 | Trelegy Ellipta | Inhaler |

## Safety Considerations

- **Key Warnings**: Anticholinergics such as umeclidinium carry a labelled warning for worsening narrow-angle glaucoma. This needs resolving before any ocular research question is pursued.

For full safety information, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no supporting trials or literature. Inhaled dosing gives low systemic exposure, so it is not clear the drug reaches the sites relevant to migraine. Its mechanism-of-action and safety data are also incomplete.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data from DrugBank
- Evidence that inhaled umeclidinium reaches relevant CNS targets, or a route-compatibility assessment for any alternative delivery
- A migraine-specific mechanistic rationale, ideally with preclinical support
- A review of the glaucoma safety signal before any ocular indication is considered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

