---
layout: default
title: Praziquantel
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Praziquantel
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

# Praziquantel: From Schistosomiasis to Plasmodium falciparum Malaria

## One-Sentence Summary

Praziquantel is the standard antiparasitic agent used to treat schistosomiasis (bilharzia) — a use confirmed repeatedly within this evidence pack's own trial and literature records, even though formal regulatory indication text is not available. TxGNN's single highest-scoring prediction is a cluster of soft-tissue sarcomas (leiomyosarcoma-type diagnoses) that carries **no clinical trial or literature support and no plausible mechanistic link** to an antiparasitic drug. The next-ranked, evidence-backed prediction — **Plasmodium falciparum malaria** — is supported by **5 clinical trials** and **20 publications**, including a 2026 double-blind, placebo-controlled randomized trial testing praziquantel directly against *P. falciparum* infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schistosomiasis (inferred from clinical-trial and literature references in this pack; formal SAHPRA-approved indication text is a data gap — DG001) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 97.22% (rank 11,228 of all drug–disease pairs) |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002 — MOA is a documented data gap in this evidence pack). Based on known information within the evidence pack itself, praziquantel is repeatedly described as the mainstay anthelmintic for schistosomiasis (e.g., "Praziquantel (PZQ) remains the sole effective drug against schistosomiasis," PMID 37446846; the SchistoSAM trial NCT03893097 benchmarks a new regimen against "standard praziquantel (PZQ) treatment").

It is worth noting that TxGNN's single top-ranked prediction for this drug (uterine corpus epithelioid leiomyosarcoma, score 97.28%) and several closely-scored neighbours (retroperitoneal sarcoma, uterine myxoid leiomyosarcoma, anus leiomyosarcoma, small intestinal sarcoma, leiomyosarcoma) return **zero clinical trials and zero literature hits**, and there is no known pharmacological rationale connecting an antiparasitic agent to soft-tissue sarcoma biology. This pattern is most consistent with a knowledge-graph embedding artifact rather than a genuine repurposing signal, and it is not carried forward as the headline finding of this report.

By contrast, malaria and other parasitic diseases (fascioliasis, gnathostomiasis) cluster just below the sarcoma group in TxGNN score and are mechanistically coherent: praziquantel's antiparasitic activity against trematodes/cestodes plausibly extends to other parasite life-cycle targets, and this overlap is directly reflected in real-world co-endemic research (schistosomiasis and malaria co-occur across sub-Saharan Africa, and mass drug administration programmes already combine anthelmintic and antimalarial treatment). The strongest single piece of evidence is a purpose-built 2026 RCT (PMID 41159886) directly testing praziquantel's antimalarial efficacy in *P. falciparum*-infected adults.

---

## Clinical Trial Evidence

