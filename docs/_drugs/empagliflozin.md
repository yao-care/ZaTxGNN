---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

*(Note: Original indication is not present in the evidence pack — `original_moa` and `original_indications` are both flagged as data gaps. "Type 2 Diabetes Mellitus" is stated here from general pharmacological knowledge of empagliflozin as an SGLT2 inhibitor, not from the supplied evidence.)*

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor and is **not currently registered or marketed in South Africa** according to the data provided. The TxGNN model predicts a possible link to **Focal Stiff Limb Syndrome**, but this is a **pure model-topology signal**: no clinical trials, no literature, and no plausible mechanistic pathway currently support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA registration or approved indication text on file |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for empagliflozin is not available in this evidence pack. Based on the rationale supplied alongside the prediction, empagliflozin acts as an SGLT2 inhibitor at the renal proximal tubule, regulating renal glucose reabsorption.

Focal stiff limb syndrome is a localized variant of stiff person syndrome, an autoimmune neurological disorder driven by anti-GAD65/amphiphysin antibodies that disrupt central GABAergic transmission. There is no known overlap between renal glucose-transport pharmacology and central autoimmune neurotransmission, and no established evidence that SGLT2 inhibitors cross the blood-brain barrier or exert immunomodulatory effects.

The evidence pack's own rationale explicitly cautions that the high TxGNN score (0.9906) should be interpreted as a **knowledge-graph connectivity signal**, not as mechanistic plausibility. Two related candidates in this same evidence pack — classic stiff person syndrome and opsismodysplasia — carry similarly high scores (0.9903–0.9906) with the same absence of mechanistic rationale, which is consistent with a shared graph-embedding artifact rather than three independent, biologically grounded signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registrations were found for empagliflozin in the data provided (`total_licenses: 0`, `licenses: []`). The drug's market status is recorded as **not marketed** in South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(All safety fields in the evidence pack — key warnings, contraindications, drug-drug interactions — are recorded as data gaps; DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on Evidence Level L5 (model output only) with no clinical trials, no literature, and a mechanistic rationale that the evidence pack itself characterizes as implausible. Empagliflozin is also not currently marketed or registered in South Africa, so there is no local regulatory or safety baseline to build on. The same Hold recommendation applies to the other two candidates in this pack (classic stiff person syndrome, opsismodysplasia — the latter carrying a specific caution that SGLT2 inhibitors have a known bone-density/fracture safety signal, working against rather than for repurposing).

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / PI warnings and contraindications (currently Blocking data gap — required before any S1 safety screening)
- Verified mechanism of action data from DrugBank or equivalent (currently High-severity data gap)
- Any preclinical or case-level evidence connecting SGLT2 inhibition to GABAergic/autoimmune neurological pathways, if this candidate is to be pursued further
- Confirmation of South African market/registration status before any repurposing pathway can be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

