---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 464
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the format specified in the prompt to build this report directly (no codebase skill applies to freeform report authoring against a supplied template).

A few things surfaced in this Evidence Pack that shape the report: `drug.original_indications` is empty and `original_moa` is `[Data Gap]`, so I've used zidovudine's well-established original indication (HIV/AIDS) for the title/table while flagging the gap. Also, rank-1 and rank-2 predictions ("simian immunodeficiency virus infection" / "feline acquired immunodeficiency syndrome") are lentivirus **animal models** of HIV, not genuinely new human indications — I've called this out explicitly rather than presenting it as a novel repurposing signal.

---

# Zidovudine: From HIV/AIDS to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Zidovudine (AZT) is a nucleoside reverse transcriptase inhibitor originally developed and approved for treating human immunodeficiency virus (HIV) infection.
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection** — a lentivirus disease of non-human primates used as an animal model for HIV —
> supported by **0 clinical trials** and **20 preclinical/animal publications**, with a tied top score also predicting the feline (FIV) analogue.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV/AIDS (Human Immunodeficiency Virus infection) — established clinical use; not present in the evidence pack's structured fields |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.96% (rank 391) |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on established clinical knowledge, zidovudine is a thymidine-analogue nucleoside reverse transcriptase inhibitor (NRTI) that has been a cornerstone antiretroviral for human HIV-1/HIV-2 infection since the 1980s, including its landmark role in preventing mother-to-child transmission.

SIV and HIV are both primate lentiviruses with closely homologous reverse transcriptase enzymes, which is why SIV-infected macaque and cynomolgus monkey models have long been used as preclinical surrogates for testing anti-HIV drugs (including zidovudine itself, as reflected in the literature below). Mechanistically, the same reverse-transcriptase inhibition that underlies zidovudine's HIV efficacy explains its activity against SIV.

**Important caveat for interpretation:** this is not a novel repurposing signal in the usual sense. SIV infection is a disease of non-human primates, not a human condition — the model is essentially rediscovering that zidovudine, an antiretroviral, is active against a closely related lentivirus. The tied second-ranked prediction (feline acquired immunodeficiency syndrome, an FIV/FeLV model in cats, same score 99.96%) and the lower-ranked predictions of "congenital human immunodeficiency virus" (rank 5) and "AIDS related complex" (rank 6, an older clinical staging term for symptomatic pre-AIDS HIV disease) reinforce this: all five HIV/lentivirus-related predictions reflect zidovudine's **already-known** indication rather than a genuinely new human disease target. Two other predictions in this pack (a rare neurodevelopmental disorder and an obsolete hyperlipidemia term) were separately flagged by the pack itself as unsupported (Evidence Level L5, Hold) and are not carried forward here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | Animal/Preclinical | Antimicrobial Agents and Chemotherapy | Oral AZT prevented SIV infection in infant rhesus macaques given prophylactically before/after low-dose viral inoculation |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Animal/Preclinical | Antimicrobial Agents and Chemotherapy | Immediate zidovudine treatment protected SIV-infected newborn macaques from rapid-onset AIDS |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Animal/Preclinical | The Journal of Infectious Diseases | Zidovudine prolonged survival and lowered CNS viral load in perinatally SIV-infected rhesus macaques |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal/Preclinical | AIDS (London, England) | Postexposure prophylaxis with zidovudine + lamivudine + indinavir prevented vaginal SIV transmission in macaques |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | Animal/Preclinical | AIDS Research and Human Retroviruses | AZT reduced viral load kinetics during acute SIV infection in cynomolgus macaques |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | Animal/Preclinical | Antimicrobial Agents and Chemotherapy | Zidovudine-resistant SIV mutant (Q151M reverse transcriptase mutation) still caused AIDS in newborn macaques, documenting resistance risk |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | Animal/Preclinical | The Journal of Infectious Diseases | Timing of zidovudine initiation after SIV inoculation affected antiviral outcome in rhesus monkeys |
| [8452370](https://pubmed.ncbi.nlm.nih.gov/8452370/) | 1993 | Animal/Preclinical | Antimicrobial Agents and Chemotherapy | AZT compared with neutralizing antibodies for controlling SIV infection in macrophages |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | Animal/Preclinical | Journal of Acquired Immune Deficiency Syndromes | Antiviral effects of AZT (zidovudine) vs. 3'-fluorothymidine in SIV-infected cynomolgus monkeys |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal/Preclinical | Journal of Virology | Persistent bone marrow hematopoiesis defect in SHIV-infected macaques despite effective HAART viral suppression |

---

## South Africa Market Information

Zidovudine currently has no SAHPRA registrations on record in this evidence pack (market status: not marketed; 0 licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A blocking data gap (missing SAHPRA/TFDA-equivalent PI warnings and contraindications) prevents any S1 safety pre-assessment.
- Zidovudine has zero SAHPRA registrations and is not currently marketed in South Africa.
- The top-ranked "predicted new indication" (SIV infection) is a non-human primate disease, not a human condition — it does not represent an actionable new clinical use, only confirmation of zidovudine's known anti-lentiviral mechanism. No clinical trials exist for this specific indication (Evidence Level L4, preclinical only).

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI (remediates DG001, Blocking)
- Confirmed mechanism-of-action data from DrugBank (remediates DG002)
- Re-scoping of the TxGNN prediction set toward a genuine human-relevant candidate indication, since ranks 1, 2, 5, and 6 all resolve to zidovudine's already-approved HIV/AIDS indication rather than a novel target
- If a true repurposing hypothesis is pursued, human clinical trial and observational evidence specific to that new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

