---
layout: default
title: Dexpanthenol
parent: Model Prediction Only (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexpanthenol: predicted new indication Anorectal stricture (evidence level L5). Approved use: Paralytic ileus, intestinal obstruction, gastroparesis, atopic eczema…"
monitor_inn: "Dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "exanthem (disease)", "punctate epithelial keratoconjunctivitis", "acute urate nephropathy", "diversion colitis", "indeterminate colitis"]
---

# Dexpanthenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Dexpanthenol: From Paralytic Ileus and Skin Conditions to Anorectal Stricture

## One-Sentence Summary

Dexpanthenol is a precursor of pantothenic acid (vitamin B5), originally associated with gastrointestinal motility disorders (such as paralytic ileus and gastroparesis) and skin conditions (such as dermatitis and eczema).
The TxGNN model predicts it may be effective for **anorectal stricture** (top-ranked prediction), but there are currently **no clinical trials and no publications** supporting this specific prediction.
The only prediction with clinical trial evidence is the lower-ranked **exanthem (rash)**, which has **1 Phase 3 trial**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paralytic ileus, intestinal obstruction, gastroparesis, atopic eczema, dermatitis, and other skin diseases (from the knowledge graph; no SAHPRA approved indication text available) |
| Predicted New Indication | Anorectal stricture |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexpanthenol is a precursor of pantothenic acid (vitamin B5) and coenzyme A. It supports epithelial repair, skin barrier function and wound healing.

Its original indications cover both gastrointestinal motility disorders and skin or mucosal conditions. A plausible, but unverified, link is that its epithelial repair and wound-healing properties could support mucosal healing in anorectal tissue. This remains a hypothesis: no trials or literature were available to test it. A stricture is a structural narrowing, and a healing-supportive agent is not clearly a disease-modifying treatment for it.

**Other predictions in the top 10** (all L5 unless noted):

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Imperforate anus | 99.71% | L5 | Congenital malformation treated surgically; at most postoperative skin care |
| 3 | Anal polyp | 99.62% | L5 | No clear mechanistic rationale |
| 4 | Vulvar inverted follicular keratosis | 99.60% | L5 | Some overlap with existing keratosis indications; benign lesion usually excised |
| 5 | Proctitis | 99.60% | L5 | Plausible mucosal-protective role |
| 6 | Exanthem | 99.60% | L3 | One Phase 3 RCT in a related rash-prevention setting |
| 7 | Punctate epithelial keratoconjunctivitis | 99.34% | L5 | Ophthalmic use for corneal healing in some regions; no data here |
| 8 | Acute urate nephropathy | 99.00% | L5 | No evident mechanism; likely a graph artifact |
| 9 | Diversion colitis | 98.87% | L5 | Speculative |
| 10 | Indeterminate colitis | 98.87% | L5 | Speculative; same score as diversion colitis |

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (anorectal stricture). The only trial in the compiled data relates to the rank 6 prediction, exanthem:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Phase 3 | Completed | 160 | Randomized, double-blind comparison of Bepanthen® cream vs cetomacrogol cream for preventing papulopustular eruption in patients receiving EGFR inhibitors (BeCet). Primary aim is to reduce the incidence of grade ≥2 skin side effects. Results were not provided. |

This trial concerns drug-induced rash prevention, which is only an indirect match to exanthem as classified. Its exact outcomes need to be verified before it can be relied on.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36/22.1/0508 | Cernevit | Infusion | Not available in the compiled data |

Cernevit is registered as a single-ingredient, valid registration in an injectable form. No topical, oral or ophthalmic dexpanthenol registration was identified, so route compatibility with the predicted indications (such as anorectal or ocular use) has not been established. Essential Medicines List (EML) status was not available.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: hemophilia is listed as a contraindicated condition in the TxGNN knowledge graph. This comes from graph data, not from product label text, and should be checked against the approved Professional Information.
- **Drug Interactions**: no interactions were found in the queried data.

Otherwise, please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (anorectal stricture) rests solely on a model score, with no clinical trials or publications, and the mechanistic link is speculative. The only Phase 3 evidence (NCT01136005) relates to rash prevention, not to the predicted anorectal indication. It may merit follow-up as a separate research question for exanthem or drug-induced dermatitis.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is currently a blocking gap for safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Results and full indication details for NCT01136005
- A literature search on dexpanthenol in anorectal and mucosal healing
- Confirmation of available topical or rectal formulations in South Africa, since the only registration is an infusion product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

