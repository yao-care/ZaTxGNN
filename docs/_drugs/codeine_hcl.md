---
layout: default
title: Codeine Hcl
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 0
---

# Codeine Hcl
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

# Codeine HCL: Incomplete Evidence Pack — Drug Repurposing Evaluation Not Possible

## One-Sentence Summary

Codeine HCL is a well-known opioid analgesic and antitussive agent used for pain management and cough suppression. The TxGNN model returned **no predicted indications** for this candidate, most likely because the DrugBank ID could not be resolved, preventing the drug from being matched to the knowledge graph. The current Evidence Pack contains **multiple critical data gaps** that block a complete repurposing evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN knowledge graph pipeline could not generate any repurposing predictions for Codeine HCL because the DrugBank ID was not resolved, meaning the drug could not be linked to the knowledge graph. Without predictions, a repurposing evaluation cannot proceed. Additionally, the drug has no current SAHPRA registrations on record, and all safety data fields carry unresolved data gaps.

**To proceed, the following is needed:**

- **Resolve DrugBank ID** — Search DrugBank for "codeine" (likely DB00318) and confirm the correct entry for Codeine HCL; update the candidate record with the verified `drugbank_id`.
- **Re-run TxGNN prediction pipeline** — Once the DrugBank ID is confirmed, re-run the KG and DL prediction steps to generate repurposing candidates with scored indications.
- **Retrieve MOA data** — Query the DrugBank API for mechanism of action (opioid receptor agonism) to populate the `original_moa` field and enable mechanistic reasoning.
- **Obtain SAHPRA PI / safety data** — Confirm whether Codeine HCL is registered in South Africa under a combination product (e.g., with paracetamol or ibuprofen); download the approved Professional Information (PI) to extract warnings and contraindications.
- **Verify market status** — Codeine-containing products are commonly registered as combination medicines in many markets; a targeted SAHPRA database search under combination product names is recommended before concluding the drug is entirely absent from the South African market.

> **Note:** This report cannot be used for clinical or formulary decision-making. All drug repurposing candidates require clinical validation before application. This output is for research reference only and does not constitute medical advice.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

