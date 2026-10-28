---
layout: default
title: Naphazoline
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Naphazoline: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not stated in the SAHPRA registration data"
monitor_inn: "NAPHAZOLINE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "primary hereditary glaucoma", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "open-angle glaucoma", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Naphazoline: From Ocular Redness (Decongestant Use) to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Naphazoline is a vasoconstrictor (alpha-adrenergic agonist) used in eye drops to temporarily reduce redness by narrowing swollen blood vessels.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but there are currently **no clinical trials and no publications** supporting this direction; it is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data; pharmacology data describe use as a vasoconstrictor to reduce eye redness |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, naphazoline is an alpha-adrenergic agonist. It acts on alpha-1A, alpha-2A and alpha-2C adrenoceptors, and its effect of narrowing blood vessels is established for ocular redness.

A plausible link between this vasoconstrictor action and a hereditary hair-growth disorder has not been established. The high score (0.9983) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions (congenital hypotrichosis milia, diffuse alopecia areata, alopecia, hypertrichosis) face the same problem. For alopecia in general, established agents such as minoxidil act through vasodilation and potassium channel opening, so the mechanistic direction of a vasoconstrictor is questionable. In alopecia areata, an autoimmune condition, topical vasoconstriction has no known immunomodulatory benefit and could in theory reduce follicular perfusion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the leading prediction (hypotrichosis simplex of the scalp).

For the lower-ranked prediction of open-angle glaucoma, one publication was linked, but it does not evaluate naphazoline:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) | 1992 | Unclear (clinical/laser study) | Australian and New Zealand Journal of Ophthalmology | Effect of topical corticosteroids on laser-induced peripheral anterior synechiae after argon laser trabeculoplasty; does not study naphazoline and does not support efficacy |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H 1272 (ACT 101/1965) | Oculosan 10ml | Drops | Not stated |
| H1236 (OM) | Covomycin 7.5ml | Een (as recorded) | Not stated |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

- **Disease associations flagged by the knowledge graph (not label text):** hypertension and other hypertensive disorders, cardiovascular and heart disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, angle-closure (closed-angle) glaucoma, hyperthyroidism (Graves disease, thyrotoxicosis), and eye infections including conjunctivitis. These come from graph-based contraindication links and should be confirmed against the approved label.
- **Glaucoma caution:** alpha-agonist mydriatic effects carry a risk of angle closure in susceptible patients, which is relevant to the glaucoma predictions.
- **Pharmacological targets:** alpha-1A, alpha-2A and alpha-2C adrenoceptors (human), plus a mouse trace amine receptor entry. No drug-drug interaction data with other medicines were identified.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are model-based only (L5), with no supporting trials or publications. The mechanism is doubtful for hair disorders (a vasoconstrictor versus established vasodilating agents), and for glaucoma predictions there is an angle-closure safety concern. Safety review cannot proceed without the PI.

**To proceed, the following is needed:**
- Retrieve and review the SAHPRA package inserts (warnings, contraindications, approved indications)
- Obtain mechanism of action data from DrugBank
- A systematic literature search for naphazoline in hair disorders (and glaucoma) to look for any direct evidence
- Preclinical or mechanistic evidence showing a plausible biological link before any clinical consideration
- Confirmation of formulation and route suitability for any new indication (currently only ophthalmic drops are registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

