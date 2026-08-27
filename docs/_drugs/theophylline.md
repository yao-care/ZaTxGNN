---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Theophylline: From Established Bronchodilator Use to Obstructive Lung Disease (TxGNN-Confirmed) and Six Additional Candidate Indications

## One-Sentence Summary

Theophylline is a long-used methylxanthine bronchodilator; this evidence pack does not contain confirmed original-indication or mechanism-of-action data (both are flagged as data gaps), but among the seven indications TxGNN linked to this drug, **Obstructive Lung Disease** (asthma/COPD) stands out as the only candidate with robust, direct clinical support — **50 clinical trials** (including multiple completed Phase 3/4 RCTs, such as a 1,670-patient trial) and **20 publications**, reaching the highest evidence tier (**L1**). The remaining six predicted indications (thrombotic disease, nasal cavity disease, laryngotracheitis, tracheal disease, pharyngitis, acute laryngopharyngitis) range from weak to no supporting evidence and are not considered actionable at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA-registered product on file for theophylline in this data set (data gap; original indication/MOA not confirmed) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a Blocking/High-severity data gap — DG002). Based on the mechanistic rationale accompanying the TxGNN prediction and the supporting literature itself, theophylline is a classic methylxanthine that relaxes airway smooth muscle through phosphodiesterase (PDE3/4) inhibition and adenosine-receptor antagonism, with additional mild anti-inflammatory activity at lower plasma concentrations.

