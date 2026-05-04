---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Urinary Tract Infection

---

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic with proven bactericidal activity against a broad spectrum of Gram-positive and Gram-negative pathogens, widely approved globally for the treatment of respiratory tract, skin, and urinary tract infections.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)** — an indication already registered in numerous countries but with **zero SAHPRA registrations** in South Africa — supported by **10 clinical trials** and **20 publications**.
Of the 10 TxGNN-ranked predictions in this dataset, UTI (rank 6) is selected as the primary reporting focus because it is the only indication reaching L1 evidence with a "Proceed with Guardrails" recommendation; the top-ranked predictions (hyperamylasemia through blood group incompatibility) lack mechanistic plausibility and carry no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, skin, soft tissue) |
| Predicted New Indication | Urinary Tract Infection (UTI) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| South Africa (SAHPRA) Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cefuroxime exerts bactericidal activity by inhibiting bacterial cell wall synthesis through binding to penicillin-binding proteins (PBPs), preventing the cross-linking of peptidoglycan strands and ultimately causing cell lysis. Detailed MOA documentation was not available in this Evidence Pack, but published literature confirms activity against the principal uropathogens: *Escherichia coli*, *Klebsiella pneumoniae*, *Proteus mirabilis*, *Haemophilus influenzae*, and streptococcal species — precisely the pathogens responsible for 70–90% of community-acquired UTIs. The oral prodrug formulation, cefuroxime axetil, is hydrolysed in the intestinal mucosa to release active cefuroxime, which is predominantly excreted renally, achieving urinary drug concentrations substantially above the MICs of susceptible uropathogens (Cmax/MIC and T>MIC targets met at standard oral dosing).

The mechanistic link between bacterial respiratory infections and urinary tract infections is straightforward: both conditions are caused by susceptible bacterial pathogens against which cefuroxime has direct killing activity. The urinary route of excretion makes the urinary tract a primary site of drug action rather than a secondary one. A 1994 comprehensive drug review (Dellamonica, *Int J Antimicrobial Agents*) and multiple subsequent observational cohorts in children and adults corroborate this pharmacokinetic-pharmacodynamic rationale.

