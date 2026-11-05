---
noindex: true
sitemap: false
layout: default
title: Bisoprolol Fumarate
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-05
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
| South Africa Market Status | Marketed (valid licences: 86 of 93) |
| Number of SAHPRA Registrations | 93 (valid: 86) |
| Recommended Decision | **Hold** |

> ⚠️ **Data Quality Notice:** Bisoprolol Fumarate is a globally available cardiovascular medicine. Independent verification against the [SAHPRA Online Medicine Register](https://www.sahpra.org.za/medicines/) is strongly recommended before drawing any regulatory conclusions.

---

## South Africa Market Information

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/6.1/0457 | Cardicor | tablet | Valid |
| 36/6.1/0458 | Cardicor | tablet | Valid |
| 36/6.1/0459 | Cardicor | tablet | Valid |
| 37/5.2/0010 | Adco-bisocor | tablet | Valid |
| 37/5.2/0011 | Adco-bisocor | tablet | Valid |

Showing 5 of 93 registrations (valid registrations first).

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

