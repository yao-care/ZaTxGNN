---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a thiazolidinedione (PPAR-γ agonist) insulin sensitiser originally used for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — score alone, no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (thiazolidinedione class; South Africa-specific approved indication text unavailable — drug is not marketed locally) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known information, pioglitazone is a PPAR-γ agonist belonging to the thiazolidinedione class, and its efficacy in improving peripheral insulin sensitivity in type 2 diabetes is well established.

Opsismodysplasia is a rare skeletal dysplasia caused by *INPPL1* gene mutations. According to the model's own repurposing rationale, there is **no known direct pathological connection** between this condition and the PPAR-γ/insulin signalling pathway that pioglitazone targets. The rationale explicitly flags this as a potential high-score false positive from the knowledge graph, with mechanistic relevance assessed as very low.

Given the complete absence of clinical trial or literature support, and the acknowledged weakness of the mechanistic link, this prediction should be treated as a hypothesis-generating signal only, not as a basis for clinical consideration at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Pioglitazone currently has no SAHPRA registrations on file (South Africa market status: Not Marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: Key warnings, contraindications, and TFDA label data for this drug are currently unavailable (flagged as a **Blocking** data gap — DG001), meaning safety review cannot proceed to initial screening (S1) until this information is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has an L5 evidence level (model prediction only), zero clinical trials, zero literature support, and the model's own rationale identifies the mechanistic link as very low confidence and possibly a false positive. The drug is also not currently marketed in South Africa.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank (DG002, High severity)
- TFDA/SAHPRA product label warnings and contraindications (DG001, Blocking severity — required before any safety screening)
- Preclinical or mechanistic studies directly linking PPAR-γ activity to *INPPL1*-related skeletal pathology
- Confirmation of South African regulatory/market pathway if pursuit is considered
- Consideration of lower-ranked but more mechanistically plausible candidates (e.g., lipodystrophy-related indications, ranks 5–8) where PPAR-γ's role in adipogenesis offers a stronger biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

