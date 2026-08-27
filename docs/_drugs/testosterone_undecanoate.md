---
layout: default
title: Testosterone Undecanoate
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
---

# Testosterone Undecanoate
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

# Testosterone Undecanoate: From Androgen Replacement Therapy to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Testosterone undecanoate is an androgen used generally for testosterone replacement in male hypogonadism and related deficiency states. The TxGNN model's top-ranked prediction is **Homozygous Familial Hypercholesterolemia (HoFH)**, but **no clinical trials and no literature** currently support this specific prediction — the evidence pack itself flags the score as a probable embedding false positive. A better-supported candidate lower on the list, **Androgen Insensitivity Syndrome**, has 2 supporting publications and a direct mechanistic rationale (see "Other Candidate Indications" below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Androgen replacement therapy (general use); no SAHPRA-approved indication text on file — not marketed in South Africa |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 98.73% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for testosterone undecanoate is not available in this evidence pack (flagged as a High-severity data gap requiring a DrugBank lookup). Based on known pharmacology, testosterone can modestly lower HDL cholesterol and affect lipid metabolism generally, which is the likely basis for an embedding-level association picked up by the model.

However, this lipid effect has **no direct mechanistic connection** to the LDL-receptor/PCSK9 pathway that underlies HoFH pathology, which is a genetic disorder of LDL clearance rather than a disorder of androgen signalling. The evidence pack's own assessment explicitly flags the 98.73% TxGNN score as a **suspected embedding false positive**: there is no mechanistic hypothesis, no clinical trial, and no literature supporting testosterone undecanoate for HoFH.

For this reason, this candidate does not currently meet the bar for further evaluation as an HoFH therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## Other Candidate Indications (Ranks 2–10)

Because this evidence pack evaluated 10 candidate indications for testosterone undecanoate, the second-ranked candidate is notably better supported than the top TxGNN score and is included here for completeness:

**Rank 2 — Androgen Insensitivity Syndrome (AIS)** — Score 95.72%, Evidence Level L4, Decision Stage S1, Recommendation: **Research Question**

Testosterone acts directly on the androgen receptor (AR), and AIS is itself an AR-signalling defect. Oral testosterone undecanoate has been studied for inducing virilization in partial AIS and for hormone-replacement purposes in complete AIS. Response is expected to differ sharply by AIS subtype (partial vs. complete), since complete AR loss-of-function would not respond to testosterone supplementation.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39039878](https://pubmed.ncbi.nlm.nih.gov/39039878/) | 2024 | Cohort/Case series | Zhonghua Er Ke Za Zhi (Chinese J Pediatrics) | Efficacy and safety of oral testosterone undecanoate in children with AIS (self-controlled study, Beijing Children's Hospital, 2009–2021) |
| [8246276](https://pubmed.ncbi.nlm.nih.gov/8246276/) | 1993 | Cohort | J Sex Marital Ther | Double-blind cross-over of oral testosterone undecanoate (Andriol) vs. placebo in gonadectomized complete testicular feminization patients; psychosexual and hormonal outcomes |

**Rank 3 — Leydig Cell Hypoplasia due to LH Resistance** (94.50%, L4, S1, Research Question): LH-receptor resistance prevents endogenous testosterone production — replacement is the direct physiological correction, but no trials/literature were found in this search.

**Rank 4 — 46,XY Disorder of Sex Development due to Impaired Androgen Production** (93.67%, L4, S1, Research Question): Disease is defined by androgen production failure; replacement is mechanistically direct, but unsupported by trials/literature in this dataset.

**Ranks 5–10** (Fragile X carrier symptoms, blepharophimosis-related syndromes, telecanthus, ovarian hyperstimulation syndrome, partial trisomy/tetrasomy 5p) — all Evidence Level L5, Decision Stage S0, **Hold**: no mechanistic link to androgen signalling and no supporting trials or literature.

---

## South Africa Market Information

Testosterone undecanoate is **not currently registered with SAHPRA** (0 licenses on file). No local Professional Information is available for this product.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HoFH) has no mechanistic support, no trials, and no literature, and is explicitly flagged in the evidence pack as a likely model artifact. The drug is also not currently marketed in South Africa, so no local safety or indication data exists to support evaluation.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism of action data via DrugBank — currently a High-severity data gap
- If pursuing repurposing research, prioritize the better-supported **Androgen Insensitivity Syndrome** candidate (Rank 2) over HoFH, including subtype-specific (partial vs. complete AIS) response data
- Independent mechanistic review to confirm or rule out the HoFH signal before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

