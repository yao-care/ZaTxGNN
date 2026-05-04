---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Diltiazem: From Hypertension and Angina to Ischaemic Stroke Susceptibility

## One-Sentence Summary

Diltiazem is a well-established non-dihydropyridine calcium channel blocker (NDHP-CCB) of the benzothiazepine class, widely used internationally for hypertension, angina pectoris, and supraventricular arrhythmias including atrial fibrillation.
The TxGNN model predicts it may be relevant to **ischaemic stroke susceptibility**, with **0 clinical trials** and **0 publications** directly supporting this specific direction.
Critically, the target disease ontology term is flagged as **formally obsolete** — the high prediction score (99.08%) is most likely an artefact of historical training data associations rather than a clinically actionable signal, and this candidate should not advance without ontology remapping.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA registration data available *(established international use: hypertension, angina, atrial fibrillation)* |
| Predicted New Indication | Ischaemic Stroke Susceptibility ⚠️ *Obsolete ontology term — formally retired from Disease Ontology* |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 — model prediction only, no supporting studies |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Diltiazem belongs to the benzothiazepine subclass of non-dihydropyridine calcium channel blockers (NDHP-CCBs). Its primary mechanism is blockade of L-type voltage-gated calcium channels (VGCC), which inhibits calcium influx into vascular smooth muscle and cardiac myocytes. The result is peripheral vasodilation, reduced heart rate, and decreased myocardial contractility. Although no MOA data was retrievable from the regulatory dataset for this evidence pack, diltiazem's pharmacology is extensively documented in international literature and guidelines.

There are plausible mechanistic pathways linking diltiazem to ischaemic stroke risk: (1) systemic blood pressure reduction decreases cerebrovascular wall shear stress and long-term endothelial injury; (2) improvement in cerebral haemodynamics through vasodilation; and (3) ventricular rate control in atrial fibrillation — a major cause of cardioembolic ischaemic stroke — which could indirectly reduce thromboembolic events. These indirect pathways offer biological plausibility for the TxGNN model's association and explain why the model assigns a high score.

However, this prediction requires significant caution before clinical consideration. The target disease term — **"obsolete susceptibility to ischemic stroke"** — has been formally retired from the Disease Ontology (DO). This means TxGNN may be mapping to a semantically invalid concept node, and the 99.08% score reflects the model's learned associations with this deprecated node rather than a validated clinical target. Furthermore, multiple large meta-analyses, including data from the Blood Pressure Lowering Treatment Trialists' Collaboration (BPLTTC), show that NDHP-CCBs such as diltiazem are inferior to dihydropyridine CCBs (e.g., amlodipine) for primary stroke prevention. This evidence base further weakens the translational case for diltiazem in this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.08%), the target disease ontology term is formally obsolete, rendering the prediction semantically uninterpretable in its current form; this, combined with a complete absence of supporting clinical trials or literature and the known inferiority of NDHP-CCBs to DHP-CCBs for stroke prevention in the broader evidence base, means there is insufficient grounds to advance this candidate.

**To proceed, the following is needed:**

- **Ontology remapping (critical):** Re-run the TxGNN prediction against an active, non-obsolete Disease Ontology term — e.g., *Ischaemic Stroke* (DOID:3455) or *Cerebrovascular Disease* (DOID:6713) — and re-score before any further evaluation
- **Safety data retrieval:** Obtain the SAHPRA Professional Information (PI) or the current international prescribing information (e.g., FDA label) to complete the safety assessment including contraindications, warnings, and drug interactions
- **Focused literature review:** Conduct a targeted search on NDHP-CCBs and primary/secondary stroke prevention, particularly diltiazem's role in atrial fibrillation rate control as a cardioembolic stroke risk modifier
- **SAHPRA registration verification:** Confirm current South African registration status directly with SAHPRA, as diltiazem is a long-established agent available internationally in multiple formulations (immediate-release tablets, extended-release capsules, intravenous)
- **Comparator context:** If the remapped indication is pursued, benchmark against DHP-CCBs (e.g., amlodipine) which have a stronger evidence base for stroke prevention in hypertensive patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

