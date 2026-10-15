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

# Abacavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Abacavir is an antiretroviral drug originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
but there are currently **0 clinical trials** and only **1 publication** (an in vitro study) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the SAHPRA registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known information, abacavir is a nucleoside reverse transcriptase inhibitor (NRTI). Its efficacy in HIV-1 infection is established, and mechanistically it may be applicable to SIV.

SIV is a closely related lentivirus with a homologous reverse transcriptase, so mechanistic plausibility is high. The one available study is an in vitro susceptibility study testing HIV-2, SIV and SHIV against various anti-HIV-1 compounds. It supports indirect antiviral activity but does not show clinical efficacy.

SIV infection is a primate model disease, not a human indication. Its value for human drug repurposing is therefore limited. Two other predictions were also generated, and both are weaker:
- **Feline acquired immunodeficiency syndrome (score 99.79%):** essentially the approved HIV/AIDS indication in another species. Its only support is a 2002 in vitro study of a zidovudine, lamivudine and abacavir combination, which does not isolate abacavir's contribution.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (score 99.78%):** a model prediction only, with no trials or literature and no identifiable mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antiviral Therapy | Evaluated 16 approved drugs and one experimental drug (AMD3100) against HIV-2, SIV and SHIV strains, to guide treatment and post-exposure prophylaxis. |

## South Africa Market Information

All 11 registrations are valid single-ingredient registrations. Approved indication text and Essential Medicines List (EML) status are not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54/20.2.8/0219 | Vexabax | Film-coated tablet | Not available |
| 49/20.2.8/0462 | Dumiva Dispersible Tablets | Effervescent tablet | Not available |
| 44/20.2.8/0293 | Auro Abacavir Lamivudine 600/300Mg Tablets | Film-coated tablet | Not available |
| 54/20.2.8/0206 | Cagol | Tablet | Not available |
| 55/20.2.8/0338 | Vuterar | Tablet | Not available |

Six further valid registrations are not shown: Damicava Paed, Sonke-abaclamizid, Heteruam 600mg/300mg, Kivexa 600mg/300mg, Quadrimune and Trizivar.

## Cytotoxicity

Abacavir is an antiviral, not an antineoplastic drug, so this section does not apply.

## Safety Considerations

- **Drug-disease contraindication signals (knowledge graph, not label text):** liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, pancreatitis, gallbladder disease, lactic acidosis, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), hypertriglyceridaemia, obesity disorders, and myopathy or myositis-type conditions (including dermatomyositis and familial periodic paralysis). These signals are not label text and must be verified against the PI.
- **Drug Interactions:** 93 potential interactions were identified in total. Naltrexone and orlistat are rated Moderate. Others, such as metformin, morphine, prednisone, omeprazole, pantoprazole, lansoprazole, vancomycin and amphotericin B, have an unknown severity level.
- **Known class concern:** abacavir carries a recognised risk of HLA-B*57:01-associated hypersensitivity. This comes from general drug knowledge, not from the data compiled for this report.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) are not available in the compiled data. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence for the top prediction is a single in vitro study in a non-human disease model, with no clinical trials. The mechanistic plausibility is reasonable, but SIV infection is not a human indication, so the repurposing value is limited. The other two predictions are a veterinary restatement of the approved indication and an unsupported model prediction.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the SAHPRA registrations
- A clear human-relevant research question, since SIV is a primate model disease
- Further target-level analysis before pursuing the neurodevelopmental disorder prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

