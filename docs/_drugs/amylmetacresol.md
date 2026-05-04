---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Topical Antiseptic Use to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol (AMC) is a phenol-derivative topical antiseptic, best known as an active ingredient in antiseptic throat lozenges (e.g., Strepsils), where it disrupts bacterial cell membranes and inhibits enveloped viruses on oropharyngeal mucosal surfaces.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome** — a compressive spinal cord emergency — yet **no clinical trials and no published literature** currently support this direction, and the mechanistic rationale is extremely weak.
Across all 10 predicted indications in this batch, evidence remains at **Level 5** (model prediction only), raising serious concern about knowledge graph structural false positives rather than genuine repurposing candidates.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication; internationally used as a topical oropharyngeal antiseptic |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established general pharmacology, Amylmetacresol is a topical antiseptic agent whose activity is confined to mucosal surfaces — it disrupts bacterial cell membranes and has demonstrated in vitro antiviral activity against enveloped viruses including herpes simplex virus (HSV). Its clinical application is strictly local (oropharyngeal cavity), and no systemic absorption, anti-inflammatory (systemic), neuroprotective, or central nervous system activity has been documented.

Cauda Equina Syndrome is a neurosurgical emergency arising from compression of the cauda equina nerve bundle — most commonly by lumbar disc herniation, spinal tumour, or epidural haematoma — and is managed primarily by urgent surgical decompression. There is no established pharmacological pathway by which a topical mucosal antiseptic could influence neurological decompression, neuroprotection, or spinal cord regeneration. The mechanistic link is, by the evidence pack's own analysis, extremely weak.

The very high TxGNN score (99.99%) most likely reflects indirect multi-hop connections within the knowledge graph — for example, shared "infection" or "inflammation" intermediate nodes linking AMC to neurological conditions — rather than genuine biological relevance. This pattern repeats across all 10 predicted indications in this batch (neurological disorders, a cluster of 6 ocular diseases, gastrointestinal disease, and ciliary body tumours), none of which have a plausible direct mechanistic connection to a topical mucosal antiseptic. This is a known failure mode of graph-based prediction models when a drug node has few direct therapeutic edges but many indirect pathway connections.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Amylmetacresol is **not currently registered with SAHPRA** and has no marketed products in South Africa. No product licences are on record.

Healthcare professionals seeking product information should consult international reference sources where AMC-containing preparations are registered (e.g., British National Formulary; EMA-approved product information for Strepsils and equivalent formulations in the UK and EU).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As this drug is not currently registered in South Africa, consult international reference sources (e.g., British National Formulary, EMA product information) for safety data. Report any adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Amylmetacresol are at Evidence Level L5 (model prediction only, with zero supporting clinical trials or publications). The top-ranked prediction — Cauda Equina Syndrome — has no plausible mechanistic link between a topical mucosal antiseptic and a compressive spinal neurological emergency. The consistent clustering of predictions around neurological, ocular, and gastrointestinal diseases without any supporting evidence strongly suggests knowledge graph structural artefacts (indirect shared nodes) rather than true repurposing signals.

**To proceed, the following is needed:**

- **MOA data**: Obtain full DrugBank pharmacological profile, mechanism of action, and any documented systemic pharmacokinetics for Amylmetacresol
- **SAHPRA & international PI**: Retrieve approved prescribing information from jurisdictions where AMC is registered (UK MHRA, EMA) to fully characterise safety, contraindications, and known indications
- **KG audit**: Investigate knowledge graph structural patterns — specifically audit shared infection and inflammation intermediate nodes — to identify and filter indirect associations before re-ranking predictions
- **Highest-plausibility follow-up (if any)**: Among all 10 predictions, **Infectious Anterior Uveitis** (Rank 7) carries the highest — though still very limited — biological plausibility, given AMC's in vitro anti-HSV activity. Any further investigation should begin here and would minimally require preclinical ocular pharmacokinetic and pharmacodynamic data in animal models before clinical relevance can be assessed
- **No clinical development pathway** should be initiated for any of these 10 indications without first establishing at least Level L4 (preclinical) evidence

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This analysis is based on computational model predictions and should not be used to guide prescribing or treatment decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

