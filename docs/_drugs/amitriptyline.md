---
layout: default
title: Amitriptyline
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 0
---

# Amitriptyline
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

# Amitriptyline (DB00321): Drug Repurposing Evaluation — Insufficient Data to Generate Predictions

---

## One-Sentence Summary

Amitriptyline is a well-established tricyclic antidepressant (TCA) with decades of clinical use for depression and neuropathic pain.
However, the current Evidence Pack contains **no TxGNN repurposing predictions**, no SAHPRA registration records, and critical safety data gaps — making a standard repurposing evaluation impossible at this stage.
**Key data gaps (DG001, DG002) must be resolved before this candidate can progress.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable (pipeline did not complete) |
| South Africa Market Status | Not registered with SAHPRA |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## South Africa Market Information

No SAHPRA registrations were found for Amitriptyline in the current dataset.

> **Note for reviewers:** Amitriptyline is a long-established generic medicine widely used internationally. The absence of SAHPRA records likely reflects a data collection gap rather than true absence from the South African market. Before concluding the drug is unavailable locally, verify directly against the [SAHPRA online medicine register](https://www.sahpra.org.za) and check Essential Medicines List (EML) inclusion status.

---

## Safety Considerations

All safety fields (warnings, contraindications, and drug interactions) were flagged as data gaps in this Evidence Pack. No DDI records were returned.

> Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information, including black-box warnings associated with tricyclic antidepressants (e.g., suicidality in young adults, cardiac arrhythmia risk, anticholinergic effects). Report adverse drug reactions to SAHPRA via the [MedSafety reporting portal](https://www.sahpra.org.za/pharmacovigilance/).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Amitriptyline is critically incomplete — the TxGNN prediction pipeline returned no repurposing candidates, no SAHPRA registration data is available for analysis, and both MOA and safety fields are empty. There is no scientific basis on which to evaluate a new indication at this time.

**To proceed, the following is needed:**

- **Resolve DG002 (High priority):** Retrieve Amitriptyline's mechanism of action from DrugBank (DB00321) via the DrugBank API — MOA data is required to evaluate mechanistic plausibility for any new indication
- **Resolve DG001 (Blocking):** Download and parse the SAHPRA-approved Professional Information (PI) PDF to populate warnings and contraindications
- **Re-run TxGNN prediction pipeline:** Investigate why no predictions were generated — check whether DB00321 is present in the knowledge graph node list and whether the drug-disease relation mappings are loading correctly
- **Verify SAHPRA market status:** Confirm registration status directly via the SAHPRA online medicine register; update `market_status` field accordingly
- **Re-submit for evaluation** once the above steps are complete and an Evidence Pack version ≥ v5 is available with at least one predicted indication

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data as of 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

