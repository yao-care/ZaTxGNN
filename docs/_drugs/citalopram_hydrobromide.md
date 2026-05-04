---
layout: default
title: Citalopram Hydrobromide
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 0
---

# Citalopram Hydrobromide
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

# Citalopram Hydrobromide: Repurposing Evaluation — Predicted Indication Pending

> **Report Status Notice:** This Evidence Pack is incomplete. The TxGNN prediction pipeline returned no predicted indications, and multiple critical data fields are unpopulated. This report documents the current data status and specifies the remediation steps required before a full repurposing evaluation can be conducted.

---

## One-Sentence Summary

Citalopram hydrobromide is a selective serotonin reuptake inhibitor (SSRI) with well-established use in depression and anxiety disorders.
The TxGNN prediction pipeline has **not generated a repurposing candidate** for this drug in the current evaluation cycle — key input data are missing.
Until the pipeline is re-run with a complete drug profile, no evidence-based repurposing direction can be assessed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not confirmed in Evidence Pack |
| Predicted New Indication | Not available — prediction pending |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| South Africa Market Status | Not registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Background: Drug Overview

Formal mechanism of action (MOA) data and original indication text are not available in this Evidence Pack (Data Gaps DG001 and DG002).

Based on established pharmacological knowledge, citalopram hydrobromide belongs to the **selective serotonin reuptake inhibitor (SSRI)** class. It exerts its effect by blocking the serotonin transporter (SERT), thereby increasing serotonergic neurotransmission in the central nervous system. Its primary established use is in **major depressive disorder (MDD)**, with additional evidence in generalised anxiety disorder, panic disorder, and obsessive-compulsive disorder.

Because no TxGNN predicted indication has been generated, it is not possible at this stage to describe the mechanistic bridge between the original indication and a repurposing target. This section will be populated once the prediction pipeline is re-run with a complete drug profile.

> **Pipeline anomaly noted:** The query log records a successful DrugBank query (`result_status: success`, `result_count: 1`) for citalopram hydrobromide, yet the `drugbank_id` field remains null. This inconsistency should be investigated — the DrugBank record may have been retrieved but not parsed correctly into the Evidence Pack.

---

## South Africa Market Information

Citalopram hydrobromide currently has **no SAHPRA registrations** recorded in this Evidence Pack.

> No registered products were found to tabulate. Before any procurement or regulatory decision, this result should be verified against the current [SAHPRA online register](https://www.sahpra.org.za/), as citalopram preparations are widely available internationally and registration data in this dataset may be incomplete or not yet ingested.

---

## Safety Considerations

Formal safety data — including key warnings, contraindications, and drug–drug interactions — were not retrieved for this Evidence Pack.

> Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predicted indication is available, and the foundational data required for a repurposing evaluation — MOA, original indication, SAHPRA registration, and safety profile — are all absent. Proceeding without these inputs would not meet the minimum evidence threshold for any recommendation level.

**To proceed, the following is needed:**

- **Re-run the TxGNN prediction pipeline** for citalopram hydrobromide to generate a predicted indication and confidence score
- **Retrieve the full DrugBank drug profile** (MOA, categories, pharmacodynamics) — Data Gap DG002; investigate why the successful DrugBank query returned a null `drugbank_id`
- **Retrieve and parse the package insert (PI)** from the SAHPRA or TFDA official source for warnings, contraindications, and approved indication text — Data Gap DG001
- **Verify SAHPRA registration status** via the official register to confirm whether citalopram products are currently authorised in South Africa
- **Confirm the DrugBank identifier** to enable consistent downstream queries across the evidence collection pipeline

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. For patient-specific decisions, consult the SAHPRA-approved Professional Information.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

