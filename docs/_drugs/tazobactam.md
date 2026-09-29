---
layout: default
title: Tazobactam
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 10
---

# Tazobactam
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

# Tazobactam: From Beta-Lactamase Inhibitor Combination Therapy to Pneumonia

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor that is used only as a partner in fixed combinations (for example piperacillin/tazobactam and ceftolozane/tazobactam). The registration data supplied contain no original indication text.
The TxGNN model predicts it may be effective for **pneumonia**, and the literature already supports its combinations in this setting.
Currently **41 clinical trials** and **20 publications** are linked to this prediction, including several completed Phase 3 RCTs. Most of that evidence is for the combination products, not for tazobactam alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (indication text is empty) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs, mostly combination products or comparator use) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, tazobactam inhibits many bacterial beta-lactamases and so protects its partner beta-lactam (piperacillin or ceftolozane) from breakdown. This restores activity against many Gram-negative bacteria that cause hospital-acquired and ventilator-associated pneumonia. Tazobactam has no antibacterial activity of its own.

Because of this, the prediction is closer to on-label combination use than to true repurposing. Pneumonia is a bacterial lower respiratory tract infection, and piperacillin/tazobactam and ceftolozane/tazobactam have both been studied in it. The evidence applies to these fixed combinations only.

Some other predicted indications are less credible. Ureaplasma lacks a cell wall, so beta-lactams are not expected to work. For gonococcal urethritis, urogenital tuberculosis and streptococcal pneumonia, no supporting evidence or mechanistic rationale was found.

## Clinical Trial Evidence

No SANCTR or PACTR identifiers were returned in the evidence supplied. Trials whose relevance was graded as pending are listed only where the record clearly concerns pneumonia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia. Primary endpoint is Day 28 all-cause mortality (non-inferiority). |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam (comparator) in HABP/VABP. |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational imipenem/relebactam vs piperacillin/tazobactam (comparator) in HABP/VABP. |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam (comparator) in mild to moderate hospital-acquired pneumonia. |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in VAP. Too few patients to give an efficacy signal. |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Prolonged vs regular piperacillin/tazobactam infusion in nosocomial pneumonia. Addresses dosing strategy. |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Short vs prolonged ceftolozane-tazobactam infusion in Pseudomonas VAP. Primary focus is pharmacokinetics. |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical piperacillin-tazobactam dosing in elderly pneumonia patients. |
| [NCT04276480](https://clinicaltrials.gov/study/NCT04276480) | N/A | Completed | 9 | Empirical piperacillin-tazobactam for VAP in patients colonised with ESBL-producing Enterobacteriaceae. Very small. |
| [NCT05102162](https://clinicaltrials.gov/study/NCT05102162) | Phase 4 | Terminated | 35 | Continuous vs intermittent beta-lactam infusion (including piperacillin/tazobactam) in severe pneumonia. Stopped early. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT (Phase 3) | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia (non-inferiority). |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP. |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT (Phase 3) | Int J Infect Dis | Non-inferiority trial of imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP. |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Compares empiric antibiotic regimens for non-ventilator hospital-acquired pneumonia across RCTs. |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/inhibitor combinations for carbapenem-resistant Gram-negative pneumonia. |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane and tazobactam for hospital-acquired pneumonia, including Pseudomonas aeruginosa. |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Ceftolozane-tazobactam in nosocomial pneumonia. |
| [38862579](https://pubmed.ncbi.nlm.nih.gov/38862579/) | 2024 | Cohort (TMLE analysis) | Sci Rep | Cefepime vs piperacillin/tazobactam in 2,026 ICU patients with community-acquired pneumonia. |
| [34158237](https://pubmed.ncbi.nlm.nih.gov/34158237/) | 2021 | Observational | J Infect Chemother | Ceftriaxone vs piperacillin-tazobactam or carbapenems in aspiration pneumonia (propensity matching). |
| [38936906](https://pubmed.ncbi.nlm.nih.gov/38936906/) | 2024 | Clinical study | In Vivo | Mini-tracheostomy plus perioperative tazobactam/piperacillin to prevent pneumonia after oesophagectomy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/1.2/0273 | Serlife | Tablet (oral) | Not recorded in the data supplied |

The manufacturer and Essential Medicines List (EML) status are not available in the data supplied. The only registration is an oral tablet, whereas the pneumonia evidence is for intravenous combination products. Confirm that this registration actually contains tazobactam, and check for registered injectable piperacillin/tazobactam or ceftolozane/tazobactam products, before any further work.

## Safety Considerations

- **Literature signal**: A 2025 case report ([PMID 41305690](https://pubmed.ncbi.nlm.nih.gov/41305690/)) describes piperacillin-tazobactam-induced haemophagocytic lymphohistiocytosis in a patient with community-acquired pneumonia. Elevated procalcitonin masked the diagnosis. This is a rare, single-case signal.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings, contraindications and drug interactions. No drug interaction records were found in the data supplied. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 RCTs and a large body of literature support tazobactam-containing combinations in hospital-acquired and ventilator-associated pneumonia. Much of this evidence uses piperacillin/tazobactam as the comparator, and tazobactam has no activity alone. Any decision therefore applies to specific fixed combinations, not to tazobactam as a standalone agent. Urinary tract infection and pyelonephritis are also L1 predictions with similar limits. The remaining predicted indications should stay on Hold.

**To proceed, the following is needed:**
- Download and review the SAHPRA Professional Information for safety information (warnings and contraindications).
- Confirm which SAHPRA-registered products contain tazobactam and by which route. The single tablet registration does not match the intravenous evidence base.
- Obtain mechanism of action data from DrugBank.
- Check EML inclusion and local antibiogram data for Gram-negative resistance in South Africa.
- Confirm the role of tazobactam (test or comparator arm) in the trials with truncated titles.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

