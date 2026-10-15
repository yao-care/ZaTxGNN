---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From Depression and Anxiety Disorders to Schizoid Personality Disorder

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI), originally used for depressive and anxiety-spectrum conditions such as major depressive disorder, obsessive-compulsive disorder and bulimia nervosa.
The TxGNN model predicts it may be effective for **schizoid personality disorder**, but there are **0 registered clinical trials** and only **2 loosely related publications** (one review and one indirect cohort study) behind this prediction. It is a computational signal, not yet a clinical one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depressive and anxiety-spectrum disorders, including major depressive disorder, obsessive-compulsive disorder and bulimia nervosa (from the knowledge-graph indication list; the SAHPRA records compiled for this report contain no indication text) |
| Predicted New Indication | Schizoid personality disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fluoxetine is an SSRI. It raises serotonergic tone, and its efficacy in depression, anxiety and obsessive-compulsive disorder is well established.

Schizoid personality disorder belongs to the cluster A personality disorders, which are marked by social detachment and restricted emotional expression. A serotonergic drug could plausibly help affective or anxiety features that often accompany these conditions. However, **no schizoid-specific mechanism has been established**.

The very high TxGNN score (rank 690 overall) most likely reflects network proximity to related personality and mood disorders in the knowledge graph. It does not reflect direct evidence that fluoxetine treats the core features of schizoid personality disorder. Any real benefit would probably come from treating comorbid depression or anxiety rather than the personality disorder itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews pharmacological treatment of cluster A personality disorders (paranoid, schizoid, schizotypal), which are characterised by social isolation and reduced quality of life. It does not provide fluoxetine-specific efficacy data for schizoid personality disorder in the excerpt available. |
| [16390895](https://pubmed.ncbi.nlm.nih.gov/16390895/) | 2006 | Cohort | American Journal of Psychiatry | Follow-up of depressed patients over 6 months of treatment, looking at course of illness and its predictors. This is indirect evidence, as it concerns depression rather than schizoid personality disorder. |

---

## South Africa Market Information

Fluoxetine is marketed in South Africa as single-ingredient oral capsules. No approved indication text was available in the registration records compiled for this report.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 34/1.2/0279 | Rezak | Capsule |
| Reg. No. 30/1.2/0356 | Fluoxetine Biotech 20 | Capsule |
| Reg. No. 37/1.2/0612 | Trizac 20 Mg | Capsule |

All three registrations are valid, and none are cancelled.

---

## Safety Considerations

The SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

The following supplementary signals are available:

- **Knowledge-graph contraindication signals** (disease-level associations from the knowledge graph, not label text): bipolar disorder and other major affective disorders, epilepsy, liver disease and liver failure, cirrhosis, orthostatic hypotension, neutropenia and agranulocytosis, blood coagulation disorders, diabetes (including diabetic ketoacidosis) and hyperglycaemia, benign prostatic hyperplasia, hyperlipidaemia and hypertriglyceridaemia, stroke and cerebrovascular disease, myocardial infarction, and gallbladder disease. These should be checked against the PI before any use.
- **Drug interactions:** 100 interactions were identified, and 20 were available for review. Those rated **Major** are bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and cisapride. Several Moderate interactions were also listed, including aspirin, morphine, clarithromycin, famotidine, loperamide, and sulfonylureas (chlorpropamide, acetohexamide).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (evidence level L5). There are no registered trials, no schizoid-specific mechanism, and only two indirect publications. Fluoxetine is widely available in South Africa, but nothing yet supports using it for this condition.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer mechanistic link to schizoid personality features
- Fluoxetine-specific clinical studies in schizoid personality disorder, or in cluster A disorders with clear outcome measures
- The SAHPRA PI warnings and contraindications, to complete safety screening
- Review of the Major drug interactions and the knowledge-graph contraindication signals, particularly bipolar disorder, epilepsy and liver disease

**Note on other predictions:** The data compiled for this report also contain candidates with stronger support than this one. These include **phobic disorder** (L2, including a completed Phase 3 trial in childhood social phobia, NCT00043537, whose fluoxetine arm is not confirmed), **melancholia** (L2, largely an extension of the existing depression indication), and **agoraphobia** (L3, with SSRI evidence in panic disorder). These may be better priorities for evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

