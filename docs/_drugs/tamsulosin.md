---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is an alpha-1 adrenergic blocker, originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no publications** currently support this prediction. It rests on a graph-based model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (from the TxGNN knowledge graph; the SAHPRA records compiled for this report contain no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Tamsulosin is generally known as an alpha-1A/1D adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which is why it is effective in BPH.

For the predicted indication, no plausible mechanism has been established. Ambras syndrome is linked to chromosome 8q regulatory rearrangements affecting *TRPS1*, a genetic cause that alpha-1 blockade is not known to influence. The high score most likely reflects network proximity to other hair-related phenotypes in the knowledge graph rather than a biological rationale. The prediction should therefore be treated as a hypothesis-generating signal only.

The other top-ranked predictions show the same pattern. Examples are hypertrichosis, hair shaft abnormalities, hypotrichosis, alopecia areata, alopecia and migraine with brainstem aura. All are L5 with no trials or supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (Ambras type hypertrichosis universalis congenita).

For the related prediction of general alopecia (rank 9), two publications were retrieved. Neither shows a benefit of tamsulosin:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohort / pharmacovigilance | JAMA Dermatology | Suicidality and psychological adverse events with finasteride, a different drug (5-alpha-reductase inhibitor); not about tamsulosin |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cross-sectional | Cornea | Meibomian gland changes in men with BPH; unrelated to hair loss |

## South Africa Market Information

Eight valid single-ingredient registrations were found. The approved indication text, and the Essential Medicines List (EML) status, were not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/34/0057 | Uriwel | Capsule | Not available |
| Reg. No. 48/34/0855 | Pravlex SR 0,4 mg | Capsule | Not available |
| Reg. No. 56/34/0989 | Urilosin 0,4 | Capsule | Not available |
| Reg. No. A40/34/0317 | Prostaflo SR | Modified-release capsule (listed as "Src") | Not available |
| Reg. No. 56/21.12/1063 | Firsoltam | Listed as "Mrt" | Not available |

The remaining three registrations are Swifsul (55/21.12/0032), Beniprosin SR (A40/34/0211) and Duodart 0.5 mg/0.4 mg (44/21.12/0850). Duodart is listed in the data as a single-ingredient registration, although its strength suggests a dutasteride/tamsulosin combination. This should be verified against the registration record.

## Safety Considerations

**Contraindications and conditions of concern (from knowledge graph associations, not label text):**
multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, and intraoperative floppy iris syndrome (relevant before cataract surgery).

**Drug Interactions** (100 interactions identified; selected examples):
- **Major:** Clarithromycin
- **Moderate:** Bupropion, Aprepitant, Morphine, Cimetidine, Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, Miconazole, Clotrimazole, Eliglustat, Opium

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature and no plausible mechanism. Tamsulosin's hypotension and ejaculatory side effects would be hard to justify in a rare genetic hair condition.

**To proceed, the following is needed:**
- A plausible biological mechanism linking alpha-1A/1D blockade to the *TRPS1*-related pathology of Ambras syndrome
- Mechanism of action data for tamsulosin from DrugBank
- SAHPRA Professional Information (warnings, contraindications and approved indications) to complete the safety screen
- Preclinical or early clinical data in the predicted indication, which is the only route that could raise the evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

