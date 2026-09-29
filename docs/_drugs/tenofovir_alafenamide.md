---
layout: default
title: Tenofovir Alafenamide
parent: Model Prediction Only (L5)
nav_order: 436
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tenofovir Alafenamide: From Antiviral Therapy to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir alafenamide (TAF) is an antiviral nucleotide reverse transcriptase inhibitor that is currently marketed in South Africa under 4 SAHPRA registrations.
The TxGNN model ranks **feline acquired immunodeficiency syndrome** as its top prediction, but no clinical trials or publications support it.
The best-supported related signal is **simian immunodeficiency virus (SIV) infection**, with **8 preclinical publications** and **1 indirectly related trial**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data provided |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (veterinary) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (SIV infection, rank 2: L4) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. TAF is a nucleotide reverse transcriptase inhibitor. After it is converted inside cells to tenofovir diphosphate, it blocks the reverse transcriptase enzyme that lentiviruses need to replicate.

Feline immunodeficiency virus (FIV) is a lentivirus that replicates through reverse transcriptase, so an antiviral rationale is plausible. However, this rests only on the model score and class-level reasoning. FIV is also a veterinary pathogen, which limits relevance to human drug repurposing.

The rank 2 prediction, **SIV infection**, has more support. SIV and SHIV infection in macaques are standard preclinical models of HIV. Several macaque studies test TAF-based regimens directly, including oral emtricitabine/TAF, a vaginal implant and topical GS-7340. This mainly supports the HIV-1 rationale, which is likely already an approved use, so it is probably not a new repurposing signal. The registration data provided contain no original indication, so the HIV-1 label status should be confirmed first.

The rank 3 prediction, a rare genetic neurodevelopmental disorder (ataxic gait, absent speech, decreased cortical white matter), has no identifiable mechanistic link to TAF. Its score (99.87%) is nearly identical to the others, which suggests a knowledge-graph artifact rather than a specific signal.

---

## Clinical Trial Evidence

No clinical trials are currently registered for the rank 1 prediction (feline AIDS). For rank 2 (SIV infection), one trial was retrieved:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab plus antiretroviral therapy to achieve virological remission in HIV-infected people. The population is HIV, not SIV, and TAF is not the investigational agent, so this is only indirect support (relevance grade C). |

No SANCTR or PACTR records were identified in the data provided.

---

## Literature Evidence

No literature is available for the rank 1 prediction. The table below covers rank 2 (SIV infection). All are animal or model studies, and none is an RCT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal study (macaque) | Nature Communications | Early treatment with oral emtricitabine/TAF and long-acting cabotegravir/rilpivirine in RT-SHIV-infected macaques, aimed at viral remission |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Animal study (macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts for post-exposure protection against SHIV. Earlier work showed 93% and 100% protection when given 4 hours before or after exposure. |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Model development (humanized mouse) | Front Immunol | Dual-purpose mouse model for testing antiviral strategies against both SIV and HIV |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Animal study (macaque) | J Antimicrob Chemother | Safety and efficacy of a biodegradable TAF implant for vaginal PrEP |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal study (macaque) | J Infect Dis | Oral TAF/emtricitabine versus TAF alone against repeated vaginal SHIV exposure |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Methods (rhesus macaque) | PLoS One | Protocol for daily oral antiretroviral dosing in macaques with high compliance |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal study (macaque) | J Infect Dis | Oral emtricitabine/TAF chemoprophylaxis protected macaques from rectal SHIV infection |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | Animal study (macaque) | J Infect Dis | Breakthrough acute SHIV infection during oral PrEP showed reduced inflammation and CD4 loss |

A further study is [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) (2006, J Acquir Immune Defic Syndr), which evaluated oral tenofovir disoproxil fumarate and topical tenofovir GS-7340 in infant macaques against repeated oral SIV challenge.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 52/20.2.8/0273 | Vemlidy | Fct |
| Reg. No. 55/20.2.8/0080.079 | Tafbin | Fct |
| Reg. No. 55/20.2.8/0455 | Altaeda | Fct |
| Reg. No. 56/20.2.8/0020 | Tavirant | Fct |

The approved indication text and Essential Medicines List status are not available in the data provided.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline AIDS) is a veterinary indication with no trials or literature behind it. The SIV signal is preclinical only, and it mostly restates the HIV-1 rationale rather than a new human use. The rank 3 prediction has no plausible mechanistic link.

**To proceed, the following is needed:**
- SAHPRA package insert data (approved indications, warnings, contraindications), which is required before any safety screening
- Confirmation of the current HIV-1 and hepatitis B label status to judge whether the SIV signal is genuinely new
- Detailed mechanism of action data (for example, from the DrugBank API)
- A clear decision on whether veterinary indications are in scope for human-focused repurposing

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

