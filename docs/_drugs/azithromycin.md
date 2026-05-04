---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Azithromycin is a broad-spectrum macrolide antibiotic widely used for community-acquired pneumonia, chlamydia, travellers' diarrhoea, and skin infections.
The TxGNN model's top-ranked prediction is **Hyperamylasemia** — however, this signal is critically flagged as a likely reverse-detection artefact of azithromycin's own known ability to cause drug-induced pancreatitis, not a genuine therapeutic target.
Across all 10 predicted indications evaluated in this multi-indication Evidence Pack, **Congenital Haematological Disorder (Sickle Cell Disease, Rank 10)** represents the most evidence-supported direction, with **4 registered clinical trials** and **2 publications** (including a Cochrane systematic review) currently available at Evidence Level L3.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, sexually transmitted infections, skin and soft tissue) |
| Top-Ranked Predicted Indication | Hyperamylasemia (TxGNN Rank 1) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level (Rank 1) | L5 — Model prediction only; no supporting studies |
| South Africa Market Status | Not registered with SAHPRA |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** (Rank 1: Hyperamylasemia) / **Proceed with Guardrails** (Best-supported: Sickle Cell Disease, Rank 10) |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacology, azithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 23S rRNA of the 50S ribosomal subunit, blocking peptide chain elongation and bacteriostatic killing of susceptible organisms. Beyond its antimicrobial action, azithromycin is recognised to have significant immunomodulatory properties — suppression of NF-κB signalling, reduction of pro-inflammatory cytokines (IL-6, IL-8), and enhancement of mucociliary airway clearance — which underpin several non-antibiotic applications currently under clinical investigation.

**Top prediction (Hyperamylasemia) — Critical Warning:** The Rank 1 prediction for hyperamylasemia is not mechanistically supported and should be treated as a methodological noise signal. Azithromycin is itself a documented cause of **drug-induced pancreatitis**, which presents clinically with elevated serum amylase. The knowledge graph has most likely detected this pharmacological association in the wrong causal direction. Similarly, the Rank 8 prediction — haematological disease with acquired peripheral neuropathy — carries an equivalent warning, as azithromycin is a known cause of peripheral neuropathy as an adverse drug reaction. Both predictions are false-positive repurposing signals arising from adverse effect associations rather than therapeutic mechanisms.

**Most plausible prediction (Sickle Cell Disease):** By contrast, the Rank 10 prediction for congenital haematological disorders, specifically Sickle Cell Disease (SCD), is mechanistically grounded and clinically relevant in the South African context. SCD is characterised by recurrent acute chest syndrome (ACS) driven by airway inflammation and atypical respiratory organism infections. Azithromycin's dual action — antimicrobial coverage of intracellular and atypical pathogens (Chlamydia, Mycoplasma) combined with its anti-inflammatory immunomodulatory properties — provides a coherent biological rationale for preventing ACS episodes and improving pulmonary function in SCD patients. This hypothesis was considered sufficiently credible by clinical researchers to warrant two formal registered trials, both subsequently withdrawn for enrolment reasons rather than safety concerns.

---

## All Predicted Indications — Overview

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Signal Assessment |
|------|---------|-------------|----------------|----------|-------------------|
| 1 | Hyperamylasemia | 99.81% | L5 | **Hold** | ⚠️ Likely reverse-detection: azithromycin *causes* elevated amylase (drug-induced pancreatitis) |
| 2 | Polyclonal Hyperviscosity Syndrome | 99.81% | L5 | **Hold** | No B-cell/immunoglobulin inhibitory mechanism; no evidence |
| 3 | Congenital Analbuminemia | 99.79% | L5 | **Hold** | Genetic *ALB* mutation disorder; antibiotics have no therapeutic role |
| 4 | Punctate Epithelial Keratoconjunctivitis | 99.78% | L4 | **Research Question** | Plausible: intracellular pathogen coverage (*Chlamydia*, *Microsporidia*); 1 case report |
| 5 | Blood Group Incompatibility | 99.70% | L5 | **Hold** | Immune-mediated haemolysis; no antibody-clearance or complement-inhibition mechanism |
| 6 | Premalignant Haematological System Disease | 99.64% | L5 | **Hold** | MDS/MGUS involve clonal haematopoiesis; no mechanistic or clinical basis |
| 7 | Monoclonal Gammopathy | 99.61% | L5 | **Hold** | No known activity against clonal plasma cells or M-protein production |
| 8 | Haematological Disease with Acquired Peripheral Neuropathy | 99.56% | L5 | **Hold** | ⚠️ Azithromycin *causes* peripheral neuropathy (known ADR); do not pursue |
| 9 | Septicemic Plague | 99.52% | L4 | **Research Question** | In vitro data present but azithromycin showed *poor* activity vs *Y. pestis*; standard therapy preferred |
| 10 | Congenital Haematological Disorder (SCD) | 99.40% | L3 | **Proceed with Guardrails** | Best-supported across all 10: 4 trials, 1 Cochrane review; strong immunomodulatory rationale |

