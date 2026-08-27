---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Fluoxetine
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

# Fluoxetine: From Major Depressive Disorder to Agoraphobia and Related Anxiety-Spectrum Disorders

## One-Sentence Summary

Fluoxetine (DrugBank DB00472) is a selective serotonin reuptake inhibitor (SSRI) with well-established use in major depressive disorder internationally. The TxGNN model returned 10 candidate indications for this drug; the top-ranked hits by raw score are Cluster A personality disorders (weak, indirect evidence), but the **best-supported repurposing signal is Agoraphobia**, backed by **19 publications**, including three tier-1 RCTs, though **no registered clinical trials** were found for this specific indication. Critically, fluoxetine currently has **zero SAHPRA registrations** in South Africa and a **blocking data gap** on Professional Information (PI) warnings, so no formal safety assessment can be completed yet.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (general pharmacological knowledge — not present in this evidence pack; South Africa registry data is empty) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed / not SAHPRA-registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (indication-level) — see Conclusion for drug-level caveat |

---

## TxGNN Predicted Indications — Full Ranking

This is a multi-indication candidate pack (10 predictions). Evidence quality varies substantially and does **not** track raw TxGNN score — the highest-scoring predictions (Cluster A personality disorders) are the weakest-supported, while several mid-ranked predictions have solid RCT/meta-analytic backing:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Schizoid personality disorder | 99.92% | L4 | S0 | Hold |
| 2 | Schizotypal personality disorder | 99.92% | L3 | S1 | Research Question |
| 3 | Paranoid personality disorder | 99.92% | L4 | S0 | Hold |
| 4 | Histrionic personality disorder | 99.92% | L4 | S0 | Hold |
| 5 | Benign paroxysmal torticollis of infancy | 99.89% | L5 | S0 | Hold |
| 6 | **Agoraphobia** | 99.86% | **L2** | **S2** | **Proceed with Guardrails** |
| 7 | Manic bipolar affective disorder | 99.64% | L4 | S0 | Hold (mechanistic concern: SSRIs can precipitate manic switch) |
| 8 | Phobic disorder | 99.63% | L2 | S2 | Proceed with Guardrails |
| 9 | Ohdo syndrome and variants | 99.63% | L5 | S0 | Hold |
| 10 | Melancholia | 99.57% | L2 | S2 | Proceed with Guardrails |

The three "Proceed with Guardrails" indications (agoraphobia, phobic disorder, melancholia) are all serotonergic/anxiety-depression spectrum conditions consistent with fluoxetine's known pharmacology. Agoraphobia is presented as the primary candidate below because it has the highest score among this group and the most direct literature base.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (DG002, High severity). Based on known pharmacological class information, fluoxetine is a selective serotonin reuptake inhibitor (SSRI); its efficacy in major depressive disorder and panic disorder has been established internationally, and mechanistically this profile may extend to agoraphobia.

Agoraphobia most commonly presents as a comorbid or secondary feature of panic disorder, and serotonergic modulation of amygdala/limbic circuit hyperactivation is the accepted mechanism underlying SSRI efficacy in panic-spectrum anxiety. Several SSRIs in this class (fluvoxamine, fluoxetine, paroxetine, sertraline, citalopram) have documented superiority over placebo for panic disorder and associated agoraphobic avoidance.

