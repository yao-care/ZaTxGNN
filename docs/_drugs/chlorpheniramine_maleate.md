---
noindex: true
sitemap: false
layout: default
title: Chlorpheniramine Maleate
parent: Model Prediction Only (L5)
nav_order: 116
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Chlorpheniramine Maleate
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

## Chlorpheniramine Maleate: From Allergic Conditions — Repurposing Evaluation Pending
{: .text-alpha }

## One-Sentence Summary

Chlorpheniramine maleate is a well-established first-generation H1 antihistamine, classically used for the symptomatic relief of allergic rhinitis, urticaria, and related hypersensitivity reactions.
The current Evidence Pack contains **no TxGNN repurposing predictions** for this drug, as critical input data — including the DrugBank ID mapping, mechanism of action, SAHPRA registration records, and safety information — are absent or unresolved.
This report documents the current data status and defines the minimum requirements before a full repurposing evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, urticaria, hypersensitivity reactions (known from pharmacological literature; no formal indication text present in current data pack) |
| Predicted New Indication | Not available — TxGNN generated no candidate predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — No predictions generated; evaluation cannot be initiated |
| South Africa Market Status | Marketed (valid licences: 64 of 98; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 98 (valid: 64, of which 5 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Integrity Note:** Chlorpheniramine maleate is a decades-old, widely available molecule present in numerous over-the-counter and prescription products across Africa (including well-known brands such as *Allergex* and *Piriton* in South Africa). SAHPRA records must be independently verified before this field is relied upon.

<!-- review:begin za-lic-20261105-chlorpheniramine_maleate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "A result of zero SAHPRA registrations almost certainly reflects an input data gap rather than a genuine absence from the South African market. SAHPRA records must be independently verified before this field is relied upon." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 98 registrations for this drug, 64 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-chlorpheniramine_maleate-1 -->

---

## Why is This Prediction Reasonable?

No repurposing prediction is currently available in this Evidence Pack. The TxGNN pipeline did not produce candidate indications, which is most likely caused by a missing DrugBank ID — without this identifier, the model cannot map the drug to its node in the knowledge graph.

From established pharmacological literature, chlorpheniramine maleate is a **competitive, reversible H1-receptor antagonist**. It reduces the effect of endogenous histamine on capillary permeability, smooth muscle, and sensory nerve endings, thereby alleviating the symptoms of immediate (Type I) hypersensitivity responses. Its first-generation status also confers sedative properties via central H1 blockade and anticholinergic activity, which have historically been explored in contexts such as motion sickness and as a sleep aid adjunct.

Detailed mechanism of action data was not provided in the Evidence Pack (recorded as a High-severity data gap). Once DrugBank ID mapping is resolved and MOA data retrieved, the TxGNN model will be able to assess potential repurposing candidates — for example, emerging literature has explored antihistamines in contexts such as COVID-19 symptom management, chronic pruritus of varied aetiology, and as chemosensitisers in oncology settings. However, none of these directions can be formally evaluated without a completed prediction run.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/5.7.1/0166 | Rhineton | tablet | Valid |
| C0668 | Allergex | tablet | Valid |
| 27/10.1/0536 | Trifen expect paediatric | syrup | Valid |
| 27/10.1/0553 | Flusin dm | syrup | Valid |
| 27/5.8/0123 | Degoran Cold And Flu Hot Medicated Drink | sachet | Valid (status not confirmed by SAHPRA) |

Showing 5 of 98 registrations (valid registrations first).

<!-- licenses:end -->

**Recommended action:** Query the SAHPRA online medicines register (`https://www.sahpra.org.za`) using the search term "chlorpheniramine" to retrieve all active and historical registration records.

<!-- review:begin za-lic-20261105-chlorpheniramine_maleate-2 -->

> **Review correction (2026-11-05)**: Originally stated: "No SAHPRA registration records are present in the current Evidence Pack." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 98 registrations for this drug, 64 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-chlorpheniramine_maleate-2 -->

<!-- review:begin za-lic-20261105-chlorpheniramine_maleate-3 -->

> **Review correction (2026-11-05)**: Originally stated: "As noted above, this is strongly suspected to be a data completeness issue. The following table is provided as a placeholder pending data retrieval:" Removed: it continued a sentence that was removed for contradicting the SAHPRA registration data as of 2026-11-05, and would not make sense on its own. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-chlorpheniramine_maleate-3 -->

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via [MedSafety Online](https://www.sahpra.org.za/pharmacovigilance/).

> The Evidence Pack records a **Blocking-severity** data gap (DG001) for TFDA/SAHPRA PI warnings and contraindications. Until the PI is retrieved and parsed, no formal safety profile can be presented. Key areas to review when the PI is available will include: anticholinergic effects, sedation and driving warnings, use in elderly patients (Beers Criteria relevance), and paediatric dosing restrictions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for chlorpheniramine maleate is critically incomplete — no TxGNN predictions were generated due to missing DrugBank ID mapping, SAHPRA registration data appears to be absent due to a pipeline data gap, and both mechanism of action and safety information are unresolved. A meaningful repurposing evaluation cannot be conducted until the foundational data elements are in place.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve and parse the SAHPRA-approved Professional Information (PI) to obtain approved indications, warnings, and contraindications
- **[High — DG002]** Resolve DrugBank ID for chlorpheniramine maleate (suggested: `DB01114`) and retrieve full MOA data via the DrugBank API
- **[Required]** Re-run the TxGNN prediction pipeline with a valid DrugBank ID to generate repurposing candidate indications
- **[Required]** Verify SAHPRA registration records independently against the SAHPRA medicines register and update `total_licenses` and `licenses` fields accordingly
- **[Optional]** Retrieve drug–drug interaction data from DrugBank or the South African Medicines Formulary (SAMF) once the DrugBank ID is confirmed
- Once the above gaps are resolved, resubmit the Evidence Pack for a full L1–L4 evaluation report

---

*This report is intended for research purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Adverse drug reactions should be reported to SAHPRA.*

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "A result of zero SAHPRA registrations almost certainly reflects an input data gap rather than a genuine absence from the South African marke" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "No SAHPRA registration records are present in the current Evidence Pack" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "As noted above, this is strongly suspected to be a data completeness issue. The following table is provided as a placeholder pending data re" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

