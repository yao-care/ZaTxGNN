---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Econazole
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

# Econazole: From Topical Antifungal Therapy to Ectothrix Infectious Disease

## One-Sentence Summary

Econazole is an imidazole-class antifungal historically used to treat superficial fungal skin and mucosal infections. The TxGNN model predicts it may also be effective for **Ectothrix Infectious Disease** (a dermatophyte infection confined to the outer hair shaft), but this is currently a **model-score-only prediction** — no clinical trials and no literature in this evidence pack support it, and the drug is not presently registered for sale in South Africa.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no SAHPRA licence on file); internationally recognised as a topical antifungal for dermatomycoses and vulvovaginal candidiasis |
| Predicted New Indication | Ectothrix Infectious Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Econazole is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge — and consistent with the rationale text attached to other predictions in this same pack — Econazole is an imidazole-class antifungal that inhibits fungal cell-membrane ergosterol synthesis, and is established for treating superficial dermatomycoses and vulvovaginal candidiasis.

Ectothrix infectious disease refers to dermatophyte infection of the outer hair shaft, a pattern of superficial fungal infection. Mechanistically, this falls within the broad antifungal spectrum that imidazoles such as Econazole are known to cover, since ectothrix and related tinea infections are caused by the same dermatophyte genera (e.g. *Microsporum*, *Trichophyton*) that Econazole is active against in its established uses.

However, this mechanistic plausibility is theoretical only. The evidence pack's own rationale explicitly notes that this prediction is "僅為 TxGNN 預測分數" (based solely on the TxGNN prediction score), with no clinical trial or published literature identified specifically linking Econazole to ectothrix infection. The prediction should be treated as a hypothesis-generation signal rather than an evidence-backed candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Econazole has no SAHPRA registrations on file — market status is **Not Marketed**, with 0 licences recorded. No approved indication text is therefore available from South African regulatory records for this drug.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns Econazole a very high prediction score (99.97%) for ectothrix infectious disease, this rests entirely on the model output — there are zero clinical trials and zero literature citations supporting it (Evidence Level L5), and the drug currently has no SAHPRA registration in South Africa.

**To proceed, the following is needed:**
- Econazole's SAHPRA-approved Professional Information (warnings/contraindications) — currently a Blocking data gap
- Detailed mechanism of action (MOA) data from DrugBank or equivalent source — currently a High-severity data gap
- A targeted literature and trial search specific to Econazole in ectothrix/tinea capitis infection (the current search returned no hits)
- Confirmation of whether Econazole will be pursued for South African market registration, given it is not currently marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

