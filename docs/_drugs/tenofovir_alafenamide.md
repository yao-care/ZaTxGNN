---
layout: default
title: Tenofovir Alafenamide
parent: Model Prediction Only (L5)
nav_order: 440
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Tenofovir Alafenamide: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
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

# Tenofovir Alafenamide: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir alafenamide is an antiviral drug originally used to treat HIV infection and AIDS (and, in South Africa, marketed in single-agent products such as Vemlidy, which is used for chronic hepatitis B).
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome** (a veterinary condition), but **no clinical trials and no publications** support this specific prediction.
The closely related prediction, simian immunodeficiency virus infection, is supported by **8 preclinical publications** in macaques and mice, but it is not a new human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (no approved indication text is available for the SAHPRA registrations) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tenofovir alafenamide is a nucleotide reverse transcriptase inhibitor (a prodrug of tenofovir), and its efficacy in HIV infection has been established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV and encodes its own reverse transcriptase, so activity against FIV is mechanistically plausible. The very high TxGNN score most likely reflects the drug's network proximity to HIV-related indications rather than direct evidence in cats.

This is a veterinary indication, so its relevance to human-medicine repurposing in South Africa is limited.

**Other predictions in the data compiled for this report:**
- **Simian immunodeficiency virus (SIV) infection** (score 99.89%, evidence level L3): Macaque studies report that oral, implant-based and topical regimens containing tenofovir alafenamide protected against, or reduced, SIV/SHIV infection. This is valuable as a validated animal model for HIV prevention and treatment, but it does not represent a new human indication, as the drug is already used for HIV.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.87%, evidence level L5): No mechanistic link was identified. The high score is likely a network-based artefact, and no trials or publications support it.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (or for the other two predictions).

## Literature Evidence

No literature is available for the top predicted indication (feline AIDS). The table below lists the preclinical publications for the related SIV/SHIV prediction, for context only. All are non-human primate or mouse studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical (macaque) | J Infect Dis | Oral emtricitabine plus TAF protected macaques from repeated rectal SHIV exposure, supporting TAF for PrEP |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical (macaque) | J Infect Dis | Compared oral TAF/emtricitabine with TAF alone against vaginal SHIV infection |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | Preclinical (macaque) | J Antimicrob Chemother | Biodegradable TAF-releasing implant assessed for safety and vaginal protection |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical (macaque) | J Infect Dis | TAF/elvitegravir vaginal inserts gave extended post-exposure protection against SHIV |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (macaque) | Nat Commun | Early treatment with oral emtricitabine/TAF plus long-acting cabotegravir/rilpivirine studied for SHIV remission |
| [41342257](https://pubmed.ncbi.nlm.nih.gov/41342257/) | 2026 | Preclinical (macaque) | J Infect Dis | Rectal TAF/elvitegravir inserts gave partial post-exposure protection against SHIV |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical (humanized mouse) | Front Immunol | Dual-purpose mouse model for testing antivirals against both SIV and HIV |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | Methods (macaque) | PLoS One | Protocol for training macaques to take daily oral antiretrovirals |

## South Africa Market Information

Four single-agent registrations are valid and none are cancelled. Approved indication text is not available for these registrations. Essential Medicines List (EML) status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/20.2.8/0273 | Vemlidy | Film-coated tablet (Fct) | Not available |
| 55/20.2.8/0080.079 | Tafbin | Film-coated tablet (Fct) | Not available |
| 55/20.2.8/0455 | Altaeda | Film-coated tablet (Fct) | Not available |
| 56/20.2.8/0020 | Tavirant | Film-coated tablet (Fct) | Not available |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The only interaction-related entry in the data compiled for this report is a pharmacological target record (the bitter taste receptor TAS2R39). It is not a clinically relevant drug-drug interaction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The feline AIDS prediction rests on model scoring alone (L5), with no trials or publications, and it is a veterinary indication with limited relevance to human healthcare in South Africa. The SIV/SHIV macaque data are consistent with the drug's known anti-HIV activity but add no new human indication. The neurodevelopmental disorder prediction has no plausible mechanism.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Safety information (warnings and contraindications) from the SAHPRA-approved Professional Information, which is currently missing and is a blocking gap for safety screening
- Approved indication text for the four SAHPRA registrations
- For any veterinary interest, direct FIV studies in cats and engagement with veterinary regulators, which are outside the scope of SAHPRA human-medicine review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