---

## Clinical Trial Evidence

*The top-ranked prediction (Hyperamylasemia) has no registered clinical trials. The table below presents evidence for the most actionable prediction: Congenital Haematological Disorder / Sickle Cell Disease (Rank 10).*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | **Direct relevance — highest grade.** Azithromycin prophylaxis specifically for acute chest syndrome (ACS) prevention in SCD. Withdrawn due to enrolment challenges; withdrawal reason was not a safety signal. Study design confirms scientific and clinical feasibility of this hypothesis. |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | **High relevance.** Macrolide therapy (including azithromycin) to improve FEV1 in adults with SCD. Dual-phase design reflects strong researcher confidence in the lung inflammation pathway. Withdrawn; enrolment reason under investigation. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | **Moderate relevance.** Large paediatric PK/PD and safety study of understudied drugs including azithromycin; provides safety data in children — a population highly relevant to SCD in South Africa. |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Phase 2 | Completed | 10 | **Lower relevance (indirect).** Ibrutinib (not azithromycin) for newly diagnosed chronic graft-versus-host disease post-stem cell transplant; provides background on haematological disorder treatment context. |

No trials were registered on SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) for azithromycin in these indications at time of data cut-off (04 April 2026).

---

## Literature Evidence

*Organised by indication, prioritised by study type.*

### Sickle Cell Disease / Congenital Haematological Disorder (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Cochrane Systematic Review | Cochrane Database of Systematic Reviews | Antibiotic prophylaxis reduces lower respiratory tract infections in high-risk children ≤12 years, with benefit-to-risk favouring use in defined populations. Provides independent evidence for azithromycin prophylaxis in SCD-related pulmonary complications. |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | Case Report | Am J Case Reports | Megadose methylprednisolone for COVID-19-associated immune thrombocytopenia in an infant; limited direct relevance but provides background on haematological complications in the paediatric setting. |

### Punctate Epithelial Keratoconjunctivitis (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult, diagnosed by metagenomic deep sequencing. Azithromycin is noted as a treatment option for microsporidial keratoconjunctivitis; supports mechanistic link via intracellular pathogen coverage. |

