---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Olopatadine
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an H1 antihistamine and mast cell stabiliser, approved for allergic conjunctivitis.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **no clinical trials and no publications** currently support this prediction. It is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conjunctivitis (from the mechanistic notes; the SAHPRA registration data contains no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Olopatadine is known as an H1 antagonist and mast cell stabiliser. Its efficacy in allergic conjunctivitis is established, and it may be applicable to inflammatory ocular surface conditions with an allergic component.

The link to rosacea conjunctivitis is only indirect. Ocular rosacea is driven mainly by meibomian gland dysfunction and inflammation, not by histamine-mediated allergy. Olopatadine might relieve itch or allergic-type symptoms, but there is no evidence it treats the underlying disease. The high score reflects the knowledge-graph model, not clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

Some lower-ranked predictions have limited, indirect literature, summarised below for context:

| Predicted Indication | TxGNN Score | PMID | Year | Type | Key Findings |
|------|------|------|------|------|---------|
| Punctate epithelial keratoconjunctivitis | 98.81% | [22606467](https://pubmed.ncbi.nlm.nih.gov/22606467/) | 2011 | Case report | Limbitis after autologous serum drops in atopic keratoconjunctivitis. Olopatadine was part of background therapy and was not tested. |
| Parasitic conjunctivitis | 97.89% | [34029500](https://pubmed.ncbi.nlm.nih.gov/34029500/) | 2021 | Preclinical | *Acanthamoeba* protein induced allergic conjunctivitis in a model. Antiallergic agents and resolvin D1 were evaluated. |
| Blepharoconjunctivitis | 97.00% | [27911432](https://pubmed.ncbi.nlm.nih.gov/27911432/) | 2016 | Clinical study (design unconfirmed) | Eyelid hygiene before refractive surgery in chronic allergic blepharoconjunctivitis. Olopatadine was not evaluated. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 53/21.5.1/0457 | Ryaltris | Spray | Not stated in the registration data |

The only registered product is a spray, so compatibility with an ocular route for this predicted indication is unconfirmed. Essential Medicines List (EML) status was not available in the Evidence Pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or literature (L5), and the mechanistic link to rosacea conjunctivitis is weak. Safety information from the SAHPRA PI has not yet been reviewed, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Detailed mechanism of action data (for example, from DrugBank)
- Confirmation of the SAHPRA-approved indication and route, and whether an ophthalmic formulation is available in South Africa
- Clinical evidence, at minimum a pilot study or case series, in ocular rosacea
- A comparison against better-supported ocular allergy predictions (punctate epithelial keratoconjunctivitis, blepharoconjunctivitis) as alternative research questions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

