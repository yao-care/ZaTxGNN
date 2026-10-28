---
layout: default
title: Fluoxetine
parent: Model Prediction Only (L5)
nav_order: 236
evidence_level: L5
indication_count: 9
monitor_inn: "FLUOXETINE"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia", "manic bipolar affective disorder", "phobic disorder", "Ohdo syndrome and variants"]
last_modified_at: 2026-10-23
description: "Fluoxetine: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Not stated in the local licence records. The prediction comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence."
---

# Fluoxetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Fluoxetine: From Depressive and Anxiety Disorders to Paranoid Personality Disorder
{: .text-alpha }

## One-Sentence Summary

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI). It is linked to anxiety disorder, depression, bipolar disorder, bulimia nervosa and obsessive-compulsive disorder.
The TxGNN model's top-ranked prediction is **paranoid personality disorder**, but there are **no clinical trials** and no study that directly examines fluoxetine for this condition.
Stronger evidence exists for other predicted uses, notably **phobic disorder** (a completed Phase 3 trial) and **agoraphobia** (panic disorder studies), and these are described below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local licence records. The knowledge graph records anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, unipolar depression, major depressive disorder, bulimia nervosa and obsessive-compulsive disorder (relations recorded in the knowledge graph, not label-approved indications) |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 3 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

**Evidence level note:** None of the retrieved publications directly studies fluoxetine in paranoid personality disorder. They concern borderline personality disorder, depression with personality disorders, and cluster A pharmacotherapy in general. The evidence level is therefore capped at L5.

**Other predictions in the data compiled for this report**

| Predicted Indication | TxGNN Score | Direct Evidence | Suggested Stance |
|------|------|------|------|
| Phobic disorder | 0.9963 | 1 completed Phase 3 trial (childhood social phobia, NCT00043537) and a placebo-controlled trial publication of fluoxetine in generalised social phobia (PMID 15466674) | Proceed with Guardrails |
| Manic bipolar affective disorder | 0.9964 | Phase 4 trial in bipolar depression relapse prevention; evidence concerns the depressive phase, not mania | Proceed with Guardrails (depressive phase only, with a mood stabiliser) |
| Agoraphobia | 0.9986 | Panic disorder studies (indirect) | Research question |
| Schizotypal personality disorder | 0.9992 | Small uncontrolled studies | Research question |
| Schizoid, histrionic, benign paroxysmal torticollis of infancy, Ohdo syndrome | 99.89–0.9992 | No relevant evidence | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fluoxetine is an SSRI. Serotonergic modulation is established in depression, anxiety and obsessive-compulsive disorder, so it could plausibly help comorbid anxiety, depressive or irritable symptoms in people with cluster A personality disorders.

There is no evidence that fluoxetine improves the core features of paranoid personality disorder, such as pervasive suspiciousness. The very high TxGNN score most likely reflects network proximity to related psychiatric conditions rather than disease-specific evidence. Identical scores were given to schizotypal, schizoid and histrionic personality disorders, which supports this interpretation.

---

## Clinical Trial Evidence

For paranoid personality disorder: currently no related clinical trials registered.

Trials found for other predicted indications:

