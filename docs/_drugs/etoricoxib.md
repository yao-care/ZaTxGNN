---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: From NSAID Pain/Inflammation Therapy to Migraine Disorder

## One-Sentence Summary

Etoricoxib is a selective COX-2 inhibitor of the NSAID class; its original approved indication and detailed mechanism-of-action documentation are not on record in this evidence pack (flagged as data gaps). The TxGNN model predicts it may be effective for **Migraine Disorder**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a knowledge-graph inference only, with no direct evidence found in ClinicalTrials.gov, ICTRP, or PubMed searches specific to this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (no licenses or original indication data available; flagged as Blocking data gap DG001) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for etoricoxib is not available in this evidence pack (data gap DG002). Based on the information that is available, etoricoxib is known to be a selective COX-2 (cyclooxygenase-2) inhibitor within the NSAID class. Its role in reducing prostaglandin-mediated inflammation is well established for pain and inflammatory conditions in clinical practice.

The mechanistic rationale offered for the migraine prediction is that COX-2 inhibition could theoretically reduce prostaglandin-mediated vascular inflammation implicated in migraine attacks, drawing a parallel to the existing clinical practice of using other NSAIDs for acute migraine treatment. This is a plausible pharmacological hypothesis, but it should be treated as **class-level reasoning by analogy**, not as evidence specific to etoricoxib in migraine.

Critically, this analogy is not yet supported by any direct data: targeted searches against ClinicalTrials.gov, WHO ICTRP, and PubMed for "etoricoxib AND migraine disorder" each returned zero results. A related literature set does exist for a different candidate in this same prediction set — "migraine with or without aura, susceptibility to" (rank 3) — but those 20 publications are predominantly epilepsy genetics/neuroinflammation studies exploring shared pathways between epilepsy and migraine susceptibility, not etoricoxib efficacy studies, and are therefore only indirect background context.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Etoricoxib is **not currently registered with SAHPRA** in South Africa — the evidence pack records 0 licenses/registrations and a market status of "Not marketed." No product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: key warnings, contraindications, and drug-interaction data for etoricoxib are flagged in this evidence pack as a Blocking data gap (DG001) — TFDA/SAHPRA label warnings could not be retrieved, which by itself is sufficient to block progression to the safety pre-assessment stage regardless of efficacy evidence.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero clinical trials and zero literature citations specifically supporting etoricoxib for migraine disorder — the prediction rests entirely on a TxGNN knowledge-graph score (Evidence Level L5) plus a plausible-but-unverified class-level mechanistic analogy to other NSAIDs. Independently, the safety data gap (DG001, Blocking) means this candidate cannot yet even enter the S1 safety pre-assessment stage, and the drug is not currently marketed or registered in South Africa.

**To proceed, the following is needed:**
- SAHPRA-approved PI warnings and contraindications (resolve DG001, Blocking)
- Etoricoxib's original approved indication(s) and detailed mechanism of action via DrugBank API (resolve DG002)
- A dedicated literature/trial search specifically targeting "etoricoxib AND migraine" beyond the current zero-hit queries, to confirm whether any unindexed or recent evidence exists
- Consider whether **"headache disorder"** (rank 9 in this same evidence pack — 2 clinical trials and 5 publications, including case reports of etoricoxib efficacy in indomethacin-responsive headache syndromes) is a better-evidenced candidate to prioritize ahead of migraine disorder specifically
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

