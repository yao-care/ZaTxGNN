---
layout: default
title: Zinc Oxide
parent: Model Prediction Only (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Zinc Oxide
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

# Zinc Oxide: From an Unspecified Original Indication to Acne

## One-Sentence Summary

Zinc oxide is a widely used zinc compound, and the SAHPRA records supplied do not state an approved indication for it.
The TxGNN model predicts it may be effective for **acne**, but there are **0 clinical trials** and only **7 publications** (mostly reviews and preclinical work) supporting this direction.
This is a model-driven hypothesis with indirect evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied SAHPRA records |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 (literature reviews and preclinical studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc oxide is a zinc compound already used in topical dermatology products, and this lowers the barrier for a skin-related use.

Zinc has documented anti-inflammatory and antibacterial activity relevant to acne. This includes suppression of *Cutibacterium acnes* and modulation of sebum and inflammation. Zinc oxide nanoparticles also show antibacterial effects in preclinical work.

The link is indirect. The main review covers zinc in general, not zinc oxide specifically. No human trial of zinc oxide for acne was found, so the prediction remains a research question rather than an established use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acne.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29193602](https://pubmed.ncbi.nlm.nih.gov/29193602/) | 2018 | Review | Dermatol Ther | Reviews zinc in acne treatment as an alternative to topical and systemic agents that cause adverse effects. It covers zinc in general, not zinc oxide specifically. |
| [21342155](https://pubmed.ncbi.nlm.nih.gov/21342155/) | 2011 | Review | Int J Dermatol | Nanoparticles such as zinc oxide and titanium dioxide are used in skin care products. Nano-preparations are under investigation for acne and other skin conditions. |
| [29284390](https://pubmed.ncbi.nlm.nih.gov/29284390/) | 2018 | Review (preclinical focus) | Curr Med Chem | Nanoparticle-coated textiles with antimicrobial properties for wounds and skin diseases such as acne. |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical study (split-face, small) | Skin Res Technol | Split-face assessment in mild inflammatory catamenial acne. The available abstract does not show a zinc oxide intervention. |
| [36888703](https://pubmed.ncbi.nlm.nih.gov/36888703/) | 2023 | Preclinical | Sci Adv | Ultrasound-responsive microneedle patch with zinc porphyrin-based nanoparticles for acne-related bacterial infection. |
| [41033952](https://pubmed.ncbi.nlm.nih.gov/41033952/) | 2025 | Preclinical | Sci Bull | ZnO@Viologen-COF heterojunction that selectively modulates skin microbiota, triggered by *C. acnes* respiration. |
| [31322532](https://pubmed.ncbi.nlm.nih.gov/31322532/) | 2019 | Formulation development | Georgian Med News | Development of powder formulas for acne treatment. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H990 (OM) | Achromide | Ointment | Not stated in record |
| G2011 (OM) | Biohist | Syrup | Not stated in record |
| E512 | Anugesic | Suppository | Not stated in record |
| 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated in record |

Approved indication text and manufacturer are blank for all four entries. Some listed products (for example, a vial presentation) do not look like typical zinc oxide products, so the registration mapping should be verified against the SAHPRA register. Essential Medicines List (EML) status is not available in the supplied data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points from the supplied data:
- A drug-interaction query returned no records. This means no data were found, not that no interactions exist.
- Any topical use in a new indication would need formulation and skin-tolerability review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.86%), but there are no clinical trials for acne. The literature is limited to a general zinc review, small or non-specific studies and preclinical work. The SAHPRA safety information is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking gap)
- Mechanism of action data, for example from the DrugBank API
- Verification of the four SAHPRA registrations, including approved indications and manufacturers
- Human clinical evidence for zinc oxide itself in acne, since current evidence covers zinc in general
- Route and formulation compatibility assessment for a topical acne product

**Other predictions in the pack:** All are on Hold. Otitis externa has only in vitro veterinary antifungal evidence (Malassezia), and post-bacterial disorder has only indirect dental antibacterial trials. The rest (anorectal stricture, anal polyp, papillary conjunctivitis, post-infectious vasculitis, Chagas cardiomyopathy, infection-related haemolytic uraemic syndrome, post-infectious syndrome) have no supporting evidence or only unrelated keyword hits.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

