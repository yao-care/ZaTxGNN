---
noindex: true
sitemap: false
layout: default
title: Brimonidine Tartrate
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Brimonidine Tartrate
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

## Brimonidine Tartrate: Evaluation Report — No Repurposing Predictions Available
{: .text-alpha }

## One-Sentence Summary

Brimonidine tartrate is an alpha-2 adrenergic agonist with established clinical use in glaucoma, ocular hypertension, and facial erythema associated with rosacea. The TxGNN model did not generate any repurposing predictions for this compound in the current pipeline run, leaving no new indication to evaluate. Two unresolved data gaps — one rated **Blocking** severity — prevent progression past the initial triage stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in evidence pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | — |
| South Africa Market Status | Marketed (valid licences: 8 of 8; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 8 (valid: 8, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned zero repurposing candidates for brimonidine tartrate in this run, and a Blocking-severity data gap (missing SAHPRA warnings and contraindications) prevents completion of even the initial safety screen. No evaluation of a new indication is possible until the pipeline is re-run with complete input data.

**To proceed, the following is needed:**

- **Resolve DrugBank ID** (DG002 prerequisite): The evidence pack records no DrugBank ID for this drug despite a successful DrugBank query (`result_count: 1`). Extract and populate the DrugBank ID from that result, then re-run the TxGNN prediction pipeline to confirm that brimonidine tartrate maps to at least one disease node in the knowledge graph.
- **Retrieve MOA data** (DG002 — High severity): Once the DrugBank ID is resolved, query the DrugBank API to obtain mechanism of action, pharmacodynamics, and drug class information. This is required for the mechanistic plausibility analysis.
- **Retrieve safety data** (DG001 — **Blocking** severity): Download and parse the SAHPRA-approved Professional Information (PI) PDF to extract warnings, contraindications, and drug interactions. This must be resolved before any safety screen can be initiated.
- **Re-run the full evidence collection pipeline**: Once a valid repurposing candidate is generated, populate clinical trial and literature evidence via the ClinicalTrials.gov, PubMed, and ICTRP collectors before repeating this evaluation.

<!-- review:begin za-lic-20261105-brimonidine_tartrate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "**Verify SAHPRA registration status**: Zero licences are currently recorded. Confirm whether registered products containing brimonidine tartrate (e.g., Alphagan®, Mirvaso®) hold current SAHPRA registrations or were withdrawn — zero entries may reflect a data retrieval gap rather than true non-registration. / **Re-run the full evidence collection pipeline**: Once a valid repurposing candidate is generated, populate clinical trial and literature evidence via the ClinicalTrials.gov, PubMed, and ICTRP collectors before repeating this evaluation." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 8 registrations for this drug, 8 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-brimonidine_tartrate-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "**Verify SAHPRA registration status**: Zero licences are currently recorded. Confirm whether registered products containing brimonidine tart" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

