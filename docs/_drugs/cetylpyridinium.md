---
layout: default
title: Cetylpyridinium
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 0
---

# Cetylpyridinium
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

# Cetylpyridinium (DB11073): Drug Repurposing Evaluation Report – No Predictions Generated

---

## One-Sentence Summary

Cetylpyridinium is a cationic quaternary ammonium compound widely recognised as a topical antiseptic, most commonly used in oral hygiene products (mouthwashes and throat lozenges) for its broad-spectrum antimicrobial activity.
The TxGNN model did **not generate any repurposing predictions** for this compound in the current analysis run, meaning no new indication could be evaluated.
As a result, **no evidence tables, clinical trial data, or literature links** are available at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oral antiseptic / antimicrobial (topical; not captured in current data pack) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 – Model prediction only (no prediction output available) |
| South Africa Market Status | Not Registered / Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction was produced for Cetylpyridinium in this evaluation cycle. Without a ranked candidate indication from the model, no mechanistic plausibility analysis can be meaningfully performed.

Currently, detailed mechanism of action (MOA) data is not available in this Evidence Pack. Based on general pharmacological knowledge, Cetylpyridinium is a cationic surfactant that disrupts microbial cell membranes, conferring broad antimicrobial activity against gram-positive and selected gram-negative organisms. Its systemic bioavailability is minimal, as it is typically applied topically to mucosal surfaces. Whether any systemic or novel therapeutic target could support a repurposing hypothesis remains to be determined pending MOA data retrieval from DrugBank (see Data Gaps below).

A repurposing evaluation can be re-initiated once the TxGNN pipeline produces ranked disease predictions for this compound and the blocking data gaps are resolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any repurposing indication.

---

## Literature Evidence

Currently no related literature available for a repurposing indication.

---

## South Africa Market Information

Cetylpyridinium is **not currently registered with SAHPRA** and has no approved products on the South African market.

> Note: Cetylpyridinium is commonly found as an inactive or active antiseptic ingredient in consumer oral hygiene products (e.g., mouthwashes) sold without prescription in many markets. Depending on the formulation and intended therapeutic claim, SAHPRA registration requirements may apply. Combination products containing Cetylpyridinium chloride should be evaluated on a product-by-product basis. Inclusion on the Essential Medicines List (EML) is not applicable at this stage.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, once a registered product is identified. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

> **Note on Data Gaps**: Two blocking/high-severity data gaps were identified in this Evidence Pack that must be resolved before any safety evaluation can proceed:
>
> | Gap ID | Item | Severity | Remediation |
> |--------|------|----------|-------------|
> | DG001 | Regulatory warnings and contraindications | **Blocking** | Retrieve and parse the registered product PI/package insert |
> | DG002 | Mechanism of action (MOA) | **High** | Query DrugBank API for DB11073 |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model did not generate any repurposing candidate predictions for Cetylpyridinium in this analysis run, and the compound has no current SAHPRA registration or South African market presence. There is insufficient data to initiate a repurposing evaluation at this time.

**To proceed, the following is needed:**

- [ ] **Re-run the TxGNN prediction pipeline** for DB11073 (Cetylpyridinium) and confirm whether a ranked list of candidate indications is generated; investigate whether the compound is present in the knowledge graph node list
- [ ] **Resolve DG002 (MOA)**: Query the DrugBank API for DB11073 to retrieve pharmacodynamic and pharmacokinetic data
- [ ] **Resolve DG001 (Safety warnings)**: Identify any registered product PI globally (e.g., FDA, EMA) and extract warnings, contraindications, and drug interactions
- [ ] **Confirm drug representation in TxGNN KG**: Verify that `CETYLPYRIDINIUM` is correctly mapped to a DrugBank node in `data/external/drugbank_vocab.csv`; check for alternative INN spellings (e.g., `cetylpyridinium chloride`, `CPC`)
- [ ] **Assess regulatory pathway**: If a repurposing indication is eventually identified, a SAHPRA Section 21 authorisation or new drug application process would need to be scoped, given zero existing local registrations

---

> ⚠️ **Disclaimer**: This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed by a qualified healthcare professional.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

