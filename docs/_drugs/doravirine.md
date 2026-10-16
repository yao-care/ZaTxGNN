---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 199
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Doravirine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease"
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

# Doravirine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and **1 publication**, and that publication concerns a different drug (islatravir). The prediction is therefore **model-based only**. SIV infection is an animal infection model, not a human clinical indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the SAHPRA registration does not list an approved indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, doravirine is an NNRTI that is approved for HIV-1, and its efficacy in HIV-1 is established. SIV is a closely related lentivirus, so NNRTI activity could plausibly extend to it.

There are important reasons for caution. SIV reverse transcriptase generally belongs to the HIV-2/SIV lineage, and NNRTIs are typically inactive against HIV-2. The high TxGNN score most likely reflects the network proximity of SIV to HIV in the knowledge graph rather than direct pharmacological evidence. SIV is also a non-human infection, so it has no direct clinical use in South African patients.

**Other predictions (all low confidence):**
- **Feline acquired immunodeficiency syndrome** (score 99.93%): a veterinary indication. NNRTIs generally show poor activity against feline immunodeficiency virus reverse transcriptase. There are no trials or literature.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.91%): a rare genetic disorder with no plausible link to reverse transcriptase inhibition. This is likely a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Discusses islatravir, a novel reverse transcriptase translocation inhibitor, for HIV-1 treatment and prevention. It does not address doravirine or SIV, so it does not support this prediction. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 53/20.2.8/0233 | Delstrigo | Film-coated tablet (Fct) | Not stated in the compiled data |

Essential Medicines List (EML) inclusion status is not available in the compiled data.

## Safety Considerations

**Drug Interactions:** The interaction screening returned **59 interactions**. The first 20 records reviewed included:
- **Major:** Dexamethasone, Lumacaftor
- **Moderate:** Glycerol phenylbutyrate, Metreleptin, Troglitazone, Deferasirox, Praziquantel, Griseofulvin
- **Minor:** Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Miconazole, Cobicistat, Ticagrelor, Ivacaftor, Zafirlukast, Chloramphenicol, Erythromycin, Fluconazole

The remaining interactions were not reviewed here. Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials, and the only linked paper concerns a different drug. SIV is an animal infection, and NNRTIs are generally not active against the HIV-2/SIV lineage. The other two predictions are also unsupported, one being a veterinary indication and the other having no plausible mechanism.

**To proceed, the following is needed:**
- Doravirine-specific in vitro or animal data showing activity against SIV reverse transcriptase
- Clarification of whether any human clinical need exists, since SIV is not a human disease
- Detailed mechanism of action data
- The SAHPRA Professional Information (PI) for Delstrigo, covering warnings, contraindications and approved indication
- A full review of the 59 drug interactions (including the Major interactions with dexamethasone and lumacaftor) should any repurposing proceed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

