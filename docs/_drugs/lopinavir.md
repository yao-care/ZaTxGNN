---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, typically co-formulated with ritonavir (lopinavir/ritonavir) as part of antiretroviral therapy for human HIV infection. The TxGNN model's top-ranked prediction for this drug is **Feline Acquired Immunodeficiency Syndrome (FIV)**, a veterinary indication, but this prediction is currently supported by **no clinical trials and no published literature** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (data gap). Lopinavir is a known HIV-1 protease inhibitor used in human antiretroviral therapy. |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this evidence pack (data gap DG002). Based on known pharmacology, Lopinavir belongs to the protease inhibitor (PI) class of antiretrovirals, typically combined with ritonavir (as lopinavir/ritonavir) to boost plasma exposure, and its efficacy against HIV-1 infection in humans is well established.

The top-ranked prediction (FIV) is a veterinary lentiviral disease of cats. According to the evidence pack's own mechanistic assessment, this prediction rests solely on the TxGNN model score: "FIV is a feline lentivirus whose protease sequence differs substantially from HIV-1's; there is no direct evidence that human protease inhibitors inhibit FIV protease activity, and no clinical trials or literature currently support this indication." In other words, the model has identified a plausible target-class analogy (both are lentivirus proteases), but the sequence divergence between FIV and HIV-1 protease means the mechanism cannot be assumed to transfer, and there is no experimental confirmation.

It is worth noting that a related, better-supported signal exists lower in this ranking: **simian immunodeficiency virus (SIV) infection** (rank 2, same TxGNN score band) is supported by 3 published animal-model studies showing lopinavir-containing regimens produce viral load reduction in SIV-infected macaques — a translational HIV research model, not a distinct human or veterinary indication. This is scientifically more coherent than the FIV prediction but does not itself constitute new-indication evidence in humans.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Lopinavir is not currently marketed in South Africa under this evidence pack (0 SAHPRA registrations on record).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (FIV) is an L5 evidence-level, model-prediction-only signal with no clinical trials, no literature, and a stated mechanistic gap (protease sequence divergence between FIV and HIV-1). It is also a veterinary rather than human indication, which falls outside the scope of a South African human-medicine repurposing pathway. Combined with the absence of SAHPRA-approved safety labeling (a blocking data gap), there is no basis to advance this candidate.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, and drug interaction data (currently blocking, DG001)
- Confirmed mechanism of action from DrugBank or equivalent source (DG002)
- Direct in vitro/in vivo evidence of lopinavir activity against FIV protease, if this candidate is to be pursued further
- If a human indication is of interest, closer evaluation of the SIV-infection signal (rank 2) is a more evidence-grounded starting point, though it currently reflects an HIV translational research model rather than a standalone treatable condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

