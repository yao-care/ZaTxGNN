---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Atazanavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor marketed in South Africa for HIV-1 infection. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary lentiviral disease. This prediction has **no clinical trials and no publications** behind it, so it rests on model score and general pharmacology only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the SAHPRA licence records supplied contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, atazanavir blocks HIV-1 protease, the enzyme that cleaves the Gag-Pol polyprotein during viral maturation. Its efficacy in HIV-1 infection is established.

Feline immunodeficiency virus (FIV) is a related lentivirus, so a homology-based link is plausible. However, atazanavir activity against FIV protease is not established in the supplied data. The prediction is best read as a knowledge-graph signal, not a validated repurposing lead. It is also a veterinary condition, not a human one.

The same drug has a second, equally scored prediction, simian immunodeficiency virus infection. Its only supporting paper is a 2010 study of HAART in SIV-infected macaques (PMID 20497048). The role of atazanavir in that regimen is unconfirmed. This is a research-model extrapolation, not a clinical indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication. No SANCTR or PACTR entries were supplied either.

## Literature Evidence

Currently no related literature available for this predicted indication.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 45/20.2.8/0925 | Zatonav | Film-coated tablet (Fct) |
| Reg. No. 50/20.2.8/0242 | Emcovir | Tablet |

Both registrations are for human use. No veterinary registration was identified in the supplied data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature. The target is a feline disease, and atazanavir is registered in South Africa only for human use. Other high-scoring predictions for this drug (a neurodevelopmental disorder and an obsolete hyperlipidaemia term) show no mechanistic link and look like graph artefacts.

Two other predictions in the pack are more informative:
- **AIDS related complex** is an obsolete term for symptomatic HIV disease. It maps to atazanavir's existing approved use, not new repurposing. The Phase 3 trial NCT00035932 (n=571) supports it.
- **Congenital HIV** is supported only by observational perinatal cohorts and Phase 2-4 trials in general HIV-1 populations. Neonatal safety must be checked against current labelling.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap). Download and parse the PI PDF from the SAHPRA website.
- Mechanism of action data from DrugBank.
- For the FIV or SIV directions, preclinical evidence of atazanavir activity against FIV or SIV protease, and a veterinary regulatory pathway if pursued.
- For congenital HIV, a review of neonatal safety (including hyperbilirubinaemia) against current labelling.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

