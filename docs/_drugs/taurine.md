---
layout: default
title: Taurine
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Taurine
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

# Taurine: From No Established Indication to Alcohol Withdrawal Delirium

## One-Sentence Summary

Taurine is a naturally occurring sulfonic amino acid; no original approved indication or SAHPRA registration is on file for this evaluation. The TxGNN model predicts a possible new role in **Alcohol Withdrawal Delirium**, but the supporting evidence base currently consists of **1 indirectly relevant clinical trial** (not testing taurine itself) and **7 publications** on alcohol-dependence pharmacotherapy in general — direct taurine-specific clinical evidence for this indication is not yet available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established (no registered indication or market history on file) |
| Predicted New Indication | Alcohol Withdrawal Delirium |
| TxGNN Prediction Score | 93.07% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for taurine is not currently available in this dataset. Based on general pharmacological knowledge, taurine is an endogenous amino acid with proposed GABAergic and glycinergic neuromodulatory activity, membrane-stabilizing effects, and calcium-flux regulation — properties that are theoretically consistent with dampening the central nervous system hyperexcitability seen in alcohol withdrawal (including delirium tremens).

However, none of the retrieved clinical trials or literature actually test taurine in this indication. The single clinical trial identified (NCT00855699) is a Phase 4 feasibility study comparing existing benzodiazepine detoxification regimens in primary care — it does not involve taurine as an intervention (reviewer relevance grade: C, disease-area match only). The literature set similarly consists of reviews and studies on approved alcohol-dependence/withdrawal agents (benzodiazepines, acamprosate, disulfiram), with taurine appearing only as a conceptual/mechanistic analogy, not as a studied agent.

In short, the TxGNN signal here rests on plausible mechanistic reasoning rather than direct experimental or clinical support, which is why the evidence level is capped at L4 (preclinical/mechanistic) despite the high prediction score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855699](https://clinicaltrials.gov/study/NCT00855699) | Phase 4 | Completed | 36 | Feasibility study (ADEPT) comparing pharmacological regimens for alcohol detoxification in UK primary care; does **not** evaluate taurine — included only for disease-area overlap. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2085344](https://pubmed.ncbi.nlm.nih.gov/2085344/) | 1990 | RCT (acamprosate, non-taurine) | Alcohol and Alcoholism | Double-blind placebo-controlled trial of acamprosate (a taurine-related calcium acetylhomotaurinate compound) reducing relapse indicators post-withdrawal; taurine itself not tested. |
| [26314552](https://pubmed.ncbi.nlm.nih.gov/26314552/) | 2016 | Review | European Addiction Research | Descriptive review of approved alcohol dependence/withdrawal medications, noting under-representation of women in trials. |
| [26394517](https://pubmed.ncbi.nlm.nih.gov/26394517/) | 2015 | Review | Nihon Rinsho | Review of pharmacological therapies for alcohol use disorder and withdrawal delirium in Japan. |
| [18281128](https://pubmed.ncbi.nlm.nih.gov/18281128/) | 2008 | Review | La Revue de Medecine Interne | General review of alcohol dependence diagnosis and treatment. |
| [14679678](https://pubmed.ncbi.nlm.nih.gov/14679678/) | 2003 | Review | Therapie | Retrospective study of acamprosate-induced adverse drug reactions during alcohol abstinence treatment. |
| [9411716](https://pubmed.ncbi.nlm.nih.gov/9411716/) | 1997 | Review | Schweizerische Medizinische Wochenschrift | Overview of pharmacotherapy classes for alcoholism (withdrawal agents, aversive agents, craving-reduction agents). |
| [8865961](https://pubmed.ncbi.nlm.nih.gov/8865961/) | 1996 | Review | Alcoholism, Clinical and Experimental Research | Review of pharmacotherapies for alcohol problems, focused on withdrawal agents and opiate antagonists. |

*Note: none of the above studies administer or evaluate taurine directly; they are included because TxGNN's disease-area match returned them as the closest available literature.*

## South Africa Market Information

Taurine currently has **no SAHPRA registration** and **no recorded market history** in this dataset (market status: Not Marketed, 0 licenses on file). No registered product, dosage form, or approved indication text is available for review.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-drug interaction data are not currently available for taurine in this dataset — this is flagged as a Blocking data gap, see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but supporting evidence is indirect (no taurine-specific trials or publications) and evidence level is capped at L4. More critically, safety/PI data (warnings, contraindications) is completely absent, which is a **Blocking** gap that prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent Professional Information (warnings, contraindications) — currently blocking
- Mechanism of action (MOA) confirmation from DrugBank or primary pharmacology sources
- Taurine-specific preclinical or clinical data in alcohol withdrawal/delirium (current evidence only covers other agents)
- Dosing and route-of-administration feasibility for an acute withdrawal setting

**Additional note:** Among the other candidates in this evidence pack, *migraine disorder* (rank 6, score 89.2%) has notably stronger literature support (L3, multiple cohort studies on taurine levels in migraine patients, decision stage S1 "Research Question") and may warrant separate, prioritized evaluation ahead of alcohol withdrawal delirium.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

