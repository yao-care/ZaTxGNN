---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

> Etonogestrel is a synthetic progestin best known as the active hormone in long-acting subdermal contraceptive implants (e.g. Nexplanon).
> The TxGNN model predicts it may be effective for **Amenorrhea**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on knowledge-graph inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (subdermal progestin implant) — not documented in this Evidence Pack; based on established pharmacological knowledge of etonogestrel |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data is not available in this Evidence Pack (`original_moa` is flagged as a data gap). Based on the drug's known pharmacology, etonogestrel is a progesterone-receptor agonist: it suppresses ovulation and induces endometrial atrophy. This same mechanism is why amenorrhea is a well-recognised **side effect** of etonogestrel implants in contraceptive use.

The TxGNN prediction appears to be drawing on this same mechanistic pathway, but in reverse — proposing etonogestrel as a deliberate treatment *for* amenorrhea-adjacent conditions (e.g. therapeutic induction of amenorrhea for heavy menstrual bleeding or endometriosis-related pain, a strategy with precedent among other progestins). However, this Evidence Pack contains **no clinical trials or literature** that test etonogestrel specifically for treating amenorrhea, so the mechanistic plausibility cannot yet be distinguished from a knowledge-graph artifact.

It is also worth noting that 7 of the other 9 top-ranked candidates in this pack are benign breast conditions (fibrocystic disease, adenosis, mammary dysplasia, etc.) with similarly zero trial/literature support — suggesting the model may be clustering around hormone-adjacent disease nodes in the graph rather than surfacing a specific, well-differentiated pharmacological signal for amenorrhea itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Etonogestrel is currently **not registered with SAHPRA** (0 licenses on file; market status: Not marketed). No approved South African product information is available to reference for indication wording, dosage form, or Essential Medicines List (EML) status.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this Evidence Pack flags TFDA/product-label warnings and contraindications as a **Blocking** data gap — this alone would prevent progression to a formal safety review even if clinical evidence for the new indication were stronger.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (amenorrhea) is supported only by the TxGNN knowledge-graph score (L5 — model prediction only, no supporting studies), with zero clinical trials or literature identified. Combined with the absence of any SAHPRA registration and a **Blocking** data gap on safety warnings/contraindications, there is insufficient evidence to advance this candidate past a research question.

**To proceed, the following is needed:**
- Verified mechanism-of-action and product-label data (SAHPRA/manufacturer PI) to resolve the Blocking data gap (DG001)
- Confirmed original indication and regulatory history for etonogestrel outside South Africa, for comparison
- Preclinical or observational evidence specifically evaluating etonogestrel for amenorrhea treatment (as opposed to amenorrhea as a contraceptive side effect)
- If pursued further, consider whether rank-8 candidate (lactation disease, L3 — 2 completed trials) is a more evidence-ready starting point, though those trials assessed breastfeeding compatibility rather than therapeutic efficacy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

