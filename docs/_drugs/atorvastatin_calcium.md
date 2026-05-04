---
layout: default
title: Atorvastatin Calcium
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Atorvastatin Calcium
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

# Atorvastatin Calcium: Repurposing Evaluation — Insufficient Evidence Pack for Full Assessment

## One-Sentence Summary

Atorvastatin calcium is a well-established HMG-CoA reductase inhibitor (statin) widely used globally for the management of hypercholesterolaemia and cardiovascular disease risk reduction.
The current Evidence Pack returned **no TxGNN-predicted repurposing indications**, and two blocking data gaps — absent SAHPRA registration records and missing mechanism of action detail — prevent a complete evaluation from proceeding.
This report documents the data gaps, summarises available context, and defines the remediation steps required before a formal repurposing assessment can be issued.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not retrieved — see data gap DG001 |
| Predicted New Indication | No predictions returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | Below L5 — no predictions generated; evaluation cannot be completed |
| South Africa Market Status | Not found in registry — likely a data retrieval failure (see note below) |
| Number of SAHPRA Registrations | 0 retrieved — atorvastatin calcium is known to be widely available in South Africa; this figure almost certainly reflects a pipeline error, not actual market absence |
| Recommended Decision | **Hold** — resolve data gaps before evaluation |

> **Note on market status:** Atorvastatin calcium (e.g., Lipitor® and numerous generics) is registered by SAHPRA and widely dispensed in South African public and private healthcare. A result of zero registrations strongly indicates a data retrieval or matching failure rather than true absence from the South African market.

---

## Safety Considerations

All safety fields in the current Evidence Pack are unpopulated due to data gap **DG001** (SAHPRA Professional Information not yet retrieved).

Please refer to the **SAHPRA-approved Professional Information (PI)** for full safety information, including warnings, contraindications, and drug interactions. Report adverse drug reactions to **SAHPRA** via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for atorvastatin calcium is incomplete: TxGNN returned no repurposing predictions, SAHPRA registration data was not retrieved, and both the MOA and PI safety data are missing. Without at minimum a valid `predicted_indications` entry, no evidence-based repurposing evaluation can be completed.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Retrieve the SAHPRA-approved Professional Information (PI) for atorvastatin calcium. Download PI PDFs from the SAHPRA website or the relevant manufacturer's package insert and parse warnings, contraindications, and approved indications. This must be resolved before safety screening (Stage 1) can proceed.

- **[DG002 — High]** Populate the DrugBank ID and mechanism of action fields. The DrugBank query log reports a successful result (`result_count: 1`) but `drugbank_id` was not captured — inspect the response payload for field-mapping issues. The expected DrugBank ID is **DB01076**. Once resolved, re-run the MOA extraction to enable mechanistic plausibility analysis.

- **[Pipeline — High]** Investigate why `predicted_indications` is an empty array. Confirm that atorvastatin calcium is present in the TxGNN knowledge graph (`data/node.csv`), that the DrugBank ID is correctly passed to `run_kg_prediction.py`, and that the prediction threshold has not been set too conservatively. Re-run the KG and DL prediction steps after the DrugBank ID is confirmed.

- **[Regulatory — Medium]** Re-run the SAHPRA registration query using the confirmed INN "atorvastatin calcium" and common synonyms ("atorvastatin"). Cross-check against the South African Essential Medicines List (EML) — atorvastatin is included on the adult hospital level EML, which is relevant for access and formulary discussions.

- **[Evidence — Post-remediation]** Once predictions are available, trigger the ClinicalTrials.gov and PubMed collectors for each predicted indication, and include SANCTR and PACTR searches for any Africa-relevant trial evidence.

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any change in prescribing practice. YMYL disclaimer: this content is intended for qualified healthcare professionals and researchers.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

