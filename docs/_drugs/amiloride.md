---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 6
---

# Amiloride
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

# Amiloride: From Potassium-Sparing Diuresis to Malignant Renovascular Hypertension

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal nephron, established internationally for managing oedema and hypertension — though it currently holds no SAHPRA registration in South Africa.
The TxGNN model predicts it may have utility in **Malignant Renovascular Hypertension**, a severe hypertensive emergency involving end-organ damage driven by over-activation of the renin–angiotensin–aldosterone axis.
Supporting evidence is currently limited to **0 clinical trials** and **1 indirect review publication**, placing confidence at the mechanistic/preclinical level (Evidence Level L4).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication; internationally used as a potassium-sparing diuretic for oedema (with or without hypokalaemia) and hypertension |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 (mechanistic / preclinical) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available for this report. Based on established pharmacology, Amiloride is a pyrazine-carbonyl-guanidine compound that selectively blocks the epithelial sodium channel (ENaC) at the apical membrane of principal cells in the distal nephron. By preventing luminal sodium entry, it reduces sodium and water reabsorption without promoting potassium loss — hence its classification as a potassium-sparing diuretic. It is commonly co-prescribed with loop or thiazide diuretics specifically to counteract drug-induced hypokalaemia.

Malignant renovascular hypertension arises when renal artery stenosis triggers a marked, sustained activation of the renin–angiotensin–aldosterone system (RAAS). The resulting aldosterone excess upregulates ENaC expression in the collecting duct, driving continued sodium retention, plasma volume expansion, and further blood pressure elevation. Amiloride's direct antagonism of ENaC represents a mechanistically coherent point of intervention in this aldosterone-driven cycle — making the TxGNN prediction biologically plausible.

That said, clinical applicability as a primary agent in this setting is uncertain. Malignant renovascular hypertension is a hypertensive emergency that typically demands rapid, potent blood pressure reduction via ACE inhibitors, ARBs, calcium-channel blockers, or vascular revascularisation. Amiloride's diuretic potency alone is unlikely to be sufficient. Furthermore, this condition frequently impairs renal function, which sharply increases the risk of dangerous hyperkalaemia with Amiloride. Its independent therapeutic role in malignant renovascular hypertension would require dedicated prospective investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Amiloride in malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review / Diagnostic Investigation | *Journal of Hypertension* (Supplement) | Examines mineralocorticoid-driven hypertension, including primary aldosteronism (Conn's syndrome) presenting with hypokalaemia and suppressed plasma renin activity; provides indirect mechanistic context for the aldosterone–ENaC axis that underpins Amiloride's predicted relevance in renovascular hypertension |

---

## South Africa Market Information

Amiloride is **not currently registered with SAHPRA** and has no approved products on the South African market. No licensed product listings are available.

Should clinical use be contemplated in the context of a research protocol, a SAHPRA Section 21 application for an unregistered medicine would be required.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As Amiloride is not currently registered in South Africa, the manufacturer's global product labelling (e.g., FDA-approved prescribing information) should be consulted as an interim reference. Report any adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a biologically plausible ENaC-mediated mechanistic link between Amiloride and malignant renovascular hypertension; however, evidence remains at the L4 (mechanistic/preclinical) level, with no registered clinical trials and only one indirectly relevant review paper. The acute severity of the target condition, the drug's absence from the South African market, and the significant safety risks inherent to its use in patients with compromised renal function collectively preclude clinical application without a structured research programme.

**To proceed, the following is needed:**
- Retrieval and review of full DrugBank mechanism of action data for Amiloride (flagged as a High-severity data gap — DG002)
- Review of SAHPRA-equivalent regulatory safety information from international labels (flagged as a Blocking data gap — DG001)
- Expanded targeted literature search for Amiloride specifically in malignant hypertension and secondary hyperaldosteronism contexts
- Pre-clinical or pilot clinical data directly examining Amiloride efficacy and safety in malignant renovascular hypertension before any human study protocol is proposed
- Renal function and hyperkalaemia risk stratification framework as a prerequisite for any future trial design
- **Note:** The **Rank 6 prediction — Chronic Pulmonary Heart Disease (Cor Pulmonale)** — carries L3 evidence including small RCT-level data (e.g., PMID [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/), [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/)) and may represent a more immediately actionable repurposing pathway worthy of parallel evaluation

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This document should be read in conjunction with SAHPRA-approved prescribing information where available.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

