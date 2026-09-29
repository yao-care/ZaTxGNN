---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 197
evidence_level: L5
indication_count: 3
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine is an antiretroviral drug (an HIV-1 non-nucleoside reverse transcriptase inhibitor), and it is registered in South Africa as part of the product Delstrigo. The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and only **1 loosely related publication** supporting this. The prediction is best regarded as a model artefact with little translational value.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (based on the drug class and the registered product; the registration data has no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Doravirine is an NNRTI. Detailed mechanism of action data is not available in the Evidence Pack, so the reasoning below rests on general knowledge of the drug class. The high score most likely reflects the knowledge graph placing HIV-1 and SIV close together, since both are lentiviruses.

That proximity does not translate into drug activity. NNRTIs bind a hydrophobic pocket in HIV-1 reverse transcriptase that is specific to HIV-1. SIV, like HIV-2, is generally not susceptible to this class. SIV infection is also a non-human primate model rather than a human indication, so a positive result would offer little clinical value.

The other top predictions are weaker still:
- **Feline acquired immunodeficiency syndrome (score 99.93%)**: a veterinary condition. Feline immunodeficiency virus reverse transcriptase differs in the NNRTI binding pocket, and there are no trials or literature.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter (score 99.91%)**: there is no plausible mechanistic link. The score is probably a knowledge-graph artefact from sparse node connectivity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Discusses islatravir, a different reverse transcriptase translocation inhibitor, for HIV-1 treatment and prevention. It does not address doravirine or SIV, so its relevance is limited. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/20.2.8/0233 | Delstrigo | Fct (film-coated tablet) | Not provided in the registration data |

Essential Medicines List (EML) inclusion status is not available in the Evidence Pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials and no relevant literature. The mechanism is implausible, because NNRTIs are generally inactive against SIV and the indication is not a human disease. Doravirine's established value remains in HIV-1 treatment.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- An independent mechanistic hypothesis and preclinical evidence of doravirine activity against SIV, if this direction is to be pursued
- A human-relevant indication, since SIV infection and feline immunodeficiency are not human diseases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

