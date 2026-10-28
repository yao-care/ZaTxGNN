---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 8
monitor_inn: "SERTRALINE"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "benign paroxysmal torticollis of infancy", "agoraphobia", "dependent personality disorder", "narcissistic personality disorder"]
last_modified_at: 2026-10-29
description: "Sertraline: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Anxiety disorder, post-traumatic stress disorder, social phobia…"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Sertraline: From Anxiety Disorders to Paranoid Personality Disorder
{: .text-alpha }

## One-Sentence Summary

Sertraline is a selective serotonin reuptake inhibitor (SSRI).
The TxGNN model predicts it may be effective for **paranoid personality disorder**, but there are **no clinical trials** and **no publications that directly study this disease**. The prediction therefore rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, post-traumatic stress disorder, social phobia, obsessive-compulsive disorder, dysthymic disorder (relations recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 4 of 4) |
| Number of SAHPRA Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sertraline is an SSRI. Its use in anxiety and mood-related conditions is recorded in the knowledge graph, and mechanistically it may influence impulsivity, affective instability and comorbid depression or anxiety.

The retrieved literature does not study paranoid personality disorder itself. It covers borderline personality disorder, personality-disorder comorbidity in depression treated with sertraline, and an aripiprazole add-on study in sertraline-resistant borderline personality disorder. These link sertraline to other conditions, not to paranoid traits.

The identical score (0.9993) given to several personality disorders (schizotypal, histrionic, schizoid) suggests a shared, class-level signal in the model rather than biology specific to paranoid personality disorder.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for paranoid personality disorder.

---

## Literature Evidence

None of these studies addresses paranoid personality disorder directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9817625](https://pubmed.ncbi.nlm.nih.gov/9817625/) | 1998 | RCT (secondary analysis) | Int Clin Psychopharmacol | 308 depressed primary-care patients treated with sertraline or citalopram; examined personality disorder frequency and change with treatment (not paranoid-specific) |
| [18848360](https://pubmed.ncbi.nlm.nih.gov/18848360/) | 2008 | Clinical trial | Psychiatry Res | Aripiprazole add-on in 21 sertraline-resistant patients with borderline personality disorder |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | Review of borderline personality disorder |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encephale | Psychiatric adverse effects of alpha-interferon; low relevance |

---

## South Africa Market Information

All four registrations are single-ingredient oral tablets. No approved indication text is available in the data compiled for this report, and Essential Medicines List status is not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36/1.2/0273 | Serlife | Tablet | Not available |
| 36/1.2/0274 | Tralidep | Tablet | Not available |
| A39/1.2/0308 | Sertra | Tablet | Not available |
| A40/1.2/0654 | Aurolift 50Mg | Tablet | Not available |

---

## Safety Considerations

**Contraindication-type relations in the knowledge graph** (these come from the knowledge graph, not from label text): epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.

**Drug Interactions**: 100 interactions were found. Examples rated **Major**: bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron, phentermine. Examples rated **Moderate**: acetylsalicylic acid, morphine, clarithromycin, famotidine, loperamide, and the sulfonylureas chlorpropamide and glimepiride.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies sertraline in paranoid personality disorder, so the evidence level is L5 and support is limited to a computational score shared across several personality disorders.

**To proceed, the following is needed:**
- Studies that directly address sertraline in paranoid personality disorder
- Mechanism of action data
- SAHPRA Professional Information, covering approved indications, warnings and contraindications
- A review of whether the knowledge-graph contraindications (e.g. bipolar disorder, serotonin syndrome) apply to this population

---

### Note on other predicted indications

Agoraphobia is the only other prediction with substantial evidence. It is supported by randomised trials and network meta-analyses in panic disorder with or without agoraphobia. It overlaps with existing anxiety-disorder uses, so it is better handled as a label clarification question than as new repurposing. It was not assessed as the primary indication in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

