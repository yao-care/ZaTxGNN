---
layout: default
title: Triamterene
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 6
---

# Triamterene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Triamterene: From Oedema/Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic conventionally used for fluid retention (oedema) and hypertension. The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oedema / hypertension (potassium-sparing diuretic class) — no South Africa-specific indication text available |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from DrugBank at the time of this report (flagged as a High-severity data gap). Based on known pharmacology, triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron, reducing sodium reabsorption and potassium excretion — its established use is chronic oral management of oedema and hypertension.

Malignant renovascular hypertension, however, is a hypertensive emergency typically driven by severe renin-angiotensin-aldosterone system (RAAS) activation, and standard management relies on intravenous antihypertensives and urgent correction of the underlying renal vascular lesion — not chronic oral diuretics. The evidence pack's own mechanistic assessment flags a specific safety concern: in a high-renin state such as this, a potassium-sparing agent carries a meaningful hyperkalaemia risk rather than a clear therapeutic benefit.

The identical prediction score assigned to a closely related disease node ("malignant hypertensive renal disease," rank 2) with the same lack of supporting evidence suggests these two high-ranking predictions likely reflect similarity between disease embeddings in the knowledge graph rather than an independently validated pharmacological signal. This prediction should be treated as hypothesis-generating only, not as clinical guidance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Triamterene is not currently marketed in South Africa — no SAHPRA registrations were found (0 licenses on record). No product, dosage form, or approved indication data is available for this evaluation.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: TFDA/PI warnings and contraindications for this drug are currently a Blocking data gap (DG001) — this alone prevents progression to a formal safety (S1) review.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but evidence level is L5 — no clinical trials, no supporting literature, and the drug is unregistered in South Africa. The rationale itself raises a plausible safety concern (hyperkalaemia risk in a high-renin hypertensive emergency) rather than supporting the prediction, and the same score applied to a near-duplicate disease node suggests a knowledge-graph artefact rather than an independent signal.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Independent preclinical or clinical evidence specific to malignant renovascular hypertension (or the related renal disease indication)
- Clinical assessment of whether a chronic oral potassium-sparing diuretic is even an appropriate drug class for a hypertensive emergency indication
- SAHPRA registration status confirmation, since the product is not currently marketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

