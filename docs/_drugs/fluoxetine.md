---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 235
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

# Fluoxetine: From Serotonin Reuptake Inhibitor Use to Schizoid Personality Disorder

## One-Sentence Summary

Fluoxetine is a serotonin reuptake inhibitor, marketed in South Africa as oral capsules; the SAHPRA records supplied do not state its approved indication text.
The TxGNN model predicts it may be effective for **schizoid personality disorder**, but only **3 publications** and **0 clinical trials** relate to this prediction.
None of the publications tests fluoxetine in this disorder, so the evidence is weak and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA licence records supplied |
| Predicted New Indication | Schizoid personality disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (indirect literature only; no disorder-specific efficacy data) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluoxetine is a serotonin reuptake inhibitor. Detailed mechanism of action data is not available in the record. The link to schizoid personality disorder is indirect. Serotonergic modulation might ease affective flattening and social withdrawal, which are features of this disorder.

The only supporting paper that addresses the disorder is a review of drug treatment in cluster A personality disorders (paranoid, schizoid and schizotypal). It gives general context rather than evidence that fluoxetine works here.

The model gives the same score (99.92%) to the schizoid, schizotypal, paranoid and histrionic personality disorders. This suggests the signal comes from a shared parent category in the knowledge graph rather than from anything specific to schizoid personality disorder. The prediction should therefore be treated as a hypothesis, not a finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews drug treatment across cluster A personality disorders, which are marked by isolation and avoidance of relationships. This is the only paper directly relevant to the disorder, and it gives indirect support at most. |
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort | Comprehensive Psychiatry | Assessed personality traits and disorders in 148 people with body dysmorphic disorder. Schizoid traits are discussed; the treatment study involved fluvoxamine, not fluoxetine. |
| [16390895](https://pubmed.ncbi.nlm.nih.gov/16390895/) | 2006 | Cohort | American Journal of Psychiatry | Course of illness and predictors of outcome in depressed patients over 6 months of treatment. It does not address schizoid personality disorder. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/1.2/0279 | Rezak | Capsule | Not provided in the registration record |
| Reg. No. 30/1.2/0356 | Fluoxetine Biotech 20 | Capsule | Not provided in the registration record |
| Reg. No. 37/1.2/0612 | Trizac 20 Mg | Capsule | Not provided in the registration record |

All three registrations are oral capsules.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no fluoxetine-specific efficacy data for schizoid personality disorder. The high model score appears to be shared across the cluster A disorders. The prediction remains a hypothesis and cannot support a repurposing decision at this stage.

**To proceed, the following is needed:**
- Controlled studies of fluoxetine specifically in schizoid personality disorder
- The SAHPRA package insert warnings and contraindications for the three registered products, which are needed before any safety screening
- Mechanism of action data, for example from DrugBank
- The approved indication text for each SAHPRA registration, to separate on-label from off-label use

**Other candidates in the same Evidence Pack:**
The pack also holds better-supported predictions for schizotypal personality disorder (L3, small uncontrolled studies), agoraphobia, manic bipolar affective disorder (bipolar depression evidence only), phobic disorder and melancholia. The last four are at L2 with guardrails. Any of these would be a stronger starting point than schizoid personality disorder.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

