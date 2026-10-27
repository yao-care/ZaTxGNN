---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 233
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Finasteride: From Benign Prostatic Hyperplasia to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **hypertrichosis** (the highest-ranked prediction, Ambras-type hypertrichosis universalis congenita, is covered in the notes below). However, there are currently **0 clinical trials** and only **4 general publications** (narrative reviews and a methods paper), so the prediction rests almost entirely on computational inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (no approved indication text is available in the SAHPRA records compiled for this report) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita (rank 1); hypertrichosis is rank 2 and is the one with literature |
| TxGNN Prediction Score | 99.99% (rank 1 prediction); 99.99% (hypertrichosis) |
| Evidence Level | L5 (Ambras type); L4 (hypertrichosis) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on established pharmacology, finasteride is a type II 5-alpha-reductase inhibitor that lowers dihydrotestosterone (DHT). This is how it works in BPH and in male pattern hair loss.

**Ambras type hypertrichosis universalis congenita (rank 1):** This is a congenital condition linked to chromosome 8q rearrangements affecting TRPS1 regulation. It is not primarily androgen-driven. The very high TxGNN score likely reflects closeness to hair-related phenotypes in the knowledge graph rather than a validated mechanism. No trials or literature support it.

**Hypertrichosis (rank 2):** DHT drives terminal hair growth in androgen-sensitive follicles, which gives a plausible rationale for androgen-dependent hirsutism. Hypertrichosis, however, is typically androgen-independent (congenital, drug-induced or metabolic), so the mechanistic fit is weak.

**Other predictions (ranks 3-6):** These are malformation syndrome with odontal/periodontal component, syndrome with Dandy-Walker malformation, isolated genetic hair shaft abnormality, and familial isolated trichomegaly. None has a credible mechanistic link to DHT suppression, and none has trials or literature. They appear to be knowledge-graph artifacts. Finasteride is also contraindicated in pregnancy because of the risk to male fetal genital development, which is relevant to any congenital-syndrome indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The four publications retrieved for hypertrichosis are narrative reviews or a methods paper. They provide indirect context only and no controlled evidence of finasteride efficacy in hypertrichosis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de Dermatologie et de Vénéréologie | Hypertrichosis occurs in non-androgen-dependent areas, unlike hirsutism. Adult cases are often drug-induced (minoxidil, ciclosporin, diazoxide, glucocorticosteroids), metabolic or paraneoplastic. |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Finasteride is cited for male pattern hair loss; laser-assisted hair removal is cited for hypertrichosis and hirsutism. |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Reviews treatment advances for androgenetic alopecia and hirsutism, including oral treatment of male pattern hair loss. |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods/Technology | Der Hautarzt | Describes TrichoScan, a digital hair analysis tool for monitoring hair density, diameter, growth rate and anagen/telogen ratio. |

## South Africa Market Information

Finasteride is available in South Africa as oral tablets. No approved-indication text or manufacturer information is available in the data compiled for this report. Essential Medicines List (EML) status is not available in the compiled data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/21.12/0594 | Finasteride 1 Unicorn | Tablet | Not available |
| Reg. No. 43/21.12/0055 | Profina | Tablet | Not available |
| Reg. No. 27/21.12/0069 | Proscar | Tablet | Not available |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** liver disease and gallbladder disease. These come from drug-disease relationships in the TxGNN knowledge graph and should be checked against the registered label.
- **Pregnancy:** Finasteride risks male fetal genital development. This is established pharmacology rather than data from the compiled records, and it is especially relevant to congenital-syndrome indications.
- **Drug interactions:** The interaction screen returned 100 potential interacting drugs, but none has a severity grade (all are "Unknown"). Examples include calcitriol, doxycycline, clotrimazole, famotidine, acetylsalicylic acid, bupropion, omeprazole, pantoprazole, metformin, glimepiride and morphine. These should not be read as confirmed clinically significant interactions.

SAHPRA package insert warnings and contraindications have not been obtained. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top predictions (Ambras-type hypertrichosis and hypertrichosis) have a weak or speculative mechanistic fit, because these conditions are largely not androgen-driven. No clinical trials exist, and the only literature is indirect narrative reviews. The remaining four predictions have no supporting evidence at all.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) warnings and contraindications, as safety screening cannot proceed without them
- Detailed mechanism-of-action data
- Controlled clinical or case-series evidence of finasteride efficacy in hypertrichosis
- Clarification of whether an androgen-dependent condition such as hirsutism is a more appropriate target than hypertrichosis
- Review of the DDI findings with severity grading
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

