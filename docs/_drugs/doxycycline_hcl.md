---
layout: default
title: Doxycycline Hcl
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 0
---

# Doxycycline Hcl
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

# Doxycycline HCL: Drug Repurposing Evaluation — Insufficient Data to Generate Predictions

## One-Sentence Summary

Doxycycline HCL is a broad-spectrum tetracycline antibiotic widely used for bacterial infections, malaria prophylaxis, and inflammatory conditions.
However, the TxGNN pipeline was unable to generate any repurposing predictions for this drug candidate in the current evidence pack.
Critical data gaps — including missing mechanism of action data and absent SAHPRA registration records — prevent a meaningful repurposing assessment at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack (see data gaps) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction unavailable; no supporting studies retrieved |
| South Africa Market Status | Not found in regulatory query |
| Number of SAHPRA Registrations | 0 (not found) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN predictions were generated for this candidate. The `predicted_indications` field in the Evidence Pack is empty.

Currently, detailed mechanism of action data is not available. Based on known pharmacological literature, Doxycycline HCL is a tetracycline-class antibiotic that inhibits bacterial protein synthesis by blocking the 30S ribosomal subunit. Beyond its antimicrobial properties, doxycycline is also known to have anti-inflammatory and matrix metalloproteinase (MMP) inhibitory effects, which have historically supported its investigation in non-infectious conditions such as rosacea, periodontitis, and certain oncological contexts.

However, since the Evidence Pack contains no predicted indications and no original indications were parsed from regulatory records, no formal mechanistic repurposing analysis can be completed at this time. The pipeline must be re-run with corrected drug identifiers and data sources before a substantive evaluation is possible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## South Africa Market Information

No SAHPRA registration records were retrieved for "DOXYCYCLINE HCL" in this pipeline run.

> **Note for reviewers:** Doxycycline is known to be widely available in South Africa under multiple brand names and is included in the South African Essential Medicines List (EML). The absence of records here is most likely a data pipeline issue — the drug name query ("DOXYCYCLINE HCL") may not have matched the exact string used in the SAHPRA database. A manual SAHPRA search using the INN "doxycycline" or known brand names (e.g., Cyclodox, Vibramycin) is recommended to retrieve actual registration data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack contains no predicted indications, no parsed regulatory data, and no mechanism of action records. Two blocking-level data gaps (DG001: SAHPRA PI warnings/contraindications; DG002: mechanism of action) prevent entry into the standard safety and efficacy evaluation workflow.

**To proceed, the following is needed:**

- **Resolve DG001** — Retrieve the SAHPRA-approved Professional Information (PI) for doxycycline; parse warnings, contraindications, and pregnancy/lactation precautions.
- **Resolve DG002** — Query the DrugBank API using the correct DrugBank ID for doxycycline (DB00254) to retrieve the full mechanism of action and pharmacological category.
- **Fix drug name matching** — Re-run the regulatory query using the INN "doxycycline" (without the salt suffix "HCL") and verify against the SAHPRA product database to recover actual market status and registration count.
- **Re-run TxGNN pipeline** — Once the DrugBank ID and regulatory data are confirmed, re-run the knowledge graph and deep learning prediction steps to generate `predicted_indications`.
- **Verify EML status** — Confirm whether doxycycline appears in the current South African Essential Medicines List and at which care level, as this affects access and formulary considerations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

