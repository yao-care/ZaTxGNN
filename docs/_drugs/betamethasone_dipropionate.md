---
layout: default
title: Betamethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 0
---

# Betamethasone Dipropionate
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

# Betamethasone Dipropionate: Repurposing Evaluation — Insufficient Data to Proceed

## One-Sentence Summary

Betamethasone dipropionate is a potent synthetic corticosteroid with established use in inflammatory conditions. The current Evidence Pack returned **no TxGNN-predicted new indications** for this compound, and **no SAHPRA registrations** were found in the dataset. A **Hold** decision is recommended pending resolution of two blocking data gaps before the prediction pipeline can be re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not applicable — no predictions returned |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a valid DrugBank ID and at least one mapped original indication to traverse the knowledge graph and generate repurposing candidates. For this submission, both fields were absent:

- **DrugBank ID**: Not resolved. Without this identifier, the drug node cannot be located in the knowledge graph, and no drug–disease edge scores can be computed.
- **Original indications**: The `original_indications` field was returned empty. Even if a DrugBank ID were available, an empty indication profile prevents the model from establishing a mechanistic baseline for comparison.

Betamethasone dipropionate is a well-characterised Class I potent corticosteroid. It acts by binding to intracellular glucocorticoid receptors, suppressing the transcription of pro-inflammatory cytokines and mediators. The drug class has documented clinical utility across dermatology, rheumatology, and respiratory medicine. This existing pharmacological knowledge, however, cannot substitute for the structured data inputs the TxGNN pipeline requires.

Two data gaps flagged in the Evidence Pack must be resolved before a meaningful repurposing evaluation is possible:

| Gap ID | Item | Severity | Recommended Remediation |
|--------|------|----------|------------------------|
| DG001 | SAHPRA Professional Information (PI) — warnings and contraindications | Blocking | Download PI PDF from SAHPRA website and parse for structured safety fields |
| DG002 | Mechanism of action (MOA) | High | Query DrugBank API using resolved DrugBank ID |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing candidates were generated because the drug's DrugBank ID and original indication data were not available in the submitted Evidence Pack. Without these inputs, neither a prediction score nor an evidence review can be produced.

**To proceed, the following is needed:**

- **Resolve DrugBank ID** for betamethasone dipropionate (search term: "betamethasone dipropionate") to enable knowledge graph node mapping
- **Remediate DG001 (Blocking):** Download and parse the SAHPRA-approved PI for warnings, contraindications, and special population data
- **Remediate DG002 (High):** Retrieve MOA data from the DrugBank API once the DrugBank ID is confirmed
- **Confirm SAHPRA registration status:** The current dataset shows zero registrations; verify whether betamethasone dipropionate is marketed under a combination product or topical formulation not captured in this query
- **Re-run the TxGNN pipeline** with a complete drug profile (DrugBank ID + original indications + MOA) and regenerate the Evidence Pack
- **Re-submit** the completed Evidence Pack for a full repurposing evaluation report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

