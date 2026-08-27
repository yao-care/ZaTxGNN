---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

# Tiotropium: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

Tiotropium is a long-acting muscarinic antagonist (LAMA) whose established global use is maintenance bronchodilator therapy for chronic obstructive pulmonary disease (COPD). The TxGNN model's top prediction, **Obstructive Lung Disease**, is essentially an upper-level ontology term for this same disease space rather than a genuinely new therapeutic target — it is supported by **89 clinical trials** and **20 publications** in this evidence pack, including multiple completed Phase 3 RCTs. Critically, tiotropium is **not currently registered with SAHPRA** and has **zero market authorizations** in South Africa, and key Professional Information safety data is flagged as a **Blocking data gap**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD) — internationally established maintenance bronchodilator indication; not captured in the SAHPRA licensing data because the product currently holds no South African registration |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The evidence pack flags detailed mechanism-of-action data as a High-severity data gap (DG002). However, the pipeline's own mechanistic analysis (attached to the closely related "chronic obstructive pulmonary disease" prediction, rank 5) already documents the pharmacology: tiotropium is a long-acting muscarinic (M1/M3) receptor antagonist that blocks acetylcholine-mediated bronchial smooth muscle contraction, producing sustained bronchodilation. This is described as the *"core, already fully validated mechanism for COPD treatment — a direct relationship, not a speculative association."*

The relationship between the "original" and "predicted new" indication in this case is unusual: the model's own rationale for rank 1 states that **"Obstructive Lung Disease" is an upper-level/parent concept term for COPD and airway obstructive disease**, and that this candidate represents *"an extension of an already-approved mechanism naming, not a novel prediction."* This is corroborated by the fact that "chronic obstructive pulmonary disease" itself appears independently at rank 5 with an almost identical score (99.87%), the same L1 evidence level, and the same "Proceed with Guardrails" stage.

