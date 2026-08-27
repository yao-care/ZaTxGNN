---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 7
---

# Verapamil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Verapamil: From Cardiovascular Indications to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a calcium channel blocker with an established cardiovascular pharmacology, though this evidence pack does not record its original approved indications or a sourced mechanism-of-action text. The TxGNN model's top-ranked prediction, **Obsolete Bundle Branch Block**, is not supported by any clinical trials or literature, and — more importantly — its own mechanistic rationale argues **against** benefit rather than for it. No candidate in this pack rises above weak, indirect evidence (L4 at best), so the overall recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licenses or `original_indications` recorded) |
| Predicted New Indication | Obsolete Bundle Branch Block ⚠️ (mechanistically contradictory — see below) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed, sourced mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, verapamil is a phenylalkylamine-class L-type calcium channel blocker with negative chronotropic, inotropic, and **dromotropic** (AV-conduction-slowing) effects, historically used for conditions such as hypertension, angina, and supraventricular arrhythmias.

This negative-dromotropic action is precisely why the top-ranked prediction does not hold up mechanistically: bundle branch block and other severe cardiac conduction disorders are a **relative or absolute contraindication** for verapamil, not a target for treatment — the drug would be expected to worsen conduction delay rather than correct it. The disease label itself ("obsolete bundle branch block") also appears to be a deprecated/non-standard ontology term, which may explain why the model surfaced a high similarity score without any grounding in trials or literature.

For context, a lower-ranked candidate in the same pack — **malignant renovascular hypertension** (rank 2, score 99.27%) — has a more coherent mechanistic story (verapamil's vasodilatory/antihypertensive effect is pharmacologically plausible for any severe hypertension subtype) and is supported by two PubMed records, though both are only indirectly relevant (a review on aldosterone/renin ratio confounders and a pediatric case report) and rated Tier 3. This makes it a "Research Question" (S1) candidate rather than an actionable one, and is not the primary subject of this report per the ranking, but is noted here because it is more scientifically defensible than rank 1.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Verapamil is currently **not marketed** in South Africa under this evidence pack, with **0 SAHPRA registrations** on record. No product listings are available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: retrieval of the manufacturer's warnings/contraindications text is flagged as a **Blocking** data gap in this pack — it must be resolved before any formal safety (S1) review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (obsolete bundle branch block) is contradicted by verapamil's own pharmacology — its conduction-slowing effect would be expected to worsen, not treat, this condition — and has zero supporting trials or literature (L5).
- No candidate in the full prediction set exceeds L4 evidence, and none has any completed clinical trial support.
- Verapamil has no current SAHPRA registration in this dataset, and a Blocking data gap (missing PI warnings/contraindications) prevents any preliminary safety assessment.

**To proceed, the following is needed:**
- Retrieval of SAHPRA-approved PI text (warnings, contraindications, DDI) to close the Blocking data gap
- A sourced, verified mechanism-of-action reference (e.g., DrugBank) rather than general pharmacology recall
- Clarification of the "obsolete bundle branch block" ontology term and whether it maps to a clinically meaningful, current diagnosis
- If pursuing repurposing further, prioritize the mechanistically coherent candidate (malignant renovascular hypertension) for a targeted literature/trial search rather than the top-scored but contradictory prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

