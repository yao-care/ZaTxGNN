---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Adapalene: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
monitor_inn: "Adapalene"
predicted_indications: ["zinc, elevated plasma", "isolated congenital adermatoglyphia", "Beare-Stevenson cutis gyrata syndrome", "demodicidosis of sebaceous gland", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "prolidase deficiency", "drug-induced osteoporosis", "seborrheic dermatitis", "sebaceous gland anomaly", "inherited skin tumor"]
---

# Adapalene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Adapalene: From Acne to Zinc, Elevated Plasma
{: .text-alpha }

## One-Sentence Summary

Adapalene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc** (the top-ranked prediction), but **no clinical trials and no publications** currently support this direction.
The prediction is model output only and should be treated as a hypothesis, not a treatment option.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (from the TxGNN knowledge graph; the SAHPRA registrations carry no indication text) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Adapalene is generally known as a topical retinoid that acts on retinoic acid receptors (RAR-beta/gamma). It normalises follicular keratinisation and has anti-inflammatory effects, which is the basis for its use in acne.

**For the top prediction (elevated plasma zinc), no plausible mechanistic link was identified.** Adapalene is applied to the skin with minimal systemic exposure, and there is no known route by which it would alter plasma zinc. The high score (99.51%) is a statistical output of the model, not supported by trials or literature.

Other predictions, ranked by TxGNN score, are summarised below. Only the two with indirect supporting literature are rated higher than a plain model prediction.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 1 | Zinc, elevated plasma | 99.51% | L5 | No plausible mechanism |
| 2 | Isolated congenital adermatoglyphia | 98.80% | L5 | Developmental genetic condition (SMARCAD1); a topical agent is unlikely to restore ridge patterns |
| 3 | Beare-Stevenson cutis gyrata syndrome | 98.78% | L5 | FGFR2 disorder; link to retinoids is speculative |
| 4 | Demodicidosis of sebaceous gland | 95.45% | L5 | Indirect rationale (overlaps with acne and rosacea); adapalene has no anti-parasitic activity |
| 5 | Pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome | 95.30% | L5 | Acne component may respond; systemic and joint features would not |
| 6 | Prolidase deficiency | 89.33% | L5 | No mechanism linking adapalene to the enzyme defect |
| 7 | Drug-induced osteoporosis | 87.21% | L5 | Direction of effect questionable; systemic retinoids are associated with adverse bone effects |
| 8 | Seborrheic dermatitis | 86.28% | L4 | Biologically plausible, but retrieved literature is indirect |
| 9 | Sebaceous gland anomaly | 85.16% | L4 | Preclinical (rat acne model) evidence only; indication is broad |
| 10 | Inherited skin tumour | 82.92% | L5 | Heterogeneous category; no specific syndrome or evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (elevated plasma zinc). No clinical trials were found for any of the other nine predicted indications either.

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication (elevated plasma zinc).

Literature was found only for two lower-ranked predictions, and all of it is indirect:

| PMID | Year | Type | Journal | Relevant Prediction | Key Findings |
|------|-----|------|------|------|---------|
| [39069843](https://pubmed.ncbi.nlm.nih.gov/39069843/) | 2024 | Randomised, double-blind clinical trial | Ital J Dermatol Venereol | Seborrheic dermatitis (rank 8) | Adapalene 0.3%/benzoyl peroxide 2.5% gel in Korean patients with **acne**, with histopathological and immunohistochemical assessment. Not studied in seborrheic dermatitis. |
| [36102580](https://pubmed.ncbi.nlm.nih.gov/36102580/) | 2022 | Clinical study | J Cosmet Dermatol | Seborrheic dermatitis (rank 8) | Moisturiser (licochalcone A, salicylic acid and others) and facial skin lipids in seborrhoea; does not involve adapalene. |
| [27504089](https://pubmed.ncbi.nlm.nih.gov/27504089/) | 2016 | Case report | Case Rep Dermatol | Seborrheic dermatitis (rank 8) | Localised late-onset Darier's disease presenting as inframammary dermatitis; a mimic of dermatitis, not a test of adapalene. |
| [25217865](https://pubmed.ncbi.nlm.nih.gov/25217865/) | 2014 | Animal model study | J Dermatol Sci | Sebaceous gland anomaly (rank 9) | 0.1% adapalene was effective in a non-inflammatory Kyoto Rhino Rat acne (comedone) model. Preclinical only. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/13.11/0162 | Dapta Cream | Cream | Not available in the data compiled |
| Reg. No. 51/13.12/0911 | Deriva Co | Gel | Not available in the data compiled |

Both registrations are valid, single-ingredient, topical products. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** The TxGNN knowledge graph links adapalene to photoparoxysmal response, photosensitivity disease, exfoliative dermatitis and dermatitis. These are model-derived associations and should be checked against the approved label.
- **Drug Interactions:** 58 potential interactions were identified. All interaction levels are currently graded "Unknown", so their clinical significance is unclassified. Examples include:
  - Antibiotics: doxycycline, minocycline, tetracycline, metronidazole
  - Acid suppressants: omeprazole, pantoprazole, rabeprazole, ranitidine
  - Corticosteroids: prednisone, triamcinolone, budesonide
  - Antihistamines: cetirizine, loratadine, fexofenadine
  - Others: bupropion, clopidogrel, ibuprofen, fluconazole, loperamide, scopolamine

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (elevated plasma zinc) has a high model score but no mechanistic plausibility, no trials and no literature (L5). A topical retinoid with minimal systemic exposure is not expected to alter plasma zinc. Of the other predictions, only seborrheic dermatitis and sebaceous gland anomaly (both L4) have any supporting material, and that material is indirect.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA Professional Information (warnings, contraindications, approved indications), which is currently a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) to support mechanistic analysis
- For seborrheic dermatitis, the most plausible lower-ranked candidate, direct clinical evidence of adapalene use, including tolerability given retinoid irritation
- Classification of the 58 drug interactions, which are currently graded "Unknown"
- Route compatibility assessment, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