This mechanism maps directly onto the pathophysiology of obstructive airway disease (asthma and COPD), where bronchospasm and airway inflammation are the core problems. Several of the literature items retrieved for this candidate (e.g., PMID 23672674, PMID 14988770) explicitly describe theophylline as having been used to treat asthma and COPD for over 80 years — meaning this "predicted" indication is, in practice, a well-established therapeutic use rather than a novel repurposing hypothesis. In that sense, this result is best read as a **positive-control confirmation** of the TxGNN model (it correctly recovered a known drug-disease relationship) rather than a genuinely new signal, which is an important distinction for interpreting the "Proceed with Guardrails" recommendation below: the guardrails relate mainly to South African regulatory/safety documentation gaps, not to scientific plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02261727](https://clinicaltrials.gov/study/NCT02261727) | Phase 4 | Completed | 1,670 | TASCS trial — low-dose theophylline ± low-dose prednisone vs. placebo for reducing COPD exacerbations and improving quality of life over 48 weeks |
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | Completed | 340 | Symbicort Turbuhaler vs. Pulmicort Turbuhaler + Theolong (theophylline) 200 mg BID in Japanese asthma patients |
| [NCT03984188](https://clinicaltrials.gov/study/NCT03984188) | Phase 3 | Completed | 100 | Low-dose theophylline for management of biomass-fuel-associated COPD |
| [NCT03015090](https://clinicaltrials.gov/study/NCT03015090) | N/A | Completed | 110 | CYP1A2 gene polymorphisms and theophylline metabolism in Han and Uygur COPD patients |
| [NCT02001935](https://clinicaltrials.gov/study/NCT02001935) | N/A | Completed | 102 | CYP1A2/CYP2E1 polymorphisms and theophylline metabolism in COPD |
| [NCT02023554](https://clinicaltrials.gov/study/NCT02023554) | N/A | Completed | 40 | PK interaction study — effect of azithromycin on steady-state theophylline plasma levels |
| [NCT00756418](https://clinicaltrials.gov/study/NCT00756418) | Phase 4 | Completed | 84 | Randomized comparison of montelukast vs. theophylline added to inhaled corticosteroid in pediatric asthma |
| [NCT00299858](https://clinicaltrials.gov/study/NCT00299858) | Phase 2/3 | Completed | 24 | Theophylline's effect on exercise capacity and lung function in COPD patients on long-acting bronchodilators |
| [NCT00241631](https://clinicaltrials.gov/study/NCT00241631) | Phase 2 | Completed | 49 | RCT of theophylline + fluticasone on induced sputum cells in COPD |
| [NCT00671151](https://clinicaltrials.gov/study/NCT00671151) | N/A | Completed | 35 | Molecular mechanisms of COPD exacerbations and modulating effect of low-dose theophylline (NF-κB, HDAC pathways) |

*Note: No South African National Clinical Trials Register (SANCTR) or Pan African Clinical Trials Registry (PACTR) entries were found in this evidence pack; all listed trials are drawn from ClinicalTrials.gov.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7982769](https://pubmed.ncbi.nlm.nih.gov/7982769/) | 1994 | RCT | Israel Journal of Medical Sciences | Double-blind crossover RCT showing theophylline improves exercise and bronchial reactivity in COPD without significant neuropsychological impairment |
| [1729064](https://pubmed.ncbi.nlm.nih.gov/1729064/) | 1992 | RCT | Chest | Double-blind, four-phase crossover RCT: theophylline and salbutamol both improve pulmonary function in irreversible COPD |
| [14988770](https://pubmed.ncbi.nlm.nih.gov/14988770/) | 2004 | Review | Drugs of Today | Comprehensive review of theophylline's mechanism of action and role in asthma/COPD treatment |
| [23672674](https://pubmed.ncbi.nlm.nih.gov/23672674/) | 2013 | Review | American Journal of Respiratory and Critical Care Medicine | Landmark review (Barnes) — theophylline used for airway disease for 80+ years; anti-inflammatory effects at low concentrations via PDE inhibition |
| [7783821](https://pubmed.ncbi.nlm.nih.gov/7783821/) | 1995 | Review | Netherlands Journal of Medicine | Reviews the clinical positioning of theophylline in asthma and COPD treatment |
| [8513541](https://pubmed.ncbi.nlm.nih.gov/8513541/) | 1993 | Review | Cleveland Clinic Journal of Medicine | Discusses controversy around theophylline toxicity risk vs. benefit in ambulatory COPD management |
| [3534060](https://pubmed.ncbi.nlm.nih.gov/3534060/) | 1986 | Clinical Study | Journal of Allergy and Clinical Immunology | Theophylline improves global cardiac function and reduces dyspnea in COPD |
| [8518774](https://pubmed.ncbi.nlm.nih.gov/8518774/) | 1993 | Cohort | Monaldi Archives for Chest Disease | Theophylline reduces hyperinflation/trapped gas in chronic airflow limitation |
| [2877017](https://pubmed.ncbi.nlm.nih.gov/2877017/) | 1986 | Clinical Review | Journal of Allergy and Clinical Immunology | Evidence that maintenance theophylline therapy produces measurable patient improvement in COPD |
| [9756187](https://pubmed.ncbi.nlm.nih.gov/9756187/) | 1998 | Clinical Review | Clinical and Experimental Allergy | Describes anti-inflammatory/immunomodulatory activity of theophylline beyond bronchodilation in COPD |

---

## South Africa Market Information

Theophylline has **no active SAHPRA registrations** in this data set (0 licenses on file; market status: Not marketed). No product name, dosage form, or SAHPRA-approved indication text is available for South Africa at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Outstanding data gap (Blocking):** TFDA/SAHPRA-equivalent package insert warnings and contraindications for theophylline have not yet been retrieved for this evidence pack. This must be resolved before any Stage 1 safety screening can be completed, given theophylline's known narrow therapeutic index and extensive CYP1A2/CYP3A4-mediated drug interaction profile referenced throughout the literature above (e.g., azithromycin PK interaction, CYP1A2/CYP2E1 polymorphism studies).

---

## Other Predicted Indications (Lower Evidence — Not Actionable)

This evidence pack included six additional TxGNN-predicted indications for theophylline, all ranked by raw model score higher than or close to Obstructive Lung Disease but with materially weaker supporting evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|---------|------|------|------|------|
| 1 | Thrombotic disease | 99.62% | L5 | Hold | 19 publications retrieved, but nearly all are unrelated to theophylline (ticlopidine PK, platelet biomarker methodology, cerebral edema); only 1 addresses theophylline directly (a biosensor detection paper, not clinical efficacy) |
| 2 | Nasal cavity disease | 99.53% | L2 | Research Question | One completed Phase 2 trial (SCENT, n=27) on nasal theophylline irrigation for post-viral smell loss, plus one supportive RCT on allergic rhinitis nasal challenge — promising but small, early-stage |
| 3 | Laryngotracheitis | 99.51% | L5 | Hold | No clinical trials or literature identified |
| 4 | Tracheal disease | 99.49% | L3 | Research Question | Strong basic pharmacology (tracheal smooth muscle relaxation) and a veterinary retrospective study on tracheal collapse, but no prospective human clinical trial |
| 6 | Pharyngitis | 99.46% | L5 | Hold | 11 publications retrieved, mostly concerning unrelated macrolide antibiotics for pediatric pharyngitis; no direct theophylline efficacy evidence |
| 7 | Acute laryngopharyngitis | 99.35% | L5 | Hold | No clinical trials or literature identified |

These candidates are documented here for completeness but require substantially more evidence generation (or should be deprioritized) before further evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Obstructive Lung Disease candidate is supported by an extensive and mature evidence base — 50 clinical trials (including large completed Phase 3/4 RCTs) and 20 publications spanning four decades — reaching evidence tier L1. However, this is functionally a confirmation of theophylline's long-established bronchodilator role rather than a novel repurposing opportunity, and two Blocking/High-severity data gaps (SAHPRA/TFDA-equivalent safety labeling, and confirmed mechanism-of-action documentation) remain unresolved, and the drug has zero current SAHPRA registrations in South Africa.

**To proceed, the following is needed:**
- Retrieval of SAHPRA-approved Professional Information (PI) — warnings, contraindications, and drug interaction data (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source (High-severity data gap, DG002)
- Confirmation of theophylline's regulatory pathway/status for potential SAHPRA registration or Section 21-type access in South Africa, given it is currently unmarketed
- For the Nasal Cavity Disease and Tracheal Disease candidates: monitor for larger prospective human trials before elevating beyond "Research Question" status
- For Thrombotic Disease, Laryngotracheitis, Pharyngitis, and Acute Laryngopharyngitis: no further action recommended unless new trial or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

