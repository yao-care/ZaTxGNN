---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Artemether: predicted new indication Plasmodium falciparum malaria . The rank 1 prediction… (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Artemether"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Artemether: From Malaria (Registered Antimalarial Use) to Plasmodium falciparum Malaria

## One-Sentence Summary

Artemether is an artemisinin-derivative antimalarial. In South Africa it is registered as a component of the fixed-dose combination Coartem (artemether-lumefantrine).
The TxGNN model's second-ranked prediction is **Plasmodium falciparum malaria**, supported by **30 listed clinical trials** and **20 publications**. This is an established, marketed use rather than true repurposing.
The other top-10 predictions (angioedema variants, scleroderma, conjunctivitis and others) have **no supporting trials or literature** and are model predictions only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the SAHPRA licence record has no indication text); in practice, treatment of malaria |
| Predicted New Indication | Plasmodium falciparum malaria (rank 2). The rank 1 prediction, acquired angioedema, has no supporting evidence. |
| TxGNN Prediction Score | 99.77% (rank 1, acquired angioedema: 99.90%) |
| Evidence Level | L1 (for P. falciparum malaria); L5 for angioedema and the other non-malaria predictions |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails (P. falciparum malaria); Hold (all other predictions) |

---

## Why is This Prediction Reasonable?

Artemether is an artemisinin derivative. Its endoperoxide bridge is activated by heme iron inside parasite-infected red blood cells. This produces free radicals that damage parasite proteins and membranes and clear parasites rapidly. It is used with lumefantrine as a first-line artemisinin-based combination therapy (ACT). Detailed mechanism-of-action data were not available in the drug record compiled for this report, so this description reflects the pharmacology of the artemisinin class.

The P. falciparum malaria prediction is therefore not a novel repurposing idea. It reflects the drug's existing, marketed use, which explains the strong trial and literature support. The same mechanism also applies to malaria in general (rank 3). Intramuscular artemether has been studied in severe malaria. Its efficacy there is comparable to quinine but inferior to artesunate.

For the non-malaria predictions, no credible mechanistic link was identified:
- **Angioedema group** (acquired, hereditary and RAAS-blocker-induced angioedema): these conditions involve the kallikrein-kinin, C1-inhibitor and bradykinin pathways, on which artemether has no known action. The high scores probably reflect network similarity between disease terms rather than pharmacology.
- **Nephrogenic syndrome of inappropriate antidiuresis**: caused by vasopressin V2 receptor mutations, with no known artemether activity.
- **Scleroderma**: only a weak, hypothetical link through preclinical anti-fibrotic effects of artemisinins.
- **Conjunctivitis (including acute contagious)**: speculative antimicrobial or anti-inflammatory rationale only.

---

## Clinical Trial Evidence

