---
layout: default
title: Aprotinin
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 0
---

# Aprotinin
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

# Aprotinin: Repurposing Evaluation — Insufficient Data for Standard Assessment

---

## One-Sentence Summary

Aprotinin (DrugBank: DB06692) is a serine protease inhibitor with a history of use as an antifibrinolytic agent in cardiac surgery, but it carries no current SAHPRA registration and is not marketed in South Africa. The TxGNN prediction pipeline returned **no repurposing candidates** for this drug in the current evidence pack, and critical data — including mechanism of action, safety warnings, and contraindications — remain unresolved. **No repurposing recommendation can be issued at this time; this report serves as a structured gap analysis.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no SAHPRA registrations on record) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not applicable — no predictions generated |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

Because the TxGNN model returned an empty prediction list for aprotinin, a mechanistic rationale for any new indication cannot be formally evaluated. Two contributing factors are likely:

**1. Missing mechanism of action data.** The evidence pack flags MOA as an unresolved gap (DG002). TxGNN relies on drug–target–disease relationships within the knowledge graph; if aprotinin's pharmacological targets are not adequately represented or linked, the model may fail to generate confident repurposing scores.

**2. No local regulatory anchor.** With zero SAHPRA registrations and no approved indication text, the pipeline lacks the local regulatory context that would normally anchor a South African repurposing assessment.

From publicly available sources, aprotinin is a broad-spectrum serine protease inhibitor (bovine pancreatic trypsin inhibitor, BPTI). It inhibits plasmin, kallikrein, and trypsin, reducing fibrinolysis and perioperative blood loss. It was previously marketed as **Trasylol®** (Bayer) for reduction of haemorrhage during cardiac surgery. Global market suspension occurred in 2008 following the BART trial, which identified excess all-cause mortality and serious renal and cardiovascular events compared with lysine analogues (tranexamic acid, aminocaproic acid). A restricted re-approval has since been granted in certain jurisdictions (e.g., Canada, Europe) with mandatory risk-minimisation measures. This historical safety context is material to any future repurposing consideration and must be explicitly addressed before any pipeline re-run.

---

## South Africa Market Information

Aprotinin is **not currently registered with SAHPRA** and has no approved products on the South African market. No Essential Medicines List (EML) inclusion applies. Before any repurposing pathway could be pursued, a full SAHPRA submission — or at minimum a Section 21 authorisation for restricted investigational use — would be required.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Important historical safety signal:** Aprotinin was subject to a global market suspension in 2008 following the BART trial (NCT00182585), which demonstrated a statistically significant increase in 30-day all-cause mortality compared with tranexamic acid and aminocaproic acid. Serious adverse events included acute renal failure, myocardial infarction, and stroke. Any consideration of use or repurposing in a South African setting must account for this risk profile and the restricted conditions under which re-approval has been granted elsewhere.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence pack is structurally incomplete — TxGNN generated no predictions, SAHPRA registration is absent, and both mechanism-of-action and safety data remain unresolved. There is no evidential basis on which to proceed with a repurposing evaluation under the current framework.

**To proceed, the following is needed:**

- **Resolve DG002 (High):** Retrieve full pharmacological target and MOA data from DrugBank API for DB06692 and confirm knowledge graph coverage before re-running TxGNN
- **Resolve DG001 (Blocking):** Obtain an equivalent regulatory document (e.g., EMA or Health Canada SmPC/Product Monograph) to substitute for the missing SAHPRA PI; extract warnings, contraindications, and special population restrictions
- **Re-run the TxGNN prediction pipeline** after data gaps are remediated to determine whether any repurposing candidates are generated with sufficient confidence scores
- **Conduct a structured safety review** of the post-2008 re-approval conditions (Health Canada 2011, EMA 2012) to understand what risk-minimisation measures apply and whether they are feasible in the South African context
- **Assess regulatory pathway:** Confirm whether a SAHPRA Section 21 authorisation or a full registration submission would be required for any repurposing indication that emerges from the pipeline
- **Consider alternative antifibrinolytics** (tranexamic acid, which is on the South African EML) as the active comparator benchmark for any future efficacy and safety comparison
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

