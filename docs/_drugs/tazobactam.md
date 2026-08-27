---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Tazobactam
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

# Tazobactam: From Beta-Lactamase Inhibitor (Combination Therapy) to Pneumonia

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor with no antibacterial activity on its own; it is always used in fixed combinations (e.g. Piperacillin-Tazobactam, Ceftolozane-Tazobactam) to restore the killing power of a partner beta-lactam against beta-lactamase-producing (including ESBL) bacteria.
The TxGNN model predicts continued/expanded relevance for **Pneumonia** (including hospital-acquired and ventilator-associated pneumonia),
with **57 clinical trials** and **20 publications** currently identified in this evidence pack supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No standalone indication — Tazobactam is used only as the beta-lactamase-inhibitor component of combination antibiotics (e.g. Piperacillin-Tazobactam, Ceftolozane-Tazobactam) |
| Predicted New Indication | Pneumonia (incl. hospital-acquired / ventilator-associated pneumonia) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tazobactam itself is not available. Based on known pharmacology, Tazobactam is a beta-lactamase inhibitor that has no clinically meaningful antibacterial activity alone. It is always co-administered with a beta-lactam partner drug — most commonly piperacillin or ceftolozane — to inhibit bacterial beta-lactamase enzymes (including extended-spectrum beta-lactamases, ESBLs), thereby restoring the partner drug's bactericidal activity against beta-lactamase-producing strains.

Pneumonia, particularly hospital-acquired and ventilator-associated pneumonia, is frequently caused by Gram-negative pathogens such as *Klebsiella pneumoniae*, *Escherichia coli*, and *Pseudomonas aeruginosa* — organisms commonly implicated in beta-lactamase-mediated resistance. This mechanistic profile aligns directly with the pathogen spectrum seen in nosocomial pneumonia.

Critically, this is not a novel repurposing hypothesis in the strict sense: Piperacillin-Tazobactam and Ceftolozane-Tazobactam are already established, guideline-referenced therapies for hospital-acquired and ventilator-associated bacterial pneumonia, and are used repeatedly as the active comparator arm in pivotal Phase 3 trials of newer beta-lactam/beta-lactamase-inhibitor combinations (e.g. imipenem/cilastatin/relebactam, ceftolozane/tazobactam vs. meropenem). This confirms the mechanistic and clinical plausibility of the TxGNN prediction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational double-blind RCT: imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP; non-inferiority on 28-day all-cause mortality |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Double-blind active-comparator RCT: imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Double-blind RCT: ceftolozane/tazobactam vs. meropenem in ventilated nosocomial pneumonia; non-inferiority on Day 28 all-cause mortality |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Open-label RCT: levofloxacin vs. piperacillin/tazobactam in mild-to-moderate hospital-acquired pneumonia |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Prolonged vs. intermittent infusion of piperacillin/tazobactam for nosocomial pneumonia in ICU; clinical, bacteriologic and PK/safety endpoints |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Randomized open-label study: IV ceftolozane/tazobactam vs. IV piperacillin/tazobactam in ventilator-associated pneumonia (terminated early, low enrollment) |
| [NCT03897582](https://clinicaltrials.gov/study/NCT03897582) | N/A | Recruiting | 65 | Beta-lactam (incl. piperacillin/tazobactam) dosing in ICU pneumonia patients on continuous renal replacement therapy |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Short vs. prolonged infusion of ceftolozane-tazobactam in VAP due to *Pseudomonas aeruginosa* |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability and PK of ceftolozane/tazobactam in pediatric nosocomial pneumonia |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Individualised dosing regimens (incl. piperacillin/tazobactam) to maximise antibiotic effectiveness in ICU pneumonia |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | Piperacillin-tazobactam vs. meropenem for 30-day mortality in ceftriaxone-resistant *E. coli*/*K. pneumoniae* bloodstream infection |
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs. meropenem for nosocomial pneumonia, Phase 3 non-inferiority trial |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial: imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: randomized double-blind multicenter trial of imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Review of ceftolozane/tazobactam for treatment of hospital-acquired pneumonia |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Review | Clin Microbiol Infect | Systematic review and network meta-analysis of empiric antibiotic regimens in non-ventilator-associated HAP |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Review of ceftolozane-tazobactam in nosocomial pneumonia |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Review | Int J Antimicrob Agents | Systematic review of PK/PD of novel beta-lactams and beta-lactam/beta-lactamase-inhibitor combinations in pneumonia from carbapenem-resistant Gram-negative bacteria |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Observational | Lancet Infect Dis | CACTUS: multicentre retrospective comparison of ceftazidime-avibactam vs. ceftolozane-tazobactam for MDR *P. aeruginosa* infections |
| [34598422](https://pubmed.ncbi.nlm.nih.gov/34598422/) | 2021 | Review | Rev Esp Quimioter | When, how and why to use ceftolozane-tazobactam |

## South Africa Market Information

Tazobactam has no active SAHPRA registrations and is currently classified as **Not Marketed** in South Africa (0 registered products in this evidence pack). No product name, dosage form, or approved indication text is available to report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (e.g. NCT03583333, NCT02493764, NCT02070757, NCT00253955) establish beta-lactam/beta-lactamase-inhibitor combinations containing tazobactam as a validated, guideline-referenced comparator for hospital-acquired and ventilator-associated pneumonia, giving strong (L1) mechanistic and clinical evidence. However, Tazobactam has no current SAHPRA registration in South Africa, and TFDA/SAHPRA-level safety data (warnings, contraindications) and detailed MOA data are both marked as data gaps — one of them (PI warnings/contraindications) is classified as **Blocking** for safety pre-assessment.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, precautions, and contraindications (Blocking data gap DG001)
- Detailed mechanism of action data from DrugBank (High-priority data gap DG002)
- Confirmation of regulatory pathway/status for tazobactam-containing combination products (e.g. Piperacillin-Tazobactam) intended for the South African market
- A drug-drug interaction (DDI) profile, currently unavailable ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

