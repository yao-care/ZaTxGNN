---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Depression/Anxiety Disorders to Obsessive-Compulsive Disorder

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) publicly known for treating major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, and fibromyalgia. Among the ten new indications flagged by the TxGNN model for this drug, the most credible candidate is **Obsessive-Compulsive Disorder (OCD)**, supported by **5 clinical trials (including a completed Phase 4 trial)** and **20 publications (including a double-blind RCT)**. Note: the model's single *highest-scoring* prediction (an infant self-limiting condition) and six other candidates carry no supporting evidence at all and are addressed separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the structured regulatory dataset (duloxetine is unregistered in South Africa). Publicly documented indications include major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, and fibromyalgia (per literature PMID 31749717). |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) — selected as the strongest evidence-backed candidate; see note on ranking below |
| TxGNN Prediction Score | 99.84% (score 0.99840, model rank 1234 of full candidate list) |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

> **Note on selecting OCD over the top-ranked prediction:** The single highest-scoring TxGNN prediction for duloxetine is *benign paroxysmal torticollis of infancy* (99.85%), a self-limiting infant condition with zero supporting trials or literature. The evidence pack itself flags this — and six further candidates (four personality disorders and three rare genetic/ophthalmic syndromes) — as likely knowledge-graph artefacts rather than genuine drug-disease signals. This report therefore focuses on OCD, the candidate with the most substantive clinical evidence, and summarises the discarded candidates in a dedicated section below for transparency.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for duloxetine is not available in this dataset ([Data Gap] — DG002). Based on established pharmacological knowledge, duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI); its efficacy in depression and anxiety-spectrum disorders is well established, and mechanistically this serotonergic/noradrenergic action may extend to OCD, since first-line OCD pharmacotherapy (SSRIs, clomipramine) also acts primarily through the serotonergic system.

OCD and duloxetine's established indications (MDD, GAD) share overlapping monoaminergic pathophysiology, and OCD is classified alongside anxiety-spectrum disorders in several diagnostic frameworks. This provides a plausible mechanistic bridge for repurposing.

