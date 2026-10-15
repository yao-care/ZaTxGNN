---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic antagonist originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (from the knowledge graph; the SAHPRA registration entries contain no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, alfuzosin is a uroselective alpha-1 adrenergic antagonist, and its efficacy in BPH is established through relaxation of smooth muscle in the prostate and bladder neck.

The predicted link to Ambras syndrome is **not mechanistically supported**. Ambras syndrome is a rare genetic disorder associated with chromosome 8q rearrangements that affect regulation of *TRPS1*. No plausible pathway connects alpha-1 blockade to this condition. The very high score (~0.99999) most likely reflects proximity in the knowledge graph to hair-growth-related nodes rather than true therapeutic potential.

Other top-ranked predictions show the same pattern. Most are rare genetic hair, skin or developmental disorders (hypertrichosis, hair shaft abnormalities, trichomegaly, hypotrichosis, Dandy-Walker-related syndromes), and none has any trial or literature support. Allergic urticaria is also predicted, but hypersensitivity reactions are a possible alfuzosin adverse effect, which argues against that use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/5.2/0740 | Alfuwin XL | Tablet (oral) | Not stated in the data compiled for this report |
| Reg. No. A40/5.2/0392 | Rantral MR | Tablet (oral) | Not stated in the data compiled for this report |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status could not be determined from the available data.

## Safety Considerations

**Contraindications / conditions of concern (from knowledge-graph drug-disease edges, not label text):**
multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorders, long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, gallbladder disease, and intraoperative floppy iris syndrome.

**Drug Interactions** (100 interactions recorded; selected examples from the DDInter-sourced list):
- **Major:** cisapride, clarithromycin, dolasetron
- **Moderate:** famotidine, aprepitant, bisacodyl, bupropion, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, granisetron, levofloxacin, and others
- **Minor:** cimetidine

Many of these relate to QT prolongation or CYP3A4 inhibition, consistent with the QT-related conditions listed above.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5) and no plausible mechanism. The high TxGNN score appears to be a knowledge-graph artifact. Alfuzosin's vasodilatory and hypotensive effects, together with the QT-related cautions, add risk without any demonstrated benefit.

**To proceed, the following is needed:**
- Mechanism of action data for alfuzosin, to allow proper mechanistic analysis
- The SAHPRA-approved package insert (PI), to confirm warnings, contraindications and approved indications
- Preclinical or mechanistic evidence linking alpha-1 blockade to hair follicle biology or the *TRPS1* pathway
- Route and formulation compatibility assessment for the proposed new indication
- Review of the other predictions only if supporting evidence emerges; none currently has any
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

