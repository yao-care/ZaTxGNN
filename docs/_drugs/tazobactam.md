---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 436
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Tazobactam: predicted new indication Pneumonia (evidence level L1). Approved use: Bacterial pneumonia, peritonitis, appendicitis…"
monitor_inn: "Tazobactam"
predicted_indications: ["pneumonia", "urinary tract infection (disease)", "Ureaplasma urethritis", "gonococcal urethritis", "bacterial arthritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "streptococcal pneumonia", "pyelonephritis"]
---

# Tazobactam
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Tazobactam: From Bacterial Pneumonia to Pneumonia (Nosocomial and Ventilator-Associated)

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor, originally used (in combination with a partner beta-lactam) for bacterial pneumonia, peritonitis, appendicitis and staphylococcal infections.
The TxGNN model predicts it may be effective for **pneumonia**, with **20 clinical trials** and **20 publications** compiled for this direction.
Note that the evidence applies to tazobactam in fixed combinations (piperacillin-tazobactam, ceftolozane-tazobactam), not as a standalone agent, so this is closer to an extension within the same disease area than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, peritonitis, appendicitis, *Staphylococcus aureus* infection (the SAHPRA registration record contains no approved indication text) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tazobactam is a beta-lactamase inhibitor used in fixed combinations with beta-lactams. It restores the activity of partner antibiotics (piperacillin, ceftolozane) against beta-lactamase-producing Gram-negative bacteria.

Its efficacy in bacterial pneumonia is already established, and nosocomial pneumonia and ventilator-associated pneumonia (HAP/VAP) are frequently caused by such resistant Gram-negative organisms. The prediction is therefore mechanistically sensible, but it is an extension within the same disease area rather than a new therapeutic concept.

Other predicted indications in the model output follow a similar pattern. Complicated urinary tract infection and pyelonephritis are well supported by Phase 3 trials (L1). Ureaplasma urethritis, gonococcal urethritis, bacterial arthritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, urogenital tuberculosis and streptococcal pneumonia have little or no tazobactam-specific evidence (L4–L5), and some are mechanistically unlikely (for example, *Ureaplasma* lacks a cell wall).

---

## Clinical Trial Evidence

Most relevant trials for pneumonia (selected from 20 compiled; all involve tazobactam combinations as study drug or comparator):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia; primary endpoint Day 28 all-cause mortality (non-inferiority) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; non-inferiority on all-cause mortality |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam in mild-to-moderate hospital-acquired pneumonia |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability and PK of ceftolozane/tazobactam in paediatric nosocomial pneumonia |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Phase 1 | Completed | 37 | Plasma PK and lung penetration of ceftolozane/tazobactam in critically ill patients |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical piperacillin-tazobactam dosing in elderly pneumonia |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Not yet recruiting | 100 | Piperacillin/tazobactam alone vs plus fluoroquinolone in severe community-acquired pneumonia (South Korea) |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Phase 4 | Recruiting | 600 | TREAT-GNB platform trial for multidrug-resistant Gram-negative bloodstream and lower respiratory infections |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in VAP; too few participants to inform efficacy |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3 | Withdrawn | 0 | Meropenem-vaborbactam vs piperacillin/tazobactam in HABP/VABP; no participants enrolled |

No SANCTR or PACTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs meropenem for Gram-negative nosocomial pneumonia (Phase 3, non-inferiority) |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of IMI/REL vs PIP/TAZ in HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review / network meta-analysis | Clin Microbiol Infect | Empiric antibiotic regimens in non-ventilator hospital-acquired pneumonia |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/beta-lactamase inhibitor combinations for carbapenem-resistant Gram-negative pneumonia |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | New antibiotics for Gram-negative pneumonia |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | New antibiotics for HAP and VAP |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane and tazobactam for hospital-acquired pneumonia |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Observational | Clin Infect Dis | Lower resistance emergence with ceftolozane-tazobactam (10%) than ceftazidime-avibactam (40%) in MDR *P. aeruginosa* bacteremia or pneumonia |
| [35699444](https://pubmed.ncbi.nlm.nih.gov/35699444/) | 2022 | Observational | Antimicrob Agents Chemother | Beta-lactam (including piperacillin-tazobactam) target attainment and outcomes in ICU HAP/VAP |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/1.2/0273 | Serlife | Tablet (oral) | Not recorded in the data compiled |

Only one SAHPRA registration was found, and it is an oral tablet. The trial evidence above relates to intravenous tazobactam combinations, so route and formulation compatibility with the pneumonia evidence has not been established. Essential Medicines List status was not available in the data compiled.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome.
- **Renal dosing:** Published literature notes that tazobactam-containing combinations carry precautionary statements for reduced clinical response in moderate renal impairment (creatinine clearance 30–50 mL/min), and that renal dose adjustment needs care.

No label-based warnings, contraindications or drug interaction data were available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several large, completed Phase 3 randomised trials (NCT02070757, NCT02493764, NCT00253955) support tazobactam-containing regimens in hospital-acquired and ventilator-associated pneumonia. However, the evidence concerns fixed combinations given intravenously, not tazobactam alone, and the only SAHPRA registration is an oral tablet.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) for the registered product
- Mechanism of action data (for example from DrugBank)
- Confirmation of which partner beta-lactam, route and formulation are registered or available in South Africa
- Local resistance data (antibiogram) for Gram-negative pathogens causing pneumonia
- Renal function dosing guidance and monitoring for neutropenia and *C. difficile* colitis
- Lower-priority predictions (Ureaplasma urethritis, gonococcal urethritis, bacterial arthritis, uterine inflammatory disease, xanthogranulomatous pyelonephritis, urogenital tuberculosis, streptococcal pneumonia) should stay on **Hold** because evidence is absent or weak
- Urinary tract infection and pyelonephritis (both L1, Proceed with Guardrails) merit separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

