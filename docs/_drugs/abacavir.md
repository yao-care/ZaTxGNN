---
layout: default
title: Abacavir
parent: Moderate Evidence (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor already marketed for HIV-1 infection. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but the support is thin: **0 clinical trials** and **1 publication**, an in vitro susceptibility study. SIV infection is a non-human primate disease used as a model for HIV, not a human clinical indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the SAHPRA registration data supplied contains no approved-indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Abacavir is a nucleoside reverse transcriptase inhibitor. Its active form, carbovir triphosphate, terminates the viral DNA chain during reverse transcription. SIV is a lentivirus whose reverse transcriptase is homologous to that of HIV, so activity against SIV is biologically plausible.

The prediction is best read as a knowledge-graph echo of abacavir's existing HIV-1 relationship, not as a new therapeutic opportunity. SIV is a primate infection used to model HIV, so the high score probably reflects the close ontological link between the two diseases. The only support is one in vitro study. Abacavir is already a marketed HIV-1 drug, so this is not true repurposing.

The model also ranked two other candidates for abacavir:
- **Feline acquired immunodeficiency syndrome.** Its four listed trials are human HIV-1 studies of dolutegravir in which abacavir/lamivudine is only the backbone. They show nothing about feline disease.
- **A rare neurodevelopmental disorder.** It has no trials, no literature and no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Tested 16 approved antiretrovirals and one experimental drug (AMD3100) against HIV-2, SIV (mac251, B670) and SHIV strains, to guide treatment and post-exposure prophylaxis. The abstract available to us is truncated, so the abacavir-specific result is not confirmed. |

## South Africa Market Information

Abacavir has 11 SAHPRA registrations. Five are shown below. The approved-indication text was not supplied for these products, and their Essential Medicines List (EML) status is not confirmed here.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 54/20.2.8/0219 | Vexabax | Film-coated tablet (listed as "Fct") |
| Reg. No. 49/20.2.8/0462 | Dumiva Dispersible Tablets | Effervescent tablet |
| Reg. No. 44/20.2.8/0293 | Auro Abacavir Lamivudine 600/300Mg Tablets | Film-coated tablet (listed as "Fct") |
| Reg. No. 54/20.2.8/0206 | Cagol | Tablet |
| Reg. No. 55/20.2.8/0338 | Vuterar | Tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for the SIV prediction is a single in vitro study. SIV infection is a primate model disease with no human clinical use, so there is nothing to translate into practice. Abacavir's real value for South African patients lies in its existing HIV-1 indication, which needs no repurposing.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the SAHPRA-approved PI, which is required before any safety screening
- Mechanism of action data from DrugBank, to complete the mechanistic analysis
- Confirmation of abacavir's approved indication text in SAHPRA registrations, since the original-indication field is empty
- A decision on whether an animal-model indication is relevant at all, or whether the review should turn to human-relevant candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

