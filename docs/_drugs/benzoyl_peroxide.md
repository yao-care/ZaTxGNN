---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Benzoyl Peroxide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Acne"
monitor_inn: "Benzoyl peroxide"
predicted_indications: ["vulvar inverted follicular keratosis", "2-hydroxyethyl methacrylate sensitization", "acrodermatitis chronica atrophicans", "acne keloid"]
---

# Benzoyl Peroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Benzoyl Peroxide: From Acne and Dermatitis to Vulvar Inverted Follicular Keratosis
{: .text-alpha }

## One-Sentence Summary

Benzoyl peroxide is a topical agent originally used for skin conditions such as acne, seborrheic dermatitis and seborrheic keratosis.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (the knowledge graph also lists atopic eczema, contact dermatitis, seborrheic dermatitis, seborrheic keratosis and granuloma annulare; no approved indication text is recorded in the SAHPRA registrations) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known information, benzoyl peroxide is a topical agent with antibacterial, comedolytic and anti-inflammatory activity in acne, and mechanistically it may be applicable to some follicular and keratinising skin conditions.

Inverted follicular keratosis is a benign lesion related to seborrheic keratosis, which is one of benzoyl peroxide's original indications. A keratolytic or anti-proliferative effect is conceivable. However, no trials or literature support this, and the drug's mechanism is not documented in the data compiled for this report, so the link is speculative. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other top-ranked predictions** were also reviewed. None has trial evidence, and several are mechanistically doubtful:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | 2-Hydroxyethyl methacrylate sensitization | 0.9943 | L5 | Benzoyl peroxide is itself a recognised contact sensitiser, so use here is implausible and potentially harmful. |
| 3 | Acrodermatitis chronica atrophicans | 0.9917 | L5 | A late Lyme disease manifestation treated with systemic antibiotics; no evidence the drug acts on Borrelia. |
| 4 | Acne keloid | 0.9906 | L5 | Plausible overlap with acne, but only indirect evidence exists (see below). |

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvar inverted follicular keratosis. No trials were identified for any of the other top-ranked predictions either.

## Literature Evidence

No literature was retrieved for the lead prediction (vulvar inverted follicular keratosis). Two publications were retrieved for lower-ranked predictions and provide only indirect context:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/) | 2024 | Review (retrospective chart review of 77 Black paediatric patients) | Dermatology Online Journal | Acne vulgaris in children with skin of colour often leads to scarring, keloid formation and post-inflammatory hyperpigmentation. Relevant to the acne keloid prediction (rank 4) only indirectly; it does not address keloidal disease treatment. |
| [25982754](https://pubmed.ncbi.nlm.nih.gov/25982754/) | 2015 | Review | Expert Review of Clinical Pharmacology | Topical anti-acne drugs, including benzoyl peroxide, have low potential for contact sensitisation and for phototoxic or photoallergic reactions. Irritant contact dermatitis is much more frequent. Relevant to the phototoxic dermatitis prediction (rank 7); it suggests the drug may cause rather than treat dermatitis. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 51/13.12/0911 | Deriva Co | Gel (topical) | Not recorded in the data compiled |
| Reg. No. X/13.12/292 | Acneclear | Cream (topical) | Not recorded in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Cytotoxicity

Not applicable. Benzoyl peroxide is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

Label-based warnings, contraindications and drug interaction data were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The knowledge graph, which is not label text, links benzoyl peroxide to the following contraindicated conditions. These should be treated as signals to verify against the PI, not as confirmed label contraindications:

- **Skin and photosensitivity:** photosensitivity disease, photoparoxysmal response, dermatitis, exfoliative dermatitis, skin atrophy
- **Vascular:** telangiectasis, capillary disease, hereditary haemorrhagic telangiectasia, peripheral vascular disease, peripheral arterial disease, intermittent claudication
- **Gastrointestinal:** Crohn disease, Crohn's colitis, inflammatory bowel disease, ulcerative colitis, *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, Addison disease
- **Other:** kidney disease, pyoureter, anogenital human papillomavirus infection, common wart

Practical points from the retrieved literature and rationale: benzoyl peroxide is a recognised contact sensitiser and irritant, which is a particular concern on delicate skin such as the vulva, in neonates, and in photosensitive disorders.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for vulvar inverted follicular keratosis is supported only by the TxGNN model score (0.9992), with no clinical trials or literature (Evidence Level L5). The mechanism is undocumented and the drug is an irritant and sensitiser, which is a concern on vulvar skin. Several other top-ranked predictions are mechanistically implausible or potentially harmful.

**To proceed, the following is needed:**
- Safety information from the SAHPRA PI (warnings and contraindications), which is currently missing and is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Targeted literature search on benzoyl peroxide for inverted follicular keratosis and other keratinising lesions
- Dermatologist review of the plausibility of topical use on vulvar skin, including irritation and sensitisation risk
- Confirmation of the approved indications and EML status of the two registered products (Deriva Co and Acneclear)
- If any prediction is pursued, acne keloid (rank 4) is the most mechanistically plausible candidate for a focused research question, though direct evidence is currently lacking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