### Septicemic Plague (Rank 9)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro Study | Antimicrob Agents Chemother | In vitro susceptibility testing of 78 *Y. pestis* strains against 14 antibiotics. Azithromycin showed **poor activity** against all strains; most active agents were ceftriaxone and ciprofloxacin. Argues strongly against azithromycin for plague. |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Animal Study | Antibiotiki i khimioterapiia | Azithromycin showed high efficacy in experimental brucellosis, with rapid normalisation of bactericidal activity in peripheral blood. Supports macrolide intracellular penetration but not *Y. pestis* specifically. |
| [19392866](https://pubmed.ncbi.nlm.nih.gov/19392866/) | 2009 | Systematic Review | Aliment Pharmacol Ther | Epidemiology and clinical features of travellers' diarrhoea; contextual background for enteric infections where azithromycin is an established treatment. Limited relevance to plague. |
| [31778198](https://pubmed.ncbi.nlm.nih.gov/31778198/) | 2019 | Surveillance Report | Military Medicine | STI surveillance in the US military including *Neisseria gonorrhoeae* and azithromycin-treated infections. Contextual only; not relevant to plague. |
| [10628822](https://pubmed.ncbi.nlm.nih.gov/10628822/) | 2000 | Conference Review | J Med Microbiol | MDR *Salmonella typhi* and emerging resistance to fluoroquinolones and cephalosporins. Contextual infectious disease background only. |

---

## South Africa Market Information

Azithromycin is **not currently registered with SAHPRA** and holds no active product licences in South Africa, as confirmed by the Evidence Pack (0 registered products). This is notable given that azithromycin is:

- Listed on the **WHO Essential Medicines List (EML)** for bacterial infections including trachoma, STIs, and community-acquired pneumonia
- A standard-of-care antibiotic available on South Africa's **National Essential Medicines List (NEML)** and broadly used in the public health sector
- Available internationally under the brand name Zithromax (Pfizer) and numerous generic formulations

The apparent discrepancy between clinical use and the zero SAHPRA registration count may reflect a data gap in the evidence pack rather than true non-availability. Healthcare professionals should consult the SAHPRA medicines register directly for current registration status. If confirmed unregistered, access for specific indications would require the **Section 21 (unregistered medicine) pathway**.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the **online ADR reporting system**.

**Key safety considerations relevant to this Evidence Pack:**

- **Drug-induced pancreatitis and hyperamylasemia:** Azithromycin is a documented cause of elevated serum amylase via drug-induced pancreatitis. This directly invalidates the Rank 1 TxGNN prediction as a therapeutic target and must be communicated clearly to any prescriber.
- **Peripheral neuropathy:** Azithromycin has been associated with peripheral neuropathy as an adverse drug reaction. This directly invalidates the Rank 8 prediction and should not be pursued.
- **QTc prolongation:** Azithromycin prolongs the cardiac QT interval, representing a critical safety concern — particularly for SCD patients who may already have baseline cardiac complications or be receiving other QT-prolonging agents. ECG monitoring is strongly recommended if azithromycin is considered in this population.
- **Drug interactions:** No DDI data was available in this Evidence Pack. A full drug interaction review is required before use, especially in complex haematological patients on multiple medications.

---

## Conclusion and Next Steps

### For Top-Ranked Prediction (Hyperamylasemia, Rank 1)

**Decision: Hold**

**Rationale:**
The top TxGNN prediction almost certainly represents a reverse-detection of azithromycin's known ability to cause drug-induced pancreatitis — a pharmacological association in the wrong causal direction. There is zero clinical or preclinical evidence supporting azithromycin as a treatment for hyperamylasemia, and pursuing this direction would be clinically inappropriate and potentially harmful.

---

### For Best-Supported Prediction (Sickle Cell Disease / Congenital Haematological Disorder, Rank 10)

**Decision: Proceed with Guardrails**

**Rationale:**
Two Phase 1/2 clinical trials were formally registered to test azithromycin's immunomodulatory properties in SCD-related acute chest syndrome and pulmonary complications. Both were withdrawn due to enrolment challenges — not safety concerns — indicating the scientific hypothesis remains valid and clinically relevant. An independent Cochrane systematic review supports antibiotic prophylaxis in high-risk children with respiratory complications, and the mechanistic rationale (NF-κB suppression, cytokine reduction, mucociliary improvement) is well-aligned with SCD pathophysiology. Given the high burden of SCD in southern Africa, this represents a particularly relevant repurposing question for the South African context.

**To proceed, the following is needed:**

- Obtain full MOA data from DrugBank or primary literature (priority: confirm immunomodulatory pathway in haematopoietic stress conditions)
- Investigate and document reasons for trial withdrawals (NCT02630394, NCT02960503) to confirm absence of safety signal
- Confirm current SAHPRA registration status; initiate Section 21 access pathway assessment if confirmed unregistered
- Conduct South African SCD epidemiology and unmet clinical need assessment
- Develop a cardiac safety monitoring protocol addressing azithromycin-associated QTc prolongation in SCD patients
- Review full drug-drug interaction profile, particularly with hydroxyurea, opioids, and other QT-prolonging agents commonly used in SCD management
- Design a feasibility study or South African registry — consider engagement with academic haematology centres in Johannesburg, Cape Town, and Durban

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before clinical application. Healthcare professionals should consult the SAHPRA-approved Professional Information before making any prescribing decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

