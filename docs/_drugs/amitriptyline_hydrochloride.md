---
layout: default
title: Amitriptyline Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
---

# Amitriptyline Hydrochloride
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

# Amitriptyline Hydrochloride: Repurposing Evaluation — Prediction Data Unavailable

---

## One-Sentence Summary

Amitriptyline hydrochloride is a tricyclic antidepressant (TCA) with established use in depression, neuropathic pain, and migraine prophylaxis.
**No TxGNN repurposing predictions were generated in this evaluation run**, and the drug carries zero SAHPRA registrations on record in this Evidence Pack.
A complete repurposing assessment cannot be completed until the two identified data gaps — SAHPRA label warnings (Blocking) and formal mechanism of action data (High) — are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — prediction pipeline not completed |
| South Africa Market Status | Not marketed (0 SAHPRA registrations on record) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The TxGNN pipeline did not return any repurposing candidates for amitriptyline hydrochloride in this run. Two contributing factors were identified:

**DG001 (Blocking severity):** SAHPRA Professional Information (PI) label data — including warnings and contraindications — was not retrieved. This prevents the mandatory safety pre-screening step that gates entry into the repurposing candidate pipeline.

**DG002 (High severity):** Formal mechanism of action (MOA) data was not populated from DrugBank, despite a successful query returning one result. Without MOA data, the mechanistic relevance scoring that informs TxGNN predictions cannot be completed.

Based on general pharmacological knowledge, amitriptyline is known to inhibit norepinephrine and serotonin reuptake, with secondary antihistamine and anticholinergic activity. These broad pharmacological properties have historically supported off-label investigation in neuropathic pain, fibromyalgia, irritable bowel syndrome, and migraine prevention — suggesting real repurposing potential once the pipeline is unblocked. However, no evidence from this Evidence Pack can be cited to support a specific new indication at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## South Africa Market Information

According to this Evidence Pack, amitriptyline hydrochloride has **zero active SAHPRA product registrations** on record.

> **Verification recommended:** Amitriptyline is an established medicine included on the WHO Essential Medicines List (EML) and is widely registered globally. Healthcare professionals should confirm current SAHPRA registration status directly via the [SAHPRA online medicines register](https://www.sahpra.org.za) before drawing conclusions from this data. A data retrieval issue cannot be excluded.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Active data gaps affecting safety assessment:**
> - **DG001 — Blocking:** SAHPRA label warnings and contraindications were not retrieved. Formal safety pre-screening cannot proceed until this is resolved by downloading and parsing the SAHPRA PI PDF.
> - **DG002 — High:** DrugBank MOA and toxicity data were not populated, limiting the ability to assess mechanism-linked safety signals.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline was not completed due to a blocking data gap (missing SAHPRA PI label data), and no repurposing candidates were generated. Without a predicted indication, clinical trial evidence, or safety data, no repurposing decision can be made at this stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Download the SAHPRA Professional Information PDF for amitriptyline hydrochloride and extract warnings and contraindications to unblock the pipeline entry gate
- **Resolve DG002 (High):** Re-query the DrugBank API to retrieve and populate formal MOA, pharmacodynamic, and toxicity data (the query returned a successful result but data was not written to the Evidence Pack — investigate the extraction step)
- **Verify SAHPRA registration status:** Manually search the SAHPRA medicines register for amitriptyline hydrochloride and all known South African brand names to confirm whether a zero-registration result reflects true absence or a data retrieval failure
- **Re-run TxGNN prediction pipeline** after the above gaps are resolved to generate repurposing candidates and a full evidence-backed report

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Include YMYL disclaimer on all public-facing outputs.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

