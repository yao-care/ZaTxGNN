---
layout: default
title: Iron Sucrose
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Iron Sucrose
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

Using no additional skill — this is a direct, single-pass document-generation task with fixed extraction rules and no ambiguity requiring brainstorming or debugging.

# Iron Sucrose: From Intravenous Iron Replacement to Primary Hyperoxaluria

## One-Sentence Summary

> Iron sucrose is an intravenous iron replacement product; the underlying Evidence Pack does not document its formally approved indication text or mechanism of action (both flagged as data gaps).
> The TxGNN model's top-ranked prediction is **Primary Hyperoxaluria**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the pack's own mechanistic-link analysis finds no known pathophysiological connection between IV iron supplementation and primary hyperoxaluria.
> Across all 10 predicted indications in this pack, only one (hyperparathyroidism, rank 8) reaches even indirect literature support — the overall evidence base for repurposing is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (no license records or indication text available) |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for iron sucrose is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on information present in the supporting literature entries elsewhere in the pack (e.g. studies on IV iron sucrose in haemodialysis and peritoneal dialysis patients), iron sucrose is understood to function as an intravenous iron-replacement therapy used to correct iron-deficiency anaemia, commonly in the setting of chronic kidney disease.

Primary hyperoxaluria is a group of rare genetic disorders (AGT, GRHPR, or HOGA1 gene defects) causing excessive hepatic oxalate production, leading to recurrent nephrolithiasis and nephrocalcinosis. The pack's own repurposing rationale for this candidate states explicitly that there is **no known mechanistic link** between IV iron supplementation and the oxalate-metabolism pathways underlying this disease.

Because the prediction carries a high TxGNN score but zero corroborating clinical or literature evidence, and the drug's own MOA is undocumented, this candidate should be treated as a hypothesis-generation signal only, not as a basis for clinical or regulatory action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Iron sucrose currently holds no SAHPRA registrations (0 licenses on file); the product is recorded as **not marketed** in South Africa in this Evidence Pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: this Evidence Pack flags TFDA/SAHPRA labelled warnings and contraindications as a Blocking-severity data gap (DG001) — a formal safety review (S1 stage) cannot proceed until PI data is obtained.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (primary hyperoxaluria) has an evidence level of L5 — a model score with no clinical trials, no ICTRP registrations, and no literature — and the pack's own rationale states no plausible mechanistic link exists.
- Reviewing all 10 predicted indications in this pack: most are L5 (no evidence); one (pancreatitis, rank 2) has literature evidence pointing in the *opposite* direction — multiple animal/mechanistic studies suggest iron overload may cause pancreatic injury, a safety signal rather than a therapeutic rationale; the only candidate reaching L3 (hyperparathyroidism, rank 8) relies on indirect, drug-class-level evidence (studies of other iron-based phosphate binders, not iron sucrose itself).
- Combined with the Blocking-severity data gap on TFDA/SAHPRA safety labelling (DG001), there is currently insufficient basis to advance any candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — required before any safety pre-screen (S1) can occur
- Confirmed mechanism of action data (DrugBank or equivalent)
- Direct (not drug-class-inferred) clinical or preclinical evidence specifically for iron sucrose in the hyperparathyroidism/CKD-MBD context, if that direction is pursued instead
- Clarification of iron sucrose's original approved indication, since no license or indication text is present in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

