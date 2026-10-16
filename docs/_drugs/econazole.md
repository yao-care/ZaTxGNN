---
layout: default
title: Econazole
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Econazole: predicted new indication Ectothrix infectious disease (evidence level L5). Approved use: Tinea pedis, tinea corporis, cutaneous candidiasis…"
---

# Econazole
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

# Econazole: From Superficial Fungal Skin Infections to Ectothrix Infectious Disease

## One-Sentence Summary

Econazole is a topical imidazole antifungal, originally used for tinea (pedis, corporis), cutaneous candidiasis and pityriasis versicolor.
The TxGNN model's top-ranked prediction is **ectothrix infectious disease** (a dermatophyte infection of the hair shaft), but **no clinical trials and no publications** support it.
The best-supported prediction in the data is **vulvovaginal candidiasis**, with **no registered trials** but **about 20 publications**, several of them comparative studies of econazole.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, cutaneous candidiasis, pityriasis versicolor (the SAHPRA records compiled for this report contain no approved indication text) |
| Predicted New Indication | Ectothrix infectious disease (rank 1) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

**Other predictions in the data (for context):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Majocchi granuloma | 99.97% | L4 | Hold |
| 3 | Endothrix infectious disease | 99.97% | L5 | Hold |
| 4 | Superficial mycosis | 99.97% | L4 | Hold |
| 5 | Dermatophytosis of scalp or beard | 99.97% | L4 | Hold |
| 6 | Tinea profunda | 99.96% | L5 | Hold |
| 7 | **Vulvovaginal candidiasis** | 99.50% | L3 | **Proceed with Guardrails** |
| 8 | Vulvovaginitis | 98.70% | L3 | Research question |
| 9 | Acne | 98.63% | L4 | Hold |
| 10 | Postmenopausal atrophic vaginitis | 98.24% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Econazole is an imidazole antifungal. As a class, imidazoles inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which disrupts ergosterol synthesis and damages the fungal membrane. Its efficacy in tinea and cutaneous candidiasis is established.

**Ectothrix infection (rank 1)** is caused by dermatophytes such as *Microsporum* and *Trichophyton* that grow on the outside of the hair shaft. These are the same organism groups econazole treats in tinea corporis and pedis, which explains the high score. However, topical agents penetrate the hair shaft and follicle poorly, so systemic therapy is usually required. The score appears to reflect similarity to the approved tinea indications rather than any direct evidence.

**Vulvovaginal candidiasis (rank 7)** involves *Candida*, the same pathogen as econazole's approved cutaneous candidiasis indication. The mechanistic fit is strongest here, and it is supported by clinical comparisons (see below). One of the two SAHPRA-registered products is a vaginal cream, so this use may already be part of local practice.

**Weak predictions:** Postmenopausal atrophic vaginitis (caused by oestrogen deficiency) has no biological rationale. Acne is linked only through *Malassezia* folliculitis, which can mimic acne but is a different condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for ectothrix infectious disease or for any of the other nine predicted indications.

---

## Literature Evidence

**Ectothrix infectious disease:** Currently no related literature available.

