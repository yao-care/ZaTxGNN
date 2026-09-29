---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 401
evidence_level: L5
indication_count: 3
---

# Ritonavir
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

# Ritonavir: From HIV Antiretroviral Therapy to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor and CYP3A4 booster used in antiretroviral combinations; the supplied record does not list its approved indication, so this is based on general drug knowledge. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**. Support is thin: **0 clinical trials** and **11 publications**, all preclinical, in vitro or commentary. SIV is a non-human infection, so this is a model-system finding, not a new human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records supplied (ritonavir is generally known as an HIV-1 protease inhibitor and pharmacokinetic booster) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical and in vitro studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the input. Ritonavir is generally known to inhibit the HIV-1 protease enzyme, which the virus needs to mature into infectious particles. It also inhibits CYP3A4, which is why it is used at low doses to "boost" other protease inhibitors.

SIV is a close relative of HIV, and its protease is similar. In vitro work supports this link. One study found SIVmac239 was inhibited by ritonavir at about 13 nM, compared with about 25 nM for HIV-1. Macaque studies also used combination antiretroviral regimens, some including lopinavir/ritonavir.

The predicted disease is a monkey infection used as a model for HIV. The clinically meaningful counterpart, HIV infection, is not part of this prediction. The high score (0.999) is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for SIV infection.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by ritonavir (EC50 about 13 nM), similar to HIV-1 (about 25 nM). |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | 16 approved anti-HIV drugs tested against HIV-2, SIV and SHIV strains, informing treatment and post-exposure prophylaxis. |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | J Virol | Rapid viral decay in SIV-infected macaques on quadruple antiretroviral therapy. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (macaque) | J Virol Methods | Oral AZT, 3TC and lopinavir/ritonavir given to SHIV-infected macaques for 28 days; effect on the CD8 subset studied. |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (macaque) | PLoS Pathog | Highly intensified multidrug ART in SIVmac251-infected macaques; viral suppression and reservoir effects studied. Ritonavir's specific role is not confirmed from the abstract. |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (macaque) | PLoS One | Suppressive cART plus the HDAC inhibitor SAHA in SIV-infected rhesus macaques, as a viral reservoir model. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical | Microbes Infect | Built a SHIV carrying the HIV-1 protease gene as a macaque tool for testing protease inhibitors. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical/Review | mBio | Lentiviral infection persists in brain despite effective ART in several models. |

## South Africa Market Information

Nine SAHPRA registrations are recorded; the five main ones are listed. Approved indication text was not included in the records supplied.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 51/20.2.8/0687.686 | Hetrovir 100 | Tablet |
| Reg. No. 51/20.2.8/0154 | Norvir Oral Powder | Sachet |
| Reg. No. 56/20.2.8/0838 | Ronivid 400/50 mg | Fct |
| Reg. No. 45/20.2.8/0925 | Zatonav | Fct |
| Reg. No. 43/20.2.8/0356 | Aluvia 100/25 | Tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for SIV infection is in vitro and macaque work, with no human trials. SIV is a research model rather than a treatable human disease. The other two predictions are weaker still:
- **Feline acquired immunodeficiency syndrome:** likely a knowledge-graph artifact. The only linked trial is a human HIV-1 study of boosted darunavir, and there is no feline evidence.
- **Rare neurodevelopmental disorder (ataxic gait, absent speech):** no plausible mechanistic link and no trials or literature.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Confirmation of the approved indication text for the registered products
- Reframing the question toward HIV infection in humans, where ritonavir's role is already established, rather than SIV or FIV
- Expert mechanistic review before any follow-up on the feline and neurodevelopmental predictions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

