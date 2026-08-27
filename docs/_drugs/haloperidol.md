---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Schizophrenia/Psychotic Disorders to Manic Bipolar Affective Disorder

> **Note on scope:** This evidence pack lists 10 TxGNN-predicted indications for haloperidol. Nine of the ten — including the single highest-scoring prediction ("congenital disorder of glycosylation with defective fucosylation") — have **zero** supporting clinical trials or literature and are flagged in the source data as Evidence Level L5 / Hold. Only the 10th-ranked prediction, **Manic Bipolar Affective Disorder**, is backed by real trial and publication evidence (Evidence Level L1). This report focuses on that indication, as it is the only one with clinical substance to evaluate.

## One-Sentence Summary

Haloperidol is a first-generation (typical) D2 dopamine receptor antagonist, historically used in psychotic disorders; formal SAHPRA-registered indication text is not available in this evidence pack. The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, a prediction that is unusually well-supported for this drug — **9 clinical trials** (three of them Phase 3, completed, with haloperidol as an active comparator) and **20 publications** are on record.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no SAHPRA licence records in evidence pack); per known pharmacology, haloperidol is a typical antipsychotic used for psychotic disorders |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed (per evidence pack) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available as a structured field (marked as a Data Gap in the evidence pack). However, the evidence pack's own rationale analysis identifies haloperidol as a classic D2 dopamine receptor antagonist that suppresses excess mesolimbic dopaminergic activity — one of the core pathophysiological mechanisms implicated in acute mania.

Unlike most of the other TxGNN-predicted indications for this drug (which involve rare congenital, ophthalmologic, or neurodevelopmental conditions with no plausible mechanistic link to dopamine antagonism), mania and psychosis share overlapping neurochemical pathways. Haloperidol is already established in real-world psychiatric practice as an active comparator and adjunct in acute manic episodes of bipolar I disorder — this is therefore less a novel repurposing hypothesis and more a consolidation of existing clinical evidence into a formal indication assessment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs. placebo vs. haloperidol in manic episodes of bipolar I disorder; haloperidol used as active comparator over 12 weeks |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and haloperidol-controlled trial of olanzapine in manic/mixed bipolar I episodes; haloperidol as active comparator |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs. placebo vs. haloperidol as add-on therapy to mood stabilizers in manic bipolar disorder |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs. placebo in acute mania; haloperidol's specific role as comparator arm needs confirmation |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic plus adherence-focused behavioural programme for chronic psychotic disorders (Tanzania); mania included but population/setting is specific |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-amisulpride vs. valproate-haloperidol in bipolar I manic episode; haloperidol arm not the primary focus of the title |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs. conventional antipsychotics (incl. haloperidol) in acute mania (Sweden); terminated early, small sample |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient/fish-oil supplementation as adjunct in bipolar disorder; not directly evaluating haloperidol |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure and maternal/infant outcomes; not an efficacy trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomized, double-blind, placebo- and haloperidol-controlled trial of olanzapine in Japanese patients with manic/mixed bipolar I episodes |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Double-blind controlled trial of lithium plus haloperidol vs. placebo plus haloperidol in excited schizoaffective disorder |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | Journal of Clinical Psychiatry | Double-blind controlled comparison of clonazepam vs. lithium and vs. haloperidol in acute mania |
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Review (network meta-analysis) | Molecular Psychiatry | Systematic review/NMA of RCTs for acute bipolar mania, comparing efficacy, tolerability and safety across agents including haloperidol |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatrica Scandinavica | Evidence-based treatment recommendations for acute manic episodes, covering mood stabilizer and antipsychotic choice |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Refractory bipolar disorder review; notes adding haloperidol, risperidone, olanzapine, quetiapine, or aripiprazole to partial responders |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Observational/mechanistic | Neuropsychobiology | Lithium and haloperidol treatment differentially affect leukocyte Gαs protein levels in bipolar affective disorder |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic review | Journal of Clinical Psychopharmacology | Antipsychotic-induced extrapyramidal side effects in bipolar disorder and schizophrenia — safety-relevant comparison |
| [39756485](https://pubmed.ncbi.nlm.nih.gov/39756485/) | 2025 | Retrospective cohort | Journal of Affective Disorders | Real-world analysis of long-acting injectable antipsychotics added during manic episodes and effect on rehospitalization |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Review | BMJ Mental Health | Comparison of antipsychotic dose equivalents between acute mania and schizophrenia |

## South Africa Market Information

The evidence pack shows **0 SAHPRA product registrations** and a market status of "Not Marketed" for haloperidol. This is unusual for a long-established, widely used generic antipsychotic and should be treated as a data gap rather than confirmed absence from the South African market — it needs direct verification against the current SAHPRA product register before this factors into any decision.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-interaction data were all returned as data gaps or "not found" in this evidence pack — this is logged as a Blocking gap (DG001) that must be closed before any safety assessment.)*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 RCTs use haloperidol as an active comparator in acute manic episodes of bipolar I disorder, consistent with its established D2-antagonist mechanism — this is corroborating existing practice more than a speculative new hypothesis. However, the complete absence of SAHPRA safety/labelling data and an apparently contradictory "not marketed" status mean this cannot move to Go without closing those gaps.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI): key warnings, contraindications (currently Blocking gap DG001)
- Confirmation of haloperidol's actual SAHPRA registration/market status in South Africa (data shows 0 licences, which needs verification)
- Formal mechanism-of-action documentation from DrugBank (currently High-severity gap DG002)
- A re-run drug-drug interaction query (current query returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

