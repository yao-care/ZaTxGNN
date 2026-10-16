---
layout: default
title: Ethinylestradiol
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Ethinylestradiol: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
---

# Ethinylestradiol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ethinylestradiol: From Acne and Postmenopausal Osteoporosis to Elevated Plasma Zinc

## One-Sentence Summary

Ethinylestradiol is a synthetic oestrogen, listed with original indications that include acne, postmenopausal osteoporosis, osteoporosis, atrophic vulva and postmenopausal atrophic vaginitis.
The TxGNN model predicts it may be relevant to **elevated plasma zinc**,
but **no clinical trials and no publications** were found to support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne; postmenopausal osteoporosis; osteoporosis; atrophic vulva; postmenopausal atrophic vaginitis (from the TxGNN knowledge graph, as no approved indication text is available in the SAHPRA data) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ethinylestradiol is a synthetic oestrogen widely used in combination oral contraceptives and other hormonal products. It has an established role in oestrogen-responsive conditions, such as those listed above. Its mechanistic applicability to elevated plasma zinc cannot be assessed from the data compiled for this report.

One possible indirect link comes from general background knowledge, not from the data compiled here. Oestrogen exposure is known to alter circulating trace-element levels, including zinc and copper, possibly through changes in binding proteins such as albumin and ceruloplasmin.

There are important caveats:
- This concerns a change in a laboratory measurement, not a demonstrated therapeutic effect.
- Elevated plasma zinc is a biochemical finding more than a disease with an established treatment goal, so the repurposing rationale is unclear.
- The direction of effect is uncertain. The prediction may reflect an association or an adverse effect instead of a benefit.

The high score (0.996) reflects a knowledge-graph pattern only. It is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Ethinylestradiol is marketed in South Africa with 20 valid SAHPRA registrations, all single-ingredient entries and none cancelled. Approved indication text was not available in the data compiled for this report, and Essential Medicines List (EML) status was not available either. Five main registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 44/18.8/0397 | Ynez | Film-coated tablet (Fct) | Not available |
| 50/21.8.2/0590 | Contrezin | Tablet | Not available |
| 47/21.8.2/0141 | Drasira | Tablet | Not available |
| 36/18.7/0491 | Evra | Patch | Not available |
| Y/18.8/78 | Mercilon | Tablet | Not available |

Other registered products include Loette 28, Ginette, Nordiol, Minerva, Ruby, Oralcon, Novynette, Trigestrel and Menoflush. Dosage forms recorded include tablet, film-coated tablet, patch and other forms (Sha, Sct).

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph** (drug-disease links in PrimeKG, not label text) include:
- Cardiovascular: hypertension, hypertensive disorder, congestive heart failure
- Hepatic and biliary: liver disease, gallbladder disease
- Renal: kidney disease, pyoureter
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypothyroidism, myxedema, congenital hypothyroidism, adrenocortical insufficiency, Addison disease, hypercalcaemia, humoral hypercalcaemia of malignancy
- Porphyria: inherited porphyria, porphyrin metabolism disease, porphyria
- Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- Other: asthma (intrinsic and allergic), systemic lupus erythematosus (including paediatric), benign prostatic hyperplasia

**Drug interactions:** The interaction query returned 100 interactions, of which 20 are shown in the data compiled. Most are rated Moderate and a few Minor. Examples include:
- Antidiabetic agents: acarbose, acetohexamide, albiglutide, alogliptin, chlorpropamide, dulaglutide, empagliflozin, glimepiride, glipizide, glyburide
- Corticosteroids: betamethasone, budesonide, dexamethasone
- Antibiotics: doxycycline, amoxicillin, clarithromycin
- Others: chenodeoxycholic acid, eliglustat; cimetidine and ascorbic acid (Minor)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). There are no clinical trials or publications, and the mechanism of action is unavailable. Elevated plasma zinc is a laboratory finding without an established treatment goal, and the direction of effect is uncertain. Safety screening cannot proceed because the package insert data are missing.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) warnings, contraindications and approved indications, obtained by downloading and parsing the PI
- Mechanism of action data for ethinylestradiol (for example from DrugBank)
- A literature search on oestrogen or ethinylestradiol effects on plasma zinc, to determine whether the effect is therapeutic or adverse
- Clarification of whether elevated plasma zinc is a clinically meaningful treatment target
- Assessment of route compatibility and similarity to the original indications, both still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

