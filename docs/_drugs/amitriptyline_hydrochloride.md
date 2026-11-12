---
noindex: true
sitemap: false
layout: default
title: Amitriptyline Hydrochloride
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Amitriptyline Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Amitriptyline Hydrochloride: Repurposing Evaluation — Prediction Data Unavailable
{: .text-alpha }

---

## One-Sentence Summary

Amitriptyline hydrochloride is a tricyclic antidepressant (TCA) with established use in depression, neuropathic pain, and migraine prophylaxis.
**No TxGNN repurposing predictions were generated in this evaluation run**.
A complete repurposing assessment cannot be completed until the two identified data gaps — SAHPRA label warnings (Blocking) and formal mechanism of action data (High) — are resolved.

<!-- review:begin za-lic-20261105-amitriptyline_hydrochloride-1 -->

> **Review correction (2026-11-05)**: Originally stated: "**No TxGNN repurposing predictions were generated in this evaluation run**, and the drug carries zero SAHPRA registrations on record in this Evidence Pack. / A complete repurposing assessment cannot be completed until the two identified data gaps — SAHPRA label warnings (Blocking) and formal mechanism of action data (High) — are resolved." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 28 registrations for this drug, 18 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amitriptyline_hydrochloride-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — prediction pipeline not completed |
| South Africa Market Status | Marketed (valid licences: 18 of 28; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 28 (valid: 18, of which 5 not confirmed by SAHPRA) |
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

> **Verification recommended:** Amitriptyline is an established medicine included on the WHO Essential Medicines List (EML) and is widely registered globally. Healthcare professionals should confirm current SAHPRA registration status directly via the [SAHPRA online medicines register](https://www.sahpra.org.za) before drawing conclusions from this data.

<!-- review:begin za-lic-20261105-amitriptyline_hydrochloride-2 -->

> **Review correction (2026-11-05)**: Originally stated: "According to this Evidence Pack, amitriptyline hydrochloride has **zero active SAHPRA product registrations** on record." Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 28 registrations for this drug, 18 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amitriptyline_hydrochloride-2 -->

<!-- review:begin za-lic-20261105-amitriptyline_hydrochloride-3 -->

> **Review correction (2026-11-05)**: Originally stated: "Healthcare professionals should confirm current SAHPRA registration status directly via the [SAHPRA online medicines register](https://www.sahpra.org.za) before drawing conclusions from this data. A data retrieval issue cannot be excluded." Removed: it continued a sentence that was removed for contradicting the SAHPRA registration data as of 2026-11-05, and would not make sense on its own. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amitriptyline_hydrochloride-3 -->

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
- **Re-run TxGNN prediction pipeline** after the above gaps are resolved to generate repurposing candidates and a full evidence-backed report

<!-- review:begin za-lic-20261105-amitriptyline_hydrochloride-4 -->

> **Review correction (2026-11-05)**: Originally stated: "**Verify SAHPRA registration status:** Manually search the SAHPRA medicines register for amitriptyline hydrochloride and all known South African brand names to confirm whether a zero-registration result reflects true absence or a data retrieval failure / **Re-run TxGNN prediction pipeline** after the above gaps are resolved to generate repurposing candidates and a full evidence-backed report" Removed: it conflicted with the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 28 registrations for this drug, 18 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amitriptyline_hydrochloride-4 -->

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Include YMYL disclaimer on all public-facing outputs.*

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "and the drug carries zero SAHPRA registrations on record in this Evidence Pack" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "According to this Evidence Pack, amitriptyline hydrochloride has **zero active SAHPRA product registrations** on record" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "A data retrieval issue cannot be excluded" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "**Verify SAHPRA registration status:** Manually search the SAHPRA medicines register for amitriptyline hydrochloride and all known South Afr" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

