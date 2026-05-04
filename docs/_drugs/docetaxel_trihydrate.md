---
layout: default
title: Docetaxel Trihydrate
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 0
---

# Docetaxel Trihydrate
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

# Docetaxel Trihydrate: Repurposing Evaluation — Prediction Data Unavailable

## One-Sentence Summary

Docetaxel Trihydrate is a well-established taxane-class antineoplastic agent used globally for solid tumours including breast, lung, prostate, and gastric cancers. However, the current Evidence Pack contains **no TxGNN repurposing predictions** for this compound, and the automated pipeline retrieved **zero SAHPRA registrations**. A **Hold** decision is warranted until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in Evidence Pack |
| Predicted New Indication | No prediction available |
| TxGNN Prediction Score | Not available |
| Evidence Level | — (No prediction generated) |
| South Africa Market Status | Not Registered (SAHPRA) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Cytotoxicity

Docetaxel Trihydrate is confirmed as a taxane-class cytotoxic agent; the drug name itself identifies it as belonging to a recognised cytotoxic chemotherapy category.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia is a clinically significant risk |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | FBC with differential count (before each cycle), liver function tests (ALT, AST, total bilirubin, alkaline phosphatase), renal function, cumulative fluid retention |
| Handling Protection | Must be handled as a hazardous cytotoxic drug; closed-system drug transfer devices (CSTD) are recommended; PPE required per national cytotoxic handling regulations |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note:** No SAHPRA-approved PI was found in this Evidence Pack, as the drug is not currently registered in South Africa under this name. Until local registration is confirmed, prescribers should refer to an internationally recognised source (e.g., EMA-approved SmPC or FDA-approved PI for Docetaxel).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Docetaxel Trihydrate is missing three critical inputs — a TxGNN repurposing prediction, SAHPRA registration records, and mechanism of action data — making it impossible to conduct any meaningful repurposing or safety assessment at this stage.

**To proceed, the following is needed:**

- **Re-run TxGNN pipeline** with the correct DrugBank ID for Docetaxel (likely DB01248); confirm whether the pipeline should query "Docetaxel" rather than the salt form "Docetaxel Trihydrate"
- **Investigate SAHPRA registration gap** — Docetaxel products (e.g., Taxotere®, Docefrez®) may be registered under the non-salt INN "Docetaxel"; repeat the SAHPRA query with the shorter INN to capture existing licenses
- **Retrieve MOA data** from DrugBank (DB01248) to enable mechanism-based repurposing rationale
- **Retrieve PI warnings and contraindications** from SAHPRA or an approved international regulatory source
- **Check Essential Medicines List (EML) inclusion** — Docetaxel may already appear on the South African EML under an oncology indication, which would affect the repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

