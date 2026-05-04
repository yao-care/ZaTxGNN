---
layout: default
title: Amiloride Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 0
---

# Amiloride Hydrochloride
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

# Amiloride Hydrochloride: Repurposing Candidacy Evaluation (No Active Prediction Available)

## One-Sentence Summary

Amiloride Hydrochloride is a potassium-sparing diuretic, well established internationally for treating hypertension and fluid retention associated with heart failure, hepatic cirrhosis, and nephrotic syndrome. The TxGNN model returned **no predicted new indications** for this drug in the current data pack, due to an unresolved DrugBank ID and missing mechanism of action data. **A full repurposing evaluation cannot be completed until these critical data gaps are addressed.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; oedema secondary to heart failure, hepatic cirrhosis, or nephrotic syndrome *(general pharmacological knowledge — not confirmed in this data pack)* |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A |
| South Africa Market Status | Not registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Drug Background and Mechanism

Amiloride Hydrochloride belongs to the pyrazine-carbonyl guanidine class of potassium-sparing diuretics. It acts by directly blocking the epithelial sodium channel (ENaC) in the late distal convoluted tubule and collecting duct of the kidney, reducing sodium reabsorption independently of aldosterone. This mechanism preserves serum potassium and explains why amiloride is frequently combined with loop diuretics or thiazides to prevent hypokalaemia.

The drug's ENaC-blocking mechanism has attracted considerable research interest beyond cardio-renal indications. ENaC is expressed in various non-renal tissues including the lung epithelium, gastrointestinal mucosa, and certain tumour cell lines, which has prompted investigation of amiloride in cystic fibrosis (inhaled formulations to reduce airway sodium absorption), fibrotic conditions, and selected malignancies. However, the current Evidence Pack contains no formal TxGNN-generated predictions to evaluate any of these directions.

The absence of a confirmed DrugBank ID in this data pack prevented the TxGNN pipeline from completing its knowledge graph traversal and deep-learning scoring steps. This is a critical upstream data gap: without a DrugBank node anchor, neither the drug–disease graph edges nor the model embedding can be generated. This must be resolved before any formal repurposing score can be produced.

---

## Clinical Trial Evidence

No TxGNN-predicted indication is available for this drug. Consequently, no targeted clinical trial evidence can be presented at this stage.

Once the pipeline is re-run with a confirmed DrugBank ID, trial evidence should be retrieved from ClinicalTrials.gov, the Pan African Clinical Trials Registry (PACTR), and the South African National Clinical Trials Register (SANCTR).

---

## Literature Evidence

No targeted literature evidence can be presented in the absence of a predicted indication.

---

## South Africa Market Information

Amiloride Hydrochloride is **not currently registered with SAHPRA** and holds no product licences in South Africa.

> **Note for procurement and clinical teams:** Amiloride is registered in numerous other jurisdictions (United States, United Kingdom, Australia, and EU member states), typically as a fixed-dose combination with hydrochlorothiazide or furosemide. If a clinical need exists, importation under Section 21 of the Medicines and Related Substances Act (Act 101 of 1965) may be considered, subject to SAHPRA approval.

---

## Safety Considerations

No SAHPRA-approved Professional Information (PI) exists for this drug in South Africa, as it is not currently registered. The following safety profile is drawn from internationally recognised prescribing references for contextual awareness only:

- **Key Warnings:** Risk of hyperkalaemia, particularly in patients with renal impairment, diabetes mellitus, or those concurrently receiving ACE inhibitors, angiotensin receptor blockers (ARBs), or potassium supplements. Routine serum potassium and creatinine monitoring is essential.
- **Contraindications:** Existing hyperkalaemia (serum K⁺ > 5.5 mmol/L); severe renal impairment (eGFR < 30 mL/min/1.73 m²); concomitant use of other potassium-sparing diuretics or potassium supplementation (unless under close clinical supervision).

> For any formal prescribing decision in South Africa, consult the imported product's approved PI and SAHPRA requirements. Adverse drug reactions should be reported to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not generate repurposing predictions for Amiloride Hydrochloride due to a missing DrugBank ID and incomplete mechanism of action data. Without a valid prediction score or candidate indication, no evidence-based repurposing evaluation is possible at this stage.

**To proceed, the following is needed:**

1. **Resolve DrugBank ID** — Confirm the DrugBank identifier for Amiloride Hydrochloride (internationally recorded as DB00594) and re-link the drug record to enable TxGNN knowledge graph scoring.
2. **Retrieve mechanism of action data** — Query the DrugBank API for full MOA, pharmacological class, molecular targets, and pathway information.
3. **Re-run TxGNN prediction pipeline** — Once the DrugBank ID is confirmed, re-execute both the knowledge graph (KG) and deep-learning prediction steps to generate candidate indications with confidence scores.
4. **Retrieve SAHPRA-relevant safety data** — If a Section 21 application or future local registration is under consideration, obtain the international PI and map it to SAHPRA's PI format requirements.
5. **Search SANCTR and PACTR** — Once a predicted indication is generated, search the South African National Clinical Trials Register and Pan African Clinical Trials Registry for any locally relevant ongoing or completed trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

