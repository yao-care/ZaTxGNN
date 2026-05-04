---
layout: default
title: Iron Dextran
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 0
---

# Iron Dextran
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

# Iron Dextran: Evaluation Pending — Insufficient Evidence Pack Data

---

## One-Sentence Summary

Iron Dextran (DrugBank ID: DB00893) is a parenteral iron complex indicated for the treatment of iron deficiency anaemia, classically used when oral supplementation is contraindicated or ineffective.
However, the current Evidence Pack contains **no TxGNN-predicted indications**, **no mechanism of action data**, and **no SAHPRA product registrations**, meaning a meaningful drug repurposing evaluation cannot be completed at this stage.
All critical data gaps must be resolved before this candidate can advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | — |
| Evidence Level | L5 (no predictions, no supporting studies retrieved) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction is Available

The TxGNN pipeline did not return any predicted indications for Iron Dextran in this run. Two blocking data gaps explain this:

**1. Missing mechanism of action (MOA):** Iron Dextran is a high-molecular-weight complex of ferric oxyhydroxide and low-molecular-weight dextran. It releases iron in the reticuloendothelial system, replenishing serum iron and ferritin stores. However, this MOA was not retrieved from DrugBank in the current run, which limits the knowledge graph's ability to identify mechanistic links to novel disease nodes.

**2. Missing original indication text:** No SAHPRA-registered product licences exist for Iron Dextran in South Africa, and no approved indication text was available to seed the prediction model. Without an anchor indication, the TxGNN ranking and scoring steps cannot be interpreted with confidence.

Before any repurposing hypothesis can be evaluated, the TxGNN pipeline must be re-run with complete DrugBank data (categories, targets, pathways) for DB00893.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Iron Dextran is **not currently registered with SAHPRA** and holds no active product licences in South Africa.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products | — | — |

Any clinical or research use in South Africa would require either:
- Full SAHPRA registration of an Iron Dextran product, **or**
- A **Section 21 authorisation** (unregistered medicine access under the Medicines and Related Substances Act, 1965)

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note for clinicians:** Iron Dextran products are generally associated with a risk of serious anaphylactic reactions following parenteral administration. A test dose is conventionally recommended before full therapeutic doses. These warnings could not be formally extracted in this run due to the absence of SAHPRA/TFDA monograph data (Data Gap DG001). Full safety review is deferred pending monograph retrieval.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The current Evidence Pack contains no TxGNN-predicted indications, no approved indication text, no mechanism of action data, and zero SAHPRA product registrations — making a structured repurposing evaluation impossible at this stage. Advancing without resolving the blocking data gap (DG001) would not meet the minimum evidence threshold for any decision tier.

**To proceed, the following is needed:**

- [ ] **Resolve DG001 (Blocking):** Download and parse the SAHPRA or TFDA Professional Information (PI) monograph for Iron Dextran to extract approved indications, warnings, and contraindications
- [ ] **Resolve DG002 (High):** Query DrugBank API for DB00893 to retrieve MOA, pharmacological targets, enzyme interactions, and drug categories
- [ ] **Re-run TxGNN pipeline** with complete input data (node.csv + kg.csv) once DrugBank fields are populated
- [ ] **SAHPRA regulatory pathway assessment:** Confirm whether a Section 21 authorisation or new registration is required for any proposed repurposed use
- [ ] **Manual literature search:** Conduct a targeted PubMed search (e.g., "iron dextran" AND "repurposing" OR "novel indication") as a bridging step while the pipeline data gaps are resolved
- [ ] **Safety review:** Once the monograph is retrieved, conduct a full DDI and contraindication review before any clinical application

---

*This report is generated for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

