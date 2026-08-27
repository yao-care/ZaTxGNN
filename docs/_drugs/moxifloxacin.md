---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Moxifloxacin (DrugBank DB00218) is a fourth-generation fluoroquinolone antibiotic; it is not currently registered with SAHPRA, so no South Africa–specific original indication text is available in this evidence pack. The TxGNN model's highest-ranked prediction for this drug is **Hyperamylasemia**, but this signal is currently supported by **0 clinical trials** and **0 publications**, and the underlying analysis flags it as a possible data artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA license text exists (drug not registered in South Africa); DrugBank original indication field is also empty |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available for moxifloxacin in this evidence pack (flagged as data gap DG002, severity High). Based on general pharmacological knowledge, moxifloxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV; it has no known pharmacological pathway connecting it to amylase metabolism or pancreatic function, which underlies hyperamylasemia.

The evaluators' own assessment of this candidate is explicit: there is **no mechanistic link** between moxifloxacin and hyperamylasemia, and no clinical trial or literature evidence supports the association. The prediction is described as a high-scoring knowledge-graph (KG) output with no corroborating signal, and the working hypothesis is that it may represent either data noise or an indirect comorbidity signal (e.g., patients receiving moxifloxacin for an infection who separately have elevated amylase for unrelated reasons) rather than a true drug-disease relationship.

Given the complete absence of supporting evidence and the lack of a plausible biological rationale, this prediction should be treated as exploratory only and not as a basis for clinical hypothesis generation at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## South Africa Market Information

Moxifloxacin currently has **no SAHPRA registrations** (0 licenses on record; market status: Not Marketed). No product/dosage-form information is available for South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA label warnings/contraindications for moxifloxacin are recorded as a Blocking data gap (DG001) in this evidence pack — this must be resolved before any safety-stage evaluation (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hyperamylasemia) has no clinical trial or literature support, no mechanistic rationale, and is explicitly flagged as a possible artifact of the knowledge-graph model rather than a real signal. Combined with the absence of MOA data and the drug's unregistered status in South Africa, there is no basis to advance this indication beyond exploratory screening.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent label warnings and contraindications (blocking gap DG001)
- Moxifloxacin mechanism of action data (DG002)
- Independent validation of the hyperamylasemia signal to rule out data noise or confounding comorbidity before any further evaluation
- Note: this candidate bundle (TW-DB00218-multi) contains other predicted indications with materially stronger evidence — **monoclonal gammopathy**, **congenital hematological disorder**, and **bubonic plague** (all scored L3/S1, "Research Question", with supporting clinical trials and/or literature, including class-effect mechanistic support for plague via fluoroquinolone activity against *Yersinia pestis*). These may warrant separate evaluation rather than hyperamylasemia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