However, the literature evidence itself tempers this rationale: a dedicated meta-analysis (PMID 28477500) found that OCD shows a *reduced* placebo and antidepressant response compared with other anxiety disorders, and the available duloxetine-OCD evidence consistently positions the drug as **augmentation therapy for SSRI/clomipramine-resistant OCD**, not as first-line monotherapy. This is an important nuance for any clinical use case built on this prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Direct interventional evaluation of duloxetine's efficacy in OCD — the most specific completed trial for this indication. |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicting medication response in OCD; duloxetine included as an alternative arm to clomipramine/escitalopram for patients with prior treatment exposure. |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Large individual-patient-data meta-analysis of antidepressant efficacy across anxiety disorders (includes duloxetine); not OCD-specific, indirect supporting evidence only. |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | Unknown | 1 | Psychoanalytic treatment study in Autism Spectrum Disorder with psychiatric comorbidities (including OCD); minimal relevance (N=1). |
| [NCT01944657](https://clinicaltrials.gov/study/NCT01944657) | N/A | Withdrawn | 0 | TMS vs. medication monotherapy for major depression; withdrawn with zero enrollment — background relevance only. |

No SANCTR or PACTR-registered trials were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | RCT (double-blind) | Journal of Clinical Psychopharmacology | Double-blind controlled trial evaluating duloxetine as add-on therapy in SSRI-resistant OCD. |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical Review | The Journal of Clinical Psychiatry | Critical review of SNRI antiobsessional evidence as an alternative to first-line SSRIs in OCD. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opinion on Pharmacotherapy | Reviews double-blind serotonergic-antidepressant trials in OCD, contextualizing SNRI use including duloxetine. |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Systematic Review | Frontiers in Psychiatry | Systematic review of duloxetine's off-label psychiatric uses beyond MDD/GAD, including OCD. |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-Analysis | Journal of Affective Disorders | Shows OCD has a *reduced* placebo and antidepressant response versus other anxiety disorders — an important caveat on expected efficacy. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Frontiers in Psychiatry | Meta-review of antidepressant efficacy/tolerability in paediatric psychiatric disorders including OCD; not duloxetine-specific. |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Cohort (Open-label) | International Journal of Neuropsychopharmacology | Open-label study directly assessing duloxetine efficacy in DSM-IV OCD. |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Review/Discussion | Innovations in Clinical Neuroscience | Proposes SNRIs, including duloxetine, as pharmacological alternatives when standard OCD treatment is inadequate. |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case Series | Journal of Psychopharmacology | Case series describing switch to duloxetine (SNRI) in SSRI-refractory OCD patients. |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case Report | Primary Care Companion to the Journal of Clinical Psychiatry | Case report of OCD symptom improvement with duloxetine. |

An additional 10 case reports/series (largely reporting high-dose or supratherapeutic duloxetine use, or unrelated adverse-event reports) were identified but are lower priority and omitted from this summary; full list available in the source evidence pack query log.

---

## South Africa Market Information

Duloxetine currently holds **no SAHPRA registrations** and is recorded as **not marketed** in South Africa. No product registration numbers, brand names, or approved indication text are available in the regulatory dataset for this drug.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Data gap flagged:** Product label warnings, contraindications, and drug-interaction data for duloxetine are currently missing from this evidence pack (DG001, severity: **Blocking**). This gap prevents completion of the mandatory preliminary safety screening (decision stage S1) and must be resolved before any further action on this candidate.

---

## Other TxGNN-Ranked Candidates (Not Recommended for Further Review)

For transparency, the remaining candidates from this model run are summarized below. None currently warrant active evaluation:

| Rank | Disease | Score | Evidence Level | Assessment |
|------|---------|-------|-----------------|------------|
| 1 | Benign paroxysmal torticollis of infancy | 99.85% | L5 | Self-limiting infant condition; no trials, no literature, no plausible mechanistic link. Likely knowledge-graph artefact. |
| 2 | Agoraphobia | 99.84% | L3 | 1 low-relevance trial (N=1, unknown status) and 3 publications, but all focused on panic disorder/GAD rather than agoraphobia specifically — indirect extrapolation only. |
| 4–7 | Schizotypal, paranoid, histrionic, and schizoid personality disorders | 99.78% (identical across all four) | L5 | No trials or literature for any of the four; identical scores strongly suggest a knowledge-graph clustering effect on the "personality disorder" node category rather than four independent signals. |
| 8 | Ohdo syndrome and variants | 99.69% | L5 | Rare genetic developmental disorder (KAT6B/MED12-related); no mechanistic link to SNRI pharmacology, no evidence. |
| 9 | Ligneous conjunctivitis | 99.66% | L5 | Rare plasminogen-deficiency ophthalmic disorder; no mechanistic link to monoamine reuptake inhibition, no evidence. |
| 10 | Blepharophimosis–intellectual disability syndrome, Ohdo type | 99.60% | L5 | Ohdo syndrome subtype; same assessment as rank 8. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The OCD candidate has meaningful L2 clinical evidence (a completed Phase 4 trial, a double-blind augmentation RCT, and a consistent open-label/case-series literature base), but a **Blocking** data gap (DG001) means duloxetine's SAHPRA/TFDA safety label information is unavailable, so the mandatory S1 safety screening cannot be completed. In addition, duloxetine has zero SAHPRA registrations and is not currently marketed in South Africa, so there is no existing local access pathway to build on. The remaining nine candidates in this evidence pack lack sufficient evidence to progress and should not be carried forward.

**To proceed, the following is needed:**
- SAHPRA-approved (or a reference-regulator, e.g. FDA/EMA) Professional Information for duloxetine, to complete safety and contraindication screening (resolves DG001)
- Formal mechanism-of-action documentation via DrugBank or pharmacology references (resolves DG002)
- Clarification of a local market-access pathway (e.g. Section 21 access or new registration), since duloxetine currently holds no SAHPRA licenses
- A dedicated systematic review or meta-analysis specifically evaluating duloxetine in OCD, ideally framed around its role as **augmentation therapy** for SSRI/clomipramine-resistant patients, to consolidate the currently scattered open-label and case-level evidence
- No further action on agoraphobia or the seven no-evidence candidates unless new mechanistic or trial data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

