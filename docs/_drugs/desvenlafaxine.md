---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI), approved by the US FDA for the treatment of major depressive disorder (MDD) under the trade name Pristiq; it is currently **not registered in South Africa**.
The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**, with **2 clinical trials** (indirect relevance) and **4 publications** currently identified in this direction.
Of note, stronger clinical evidence exists for two secondary predictions — **dysthymic disorder** and **melancholia** — which are discussed further below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (US FDA-approved; not registered in South Africa) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (Preclinical / mechanistic studies; no direct desvenlafaxine-OCD trial) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications at a Glance

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Trials | Publications | Recommendation |
|------|---------------------|-------------|----------------|--------|-------------|----------------|
| 1 | Obsessive-Compulsive Disorder | 99.91% | L4 | 2 (indirect) | 4 | Hold |
| 2 | Schizotypal Personality Disorder | 99.84% | L5 | 0 | 0 | Hold |
| 3 | Paranoid Personality Disorder | 99.84% | L5 | 0 | 0 | Hold |
| 4 | Schizoid Personality Disorder | 99.84% | L5 | 0 | 0 | Hold |
| 5 | Histrionic Personality Disorder | 99.84% | L5 | 0 | 0 | Hold |
| 6 | Ohdo Syndrome and Variants | 99.74% | L5 | 0 | 0 | Hold |
| 7 | Benign Paroxysmal Torticollis of Infancy | 99.74% | L5 | 0 | 0 | Hold |
| **8** | **Dysthymic Disorder** | **99.73%** | **L2** | **3** | **2** | **Proceed with Guardrails** |
| 9 | Agoraphobia | 99.70% | L4 | 0 | 0 | Hold |
| **10** | **Melancholia** | **99.64%** | **L2** | **1** | **19** | **Proceed with Guardrails** |

> **Note:** Ranks 8 (dysthymic disorder) and 10 (melancholia) carry substantially stronger clinical evidence than the top-ranked OCD prediction. These are detailed in dedicated sections below.

---

## Why is This Prediction Reasonable?

### Mechanism of Action

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, desvenlafaxine is the major active metabolite of venlafaxine and belongs to the SNRI class. It inhibits the reuptake of both serotonin (5-HT) and norepinephrine (NE), with relatively greater potency at the serotonin transporter. It is approved for MDD in the United States, Canada, and several other jurisdictions.

### Relationship Between Original and New Indication

OCD is a neuropsychiatric disorder in which serotonin system dysregulation plays a central pathological role. First-line pharmacotherapy for OCD relies on high-dose SSRIs or clomipramine, both of which act through potent serotonin reuptake inhibition. Since desvenlafaxine has strong 5-HT reuptake inhibition activity, there is a mechanistic rationale for its potential efficacy in OCD.

### Caveats

The parent compound venlafaxine has been directly studied in OCD (see PMID 14624187), showing comparable efficacy to paroxetine. However, desvenlafaxine itself has never been tested in a dedicated OCD trial. Furthermore, SNRI efficacy in OCD may be inferior to that of pure SSRIs, because the clinical role of the norepinephrine component in OCD remains unclear and could theoretically counteract some serotonergic benefits. The TxGNN prediction should therefore be interpreted as mechanistically plausible but clinically unproven for this specific drug.

---

## Clinical Trial Evidence — OCD

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Evaluated troriluzole (a glutamate modulator) as adjunctive therapy in OCD patients with inadequate response to SSRI, clomipramine, venlafaxine, or desvenlafaxine. **Note:** Desvenlafaxine was background therapy, not the intervention under study. Indirect relevance only. |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Pilot study of desvenlafaxine in postpartum depression, examining functional outcomes. **Not an OCD study** — matched only on drug name. |

> **Interpretation:** No clinical trial has directly tested desvenlafaxine as a treatment for OCD. The trials above are indirect matches only.

---

## Literature Evidence — OCD

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | J Clin Psychopharmacol | Double-blind comparison of **venlafaxine** (parent compound) vs paroxetine in 150 OCD patients. Demonstrated comparable efficacy between the two drugs, supporting SNRI class activity in OCD. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Narrative Review | Expert Opin Pharmacother | Review of serotonergic antidepressants in OCD, confirming key role of 5-HT system in OCD pathophysiology and treatment response. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression, noting its association with later development of OCD and anxiety. Indirect relevance. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical Study | Psychiatry Clin Psychopharmacol | Case study of risperidone augmentation for treatment-resistant somatic symptom disorder, mentioning OCD as a context. Tangential relevance. |

---

## Notable Secondary Prediction: Dysthymic Disorder (Rank 8)

### Rationale

Persistent depressive disorder (dysthymia) shares the same serotonin/norepinephrine neurotransmitter imbalance as MDD. Desvenlafaxine is already FDA-approved for MDD, and dysthymia represents a natural extension of its therapeutic spectrum. The SNRI dual mechanism may be particularly beneficial for the chronic, low-grade mood disturbance accompanied by fatigue and motivational deficits that characterise dysthymia.

