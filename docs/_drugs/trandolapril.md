---
layout: default
title: Trandolapril
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

# Trandolapril: From ACE Inhibitor Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE inhibitor (ACEi); detailed original-indication and mechanism-of-action records were not available in this evidence pack, though ACEi-class drugs are typically used for hypertension and heart failure via RAAS blockade. The TxGNN model's top-scoring prediction for this drug is **Malignant Renovascular Hypertension** (score 99.92%), but this candidate currently has **zero supporting clinical trials or literature**, and the evidence pack's own mechanistic notes flag it as a likely contraindicated, high-risk scenario rather than a genuine repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug is annotated as an ACE inhibitor; ACEi class is typically indicated for hypertension/heart failure) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (no clinical trials, no literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for trandolapril was not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the classification referenced in the evidence pack's own rationale annotations, trandolapril is an ACE inhibitor: it blocks the renin-angiotensin-aldosterone system (RAAS) by inhibiting conversion of angiotensin I to angiotensin II, lowering blood pressure and reducing renal vascular resistance.

On the surface, this mechanism looks applicable to renovascular hypertension, since RAAS activation is central to that condition's pathophysiology. However, **malignant** renovascular hypertension is frequently associated with bilateral (or solitary-kidney) renal artery stenosis. In this specific setting, ACE inhibitors carry a well-recognised risk of precipitating acute renal failure, because glomerular filtration in stenotic kidneys becomes dependent on angiotensin II-mediated efferent arteriolar constriction — which ACEi therapy removes. The evidence pack's own rationale explicitly identifies this as "a clinical contraindication or high-risk scenario rather than a priority repurposing direction," which is consistent with the complete absence of clinical trials or literature for this drug-disease pair.

In short, the high TxGNN similarity score appears to reflect embedding-space proximity between hypertension-related disease terms rather than a genuine, clinically actionable repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

No SAHPRA registrations were found for trandolapril in this evidence pack (market status: Not Marketed, 0 licenses on record).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: the evidence pack's mechanistic rationale specifically flags that ACE inhibitors are associated with a risk of acute renal failure in patients with bilateral renal artery stenosis — a condition commonly underlying malignant renovascular hypertension. This should be treated as a critical safety signal for this specific candidate pending confirmation against the official PI (TFDA/SAHPRA warning data is currently missing — DG001, Blocking).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring TxGNN prediction for trandolapril (malignant renovascular hypertension) has no clinical trial or literature support (Evidence Level L5, decision stage S0), and the drug's own mechanistic profile suggests a probable contraindication (ACEi-induced acute renal failure risk in stenotic renal vasculature) rather than therapeutic benefit. This candidate should not advance without dedicated safety and mechanistic review.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information, particularly warnings/contraindications related to renal artery stenosis (DG001, Blocking)
- Confirmed mechanism-of-action data from DrugBank (DG002, High)
- Independent clinical or preclinical evidence specific to malignant renovascular hypertension, since none currently exists
- For context: among the six TxGNN-predicted indications provided for this drug, only **chronic pulmonary heart disease** (rank 6) has any literature support (one preclinical rat study, PMID 8989645) and reached decision stage S1 ("Research Question"); this may be a more worthwhile direction to monitor going forward, though it remains preclinical-only (L4) and unconfirmed in humans.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

