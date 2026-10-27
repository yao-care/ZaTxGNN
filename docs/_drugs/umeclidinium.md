---
layout: default
title: Umeclidinium
parent: Model Prediction Only (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Umeclidinium: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the registration data compiled for this report"
monitor_inn: "Umeclidinium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "open-angle glaucoma", "primary hereditary glaucoma", "nephrogenic syndrome of inappropriate antidiuresis", "gastroduodenitis", "common cold", "atrophoderma vermiculata", "peptic ulcer disease", "allergic urticaria"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Umeclidinium: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Umeclidinium is an inhaled long-acting muscarinic antagonist (LAMA). In South Africa it is registered only as part of the Trelegy Ellipta inhaler, and the registration text compiled for this report does not state an approved indication.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no relevant publications** support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 96.36% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Umeclidinium is a well-known inhaled muscarinic antagonist (LAMA), a class used in chronic obstructive pulmonary disease (COPD). In Trelegy Ellipta it is combined with other agents. This background comes from general pharmacological knowledge, not from the data compiled here.

A link to migraine would be speculative. The only conceivable route is cholinergic modulation of trigeminovascular or central pain pathways. Inhaled delivery gives low systemic exposure, which weakens any plausible central effect. The high score is likely a model-based association, not a demonstrated therapeutic relationship.

The same applies to the other predictions. Migraine with brainstem aura (95.83%) is a rare subtype that probably inherits its score from the parent migraine node. Peptic ulcer disease and gastroduodenitis have class-level plausibility for antimuscarinics, but inhaled doses give minimal gastric exposure. The glaucoma predictions (open-angle glaucoma 93.28%, primary hereditary glaucoma 92.91%) run opposite to known pharmacology, because anticholinergics are cautioned in glaucoma and may raise intraocular pressure. Nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata and allergic urticaria have no plausible muscarinic mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (migraine disorder), currently no related literature is available.

The only publication linked to any of the top 10 predictions concerns the common cold (rank 7). It is a general COPD review, not evidence for use in the common cold:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29583021](https://pubmed.ncbi.nlm.nih.gov/29583021/) | 2018 | Review | COPD | "COPD 2017: A Year in Review". Covers COPD treatment studies, including fluticasone furoate/vilanterol/umeclidinium in severe patients. It does not address migraine or the common cold. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/21.5.1/0177 | Trelegy Ellipta | Inhaler | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

**Drug Interactions:** The interaction screening found 100 potential interactions. The 20 listed in the data compiled for this report are all rated Moderate. They are mostly other anticholinergic or antimuscarinic agents, where additive effects are the concern:

- **Antimuscarinics/anticholinergics:** hyoscyamine, atropine, glycopyrronium (including topical), clidinium, dicyclomine, trospium, mepenzolate, methscopolamine, propantheline, scopolamine, aclidinium
- **Anticholinergic antihistamines:** promethazine, chlorpheniramine, acrivastine
- **Others:** eluxadoline, prucalopride, acetylcholine, ophthalmic physostigmine, inhaled human insulin (rapid acting)

**Additional caution (glaucoma):** The glaucoma predictions are mechanistically contradictory. Anticholinergics are generally cautioned in glaucoma, particularly angle-closure, so any consideration of those indications should begin with a safety review.

Warnings and contraindications from the product label are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no trials or relevant publications, and the mechanistic link to migraine is speculative, particularly with inhaled delivery and low systemic exposure. The drug's registration, safety label data and mechanism data are also incomplete.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI), covering approved indication, warnings and contraindications. This is a blocking gap for safety screening.
- Detailed mechanism of action data (for example from DrugBank).
- A mechanistic rationale, ideally preclinical, showing how muscarinic antagonism could affect migraine pathways.
- Assessment of whether the inhaled route can reach relevant targets, since route compatibility is still pending.
- A targeted literature search for muscarinic antagonists in migraine, followed by early-phase clinical evidence if the rationale holds.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

