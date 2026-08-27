---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a DPP-4 inhibitor used to manage type 2 diabetes (confirmed only via literature captured in this evidence pack — no official SAHPRA indication text is on file). The TxGNN model's top-ranked prediction for this drug is **Classic Stiff Person Syndrome**, but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from literature within this pack; not confirmed by SAHPRA licensing data — none on file) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for vildagliptin is not available in this evidence pack (flagged as a High-severity data gap). Based on literature captured elsewhere in this pack, vildagliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor that raises endogenous GLP-1/GIP levels to improve glycemic control in type 2 diabetes, primarily by enhancing pancreatic islet (alpha and beta cell) function.

Classic Stiff Person Syndrome, by contrast, is a rare autoimmune neurological disorder driven by anti-GAD65 antibodies and disrupted GABAergic transmission. As the model's own repurposing rationale explicitly states, there is **no known mechanistic overlap** between the DPP-4/incretin pathway and GABAergic/autoimmune neurological pathways.

This prediction should therefore be read as a pure graph-embedding association from TxGNN, not a mechanistically or clinically supported hypothesis. The high similarity score reflects pattern-matching within the knowledge graph rather than any biological or empirical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Vildagliptin currently holds no SAHPRA registrations and is not marketed in South Africa (0 licenses on file in this evidence pack).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A blocking data gap exists — TFDA/SAHPRA label warnings and contraindications have not yet been retrieved, which prevents this candidate from entering the S1 safety pre-assessment stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support, and the model's own rationale confirms no established mechanistic link between DPP-4 inhibition and stiff person syndrome's autoimmune/GABAergic pathology. Combined with the absence of SAHPRA registration and missing safety/label data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Vildagliptin's SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data from DrugBank — currently a High-severity data gap
- Any emerging preclinical or case-level evidence linking DPP-4 inhibition to autoimmune neurological disease before further evaluation
- Alternative predicted indications in this evidence pack should be considered instead: notably **Type 1 Diabetes Mellitus** (rank 10) has an L2 evidence level with 50 clinical trials and 20 publications, including a completed RCT on β-cell function (rapamycin + vildagliptin), and is flagged "Research Question" rather than "Hold" — a substantially stronger starting point for further review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