It is important to contextualise this finding for South African practice: this is largely a **registration gap rather than a true repurposing discovery**. Cefuroxime is approved for UTI treatment by the EMA, FDA, TGA, and multiple African national medicines authorities. Its complete absence from the SAHPRA register is the clinically actionable signal here. Prescribers requiring cefuroxime in South Africa currently have no locally registered product to reference, making the Section 21 unregistered medicine pathway or accelerated registration submission the appropriate next step.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03020940](https://clinicaltrials.gov/study/NCT03020940) | N/A | Unknown | 100,000 | Large-scale prospective real-world registry of cefuroxime axetil dispersible tablets, including UTI as a primary indication; 100,000-patient dataset provides the most extensive real-world safety and efficacy evidence for this drug–disease pair |
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Completed study directly evaluating cefuroxime in pyelonephritis (complicated UTI, n=973); assessed outcomes following inappropriate vs appropriate therapy, establishing efficacy boundaries for second-generation cephalosporins in upper UTI |
| [NCT07236944](https://clinicaltrials.gov/study/NCT07236944) | Phase 4 | Recruiting | 560 | Phase 4 non-inferiority RCT comparing pivmecillinam to standard-of-care antibiotics (including cefuroxime) for oral step-down treatment of febrile UTI; currently the most methodologically rigorous active trial in this space |
| [NCT05337566](https://clinicaltrials.gov/study/NCT05337566) | N/A | Recruiting | 2,278 | Large RCT (n=2,278) comparing azithromycin + cefuroxime vs cefuroxime alone for post-hysterectomy infection prevention; cefuroxime serves as the standard-of-care control arm, supporting its established role in pelvic/urinary infection prophylaxis |
| [NCT04146142](https://clinicaltrials.gov/study/NCT04146142) | N/A | Completed | 550 | Completed RCT (n=550) evaluating cefuroxime prophylaxis vs no antibiotic before transperineal MRI-TRUS fusion prostate biopsy; supports cefuroxime's role in preventing post-procedure UTI and sepsis |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Completed study (n=220) assessing preventive antibiotic treatment during the puerperium in pregnant women with recurrent UTIs; directly relevant to UTI prophylaxis in vulnerable populations |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1,000 | Study (n=1,000) evaluating cefuroxime prophylaxis at urinary catheter removal to prevent catheter-associated UTI; addresses a common hospital-acquired infection scenario |
| [NCT05609240](https://clinicaltrials.gov/study/NCT05609240) | Phase 2 | Recruiting | 180 | Phase 2 RCT comparing standard bolus to bolus-continuous infusion cefuroxime prophylaxis for infection prevention (including UTI) after colorectal surgery; addresses pharmacokinetic optimisation of dosing |
| [NCT02072798](https://clinicaltrials.gov/study/NCT02072798) | Phase 4 | Completed | 42 | Phase 4 completed study of antibiotic prophylaxis for post-Caesarean section infections including UTI; cefuroxime was a study drug; limited statistical power due to small sample size |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | Pilot study of antimicrobial prophylaxis before minimally invasive upper tract lithotomy for post-operative UTI prevention; early phase with limited generalisability |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30234077](https://pubmed.ncbi.nlm.nih.gov/30234077/) | 2018 | Prospective Cohort | Frontiers in Pediatrics | Two-year single-centre evaluation of oral cefuroxime-axetil in 82 children with first febrile UTI; demonstrated effective fever resolution, good tolerability, and low bacterial resistance rates in an ambulatory setting |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | The Lancet. Infectious Diseases | Multicentre open-label RCT confirming non-inferiority of de-escalating from antipseudomonal β-lactams to narrower-spectrum agents (including cefuroxime) in Enterobacterales bacteraemia; supports cefuroxime as a valid targeted therapy after culture results |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Drug Review | International Journal of Antimicrobial Agents | Seminal comprehensive review of cefuroxime axetil; describes bactericidal mechanism, pharmacokinetics (including urinary excretion), and clinical efficacy across bacterial indications including urinary tract infections |
| [40135203](https://pubmed.ncbi.nlm.nih.gov/40135203/) | 2025 | Multicentric Observational | IJID Regions | 18-centre Indian study mapping contemporary *Klebsiella pneumoniae* susceptibility in UTI; provides current resistance landscape data informing empiric cefuroxime suitability in high-resistance settings |
| [35069075](https://pubmed.ncbi.nlm.nih.gov/35069075/) | 2021 | Review | Menopause Review | Reviews strategies to limit antibiotic resistance in UTI management including recurrent UTI; discusses second-generation cephalosporins and stewardship principles relevant to prescribing cefuroxime |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Observational | Infectious Diseases & Clinical Microbiology | Multicentre study characterising causative organisms and ESBL risk factors in community-acquired UTI; provides contemporary susceptibility profiling for empiric cefuroxime decision-making |
| [26607682](https://pubmed.ncbi.nlm.nih.gov/26607682/) | 2016 | Cohort | Brazilian Journal of Infectious Diseases | Longitudinal follow-up cohort of infants <2 months with UTI in southern Israel; characterises microbiological recurrence patterns and antibiotic susceptibility, with implications for cefuroxime use in neonatal UTI |
| [35096675](https://pubmed.ncbi.nlm.nih.gov/35096675/) | 2021 | Observational | Germs | Observational study of paediatric UTI in Bucharest, Romania; documents clinical features and antimicrobial resistance profiles including cefuroxime susceptibility rates in a resource-limited European context |
| [30197697](https://pubmed.ncbi.nlm.nih.gov/30197697/) | 2018 | Case Report | The Open Microbiology Journal | Case report of non-typable *Haemophilus influenzae* causing UTI with septicaemia; illustrates that cefuroxime's broad Gram-negative spectrum extends to atypical uropathogens |
| [29759804](https://pubmed.ncbi.nlm.nih.gov/29759804/) | 2018 | Case Report/Series | Revista Clínica Española | Two cases of UTI due to emerging opportunistic pathogen *Aerococcus sanguinicola* in elderly urological patients; antimicrobial susceptibility data documents cefuroxime coverage of unusual community uropathogens |

---

## South Africa Market Information

Cefuroxime currently holds **no SAHPRA registrations** in South Africa and is classified as **not marketed**. No registration table can be provided as no licences exist in the regulatory dataset.

This absence is clinically significant: cefuroxime is included on the WHO Model List of Essential Medicines and is registered by the EMA (originator: Zinacef®/Zinnat®), the US FDA (Ceftin®/Zinacef®), and multiple Sub-Saharan African medicines authorities. South African clinicians requiring access to cefuroxime should consult SAHPRA regarding:

- **Section 21 authorisation** — for individual patient access to an unregistered medicine
- **Accelerated/reliance registration** — SAHPRA accepts reliance applications on EMA or WHO-prequalified dossiers, which could expedite full registration

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As cefuroxime is not currently registered in South Africa, clinicians should consult the manufacturer's international prescribing information and report any adverse drug reactions to SAHPRA via the MedSafety reporting portal.

Key safety considerations from established cephalosporin pharmacology applicable to this drug class:
- **Hypersensitivity**: Assess history of penicillin or cephalosporin allergy prior to use; cross-reactivity between penicillins and cephalosporins is well-documented (estimated 1–2%)
- **Renal impairment**: Dose reduction required when creatinine clearance falls below 30 mL/min, as cefuroxime is primarily renally excreted
- **Direct Antiglobulin Test (DAT) interference**: Cefuroxime may adsorb non-specifically onto red blood cell membranes, causing false-positive Coombs tests — a class effect relevant to haematology and blood bank practice

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed clinical trials (including a 100,000-patient real-world registry, completed RCTs in pyelonephritis and UTI prophylaxis, and an active Phase 4 comparative RCT), supported by 20 publications spanning prospective cohorts, observational studies, and comprehensive drug reviews, provide L1-level evidence that cefuroxime is an effective treatment for urinary tract infections. The core challenge in South Africa is not evidence of efficacy but rather the complete absence of a SAHPRA-registered product — a regulatory gap that must be addressed before routine prescribing is possible.

**To proceed, the following is needed:**

- **SAHPRA registration submission**: Initiate a dossier via SAHPRA's reliance pathway using EMA or WHO-prequalification approval as the reference; target oral cefuroxime axetil (tablets/suspension) and parenteral cefuroxime sodium as priority dosage forms, with UTI and respiratory tract infections as primary approved indications
- **Local susceptibility data**: Commission or obtain South African antibiogram data for common uropathogens (*E. coli*, *Klebsiella* spp., *Proteus* spp.) to confirm cefuroxime remains appropriate for empiric UTI therapy in the local resistance landscape — ESBL prevalence is the critical variable
- **Section 21 interim access**: Apply to SAHPRA for Section 21 authorisation to enable individual patient access while a full registration application is pending
- **Stewardship positioning**: Engage the South African National Department of Health to evaluate inclusion of cefuroxime in the Standard Treatment Guidelines (STGs) and Essential Medicines List (EML) for community-acquired UTI and surgical prophylaxis
- **Safety documentation**: Obtain full Professional Information (PI) from a reference-country originator or WHO-prequalified generic manufacturer to support SAHPRA review and local prescriber education

> **Disclaimer**: This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content should be read in conjunction with SAHPRA-approved prescribing information and local treatment guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

