---
layout: default
title: Tolnaftate
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Tolnaftate
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

# Tolnaftate: From Superficial Dermatophyte Infections to Majocchi Granuloma

## One-Sentence Summary

Tolnaftate is a topical thiocarbamate antifungal historically used to treat superficial dermatophyte ("ringworm"/tinea) skin infections. The TxGNN model's top-ranked prediction is **Majocchi Granuloma** (a deeper, follicular dermatophyte infection), but **no clinical trials and no published literature** currently support this specific use — the prediction rests on mechanistic reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial fungal (dermatophyte/tinea) skin infections — derived from the evidence pack's own tolnaftate literature (e.g., PMID 14275504, 14288002); no SAHPRA license text is available because the product is not marketed in South Africa |
| Predicted New Indication | Majocchi Granuloma |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known information, Tolnaftate is a thiocarbamate-class topical antifungal that inhibits squalene epoxidase, disrupting ergosterol synthesis in dermatophyte fungi. Its efficacy against superficial dermatophyte skin infections is well established in the older literature (e.g., PMID 14275504 "Tolnaftate, a Potent Topical Antifungal Agent"; PMID 14288002 "Effect of Tolnaftate on Superficial Mycotic Infections"), and mechanistically the same antifungal target could plausibly extend to other dermatophyte-driven conditions.

Majocchi granuloma is a deep, follicular dermatophyte infection — the causative organisms overlap with those tolnaftate is active against. However, this condition typically requires an antifungal that can penetrate into and around the hair follicle, and clinical practice generally favors systemic (oral) antifungal therapy for this reason. Whether tolnaftate's topical formulation achieves adequate follicular penetration is unproven; no pharmacokinetic, preclinical, or clinical data address this specific question.

The prediction should therefore be read as a hypothesis generated from shared pathogen biology, not as evidence of clinical efficacy in this deeper infection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Tolnaftate is **not currently marketed** in South Africa, and no SAHPRA registrations are recorded in this evidence pack (0 licenses). No product-level information (registration number, brand, dosage form, approved indication text) is available to tabulate.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Majocchi granuloma) has no supporting clinical trials or literature — only a plausible but unverified mechanistic rationale, and a known concern that a topical formulation may not adequately penetrate the hair follicle where this infection resides.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) data from DrugBank or SAHPRA PI
- Preclinical or pharmacokinetic data on follicular penetration of topical tolnaftate
- At minimum a case series or pilot study of topical tolnaftate specifically in Majocchi granuloma
- SAHPRA registration status confirmation, since the product is currently not marketed in South Africa

**Note for reviewers:** this evidence pack also contains a separate candidate, *superficial mycosis* (rank 5, Evidence Level L2, decision stage S3, "Proceed with Guardrails"), which is essentially a restatement of tolnaftate's already-established original indication rather than a genuinely new use. It is flagged here only because it demonstrates the model correctly recovering known pharmacology — it is not part of this report's headline repurposing claim.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

