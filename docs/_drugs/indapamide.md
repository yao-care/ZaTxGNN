---
noindex: true
sitemap: false
layout: default
title: Indapamide
parent: Model Prediction Only (L5)
nav_order: 262
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Indapamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Indapamide: Drug Repurposing Evaluation — Prediction Data Unavailable
{: .text-alpha }

---

## One-Sentence Summary

Indapamide (DB00808) is a thiazide-like sulfonamide diuretic widely used internationally for hypertension and oedema associated with heart failure.
**No TxGNN repurposing predictions are available in this Evidence Pack**, as the predicted indications list is empty — this evaluation cannot proceed to a standard repurposing assessment.
The data collection pipeline retrieved only DrugBank records; South African regulatory, mechanism of action, and safety data were not successfully captured, leaving critical gaps across all evaluation domains.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; oedema (general pharmacological knowledge — not confirmed in Evidence Pack) |
| Predicted New Indication | Not available — TxGNN returned no candidates |
| TxGNN Prediction Score | Not available |
| Evidence Level | N/A |
| South Africa Market Status | Marketed (valid licences: 58 of 65; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 65 (valid: 58, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Reliability Note:** The Evidence Pack was built from DrugBank data only (`inputs_received: ["drugbank"]`). Indapamide is a well-established antihypertensive on the WHO Essential Medicines List and is expected to hold SAHPRA registration. Independent SAHPRA database verification is required before any regulatory conclusions are drawn.

<!-- review:begin za-lic-20261105-indapamide-1 -->

> **Review correction (2026-11-05)**: Originally stated: "SAHPRA registration data was not collected. Indapamide is a well-established antihypertensive on the WHO Essential Medicines List and is expected to hold SAHPRA registration — the 0-registration result very likely reflects a collection gap rather than true absence from the South African market. Independent SAHPRA database verification is required before any regulatory conclusions are drawn." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 65 registrations for this drug, 58 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-indapamide-1 -->

---

## Why This Assessment Cannot Be Completed

Two blocking data gaps prevent a standard repurposing evaluation:

**1. No TxGNN repurposing predictions were generated.**
The `predicted_indications` array in the Evidence Pack is empty. TxGNN predictions require successful mapping of the drug to the knowledge graph via DrugBank ID and disease vocabulary. Without at least one predicted indication, there is no repurposing candidate to evaluate, no evidence to assess, and no mechanism-to-indication argument to construct.

**2. Mechanism of action data is absent.**
The `original_moa` field is flagged as a data gap. For a repurposing evaluation, the mechanism of action is the analytical foundation: it explains *why* a drug approved for one condition might work in another. Without this, even if a prediction were available, the mechanistic rationale section could not be completed with confidence.

Until these two gaps are resolved, this report serves only as a **data readiness assessment**, not a full repurposing evaluation.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA at [www.sahpra.org.za](https://www.sahpra.org.za).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate cannot be evaluated for drug repurposing potential because no TxGNN predictions were generated and all drug-level data fields (MOA, safety warnings, contraindications) are unpopulated. There is no evidence base to assess, no mechanistic argument to make, and no regulatory foundation to work from.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Obtain the SAHPRA-approved Professional Information (PI) for Indapamide; extract approved indications, warnings, and contraindications from the PDF document
- **[High — DG002]** Query the DrugBank API for Indapamide's mechanism of action (`DB00808`) and populate `original_moa`
- **[Blocking]** Re-run the TxGNN prediction pipeline with Indapamide's DrugBank ID to generate `predicted_indications`; confirm that the drug node exists in the knowledge graph (`data/node.csv`) and that disease vocabulary mapping is functioning
- **[Medium]** Check whether Indapamide appears on the South African Essential Medicines List (EML) and the Standard Treatment Guidelines (STG), as this would be directly relevant to any repurposing access pathway
- **[Medium]** Collect DDI data from DrugBank or a South African formulary source once the PI is available

<!-- review:begin za-lic-20261105-indapamide-2 -->

> **Review correction (2026-11-05)**: Originally stated: "**[High]** Independently verify SAHPRA registration status through the SAHPRA online register ([https://www.sahpra.org.za/find-a-medicine/](https://www.sahpra.org.za/find-a-medicine/)) to resolve the 0-registration anomaly / **[Medium]** Check whether Indapamide appears on the South African Essential Medicines List (EML) and the Standard Treatment Guidelines (STG), as this would be directly relevant to any repurposing access pathway" Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 65 registrations for this drug, 58 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-indapamide-2 -->

Once the above data is retrieved and TxGNN predictions are generated, a full repurposing evaluation report should be regenerated using Evidence Pack v5 format.

---

> *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. All adverse drug reactions should be reported to SAHPRA.*

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "SAHPRA registration data was not collected. — the 0-registration result very likely reflects a collection gap rather than true absence from " | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "**[High]** Independently verify SAHPRA registration status through the SAHPRA online register ([https://www.sahpra.org.za/find-a-medicine/](" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

