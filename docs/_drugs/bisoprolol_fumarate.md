---
noindex: true
sitemap: false
layout: default
title: Bisoprolol Fumarate
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Bisoprolol Fumarate
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

## Bisoprolol Fumarate: Repurposing Evaluation — No TxGNN Prediction Available
{: .text-alpha }

## One-Sentence Summary

Bisoprolol Fumarate is a well-established cardioselective beta-1 adrenergic blocker, widely used internationally for hypertension, chronic heart failure, and angina pectoris. **No TxGNN repurposing predictions were generated for this drug** in the current evidence pack, most likely because the DrugBank ID could not be resolved, which prevented the prediction pipeline from running. A full repurposing evaluation cannot be completed until the critical data gaps identified below are addressed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — prediction pipeline did not produce output |
| South Africa Market Status | Marketed (valid licences: 86 of 93; 3 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 93 (valid: 86, of which 3 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Quality Notice:** Bisoprolol Fumarate is a globally available cardiovascular medicine. Independent verification against the [SAHPRA Online Medicine Register](https://www.sahpra.org.za/medicines/) is strongly recommended before drawing any regulatory conclusions.

<!-- review:begin za-lic-20261105-bisoprolol_fumarate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The absence of SAHPRA registrations and a null DrugBank ID are likely indicators of upstream data mapping failures rather than true absence from the South African market. Independent verification against the [SAHPRA Online Medicine Register](https://www.sahpra.org.za/medicines/) is strongly recommended before drawing any regulatory conclusions." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 93 registrations for this drug, 86 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-bisoprolol_fumarate-1 -->

<!-- review:begin za-lic-20261105-bisoprolol_fumarate-2 -->

> **Review correction (2026-11-05)**: Originally stated: "No SAHPRA-registered products were identified for Bisoprolol Fumarate in the current evidence pack." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 93 registrations for this drug, 86 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-bisoprolol_fumarate-2 -->

<!-- review:begin za-lic-20261105-bisoprolol_fumarate-3 -->

> **Review correction (2026-11-05)**: Originally stated: "No products are listed because the SAHPRA data query returned zero registrations. This should be treated as a data gap pending manual verification, not as confirmation that the drug is unregistered in South Africa." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 93 registrations for this drug, 86 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-bisoprolol_fumarate-3 -->

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/6.1/0457 | Cardicor | tablet | Valid |
| 36/6.1/0458 | Cardicor | tablet | Valid |
| 36/6.1/0459 | Cardicor | tablet | Valid |
| 37/5.2/0010 | Adco-bisocor | tablet | Valid |
| 37/5.2/0011 | Adco-bisocor | tablet | Valid |

Showing 5 of 93 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline produced no output for this drug because the DrugBank ID could not be resolved. Without a prediction, there is no repurposing candidate to evaluate, and all downstream evidence (clinical trials, literature, mechanism of action analysis) is absent. The evidence pack is insufficient to support any repurposing recommendation at this stage.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping** — Query the DrugBank API using the INN "bisoprolol fumarate" to retrieve the correct DrugBank accession number (expected: DB00612), then re-run the TxGNN prediction pipeline
- **Retrieve Mechanism of Action data** — Once DrugBank ID is confirmed, extract pharmacology and MOA data (beta-1 adrenoceptor selective antagonist; reduces heart rate, myocardial contractility, and blood pressure)
- **Retrieve original approved indications** — Pull indication text from DrugBank and cross-reference with the SAHPRA PI document
- **Verify SAHPRA registration status** — Manually search the SAHPRA online register for bisoprolol-containing products (known brands include Concor®, Bisocor®, Cardicor®) and record registration numbers and approved indications
- **Download and parse the SAHPRA-approved PI** — Extract key warnings, contraindications, and drug interaction data to complete the safety profile (currently blocking the S1 safety evaluation, severity: Blocking per DG001)
- **Re-run evidence collection** — Once a TxGNN prediction is available, run ClinicalTrials.gov, PubMed, and ICTRP collectors against the top-ranked predicted indication to populate the clinical trial and literature evidence tables

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. This report was prepared under the TxGNN Drug Repurposing Research Programme. Data cut-off: 4 April 2026.*

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The absence of SAHPRA registrations and a null DrugBank ID are likely indicators of upstream data mapping failures rather than true absence " | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "No SAHPRA-registered products were identified for Bisoprolol Fumarate in the current evidence pack" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "No products are listed because the SAHPRA data query returned zero registrations. This should be treated as a data gap pending manual verifi" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

