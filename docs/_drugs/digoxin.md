---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Digoxin: From Heart Failure/Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside historically used to manage heart failure and rate control in atrial fibrillation (note: this evidence pack does not contain South African licensing text for the original indication — this classification reflects widely established pharmacology, not a SAHPRA-sourced label). The TxGNN model's top-ranked new-indication prediction is **Prinzmetal angina** (vasospastic angina), but this signal is currently supported by **0 clinical trials** and only **2 general, non-specific review articles**, and the accompanying mechanistic review flags it as a probable false positive with a possible relative contraindication rather than a therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (no South African licence text available); widely known internationally for heart failure and atrial fibrillation |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, source-verified mechanism-of-action data for digoxin is not available in this evidence pack (flagged as a High-severity data gap). Based on established pharmacology, digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump, producing a positive inotropic (increased contractility) and negative dromotropic (slowed AV conduction) effect. It is used clinically for heart failure and ventricular rate control in atrial fibrillation.

Prinzmetal angina, however, is caused by transient coronary artery vasospasm rather than by impaired myocardial contractility or conduction. Digoxin has no known vasodilatory or anti-spasmodic action on coronary smooth muscle, so its established mechanism does not naturally extend to this indication.

Critically, the evidence pack's own mechanistic review goes further: it notes that digoxin can *increase* myocardial oxygen consumption and arrhythmia risk, which is potentially unfavourable — and even relatively cautioned against — in vasospastic angina. The high TxGNN score most likely reflects an indirect graph relationship (e.g., shared "angina"-adjacent nodes in the knowledge graph) rather than genuine pharmacological plausibility. This prediction should therefore be treated as a low-confidence, model-only signal rather than a mechanistically supported hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiologica et Pharmacologica Bulgarica | General review of circadian rhythms and chronopharmacology in antihypertensive treatment; does not specifically address digoxin or Prinzmetal angina |
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Review | Chinese Medical Sciences Journal | Re-evaluates the mechanism of angina decubitus (effort angina) in 30 hospitalised patients; focuses on hemodynamic monitoring findings and does not evaluate digoxin therapy |

**Note:** Both articles are classified as low-relevance/Tier 3 reviews with "relevance: pending" status in the source data. Neither directly evaluates digoxin for Prinzmetal (vasospastic) angina; they were likely surfaced by keyword co-occurrence rather than topical relevance.

---

## South Africa Market Information

Digoxin currently has no SAHPRA registrations recorded in this evidence pack (0 licences; market status: Not Marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/SAHPRA package-insert warnings and contraindications for digoxin are recorded as a **Blocking** data gap in this evidence pack — see Conclusion below. This absence prevents a full safety pre-screen (S1) at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence Level is L5 — this is a model-only prediction with no supporting clinical trials and no directly relevant literature. The mechanistic review accompanying this candidate actively argues against plausibility for Prinzmetal angina and flags a possible safety concern (increased myocardial oxygen demand/arrhythmia risk in a vasospastic-angina population) rather than supporting benefit.
- For context, all six TxGNN-predicted indications for digoxin in this evidence pack (Prinzmetal angina, duodenal obstruction, duodenal ulcer, duodenogastric reflux, "obsolete" ischemic stroke susceptibility, and hypoalphalipoproteinemia) were independently scored Evidence Level L5 with a Hold recommendation — none currently has clinical-trial or strong mechanistic support, and two (duodenogastric reflux, obsolete ischemic stroke susceptibility) have no supporting literature at all.
- Digoxin is not currently marketed in South Africa (0 SAHPRA registrations), and package-insert warnings/contraindications are a **Blocking** data gap, which independently prevents progression to a safety pre-screen regardless of the efficacy signal.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings and contraindications) — currently a Blocking data gap (DG001)
- Verified mechanism-of-action data from DrugBank or an equivalent source — currently a High-severity data gap (DG002)
- Dedicated pharmacological or preclinical studies evaluating digoxin specifically in coronary vasospasm/Prinzmetal angina, given the complete absence of clinical trial evidence
- Reassessment of market/registration status if South African availability of digoxin changes
- Given the mechanistic concerns raised, this candidate should be deprioritised relative to any higher-plausibility signals identified for this drug in future evidence updates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

