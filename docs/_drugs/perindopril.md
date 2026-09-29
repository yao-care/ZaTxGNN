---
layout: default
title: Perindopril
parent: Model Prediction Only (L5)
nav_order: 362
evidence_level: L5
indication_count: 5
---

# Perindopril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Perindopril: From ACE Inhibitor Therapy (Approved Indication Not Listed) to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Perindopril is an ACE inhibitor, and the SAHPRA records supplied list no approved indication text for it.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
There are **0 clinical trials** and **1 publication** retrieved for this indication, and the publication does not address perindopril, so this remains a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA records (drug class: ACE inhibitor) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, perindopril is an angiotensin-converting enzyme (ACE) inhibitor. ACE inhibitors block the renin-angiotensin-aldosterone system (RAAS), which can lower blood pressure and reduce pressure-related kidney injury. This class-based reasoning comes from general pharmacology, not from the supplied data.

Malignant hypertensive renal disease is kidney damage caused by severely raised blood pressure, and RAAS activity is often central to it. This is why blocking the RAAS is a plausible link. The prediction is high-scoring, but it has not been tested in this setting.

Other predicted indications rank similarly. Malignant renovascular hypertension is strongly RAAS-driven, so ACE inhibition is plausible there too. Two pulmonary hypertension entries and Braddock syndrome have no clear mechanistic link in the supplied data. None of the five predictions has a supporting clinical trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Observational (inferred from title, not verified) | Urologiia (Moscow) | Kidney function after nephrectomy for renal cancer. It does not study perindopril or ACE inhibitors, so it does not support the prediction. |

---

## South Africa Market Information

Perindopril has 9 SAHPRA registrations. The first 5 are listed below, and all are oral tablets. The supplied records contain no approved indication text or Essential Medicines List (EML) status.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 34/7.1.3/0480 | Vectoryl | Tablet |
| Reg. No. 37/7.1.3/0021 | Perindopril unicorn | Tablet |
| Reg. No. 41/7.1.3/0652 | Spec-perindopril | Tablet |
| Reg. No. 44/7.1.3/0503 | Ciplasyl plus 4mg/1.25mg | Tablet |
| Reg. No. 55/7.1.3/0812 | Teprilam 10/10 | Tablet |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The safety warnings and contraindications could not be retrieved. No drug interaction records were found.

For any future work on renovascular disease, renal function and renal artery stenosis status would need careful safety review. This point comes from the prediction rationale, not from PI data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.77%), but there are no clinical trials and no relevant publications, so the evidence level is L5. Safety data from the SAHPRA package insert is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and review the PI)
- SAHPRA approved indication text, to confirm the original indication
- Mechanism of action data (for example from DrugBank)
- A targeted literature search on ACE inhibitors in malignant hypertension and hypertensive nephropathy
- A search of trial registries, including SANCTR and PACTR, for relevant studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

