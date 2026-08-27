---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhoea to Acute Contagious Conjunctivitis

## One-Sentence Summary

> Loperamide is a peripherally-acting μ-opioid receptor agonist internationally used to control diarrhoea. The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely spurious (false-positive) association rather than a plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoea (internationally recognised use; not SAHPRA-registered — see Market Status below) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known pharmacology, loperamide is a peripherally-acting μ-opioid receptor agonist that acts on the myenteric plexus of the gut to slow intestinal motility; it does not cross the blood-brain barrier and has no ocular formulation.

The model's own repurposing rationale explicitly cautions against this prediction: it states there is no known pharmacological connection between loperamide's peripheral antidiarrheal mechanism and acute contagious conjunctivitis (a viral/bacterial or allergic ocular condition), and that the high TxGNN score is most likely explained by node-proximity artefacts in the knowledge graph rather than a genuine biological relationship.

This pattern repeats across all ten of the model's top predictions for this drug — nine of the ten relate to conjunctivitis-family conditions with no cited mechanistic basis, and the second-ranked prediction (amebic dysentery) is flagged as a potential **safety risk rather than a therapeutic opportunity**: international guidance treats loperamide as relatively contraindicated in invasive/inflammatory dysentery because slowing gut motility can delay pathogen/toxin clearance and increase the risk of toxic megacolon. None of the ten candidates in this evidence pack should be read as a credible repurposing signal without independent mechanistic or clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Loperamide is currently **not marketed** in South Africa according to this evidence pack (0 SAHPRA registrations on record).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: this evidence pack flags TFDA/SAHPRA warning and contraindication data as a Blocking data gap — no safety pre-screening (S1) has been possible for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications sit at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the model's own rationale text identifies the top-ranked prediction — along with most of the others — as a likely knowledge-graph artefact rather than a mechanistically plausible signal. One candidate (amebic dysentery) may represent an actual safety risk rather than a therapeutic use. There is no basis to advance any of these candidates at this time.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action data from DrugBank or equivalent source
- Independent literature or preclinical evidence establishing a plausible mechanistic link before any candidate in this set is escalated beyond S0
- If South African market entry is ever considered, a full SAHPRA registration pathway assessment, since loperamide currently has no registered product in this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