The TxGNN signal for agoraphobia is corroborated by a Cochrane network meta-analysis and multiple randomized, double-blind trials evaluating fluoxetine specifically in panic disorder with agoraphobia, which strengthens confidence in this prediction relative to the higher-scoring but mechanistically unsupported personality-disorder predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for agoraphobia specifically (0 results in ClinicalTrials.gov and ICTRP queries). Evidence for this indication comes from published literature (below), not registry-indexed trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7786880](https://pubmed.ncbi.nlm.nih.gov/7786880/) | 1995 | RCT | J Psychiatry Neurosci | Fluoxetine (mean 20mg/day) demonstrated anti-panic efficacy in patients with panic disorder and agoraphobia |
| [11001241](https://pubmed.ncbi.nlm.nih.gov/11001241/) | 2000 | RCT (double-blind, placebo-controlled) | J Clin Psychopharmacol | Pindolol augmentation of fluoxetine studied in treatment-resistant panic disorder with/without agoraphobia |
| [10362436](https://pubmed.ncbi.nlm.nih.gov/10362436/) | 1999 | RCT | J Clin Psychiatry | Once-weekly fluoxetine maintained remission in panic disorder, leveraging its long half-life |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Review (network meta-analysis, Cochrane) | Cochrane Database Syst Rev | Comparative efficacy of pharmacological treatments for panic disorder in adults |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | SSRIs (incl. fluoxetine) superior to placebo for panic disorder, agoraphobia, and associated depression |
| [14967551](https://pubmed.ncbi.nlm.nih.gov/14967551/) | 2004 | Cohort | Psychiatry Research | Factors influencing psychiatrists' treatment choices (CBT ± benzodiazepine ± fluoxetine) in panic disorder with agoraphobia |
| [22090798](https://pubmed.ncbi.nlm.nih.gov/22090798/) | 2011 | Review | Neuropsychiatr Dis Treat | Pharmacological interventions, including SSRIs, for complex agoraphobia |
| [18090457](https://pubmed.ncbi.nlm.nih.gov/18090457/) | 2007 | Naturalistic comparison study | Clin Neuropharmacol | Long-term comparison of SSRIs (incl. fluoxetine) in panic disorder tolerability and outcome |
| [3500189](https://pubmed.ncbi.nlm.nih.gov/3500189/) | 1987 | Open-label pilot study | J Clin Psychopharmacol | Early open trial: 7/16 patients with panic disorder/agoraphobia had complete cessation of panic attacks on fluoxetine |
| [1884341](https://pubmed.ncbi.nlm.nih.gov/1884341/) | 1991 | Case series | Can J Psychiatry | Two treatment-refractory panic disorder with agoraphobia cases responded to fluoxetine after failing other agents |

---

## South Africa Market Information

Fluoxetine currently has **no registered products in South Africa** (`market_status: 未上市`, `total_licenses: 0`). No dosage forms, brand names, or approved indication texts are available from the evidence pack. Any repurposing pathway would first require a SAHPRA marketing authorization (new application or import route) before local prescribing could occur.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-interaction data were queried but are not currently available in this evidence pack — DG001, Blocking severity: TFDA/SAHPRA PI warnings and contraindications could not be retrieved, which prevents a formal S1 safety pre-assessment for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (indication-level, contingent on resolving Blocking data gap)**

**Rationale:**
Agoraphobia (and the related phobic disorder / melancholia predictions) are mechanistically plausible and supported by L2-level literature evidence, including tier-1 RCTs, unlike the top-scoring but weakly-evidenced personality-disorder predictions. However, fluoxetine is **not currently registered in South Africa** and a **Blocking** data gap (DG001) prevents completion of the mandatory S1 safety pre-assessment — so this candidate cannot advance past guarded research status until that gap is closed.

**To proceed, the following is needed:**
- Retrieve SAHPRA/TFDA-approved Professional Information (PI) — warnings, contraindications, DDI — to close DG001 (Blocking)
- Retrieve fluoxetine's mechanism of action via DrugBank API to close DG002 (High) and strengthen the mechanistic rationale
- Confirm a SAHPRA registration or import pathway, since the product currently has zero local licenses
- If pursuing agoraphobia specifically, commission or identify a registered clinical trial (none currently exist) rather than relying solely on published literature
- Clarify whether "manic bipolar affective disorder" (rank 7) should be down-weighted or excluded given the known risk of SSRI-induced manic switch — this is a case where a high TxGNN score does not track clinical appropriateness
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

