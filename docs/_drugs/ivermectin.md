---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Strongyloidiasis, onchocerciasis"
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "congenital candidiasis", "neonatal candidiasis", "candida glabrata", "postmenopausal atrophic vaginitis", "candidiasis, invasive", "vulvitis"]
---

# Ivermectin
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

# Ivermectin: From Strongyloidiasis and Onchocerciasis to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is an antiparasitic drug, originally used to treat **strongyloidiasis** and **onchocerciasis**.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but this is a model prediction only: **no clinical trials** and **no relevant publications** support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Strongyloidiasis, onchocerciasis (from the knowledge graph; the SAHPRA registration entry carries no indication text) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ivermectin is generally understood to act on glutamate-gated chloride channels in invertebrates, which is why it works against parasites such as *Strongyloides* and *Onchocerca*.

Fungi such as *Candida* lack these targets, so a plausible antifungal mechanism is **not established**. The high score (99.95%) most likely reflects network similarity within the knowledge graph rather than a biological rationale. The prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern. Most are candidiasis-related conditions or vulvovaginal conditions (for example esophageal, congenital, neonatal and invasive candidiasis, vulvovaginitis and vulvitis). All are L5, with no supporting trials. Two are especially doubtful:
- **Postmenopausal atrophic vaginitis** is driven by oestrogen deficiency, not infection.
- **Candida glabrata** is a pathogen name, not a clinical indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications directly support ivermectin for vulvovaginal candidiasis. The only papers linked to the broader candidiasis predictions concern ivermectin's existing antiparasitic uses and give no antifungal evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | Case report | BMJ Case Reports | Disseminated strongyloidiasis after prolonged corticosteroid treatment. This is the approved indication, not candidiasis (linked to the esophageal candidiasis prediction). |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | Case report | Australas J Dermatol | Oral ivermectin cleared crusted scabies in two immunocompromised children, one with chronic mucocutaneous candidiasis. Scabies, not candidiasis, was treated. At most this is an indirect safety observation (linked to the congenital candidiasis prediction). |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 49/13.12/0906 | Soolantra | Cream | Not available in the data compiled for this report |

Soolantra is a topical cream registered as a single-ingredient product. No oral ivermectin registration appears in the data compiled for this report. This matters because the original indications (strongyloidiasis, onchocerciasis) are conventionally treated with oral ivermectin. Essential Medicines List status was not available in the data.

## Safety Considerations

- **Knowledge-graph contraindication associations**: loiasis and filariasis. These come from the TxGNN knowledge graph, not from SAHPRA label text.
- **Drug Interactions**: The interaction query returned 100 interacting drugs. Examples flagged as **Moderate** include:
  - Warfarin and dicoumarol (anticoagulants)
  - Clarithromycin
  - Aprepitant
  - Cobicistat
  - Deferasirox
  - Fostamatinib
  - Ethanol
  - Radioactive iodide (I-123, I-131)
  - Topical abametapir

  Several others (for example omeprazole, lansoprazole, prednisone, prednisolone, dexamethasone, ranitidine, famotidine, heparin and ursodeoxycholic acid) have an unclassified severity level.
- **Special populations**: Neonatal and young-infant use is not established for ivermectin, which is relevant to the neonatal and congenital candidiasis predictions.

For full warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials or relevant publications, and no plausible antifungal mechanism, since fungi lack ivermectin's known invertebrate targets. Established antifungal therapies already exist for candidiasis.

**To proceed, the following is needed:**
- In vitro data showing ivermectin activity against *Candida* species
- Detailed mechanism of action data, and a mechanistic rationale for antifungal or other vulvovaginal effects
- Confirmation of the SAHPRA PI warnings and contraindications for Soolantra
- An assessment of whether topical ivermectin can reach the intended site of infection (route compatibility has not yet been evaluated)
- Preclinical and early-phase clinical evidence before any further evaluation
- Drug-interaction review, especially for patients on anticoagulants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

