---
layout: default
title: Naphazoline
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Nasal/Ocular Decongestant to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is an imidazoline-class alpha-1/alpha-2 adrenergic agonist historically used as a topical vasoconstrictor for nasal and ocular decongestion. The TxGNN model predicts potential efficacy for **Hypotrichosis Simplex of the Scalp**, but this is currently supported by **0 clinical trials** and **0 publications**, and the drug's core mechanism (vasoconstriction) runs counter to the vasodilatory mechanism typically associated with hair-growth therapies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nasal/ocular congestion (topical decongestant) — based on known pharmacological class; no formal SAHPRA-approved indication text available |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for naphazoline is not currently available in this evidence pack. Based on known pharmacological class information, naphazoline is an imidazoline-derivative alpha-1/alpha-2 adrenergic receptor agonist; its established efficacy in nasal and ocular decongestion is achieved through local vasoconstriction.

Hair-growth-promoting therapies (e.g., minoxidil) generally rely on the opposite mechanism — vasodilation and increased cutaneous blood flow to the follicle. Naphazoline's vasoconstrictive action is therefore mechanistically discordant with, rather than supportive of, a hair-growth indication. The evidence pack's own repurposing rationale flags this contradiction directly, noting that the high TxGNN score likely reflects knowledge-graph embedding similarity rather than genuine pharmacological plausibility. Notably, the same drug also receives a high TxGNN score for the opposite phenotype, hypertrichosis (excess hair growth), which is internally inconsistent and further suggests the signal is statistical noise rather than a mechanistic finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Naphazoline is not currently registered with SAHPRA (0 registrations on file); no local market/product information is available for this evidence pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: Safety warning and contraindication data for this evidence pack are flagged as a blocking data gap — TFDA/local PI warnings could not be retrieved, which by itself precludes a formal safety pre-screen (S1) for this candidate.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a model prediction alone (L5) with no supporting clinical trials or literature, and the proposed mechanism (vasoconstriction) is mechanistically inconsistent with the biology of hair growth. Naphazoline is also unregistered in South Africa, and mandatory safety data (warnings/contraindications) is missing, which blocks any formal safety pre-screen.

**To proceed, the following is needed:**
- Verified mechanism-of-action data (DrugBank/primary literature)
- SAHPRA/manufacturer Professional Information, including warnings and contraindications, to unblock safety pre-screening
- Preclinical or mechanistic studies specifically evaluating naphazoline (or the imidazoline class) in hair-follicle biology
- Resolution of the internal inconsistency between this prediction and the drug's concurrent high-score prediction for hypertrichosis (opposite phenotype) before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

