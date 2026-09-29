---
layout: default
title: Zidovudine
parent: Moderate Evidence (L3-L4)
nav_order: 472
evidence_level: L4
indication_count: 6
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Zidovudine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Zidovudine is a nucleoside reverse transcriptase inhibitor (NRTI) used in antiretroviral therapy, and its South African registrations are mainly HIV products. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but this is an animal-model disease with no human patients. The supporting evidence is **0 clinical trials** and **20 publications**, all preclinical (mostly macaque studies), so this prediction is not a human repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection (inferred from the antiretroviral products registered; the registration records contain no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Zidovudine is a well-known NRTI. Inside cells it is converted to its triphosphate form, which blocks reverse transcriptase and terminates the growing viral DNA chain.

SIV is a lentivirus closely related to HIV, and its reverse transcriptase is similar to that of HIV-1. A drug that blocks HIV replication is therefore expected to block SIV too, which explains the high model score. The macaque literature confirms this: zidovudine reduced viral load, prolonged survival and, in some newborn animals, prevented infection.

The limits matter. SIV infects non-human primates only, so this indication has no human patient population. The literature validates the mechanism and serves as a preclinical model for HIV drug development. It does not support a human repurposing claim.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The pack contains 20 publications, and the 10 most relevant are listed below. All are animal or in vitro studies. No RCTs or human studies were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | Animal study | Antimicrob Agents Chemother | Oral AZT prevented SIV infection in infant rhesus macaques |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal study | AIDS | Post-exposure prophylaxis with zidovudine, lamivudine and indinavir against vaginal SIV transmission in macaques |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | Animal study | AIDS Res Hum Retroviruses | Effect of AZT on viral load during acute SIV infection in cynomolgus macaques |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Animal study | Antimicrob Agents Chemother | Immediate AZT protected SIV-infected newborn macaques against rapid onset of AIDS |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Animal study | J Infect Dis | AZT prolonged survival and lowered CNS viral load in perinatally infected macaques, but did not prevent infection |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | Animal study | J Infect Dis | Effects of starting zidovudine 1 to 72 hours after SIV inoculation in rhesus monkeys |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | Animal study | J Acquir Immune Defic Syndr | Antiviral effects of 3'-fluorothymidine versus zidovudine in SIV-infected cynomolgus monkeys; neither prevented infection |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | Virology / animal | Antimicrob Agents Chemother | A zidovudine-resistant SIV mutant (Q151M) caused AIDS in newborn macaques |
| [8452370](https://pubmed.ncbi.nlm.nih.gov/8452370/) | 1993 | In vitro | Antimicrob Agents Chemother | AZT versus neutralising antibodies against SIV infection in macaque macrophages |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Rapid viral decay in SIV-infected macaques on quadruple antiretroviral therapy |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/20.2.8/0106 | Adco lamivudine & zidovudine 150mg/300mg | Tablet | Not stated in records |
| Reg. No. 32/20.2.8/0200 | Retrovir/3tc HIV starter pack (AZT) 100m | Kit | Not stated in records |
| Reg. No. 43/20.2.8/0363 | Hevaz | Tablet | Not stated in records |
| Reg. No. A40/20.2.8/0244 | Cipla-duovir | Tablet | Not stated in records |
| Reg. No. 36/7.5/0372 | Simayla Simvastatin 40 | Tablet | Not stated in records |

Nine registrations exist in total, and five are shown. Simayla Simvastatin 40 is a statin product, so its link to zidovudine looks like a data-matching error. It should be checked against the SAHPRA register.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection occurs only in non-human primates, so the 20 macaque publications support the mechanism but not a human indication. There are no clinical trials, and the evidence stays at L4. The Evidence Pack lists the missing SAHPRA package insert safety data as a blocking gap.

Two other predictions in the pack have human relevance:
- **Congenital HIV** (L3, Proceed with Guardrails): this is an established use for preventing mother-to-child transmission and neonatal prophylaxis, not a new repurposing.
- **AIDS-related complex** (L1, Proceed with Guardrails): this is a historical term for symptomatic HIV disease, and zidovudine is long-established therapy for it. Both are better handled as separate on-label reviews.

**To proceed, the following is needed:**
- Download and parse the SAHPRA package insert to obtain warnings and contraindications (blocking gap).
- Mechanism of action data from DrugBank.
- Confirmation of the original indication, since the registration records contain no indication text.
- Correction or confirmation of the Simayla Simvastatin 40 registration link.
- A decision to re-scope the review to a human-relevant indication, such as congenital HIV or AIDS-related complex. If so, guardrails would include monitoring for anaemia and neutropenia, weight- and age-based neonatal dosing, and regimen selection per current guidelines.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

