---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Naphazoline
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

# Naphazoline: From Ophthalmic Decongestant to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Naphazoline is an imidazoline alpha-adrenergic agonist and vasoconstrictor, used as an ophthalmic decongestant.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp** with a very high score.
However, there are **0 clinical trials** and **0 relevant publications** for this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ophthalmic vasoconstrictor/decongestant (based on drug class; the registration records do not state an indication) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Naphazoline is known as an imidazoline alpha-adrenergic agonist. It narrows blood vessels, which is how it relieves redness and congestion in the eye.

The link between this action and hair loss is weak. A vasoconstrictor would, if anything, reduce blood flow to the scalp, which is the opposite of established hair-growth agents. The high score most likely reflects proximity to hair-related nodes in the knowledge graph rather than a real pharmacological relationship. It should be treated as a probable model artifact.

The top 10 predictions show the same pattern. Most are hair disorders or rare congenital conditions with no mechanistic link to naphazoline:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 1 | Hypotrichosis simplex of the scalp | 99.83% | L5 | No plausible pathway |
| 2 | Congenital hypotrichosis milia | 99.82% | L5 | Rare genetic disorder |
| 3 | Diffuse alopecia areata | 99.79% | L5 | Autoimmune; no immunomodulatory action |
| 4 | Alopecia | 99.76% | L5 | Vasoconstriction runs opposite to hair-growth agents |
| 5 | Primary hereditary glaucoma | 99.62% | L5 | Class analogy to alpha-2 agonists only; safety concern |
| 6 | Hypertrichosis | 99.60% | L5 | Opposite phenotype to ranks 1-4, which suggests a non-specific score |
| 7 | Ambras type hypertrichosis universalis congenita | 99.60% | L5 | Rare genetic disorder |
| 8 | Open-angle glaucoma | 99.59% | L5 | The one retrieved paper does not involve naphazoline |
| 9 | Malformation syndrome with odontal/periodontal component | 99.57% | L5 | Retrieved literature matches disease terms only |
| 10 | Syndrome with Dandy-Walker malformation | 99.52% | L5 | Congenital brain malformation |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top prediction.

Two lower-ranked predictions returned papers, but none concern naphazoline:
- **Open-angle glaucoma:** one 1992 paper (PMID [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/)) on topical corticosteroids after laser trabeculoplasty.
- **Periodontal malformation syndrome:** generic periodontitis guidelines and reviews, which appear to match on disease terms only.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. H 1272 (Act 101/1965) | Oculosan 10ml | Drops |
| Reg. No. H1236 (OM) | Covomycin 7.5ml | Een (as recorded) |

The records do not include approved indication text or Essential Medicines List (EML) status.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One caution comes from the evidence review. Ophthalmic vasoconstrictors carry an intraocular-pressure warning, and naphazoline labelling advises against use in narrow-angle glaucoma. This must be resolved before any glaucoma-related use is considered.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are model-only (L5) with no supporting trials or relevant literature. The pharmacology of a vasoconstrictor does not plausibly support hair growth, and the glaucoma predictions conflict with known safety cautions.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank)
- A plausible biological pathway, or preclinical evidence, linking naphazoline to hair follicle biology
- Route compatibility assessment: the registered products are ophthalmic drops, and no scalp formulation is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

