---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

---

## One-Sentence Summary

Bisoprolol is a highly selective β1-adrenergic receptor blocker, established in clinical practice globally for the management of hypertension, angina pectoris, and chronic heart failure. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, achieving a prediction score of **99.94%**; however, this prediction is currently supported by **0 clinical trials** and **0 directly relevant publications**, representing knowledge graph inference only (Evidence Level L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, Angina Pectoris, Chronic Heart Failure (globally established; no SAHPRA-approved indication currently on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 – Mechanistic inference / knowledge graph only; no clinical studies |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available in the current Evidence Pack. Based on established pharmacology, bisoprolol is a highly selective β1-adrenergic receptor antagonist. Its primary actions include reducing heart rate and cardiac output via cardiac β1-blockade, and — critically relevant here — suppressing renin secretion from the kidney's juxtaglomerular cells, thereby reducing angiotensin II and aldosterone production through the renin-angiotensin-aldosterone system (RAAS). This dual cardiovascular and renal RAAS-modulating profile provides the theoretical basis for the TxGNN prediction.

The predicted indication, malignant hypertensive renal disease, is characterised by extremely elevated blood pressure causing progressive microvascular injury to glomeruli and renal arterioles, frequently exacerbated by RAAS overactivation. The mechanistic extrapolation is that bisoprolol, by blunting juxtaglomerular renin release, could theoretically interrupt the self-perpetuating RAAS cycle driving hypertensive renal injury — a pathway conceptually similar to the rationale behind ACE inhibitors and ARBs in hypertensive nephropathy.

However, there are significant clinical limitations to this prediction. Malignant hypertension (hypertensive emergency) requires immediate blood pressure reduction with intravenous agents such as labetalol, nicardipine, or sodium nitroprusside. Oral β1-selective blockers are not appropriate for acute-phase intervention and may paradoxically worsen renal perfusion by allowing unopposed α-adrenergic peripheral vasoconstriction. It is also notable that the TxGNN scores for ranks 1 and 2 are identical (0.999363), suggesting the knowledge graph may treat these two related disease nodes as part of the same cluster — increasing the risk of score inflation and false-positive interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Bisoprolol currently has **no SAHPRA-registered products** in South Africa. There are no registration numbers, approved dosage forms, or approved indication texts on record.

> **Important Note:** Bisoprolol is not marketed in South Africa under SAHPRA registration. Any clinical use in the South African context would require access via special import mechanisms (e.g., Section 21 of the Medicines and Related Substances Act authorisation). Bisoprolol is widely registered in other jurisdictions (UK MHRA, EMA, US FDA) and should be readily accessible for reference label review.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) — or a comparable internationally recognised regulatory label (MHRA/EMA) — for full safety information, including key warnings, contraindications, and drug interaction data. Report any adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.94%), bisoprolol for malignant hypertensive renal disease has zero supporting clinical trials or directly relevant published literature (Evidence Level L4). The mechanistic link, while biologically plausible in the chronic RAAS-suppression context, is an indirect extrapolation; the acute clinical presentation of malignant hypertension is contraindicated for oral β-blocker therapy. Additionally, the drug is not currently marketed in South Africa, introducing a regulatory barrier that must be addressed before any repurposing pathway can advance.

**To proceed, the following is needed:**

- **MOA data retrieval:** Query DrugBank API for DB00612 to obtain the complete mechanism of action, enabling a more rigorous mechanistic plausibility assessment
- **Safety data review:** Obtain SAHPRA PI or equivalent international regulatory label (MHRA SmPC / FDA label) for full contraindications, key warnings, and drug interaction profile
- **Clinical scenario clarification:** Determine whether the hypothesis targets the *chronic* phase of hypertensive nephropathy (long-term renoprotection after acute blood pressure stabilisation) rather than the acute hypertensive emergency — the former is mechanistically more defensible
- **Targeted literature search:** Conduct a focused search for bisoprolol (and class-effect β1-blockers) specifically in hypertensive nephropathy, chronic kidney disease with hypertension, and RAAS-modulation in renal protection contexts
- **SAHPRA registration pathway assessment:** If evidence from comparable markets supports this use, evaluate the regulatory route for South African registration or Section 21 authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

