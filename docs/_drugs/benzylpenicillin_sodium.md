---
layout: default
title: Benzylpenicillin Sodium
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 0
---

# Benzylpenicillin Sodium
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

# Benzylpenicillin Sodium: No Repurposing Prediction Generated

## One-Sentence Summary

Benzylpenicillin Sodium (Penicillin G) is a foundational beta-lactam antibiotic with well-established use in treating serious bacterial infections such as pneumococcal pneumonia, syphilis, meningococcal meningitis, and streptococcal septicaemia.
The TxGNN model **did not generate any repurposing predictions** for this drug in the current run, likely due to an unresolved DrugBank identifier and absent regulatory input data.
Without prediction output, mechanism of action documentation, or SAHPRA registration records in the Evidence Pack, **no evidence-based repurposing recommendation can be made at this stage**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (beta-lactam antibiotic class) |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no prediction output produced |
| South Africa Market Status | Not marketed (per Evidence Pack) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedErr reporting system.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned no predictions for Benzylpenicillin Sodium, and the Evidence Pack is missing all three inputs required for evaluation — a resolved DrugBank ID, SAHPRA licensing records, and mechanism of action data — making any repurposing recommendation premature.

> **Note for reviewers:** Benzylpenicillin Sodium (Penicillin G) is a WHO Essential Medicine and is in routine clinical use across South Africa (e.g., for syphilis treatment in PMTCT programmes and rheumatic fever prophylaxis). The absence of SAHPRA records in this Evidence Pack most likely reflects a **data ingestion gap** rather than a genuine lack of registration. This should be confirmed before interpreting the "Not marketed" status.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Query the DrugBank API for "Benzylpenicillin" / "Penicillin G" to obtain the canonical identifier (expected: DB01053) and retrieve the full mechanism of action
- **Verify SAHPRA registration**: Cross-check the SAHPRA online medicines register directly; Penicillin G injections are expected to appear under several licence holders
- **Check Essential Medicines List (EML) status**: Confirm inclusion on the South African Standard Treatment Guidelines and EML (adult and paediatric), which would affect formulary access decisions
- **Confirm correct INN in pipeline**: Ensure the data pipeline maps "BENZYLPENICILLIN SODIUM" to the same node as "Penicillin G" in the TxGNN knowledge graph to avoid missed predictions
- **Re-run TxGNN prediction** once drug identity and regulatory inputs are confirmed
- **Retrieve PI document**: Download the SAHPRA-approved package insert to populate contraindications, warnings (particularly penicillin hypersensitivity / anaphylaxis risk), and drug interaction data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

