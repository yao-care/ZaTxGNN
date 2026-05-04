---
layout: default
title: Hydrochlorothiazide
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 0
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: Evaluation Incomplete — No TxGNN Repurposing Predictions Available

---

## One-Sentence Summary

Hydrochlorothiazide is a long-established thiazide diuretic used primarily for hypertension and oedema. This Evidence Pack (v4, data cutoff 2026-04-04) contains **no TxGNN-predicted new indications** — the predictions array is empty and two critical data gaps (regulatory PI and mechanism of action) remain unresolved. A full repurposing evaluation **cannot proceed** until these gaps are remediated and the prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; oedema (heart failure, hepatic cirrhosis, renal impairment) — *based on established pharmacological knowledge; no SAHPRA records were retrieved in this pack* |
| Predicted New Indication | None generated in this Evidence Pack |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions to evaluate |
| South Africa Market Status | Not Marketed *(per Evidence Pack — see data quality note below)* |
| Number of SAHPRA Registrations | 0 *(per Evidence Pack — likely a data retrieval gap; see note)* |
| Recommended Decision | **Hold** |

> **⚠️ Data Quality Note:** Hydrochlorothiazide is a well-established generic listed on South Africa's Essential Medicines List (EML) for primary care and present in numerous combination antihypertensive products. A result of zero SAHPRA registrations almost certainly reflects a data retrieval failure rather than true market absence. **Direct verification via the [SAHPRA online register](https://www.sahpra.org.za/find-a-medicine/) is required before this figure is acted upon.**

---

## Why is This Prediction Reasonable?

No TxGNN predictions were generated for hydrochlorothiazide in this Evidence Pack. Accordingly, no repurposing hypothesis can be formally evaluated at this stage.

Mechanism of action data is flagged as a high-severity data gap (DG002). From established pharmacology, hydrochlorothiazide inhibits the sodium-chloride cotransporter (NCC / SLC12A3) in the distal convoluted tubule of the kidney, increasing urinary excretion of sodium, chloride, and water, which reduces plasma volume and lowers blood pressure. Its calcium-sparing effect in the tubule is also clinically recognised and underpins its off-label use in nephrolithiasis prevention.

Once the DrugBank API is queried to populate the formal MOA entry and the TxGNN pipeline is re-run with complete inputs, the model will be positioned to identify mechanistic links to candidate new indications — potentially including nephrogenic diabetes insipidus, calcium kidney stone prevention, or osteoporosis — that could be formally assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no predicted indication is available to search against.

---

## Literature Evidence

Currently no related literature available — no predicted indication is available to search against.

---

## South Africa Market Information

No SAHPRA registration records were retrieved for hydrochlorothiazide in this Evidence Pack.

**Action required:** Verify directly at the [SAHPRA online register](https://www.sahpra.org.za/find-a-medicine/). Hydrochlorothiazide appears on South Africa's EML (Standard Treatment Guidelines, Primary Care level) and is commercially available in single-ingredient and fixed-dose combination tablets (e.g., with amiloride, with ACE inhibitors). The zero-registration result likely reflects a data collection limitation and should be corrected before any formulary or access assessment is made.

---

## Safety Considerations

All safety fields — key warnings, contraindications, and drug interactions — returned as data gaps in this Evidence Pack. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

For orientation purposes, the following reflects well-characterised safety information from the published literature *(not sourced from the Evidence Pack; formal safety screening requires resolution of DG001)*:

- **Electrolyte disturbances:** Hypokalaemia, hyponatraemia, and hypomagnesaemia are dose-dependent risks requiring routine monitoring, particularly in patients on digoxin or antiarrhythmics.
- **Metabolic effects:** Hyperuricaemia (gout precipitation), impaired glucose tolerance, and dyslipidaemia have been reported with long-term use.
- **Photosensitivity / Skin cancer signal:** The European Medicines Agency (2019) identified an association between cumulative hydrochlorothiazide exposure and non-melanoma skin cancer (lip cancer, squamous cell carcinoma). Patients should be advised on sun protection.
- **Known contraindications:** Anuria; known hypersensitivity to sulfonamide-derived compounds.
- **Key interactions:** Lithium (reduced renal clearance, increased toxicity); NSAIDs (attenuated diuretic and antihypertensive effect); insulin and oral hypoglycaemics (impaired glucose control).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for hydrochlorothiazide is critically incomplete — no TxGNN repurposing predictions were generated, regulatory safety data and MOA data are both flagged as unresolved gaps, and SAHPRA market information could not be verified. A meaningful repurposing evaluation requires all three inputs before it can proceed.

**To proceed, the following is needed:**

1. **Resolve DG001 (Blocking — Safety PI):** Download and parse the SAHPRA-approved Professional Information to populate warnings and contraindications, enabling the S1 safety screening step.
2. **Resolve DG002 (High — MOA):** Query the DrugBank API for DB00999 to retrieve the formal mechanism of action entry for use in mechanistic plausibility analysis.
3. **Correct SAHPRA registration data:** Manually verify hydrochlorothiazide listings in the SAHPRA online register and update `total_licenses` and `licenses` fields accordingly.
4. **Re-run the TxGNN prediction pipeline:** With complete regulatory and MOA inputs, re-execute both the knowledge graph (KG) and deep learning (DL) prediction models to generate `predicted_indications`.
5. **Re-issue the Evidence Pack:** Once all Blocking and High-severity gaps are resolved, generate a new version (v5) and submit for a fresh evaluation.

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

