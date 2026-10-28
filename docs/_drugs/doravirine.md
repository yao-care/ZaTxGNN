---
layout: default
title: Doravirine
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 3
monitor_inn: "DORAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-29
description: "Doravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease and AIDS"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Doravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Doravirine is an antiretroviral drug (a non-nucleoside reverse transcriptase inhibitor) that has a relation recorded in the knowledge graph for HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 clinical trials** and **0 publications** directly studying this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relations recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Number of approvals | 1 SAHPRA registration (a single-ingredient record) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge of the drug class, doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that acts against HIV-1.

Feline immunodeficiency virus (FIV) is a lentivirus that also uses a reverse transcriptase, so a theoretical link exists. However, NNRTIs are generally poorly active against reverse transcriptases of non-HIV-1 lentiviruses, because the NNRTI binding pocket differs structurally. The very high score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Confidence in the prediction is therefore low.

Two other predictions were also generated, with similar scores:
- **Simian immunodeficiency virus infection** (score 0.9993): biologically plausible because SIV is a standard animal model for HIV. However, SIV strains resembling HIV-2 are intrinsically resistant to many NNRTIs. The only retrieved paper concerns islatravir, a different drug, in human HIV-1, so it gives no direct support.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 0.9991): no plausible mechanistic link was found, and this is likely a false positive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 53/20.2.8/0233 | Delstrigo | Film-coated tablet (Fct) | Not stated in the data compiled for this report |

Delstrigo is a registered product, and the data compiled for this report do not describe how doravirine is licensed or marketed as a single ingredient. Essential Medicines List inclusion status was not available.

## Safety Considerations

**Drug Interactions:** The interaction search returned 59 entries; the 20 listed here include the following.
- **Major:** dexamethasone, lumacaftor
- **Moderate:** glycerol phenylbutyrate, metreleptin, troglitazone, deferasirox, praziquantel, griseofulvin
- **Minor:** aprepitant, cimetidine, clarithromycin, clotrimazole, miconazole, cobicistat, ticagrelor, ivacaftor, zafirlukast, chloramphenicol, erythromycin, fluconazole

For warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. No clinical trials or publications directly study doravirine in this disease, so the evidence level is L5. The known weak activity of NNRTIs against non-HIV-1 lentiviral reverse transcriptases further lowers confidence. Feline AIDS is a veterinary condition, which also raises questions about relevance to South African human healthcare.

**To proceed, the following is needed:**
- In vitro activity data of doravirine against FIV (and SIV) reverse transcriptase
- Mechanism of action data for doravirine
- Package insert warnings and contraindications from SAHPRA (a blocking gap for safety screening)
- A decision on whether a veterinary or animal-model indication is within the scope of this evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

