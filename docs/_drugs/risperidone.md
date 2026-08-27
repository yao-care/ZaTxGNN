---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Risperidone: From Schizophrenia and Bipolar Mania to Major Affective Disorder

## One-Sentence Summary

Risperidone is a second-generation (atypical) antipsychotic originally approved for schizophrenia and bipolar mania. The TxGNN model predicts it may also be effective for **Major Affective Disorder** (mood disorders, including treatment-resistant depression as an augmentation agent), with **36 clinical trials** and **20 publications** currently supporting this direction — by far the strongest-evidenced of six TxGNN-predicted indications in this evidence pack.

> **Note on candidate selection:** The evidence pack scored six candidate indications for risperidone. Five of them (e.g., "gaze palsy, familial horizontal, with progressive scoliosis," "Asperger syndrome, susceptibility to") had TxGNN scores above 99.6% but **zero clinical trials, zero-to-minimal literature, and an evidence level of L5 with a "Hold" recommendation** — the evidence pack itself flags several as likely knowledge-graph noise. Major Affective Disorder, despite a slightly lower raw TxGNN score, is the only candidate with substantial, directly relevant clinical and literature support (evidence level L1, decision stage S3). This report focuses on that candidate as the clinically actionable one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia and bipolar mania (internationally approved indication, per supporting trial records; South Africa-specific PI/label text not yet available — see Data Gap DG001) |
| Predicted New Indication | Major Affective Disorder (mood disorders, incl. treatment-resistant depression augmentation) |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| South Africa Market Status | Not currently marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action data is not available from the DrugBank query result (Data Gap DG002). Based on the supporting literature in this evidence pack (PMID 7545159), risperidone is described as "a new-generation atypical antipsychotic agent with potent dopaminergic and serotonergic antagonist activity" — i.e., a combined dopamine D2 / serotonin 5-HT2A receptor antagonist.

Risperidone's original approved indications — schizophrenia and bipolar mania — are themselves primary disorders of dopaminergic/serotonergic dysregulation. Bipolar mania is, by definition, a subtype of major affective (mood) disorder, so the drug already has a foothold in this disease family. The extension to broader "major affective disorder" (including treatment-resistant unipolar depression) follows the same mechanistic logic: adding a D2/5-HT2A antagonist to a serotonergic antidepressant (SSRI/SNRI) is a well-established augmentation strategy, described in this evidence pack as "risperidone augmentation of serotonin reuptake inhibitors."

This is not a novel or speculative extrapolation — the evidence pack itself contains multiple completed Phase 3 randomized controlled trials and several systematic reviews/meta-analyses (including a Cochrane review) directly testing risperidone or the wider second-generation-antipsychotic-augmentation class in mood disorders, giving this prediction a much firmer evidentiary base than the other five TxGNN candidates.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00107939](https://clinicaltrials.gov/study/NCT00107939) | Phase 3 | Completed | 453 | Randomized, double-blind, placebo-controlled trial of licarbazepine as adjunctive therapy to an atypical antipsychotic (including risperidone) for manic episodes of bipolar I disorder |
| [NCT00057681](https://clinicaltrials.gov/study/NCT00057681) | Phase 3 | Completed | 379 | TEAM study — lithium vs. valproate vs. risperidone in children/adolescents with bipolar disorder or mania |
| [NCT00221403](https://clinicaltrials.gov/study/NCT00221403) | Phase 3 | Completed | 46 | Placebo-controlled trial of valproate and risperidone in young children (ages 3–7) with bipolar disorder |
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind trial of adjunctive risperidone vs. placebo in major depressive disorder with suboptimal antidepressant response |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Efficacy, safety, and long-term maintenance of risperidone augmentation of SSRI therapy vs. placebo in unipolar treatment-resistant depression |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Randomized, double-blind, placebo- and active-controlled study of risperidone long-acting injectable for prevention of mood episodes in bipolar I disorder |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Randomized, double-blind, placebo-controlled study of risperidone monotherapy in bipolar disorder with comorbid panic/generalized anxiety disorder |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Controlled trial of risperidone vs. divalproex sodium with MRI assessment of affected circuitry in pediatric bipolar disorder |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Randomized, double-blind, placebo-controlled study of risperidone monotherapy in bipolar disorder with comorbid panic disorder or generalized anxiety disorder |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Safety and efficacy of risperidone augmentation in patients with partial or no response to an adequate antidepressant trial |

*Note: current South African trial registry (SANCTR) or Pan-African Clinical Trials Registry (PACTR) identifiers were not present in the source data.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Annals of Internal Medicine | Randomized trial of risperidone for treatment-refractory major depressive disorder |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review/Network Meta-analysis | Journal of Affective Disorders | Compares efficacy and discontinuation of augmentation agents (incl. risperidone) in treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review/Meta-analysis | Journal of Psychopharmacology | Evaluates augmentation/combination treatments for early-stage treatment-resistant depression |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematic Review/Meta-analysis | Journal of Psychopharmacology | Compares antidepressant + second-generation antipsychotic augmentation vs. esketamine vs. lithium in MDD |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Review/Meta-analysis | Psychological Medicine | Efficacy and safety/tolerability of antipsychotics (monotherapy and adjunctive) in major depressive disorder |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Second-generation antipsychotics, including risperidone, added to antidepressants for major depression and dysthymia |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Nationwide Population-Based Study | The Journal of Clinical Psychiatry | Effectiveness of aripiprazole, olanzapine, quetiapine, and risperidone augmentation for MDD in a nationwide cohort |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Brazilian Journal of Medical and Biological Research | Efficacy and tolerability of atypical antipsychotic augmentation (17 trials, 3,807 patients) in major depressive disorder |
| [7545159](https://pubmed.ncbi.nlm.nih.gov/7545159/) | 1995 | Clinical Study | The Journal of Clinical Psychiatry | Early foundational report on risperidone's potential role in affective illness and obsessive-compulsive disorder |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | The Annals of Pharmacotherapy | Reviews efficacy and safety of risperidone augmentation in major depressive disorder |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug interaction data were not returned by the source query for this candidate — DG001, blocking gap.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and several systematic reviews/meta-analyses (including a Cochrane review) support risperidone augmentation therapy in mood disorders, and risperidone already carries an internationally-recognized indication for bipolar mania — itself a major affective disorder subtype — giving strong mechanistic and clinical continuity. However, the drug is not currently marketed in South Africa (0 SAHPRA registrations) and SA-specific safety labeling is missing, so guardrails are required before any clinical application.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, precautions, and contraindications (Data Gap DG001, blocking)
- Structured mechanism-of-action confirmation via DrugBank API (Data Gap DG002)
- A regulatory pathway assessment, since risperidone currently has no SAHPRA registration in this dataset
- A drug-drug interaction (DDI) profile, since the interaction query returned no results (`not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

