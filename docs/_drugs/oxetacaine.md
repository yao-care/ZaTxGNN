---
layout: default
title: Oxetacaine
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Oxetacaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Oxetacaine: From Topical Local Anaesthetic Use to Primary Release Disorder of Platelets

## One-Sentence Summary

Oxetacaine (oxethazaine) is classified as a topical local anaesthetic, but no confirmed original indication or mechanism-of-action data is available in this evidence pack. The TxGNN model's top prediction is **Primary Release Disorder of Platelets**, with a very high raw score (**97.89%**), but this is currently supported by **0 clinical trials** and **0 publications** — and the model's own rationale explicitly flags this as a likely spurious knowledge-graph correlation rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in available data (drug is generally classified as a topical local anaesthetic) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of TFDA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (flagged as a High-severity data gap — DG002). No confirmed original indications are recorded for this drug in the evidence pack either, so no direct pharmacological bridge between an established use and the predicted indication can be constructed.

More importantly, the evidence pack's own mechanistic rationale for this candidate states there is "no known pharmacological pathway involving platelet granule release or aggregation" for a topical surface anaesthetic, and characterizes the high TxGNN score as a possible **spurious knowledge-graph connection** rather than a biologically grounded link.

This assessment is reinforced by a pattern across the full top-10 prediction list: six of the ten highest-scoring candidates (ranks 4–9) are anatomically unrelated "polyp" diagnoses — uterine, vocal cord, middle ear, ureter, frontal sinus, and external auditory canal. Because these conditions share no plausible common mechanism with a topical local anaesthetic, this clustering strongly suggests the predictions are driven by a shared node or embedding artifact in the knowledge graph rather than independent biological signals. The remaining top predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia) are inherited platelet-receptor disorders with no described mechanistic link to oxetacaine either.

## Other Predicted Indications (Same Evidence Tier)

All top-10 predictions share the same evidence status — L5, Hold, zero trials, zero literature:

| Rank | Predicted Indication | TxGNN Score |
|------|----------------------|-------------|
| 2 | Pseudo-von Willebrand disease | 97.43% |
| 3 | Glanzmann thrombasthenia | 97.30% |
| 4 | Uterine polyp | 97.29% |
| 5 | Polyp of vocal cord | 97.16% |
| 6 | Polyp of middle ear | 97.14% |
| 7 | Polyp of ureter | 97.09% |
| 8 | Polyp of frontal sinus | 97.08% |
| 9 | Polyp of external auditory canal | 97.05% |
| 10 | Epulis (gingival growth) | 97.05% |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Oxetacaine is not currently marketed in Taiwan — the evidence pack records zero TFDA registrations and no licensed products, so no dosage form or approved indication text is available.

---

## Safety Considerations

Please refer to the TFDA-approved Professional Information (PI) for safety information. Report adverse drug reactions to TFDA.

*(Note: TFDA label warnings/contraindications are recorded as a **Blocking** data gap — DG001 — meaning this candidate cannot yet pass initial safety screening.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support, no confirmed mechanism of action, and the model's own generated rationale identifies the top prediction cluster as a likely knowledge-graph artifact rather than a genuine pharmacological signal. The drug is also not currently marketed in Taiwan, and the safety/label data gap is classified as Blocking, so this candidate cannot proceed to safety screening in its current state.

**To proceed, the following is needed:**
- TFDA-approved Professional Information (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirmed mechanism of action via DrugBank or equivalent pharmacological source (DG002)
- Independent mechanistic review to determine whether the top-ranked predictions (especially the six-way polyp cluster) reflect a real signal or a knowledge-graph embedding artifact
- Preclinical or in-vitro evidence before any clinical evidence-generation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