*(For Plasmodium falciparum malaria; note most of these trials study malaria–helminth co-infection populations where praziquantel is used for deworming, with malaria as a co-measured outcome, rather than dedicated praziquantel-vs-malaria registration trials.)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03640403](https://clinicaltrials.gov/study/NCT03640403) | Phase 3 | Completed | 1,555 | Intermittent preventive treatment trial in school-aged children in Tanzania, in a population where malaria/helminth co-infection and cognitive impact are studied together. |
| [NCT01722539](https://clinicaltrials.gov/study/NCT01722539) | Phase 3 | Completed | 616 | Intermittent preventive antimalarial regimens in DRC schoolchildren; relevant as a co-infection control population where anthelmintic treatment status is tracked. |
| [NCT03893097](https://clinicaltrials.gov/study/NCT03893097) | Phase 3 | Completed | 726 | Head-to-head trial of artesunate-mefloquine vs. standard praziquantel for schistosomiasis in a malaria-endemic Senegalese cohort. |
| [NCT02769013](https://clinicaltrials.gov/study/NCT02769013) | N/A | Completed | 380 | Assesses effect of neglected tropical diseases (incl. helminths treated with praziquantel) on *P. falciparum* transmission dynamics. |
| [NCT00347113](https://clinicaltrials.gov/study/NCT00347113) | N/A | Completed | 620 | Anthelminthic intervention trial evaluating effect on malaria infection/morbidity in Tanzanian school and pre-school children. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41159886](https://pubmed.ncbi.nlm.nih.gov/41159886/) | 2026 | RCT | The Journal of Infectious Diseases | Double-blind, placebo-controlled RCT of praziquantel for *P. falciparum* infection in asymptomatic Gabonese adults — the direct efficacy evidence behind this prediction. |
| [10531774](https://pubmed.ncbi.nlm.nih.gov/10531774/) | 1998 | Clinical study | JPMA (Pakistan Medical Association) | Small case series (9 *P. falciparum*, 1 *P. vivax*) treated with oral praziquantel 30 mg/kg/day; 8/10 achieved complete cure within 4–6 days. |
| [37957702](https://pubmed.ncbi.nlm.nih.gov/37957702/) | 2023 | RCT | Malaria Journal | Randomized, observer-blind trial integrating helminth mass drug administration (praziquantel) with seasonal malaria chemoprevention in Senegalese children; feasible and safe. |
| [25887977](https://pubmed.ncbi.nlm.nih.gov/25887977/) | 2015 | RCT (open-label) | BMC Infectious Diseases | Anthelmintic treatment approaches assessed for impact on malaria infection and anaemia in Tanzanian school/pre-school children. |
| [21696629](https://pubmed.ncbi.nlm.nih.gov/21696629/) | 2011 | Intervention study | BMC Int Health & Human Rights | 33-month follow-up of integrated school-based deworming plus prompt malaria treatment on helminth–*P. falciparum* co-infection. |
| [38265982](https://pubmed.ncbi.nlm.nih.gov/38265982/) | 2024 | Scoping review | PLoS Neglected Tropical Diseases | Reviews prior efforts to integrate malaria and schistosomiasis prevention/control programmes. |
| [20350194](https://pubmed.ncbi.nlm.nih.gov/20350194/) | 2010 | RCT (exploratory, open-label) | Clinical Infectious Diseases | Compares mefloquine, artesunate, mefloquine-artesunate and praziquantel efficacy/safety against *Schistosoma haematobium* in a malaria-endemic setting. |
| [30080853](https://pubmed.ncbi.nlm.nih.gov/30080853/) | 2018 | Cohort study | PLoS Neglected Tropical Diseases | Schistosomiasis (praziquantel-treated) modifies *P. falciparum* infection prevalence/incidence in Gabonese school-age children. |
| [25210876](https://pubmed.ncbi.nlm.nih.gov/25210876/) | 2014 | Prospective cohort | PLoS Neglected Tropical Diseases | Long-term *P. falciparum* carriers co-infected with *S. haematobium* show enhanced protection from febrile malaria in Mali. |
| [24609234](https://pubmed.ncbi.nlm.nih.gov/24609234/) | 2014 | Review | Parasitology Research | Reviews dihydroartemisinin's dual antimalarial/antischistosomal activity, contextualising drug repurposing across these two parasitic diseases. |

---

## South Africa Market Information

No SAHPRA product registrations are present in this evidence pack (`total_licenses: 0`, market status: **not marketed**). No registration number, product name, dosage form, or approved indication text is currently available for praziquantel in South Africa within the data reviewed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug–drug interaction data were queried but returned no results in this evidence pack — flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Praziquantel is not currently marketed or SAHPRA-registered in South Africa, and mandatory safety data (PI warnings/contraindications) is a **Blocking** data gap (DG001) that prevents any S1 safety assessment. While the *Plasmodium falciparum* malaria signal is genuinely evidence-backed — including a 2026 placebo-controlled RCT — it stands alongside a top-ranked TxGNN prediction (leiomyosarcoma/sarcoma cluster) that has no supporting evidence and no plausible mechanism, indicating the raw model ranking should not be used to prioritize indications for this candidate without human review.

**To proceed, the following is needed:**
- SAHPRA-approved PI (warnings, contraindications, DDI) to close DG001 before any safety evaluation
- Confirmed mechanism of action data to close DG002 and support a mechanistic case for the malaria indication
- Determination of whether SAHPRA registration/import pathway exists for praziquantel in South Africa
- A confirmatory, adequately powered RCT of praziquantel specifically for *P. falciparum* malaria (current evidence is one small RCT plus mostly co-infection/observational studies)
- Independent review confirming the leiomyosarcoma/sarcoma cluster of predictions should be deprioritized given the absence of any corroborating evidence or mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

