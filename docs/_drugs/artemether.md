---
layout: default
title: Artemether
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From WHO-Recommended Antimalarial to Plasmodium falciparum Malaria in South Africa

## One-Sentence Summary

Artemether is an artemisinin derivative and core component of artemether-lumefantrine (Coartem®), the WHO first-line combination therapy for uncomplicated malaria — yet it holds **zero SAHPRA registrations** in South Africa.
The TxGNN model confirms **Plasmodium falciparum Malaria** as its primary actionable prediction (rank 2, score 99.77%), supported by **10+ completed Phase 3/4 RCTs** and **20 publications**, including multiple Cochrane systematic reviews.
The highest-ranked prediction (acquired angioedema, rank 1, score 99.99%) has been identified as a **knowledge graph false positive** with no supporting clinical evidence and is not recommended for further evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | WHO first-line antimalarial; artemether-lumefantrine (AL/Coartem®) is the global standard of care for uncomplicated *Plasmodium falciparum* malaria |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.77% (rank 2) |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed in South Africa |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Artemether contains an endoperoxide bridge that, upon entering parasitised erythrocytes, reacts with ferrous iron (Fe²⁺) released during haemoglobin degradation. This reaction generates carbon-centred free radicals and reactive oxygen species (ROS) that directly damage *P. falciparum* proteins, lipids, and cell membranes. A secondary mechanism involves inhibition of PfATP6 — a *P. falciparum*-specific SERCA-like Ca²⁺-ATPase — which disrupts parasite calcium homeostasis. Critically, the selectivity of this mechanism for parasitised (iron-rich) cells over healthy human erythrocytes explains the drug's therapeutic window.

The ROS-generating endoperoxide mechanism is effective across multiple *Plasmodium* species (*P. falciparum*, *P. vivax*, *P. ovale*, *P. malariae*), making artemether a broad-spectrum antimalarial. This mechanistic breadth is validated by two independent Cochrane systematic reviews (PMID 31210357, 25209020) and by the WHO's designation of artemether-lumefantrine as first-line therapy in 86 countries, including 30 of 47 sub-Saharan African nations.

Despite this global evidence base, artemether carries **zero SAHPRA registrations** in South Africa. This creates a regulatory gap in a country where malaria remains endemic in Limpopo, Mpumalanga, and KwaZulu-Natal, and where the National Department of Health already recommends artemether-lumefantrine as standard of care. Formalising SAHPRA registration would strengthen supply chain assurance, enable structured pharmacovigilance, and support rational prescribing — particularly important given South Africa's significant HIV/malaria co-infection burden and the well-documented pharmacokinetic interactions between AL and antiretroviral therapy.

---

## Note on Rank 1 Prediction: Acquired Angioedema

