---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor used in antiretroviral therapy for HIV-1 infection. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, with **0 clinical trials** and **4 publications**, all in non-human primates. This is most likely a preclinical research use of an existing antiretroviral, not a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (drug-class knowledge; the SAHPRA indication text was not supplied) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical/animal studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Darunavir inhibits the HIV-1 protease enzyme, which the virus needs to mature into infectious particles. Detailed mechanism of action data is not available in the input. Based on known information, darunavir is a protease inhibitor whose efficacy in HIV-1 infection is established. Mechanistically it may be applicable to SIV, a close lentiviral relative of HIV.

SIV-infected macaques are a standard model for testing antiretroviral regimens and studying the persistent viral reservoir. The high score most likely reflects this close link to darunavir's existing anti-retroviral use rather than a genuinely new therapeutic direction. SIV infection is not a human disease, so this prediction has no direct patient indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for SIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal study (macaque) | AIDS Res Hum Retroviruses | Compared coformulated injectable combination ART regimens in SIVmac239-infected rhesus macaques, including a triple regimen with emtricitabine and tenofovir disoproxil fumarate |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal study (macaque) | PLoS One | Intensive cART plus 3 weeks of the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques, to study the viral reservoir |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study (macaque) | PLoS Pathog | Highly intensified multidrug ART in SIVmac251-infected macaques, evaluating viral suppression and impact on the reservoir |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal study (macaque) | AIDS | Auranofin added to ART in the monkey AIDS model, examining its effect on the viral reservoir |

The abstract excerpts provided do not show the role of darunavir in each regimen. The full texts should be checked before these studies are cited as darunavir-specific evidence.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/20.2.8/0838 | Ronivid 400/50 Mg | Film-coated tablet (Fct) | Not stated in the supplied data |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only support is four macaque studies, with no human or registered clinical trials for this indication.
- SIV infection is a veterinary/research model condition, so the prediction adds no new treatment option for South African patients.
- The other predictions in the pack are also weak. Feline immunodeficiency and a rare neurodevelopmental disorder have no relevant evidence. The obsolete familial combined hyperlipidaemia term is a concern because HIV protease inhibitors are associated with dyslipidaemia.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is required before any safety screening
- Mechanism of action data from DrugBank
- Full-text review of the four macaque studies to confirm whether darunavir was part of the regimens
- A decision on whether an animal-model prediction is in scope for a human repurposing pipeline at all; if not, deprioritise it
- Remapping of the obsolete hyperlipidaemia term to a current ontology term before any further review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

