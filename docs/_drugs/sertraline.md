---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Sertraline: predicted new indication Histrionic personality disorder (evidence level L5). Approved use: Anxiety disorder, obsessive-compulsive disorder…"
monitor_inn: "SERTRALINE"
predicted_indications: ["histrionic personality disorder (disease)", "paranoid personality disorder", "schizoid personality disorder", "schizotypal personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "dependent personality disorder", "narcissistic personality disorder"]
---

# Sertraline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Sertraline: From Anxiety Disorder to Histrionic Personality Disorder

## One-Sentence Summary

Sertraline is an antidepressant of the SSRI class. Its original indications include anxiety disorder, obsessive-compulsive disorder, post-traumatic stress disorder and social phobia.
The TxGNN model predicts it may be effective for **histrionic personality disorder**, with a very high model score.
However, **no clinical trials and no publications** were found for this specific prediction, so it rests on the model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, obsessive-compulsive disorder, post-traumatic stress disorder, social phobia, dysthymic disorder (from the knowledge graph; SAHPRA indication text was not available) |
| Predicted New Indication | Histrionic personality disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sertraline is a selective serotonin reuptake inhibitor (SSRI). Its efficacy in anxiety and obsessive-compulsive disorders is established. Mechanistically, it may modulate emotional dysregulation and anxiety symptoms that occur alongside some personality disorders.

The original indications (anxiety, OCD, PTSD, social phobia) are mood and anxiety conditions. Histrionic personality disorder is a personality disorder, which is a different kind of condition. The prediction may reflect shared symptom features such as affective instability, but the data compiled for this report do not show a direct mechanistic link. Treating this as a drug-for-personality-disorder claim would go beyond the evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for histrionic personality disorder.

---

## Literature Evidence

Currently no related literature available for histrionic personality disorder.

---

## South Africa Market Information

All four registrations are valid single-ingredient oral tablets. Approved indication text was not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A40/1.2/0654 | Aurolift 50Mg | Tablet | — |
| A39/1.2/0308 | Sertra | Tablet | — |
| 36/1.2/0274 | Tralidep | Tablet | — |
| 36/1.2/0273 | Serlife | Tablet | — |

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for these. Report adverse drug reactions to SAHPRA.

- **Contraindication-related conditions (knowledge graph, not label text)**: epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug interactions**: The interaction screen returned 100 entries. Those rated **Major** among the first 20 reviewed are:
  - bupropion
  - lorcaserin
  - diethylpropion
  - dolasetron
  - eliglustat
  - palonosetron
  - phentermine

  Moderate interactions include aspirin, morphine, clarithromycin, famotidine, loperamide, and several sulfonylureas and insulin (glimepiride, chlorpropamide, insulin aspart).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for histrionic personality disorder has a high model score but no supporting trials or publications (L5). Sertraline is marketed in South Africa, but there is no evidence of benefit for this specific condition.

**To proceed, the following is needed:**
- Disorder-specific clinical or observational evidence for sertraline in histrionic personality disorder
- Mechanism of action data to assess whether a plausible link exists
- SAHPRA Professional Information, to complete safety screening (warnings, contraindications)

**Other predicted indications from the same analysis:**
- **Agoraphobia** has by far the strongest support (L1). Evidence includes randomised trials and network meta-analyses of SSRIs, including sertraline, in panic disorder with or without agoraphobia. This is an extension within the anxiety-disorder class, and the evidence is specific to panic disorder rather than agoraphobia alone. It is the most actionable candidate and could be assessed as Proceed with Guardrails.
- **Schizotypal personality disorder** has only one very small trial (n=8, completed), so it is hypothesis-generating at most.
- **Paranoid, schizoid, dependent and narcissistic personality disorders** have only indirect or irrelevant literature and remain on Hold.
- **Benign paroxysmal torticollis of infancy** has no evidence, and SSRI use in infants raises additional safety concerns.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

