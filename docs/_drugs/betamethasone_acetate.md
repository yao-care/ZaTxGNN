---
noindex: true
sitemap: false
layout: default
title: Betamethasone Acetate
parent: Model Prediction Only (L5)
nav_order: 68
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Betamethasone Acetate
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

## BETAMETHASONE ACETATE: Drug Repurposing Candidate Assessment
{: .text-alpha }

---

## One-Sentence Summary

Betamethasone Acetate is a synthetic corticosteroid in the glucocorticoid class, recognised for its anti-inflammatory and immunosuppressive properties.
However, the current Evidence Pack contains **no TxGNN-predicted new indications** and has critical data gaps in mechanism of action, original approved indications, and safety information, meaning a full repurposing evaluation **cannot be completed at this stage**.
This report documents current findings and outlines the remediation steps required before a Go/Hold decision can be made.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — TxGNN output absent |
| South Africa Market Status | Marketed (valid licences: 57 of 65; 10 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 65 (valid: 57, of which 10 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predicted indications for Betamethasone Acetate, and two blocking or high-severity data gaps prevent the safety and mechanistic analyses required for a repurposing evaluation.

<!-- review:begin za-lic-20261105-betamethasone_acetate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The TxGNN pipeline returned no predicted indications for Betamethasone Acetate, and two blocking or high-severity data gaps prevent the safety and mechanistic analyses required for a repurposing evaluation. No SAHPRA registrations were located for this specific salt form, further limiting the regulatory basis for any recommendation." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 65 registrations for this drug, 57 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-betamethasone_acetate-1 -->

**To proceed, the following is needed:**

- **[Blocking — DG001]** Obtain the SAHPRA Professional Information (PI) to extract approved warnings and contraindications. *Suggested method: download the PI PDF from the SAHPRA website and parse relevant sections.*
- **[High — DG002]** Retrieve the DrugBank entry for Betamethasone Acetate to confirm the DrugBank ID and mechanism of action. *Suggested method: query the DrugBank API using the INN.*
- **[Required for prediction]** Re-run the TxGNN prediction pipeline once the DrugBank ID is confirmed; the current Evidence Pack shows an empty `predicted_indications` array, which indicates the drug could not be matched to a knowledge graph node.
- **[Optional]** Confirm whether Betamethasone Acetate or a related betamethasone formulation appears on the South African Essential Medicines List (EML) to assess procurement and access feasibility.

<!-- review:begin za-lic-20261105-betamethasone_acetate-2 -->

> **Review correction (2026-11-05)**: Originally stated: "**[Regulatory]** Verify whether any betamethasone-containing products (free acid, sodium phosphate, or dipropionate formulations) are registered with SAHPRA, as the zero-license result may reflect a salt-form mismatch rather than a genuine absence from the South African market. / **[Optional]** Confirm whether Betamethasone Acetate or a related betamethasone formulation appears on the South African Essential Medicines List (EML) to assess procurement and access feasibility." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 65 registrations for this drug, 57 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-betamethasone_acetate-2 -->

<!-- review:begin za-lic-20261106-betamethasone_acetate-3 -->

> **Review correction (2026-11-06)**: Originally stated: "**[Blocking — DG001]** Obtain the SAHPRA Professional Information (PI) or the TFDA package insert to extract approved warnings and contraindications." Removed: leftover template text about Taiwan's TFDA, which does not apply to this South African page. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261106-betamethasone_acetate-3 -->

> **Disclaimer:** This report is generated for research purposes only and does not constitute medical advice. Any drug repurposing candidate identified by TxGNN requires formal clinical validation before therapeutic application. All content should be reviewed against SAHPRA-approved labelling.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "No SAHPRA registrations were located for this specific salt form, further limiting the regulatory basis for any recommendation" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "**[Regulatory]** Verify whether any betamethasone-containing products (free acid, sodium phosphate, or dipropionate formulations) are regist" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-06 | Removed: "or the TFDA package insert" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