| Trial Number | Indication | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT00043537](https://clinicaltrials.gov/study/NCT00043537) | Phobic disorder | Phase 3 | Completed | 139 | Compares behavioural treatment, fluoxetine and placebo for childhood social phobia over four years |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | Phobic disorder | N/A | Unknown | 8800 | Individual patient data meta-analysis of antidepressant efficacy in anxiety disorders by initial severity; not fluoxetine-specific |
| [NCT00961961](https://clinicaltrials.gov/study/NCT00961961) | Manic bipolar affective disorder | Phase 4 | Completed | 177 | Antidepressant plus mood stabiliser versus mood stabiliser alone for preventing relapse of bipolar depression |

---

## Literature Evidence

Publications most relevant to paranoid personality disorder (none directly tests fluoxetine for this condition):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | Reviews drug treatment in cluster A personality disorders (paranoid, schizoid, schizotypal) |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | Review of borderline personality disorder, a different condition |
| [12524634](https://pubmed.ncbi.nlm.nih.gov/12524634/) | 2003 | Cohort | Comprehensive Psychiatry | Depressed patients in a fluoxetine/nortriptyline trial, with and without borderline personality disorder |
| [12214786](https://pubmed.ncbi.nlm.nih.gov/12214786/) | 2002 | Review | Psychological Medicine | Personality disorder diagnoses before and after fluoxetine treatment in depressed outpatients |

Publications for other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15466674](https://pubmed.ncbi.nlm.nih.gov/15466674/) | 2004 | Controlled trial | Archives of General Psychiatry | Fluoxetine, cognitive behavioural therapy and placebo in generalised social phobia |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network meta-analysis | Cochrane Database of Systematic Reviews | Drug treatments for panic disorder in adults |
| [10362436](https://pubmed.ncbi.nlm.nih.gov/10362436/) | 1999 | RCT | J Clin Psychiatry | Once-weekly fluoxetine for maintaining remission in panic disorder |
| [1853957](https://pubmed.ncbi.nlm.nih.gov/1853957/) | 1991 | Open-label study | Am J Psychiatry | 22 patients with borderline/schizotypal personality disorder; reduced self-injury and symptom scores |
| [9664779](https://pubmed.ncbi.nlm.nih.gov/9664779/) | 1998 | Case report | Psychosomatics | Transient psychosis with polydipsia in a schizotypal patient taking fluoxetine (safety signal) |
| [23218251](https://pubmed.ncbi.nlm.nih.gov/23218251/) | 2013 | Systematic review | J Affect Disord | Olanzapine plus fluoxetine in bipolar depression |

---

## South Africa Market Information

All three registrations are single-ingredient oral capsules and are currently valid. The data compiled for this report contain no approved indication text and no Essential Medicines List information for these products.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/1.2/0279 | Rezak | Capsule | Not available |
| Reg. No. 30/1.2/0356 | Fluoxetine Biotech 20 | Capsule | Not available |
| Reg. No. 37/1.2/0612 | Trizac 20 Mg | Capsule | Not available |

---

## Safety Considerations

**Knowledge-graph contraindication relations** (not label text): hepatic disease and liver failure, cirrhosis, epilepsy, bipolar disorder and major affective disorder, diabetes and hyperglycaemia, diabetic ketoacidosis, neutropenia and agranulocytosis, blood coagulation disorders, benign prostatic hyperplasia, orthostatic hypotension, stroke and cerebrovascular disease, myocardial infarction, hyperlipidaemia and obesity, among others.

**Drug interactions** (100 recorded; examples):
- **Major:** bupropion, lorcaserin, diethylpropion, dolasetron, palonosetron, eliglustat, cisapride
- **Moderate:** acetylsalicylic acid (bleeding risk), morphine, clarithromycin, famotidine, loperamide, chlorpropamide and other sulfonylureas

**Other signals from the literature:**
- A case report describes transient psychosis in a schizotypal patient taking fluoxetine (PMID 9664779).
- SSRI monotherapy in mania carries a risk of mood switching.
- Paediatric use warrants suicidality monitoring.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for paranoid personality disorder)

**Rationale:**
- There are no trials and no direct publications for fluoxetine in paranoid personality disorder. The high score is most likely a network artefact, and evidence for core features is absent.
- If the programme wishes to move forward, phobic disorder (social anxiety disorder) and bipolar depression (with a mood stabiliser) are better-supported candidates and merit Proceed with Guardrails, subject to the verification below.

**To proceed, the following is needed:**
- Confirmation that fluoxetine was a tested arm in NCT00043537 and the actual outcome data
- Retrieval of the SAHPRA Professional Information for warnings, contraindications and approved indications of the three registered products
- Mechanism of action data (currently missing)
- For any personality disorder indication, a controlled trial targeting core features, with a safety plan addressing psychosis and mood-switch risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

