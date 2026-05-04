---
layout: default
title: Drospirenone
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 0
---

# Drospirenone
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

# Drospirenone: Repurposing Evaluation Pending — Insufficient Evidence Pack Data

## One-Sentence Summary

Drospirenone is a 4th-generation synthetic progestogen with antimineralocorticoid and antiandrogenic properties, widely used internationally in oral contraceptives and menopausal hormone therapy formulations.
This Evidence Pack contains **no TxGNN repurposing predictions** for drospirenone, and critical data elements — including original indications, mechanism of action, and safety warnings — are absent.
A complete drug repurposing evaluation **cannot be conducted** until these data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no linked studies; prediction pipeline not yet run |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

There are **no TxGNN-predicted indications** in this Evidence Pack, so no formal mechanistic justification for a new indication can be assessed at this stage.

From established pharmacological knowledge, drospirenone is structurally derived from 17α-spirolactone and is closely related to spironolactone. It exerts three distinct receptor-level actions: progestogenic (progesterone receptor agonist), antimineralocorticoid (aldosterone antagonist), and antiandrogenic activity. These properties distinguish it from older progestogens and underpin its role in combined oral contraceptives (e.g., with ethinyl estradiol) and hormone replacement therapy.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, drospirenone's aldosterone-antagonist mechanism may be mechanistically relevant to conditions such as primary hypertension, polycystic ovary syndrome (PCOS), hyperandrogenism, or oedematous states. However, until the TxGNN prediction pipeline is executed and predictions are generated, no repurposing direction can be formally evaluated or recommended.

---

## Clinical Trial Evidence

Currently no clinical trials are linked to this Evidence Pack. This reflects the absence of predicted indications, not the absence of evidence globally.

---

## Literature Evidence

Currently no literature is available in this Evidence Pack.

---

## South Africa Market Information

Drospirenone is currently **not marketed in South Africa** as a single-ingredient product and has **no SAHPRA-registered licences** recorded in this dataset.

> **Note for evaluators:** Drospirenone-containing combination products (e.g., drospirenone 3 mg + ethinyl estradiol 30 mcg; drospirenone 3 mg + estradiol 1 mg) may hold SAHPRA registration under separate DrugBank IDs corresponding to the fixed-dose combination. These are not captured in this single-entity evaluation and should be searched independently. Neither drospirenone alone nor drospirenone combinations currently appear on the South African Essential Medicines List (EML).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **Known class-level caution:** As an aldosterone antagonist, drospirenone carries a recognised risk of hyperkalaemia, particularly when co-administered with ACE inhibitors, ARBs, potassium-sparing diuretics, or NSAIDs. This interaction should be flagged in any future full safety review once PI data are obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is critically incomplete — there are no TxGNN repurposing predictions, no SAHPRA-registered products, no approved indication data, no mechanism of action, and no safety profile. No evidence-based repurposing recommendation can be issued in this state.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain the SAHPRA-approved Professional Information (PI) for drospirenone or its combination products to extract warnings, contraindications, and precautions
- **Resolve DG002 (High):** Confirm full mechanism of action via DrugBank API (DB01395) — including receptor binding data, pharmacodynamic profile, and known pharmacokinetic interactions
- **Run TxGNN pipeline:** Execute the knowledge-graph and deep-learning prediction pipeline for drospirenone (DB01395) to generate repurposing candidates
- **Check combination products:** Search SAHPRA register for drospirenone-containing fixed-dose combinations (FDCs) to establish actual market presence and approved indications
- **Confirm original indications:** Cross-reference EMA, FDA, and SAHPRA databases to populate the `original_indications` field before any repurposing analysis proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