For the most relevant prediction with literature, **vulvovaginal candidiasis**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7820892](https://pubmed.ncbi.nlm.nih.gov/7820892/) | 1994 | Double-blind comparative study | Ceylon Med J | Econazole vs clotrimazole in vaginal candidiasis |
| [7383476](https://pubmed.ncbi.nlm.nih.gov/7383476/) | 1980 | Randomised comparison | Obstet Gynecol | 1% econazole vaginal cream vs clotrimazole tablets for 7 days in 178 women; comparable mycological cure rates and low local adverse reactions |
| [984105](https://pubmed.ncbi.nlm.nih.gov/984105/) | 1976 | Multicentric open study | Am J Obstet Gynecol | 3-day econazole 150 mg suppositories in 996 women; 93.4% cure in studies I and II |
| [2257961](https://pubmed.ncbi.nlm.nih.gov/2257961/) | 1990 | Comparative study | J Int Med Res | Butoconazole 3 days vs econazole 7 days, randomised, single-blind, 75 patients |
| [6761088](https://pubmed.ncbi.nlm.nih.gov/6761088/) | 1982 | Multicentre comparative study | Chemotherapy | Clotrimazole tablets vs econazole ovules, 3-day therapy |
| [11118564](https://pubmed.ncbi.nlm.nih.gov/11118564/) | 2000 | Comparative study | Int J Gynaecol Obstet | Sertaconazole vs econazole sustained-release suppositories |
| [98315](https://pubmed.ncbi.nlm.nih.gov/98315/) | 1978 | Review | Drugs | Econazole antifungal activity and therapeutic efficacy |
| [18606589](https://pubmed.ncbi.nlm.nih.gov/18606589/) | 2008 | Clinical study | J Chemother | Econazole-polycarbophil bioadhesive vaginal ovules in 180 women |
| [25442913](https://pubmed.ncbi.nlm.nih.gov/25442913/) | 2014 | In vitro study | J Mycol Med | Susceptibility of 200 *Candida* isolates to imidazoles and nystatin; non-albicans species respond less well to imidazoles |
| [37601561](https://pubmed.ncbi.nlm.nih.gov/37601561/) | 2023 | In vitro study | Infect Drug Resist | Biofilm formation and azole resistance in *C. albicans* from VVC |

**Other predictions with limited evidence:**
- **Superficial mycosis:** The records are mostly reviews of other azoles (bifonazole, sulconazole, tioconazole, sertaconazole), plus a [follow-up study of 100 patients](https://pubmed.ncbi.nlm.nih.gov/7351270/) treated with econazole 1% (± triamcinolone), in which 95% of followed patients had no relapse. This is effectively an on-label use.
- **Scalp/beard dermatophytosis:** Evidence is indirect, mainly [PMID 19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) (review) and case reports where topical econazole was used alongside oral therapy ([12950911](https://pubmed.ncbi.nlm.nih.gov/12950911/), [20521116](https://pubmed.ncbi.nlm.nih.gov/20521116/)).
- **Majocchi granuloma:** One general [case report](https://pubmed.ncbi.nlm.nih.gov/37899944/) (2023), not specific to econazole.
- **Acne:** One [1995 study](https://pubmed.ncbi.nlm.nih.gov/8593718/) on *Pityrosporum* folliculitis, a different condition.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| R/18.6/179 | Gyno-Pevaryl Depot | Vaginal cream | Not available in the data compiled |
| Q/13.4.1/0220 | Pevisone | Cream | Not available in the data compiled |

Both registrations are valid single-ingredient entries. Essential Medicines List (EML) status is not available in the data compiled for this report.

---

## Safety Considerations

- **Drug Interactions:** 41 potential interactions were identified, with interaction severity not graded. Examples include clotrimazole, fluconazole, metformin, glipizide, rosiglitazone, omeprazole, lansoprazole, clopidogrel, heparin, dexamethasone, fluticasone, levothyroxine, diazepam, lorazepam, loperamide, cytarabine, didanosine and acyclovir. These are most relevant if there is meaningful systemic absorption (for example, damaged skin or mucosa, or extensive use).

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked indication, ectothrix infectious disease)

**Rationale:**
- The high TxGNN score reflects similarity to approved tinea indications, with no trials or publications. Topical therapy is also unlikely to reach infected hair shafts, and systemic therapy is standard.
- The most promising candidate is **vulvovaginal candidiasis** (**Proceed with Guardrails**). It has several comparative clinical studies of econazole and a marketed vaginal cream in South Africa, but the data give no registered trial or design detail.

**To proceed, the following is needed:**
- Review of the SAHPRA Professional Information for both products (indications, warnings and contraindications), which is currently missing and blocks safety screening
- Confirmation of whether vulvovaginal candidiasis is already on the approved label of the registered vaginal product (Gyno-Pevaryl Depot)
- Mechanism of action data from DrugBank to support the mechanistic analysis
- Local data on azole resistance, particularly non-albicans *Candida*
- Review of the interaction burden if systemic absorption is possible
- For ectothrix, endothrix, tinea profunda and Majocchi granuloma: clinical evidence that topical econazole reaches follicular and deep infection, or a comparison against standard systemic therapy
- Do not pursue postmenopausal atrophic vaginitis or acne (other than confirmed *Malassezia* folliculitis), given the absence of a biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

