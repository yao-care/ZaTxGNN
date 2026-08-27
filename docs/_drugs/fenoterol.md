---
layout: default
title: Fenoterol
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Fenoterol
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

# Fenoterol: From Bronchodilation to Multiple System Atrophy

## One-Sentence Summary

Fenoterol is a short-acting β2-adrenergic receptor agonist historically used for bronchodilation (e.g., asthma/COPD symptom relief), though formal original-indication and licensing data were not available in this evidence pack. The TxGNN model's top-ranked prediction for repurposing is **Multiple System Atrophy**, but this pairing is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-generated signal with no mechanistic or empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchodilation (β2-adrenergic agonist) — derived from model rationale text; no SAHPRA/formulary licensing data available |
| Predicted New Indication | Multiple System Atrophy |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only, no studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Fenoterol was not available in DrugBank for this evidence pack (data gap, high severity). Based on the repurposing model's own rationale text, Fenoterol is understood as a short-acting β2-adrenergic receptor agonist, primarily used for bronchial smooth-muscle relaxation.

Multiple System Atrophy (MSA), however, is a neurodegenerative disorder whose core pathology is autonomic nervous system degeneration — most notably orthostatic hypotension and dysautonomia. There is no established pharmacological pathway connecting β2-receptor agonism to the neurodegenerative processes underlying MSA. According to the evidence pack's own assessment, this high TxGNN score appears to reflect network-topology inference rather than an interpretable receptor–disease mechanism, and it is not corroborated by any clinical trial or literature evidence to date.

In short: **this is a high-confidence model score without a plausible mechanistic story or any supporting real-world data** — the combination that most warrants caution before any further investment of review resources.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Multiple System Atrophy) carries a high TxGNN score but zero supporting clinical trials, zero literature, and a mechanistic rationale that the evidence pack itself flags as biologically unsupported (decision stage S0). There is no basis to advance this pairing.

**To proceed, the following is needed:**
- Confirmed original indication and SAHPRA/PI data for Fenoterol (currently a blocking data gap)
- DrugBank-sourced mechanism-of-action confirmation
- Any preclinical or case-level evidence specifically linking β2-adrenergic agonism to autonomic/neurodegenerative pathology in MSA, before this candidate is reconsidered

**Note on other candidates in this batch:** Among the 10 predictions reviewed for Fenoterol, the strongest evidentiary support was for **anaphylaxis** (rank 9, score 98.28%, evidence level L4), backed by 11 animal-study publications (1977–1989) showing β2-agonists inhibit antigen-induced histamine release — though all evidence is preclinical and decades old, with no modern or human data. Two candidates — **sinoatrial block** and **sinoatrial node disease** (ranks 7–8) — reached decision stage S1 with a plausible positive-chronotropic rationale but no direct evidence. Conversely, the **open-angle glaucoma** predictions (ranks 4, 6, 10) show a mechanistically *contradictory* signal (β2-agonism may raise rather than lower intraocular pressure) and should be deprioritized. If resources allow further evaluation in this batch, anaphylaxis is the more defensible next research question — not the top-ranked MSA prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

