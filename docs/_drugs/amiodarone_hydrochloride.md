---
layout: default
title: Amiodarone Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 0
---

# Amiodarone Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amiodarone Hydrochloride: Repurposing Evaluation — Prediction Data Unavailable

## One-Sentence Summary

Amiodarone hydrochloride is a well-established Class III antiarrhythmic agent used globally for the management of life-threatening ventricular arrhythmias and atrial fibrillation.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug — the prediction pipeline could not be completed due to a missing DrugBank identifier and unresolved regulatory data, representing a **blocking data gap**.
A complete repurposing evaluation cannot be produced at this time; the recommended action is to resolve upstream data issues and re-run the pipeline.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack *(see Drug Background below)* |
| Predicted New Indication | Not available — TxGNN prediction not completed |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| South Africa Market Status | Not marketed (0 SAHPRA registrations on file) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Drug Background

Although the automated pipeline did not retrieve mechanism of action or original indication data, amiodarone hydrochloride is a well-characterised agent in clinical pharmacology. This context is provided to support remediation planning.

**Established clinical indications:**
- Haemodynamically unstable ventricular tachycardia and ventricular fibrillation (acute management)
- Atrial fibrillation and flutter (rate and rhythm control)
- Paroxysmal supraventricular tachycardias (second-line)

**Mechanism of action (from clinical literature):**
Amiodarone is a Vaughan Williams Class III antiarrhythmic. Its primary action is blockade of cardiac potassium channels (I_Kr, I_Ks), prolonging the action potential duration and effective refractory period across atrial and ventricular tissue. It also exhibits Class I (sodium channel), Class II (non-competitive beta-adrenergic), and Class IV (calcium channel) properties, which accounts for both its broad antiarrhythmic efficacy and its extensive adverse-effect profile.

**Important note on market status:**
Amiodarone is included on the **WHO Model List of Essential Medicines** and is marketed as a generic product in the vast majority of countries worldwide, including many African markets. The "Not marketed / 0 SAHPRA registrations" result returned by the pipeline is almost certainly a **data retrieval failure** rather than a true reflection of market availability. Manual verification against the SAHPRA online medicines register is essential before drawing any regulatory conclusions.

---

## Safety Considerations

No drug-specific safety data was retrievable via the automated pipeline for this submission.

> Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the MedSafety online ADR reporting portal.

As a clinical reminder for evaluation teams, amiodarone carries several black-box–level risks well documented in the literature. Any future repurposing study protocol must address:

- **Thyroid toxicity** — Both hypothyroidism and hyperthyroidism (amiodarone contains ~37% iodine by weight); thyroid function must be monitored before and during treatment
- **Pulmonary toxicity** — Potentially fatal pulmonary fibrosis or pneumonitis; baseline and periodic chest X-ray and lung function testing required
- **Hepatotoxicity** — Elevated liver enzymes common; cirrhosis reported rarely; LFTs must be monitored
- **Cardiac pro-arrhythmia** — QT prolongation and risk of torsades de pointes; ECG monitoring essential
- **Drug–drug interactions** — Numerous and clinically significant, including with warfarin (INR potentiation), digoxin (toxicity), and other antiarrhythmics (additive QT effects); a formal DDI review is mandatory before any co-administration

These safety considerations must be formally populated from the SAHPRA-approved PI before this candidate proceeds to any evaluation stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN repurposing prediction pipeline could not be executed for amiodarone hydrochloride because the DrugBank identifier is missing — a blocking data gap that prevents knowledge graph traversal and deep learning scoring. With no predicted indications generated, no evidence-based repurposing evaluation can be conducted.

**To proceed, the following is needed:**

1. **Populate the DrugBank ID manually** — Amiodarone's DrugBank accession number is **DB01118**; this should be entered directly into the candidate record to unblock the pipeline.
2. **Re-run TxGNN prediction modules** — Once DB01118 is populated, re-execute both the knowledge graph (KG) and deep learning (DL) prediction workflows to generate repurposing candidates with scored indications.
3. **Verify SAHPRA registration status** — Search the SAHPRA online medicines register directly for "amiodarone" (all salt forms and brand names, e.g., Cordarone, Aratac, Amiodarone Generic); the 0-license result is likely a retrieval error.
4. **Download and parse the SAHPRA-approved Professional Information (PI)** — Required to populate warnings, contraindications, dosage forms, and approved indication text; resolves Data Gap DG001 (currently blocking safety pre-screening).
5. **Query DrugBank API for structured MOA and pharmacokinetics data** — Use DB01118 to retrieve pharmacodynamics, mechanism, absorption/distribution/metabolism/excretion, and toxicity fields; resolves Data Gap DG002.
6. **Re-submit a complete Evidence Pack** — Once steps 1–5 are completed, a full repurposing evaluation report can be generated per standard v4 format.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

