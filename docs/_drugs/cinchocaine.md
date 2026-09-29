---
layout: default
title: Cinchocaine
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 7
---

# Cinchocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cinchocaine: From Topical Local Anaesthesia to Bronchitis

## One-Sentence Summary

Cinchocaine is a local anaesthetic, marketed in South Africa as an ointment (Scheriproct) and a suppository (Proctosedyl).
The TxGNN model predicts it may be effective for **bronchitis**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data provided (cinchocaine is generally known as a local anaesthetic) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cinchocaine is generally known as a sodium-channel-blocking local anaesthetic, which could at most suggest symptomatic relief, such as cough suppression. This has not been verified here.

Nothing in the data links a local anaesthetic to disease-modifying activity in bronchitis. The high score (99.77%) most likely reflects proximity in the knowledge graph rather than biology.

The available formulations are an ointment and a suppository. Neither is an obvious route for treating airway disease, and route compatibility has not yet been assessed.

The six other predictions in the pack are also L5, with no trials or publications, and all are on Hold: acrodermatitis chronica atrophicans, neonatal dermatomyositis, childhood connective-tissue-disease-associated interstitial lung disease, acne keloid, familial hydroa vacciniforme and amyopathic dermatomyositis. Most have no plausible mechanistic link, and several involve paediatric populations with no safety data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. E/11.8/0667 | Scheriproct (new formulary) | Ointment | Not stated in the registration data provided |
| Reg. No. E529 (Act 101 of 1965) | Proctosedyl Suppositories | Suppository | Not stated in the registration data provided |

Essential Medicines List (EML) status was not included in the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no documented mechanism. The registered formulations (ointment and suppository) are also not obviously suited to bronchitis.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), which is required before any safety screening
- Mechanism of action data (for example from DrugBank) to test whether any plausible link to bronchitis exists
- Any preclinical or clinical evidence in bronchitis; without it, the prediction stays at L5
- A route and formulation assessment showing that a suitable dosage form exists for the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

