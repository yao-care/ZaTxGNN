---
noindex: true
sitemap: false
layout: default
title: Arginine Hydrochloride
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Arginine Hydrochloride
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

## Arginine Hydrochloride: Insufficient Data for Drug Repurposing Assessment
{: .text-alpha }

---

## One-Sentence Summary

Arginine hydrochloride is an amino acid salt with established clinical roles in treating metabolic alkalosis and as a diagnostic provocative agent in growth hormone stimulation testing.
No TxGNN repurposing predictions were generated for this drug in the current analysis cycle.
A complete repurposing evaluation cannot be conducted until critical data gaps — including DrugBank mapping, mechanism of action, and safety documentation — are resolved.

<!-- review:begin za-lic-20261105-arginine_hydrochloride-1 -->

> **Review correction (2026-11-05)**: Originally stated: "No TxGNN repurposing predictions were generated for this drug in the current analysis cycle, and the drug holds no SAHPRA registration in South Africa. / A complete repurposing evaluation cannot be conducted until critical data gaps — including DrugBank mapping, mechanism of action, and safety documentation — are resolved." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 54 registrations for this drug, 35 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-arginine_hydrochloride-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current dataset |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — no predictions or supporting studies available |
| South Africa Market Status | Marketed (valid licences: 35 of 54; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 54 (valid: 35, of which 5 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing predictions were generated for Arginine Hydrochloride in this analysis cycle, so a mechanism-based rationale for a specific new indication cannot currently be provided.

Arginine hydrochloride is the ionised salt form of L-arginine, a conditionally essential amino acid with well-characterised roles in protein biosynthesis, the urea cycle, nitric oxide (NO) production via nitric oxide synthase (NOS), and immune regulation. Its established clinical applications include correction of hypochloraemic metabolic alkalosis and pharmacological provocation of pituitary growth hormone secretion. These broad physiological roles — particularly the NO pathway — have generated investigational interest across cardiovascular disease, wound healing, immune dysfunction, and male sexual health, though no formal TxGNN prediction has been computed for this candidate.

The absence of predictions most likely reflects a failure to map the drug name "ARGININE HYDROCHLORIDE" to a confirmed DrugBank identifier in the current pipeline run. Resolving this mapping is the critical first step before any repurposing evaluation can proceed.

---

## South Africa Market Information

It does not appear on the South African Essential Medicines List (EML).

<!-- review:begin za-lic-20261105-arginine_hydrochloride-2 -->

> **Review correction (2026-11-05)**: Originally stated: "Arginine hydrochloride is **not currently registered with SAHPRA** and carries no approved South African product licences on record. It does not appear on the South African Essential Medicines List (EML). Any clinical use in South Africa would require a **Section 21 Unregistered Medicine Authorisation** from SAHPRA before procurement or administration." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 54 registrations for this drug, 35 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-arginine_hydrochloride-2 -->

---

## Safety Considerations

No SAHPRA-sourced safety data, contraindications, or drug-drug interaction records are available in the current dataset. Please refer to the manufacturer's Professional Information (PI) and any relevant international regulatory documents (EMA, FDA) for safety guidance. Report all suspected adverse drug reactions to SAHPRA via the MedSafety online portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline did not generate repurposing predictions for this drug, and both the DrugBank identifier and safety documentation are absent — making a meaningful evidence-based evaluation impossible at this stage.

**To proceed, the following is needed:**

- **Resolve DrugBank mapping**: Confirm whether Arginine Hydrochloride maps to DrugBank DB00148 (L-Arginine) or a distinct salt entry, and rerun the TxGNN prediction pipeline with the correct identifier
- **Obtain safety documentation**: Download and parse the manufacturer's PI or SPC to extract warnings, contraindications, and drug interactions (identified as a blocking data gap in the current pack)
- **Retrieve MOA data**: Query the DrugBank API or PharmGKB for mechanism of action details to support future mechanism-relatedness analysis
- **Establish original registered indications**: Confirm approved indications from SAHPRA, EMA, or FDA sources to populate the repurposing baseline
- **Assess regulatory pathway**: If clinical repurposing use is being considered, initiate a Section 21 application with SAHPRA and identify any South African or regional clinical trial activity via the Pan African Clinical Trials Registry (PACTR) at [www.pactr.org](https://www.pactr.org)

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content must be interpreted in conjunction with SAHPRA-approved prescribing information.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "and the drug holds no SAHPRA registration in South Africa" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "Arginine hydrochloride is **not currently registered with SAHPRA** and carries no approved South African product licences on record. Any cli" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

