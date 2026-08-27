---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial-Onset Seizures to Status Epilepticus

## One-Sentence Summary

> Levetiracetam is an established antiepileptic medication, widely used for partial-onset and generalized seizures. The TxGNN model predicts it may be effective for **Status Epilepticus**, and this is already the strongest-supported prediction in this evidence pack — backed by **26 clinical trials** (including a landmark multicentre Phase 3 RCT) and **20 publications**, several of which are randomized controlled trials and network meta-analyses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial-onset seizures (adjunctive and monotherapy) |
| Predicted New Indication | Status Epilepticus |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L1 |
| South Africa Market Status | Not currently marketed in South Africa |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: Of the 10 TxGNN-predicted indications supplied in this evidence pack (visual epilepsy, eating seizures, orgasm-induced seizures, thinking seizures, startle epilepsy, audiogenic seizures, micturition-induced seizures, reading seizures, status epilepticus, beta-ketothiolase deficiency), status epilepticus is the only candidate reaching evidence level L1 with a "Proceed with Guardrails" recommendation. The other candidates — mostly rare reflex-epilepsy subtypes — remain at evidence level L3–L5 ("Research Question" or "Hold") due to sparse or indirect evidence, and are not the focus of this report.*

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation for levetiracetam was not available in the source data for this evaluation (DrugBank MOA field returned a data gap). However, based on well-characterized pharmacology summarized in the supporting literature, levetiracetam binds to the synaptic vesicle protein **SV2A**, modulating vesicular neurotransmitter release and reducing abnormal, synchronized neuronal discharge. This is the same broad-spectrum antiepileptic mechanism that underlies its approved use in partial-onset and generalized seizures.

Status epilepticus is a neurological emergency defined by prolonged or repetitive seizure activity failing normal termination mechanisms — mechanistically, an extension of the same abnormal cortical hyperexcitability and synchronization that levetiracetam already targets in chronic epilepsy. Because levetiracetam is available in an intravenous formulation with rapid onset, favorable renal (non-hepatic) clearance, and minimal drug-drug interactions, it is pharmacologically well suited for acute seizure termination in emergency and intensive care settings.

