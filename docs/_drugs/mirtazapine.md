---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Mirtazapine: predicted new indication Ohdo syndrome and variants (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "MIRTAZAPINE"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is an antidepressant, originally used for unipolar depression, major depressive disorder and anxiety disorder.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (from the knowledge graph; the SAHPRA registration records contain no indication text) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Mirtazapine is generally known as a noradrenergic and specific serotonergic antidepressant, but this is background knowledge and not part of the supplied record.

Ohdo syndrome is a rare genetic neurodevelopmental disorder (KAT6B-related). The data compiled for this report supports no mechanistic link between mirtazapine and this condition. The high score (0.994) probably reflects proximity in the knowledge graph, for example through shared symptoms or genes, rather than a true therapeutic relationship.

Two other predictions deserve mention because they are related or overlapping:
- **Blepharophimosis - intellectual disability syndrome, Ohdo type** (score 99.11%) is closely related to, and likely overlaps with, the first prediction. The two are probably not independent. There are no trials or publications. Any symptomatic benefit (for mood, sleep or appetite) cannot be assessed from the available data, and there is no evidence that mirtazapine modifies the underlying genetic disorder.
- **Benign paroxysmal torticollis of infancy** (score 99.11%) is a self-limiting episodic disorder of infancy, often linked to CACNA1A variants and considered a migraine equivalent. Any rationale would be speculative. Because it usually resolves on its own and affects infants, the benefit-risk of an antidepressant would need careful justification, including the boxed warnings for antidepressants in young patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/1.2/1005 | Mirtaneo 15 | Tablet | Not available in the compiled data |
| Reg. No. 41/1.2/0529 | Ramure 15Mg | Tablet | Not available in the compiled data |

Both registrations are valid single-ingredient oral tablets. Essential Medicines List (EML) status is not available in the compiled data.

---

## Safety Considerations

- **Drug Interactions**: The interaction query found 100 interactions in total. The main ones are listed below (DDInter classification, first 20 returned).
  - **Major**: bupropion, lorcaserin, dolasetron, palonosetron
  - **Moderate**: famotidine, cimetidine, loperamide, aprepitant, morphine, dexamethasone, bisacodyl, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), dronabinol, eliglustat, obeticholic acid, sodium sulfate, nabilone, levofloxacin
- **Knowledge-graph contraindication signals** (from disease-drug links, not label text):
  - Neurological and psychiatric: epilepsy, manic bipolar affective disorder, serotonin syndrome, drug-induced akathisia, multiple system atrophy
  - Cardiovascular: orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis
  - Haematological: neutropenia, agranulocytosis, hemoglobinopathy
  - Metabolic and organ: liver disease, gallbladder disease, impaired renal function, hypertriglyceridemia, obesity disorders

The label warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no publications and no supported mechanistic link (evidence level L5). The three predicted conditions are rare or paediatric, and the paediatric safety profile of an antidepressant would need careful justification.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank to assess a mechanistic link
- A systematic literature search for mirtazapine in Ohdo syndrome and related neurodevelopmental disorders
- Evidence of whether any symptomatic benefit (mood, sleep, appetite) is plausible in this population
- A paediatric safety and benefit-risk assessment before considering benign paroxysmal torticollis of infancy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

