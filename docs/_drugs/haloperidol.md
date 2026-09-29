---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Antipsychotic Use to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is an oral antipsychotic that acts by blocking dopamine D2 receptors, and three tablet products are registered in South Africa. The TxGNN model's top-ranked prediction is **congenital disorder of glycosylation with defective fucosylation**, but there are **0 clinical trials** and **0 publications** for it, so it is a model output only. Of the ten predicted indications, only **manic bipolar affective disorder** has real evidence (**9 clinical trials** and **20 publications**), and that use is already established practice.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record; the mechanism (D2 antagonist antipsychotic) is general pharmacology |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation (rank 1) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not well supported. Detailed mechanism of action data is not available in the supplied record. From general pharmacology, haloperidol is a dopamine D2 receptor antagonist. No biological rationale links D2 blockade to fucosylation defects, so the score of 0.9991 looks like a graph-proximity artefact rather than a pharmacological signal.

The same holds for most of the other predictions. They are congenital or genetic conditions (X-linked myopia, hydranencephaly, Charcot-Marie-Tooth type 1G, polymicrogyria syndromes and others) with no trials and no relevant literature. The retrieved papers for rank 2 (retinal dystrophy) concern congenital eye and orbit anomalies and do not involve haloperidol.

The exception is rank 10, **manic bipolar affective disorder** (score 99.83%). Blocking D2 receptors plausibly dampens the dopaminergic hyperactivity and psychomotor agitation of acute mania. This use is already established in clinical practice, so it validates the model more than it offers a new repurposing finding. This link is inferred from general pharmacology, not from the supplied record.

## Clinical Trial Evidence

The rank-1 prediction has no registered trials. The table below covers rank 10 (manic bipolar affective disorder). In most of these trials haloperidol is the active comparator, not the investigational drug.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs placebo or haloperidol in acute mania (bipolar I); haloperidol as active comparator over 12 weeks |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Olanzapine vs placebo and haloperidol in manic or mixed episodes of bipolar I |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs placebo vs haloperidol as add-on to mood stabilisers in mania |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-amisulpride vs valproate-haloperidol in bipolar I mania over 3 months |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole vs placebo in acute mania; no haloperidol arm, contextual only |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Open-label olanzapine vs conventional antipsychotics in acute mania in Sweden; underpowered |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotic plus adherence programme in chronic psychosis in Tanzania; tangential |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study of antenatal antipsychotic exposure and infant development; not efficacy evidence |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient adjunct in bipolar disorder; no haloperidol |

## Literature Evidence

The rank-1 prediction has no publications. The table below covers rank 10, prioritising systematic reviews, RCTs and reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic review / network meta-analysis | Mol Psychiatry | Compares efficacy, tolerability and safety of drugs for acute bipolar mania across double-blind RCTs |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | J Affect Disord | Olanzapine vs placebo and haloperidol in Japanese patients with bipolar I manic or mixed episodes |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | Controlled studies | J Clin Psychiatry | Clonazepam compared with lithium and with haloperidol in acute mania |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | Controlled trial | Arch Gen Psychiatry | Lithium plus haloperidol vs placebo plus haloperidol in excited schizo-affective patients (18 per group); modest but significant benefit |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Comparative analysis | BMJ Ment Health | Compares antipsychotic dose equivalents between acute mania and schizophrenia |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based options for managing a manic episode, including choice of antipsychotic |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neurosci Ther | In partial responders to lithium, valproate or carbamazepine, adding haloperidol or other antipsychotics is a strategy |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic review | J Clin Psychopharmacol | Antipsychotic-induced extrapyramidal side effects in bipolar disorder and schizophrenia |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | Systematic review / economic evaluation | Health Technol Assess | Clinical and cost-effectiveness of newer drugs for mania |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Clinical study | Neuropsychobiology | Lithium and haloperidol affect leukocyte Galphas protein levels differently in bipolar disorder |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/2.6.5/170 | Haloperidol 5 oethmaan | Tablet | Not stated in the record |
| Q/2.6.5/170 | Sandoz Haloperidol 5 | Tablet | Not stated in the record |
| Q/2.6.5/169 | Haloperidol 1.5 oethmaan | Tablet | Not stated in the record |

All three registrations are oral tablets. The record has no manufacturer, approved indication text or Essential Medicines List (EML) status.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (congenital disorder of glycosylation with defective fucosylation) has no trials, no literature and no plausible mechanism, so it should not be pursued. Only manic bipolar affective disorder has substantial evidence (L1, several Phase 3 RCTs), but that is existing practice, not new repurposing, and haloperidol is mostly the comparator in those trials.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which block any safety screening
- Approved indication text from the SAHPRA registrations
- Mechanism of action data, for example from the DrugBank API
- If manic bipolar disorder is to be reviewed as a separate indication, a check of local guidelines and the registered indications, since the record does not show whether it is already labelled

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

