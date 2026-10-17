---
layout: default
title: Norgestimate
parent: Model Prediction Only (L5)
nav_order: 350
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Norgestimate: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne, postmenopausal osteoporosis, osteoporosis…"
monitor_inn: "norgestimate"
predicted_indications: ["zinc, elevated plasma"]
---

# Norgestimate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Norgestimate: From Acne and Postmenopausal Conditions to Elevated Plasma Zinc

## One-Sentence Summary

Norgestimate is a progestin, mainly used in combined hormonal products. The knowledge graph links it to acne, postmenopausal osteoporosis, osteoporosis and atrophic vulvovaginal conditions.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, postmenopausal osteoporosis, osteoporosis, atrophic vulvovaginal conditions (from the knowledge graph; the SAHPRA registration data contain no approved indication text) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norgestimate is a progestin (a prodrug whose active metabolites include levonorgestrel and norgestrel) used mainly in combined oral contraceptives. Its role in the original indications is hormonal, but a mechanistic link to elevated plasma zinc has not been established.

Hormonal contraceptives have been reported to alter circulating trace-element levels (for example, higher copper and lower zinc). This is general class-level background and not evidence from the data compiled for this report. It also points in the opposite direction to what the prediction would need, since it suggests lowering rather than raising zinc.

"Elevated plasma zinc" is a laboratory finding rather than a clearly treatable disease, and it is unclear what therapeutic benefit a progestin would offer. The score of 0.99 is a model output only and may reflect knowledge-graph artefacts, such as shared links to other conditions or zinc-related pathways.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. X/18.8/46 | Cilest | Tablet | Not stated in the data compiled for this report |
| Reg. No. X/18.8/47 | Tricilest | Tablet | Not stated in the data compiled for this report |

Both registrations are valid, single-ingredient entries for oral tablets. Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug-disease edges, not label text, so they must be confirmed against the Professional Information):
- Cardiovascular and metabolic: hypertension and hypertensive disorders, diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypertriglyceridaemia
- Hepatic and renal: liver disease, gallbladder disease, kidney disease
- Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- Metabolic and endocrine: porphyria (including inherited forms), hypothyroidism (including myxoedema and congenital hypothyroidism), hypercalcaemia and related calcium/phosphorus disorders, nephrocalcinosis
- Other: systemic lupus erythematosus, asthma (intrinsic and allergic), female breast carcinoma

**Drug Interactions:** 38 interactions were identified. Examples of those graded **Major**:
- Sugammadex
- Griseofulvin
- Bexarotene
- Brigatinib
- Dabrafenib
- Encorafenib

Examples graded **Moderate** include metreleptin, miltefosine, adalimumab, anakinra, cladribine, enasidenib and entrectinib. Minor examples include rosuvastatin and ethanol. Only 20 of the 38 interactions were available for this report.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications from the label. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no literature and no established mechanistic link. Elevated plasma zinc is a laboratory finding rather than a defined treatment target, so there is no clear therapeutic rationale.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), which is currently a blocking gap for safety screening
- Mechanism of action data for norgestimate and its active metabolites
- A clinical justification for treating elevated plasma zinc, and a literature search for any link between progestins and zinc homeostasis
- Confirmation of the knowledge-graph contraindications against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