Because both predictions sit within tiotropium's already-approved disease space, the mechanism is directly and extensively validated — including landmark trials such as the NEJM early-stage COPD study and multiple Cochrane systematic reviews. In practical terms, this evidence pack should be read as **confirming tiotropium's established utility in obstructive airway disease**, not as surfacing a novel repurposing signal. For context, the model also generated several structurally or genetically implausible predictions for this drug (e.g., respiratory malformation, Rienhoff syndrome, tracheal stenosis, CD8α-deficiency-related infection susceptibility) — all scored L5 with a "Hold" recommendation, as none have a plausible mechanistic link to smooth-muscle bronchodilation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00776984](https://clinicaltrials.gov/study/NCT00776984) | Phase 3 | Completed | 453 | Placebo-controlled trial of tiotropium Respimat (5 mcg/day) as add-on controller therapy over 48 weeks in severe persistent asthma — Grade A relevance |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | Completed | 872 | GSK573719/GW642444 vs GSK573719 vs tiotropium over 24 weeks in COPD — large registrational-quality comparator trial, Grade A relevance |
| [NCT00277264](https://clinicaltrials.gov/study/NCT00277264) | Phase 3 | Completed | 914 | SAFE study — one-year effect of 18 mcg tiotropium once daily on trough FEV1 vs placebo in COPD |
| [NCT00144339](https://clinicaltrials.gov/study/NCT00144339) | Phase 3 | Completed | 5,993 | Large RCT assessing whether tiotropium slows the rate of lung-function decline in COPD |
| [NCT00523991](https://clinicaltrials.gov/study/NCT00523991) | Phase 4 | Completed | 457 | 24-week RCT of tiotropium + PRN albuterol vs placebo + PRN albuterol in maintenance-naïve COPD patients |
| [NCT01012765](https://clinicaltrials.gov/study/NCT01012765) | Phase 3 | Completed | 173 | Crossover study using open-label tiotropium as active control vs indacaterol/placebo in moderate COPD |
| [NCT01112241](https://clinicaltrials.gov/study/NCT01112241) | Phase 4 | Completed | 17 | Bronchodilator responsiveness to tiotropium in obliterative bronchiolitis post-HSCT — Grade B relevance (obstructive-disease subgroup) |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | Terminated | 80 | Intermittent tiotropium vs fluticasone vs salbutamol alone for episode-free days in early childhood recurrent wheeze |
| [NCT00515502](https://clinicaltrials.gov/study/NCT00515502) | Phase 2 | Completed | 24 | Dose-ascending safety/PK/PD study of GSK573719 using tiotropium 18 mcg as active comparator in COPD |
| [NCT00279019](https://clinicaltrials.gov/study/NCT00279019) | Phase 1 | Completed | 31 | Safety/PK/PD comparison of GSK233705 vs tiotropium bromide in COPD patients |

*79 additional trials are recorded in the underlying evidence pack (SANCTR/PACTR identifiers were not present in the source data).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | The New England Journal of Medicine | Long-term tiotropium improves lung function and slows decline in mild/moderate, early-stage COPD |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review confirming efficacy of tiotropium vs placebo across COPD symptom, exacerbation, and lung-function outcomes |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Comparative review of tiotropium vs ipratropium bromide in stable COPD |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respiratory Research | Overview of tiotropium's clinical development program supporting LAMA monotherapy as GOLD-recommended initial COPD treatment |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | Establishes tiotropium's pharmacology (M1/M2/M3 antagonism) and clinical profile improving lung function vs placebo/ipratropium in COPD |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | Review | Life Sciences | Mechanistic and clinical profile of tiotropium (Spiriva) as first-line bronchodilator in obstructive lung disease |
| [11281822](https://pubmed.ncbi.nlm.nih.gov/11281822/) | 2001 | Review | Expert Opinion on Investigational Drugs | Early clinical pharmacology review describing prolonged bronchodilator effect of tiotropium in Phase 2 studies |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Current Medical Research and Opinion | Evidence review of tiotropium + olodaterol fixed-dose combination per GOLD 2020 recommendations for reducing COPD exacerbations |
| [29206658](https://pubmed.ncbi.nlm.nih.gov/29206658/) | 2018 | Review | Current Opinion in Pulmonary Medicine | Review of lung-function trajectories in COPD, including pharmacologic intervention effects in early disease phases |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | The Annals of Pharmacotherapy | Review of efficacy/safety data for concomitant ipratropium and tiotropium use in COPD |

---

## South Africa Market Information

Tiotropium currently holds **no SAHPRA registration** — the evidence pack records 0 licenses and a market status of "Not Marketed." There is no existing South African product, dosage form, or approved-indication text to summarize at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: this evaluation flags TFDA/SAHPRA-equivalent label warnings and contraindications as a **Blocking data gap (DG001)** — retrieval and parsing of the official Professional Information is required before this candidate can enter the S1 safety screening stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and clinical-trial/literature evidence base for tiotropium in obstructive airway disease is extensive and mature (L1, multiple completed Phase 3 RCTs plus Cochrane-level systematic reviews). However, this candidate is best understood as **confirming an already-established indication** rather than a novel repurposing discovery, and two structural blockers remain: the drug is **not currently registered with SAHPRA** (0 licenses), and label-level safety data (warnings/contraindications) is a documented **Blocking gap**. "Proceeding with guardrails" here should be read as proceeding toward a standard registration/importation review, not a research-validation pathway.

**To proceed, the following is needed:**
- Retrieval and parsing of the SAHPRA/manufacturer Professional Information (PI) to close the Blocking safety data gap (DG001)
- Formal documentation of mechanism of action from DrugBank or equivalent source to close the High-severity MOA gap (DG002)
- A SAHPRA registration/import pathway assessment, since the product currently has zero South African market authorization
- Clarification of route/formulation availability (inhaled capsule vs. Respimat soft-mist) suitable for the South African market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

