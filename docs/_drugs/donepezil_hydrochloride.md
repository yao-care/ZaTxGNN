---
noindex: true
sitemap: false
layout: default
title: Donepezil Hydrochloride
parent: Model Prediction Only (L5)
nav_order: 197
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Donepezil Hydrochloride
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

## Donepezil Hydrochloride: Evidence Pack Incomplete — Awaiting TxGNN Predictions
{: .text-alpha }

---

## One-Sentence Summary

Donepezil hydrochloride is a reversible acetylcholinesterase inhibitor internationally established for Alzheimer's disease and related dementias.
This Evidence Pack was generated with critical data gaps — the TxGNN pipeline has **not returned any predicted new indications**, and SAHPRA regulatory and safety records are absent.
**No repurposing recommendation can be issued at this time; the decision is Hold pending data resolution.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Model prediction not yet completed |
| South Africa Market Status | Marketed (valid licences: 37 of 42; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 42 (valid: 37, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | **Hold** |

---

## Background on This Drug

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on published pharmacological knowledge, donepezil hydrochloride is a **reversible, selective acetylcholinesterase (AChE) inhibitor**. By preventing the enzymatic breakdown of acetylcholine at cholinergic synapses in the central nervous system, it sustains and amplifies cholinergic neurotransmission in regions critical to memory and cognition — most notably the hippocampus and cerebral cortex.

Donepezil is internationally registered and widely used for **mild, moderate, and severe Alzheimer's disease**, as well as for dementia associated with Parkinson's disease. It does not carry an antineoplastic mechanism.

Once TxGNN predictions are available, any predicted new indication should be evaluated against this cholinergic mechanism. Candidate areas likely to show mechanistic plausibility include other neurodegenerative conditions, neuropsychiatric disorders, or conditions involving impaired cholinergic signalling.

> **Note:** The DrugBank query for this drug returned 1 result (query date 2026-03-26, status: success). That data has not been incorporated into this Evidence Pack. Retrieving DrugBank MOA, categories, and safety data should be the first remediation step.

---

## South Africa Market Information

> Donepezil is registered and in active clinical use in many other jurisdictions, including the United States (FDA), European Union (EMA), and United Kingdom (MHRA), for Alzheimer's disease.

<!-- review:begin za-lic-20261105-donepezil_hydrochloride-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Donepezil hydrochloride is currently **not registered with SAHPRA** and holds no marketing authorisation in South Africa. No registration records are available." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The SAHPRA data list 42 registrations for this drug, 37 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-donepezil_hydrochloride-1 -->

<!-- review:begin za-lic-20261105-donepezil_hydrochloride-2 -->

> **Review correction (2026-11-05)**: Originally stated: "> Donepezil is registered and in active clinical use in many other jurisdictions, including the United States (FDA), European Union (EMA), and United Kingdom (MHRA), for Alzheimer's disease. The absence of SAHPRA registration reflects the local regulatory status only." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 42 registrations for this drug, 37 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-donepezil_hydrochloride-2 -->

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> Key warnings and contraindications data were flagged as a **Blocking data gap (DG001)** in this Evidence Pack. No safety evaluation can proceed until the PI or equivalent source is obtained and reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is materially incomplete — there are no TxGNN-predicted indications, and no verified safety information.

<!-- review:begin za-lic-20261105-donepezil_hydrochloride-3 -->

> **Review correction (2026-11-05)**: Originally stated: "**Rationale:** / This Evidence Pack is materially incomplete — there are no TxGNN-predicted indications, no SAHPRA registration data, and no verified safety information. A repurposing recommendation cannot responsibly be made in the absence of these foundational inputs." Removed: it continued a sentence that was removed for contradicting the SAHPRA registration data as of 2026-11-05, and would not make sense on its own. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-donepezil_hydrochloride-3 -->

**To proceed, the following is needed:**

1. **Run TxGNN prediction pipeline** for Donepezil Hydrochloride to generate predicted new indications and evidence links
2. **Incorporate the DrugBank record** already retrieved (1 result confirmed) — extract MOA, drug categories, toxicity, and DDI data (resolves DG002)
3. **Obtain SAHPRA PI or international equivalent** (e.g., FDA label, EMA SmPC) for key warnings, contraindications, and monitoring requirements (resolves DG001 — currently Blocking)
4. **Clarify original approved indications** — populate `original_indications` field from the DrugBank or PI source
5. **Assess SAHPRA registration pathway** — if a repurposing candidate is identified and evidence is sufficient, determine whether a new application or Section 21 authorisation is required given current zero-registration status in South Africa

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Donepezil hydrochloride is currently **not registered with SAHPRA** and holds no marketing authorisation in South Africa. No registration re" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "The absence of SAHPRA registration reflects the local regulatory status only" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "no SAHPRA registration data, A repurposing recommendation cannot responsibly be made in the absence of these foundational inputs" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

