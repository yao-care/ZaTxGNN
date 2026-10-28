---
layout: default
title: Desvenlafaxine
parent: Model Prediction Only (L5)
nav_order: 165
evidence_level: L5
indication_count: 8
monitor_inn: "DESVENLAFAXINE"
predicted_indications: ["obsessive-compulsive disorder", "paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
last_modified_at: 2026-10-29
description: "Desvenlafaxine: predicted new indication obsessive-compulsive disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Desvenlafaxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Desvenlafaxine: serotonin–norepinephrine reuptake inhibitor (SNRI) → obsessive-compulsive disorder
{: .text-alpha }

## One-Sentence Summary

Desvenlafaxine is a serotonin–norepinephrine reuptake inhibitor (SNRI) that is marketed in South Africa.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder**,
but **no clinical trials** and **3 publications** (none testing desvenlafaxine in this condition) are currently available, so the prediction rests mainly on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsessive-compulsive disorder |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on the drug class, desvenlafaxine is an SNRI, and blocking serotonin reuptake is the core mechanism of first-line pharmacotherapy for obsessive-compulsive disorder (OCD), namely SSRIs and clomipramine.

This gives a plausible but indirect link. The publications retrieved are a general review of serotonergic antidepressants in OCD, a review of postpartum depression, and a study of risperidone augmentation in somatic symptom disorder. None of them tests desvenlafaxine in OCD.

The very high TxGNN score (0.9991) is a computational output. It does not replace clinical data and should not be read as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Reviews double-blind studies of serotonergic antidepressants in OCD, confirming the central role of the serotonin system. Does not address desvenlafaxine specifically. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression; notes that mothers may later develop OCD and anxiety. Not about desvenlafaxine treatment. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Cohort | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder. Not about desvenlafaxine or OCD treatment. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/1.2/0505 | Deslafore Xr 50 | Tablet | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. Examples of interactions rated **Major** include bupropion, lorcaserin, dexfenfluramine, diethylpropion, dolasetron, fenfluramine, granisetron and mazindol. Several others are rated Moderate (e.g. epinephrine, morphine, acetylsalicylic acid, ephedrine, mannitol, dronabinol) and cimetidine is rated Minor. Many of the Major pairings involve other serotonergic or sympathomimetic agents, so serotonin syndrome and blood-pressure effects deserve attention.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high model score and a class-level mechanistic argument from other serotonergic antidepressants. No trial or publication directly studies desvenlafaxine in obsessive-compulsive disorder.

**To proceed, the following is needed:**
- Clinical evidence (trials or controlled studies) of desvenlafaxine in obsessive-compulsive disorder
- Detailed mechanism of action data
- SAHPRA Professional Information warnings and contraindications for a formal safety review
- Comparison with established first-line OCD treatments (SSRIs, clomipramine)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

