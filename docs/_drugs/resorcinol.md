---
layout: default
title: Resorcinol
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Resorcinol
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

# Resorcinol: From Topical Keratolytic (Acne) Use to Predicted Acne Keloid

## One-Sentence Summary

> Resorcinol is a phenolic keratolytic agent known internationally for topical use in acne and hyperkeratotic skin conditions, though it is not currently registered or marketed in South Africa.
> The TxGNN model predicts it may be effective for **Acne Keloid** (acne keloidalis),
> but **no clinical trials or published literature** currently support this direction — the prediction rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on South African license record; internationally documented as a topical keratolytic for acne and keratinizing skin disorders |
| Predicted New Indication | Acne Keloid (acne keloidalis) |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only — no supporting trials or literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for resorcinol is not available in this evidence pack. Based on known pharmacological information, resorcinol is a phenolic keratolytic that has long been used topically for acne and other hyperkeratotic dermatological conditions, exerting anti-inflammatory and keratolytic (keratin-dissolving) effects.

Acne keloid (acne keloidalis nuchae) shares pathophysiological features with acne — follicular occlusion, excess keratinization, and chronic inflammation — which provides a plausible, indirect mechanistic rationale for resorcinol's predicted activity in this condition.

However, this link should be interpreted cautiously: the very high TxGNN score most likely reflects resorcinol's existing knowledge-graph proximity to "acne"-related nodes rather than independent new evidence. No clinical trials or literature currently corroborate efficacy specifically in acne keloid, so this remains a hypothesis generated purely by graph inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Resorcinol currently has no SAHPRA registrations and is not marketed in South Africa (0 licenses on record). No product, dosage form, or approved indication data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(No TFDA/SAHPRA warnings, contraindications, or drug interaction data are currently available — this is flagged as a blocking data gap for any further safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (L5), with zero corroborating clinical trials or literature, no confirmed MOA data, and no South African market presence. There is insufficient evidence to advance beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI (currently a Blocking data gap)
- Confirmed mechanism of action data from DrugBank or primary literature
- At least preclinical or observational evidence directly linking resorcinol to acne keloid before considering trial design
- SAHPRA registration status review, since the drug is not currently marketed in South Africa

**Note on other predicted indications:** Ranks 2–10 in this evidence pack (e.g., amyopathic/neonatal dermatomyositis, rheumatoid vasculitis, ankylosing spondylitis, hypermobility of coccyx) were annotated by the source analysis as lacking any plausible mechanistic link to resorcinol's known topical/keratolytic pharmacology, and are likely artifacts of knowledge-graph proximity within dermatology-adjacent nodes rather than genuine repurposing signals. None are recommended for further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

