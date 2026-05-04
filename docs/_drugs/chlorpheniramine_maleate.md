---
layout: default
title: Chlorpheniramine Maleate
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 0
---

# Chlorpheniramine Maleate
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

# Chlorpheniramine Maleate: From Allergic Conditions — Repurposing Evaluation Pending

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
| South Africa Market Status | Not registered (per current data pack — see note below) |
| Number of SAHPRA Registrations | 0 (per current data pack — likely a data completeness issue) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Integrity Note:** Chlorpheniramine maleate is a decades-old, widely available molecule present in numerous over-the-counter and prescription products across Africa (including well-known brands such as *Allergex* and *Piriton* in South Africa). A result of zero SAHPRA registrations almost certainly reflects an input data gap rather than a genuine absence from the South African market. SAHPRA records must be independently verified before this field is relied upon.

---

## Why is This Prediction Reasonable?

No repurposing prediction is currently available in this Evidence Pack. The TxGNN pipeline did not produce candidate indications, which is most likely caused by a missing DrugBank ID — without this identifier, the model cannot map the drug to its node in the knowledge graph.

From established pharmacological literature, chlorpheniramine maleate is a **competitive, reversible H1-receptor antagonist**. It reduces the effect of endogenous histamine on capillary permeability, smooth muscle, and sensory nerve endings, thereby alleviating the symptoms of immediate (Type I) hypersensitivity responses. Its first-generation status also confers sedative properties via central H1 blockade and anticholinergic activity, which have historically been explored in contexts such as motion sickness and as a sleep aid adjunct.

Detailed mechanism of action data was not provided in the Evidence Pack (recorded as a High-severity data gap). Once DrugBank ID mapping is resolved and MOA data retrieved, the TxGNN model will be able to assess potential repurposing candidates — for example, emerging literature has explored antihistamines in contexts such as COVID-19 symptom management, chronic pruritus of varied aetiology, and as chemosensitisers in oncology settings. However, none of these directions can be formally evaluated without a completed prediction run.

---

## South Africa Market Information

No SAHPRA registration records are present in the current Evidence Pack.

As noted above, this is strongly suspected to be a data completeness issue. The following table is provided as a placeholder pending data retrieval:

| Registration Number | Product Name | Dosage Form | Approved Indication |
|--------------------|-------------|-------------|-------------------|
| *Pending SAHPRA verification* | — | — | — |

**Recommended action:** Query the SAHPRA online medicines register (`https://www.sahpra.org.za`) using the search term "chlorpheniramine" to retrieve all active and historical registration records.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

