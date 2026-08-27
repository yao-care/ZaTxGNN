---
layout: default
title: Pramipexole
parent: 僅模型預測 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Pramipexole
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

# Pramipexole: From Parkinson's Disease/Restless Legs Syndrome to Schizophrenia (Adjunctive Therapy)

## One-Sentence Summary

Pramipexole is a D2/D3 dopamine receptor agonist established internationally for Parkinson's disease and restless legs syndrome. Among the 10 new indications TxGNN predicted for this drug, **Schizophrenia** (as an adjunctive therapy) is the one with the strongest actual supporting evidence — **4 clinical trials** and **20 publications**, including a completed 200-patient randomized controlled trial and a systematic review/meta-analysis. Note: TxGNN's single highest-scoring prediction was attention-deficit/hyperactivity disorder (ADHD), but it is not used as the headline indication here because the evidence pack's own mechanistic analysis flags it as weak, indirect, and possibly wrong-direction (evidence level L4, recommendation "Hold") — see the note at the end of the next section.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied regulatory data (SAHPRA/TFDA license fields are empty). Trial and literature context in this evidence pack indicate established use in Parkinson's disease and restless legs syndrome. |
| Predicted New Indication | Schizophrenia (adjunctive to antipsychotics) |
| TxGNN Prediction Score | 99.52% (graph rank #2,814) |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Pramipexole's mechanism of action is marked as a data gap in the formal regulatory record, but the literature evidence in this pack independently documents it: pramipexole is a non-ergoline **D2/D3 dopamine receptor agonist with D3 selectivity**, used to restore dopaminergic tone in Parkinson's disease and to relieve restless legs syndrome (see PMID 9088887, PMID 11829733, PMID 19412489).

At first glance, a dopamine *agonist* being predicted for schizophrenia looks paradoxical — antipsychotics work by *blocking* D2 receptors, since excess mesolimbic dopaminergic signaling drives positive symptoms. The evidence pack's clinical trial and literature record clarifies that this is not the mechanism being proposed. Instead, the signal converges on a narrower, coherent niche: (1) **negative symptoms**, which are associated with prefrontal dopaminergic *hypofunction* — a state where added D3-preferring agonism may help (supported by a systematic review/meta-analysis, PMID 31688399); and (2) **antipsychotic-induced extrapyramidal symptoms (EPS) and hyperprolactinemia**, which arise from D2 blockade in the nigrostriatal and tuberoinfundibular pathways — the same pathways pramipexole already treats in Parkinson's disease (NCT03430596, PMID 21364336). This "adjunct for side effects and negative symptoms" framing, rather than "replacement for antipsychotics," is mechanistically defensible and is exactly what the strongest trials (a completed 200-patient RCT, PMID 35921506) tested.

**Note on the top-ranked TxGNN prediction (ADHD):** ADHD scored highest by raw TxGNN probability (99.998%), but the pack's own relevance grading and rationale rate this signal as weak — the only clinical trial is graded "C" (unrelated topic, Parkinson's reward signaling), and the 9 literature hits are mostly case reports, reviews of unrelated conditions (restless legs syndrome, Tourette's), or incidental drug mentions. The rationale explicitly notes the mechanistic direction may be reversed (D2/D3 autoreceptor feedback can *reduce* dopamine release at low doses, opposite to stimulant-based ADHD treatment). Given this, ADHD is not a credible candidate for clinical decision-making and is excluded from the headline of this report.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01320982](https://clinicaltrials.gov/study/NCT01320982) | Phase 3 | Unknown | 400 | Randomized trial of pramipexole, minocycline, or aspirin as add-on to antipsychotics vs. placebo in schizophrenia/schizoaffective disorder; outcome status not confirmed. |
| [NCT03430596](https://clinicaltrials.gov/study/NCT03430596) | Early Phase 1 | Completed | 50 | Pilot study of pramipexole for antipsychotic-induced extrapyramidal symptoms; two-stage design, randomized/rater-blinded second stage. |
| [NCT02397837](https://clinicaltrials.gov/study/NCT02397837) | Phase 4 | Completed | 103 | Pramipexole for persistent neurocognitive deficits in bipolar disorder (related psychiatric population, not schizophrenia itself). |
| [NCT01066897](https://clinicaltrials.gov/study/NCT01066897) | Phase 4 | Terminated | 16 | Imaging nucleus accumbens response to pramipexole in major depression; terminated early, low evidentiary weight. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35921506](https://pubmed.ncbi.nlm.nih.gov/35921506/) | 2022 | RCT | J Clin Psychiatry | 16-week, multicenter, double-blind, placebo-controlled trial (n=200) of add-on pramipexole for schizophrenia/schizoaffective disorder. |
| [31496702](https://pubmed.ncbi.nlm.nih.gov/31496702/) | 2019 | RCT | Neuropsychiatric Disease and Treatment | Stage-1 open-label pilot testing low-dose pramipexole (0.375–0.75 mg/day) for antipsychotic-induced EPS and schizophrenia symptoms. |
| [31688399](https://pubmed.ncbi.nlm.nih.gov/31688399/) | 2019 | Systematic Review/Meta-analysis | J Clin Psychopharmacol | Prodopaminergic drugs (including pramipexole) for negative symptoms of schizophrenia — systematic review and meta-analysis of RCTs. |
| [9088887](https://pubmed.ncbi.nlm.nih.gov/9088887/) | 1997 | RCT | Eur Neuropsychopharmacol | Pramipexole as adjunct to haloperidol (n=15): PANSS reduction >20% in 9/15 patients, no serious adverse events. |
| [22182458](https://pubmed.ncbi.nlm.nih.gov/22182458/) | 2012 | Review | Clin Schizophr Relat Psychoses | Reviews repurposed adjunct drugs for schizophrenia/bipolar disorder, including pramipexole. |
| [8775758](https://pubmed.ncbi.nlm.nih.gov/8775758/) | 1995 | Review | Eur Neuropsychopharmacol | Review of dopamine agonists in schizophrenia and the autoreceptor feedback hypothesis. |
| [21364336](https://pubmed.ncbi.nlm.nih.gov/21364336/) | 2011 | Trial | J Clin Psychopharmacol | Low-dose adjunctive pramipexole for risperidone-associated hyperprolactinemia and sexual dysfunction. |
| [34061895](https://pubmed.ncbi.nlm.nih.gov/34061895/) | 2021 | Cohort | PLoS One | Swedish nationwide register study: increased gambling disorder risk with pramipexole, ropinirole, and aripiprazole — safety signal. |
| [11829733](https://pubmed.ncbi.nlm.nih.gov/11829733/) | 2002 | Review | Expert Opin Pharmacother | Review of pramipexole's clinical utility in Parkinson's disease (background/mechanism context). |
| [31877244](https://pubmed.ncbi.nlm.nih.gov/31877244/) | 2019 | Case Report | Prim Care Companion CNS Disord | Case of schizophrenia decompensation on clozapine plus pramipexole — negative safety signal. |

## South Africa Market Information

Pramipexole has **0 SAHPRA registrations** and is currently **not marketed** in South Africa. No product license, brand name, dosage form, or approved indication text is available in the supplied regulatory data. Any clinical use would currently require an alternate access route (e.g., Section 21 named-patient authorization) rather than routine prescribing.

## Safety Considerations

Formal safety data (key warnings, contraindications, drug–drug interactions) are not available in the supplied dataset. Please refer to the SAHPRA-approved Professional Information (PI) for safety information, and report adverse drug reactions to SAHPRA.

**Evidence-derived caution (from literature, not official PI/DDI data):** A Swedish nationwide register study (PMID 34061895) found increased risk of gambling disorder and other impulse-control disorders with pramipexole. Given pramipexole's dopamine-agonist mechanism, this signal is biologically plausible and should be factored into any monitoring plan for psychiatric use.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tier-1 evidence (a completed 200-patient RCT and a systematic review/meta-analysis) supports pramipexole as adjunctive therapy for negative symptoms and antipsychotic-induced EPS/hyperprolactinemia in schizophrenia. However, the drug has no SAHPRA registration in South Africa, one key Phase 3 add-on trial (NCT01320982, n=400) has unknown/unreported outcomes, and literature flags an impulse-control disorder safety signal — together these warrant a guarded, monitored approach rather than routine adoption.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) or regulatory dossier, including formal warnings, contraindications, and DDI data (currently a data gap)
- Documented mechanism of action source (DrugBank/SmPC) for the local regulatory submission
- Follow-up on the outcome/publication status of NCT01320982 to confirm the Phase 3 add-on efficacy signal
- Local access-pathway assessment (Section 21 named-patient use, or a new registration application), given "Not Marketed" status
- A structured impulse-control disorder monitoring protocol for any patient started on adjunctive pramipexole
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