### Clinical Trial Evidence — Dysthymic Disorder

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01537068](https://clinicaltrials.gov/study/NCT01537068) | Phase 4 | Completed | 59 | **Desvenlafaxine vs placebo** for chronic depression / dysthymia. Rigorous RCT design. Directly tests the predicted indication. Highest-relevance evidence. |
| [NCT01948895](https://clinicaltrials.gov/study/NCT01948895) | N/A | Completed | 30 | Open-label, flexible-dose study of **desvenlafaxine monotherapy** for dysthymia over 8 weeks. Provides preliminary efficacy and safety data. |
| [NCT04437485](https://clinicaltrials.gov/study/NCT04437485) | Phase 2 | Completed | 46 | Collaborative care for depression in patients with pre-diabetes. Partial overlap with dysthymia but primarily focused on metabolic outcomes. |

### Literature Evidence — Dysthymic Disorder

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [21527126](https://pubmed.ncbi.nlm.nih.gov/21527126/) | 2011 | Meta-analysis of RCTs | J Clin Psychiatry | Determined efficacy of antidepressants in dysthymic disorder; compared antidepressant vs placebo response rates between MDD and dysthymia. Strong class-level evidence. |
| [28064115](https://pubmed.ncbi.nlm.nih.gov/28064115/) | 2017 | Longitudinal Cohort | J Affect Disord | Investigated continued SNRI (duloxetine) treatment on symptoms and social functioning in dysthymia patients. Supports SNRI class activity. |

> **Evidence Level: L2** — One completed placebo-controlled RCT (NCT01537068) directly testing desvenlafaxine in dysthymia, plus a completed open-label trial. **Recommendation: Proceed with Guardrails.**

---

## Notable Secondary Prediction: Melancholia (Rank 10)

### Rationale

Melancholia (melancholic depression) is a severe subtype of MDD characterised by pronounced neurobiological dysregulation, including HPA axis overactivation and severe monoamine system disruption. Desvenlafaxine's dual 5-HT + NE reuptake inhibition mechanism is particularly suited to this subtype, as melancholic patients often respond poorly to single-mechanism agents, and the norepinephrine component may specifically address psychomotor retardation and energy loss.

### Clinical Trial Evidence — Melancholia

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01916824](https://clinicaltrials.gov/study/NCT01916824) | Phase 4 | Completed | 53 | Studied effects of antidepressant treatment on decision-making in MDD patients. Not specific to the melancholic subtype but provides indirect supporting data. |

### Literature Evidence — Melancholia (Top 10 of 19 publications)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26895080](https://pubmed.ncbi.nlm.nih.gov/26895080/) | 2016 | Integrated Analysis | Int Clin Psychopharmacol | Integrated efficacy and safety analysis of desvenlafaxine in MDD. Supports full remission as treatment goal. |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Systematic Review & NMA | Mol Psychiatry | Compared antidepressants for MDD maintenance; ranked by efficacy, acceptability, tolerability, and safety. |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Clinical Practice Guideline | Clin Pharmacol Ther | CPIC guideline for pharmacogenomic-guided use of SRI antidepressants including desvenlafaxine. CYP2D6/CYP2C19 genotyping recommendations. |
| [37450377](https://pubmed.ncbi.nlm.nih.gov/37450377/) | 2023 | Real-World Evidence | Expert Opin Pharmacother | Narrative review of desvenlafaxine efficacy and tolerability in real-world MDD treatment. |
| [36700320](https://pubmed.ncbi.nlm.nih.gov/36700320/) | 2023 | RCT | Clin Psychopharmacol Neurosci | Compared escitalopram, desvenlafaxine, and vortioxetine in anxious depression (6-week rater-blinded trial). |
| [40172868](https://pubmed.ncbi.nlm.nih.gov/40172868/) | 2025 | Observational | JAMA Psychiatry | Esketamine combined with SSRI or SNRI for treatment-resistant depression; includes desvenlafaxine as combination partner. |
| [41135546](https://pubmed.ncbi.nlm.nih.gov/41135546/) | 2025 | Systematic Review (Safety) | Lancet | Compared cardiometabolic and physiological effects of antidepressants from RCT data. |
| [28817491](https://pubmed.ncbi.nlm.nih.gov/28817491/) | 2017 | Post-hoc Analysis | J Clin Psychopharmacol | Examined speed of symptom improvement with desvenlafaxine 50 mg and 100 mg vs placebo in MDD. |
| [28146000](https://pubmed.ncbi.nlm.nih.gov/28146000/) | 2017 | Post-hoc Meta-analysis | J Clin Psychopharmacol | Efficacy of desvenlafaxine vs placebo across age groups and depression severity at baseline. |
| [35500900](https://pubmed.ncbi.nlm.nih.gov/35500900/) | 2022 | RCT | Psychiatry Investig | Compared escitalopram, vortioxetine, and desvenlafaxine for MDD with cognitive complaints. |

> **Evidence Level: L2** — One completed Phase 4 trial with multiple systematic reviews and meta-analyses supporting desvenlafaxine in depressive subtypes. **Recommendation: Proceed with Guardrails.**

---

## South Africa Market Information

Desvenlafaxine is **not currently registered with SAHPRA** and has no marketed products in South Africa. There are **0 active registrations**.

| Item | Detail |
|------|--------|
| SAHPRA Registration Status | Not registered |
| Number of Registrations | 0 |
| Essential Medicines List (EML) | Not listed |
| Implication | Any clinical use would require Section 21 application (unregistered medicines) via SAHPRA |

> For reference, desvenlafaxine is marketed internationally as **Pristiq** (Pfizer) in extended-release tablet form (25 mg, 50 mg, 100 mg), approved for MDD.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As desvenlafaxine is not registered in South Africa, clinicians should consult the US FDA-approved prescribing information or other regulatory references. Report adverse drug reactions to SAHPRA.

**General SNRI class warnings (from international labels) include:**

- **Suicidality:** Black box warning (US FDA) — increased risk of suicidal thinking and behaviour in children, adolescents, and young adults
- **Serotonin syndrome:** Risk when combined with other serotonergic agents or MAOIs
- **Discontinuation syndrome:** Gradual dose tapering recommended; abrupt withdrawal may cause dizziness, nausea, headache, irritability
- **Hypertension:** Blood pressure monitoring recommended; sustained increases reported
- **Bleeding risk:** Increased risk when combined with NSAIDs, aspirin, or anticoagulants
- **Hepatic/Renal impairment:** Dose adjustment may be required

> ⚠️ *The above are general class warnings. Specific desvenlafaxine safety data was not available in this evidence pack. Clinicians should obtain the full prescribing information before clinical use.*

---

## Conclusion and Next Steps

### Primary Prediction: Obsessive-Compulsive Disorder

**Decision: Hold**

**Rationale:**
While the TxGNN prediction score is high (99.91%) and the mechanistic rationale is plausible based on desvenlafaxine's serotonergic activity, there are no clinical trials directly testing desvenlafaxine for OCD. The parent compound venlafaxine has one RCT showing efficacy comparable to paroxetine in OCD, but this cannot be directly extrapolated. Current evidence is insufficient to recommend clinical pursuit.

**To proceed, the following is needed:**
- A dedicated pilot study or RCT of desvenlafaxine in OCD
- Head-to-head comparison data vs established OCD treatments (high-dose SSRIs)
- SAHPRA registration of desvenlafaxine in South Africa

---

### Secondary Prediction: Dysthymic Disorder

**Decision: Proceed with Guardrails**

**Rationale:**
A completed placebo-controlled RCT (NCT01537068) directly tested desvenlafaxine for dysthymia, supported by an additional open-label trial and meta-analytic evidence for the SNRI class. Dysthymia shares pathophysiological mechanisms with MDD, for which desvenlafaxine is already approved.

**To proceed, the following is needed:**
- SAHPRA registration or Section 21 authorisation for desvenlafaxine
- Publication of full results from NCT01537068 and NCT01948895
- Local safety monitoring plan including blood pressure and suicidality screening
- Pharmacogenomic considerations (CYP2D6 genotyping per CPIC guideline)

---

### Secondary Prediction: Melancholia

**Decision: Proceed with Guardrails**

**Rationale:**
Melancholia is a severe MDD subtype for which desvenlafaxine's dual 5-HT/NE mechanism offers a strong pharmacological rationale. Extensive literature (19 publications including multiple systematic reviews and meta-analyses) supports desvenlafaxine's efficacy across MDD subtypes, and the SNRI dual mechanism may be especially beneficial for psychomotor retardation and anhedonia, which are hallmarks of melancholic depression.

**To proceed, the following is needed:**
- SAHPRA registration or Section 21 authorisation for desvenlafaxine
- Subtype-specific efficacy analysis from existing RCT datasets (post-hoc analyses on melancholic features)
- Local clinical protocol for identifying and managing melancholic depression

---

### Predictions Not Recommended for Pursuit

| Prediction | Reason for Hold |
|-----------|----------------|
| Personality disorders (schizotypal, paranoid, schizoid, histrionic) | No evidence; SNRI mechanism does not target core personality disorder pathology |
| Ohdo syndrome | Rare genetic/developmental disorder; no pharmacological rationale for SNRI use |
| Benign paroxysmal torticollis of infancy | Paediatric self-limiting condition; significant safety concerns with SNRI use in infants |
| Agoraphobia | Plausible mechanism (venlafaxine approved for related anxiety disorders) but no direct evidence for desvenlafaxine |

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Data cutoff: 2026-04-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

