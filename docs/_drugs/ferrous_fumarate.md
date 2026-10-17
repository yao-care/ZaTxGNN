---
layout: default
title: Ferrous Fumarate
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Ferrous Fumarate: predicted new indication Non-syndromic oesophageal malformation (evidence level L5). Approved use: Iron deficiency anaemia, folic acid deficiency anaemia…"
monitor_inn: "FERROUS FUMARATE"
predicted_indications: ["non-syndromic esophageal malformation"]
---

# Ferrous Fumarate
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

# Ferrous Fumarate: From Iron Deficiency Anaemia to Non-Syndromic Oesophageal Malformation

## One-Sentence Summary

Ferrous fumarate is an oral iron supplement, originally used to treat iron deficiency anaemia and related anaemias.
The TxGNN model predicts it may be effective for **non-syndromic oesophageal malformation**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anaemia, folic acid deficiency anaemia, anaemia of prematurity, hypochromic anaemia, microcytic anaemia, deficiency anaemia (knowledge-graph indications; the SAHPRA registrations list no approved indication text) |
| Predicted New Indication | Non-syndromic oesophageal malformation |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous fumarate is an oral iron salt used to replenish iron stores and correct iron deficiency anaemia. It is not known to act on the pathways involved in oesophageal development.

The predicted condition, non-syndromic oesophageal malformation (for example oesophageal atresia or tracheo-oesophageal fistula), is a congenital structural defect arising during embryonic development. There is no established biological rationale for oral iron supplementation correcting or treating such defects. The link between the original and predicted indications is therefore weak.

The high TxGNN score (99.49%) is a model-derived prediction only. The association is likely a knowledge-graph artefact, for example through shared gene or pathway neighbours, and has not been validated. The score should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H0689 (ACT 101/1965) | Autrin | Capsule | Not stated in the data compiled |
| H2062 (ACT 101) | Filibon | Capsule | Not stated in the data compiled |

Both registrations are valid single-ingredient products for oral use. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** The TxGNN knowledge graph links ferrous fumarate with the following conditions, including:
  - Iron overload and metabolism: hereditary haemochromatosis, haemosiderosis, iron metabolism disease
  - Haematological: sickle cell anaemia, hereditary persistence of fetal haemoglobin
  - Organ disease: kidney disease, liver disease, gallbladder disease, peptic ulcer disease
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency disease
  - Other: porphyria and other porphyrin metabolism diseases, Wilson disease, primary hyperoxaluria, sarcoidosis, hypertension, anxiety, neurotic and dysthymic disorders, pyoureter

  These come from graph edges, not SAHPRA label text, and must be verified against the approved Professional Information (PI).
- **Drug Interactions:** 80 interactions were identified in total. The 20 listed in the data compiled are mostly of Moderate severity, with a few Minor:
  - Proton pump inhibitors (rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole): Moderate
  - Tetracyclines (doxycycline, tetracycline, minocycline) and levofloxacin: Moderate
  - Antacids and minerals (magnesium oxide, calcium carbonate, aluminium hydroxide, magaldrate, sodium sulfate): Moderate
  - Pancrelipase and triethylenetetramine: Moderate
  - Cimetidine, zinc sulfate and zinc acetate: Minor

  Spacing of administration and absorption effects should be checked in the PI.

Warnings and contraindications from the SAHPRA-approved PI have not been obtained. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5), and no plausible mechanism links oral iron to correcting a congenital structural malformation. The label-based safety review is also incomplete.

**To proceed, the following is needed:**
- Obtain and review the SAHPRA package insert (warnings, contraindications, approved indications). This is a blocking gap for safety screening.
- Obtain mechanism of action data from DrugBank.
- Conduct a systematic literature and trial registry search (including SANCTR, PACTR and ICTRP) for any link between iron and oesophageal malformation.
- Examine the knowledge-graph path behind the prediction to determine whether it is an artefact.
- Assess route compatibility and the clinical relevance of the predicted indication, since this is a congenital condition managed surgically.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

