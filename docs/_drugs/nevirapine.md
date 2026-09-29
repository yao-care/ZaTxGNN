---
layout: default
title: Nevirapine
parent: Moderate Evidence (L3-L4)
nav_order: 337
evidence_level: L4
indication_count: 3
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Nevirapine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Nevirapine is an HIV-1 reverse transcriptase inhibitor that is marketed in South Africa. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, with a very high score. However, there are **0 clinical trials** and only preclinical literature, so this looks more like a research-model use than a true repurposing indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the SAHPRA registration entries in the data have no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Nevirapine is known to be a non-nucleoside reverse transcriptase inhibitor (NNRTI) that targets HIV-1 reverse transcriptase (RT). Its efficacy in HIV-1 is established, and SIV is a related lentivirus, so a graph model could plausibly link the two.

The link is weaker than the score suggests. Native SIV and HIV-2 RT are generally reported to be intrinsically insensitive to NNRTIs. The high score probably reflects HIV-related network proximity rather than true anti-SIV activity.

The literature shows activity mainly against RT-SHIV chimeras. These are SIV constructs carrying HIV-1 RT, and they are used as macaque models to study drug resistance. This supports using nevirapine in preclinical models, not as a treatment for SIV infection. This assessment is based on titles and truncated abstracts only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | Preclinical in vitro | Biochem Biophys Res Commun | A hybrid SIV carrying the HIV-1 RT gene (RT-SHIV) was markedly sensitive to nucleoside and non-nucleoside RT inhibitors, unlike wild-type SIV |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | Preclinical in vitro | J Virol | NNRTIs do not effectively inhibit SIV RT; an SIV-HIV chimera expressing HIV-1 RT was characterised to study NNRTI resistance in pigtail macaques |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Preclinical animal model | AIDS Res Hum Retroviruses | RT-SHIV-infected cynomolgus monkeys were used as an in vivo model of RT-inhibitor resistance development |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Preclinical in vitro | Antivir Ther | Compared 16 approved anti-HIV drugs against HIV-2, SIV and SHIV, to guide treatment and postexposure prophylaxis |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Preclinical animal model | Virology | RT-SHIV (with HIV-1 RT) transmitted efficiently by the vaginal route in rhesus macaques, supporting its use as a model |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | Not classified (in vitro) | Virology | NRTIs and NNRTIs were tested for inactivating HIV-1 and SIV virions through endogenous reverse transcription |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | Non-occupational HIV postexposure prophylaxis; indirect support comes from animal studies with antiretrovirals against SIV |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | Preclinical in vitro (other compound) | Chem Biol Drug Des | A different compound (3G11) blocked HIV-1 but not SIVmac; not evidence for nevirapine |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | Preclinical in vitro (other compound) | Antimicrob Agents Chemother | Integrase inhibitor combined with nevirapine was subsynergistic; not evidence of nevirapine activity against SIV |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/20.2.8/0659 | Sonke-Laminevstav 30 | Tablet | Not stated in the registration data |
| Reg. No. 45/20.2.8/0388 | Mivirdo | Tablet | Not stated in the registration data |
| Reg. No. 44/20.2.8/0212 | Tri-Nestlam 150/30/200 | Tablet | Not stated in the registration data |
| Reg. No. 46/20.2.8/0943 | Nevasta | Tablet | Not stated in the registration data |

All four registrations are oral tablets. Essential Medicines List (EML) status is not included in the data provided and should be checked against the current EML.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to preclinical work (L4) with no clinical trials. The literature mainly supports nevirapine's use in macaque RT-SHIV models, and native SIV is generally insensitive to NNRTIs. The high TxGNN score therefore likely reflects network proximity rather than a real therapeutic opportunity. SIV infection is also not a human disease, so it is not a clinically actionable indication for South African patients.

The other two predictions for this drug are also on Hold:
- **Feline acquired immunodeficiency syndrome (L4):** one 2023 biochemical and structural comparison of NNRTIs against feline and human immunodeficiency viruses. This is a veterinary condition with no trials.
- **A rare neurodevelopmental disorder (L5):** no trials, no literature and no identifiable mechanistic rationale. This is likely a graph-prediction artifact.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications, currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Full-text review of the RT-SHIV literature to confirm the findings, since this assessment is based on titles and truncated abstracts
- Approved indication text for the four SAHPRA registrations
- An independent mechanistic review of the third prediction before any further work

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

