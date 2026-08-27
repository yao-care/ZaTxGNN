---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

Using the drug-repurposing report template directly — this is a content-generation task, not code, and the prompt already supplies the full spec, so no additional skill is needed.

One judgment call before drafting: `predicted_indications[0]` (trigeminal nerve neoplasm, score 99.97%) is explicitly flagged in its own `repurposing_rationale` as a likely knowledge-graph artifact (TxGNN confusing "trigeminal neuralgia" with "trigeminal nerve neoplasm" nodes) — zero clinical trials, only two tangentially related papers, `L5`/`Hold`. Reporting that as the headline finding would be misleading. Rank 2, **trigeminal neuralgia** (99.89%), has real supporting evidence (4 trials including a completed Phase 2/3 head-to-head vs. carbamazepine, 19 publications including an EAN clinical guideline, `L2`/`Proceed with Guardrails`) — that's the clinically meaningful signal, so the report is built around it.

---

# Lamotrigine: From Epilepsy/Bipolar Disorder to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is a well-established antiepileptic and mood-stabilising agent, approved for partial-onset seizures, Lennox-Gastaut syndrome, and maintenance treatment of Bipolar I Disorder.
The TxGNN model predicts it may also be effective for **Trigeminal Neuralgia**,
with **4 clinical trials** (including a completed Phase 2/3 head-to-head trial against carbamazepine) and **19 publications** (including a European Academy of Neurology clinical guideline) currently supporting this direction.

> **Note on the model's top-ranked prediction:** TxGNN's single highest-scoring prediction for lamotrigine was "trigeminal nerve neoplasm" (99.97%), not trigeminal neuralgia. The evidence pack's own analysis flags this as a probable knowledge-graph artefact — the model likely conflated the "trigeminal neuralgia" and "trigeminal nerve neoplasm" nodes, since the two retrieved papers discuss trigeminal neuralgia surgery and a cavernous-malformation case, not any antitumour effect of lamotrigine. No clinical trials, no evidence level above L5. It is not carried forward in this report; trigeminal neuralgia (rank 2) is the indication with an actual evidence trail.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset seizures, Lennox-Gastaut syndrome) and Bipolar I Disorder maintenance treatment *(general pharmacological knowledge — SAHPRA-specific label text not available in this evidence pack, see Data Gaps)* |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed (per evidence pack) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text was not returned for this candidate (data gap). Based on known pharmacology, lamotrigine is a voltage-gated sodium-channel blocker that stabilises presynaptic neuronal membranes, reduces glutamate release, and dampens repetitive high-frequency neuronal firing — the same broad mechanism that underlies its efficacy as an antiepileptic and mood stabiliser.

Trigeminal neuralgia is itself a paroxysmal, high-frequency neuronal discharge disorder of the trigeminal nerve root, most often triggered by focal demyelination from neurovascular compression. Its first-line treatment, carbamazepine, works through the same voltage-gated sodium-channel mechanism as lamotrigine. This shared mechanistic basis — rather than a repurposing leap across unrelated disease biology — is why the prediction is plausible and why lamotrigine already has real-world clinical use here.

This is reflected in the evidence: the European Academy of Neurology's 2019 guideline on trigeminal neuralgia already lists lamotrigine as a second-line/adjunctive agent, and a completed Phase 2/3 trial (NCT00913107, n=21) directly compared lamotrigine against carbamazepine for efficacy and safety. Most of lamotrigine's other TxGNN-predicted "new" indications (audiogenic seizures, startle epilepsy, reading seizures, eating seizures, orgasm-induced seizures, etc.) are reflex-epilepsy subtypes clustered near lamotrigine's existing antiepileptic indication in the knowledge graph — they represent proximity to an already-approved use rather than genuine novel repurposing, and evidence for them ranges from thin (case reports) to essentially absent (orgasm-induced seizures: zero trials, zero literature).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (lamotrigine) in adults with trigeminal neuralgia, assessing safety and reduction in attack frequency. |
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head comparison of lamotrigine vs. carbamazepine for efficacy and safety in trigeminal neuralgia — direct evidence for this indication. |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study evaluating the central mechanism of lamotrigine's effect on neuropathic facial pain/neuralgia. |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Compares carbamazepine vs. oxcarbazepine in trigeminal neuralgia; does not test lamotrigine directly — background context only. |

No SANCTR or PACTR-registered trials were identified for this indication in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative study | Journal of the Chinese Medical Association | Direct evaluation of lamotrigine efficacy and side-effect profile vs. carbamazepine in trigeminal neuralgia patients. |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | European Academy of Neurology guideline on trigeminal neuralgia management, including lamotrigine as a treatment option. |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drug therapies for trigeminal neuralgia, comparing efficacy and side effects across agents. |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical guide to diagnosis and medical/surgical management of trigeminal neuralgia. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of trigeminal neuralgia pathophysiology and pharmacological treatment rationale. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Update on pharmacotherapy for trigeminal neuralgia, contextualising newer agents against carbamazepine/oxcarbazepine. |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Multiple Sclerosis and Related Disorders | Refractory trigeminal neuralgia in an MS patient successfully treated with pregabalin + lamotrigine combination therapy. |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Cohort | Pain | Nationwide Danish disease-trajectory study of comorbidities associated with trigeminal neuralgia. |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | Review | Asian Journal of Neurosurgery | General overview of trigeminal neuralgia pathophysiology and management. |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clinical Evidence | Evidence review of trigeminal neuralgia diagnosis and treatment options. |

---

## South Africa Market Information

No SAHPRA product registrations for lamotrigine are on file in this evidence pack (`total_licenses: 0`, `market_status: 未上市 / Not marketed`). This is inconsistent with lamotrigine's broad international availability (e.g., as Lamictal) and should be treated as a data gap requiring direct SAHPRA verification, not confirmation of true non-availability — see Conclusion below.

---

## Safety Considerations

A **Blocking** data gap (DG001) applies: TFDA/SAHPRA-approved warnings and contraindications for lamotrigine were not retrievable in this evidence pack, and the safety fields (`key_warnings`, `contraindications`, `ddi`) all returned no data. This gap blocks progression to the S1 safety-review stage.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information — lamotrigine carries well-known class warnings (notably serious/life-threatening skin reactions such as Stevens-Johnson syndrome) that must be confirmed from the official PI before any prescribing decision. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Trigeminal neuralgia has a mechanistically coherent rationale, a completed Phase 2/3 head-to-head trial, and guideline-level recognition (EAN 2019) as a second-line/adjunctive use for lamotrigine — meaningfully stronger evidence than a single-study/off-label signal. However, this evidence exists despite, not because of, this evidence pack's regulatory data, which shows lamotrigine as unregistered in South Africa and is missing all PI-level safety data (Blocking gap DG001).

**To proceed, the following is needed:**
- Direct SAHPRA registration lookup to confirm whether lamotrigine/Lamictal is genuinely unregistered in South Africa or whether this is a data-collection gap
- TFDA/SAHPRA-approved Professional Information (PI) — warnings, contraindications, and DDI profile — to complete the S1 safety assessment
- DrugBank-sourced mechanism-of-action confirmation (DG002)
- If pursued clinically: local prescribing guidance for off-label use in trigeminal neuralgia, given the small sample sizes (n=20–21) in the supporting trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

