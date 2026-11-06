---
layout: default
title: Citric Acid
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-06
monitor_inn: "Citric acid"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis"]
description: "Citric Acid: predicted new indication Stomach disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Citric Acid
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

## Citric Acid: Stomach disease
{: .text-alpha }

## One-Sentence Summary

Citric acid is a widely used organic acid with a single valid SAHPRA registration in South Africa.
The TxGNN model predicts it may be useful for **stomach disease**,
but **no clinical trials** and **no publications that test citric acid as a treatment for stomach disease** were found, so the prediction currently rests on the model alone (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 48 of 67) |
| Number of SAHPRA Registrations | 67 (valid: 48) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for citric acid, so the mechanism cannot be tied rigorously to stomach pathology.

Citric acid is an organic acid. The model's high score may reflect its similarity to other agents used for gastrointestinal complaints, but this has not been tested. The retrieved literature is indirect: a citric acid test meal used to improve the accuracy of the 13C-urea breath test for *H. pylori* is a diagnostic adjunct rather than a treatment, and other papers (gastric cancer metabolism, *H. pylori* physiology, dietary advice in ulcer disease) mention citric acid or related metabolism only in passing. The score of 0.9974 is a model output and not evidence of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publication tests citric acid as a treatment for stomach disease. The most relevant items found are listed below for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Diagnostic study (editorial-style commentary) | Gut and Liver | Discusses a citric acid meal to improve 13C-urea breath test accuracy; diagnostic use, not treatment |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | Clinical diagnostic | Gut and Liver | Effect of citric acid on 13C-urea breath test accuracy after *H. pylori* eradication in a region with common atrophic gastritis |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | Clinical physiology | Aliment Pharmacol Ther | Compares citric, malic and ascorbic acid effects on intragastric urease activity; mechanism of citric acid-enhanced *H. pylori* urease activity |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet and nutrition in peptic ulcer disease; no restrictive diet needed |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Physiology and metabolism of *H. pylori* |

---

## South Africa Market Information

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| A39/11.5/0058 | Picolax 16.1g | sachet | Valid |
| D/8.2/262 | Fenwal Acd Solution Usp Formula A (500 Ml) | solution | Valid |
| T1100 | Minamino | syrup | Valid |
| 54/18.3/0663 | Prazgen Otc | Not recorded | Valid |
| 27/18.3/0542 | CITROSOL* | talbet | Valid |

Showing 5 of 67 registrations (valid registrations first).

---

## Safety Considerations

- **Drug Interactions** (15 recorded, from a drug-interaction database):
  - **Major**: aluminium hydroxide.
  - **Moderate**: cinoxacin, ciprofloxacin, enoxacin, gatifloxacin, gemifloxacin, grepafloxacin, levofloxacin, lomefloxacin, moxifloxacin, nalidixic acid, norfloxacin, ofloxacin, sparfloxacin, trovafloxacin (quinolone antibacterials).

Product-specific warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication tests citric acid as a treatment for stomach disease, so the evidence level is L5. The high TxGNN score (0.9974) is a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data for citric acid
- Product safety information (warnings and contraindications) from the SAHPRA Professional Information
- Preclinical or clinical studies that directly test citric acid in stomach disease, with a clear therapeutic hypothesis

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

