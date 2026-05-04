---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin Glargine is a long-acting basal insulin analogue, widely used as a cornerstone treatment for both Type 1 and Type 2 Diabetes Mellitus.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, however there are **no registered clinical trials** and **no supporting publications** currently available for this specific indication, making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 1 and Type 2 Diabetes Mellitus (basal insulin replacement therapy) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established clinical knowledge, Insulin Glargine is a long-acting insulin analogue engineered to mimic endogenous basal insulin secretion. It binds to insulin receptors to regulate glucose uptake and suppress hepatic glucose output, providing a stable 24-hour glycaemic baseline. Its efficacy in both Type 1 and Type 2 Diabetes Mellitus is supported by decades of clinical evidence and international guidelines.

Autoimmune oophoritis is closely associated with Autoimmune Polyglandular Syndrome Type 2 (APS-2, also known as Schmidt's Syndrome), a condition characterised by the co-occurrence of autoimmune Addison's disease, autoimmune thyroid disease, and Type 1 Diabetes Mellitus (T1DM). Because T1DM and autoimmune oophoritis frequently co-occur within the APS-2 spectrum, the TxGNN model likely captured this connection through a shared comorbidity node in its knowledge graph, resulting in a high prediction score.

However, this link represents a **comorbidity association, not a causal treatment pathway**. Insulin Glargine has no known mechanism of action against anti-ovarian autoantibodies (such as anti-21-hydroxylase or anti-oocyte antibodies), and there is no biological rationale for it to directly modify the autoimmune pathology affecting the ovaries. This prediction should be interpreted as a false positive arising from shared disease context within the APS-2 network, and does not constitute a clinically actionable repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Insulin Glargine is currently **not listed** with any SAHPRA-registered products in this evidence pack (0 registrations, status: Not Marketed).

> **Important note for clinicians:** This likely reflects a data gap in the current evidence pack rather than true market absence. Insulin Glargine products (e.g., Lantus® 100 U/mL, Toujeo® 300 U/mL) are widely used globally and Insulin Glargine is included in the **South African Essential Medicines List (EML)** for primary and hospital level care. Verification against the current SAHPRA medicines register is strongly recommended before drawing conclusions about local availability.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction linking Insulin Glargine to Autoimmune Oophoritis is driven by shared comorbidity associations within the Autoimmune Polyglandular Syndrome Type 2 network, not by any direct pharmacological mechanism. With no supporting clinical trials, no published literature, and no mechanistic basis for treating ovarian autoimmune pathology with insulin, there is currently insufficient justification to pursue this as a repurposing candidate.

**To proceed, the following is needed:**

- **Mechanism of action data (MOA):** Retrieve from DrugBank API (DB00047) to enable formal mechanistic linkage analysis
- **Safety data:** Download SAHPRA-approved PI documents to obtain key warnings, contraindications, and drug interactions — currently blocking entry to safety screening (Data Gap DG001)
- **SAHPRA registration verification:** Confirm current market authorisation status against the live SAHPRA register, as 0 registrations likely reflects a data extraction gap
- **Preclinical evidence:** Any in vitro or animal studies demonstrating a direct effect of Insulin Glargine on autoimmune oophoritis pathology would be required before this prediction could be elevated beyond L5
- **Clinical context review:** Consider whether this prediction is more accurately classified as a **false positive** due to APS-2 comorbidity bias, and flag it accordingly in the TxGNN candidate ranking pipeline

> ⚠️ **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All findings should be interpreted in conjunction with the full SAHPRA-approved prescribing information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

