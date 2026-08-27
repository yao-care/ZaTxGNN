---
layout: default
title: Ferrous Gluconate
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 5
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ferrous Gluconate: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferrous gluconate is an oral iron salt used to correct iron deficiency and iron deficiency anemia. The TxGNN model's top-ranked prediction is **Plummer-Vinson syndrome**, a condition whose core pathology is chronic iron deficiency anemia with esophageal web — a mechanistically strong pairing, but this evidence pack currently holds **no clinical trials and no literature** specifically confirming it, and key safety data (warnings, contraindications) is also missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency / iron deficiency anemia (no formal SAHPRA-approved indication text on file — product not marketed in South Africa) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this candidate. Based on known pharmacology, ferrous gluconate is a ferrous (Fe²⁺) iron salt that replenishes iron stores and corrects iron-restricted erythropoiesis — this is its established, well-proven action in treating iron deficiency and iron deficiency anemia.

Plummer-Vinson syndrome (also known as Paterson-Kelly syndrome) is classically defined by the triad of dysphagia, esophageal web, and iron deficiency anemia. Correcting the underlying iron deficiency with oral iron therapy is already standard clinical practice for this condition — so the mechanistic link here is direct rather than an indirect extrapolation across unrelated disease biology.

The main caveat is evidentiary, not mechanistic: this evidence pack contains **zero clinical trials and zero literature entries** indexed specifically against "Plummer-Vinson syndrome" (see query log entries #2–#4, all 0 results). The source scoring itself frames this as a "Research Question" — a biologically plausible, practice-consistent hypothesis that has not been independently validated within this database.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications (For Context)

TxGNN generated four additional candidates for ferrous gluconate. Notably, the disease with the strongest *actual* evidence in this pack is ranked lowest by model score:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 2 | Vitamin B12/folate-independent constitutional megaloblastic anemia | 99.94% | L5 | Hold |
| 3 | Non-syndromic esophageal malformation | 99.67% | L5 | Hold |
| 4 | Biotin metabolic disease | 99.42% | L5 | Hold |
| 5 | Vitamin deficiency disorder | 99.17% | **L2** | **Proceed with Guardrails** |

Rank 5 ("vitamin deficiency disorder") is supported by 4 clinical trials (including a completed double-blind RCT, NCT06869824, n=36) and 2 literature items, and carries the highest evidence tier of any candidate for this drug. It may warrant separate evaluation alongside the top-ranked Plummer-Vinson prediction.

---

## South Africa Market Information

Ferrous gluconate has **0 SAHPRA registrations** on file in this evidence pack; the product is currently listed as not marketed in South Africa. No registration numbers, product names, or approved indication texts are available to tabulate.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: the underlying data pack flags TFDA-equivalent label warnings/contraindications as a **Blocking** data gap (DG001) — this alone prevents a formal initial safety assessment (S1 stage) for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale for Plummer-Vinson syndrome is strong and consistent with existing clinical practice, but no clinical trials or literature in this dataset independently confirm it, and TxGNN's own scoring labels it a "Research Question" (S1 stage).
- A Blocking data gap on label warnings/contraindications (DG001) prevents even an initial safety assessment.

**To proceed, the following is needed:**
- SAHPRA/manufacturer Professional Information (PI): warnings, contraindications, drug interactions
- Mechanism of action (MOA) documentation from DrugBank or equivalent source
- Targeted literature/trial search for "ferrous gluconate" + "Plummer-Vinson syndrome" beyond this evidence pack, given the current zero-hit query log
- Consider parallel evaluation of rank-5 candidate (vitamin deficiency disorder), which already has L2 evidence support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

