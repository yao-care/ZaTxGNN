---
layout: default
title: Phenoxymethylpenicillin
parent: Model Prediction Only (L5)
nav_order: 366
evidence_level: L5
indication_count: 10
---

# Phenoxymethylpenicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Phenoxymethylpenicillin: From Penicillin-Sensitive Bacterial Infections to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (penicillin V) is an oral penicillin antibiotic, used for infections caused by penicillin-sensitive bacteria. The registration data supplied did not include an approved-indication text, so this original use is inferred from the drug class. The TxGNN model predicts it may be effective for **epiglottitis**, but **no clinical trials and no publications** were found for this pairing, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Penicillin V is a beta-lactam, and beta-lactams inhibit bacterial cell wall synthesis by binding penicillin-binding proteins. Epiglottitis is a bacterial infection, so there is a plausible link at the class level, which probably explains the high model score.

The link weakens on closer inspection. The main causative organism, *Haemophilus influenzae* type b, often produces beta-lactamase, which inactivates penicillin V. Acute epiglottitis is also an airway emergency that needs parenteral therapy, and an oral tablet is unsuitable. The 99.90% score is a knowledge-graph prediction, not evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G/20.1.2/145 | Incil Vk | Tablet | Not stated in the data provided |

Only oral tablets are registered. No injectable form is registered, which matters because epiglottitis needs parenteral treatment.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no trial or literature support for epiglottitis, and the mechanism is a poor fit for the likely pathogen and the required route of administration. The prediction should not be advanced on the model score alone.

Other candidates from the same run do not offer a better route forward:
- **Laryngitis:** a double-blind trial of penicillin V (PMID 3918495) and the Cochrane reviews found no benefit.
- **Gonococcal urethritis:** the only evidence is 1950s uncontrolled series, and gonococcal penicillin resistance is now widespread.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Local *H. influenzae* type b beta-lactamase and penicillin susceptibility data
- A specific clinical hypothesis that explains why an oral penicillin would be used instead of established parenteral therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

