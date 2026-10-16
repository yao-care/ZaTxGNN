---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cefuroxime: predicted new indication Urinary tract infection (evidence level L5). Approved use: Bacterial infections (otitis media, pneumonia, meningitis, gonorrhoea…"
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections (Including Otitis Media and Pneumonia) to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for bacterial infections such as otitis media, pneumonia, meningitis, gonorrhoea and Lyme disease.
The TxGNN model's top-ranked predictions are mostly unsupported (for example hyperamylasemia), and the best-evidenced prediction is **urinary tract infection (UTI)**, supported by **5 clinical trials** and **20 publications**. This is closer to an established antibiotic use than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (otitis media, pneumonia, meningitis, gonorrhoea, Lyme disease and others) |
| Predicted New Indication | Urinary tract infection (best-evidenced prediction; the rank 1 prediction, hyperamylasemia, has no supporting evidence) |
| TxGNN Prediction Score | 99.62% (UTI); 99.76% for the rank 1 prediction (hyperamylasemia) |
| Evidence Level | L3 (UTI) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Proceed with Guardrails (UTI only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cefuroxime is a beta-lactam cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. Its efficacy in respiratory, ear and other bacterial infections is established.

For UTI, the fit is strong. Cefuroxime is active against common uropathogens such as *E. coli*, *Klebsiella* and *Proteus*, and renal excretion gives high urinary concentrations. UTI is a bacterial infection like its original indications, so this prediction mainly confirms an existing antibacterial use rather than revealing a new biology.

Several other predictions deserve a brief comment:
- **Suppurative otitis media** and **Peptostreptococcus infection** are mechanistically plausible, but they largely overlap with existing indications (otitis media) or rest on indirect in-vitro evidence. Chronic suppurative otitis media often involves *Pseudomonas* and biofilms, which cefuroxime does not reliably cover.
- **Hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy and haematological disease with peripheral neuropathy** have no plausible mechanistic link to an antibiotic. The high scores likely reflect network-level associations in the knowledge graph rather than biology.

---

## Clinical Trial Evidence

Trials for urinary tract infection:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Effect of inappropriate cefuroxime therapy in adults hospitalised with pyelonephritis (observational design) |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal to prevent UTI |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in the puerperium among pregnant women with recurrent UTI |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial application to prevent UTI before minimally invasive upper tract lithotomy |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Antibiotic prophylaxis for postpartum infections after caesarean section; no data |

No Phase 3 randomised trial directly demonstrating cefuroxime efficacy in UTI is included. No SANCTR or PACTR identifiers were available in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams versus trimethoprim/sulfamethoxazole and fluoroquinolones for complicated UTI |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | Randomised trial | Lancet Infect Dis | SIMPLIFY: de-escalation from antipseudomonal β-lactams in Enterobacterales bloodstream infection |
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Randomised comparison | Infection | Aztreonam versus cefuroxime in gram-negative upper UTI |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime: mechanism, spectrum (excellent Enterobacteriaceae activity, except *Serratia* and indole-positive *Proteus*), pharmacokinetics and adverse reactions |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology and clinical efficacy |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil overview |
| [20027983](https://pubmed.ncbi.nlm.nih.gov/20027983/) | 2009 | Review/guideline | Harefuah | Diagnosis and therapy of first community-acquired UTI in children |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Cohort | Infect Dis Clin Microbiol | Causative organisms in community-acquired UTI and risk factors for ESBL-producing species |
| [35733866](https://pubmed.ncbi.nlm.nih.gov/35733866/) | 2022 | Cohort | Front Med | Carbapenem prophylaxis and ESC-resistant Enterobacterales UTI in kidney transplant recipients |

Only a few of these studies test cefuroxime directly, and one is a 1989 head-to-head comparison. Many other retrieved papers are resistance surveillance studies, which are relevant to local susceptibility but not to efficacy.

---

## South Africa Market Information

Cefuroxime is marketed in South Africa, and all 4 registrations are valid single-ingredient injectable products. The data compiled for this report contain no approved indication text and no Essential Medicines List (EML) information.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A38/20.1.1/0676 | Betaroxime | Injection | Not available in the compiled data |
| 42/20.1.1/0737 | Fksa cefuroxime vial powder for solution | Injection | Not available in the compiled data |
| 36/20.1.1/0296 | Sabax cefuroxime 250mg | Injection | Not available in the compiled data |
| L/20.1.1/0098 | Zinacef | Injection | Not available in the compiled data |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Disease-level contraindication signals** (from the knowledge graph, not label text) include:
- Kidney disease, pyoureter, liver disease, gallbladder disease
- Blood coagulation disease and congenital prothrombin deficiency
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis

These signals should be verified against the PI. Kidney disease is particularly relevant to UTI use because of renal dose adjustment.

**Drug interactions:** 100 interactions were identified, and all 20 listed in the compiled data are rated Moderate. The main groups are:
- Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
- Antacids: aluminium hydroxide, calcium carbonate, magaldrate and magnesium salts
- Aminoglycosides: kanamycin and neomycin
- Balsalazide

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (UTI only). Hold for all other predictions.**

**Rationale:**
- UTI has a strong mechanistic fit, completed large studies, and a systematic review and randomised comparison in the literature. However, this is largely an established antibacterial use, and no Phase 3 RCT directly demonstrates cefuroxime efficacy (evidence level L3).
- The remaining top predictions (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility and others) have no plausible mechanism and little or no evidence (L5), so they should be held. Suppurative otitis media and Peptostreptococcus infection are research questions only (L4).

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the South African registrations, to confirm whether UTI is already labelled
- Local South African resistance data (ESBL and rising resistance) to guide use
- A stewardship and renal dose adjustment plan
- Confirmation of the status of trials with unknown status (NCT05577273, NCT02789579)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