The table below shows the 10 most relevant trials for P. falciparum malaria. Most trials test artemether-lumefantrine (the combination), not artemether alone. No SANCTR or PACTR identifiers were available in the data compiled for this report.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Completed | 1272 | Double-blind, double-dummy comparison of pyronaridine-artesunate vs Coartem in children and adults (Africa and South-East Asia) |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Completed | 323 | In vivo efficacy of artemisinin combination therapies in Tanzanian children aged 6-59 months |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Completed | 361 | Azithromycin plus chloroquine vs artemether-lumefantrine (comparator) in African children |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Completed | 452 | In vivo efficacy of artemether-lumefantrine and artesunate-amodiaquine in Malawi |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Completed | 340 | Artemether-lumefantrine vs artesunate-amodiaquine under real-life conditions in Burkina Faso |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Completed | 267 | Suspension vs tablet formulation in Kenyan children under five |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Completed | 305 | Extended-duration dosing in children, including HIV-infected children on efavirenz-based ART |
| [NCT05060198](https://clinicaltrials.gov/study/NCT05060198) | Not applicable | Completed | 340 | Efficacy of artemether-lumefantrine and dihydroartemisinin-piperaquine in western Kenya |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | Recruiting | 1680 | Fixed-dose triple ACT (artemether-lumefantrine-amodiaquine) vs standard ACTs |
| [NCT01998295](https://clinicaltrials.gov/study/NCT01998295) | Phase 4 | Completed | 45 | Parasite clearance time and recurrence after artemether-lumefantrine in Tanzanian children |

The data also list further trials for the broader "malaria" prediction, including a Phase 3 trial in pregnant African women (NCT00852423, 3428 participants) and Phase 3 trials in Cameroon and Kenya. The angioedema, nephrogenic SIAD, scleroderma and conjunctivitis predictions have no registered trials.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Meta-analysis | PLoS One | Efficacy of artemether-lumefantrine and other ACTs in sub-Saharan Africa |
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Meta-analysis | Malaria Journal | Efficacy and safety of artemether-lumefantrine in Ethiopia |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Meta-analysis of RCTs | Malaria Journal | Safety of dihydroartemisinin-piperaquine vs artemether-lumefantrine in African children |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic review | Malaria Journal | Safety and efficacy of artemether-lumefantrine in pregnancy |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Cochrane review | Cochrane Database Syst Rev | Intramuscular artemether for severe malaria compared with quinine and artesunate |
| [40845863](https://pubmed.ncbi.nlm.nih.gov/40845863/) | 2026 | Phase 4 RCT | Lancet Infect Dis | Efficacy of four ACTs in Ugandan children, amid concern about declining ACT efficacy in east Africa |
| [1346408](https://pubmed.ncbi.nlm.nih.gov/1346408/) | 1992 | RCT | Lancet | Artemether vs chloroquine for severe malaria in Gambian children |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Study | J Infect Dis | Artemether-lumefantrine treatment selects pfmdr1 increased copy number in African infections; reduced efficacy has recently emerged |
| [41327422](https://pubmed.ncbi.nlm.nih.gov/41327422/) | 2025 | Efficacy study | Malaria Journal | Reduced artemether-lumefantrine efficacy in Burkina Faso since 2008 |
| [16258328](https://pubmed.ncbi.nlm.nih.gov/16258328/) | 2005 | Review | Curr Opin Infect Dis | Artemisinin-based combinations as first-line treatment worldwide |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 34/20.2.6 /0161 | Coartem | Tablet (oral) | Not recorded in the data compiled for this report |

Essential Medicines List (EML) status was not available in the data compiled for this report and should be checked against the current South African EML.

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (disease-level contraindication links, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes and potassium deficiency disease. These point to a QT-prolongation concern. A Phase 1 QT study of a related artemisinin combination (NCT01103830) has been conducted.
- **Drug interactions**: 95 interactions were identified. Major-level interactions include clarithromycin, cobicistat, amprenavir, atazanavir, apalutamide and boceprevir. Moderate-level interactions include dexamethasone, miconazole, troglitazone, deferasirox, bosentan, bexarotene and armodafinil. These are largely CYP-related. Pharmacokinetic studies in the data also address interactions with antiretrovirals (dolutegravir, nevirapine, efavirenz), which matters in South Africa's high HIV burden.
- **Resistance signal**: recent publications report reduced artemether-lumefantrine efficacy in parts of Africa, so local efficacy monitoring is important.

Warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (P. falciparum malaria and malaria). **Hold** (acquired angioedema, angioedema, hereditary angioedema, RAAS-blocker-induced angioedema, nephrogenic SIAD, scleroderma, acute contagious conjunctivitis, conjunctivitis).

**Rationale:**
- Malaria has Level L1 evidence: multiple completed Phase 3 trials and systematic reviews support artemether-lumefantrine, which is already registered in South Africa as Coartem. It is established use, not new repurposing.
- The other predictions, including the top-scoring acquired angioedema (99.90%), have no trials or literature and no plausible mechanism. The high scores should not be taken as clinical support.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication text), the main gap blocking safety screening
- Drug-record mechanism-of-action data
- A QT-risk and interaction management plan, including antiretroviral co-therapy and patients with long QT or electrolyte disturbance
- Local surveillance of efficacy given emerging artemisinin partial resistance in Africa
- EML status confirmation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

