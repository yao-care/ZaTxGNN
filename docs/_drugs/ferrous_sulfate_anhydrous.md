---
layout: default
title: Ferrous Sulfate Anhydrous
parent: Model Prediction Only (L5)
nav_order: 230
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Ferrous Sulfate Anhydrous: predicted new indication Vitamin B12- and folate-independent constitutional megaloblastic anae… (evidence level L5). Approved use: Iron deficiency anaemia and related defic…"
monitor_inn: "Ferrous sulfate anhydrous"
predicted_indications: ["vitamin B12- and folate-independent constitutional megaloblastic anemia", "Plummer-Vinson syndrome", "biotin metabolic disease", "non-syndromic esophageal malformation"]
---

# Ferrous Sulfate Anhydrous
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

## Ferrous Sulfate Anhydrous: From Iron Deficiency Anaemia to Vitamin B12- and Folate-Independent Constitutional Megaloblastic Anaemia
{: .text-alpha }

## One-Sentence Summary

Ferrous sulfate anhydrous is an oral iron supplement, originally used to treat iron deficiency anaemia and related deficiency anaemias.
The TxGNN model predicts it may be effective for **vitamin B12- and folate-independent constitutional megaloblastic anaemia**,
but **no clinical trials and no publications** were available in the data compiled for this report, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anaemia and related deficiency anaemias (the SAHPRA records in the data compiled for this report contain no approved indication text) |
| Predicted New Indication | Vitamin B12- and folate-independent constitutional megaloblastic anaemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous sulfate supplies elemental iron for haemoglobin synthesis, and its efficacy in iron deficiency anaemia is well established.

The link to the predicted indication is weak. Megaloblastic anaemia is typically driven by impaired DNA synthesis (B12 and folate pathways). A constitutional form independent of both would involve other defects, and iron is not an established treatment for these. A link is plausible only if iron deficiency coexists, and the data compiled for this report do not support that. The high score (99.78%, model rank 1577) is a computational prediction and should not be read as evidence of efficacy.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Plummer-Vinson syndrome | 99.77% | The most credible candidate. The condition is driven by iron deficiency (with dysphagia and oesophageal webs), and iron repletion is widely described as standard management. It is largely an extension of the existing iron deficiency indication, not a novel repurposing. Supporting evidence (case series, reviews) should be retrieved and graded before any upgrade. |
| 3 | Biotin metabolic disease | 99.51% | No clear mechanistic route. The score likely reflects proximity in the knowledge graph (shared vitamin-deficiency neighbours). Biotin supplementation, not iron, is the treatment. |
| 4 | Non-syndromic oesophageal malformation | 99.49% | These are structural defects managed surgically or endoscopically. The prediction probably arises from association with Plummer-Vinson syndrome. Oral iron may irritate the oesophagus in strictures or dysphagia. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2466 | Complenatal Ff | Capsule | Not stated in the data compiled for this report |
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not stated in the data compiled for this report |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not stated in the data compiled for this report |

All three registrations are valid single-ingredient entries. The oral products are capsules. The Spiriva Respimat entry is an inhaler and is unusual for an iron product, so it should be verified against the SAHPRA register. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (disease associations from the TxGNN knowledge graph, not label text):
- Peptic ulcer disease
- Ulcerative colitis and inflammatory bowel disease
- Gastroenteritis
- Dyskinesia of the oesophagus
- Sickle cell anaemia and haemolytic anaemia
- Hereditary persistence of fetal haemoglobin
- Hereditary haemochromatosis, haemosiderosis and iron metabolism disease
- Primary hyperoxaluria
- Wilson disease

**Drug Interactions:** 37 interactions were recorded. The 20 listed in the data compiled for this report are mostly Moderate, with a few Minor.
- **Moderate:**
  - Proton pump inhibitors: rabeprazole, omeprazole, dexlansoprazole, lansoprazole, pantoprazole, esomeprazole
  - Tetracyclines: doxycycline, tetracycline, minocycline
  - Fluoroquinolone: levofloxacin
  - Antacids and minerals: magnesium oxide, calcium carbonate, aluminium hydroxide, magaldrate, sodium sulfate
  - Others: pancrelipase, triethylenetetramine
- **Minor:** cimetidine, zinc sulfate, zinc acetate

Practical points are to separate dosing from tetracyclines, quinolones and antacids, and to recognise that acid suppression reduces iron absorption.

Warnings and contraindications from the SAHPRA label were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the proposed mechanism does not fit the disease. Only Plummer-Vinson syndrome looks biologically credible, and it largely overlaps the existing iron deficiency indication.

**To proceed, the following is needed:**
- Retrieve and grade the literature for Plummer-Vinson syndrome (case series, reviews) as the priority candidate
- Download and review the SAHPRA package inserts for warnings, contraindications and approved indications, which is a blocking gap for safety screening
- Obtain mechanism of action data (for example from DrugBank)
- Verify the registrations, especially the Spiriva Respimat entry, and check EML status
- Review oral iron safety in patients with oesophageal strictures or dysphagia before considering any oesophageal-related indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

