---
layout: default
title: Dextropropoxyphene
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 1
---

# Dextropropoxyphene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dextropropoxyphene: From Opioid Analgesic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Dextropropoxyphene is a propionate-derivative opioid historically used for mild-to-moderate pain relief (a use not documented in this evidence pack and withdrawn from many markets due to cardiotoxicity concerns). The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no external validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (`original_indications` is empty) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for dextropropoxyphene in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, dextropropoxyphene is a weak mu-opioid receptor agonist structurally related to methadone, historically used for mild-to-moderate pain (often in combination with paracetamol). It is not currently registered or marketed in South Africa according to this dataset.

No mechanistic pathway connecting opioid receptor activity to vasopressin V2-receptor-mediated inappropriate antidiuresis is documented in this pack, and no clinical or literature evidence has been retrieved to support such a link. As a result, the biological plausibility of this repurposing candidate cannot currently be assessed — the association appears to originate solely from the TxGNN knowledge-graph embedding model, without independent mechanistic or clinical corroboration.

Given the absence of any supporting mechanistic, clinical, or literature evidence, this candidate should be treated as an early-stage computational hypothesis only, not as a pharmacologically substantiated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Dextropropoxyphene has **0 SAHPRA registrations** and is currently **not marketed** in South Africa. No product licenses, dosage forms, or approved indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: a **Blocking** data gap (DG001 — TFDA/SAHPRA package insert warnings and contraindications) has been identified in this evidence pack. This gap must be resolved before any Stage 1 (S1) safety screening can be performed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only, with zero supporting clinical trials or literature), and a Blocking data gap prevents even an initial (S1) safety assessment. There is insufficient basis to advance this candidate at this time.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / package insert (warnings, contraindications) — resolves Blocking gap DG001
- Detailed mechanism of action data via DrugBank API — resolves High-severity gap DG002
- Any preclinical or mechanistic studies linking opioid pharmacology to vasopressin V2-receptor-mediated antidiuresis
- Ongoing monitoring for new clinical trial registrations or publications on this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

