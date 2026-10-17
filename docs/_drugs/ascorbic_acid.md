---
layout: default
title: Ascorbic Acid
parent: Model Prediction Only (L5)
nav_order: 47
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ascorbic Acid: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Ascorbic acid deficiency, scurvy"
monitor_inn: "Ascorbic acid"
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "congenital prothrombin deficiency", "injury", "biotin metabolic disease", "segmental odontomaxillary dysplasia", "florid cemento-osseous dysplasia", "perinatal disease", "disease by subcellular system affected"]
---

# Ascorbic Acid
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

# Ascorbic Acid: From Ascorbic Acid Deficiency (Scurvy) to Non-syndromic Esophageal Malformation

## One-Sentence Summary

Ascorbic acid (vitamin C) is originally used to prevent and treat vitamin C deficiency and scurvy.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**, but there are **no clinical trials** and **no publications** supporting this prediction. It rests on the model score alone and is most likely a graph-prediction artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency, scurvy (from the TxGNN knowledge graph; indication text was not available for the SAHPRA registrations) |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ascorbic acid is not available in the data compiled for this report. Based on known pharmacology, ascorbic acid is an antioxidant and a cofactor for collagen and catecholamine synthesis. Its efficacy in correcting vitamin C deficiency is well established.

No mechanistic link to the predicted indication was identified. Non-syndromic esophageal malformation is a structural congenital defect, and an antioxidant or cofactor vitamin is unlikely to correct it. The very high TxGNN score (rank 398 overall) is therefore best read as a likely graph artifact rather than a credible repurposing signal.

Other predictions for this drug have more supporting evidence than this top-ranked one (see Conclusion and Next Steps).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

SAHPRA lists 18 valid registrations, none cancelled. Dosage forms include tablets, capsules, effervescent tablets, sachets, syrup and infusions. Approved indication text and Essential Medicines List status were not available in the data compiled for this report. The five registrations below are examples.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36/22.1/0508 | Cernevit | Infusion | Not available in compiled data |
| H2466 | Complenatal Ff | Capsule | Not available in compiled data |
| H0689 (ACT 101/1965) | Autrin | Capsule | Not available in compiled data |
| 35/5.8/0152 | Flutex effervescent | Effervescent tablet | Not available in compiled data |
| A/21.8.1/743 | Menoflush | Tablet | Not available in compiled data |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (graph-derived drug-disease links, not label text; they need confirmation against the Professional Information):
- Cardiovascular and metabolic: hypertension, diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Renal and urinary: kidney disease, anuria, nephrocalcinosis, primary hyperoxaluria
- Hepatic and gastrointestinal: liver disease, gallbladder disease, peptic ulcer disease
- Haematological: blood coagulation disease, sickle cell anaemia, hereditary hemochromatosis, hereditary persistence of fetal haemoglobin
- Other: epilepsy, multiple sclerosis, sarcoidosis, rheumatoid arthritis, systemic lupus erythematosus, hypercalcaemia, hyperparathyroidism, allergic and vasomotor rhinitis, sunburn

**Drug interactions** (25 recorded; DDInter):
- Moderate: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine, aluminium hydroxide, bortezomib, deferoxamine
- Minor: paclitaxel, cisplatin, doxorubicin (including liposomal), ethinylestradiol, pseudoephedrine, ephedrine, flecainide, fluphenazine, indinavir, mexiletine, and others

**Other signal:** In a rat acid-reflux model, ascorbic acid combined with sodium nitrite enhanced esophageal carcinogenesis (PMID 17953708). This was found under a different esophageal prediction, not this one, but it is relevant to any esophageal use.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no trials, no literature and no plausible mechanism, so it should not be pursued.
- Ascorbic acid is widely marketed in South Africa, but this does not support efficacy in a structural congenital malformation.

**To proceed, the following is needed:**
- Redirect evaluation to better-supported predictions for this drug:
  - **Injury** (L2): Phase 2 trials in sepsis-induced and COVID-19 acute lung injury, with small and heterogeneous evidence.
  - **Vitamin deficiency disorder** (L3): largely an on-label extension.
  - **Esophageal disease** (L4): literature is mainly old epidemiology and animal work, with a potential safety signal.
- Obtain the SAHPRA Professional Information to confirm approved indications, warnings and contraindications.
- Obtain detailed mechanism-of-action data to support any mechanistic-link analysis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

