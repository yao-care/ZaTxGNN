---
layout: default
title: Terbinafine
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Terbinafine
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

# Terbinafine: From Fungal Skin Infections to Creeping Myiasis

## One-Sentence Summary

Terbinafine is an allylamine-class antifungal, with a pharmacology described in the available evidence as inhibiting squalene epoxidase (fungicidal action against dermatophytes). The TxGNN model's top-ranked prediction is **Creeping Myiasis**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the underlying evidence pack itself flags the mechanistic link as absent — creeping myiasis is caused by migrating fly larvae, not fungi.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from SAHPRA licensing data (drug not registered in South Africa); evidence pack characterizes terbinafine as an antifungal for dermatophyte/fungal skin infections |
| Predicted New Indication | Creeping Myiasis |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal DrugBank mechanism-of-action field is a data gap. However, the evidence pack's own rationale notes consistently describe terbinafine as an allylamine-class antifungal that inhibits squalene epoxidase, blocking ergosterol synthesis in fungal cell membranes — a mechanism validated for dermatophyte infections (tinea, onychomycosis) elsewhere in this same evidence set (see ranks 8 and 10 below).

For the top-ranked candidate, **creeping myiasis**, the evidence pack explicitly states this prediction is **not mechanistically supported**: creeping myiasis results from subcutaneous migration of fly larvae, a parasitic/entomological process entirely unrelated to fungal ergosterol synthesis. No clinical trials and no literature exist for this drug-disease pair; the signal is a pure TxGNN model output (data-driven pattern in the knowledge graph) rather than a biologically grounded hypothesis.

In short, this is a case where the model's highest-scoring prediction does not correspond to its most credible one — the evidence pack itself surfaces stronger, mechanistically coherent candidates further down the ranking (see note in Conclusion).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Terbinafine currently has **0 SAHPRA registrations** and is recorded as **not marketed** in South Africa. No product licenses or approved indication text are available in this evidence pack to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (creeping myiasis) has no mechanistic plausibility, no clinical trials, and no supporting literature — it is a model-score-only (L5) signal, and the evidence pack's own analysis states the antifungal mechanism does not apply to a fly-larvae parasitic condition.

**To proceed, the following is needed:**
- Independent parasitological/entomological rationale for any anti-myiasis effect of terbinafine, if one is to be pursued
- SAHPRA-approved PI (warnings, contraindications) — currently a blocking data gap
- Formal DrugBank MOA confirmation
- SAHPRA registration/market authorization, since terbinafine is currently not marketed in South Africa

**Note:** Within this same evidence pack, other TxGNN-predicted indications for terbinafine show materially stronger support and may warrant separate evaluation — notably **superficial mycosis** (L2, one completed comparative trial vs. itraconazole, extensive literature, "Proceed with Guardrails") and **tinea manuum** (L2, "Proceed with Guardrails"), both mechanistically consistent with terbinafine's established antifungal activity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

