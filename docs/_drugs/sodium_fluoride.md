---
layout: default
title: Sodium Fluoride
parent: Model Prediction Only (L5)
nav_order: 424
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Sodium Fluoride: predicted new indication Epiglottitis (evidence level L5). Approved use: Vitamin deficiency disorder"
---

# Sodium Fluoride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sodium Fluoride: From Vitamin Deficiency Disorder to Epiglottitis

## One-Sentence Summary

Sodium fluoride is registered in South Africa mainly as a trace-element component of multi-ingredient nutritional products. Its original indication in the knowledge graph is vitamin deficiency disorder.
The TxGNN model predicts it may be effective for **epiglottitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder (from the knowledge graph; no approved indication text is available in the SAHPRA registrations) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium fluoride is used as a trace-element and mineral supplement ingredient, and its original indication is vitamin deficiency disorder. No mechanistic link to epiglottitis has been established.

Epiglottitis is an acute, potentially life-threatening bacterial infection of the epiglottis. It is treated with antibiotics and airway management. There is no documented antimicrobial or anti-inflammatory role for fluoride at safe doses in this condition.

The TxGNN score is very high, but it reflects patterns in the knowledge graph rather than drug-specific evidence. The other top predictions are also infections or inflammatory conditions of the urogenital and respiratory tracts (urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis and laryngitis). None has clinical trial or supporting literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications support epiglottitis. For the seventh-ranked prediction, laryngitis, four publications were retrieved. None shows therapeutic efficacy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29245332](https://pubmed.ncbi.nlm.nih.gov/29245332/) | 2017 | Case report | Medicine | Elevated 18F-NaF uptake in the cricoid cartilage of a patient with laryngeal carcinoma; diagnostic imaging, not treatment |
| [42721223](https://pubmed.ncbi.nlm.nih.gov/42721223/) | 2026 | Imaging methodology | Cartilage | [18F]NaF and [18F]FDG PET/CT used to assess calcification and glucose metabolism of thyroid cartilage with age |
| [24178785](https://pubmed.ncbi.nlm.nih.gov/24178785/) | 2013 | Animal toxicity study | Biol Trace Elem Res | High dietary fluorine suppressed intestinal development in broilers (a toxicity finding) |
| [235491](https://pubmed.ncbi.nlm.nih.gov/235491/) | 1975 | In vitro | Infect Immun | Ammonium chloride protected cultured cells from diphtheria toxin; not about fluoride therapy |

## South Africa Market Information

All nine registrations are single-ingredient entries with valid status. No approved indication text is available for any of them. Essential Medicines List (EML) status was not part of the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 29/24/0462 | Peditrace 10ml pdp100010 | Infusion | Not available |
| 49/24/0996 | Addaven | Infusion | Not available |
| 52/24/0031 | Nutryelt | Infusion | Not available |
| H2466 | Complenatal Ff | Capsule | Not available |
| 41/10.2.1/0849 | Spiriva respimat inhaler 60 doses | Inhaler | Not available |

Four further registrations are not listed above: ITN 1606n 150ml and ITN 55a 600ml (TPN), Gericomplex (capsule) and Filibon (capsule).

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text):** kidney disease, pyoureter, sarcoidosis, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, nephrolithiasis (including the SLC26A1-related form), acute urate nephropathy, constipation disorder, lytic metastatic bone lesion and dental fluorosis.
- **Drug interactions:** No interaction data were found.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials and no supporting literature. No plausible mechanism links fluoride to epiglottitis, and effective standard-of-care treatment already exists. Safety information from the PI is also missing.

**To proceed, the following is needed:**
- Mechanism of action data for sodium fluoride (e.g. from DrugBank)
- SAHPRA package insert warnings and contraindications, which block safety screening
- A mechanistic rationale and preclinical evidence for the predicted indication
- Route compatibility assessment (not yet evaluated)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