> **Assessment: False Positive — Do Not Pursue**
>
> TxGNN assigned its highest score (99.99%) to **acquired angioedema** (AAE). AAE is caused by acquired C1-esterase inhibitor deficiency (typically secondary to B-cell malignancy or autoantibodies), leading to bradykinin accumulation and increased vascular permeability. Artemether's mechanism — ROS generation and PfATP6 inhibition — has **no connection** to the complement pathway or bradykinin system. There are zero clinical trials and zero publications supporting this use. The high TxGNN score is attributed to structural clustering of angioedema-class nodes in the knowledge graph rather than pharmacological relevance. Predictions for angioedema (ranks 1, 4, 5, 10) all carry the same false-positive signature and are uniformly recommended as **Hold**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05842954](https://clinicaltrials.gov/study/NCT05842954) | Phase 3 | Completed | 1,720 | KLU156 (ganaplacide + lumefantrine-SDF) vs. Coartem® as active comparator in adults and children ≥10 kg with uncomplicated *P. falciparum* malaria; large-scale validation of AL as the standard benchmark |
| [NCT01651416](https://clinicaltrials.gov/study/NCT01651416) | Phase 4 | Completed | 2,400 | Seasonal malaria chemoprevention vs. long-acting artemisinin combination therapy for prevention of malaria and anaemia in children in extended transmission settings, Ghana |
| [NCT00885287](https://clinicaltrials.gov/study/NCT00885287) | Phase 4 | Completed | 830 | Therapeutic efficacy, safety, and pharmacokinetic interactions of artemether-lumefantrine with nevirapine-based antiretrovirals in HIV-infected patients with uncomplicated falciparum malaria, Tanzania — directly relevant to South Africa's HIV co-infection context |
| [NCT00344006](https://clinicaltrials.gov/study/NCT00344006) | Phase 3 | Completed | 1,395 | Multicentre double-blind double-dummy RCT: chlorproguanil-dapsone-artesunate vs. artemether-lumefantrine in children and adolescents with uncomplicated *P. falciparum* malaria across Africa |
| [NCT00316329](https://clinicaltrials.gov/study/NCT00316329) | Phase 3 | Completed | 1,032 | Multinational RCT comparing artesunate-amodiaquine (once or twice daily dosing) vs. Coartem® for uncomplicated *P. falciparum* malaria; non-inferiority design across multiple African sites |
| [NCT01845701](https://clinicaltrials.gov/study/NCT01845701) | Phase 3 | Completed | 720 | 42-day follow-up comparing artesunate-amodiaquine and dihydroartemisinin-piperaquine vs. artemether-lumefantrine in children with *P. falciparum* malaria in two ecological zones, Cameroon |
| [NCT01916954](https://clinicaltrials.gov/study/NCT01916954) | Phase 3 | Completed | 96 | Direct comparison of two AL dosing regimens for *P. falciparum* treatment in pregnant women, Democratic Republic of Congo; addresses special population safety gap |
| [NCT00540410](https://clinicaltrials.gov/study/NCT00540410) | Phase 4 | Completed | 366 | Head-to-head RCT: artesunate+amodiaquine vs. artemether+lumefantrine for repeated uncomplicated *P. falciparum* episodes over 2 years, Senegal; includes QTc cardiac tolerability assessment |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Completed | 267 | AL suspension vs. tablets in children aged 6–59 months with uncomplicated *P. falciparum* malaria, Kenya; paediatric formulation comparison directly relevant to child dosing |
| [NCT02090036](https://clinicaltrials.gov/study/NCT02090036) | Phase 4 | Completed | 220 | Efficacy and safety of single low-dose primaquine added to standard AL for *P. falciparum* gametocyte clearance; supports AL as platform for transmission-blocking strategies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Systematic Review & Meta-analysis | *PLoS One* | Therapeutic efficacy of AL, ASAQ, and DHA-PQ for uncomplicated *P. falciparum* in Sub-Saharan Africa; confirms AL as consistently effective first-line ACT |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Cochrane Systematic Review | *Cochrane Database Syst Rev* | Intramuscular artemether vs. quinine and artesunate for severe malaria; supports artemether efficacy in severe disease |
| [25209020](https://pubmed.ncbi.nlm.nih.gov/25209020/) | 2014 | Cochrane Systematic Review | *Cochrane Database Syst Rev* | Earlier Cochrane review confirming artemether vs. quinine for severe malaria; foundational evidence base |
| [37979594](https://pubmed.ncbi.nlm.nih.gov/37979594/) | 2023 | RCT | *Lancet* | PRIMA trial: primaquine radical cure in *P. falciparum*/*P. vivax* co-endemic settings; AL used as ACT backbone — demonstrates AL's role in combination strategies |
| [38705163](https://pubmed.ncbi.nlm.nih.gov/38705163/) | 2024 | Phase 2 RCT | *Lancet Microbe* | AL ± single-dose primaquine vs. SP+amodiaquine ± tafenoquine for gametocyte carriage reduction and transmission blockade, Mali |
| [34384431](https://pubmed.ncbi.nlm.nih.gov/34384431/) | 2021 | Systematic Review & Meta-analysis | *Malaria Journal* | DHA-PQ vs. AL efficacy for uncomplicated *P. falciparum* in Africa; AL remains the well-characterised standard comparator |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Systematic Review & Meta-analysis | *Malaria Journal* | Comprehensive safety comparison of DHA-PQ vs. AL for uncomplicated *P. falciparum* in African children; AL safety profile well-documented |
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Systematic Review & Meta-analysis | *Malaria Journal* | Efficacy and safety of AL for uncomplicated *P. falciparum* in Ethiopia; high PCR-corrected cure rates across multiple studies |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Systematic Review | *Malaria Journal* | Safety and efficacy of AL for uncomplicated *P. falciparum* during pregnancy; underpins WHO recommendation for second/third trimester use |
| [23419113](https://pubmed.ncbi.nlm.nih.gov/23419113/) | 2013 | Expert Review | *Expert Opin Pharmacother* | AL for uncomplicated *P. falciparum* in sub-Saharan Africa; approved in 86 countries, first-line in 30/47 sub-Saharan African countries — contextualises the SA registration gap |

---

## South Africa Market Information

Artemether is currently **not registered with SAHPRA** and there are **no approved products** on the South African market.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|--------------------|-------------|-------------|---------------------|
| — | No SAHPRA-registered products | — | — |

**Practical context for South African prescribers:**

- Access to artemether-lumefantrine (Coartem®) in South Africa currently occurs via:
  - **Section 21 authorisation** (unregistered medicine access, SAHPRA approval required per patient or per programme)
  - **Government procurement** through National Department of Health malaria programmes aligned with WHO/Global Fund supply channels
- Artemether-lumefantrine is included on the **WHO Essential Medicines List** and the **South African Essential Drugs Programme (EDP)** formulary for use in malaria-endemic provinces (Limpopo, Mpumalanga, KwaZulu-Natal)
- Formal SAHPRA registration would enable routine commercial availability, structured pharmacovigilance, and inclusion in provincial formularies

---

## Safety Considerations

Detailed SAHPRA-specific safety labelling data are not available in this evidence pack. Based on global clinical trial data, the following are clinically important for the South African context:

**Drug Interactions (particularly relevant given South Africa's HIV/malaria co-infection burden):**
- Artemether-lumefantrine is metabolised via **CYP3A4** (artemether) and **CYP3A4/CYP2D6** (lumefantrine)
- **Efavirenz**: reduces lumefantrine AUC by approximately 50% — standard AL dosing may be insufficient in HIV patients on efavirenz-based ART; double-dose AL or alternative ACT should be considered
- **Nevirapine**: reduces lumefantrine exposure by approximately 40%
- **Ritonavir-boosted protease inhibitors** (e.g., lopinavir/ritonavir): may increase lumefantrine exposure and QTc prolongation risk
- **QTc-prolonging agents**: AL prolongs the QTc interval; avoid concurrent use with other QTc-prolonging drugs (antifungals, fluoroquinolones, antipsychotics)

> Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information once registered. Report suspected adverse drug reactions to SAHPRA using the **MedSafety** online reporting system (www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Artemether-lumefantrine has overwhelming L1 evidence — multiple completed Phase 3/4 RCTs enrolling thousands of patients and two independent Cochrane systematic reviews — confirming efficacy and safety for *Plasmodium falciparum* malaria across sub-Saharan Africa. It is already recommended by South Africa's National Department of Health and administered in malaria-endemic provinces, but the absence of formal SAHPRA registration creates a pharmacovigilance blind spot, supply chain vulnerability, and prescribing uncertainty — all of which formal registration would address.

**To proceed, the following is needed:**

- **SAHPRA registration application**: submit a complete Common Technical Document (CTD) dossier for artemether-lumefantrine fixed-dose combination, including quality, safety, and efficacy modules; bioequivalence/PK data
- **South Africa-specific Professional Information (PI)**: develop SAHPRA-compliant labelling addressing key SA-relevant concerns — antiretroviral drug interactions (efavirenz, nevirapine, ritonavir), pregnancy safety, and G6PD deficiency guidance
- **HIV/malaria co-infection sub-study data**: formal review or prospective data collection on AL dosing strategies in South African patients on efavirenz- or nevirapine-based ART (Limpopo, Mpumalanga, KwaZulu-Natal enrolment sites recommended)
- **Pharmacovigilance plan**: establish structured ADR monitoring and reporting through SAHPRA's MedSafety system for all malaria-endemic provinces
- **EML formal listing**: pursue inclusion on national and provincial Essential Medicines Lists with specific malaria-endemic province formulary entries to ensure equitable access and procurement visibility

---

> **Disclaimer:** This report is generated for research and drug repurposing evaluation purposes only and does not constitute medical advice or a prescribing recommendation. Drug repurposing predictions from the TxGNN model are investigational and require clinical validation before therapeutic application. All prescribing decisions must be based on current SAHPRA-approved Professional Information and applicable South African treatment guidelines. This report does not replace clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