Importantly, this is not a novel mechanistic extrapolation: intravenous levetiracetam is already used internationally as a second-line/alternative first-line agent for benzodiazepine-refractory status epilepticus, most notably validated in the ESETT trial (NCT01960075, published in *Lancet* and *NEJM*). The TxGNN prediction therefore reflects and reinforces existing real-world clinical practice rather than proposing an untested mechanistic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01960075](https://clinicaltrials.gov/study/NCT01960075) | Phase 3 | Completed | 478 | ESETT trial — multicentre RCT comparing fosphenytoin, valproic acid, and levetiracetam for benzodiazepine-refractory status epilepticus |
| [NCT02920060](https://clinicaltrials.gov/study/NCT02920060) | Phase 2 | Completed | 80 | Open randomized study, levetiracetam vs sodium valproate in children with refractory generalized convulsive status epilepticus |
| [NCT01150331](https://clinicaltrials.gov/study/NCT01150331) | Phase 3 | Completed | 203 | IV levetiracetam + clonazepam vs clonazepam alone in prehospital treatment of generalized tonic-clonic status epilepticus |
| [NCT02056236](https://clinicaltrials.gov/study/NCT02056236) | N/A | Completed | 172 | TELSTAR trial — treatment of EEG-diagnosed status epilepticus after cardiopulmonary resuscitation |
| [NCT07052136](https://clinicaltrials.gov/study/NCT07052136) | N/A | Completed | 138 | Levetiracetam vs valproic acid in pediatric status epilepticus |
| [NCT04926844](https://clinicaltrials.gov/study/NCT04926844) | Phase 2 | Completed | 144 | Combined levetiracetam + midazolam vs midazolam alone in pediatric generalized convulsive status epilepticus |
| [NCT07163572](https://clinicaltrials.gov/study/NCT07163572) | N/A | Completed | 152 | IV brivaracetam vs levetiracetam in pediatric status epilepticus |
| [NCT06067412](https://clinicaltrials.gov/study/NCT06067412) | N/A | Completed | 70 | Phenytoin vs levetiracetam in pediatric status epilepticus |
| [NCT06907173](https://clinicaltrials.gov/study/NCT06907173) | Phase 3 | Recruiting | 770 | KESETT trial — ketamine + levetiracetam vs levetiracetam alone for established status epilepticus |
| [NCT07046611](https://clinicaltrials.gov/study/NCT07046611) | Phase 2/3 | Recruiting | 124 | Ketamine + levetiracetam as second-line therapy for pediatric benzodiazepine-refractory status epilepticus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31774955](https://pubmed.ncbi.nlm.nih.gov/31774955/) | 2019 | RCT | New England Journal of Medicine | ESETT — randomized trial of three anticonvulsants (levetiracetam, fosphenytoin, valproate) for benzodiazepine-refractory status epilepticus |
| [32203691](https://pubmed.ncbi.nlm.nih.gov/32203691/) | 2020 | RCT (age-group analysis) | The Lancet | Efficacy of levetiracetam, fosphenytoin, and valproate by age group in established status epilepticus (ESETT extended analysis) |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Network Meta-analysis | Seizure | Comparative effectiveness ranking of treatments for benzodiazepine-resistant status epilepticus |
| [33060105](https://pubmed.ncbi.nlm.nih.gov/33060105/) | 2021 | Systematic Review/Meta-analysis | Archives of Disease in Childhood | Levetiracetam for convulsive status epilepticus in childhood |
| [31830677](https://pubmed.ncbi.nlm.nih.gov/31830677/) | 2020 | Meta-analysis | Seizure | Efficacy and safety of intravenous levetiracetam in status epilepticus |
| [35538830](https://pubmed.ncbi.nlm.nih.gov/35538830/) | 2023 | Meta-analysis | CNS & Neurological Disorders Drug Targets | Comparison of levetiracetam and phenytoin in pediatric status epilepticus |
| [40119876](https://pubmed.ncbi.nlm.nih.gov/40119876/) | 2025 | Cohort | Epilepsia | Comparison of lacosamide, levetiracetam, and valproate as second-line therapy in a large adult status epilepticus cohort |
| [38580318](https://pubmed.ncbi.nlm.nih.gov/38580318/) | 2024 | Review | Seminars in Neurology | Update on pharmacological management of status epilepticus |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Diagnosis, monitoring and treatment of status epilepticus |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | Review | Intensive Care Medicine | Status epilepticus management in the ICU |

---

## South Africa Market Information

Levetiracetam has **no active SAHPRA registrations** recorded in the evidence pack (`total_licenses: 0`, `market_status: "未上市"` / not marketed). No product name, dosage form, or approved indication text is available for South Africa at this time. This is a key gap for repurposing feasibility: any move toward status-epilepticus use in South Africa would first require a marketed, SAHPRA-registered levetiracetam product (or an import/named-patient access pathway) before formulary or clinical-guideline adoption can proceed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(No key warnings, contraindications, or drug-interaction data were available in the source evidence pack for this evaluation — all fields returned a data gap.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Status epilepticus is supported by evidence level L1 — a landmark completed Phase 3 RCT (ESETT), multiple additional completed RCTs across adult and pediatric populations, and several published meta-analyses/network meta-analyses — making it by far the strongest candidate in this evidence pack. IV levetiracetam is already used internationally as an established second-line/alternative first-line agent for status epilepticus, so this represents formalizing existing practice rather than a speculative new use. The main constraint is regulatory: levetiracetam is not currently registered or marketed in South Africa.

**To proceed, the following is needed:**
- SAHPRA registration or import pathway for an IV levetiracetam product in South Africa
- Full Professional Information (PI) — warnings, contraindications, and drug-interaction data (currently a data gap)
- Formal DrugBank/manufacturer mechanism-of-action documentation to support a clinical guideline submission
- Local (South African) clinical guideline or emergency medicine society input on positioning levetiracetam relative to existing status epilepticus protocols (benzodiazepines, phenytoin/fosphenytoin, valproate)
- Confirmation of IV formulation supply chain and cold-chain/storage requirements for emergency department and ICU use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

