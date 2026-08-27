---
layout: default
title: Oseltamivir
parent: 僅模型預測 (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pneumonia (Influenza-Associated)

> **Candidate selection note**: TxGNN's highest-scoring prediction for Oseltamivir was *pyelonephritis* (97.85%), but the evidence pack's own review flags this as co-occurrence noise with no plausible mechanism (an antiviral drug has no antibacterial activity against a bacterial kidney infection). Ranks 2–7 and 10 are similarly flagged as noise with L5/Hold status. Of the ten predictions, only *pneumonia* (rank 8) and *streptococcal pneumonia* (rank 9) carry actual supporting evidence (L4, decision stage S1, "Research Question"). This report focuses on **pneumonia**, the most evidence-supported candidate.

## One-Sentence Summary

Oseltamivir is a neuraminidase inhibitor established for treatment and prophylaxis of influenza A and B. The TxGNN model predicts a possible role in **preventing/reducing severe pneumonia** (viral and secondary bacterial) associated with influenza, supported by **50 clinical trials** and **20 publications**, though the mechanism is indirect and not yet clinically confirmed as a standalone pneumonia treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack (no SAHPRA licenses on file); based on known pharmacology, Oseltamivir is indicated for treatment/prophylaxis of Influenza A and B |
| Predicted New Indication | Pneumonia (influenza-associated, viral and secondary bacterial) |
| TxGNN Prediction Score | 92.14% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacological knowledge, Oseltamivir is a neuraminidase inhibitor that blocks release of newly formed influenza virus particles from infected respiratory epithelial cells, limiting viral spread within the airway.

Influenza infection is a well-documented risk factor for progression to pneumonia — both primary viral pneumonia and secondary bacterial pneumonia (notably *Streptococcus pneumoniae* and *Staphylococcus aureus*, including PVL-producing strains causing necrotizing pneumonia). Since Oseltamivir reduces viral replication, it may plausibly lower the incidence or severity of this downstream complication by shortening the window of viral-mediated epithelial damage that predisposes to bacterial superinfection.

This is an **indirect, adjunctive mechanism**, not a direct antimicrobial or anti-inflammatory effect on pneumonia itself. Preclinical work (e.g., McCullers 2004, PMID 15243927) shows oseltamivir improves survival in mouse models of post-influenza pneumococcal pneumonia, and observational/cohort data in humans associate early oseltamivir treatment with reduced pneumonia risk — but no trial has been designed with pneumonia (rather than influenza) as the primary endpoint. This is why the evidence pack scores this candidate L4 / decision stage S1 ("Research Question") rather than a stronger tier.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01248715](https://clinicaltrials.gov/study/NCT01248715) | Phase 4 | Completed | 1107 | Effectiveness of empiric antiviral treatment for hospitalized community-acquired pneumonia during influenza season |
| [NCT00707941](https://clinicaltrials.gov/study/NCT00707941) | Phase 3 | Completed | 1190 | Oseltamivir efficacy in reducing illness duration, viral shedding, and household transmission (Dhaka, Bangladesh cohort) |
| [NCT00545532](https://clinicaltrials.gov/study/NCT00545532) | Phase 3 | Completed | 228 | Conventional vs double-dose oseltamivir in immunocompromised influenza patients — a group at elevated pneumonia risk |
| [NCT01620307](https://clinicaltrials.gov/study/NCT01620307) | Phase 2 | Completed | 38 | Adjuvant mTOR inhibitor (rapamune) for severe H1N1 pneumonia with respiratory failure (oseltamivir as background therapy) |
| [NCT03900988](https://clinicaltrials.gov/study/NCT03900988) | Phase 3 | Unknown | 160 | IV N-acetylcysteine + oseltamivir vs dextrose + oseltamivir in influenza complicated by lower respiratory tract infection |
| [NCT00936013](https://clinicaltrials.gov/study/NCT00936013) | Phase 4 | Unknown | 400 | Chinese medicinal herbs + oseltamivir vs oseltamivir alone for H1N1 influenza pneumonia |
| [NCT02561169](https://clinicaltrials.gov/study/NCT02561169) | Phase 4 | Terminated (n=1) | 1 | RCT of oseltamivir vs placebo in high-risk ED patients with influenza; primary outcome hospitalization |
| [NCT02282384](https://clinicaltrials.gov/study/NCT02282384) | Phase 4 | Withdrawn | 0 | Pilot RCT of oseltamivir in outpatients with chronic pulmonary disease (feasibility study) |
| [NCT00958776](https://clinicaltrials.gov/study/NCT00958776) | Phase 3 | Terminated | 405 | IV peramivir + standard of care vs standard of care alone (incl. oseltamivir) in hospitalized serious influenza |
| [NCT05648448](https://clinicaltrials.gov/study/NCT05648448) | Phase 2 | Recruiting | 3000 | AD ASTRA adaptive platform trial comparing antiviral pharmacodynamics, including oseltamivir, in early influenza |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24718923](https://pubmed.ncbi.nlm.nih.gov/24718923/) | 2014 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of neuraminidase inhibitors for preventing/treating influenza in adults and children |
| [40050867](https://pubmed.ncbi.nlm.nih.gov/40050867/) | 2025 | Review | Virology Journal | Antiviral treatment options for viral pneumonia, including oseltamivir's mechanism |
| [35993199](https://pubmed.ncbi.nlm.nih.gov/35993199/) | 2022 | Review | Journal of Global Health | Role of adjunctive oseltamivir, steroids, macrolides, vitamins for severe pneumonia in children (LMIC) |
| [31189475](https://pubmed.ncbi.nlm.nih.gov/31189475/) | 2019 | Review | Critical Care | Prevention, diagnosis and treatment of influenza-related critical illness |
| [39172994](https://pubmed.ncbi.nlm.nih.gov/39172994/) | 2025 | Cohort (FluSurv-NET) | Clinical Infectious Diseases | Timing of influenza antiviral therapy and risk of death in adults with influenza-associated pneumonia |
| [15243927](https://pubmed.ncbi.nlm.nih.gov/15243927/) | 2004 | Preclinical (mouse model) | Journal of Infectious Diseases | Oseltamivir improved survival (0%→75%) in mouse model of secondary pneumococcal pneumonia after influenza |
| [21760915](https://pubmed.ncbi.nlm.nih.gov/21760915/) | 2011 | Retrospective Cohort | PLoS ONE | Early oseltamivir administration reduced occurrence/severity of pandemic H1N1-associated pneumonia (Mexico) |
| [15969875](https://pubmed.ncbi.nlm.nih.gov/15969875/) | 2005 | Review | Current Medical Research and Opinion | Risk of pneumonia and other complications of influenza-like illness in oseltamivir-treated patients |
| [32527739](https://pubmed.ncbi.nlm.nih.gov/32527739/) | 2020 | Retrospective Cohort | European Respiratory Journal | Oseltamivir and influenza-related complications in children in primary care |
| [39189087](https://pubmed.ncbi.nlm.nih.gov/39189087/) | 2024 | Retrospective Cohort | Influenza and Other Respiratory Viruses | Comparison of baloxavir vs oseltamivir effectiveness in preventing hospitalization/pneumonia in influenza B |

## South Africa Market Information

Oseltamivir currently has **no SAHPRA registrations on file** in this Evidence Pack (`market_status: 未上市` / Not marketed, `total_licenses: 0`). No product name, dosage form, or approved indication text is available for South Africa at this time.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: Key warnings, contraindications, and DDI data are flagged as Blocking data gaps (DG001) in this Evidence Pack and could not be assessed here.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The pneumonia signal has real but indirect mechanistic support (L4, decision stage S1, "Research Question") — no trial has tested oseltamivir with pneumonia as a primary endpoint, and the drug has no direct antimicrobial activity against the bacterial pathogens implicated in secondary pneumonia.
- Oseltamivir has zero SAHPRA registrations and is not currently marketed in South Africa, and safety data (warnings, contraindications, DDI) is a **Blocking** data gap — these must be resolved before any S1 safety screening can proceed.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, drug interactions (DG001, Blocking)
- Confirmed mechanism of action data via DrugBank/other pharmacological source (DG002, High)
- Clarification of SAHPRA registration pathway/status for Oseltamivir in South Africa
- A dedicated trial or well-controlled observational study evaluating oseltamivir's effect specifically on pneumonia incidence/severity as a primary (not secondary) endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

