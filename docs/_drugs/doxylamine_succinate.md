---
layout: default
title: Doxylamine Succinate
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 0
---

# Doxylamine Succinate
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

# Doxylamine Succinate: Evaluation Report — No TxGNN Repurposing Prediction Available

---

## One-Sentence Summary

Doxylamine succinate is a first-generation H1 antihistamine with sedative properties, widely used internationally for short-term insomnia and pregnancy-related nausea (in combination with pyridoxine). The current evidence pack contains **no TxGNN repurposing predictions** for this drug, and it carries **zero SAHPRA registrations** in South Africa. This report serves as a data gap summary; a full repurposing evaluation cannot be completed until core data items are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in evidence pack (antihistamine/sedative class by pharmacological class) |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — model prediction only; no actual studies linked |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Evaluation Is Possible at This Stage

Two blocking data gaps prevent a standard repurposing evaluation:

**1. No TxGNN prediction output.** The `predicted_indications` field is an empty array. Without a candidate target disease from the TxGNN model, there is no repurposing hypothesis to evaluate, no mechanistic link to explore, and no evidence table to populate.

**2. Missing mechanism of action (MOA) data.** The DrugBank query returned a result (query log ID 1), but the `drugbank_id` and `original_moa` fields were not populated. Doxylamine's H1 receptor antagonism is well-established in the scientific literature, but the pipeline did not capture this, suggesting a name-matching or API extraction issue that must be resolved before automated analysis can proceed.

Until both gaps are resolved, any repurposing inference would be speculative and outside the scope of this evidence-based report format.

---

## South Africa Market Status

Doxylamine succinate currently has **no SAHPRA registrations**. It is not listed on the South African Essential Medicines List (EML). Healthcare professionals seeking to use this drug in South Africa would need to access it through Section 21 unregistered medicine provisions, or await a formal registration application.

> Note: Doxylamine-containing products (e.g., combined with pyridoxine for pregnancy nausea) are available in other markets such as the United States (Diclegis®/Bonjesta®) and Canada. A targeted SAHPRA registration pathway for the pregnancy nausea indication may be worth exploring separately.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the [MedSafety reporting platform](https://www.sahpra.org.za/).

> Clinicians should be aware that doxylamine is a first-generation antihistamine with known CNS sedation effects. Standard antihistamine precautions apply (avoid concurrent CNS depressants, caution in elderly patients and those operating machinery). Full safety data must be extracted from the SAHPRA or international PI before any institutional use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no TxGNN-generated repurposing hypothesis to evaluate, and critical drug-level data (DrugBank ID, MOA, regulatory warnings) are absent. Without these inputs the report framework cannot produce a meaningful evidence-based recommendation.

**To proceed, the following is needed:**

- [ ] **Resolve TxGNN pipeline gap** — Re-run the prediction pipeline after confirming that `DOXYLAMINE SUCCINATE` maps correctly to a DrugBank node; check for name-variant issues (e.g., "doxylamine" without salt suffix)
- [ ] **Extract MOA from DrugBank** — The query returned 1 result; investigate why `drugbank_id` and `original_moa` were not populated and re-run the API extraction step
- [ ] **Obtain SAHPRA/international PI** — Download and parse the approved Professional Information for key warnings and contraindications (marked as Blocking, DG001)
- [ ] **Confirm intended repurposing hypothesis** — If a specific new indication is already under consideration by the requesting clinician or researcher, provide this as a manual input to bypass the empty `predicted_indications` and proceed with a targeted evidence review
- [ ] **Assess SAHPRA registration feasibility** — If the pregnancy nausea (with pyridoxine) or insomnia indication is the intended use case, initiate a Section 21 or full registration pathway assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

