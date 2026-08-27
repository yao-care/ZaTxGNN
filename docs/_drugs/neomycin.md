---
layout: default
title: Neomycin
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Neomycin
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

# Neomycin: From Bacterial Infection to Irritable Bowel Syndrome

## One-Sentence Summary

Neomycin is a classical aminoglycoside antibiotic; South African regulatory registration data for its original indication is not currently on file (0 SAHPRA licenses). The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, specifically the methane-positive, constipation-predominant subtype, with **2 clinical trials** and **14 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from SAHPRA/regulatory data (drug not registered in South Africa); as background, neomycin is a non-absorbable aminoglycoside classically used for bacterial infections and gut decontamination |
| Predicted New Indication | Irritable Bowel Syndrome (methane-positive, constipation-predominant subtype) |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, Neomycin is an aminoglycoside antibiotic that is poorly absorbed when given orally and acts locally within the gut lumen — a property that has long supported its use for bowel decontamination and hepatic encephalopathy management.

Irritable bowel syndrome, particularly the methane-positive, constipation-predominant subtype (C-IBS), has been linked to small intestinal bacterial overgrowth (SIBO) and elevated colonic methanogen activity. As a non-absorbable, gut-restricted antibiotic, Neomycin can reduce intestinal methane production and bacterial load — a mechanistic link that is direct rather than a mere statistical co-occurrence in the knowledge graph.

However, the supporting evidence comes largely from small, single- or dual-center trials conducted 15–20 years ago, and repeated antibiotic courses carry known nephrotoxicity/ototoxicity risk. Clinically, Neomycin's role in this niche has been largely superseded by rifaximin, which shows a more favorable safety profile in more recent, larger studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00945334](https://clinicaltrials.gov/study/NCT00945334) | Phase NA | Completed | 37 | Double-blind, placebo-controlled comparison of Neomycin alone vs. Rifaximin+Neomycin in methane-positive, constipation-predominant IBS (conducted with Mayo Clinic and Georgia Regents University) |
| [NCT00259155](https://clinicaltrials.gov/study/NCT00259155) | Phase 2 | Completed | 92 | Multicenter RCT of Rifaximin for SIBO/IBS; Neomycin referenced as the historical antibiotic comparator, noted to normalize the lactulose breath test in 20–25% of cases |

No South African (SANCTR) or Pan-African (PACTR) trial registrations were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16832617](https://pubmed.ncbi.nlm.nih.gov/16832617/) | 2006 | RCT | Digestive Diseases and Sciences | Sub-analysis of a double-blind RCT: Neomycin improved constipation-predominant IBS specifically in patients whose breath test normalized (methane elimination correlated with symptom relief) |
| [19996983](https://pubmed.ncbi.nlm.nih.gov/19996983/) | 2010 | RCT/Cohort | Journal of Clinical Gastroenterology | Combination of Rifaximin + Neomycin was most effective in methane-positive IBS patients versus either agent alone |
| [40240267](https://pubmed.ncbi.nlm.nih.gov/40240267/) | 2025 | Cohort | Revista de Gastroenterología de México (English) | Prospective comparative study of Rifaximin, ciprofloxacin, and Neomycin for SIBO treatment in IBS patients |
| [24788320](https://pubmed.ncbi.nlm.nih.gov/24788320/) | 2014 | Review | Digestive Diseases and Sciences | Reviews antibiotic treatment of constipation-predominant IBS; cites prior retrospective data that Rifaximin+Neomycin outperformed Neomycin alone |
| [30288076](https://pubmed.ncbi.nlm.nih.gov/30288076/) | 2018 | Review | Clinical and Experimental Gastroenterology | Reviews antibiotic mechanisms (including Neomycin) and gut microbiota effects in IBS management |
| [26819502](https://pubmed.ncbi.nlm.nih.gov/26819502/) | 2016 | Review | World Journal of Gastroenterology | Discusses SIBO and infectious mechanisms underlying IBS, supporting rationale for antibiotic therapy |
| [31363445](https://pubmed.ncbi.nlm.nih.gov/31363445/) | 2019 | Review | Cureus | Reviews the relationship between methane production and constipation-predominant IBS |
| [38700306](https://pubmed.ncbi.nlm.nih.gov/38700306/) | 2023 | Review | Journal of the Association of Physicians of India | Reviews gut dysbiosis in IBS, including the role of antibiotics such as Neomycin |
| [24666019](https://pubmed.ncbi.nlm.nih.gov/24666019/) | 2014 | Review | Current Medical Research and Opinion | Reviews probiotics and antimicrobials, including Neomycin, in functional bowel disorder management |
| [19303541](https://pubmed.ncbi.nlm.nih.gov/19303541/) | 2009 | Review | Gastroentérologie Clinique et Biologique | Reviews dietary and pharmacological options for IBS treatment |

---

## South Africa Market Information

Neomycin currently has no SAHPRA product registrations on file (0 licenses; market status: not marketed). No dosage form or approved indication text is available for the South African market.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A blocking data gap exists — TFDA/local PI warnings and contraindications for Neomycin have not yet been retrieved, which prevents a formal S1 safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Neomycin has no current SAHPRA registration in South Africa, and the safety data (warnings, contraindications, drug interactions) required to complete an initial S1 safety review is missing — a blocking gap. While the IBS indication reaches evidence level L2, supporting trials are small, dated, and largely superseded clinically by rifaximin, so the case does not yet support advancing to guardrail-based deployment.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent PI warnings and contraindications (resolves blocking gap DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Assessment of registration pathway/feasibility for the South African market
- Updated, adequately powered trial data on methane-positive IBS-C, ideally benchmarked against rifaximin
- A renal and ototoxicity monitoring protocol, given known aminoglycoside class risk with repeated dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

