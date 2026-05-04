---
layout: default
title: Amlodipine Besylate
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 0
---

# Amlodipine Besylate
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

# Amlodipine Besylate: Drug Repurposing Evaluation — Pending TxGNN Prediction Data

## One-Sentence Summary

Amlodipine besylate is a well-established dihydropyridine calcium channel blocker widely used for the management of hypertension and angina pectoris.
The TxGNN model did not generate any repurposing predictions for this drug in the current evidence pack — the prediction pipeline could not complete due to an unresolved DrugBank ID mapping.
This report is a **preliminary holding record** and cannot proceed to a full repurposing evaluation until the data gaps below are remediated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Angina Pectoris (established from pharmacological class; not retrieved from registry) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| South Africa Market Status | Not Marketed (per available data — see note below) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

> ⚠️ **Data Note:** The market status of "Not Marketed" reflects what was retrieved during this pipeline run. Amlodipine is a globally ubiquitous antihypertensive that is almost certainly registered in South Africa under multiple brand names. This result most likely indicates a data retrieval failure rather than actual non-registration. **SAHPRA's online registry must be consulted directly before drawing any conclusions.**

---

## South Africa Market Information

No SAHPRA registration records were returned in this evidence pack. The regulatory data module could not locate any active licences for AMLODIPINE BESYLATE.

**Recommended action:** Search the [SAHPRA MCC Registered Medicines Database](https://www.sahpra.org.za/analytical-laboratory/mcc-registered-medicines/) directly using both the INN "amlodipine" and the salt form "amlodipine besylate" to retrieve current licence holders, dosage forms, and approved indications. Known South African brand names likely to appear include Amloc, Amlovasc, and Norvasc, among generics.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the [MedErr online reporting system](https://www.sahpra.org.za/pharmacovigilance/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline did not produce any repurposing candidates for amlodipine besylate because the DrugBank ID could not be resolved, which is a prerequisite for knowledge-graph traversal. Without at least one ranked predicted indication, no evidence review, mechanistic plausibility assessment, or clinical decision can be made.

**To proceed, the following is needed:**

- **[Blocking — DG001]** Retrieve the SAHPRA-approved Professional Information (PI) to obtain current warnings, contraindications, and approved indications. Source: [SAHPRA website](https://www.sahpra.org.za).
- **[High — DG002]** Resolve the DrugBank ID for amlodipine besylate (expected: DB00381) and re-query the DrugBank API to retrieve the mechanism of action and drug interaction data. Source: [DrugBank Open Data](https://go.drugbank.com/drugs/DB00381).
- **[Pipeline]** Re-run the TxGNN KG + DL prediction pipeline after DrugBank ID is confirmed, to generate scored repurposing candidates.
- **[Registry]** Manually verify South Africa market and SAHPRA registration status independently of the automated pipeline.
- **[Safety]** Once DrugBank ID is confirmed, re-query the DDI module to populate drug-drug interaction data.

Once the DrugBank ID is resolved and the prediction pipeline is re-run, this record should be automatically updated and escalated to a full evaluation report.

---

*This report was generated on 2026-04-04 using Evidence Pack v4 (candidate ID: TW-UNKNOWN-multi). All findings are for research reference only and do not constitute medical advice. Drug repurposing candidates require clinical validation before any application. This document contains YMYL content — consult a qualified healthcare professional for clinical decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

