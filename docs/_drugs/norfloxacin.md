---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: From Antibacterial Use to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is a fluoroquinolone-class antibacterial agent (detailed original indication and mechanism-of-action data are not available in this evidence pack). The TxGNN model predicts it may be effective for **Hyperamylasemia**, but this ranking is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph score with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no license records available) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Norfloxacin is not available in this evidence pack. Norfloxacin is generally known as a fluoroquinolone-class antibacterial agent (DNA gyrase/topoisomerase IV inhibitor), but no original-indication or MOA record was returned from the source query, so the mechanistic basis cannot be independently verified here.

For the top-ranked prediction, hyperamylasemia, the evidence pack's own rationale is explicit: there is **no plausible mechanistic link**. The high TxGNN score (0.997) reflects a strong knowledge-graph connection between the drug and disease nodes, but no supporting clinical trial, observational study, or mechanistic literature was found. Hyperamylasemia (elevated blood amylase) is typically related to pancreatic, salivary gland, or renal pathology, and there is no known pharmacological pathway connecting fluoroquinolone antibacterial activity to amylase regulation.

Because of this, the prediction should be treated as a hypothesis-generating signal only, not as evidence of therapeutic potential. It would require dedicated preclinical or mechanistic investigation before any further evaluation is warranted.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registration records are available for Norfloxacin in this evidence pack (`total_licenses: 0`, market status: Not marketed). The product does not currently appear to be registered for sale in South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hyperamylasemia) has no clinical trial or literature support and no biologically plausible mechanism — it is a pure model score (Evidence Level L5). Combined with the drug's unregistered market status in South Africa and a blocking gap in PI safety data, there is currently no basis to proceed.

**To proceed, the following is needed:**
- SAHPRA/TFDA-equivalent Professional Information (PI) — package insert warnings, contraindications, and drug interactions (currently a blocking data gap)
- Confirmed mechanism-of-action data from DrugBank or an equivalent authoritative source
- Confirmed original indication(s) for Norfloxacin, since no license record was returned
- Independent mechanistic or preclinical rationale linking fluoroquinolone pharmacology to hyperamylasemia, before any further evaluation

**Note on other candidates in this evidence pack:** Among the 10 predicted indications supplied, rank 10 (**septicemic plague**) has comparatively stronger biological plausibility — same-class fluoroquinolones (ciprofloxacin, levofloxacin) are recognized treatments for *Yersinia pestis* infection, and two supporting animal-study publications were found (Evidence Level L4, decision stage S1, "Research Question"). If this evaluation is being used to prioritize repurposing candidates for Norfloxacin generally, that candidate merits separate consideration rather than the top-ranked TxGNN score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

