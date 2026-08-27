---
layout: default
title: Moclobemide
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 2
---

# Moclobemide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Moclobemide: From Depression to Agoraphobia

## One-Sentence Summary

> Moclobemide is a reversible MAO-A inhibitor (RIMA) whose evidence pack does not record its originally approved indication, though it is pharmacologically established as an antidepressant.
> The TxGNN model predicts it may be effective for **Agoraphobia**,
> with **no dedicated clinical trials** but **12 supporting publications**, including two double-blind RCTs in panic disorder with agoraphobia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in evidence pack (`original_indications` empty); Moclobemide is a known RIMA-class antidepressant |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa` = Data Gap). Based on known pharmacology, moclobemide is a reversible, selective inhibitor of monoamine oxidase A (RIMA). By slowing the metabolism of noradrenaline, serotonin, and dopamine, it raises synaptic monoamine concentrations — the same pharmacological logic underlying older, irreversible MAOIs (e.g., phenelzine), which have long-standing literature support for efficacy in panic disorder and agoraphobia.

Panic disorder and agoraphobia are closely related, frequently comorbid anxiety conditions. Moclobemide extends the MAOI mechanistic rationale for this disease cluster while offering a better tolerability profile and fewer dietary restrictions than irreversible MAOIs. However, most of the supporting clinical literature enrolled patients with "panic disorder" as the primary diagnosis, with agoraphobia typically present as a comorbid feature rather than an independent trial endpoint — so the disease-specific match to "agoraphobia" alone is moderate rather than direct.

No mechanistic or clinical link supports the model's second-ranked prediction (benign paroxysmal torticollis of infancy), which is excluded from this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10448444](https://pubmed.ncbi.nlm.nih.gov/10448444/) | 1999 | RCT | Br J Psychiatry | Randomised placebo-controlled trial of moclobemide, CBT, and their combination in panic disorder with agoraphobia |
| [10361962](https://pubmed.ncbi.nlm.nih.gov/10361962/) | 1999 | RCT | Eur Arch Psychiatry Clin Neurosci | Multicenter double-blind RCT: moclobemide 450 mg/day vs clomipramine 150 mg/day in DSM-III-R panic disorder with/without agoraphobia (n=135) |
| [16850261](https://pubmed.ncbi.nlm.nih.gov/16850261/) | 2006 | Cohort | Metab Brain Dis | SPECT study comparing citalopram vs moclobemide effects on resting brain perfusion in social anxiety disorder |
| [28867934](https://pubmed.ncbi.nlm.nih.gov/28867934/) | 2017 | Review | Dialogues Clin Neurosci | Guideline-based review of pharmacotherapy for anxiety disorders, including panic disorder/agoraphobia |
| [32002937](https://pubmed.ncbi.nlm.nih.gov/32002937/) | 2020 | Review | Adv Exp Med Biol | Review of current and novel psychopharmacological drugs for anxiety disorders, including panic disorder/agoraphobia |
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatr Scand Suppl | Review of reversible MAO-A inhibitors (brofaromine, moclobemide, toloxatone) in mental disorders |
| [2248064](https://pubmed.ncbi.nlm.nih.gov/2248064/) | 1990 | Review | Acta Psychiatr Scand Suppl | Review of MAOI efficacy in panic disorder with agoraphobia, social phobia, and related psychiatric disorders |
| [8313401](https://pubmed.ncbi.nlm.nih.gov/8313401/) | 1993 | Review | Clin Neuropharmacol | Review of reversible, selective MAO-A inhibitors in panic disorder, incl. a randomized trial vs clomipramine |
| [1498904](https://pubmed.ncbi.nlm.nih.gov/1498904/) | 1992 | Review | Clin Neuropharmacol | Review of reversible monoamine-A inhibitors in panic disorder |
| [7892341](https://pubmed.ncbi.nlm.nih.gov/7892341/) | 1995 | Case Report | Psychiatrische Praxis | Treatment-refractory panic disorder with agoraphobia, social phobia, and depression remitted with combined imipramine + moclobemide + behavioural therapy |

---

## South Africa Market Information

Moclobemide is currently **not marketed** in South Africa — the evidence pack records zero SAHPRA registrations. No product, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Supporting evidence consists of older literature (RCTs from 1999, reviews through 2020) largely enrolling "panic disorder" patients rather than agoraphobia as a primary endpoint, and no clinical trials directly targeting agoraphobia exist. Combined with a blocking data gap on SAHPRA/PI safety information and zero market presence in South Africa, the evidence is not yet sufficient to advance beyond a research question.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications, DDI) — currently a blocking data gap preventing initial safety screening
- Detailed mechanism of action documentation
- A South Africa market-entry or import pathway assessment, since the product is not currently registered
- Prospective or retrospective studies specifically targeting agoraphobia (rather than panic disorder generally) to raise the evidence level
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

