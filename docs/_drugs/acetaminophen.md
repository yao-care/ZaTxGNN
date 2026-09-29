---
layout: default
title: Acetaminophen
parent: Model Prediction Only (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Acetaminophen
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

# Acetaminophen: From Pain and Fever to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is a widely marketed analgesic and antipyretic. It is also already used for acute migraine in general.
The TxGNN model predicts it may be useful for **migraine with brainstem aura**, but there are **0 clinical trials** and **20 publications** on this subtype, and all of the publications concern migraine or headache in general.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain and fever (general analgesic/antipyretic use; the SAHPRA indication text was not supplied) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (indirect evidence from general migraine; nothing specific to this subtype) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available. Acetaminophen is thought to act centrally through COX inhibition, with serotonergic and endocannabinoid modulation of descending pain pathways. This is the mechanistic basis for its use in acute migraine.

The retrieved literature supports migraine in general. It includes the American Headache Society evidence assessment of acute migraine treatments and several pregnancy-related reviews. None of the retrieved records address the brainstem-aura subtype specifically.

The link is therefore indirect, an extrapolation from general migraine. It is not a novel repurposing signal, because acetaminophen is already used for migraine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT (per title) | Arch Intern Med | Randomized, double-blind, placebo-controlled, population-based study of acetaminophen efficacy and safety in migraine. Results are not in the supplied abstract. |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (per title) | Arch Neurol | Three double-blind, placebo-controlled trials of acetaminophen, aspirin and caffeine for migraine pain. Results are not in the supplied abstract. |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Retrospective analysis of 3 RCTs | Clin Ther | Acetaminophen, aspirin and caffeine combination in menstruation-associated versus non-menstrual migraine. |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative study | Headache | An isometheptene, dichloralphenazone and acetaminophen combination compared with sumatriptan in mild-to-moderate migraine, with or without aura. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society update of the evidence for acute migraine pharmacotherapies in adults. |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurol Clin | Headache in pregnancy. Acetaminophen is described as first-line symptomatic treatment. |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and prophylactic migraine therapies in pregnancy. |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine in pregnancy and breastfeeding, with a treatment approach. |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus, a complication of migraine with or without aura. |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurol Int | Ubrogepant for acute migraine. Notes acetaminophen among non-prescription options for mild to moderate attacks. |

## South Africa Market Information

Twenty registrations are on file. The five main ones are shown below. Manufacturer, approved indication text and Essential Medicines List (EML) status were not supplied.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. X/2.8/64 | Antalgic Sf | Syrup | Not stated in supplied data |
| Reg. No. 45/2.9/0303 | Tramazac co 37.5mg/325mg | Tablet | Not stated in supplied data |
| Reg. No. 37/5.8/0138 | Sinutab sinus pain non-drowsy | Tablet | Not stated in supplied data |
| Reg. No. 27/2.7/0352 | Dynadol | Tablet | Not stated in supplied data |
| Reg. No. A39/5.8/0451 | Efferflu-c | Effervescent tablet | Not stated in supplied data |

Other registered forms include capsules, infusion and suspension.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no registered trials and no literature specific to migraine with brainstem aura. The high model score reflects the general link between acetaminophen and migraine, which is already established practice, so this is not a distinct new-indication finding. Other predicted indications in this pack have more direct evidence. Sciatic neuropathy has two Phase 4 randomized emergency department trials of IV paracetamol (NCT02504996 and NCT02777320). Fibromyalgia has a tramadol/acetaminophen RCT in which the acetaminophen contribution cannot be separated.

**To proceed, the following is needed:**
- Subtype-specific evidence, such as trials or case series in migraine with brainstem aura
- SAHPRA Professional Information (PI) safety data, currently a blocking gap
- Mechanism of action data from DrugBank
- The approved indication text for the South African registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

