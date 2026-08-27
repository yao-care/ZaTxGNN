---
layout: default
title: Phenoxymethylpenicillin
parent: 僅模型預測 (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
---

# Phenoxymethylpenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Phenoxymethylpenicillin: From Bacterial Infections to Epiglottitis

## One-Sentence Summary

Phenoxymethylpenicillin (Penicillin V, DrugBank DB00417) is a narrow-spectrum oral penicillin classically used for susceptible bacterial infections. The TxGNN model assigns its single highest-scoring candidate indication to **Epiglottitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review argues against biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the evidence pack (Phenoxymethylpenicillin/Penicillin V is a narrow-spectrum beta-lactam antibiotic) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Phenoxymethylpenicillin is not available in this evidence pack. Based on known pharmacological classification, it is a narrow-spectrum beta-lactam antibiotic that acts by inhibiting bacterial cell wall synthesis through binding to penicillin-binding proteins (PBPs) — the same class-level mechanism referenced elsewhere in this evidence pack for its other candidate indications.

For epiglottitis specifically, the model's own rationale weighs against clinical applicability: the dominant causative organism, *Haemophilus influenzae*, is frequently resistant to narrow-spectrum penicillins, and epiglottitis is a life-threatening airway emergency that is managed with immediate broad-spectrum intravenous antibiotics — not an oral narrow-spectrum agent. In other words, while the TxGNN model produces a very high numerical prediction score, the underlying pharmacological and clinical logic does not support this repurposing direction, and no clinical trial, literature, or registry evidence currently exists to counterbalance that concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA-registered products were found for this drug in the evidence pack (0 registrations; market status: not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction carries a very high TxGNN score but no supporting clinical trial or literature evidence (Evidence Level L5), and the drug's mechanistic profile (narrow-spectrum, oral, poor coverage of *H. influenzae*) conflicts with the standard emergency, broad-spectrum IV management required for epiglottitis.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Phenoxymethylpenicillin from DrugBank or an equivalent source
- Local/regional antimicrobial susceptibility data for epiglottitis pathogens against Penicillin V
- SAHPRA Professional Information (PI), including warnings, contraindications, and drug interaction data
- Preclinical or observational evidence before any advancement beyond the current model-prediction-only stage

*Note: This evidence pack also lists nine additional lower-scoring TxGNN candidates for this drug (e.g., laryngitis, gonococcal urethritis), several with partial historical literature support; these were not evaluated in this report, which is scoped to the top-ranked candidate only.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

