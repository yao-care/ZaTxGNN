---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 5
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-11-12
description: "Ergocalciferol: predicted new indication Acromesomelic dysplasia, Campailla-Martinelli type (evidence level L5). Approved use: Rickets, osteomalacia, osteoporosis…"
---

# Ergocalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ergocalciferol: From Vitamin D Deficiency and Bone Disorders to Acromesomelic Dysplasia, Campailla-Martinelli Type
{: .text-alpha }

## One-Sentence Summary

Ergocalciferol (vitamin D2) has relations recorded in the knowledge graph with bone and mineral disorders such as rickets, osteomalacia, osteoporosis and vitamin deficiency. The TxGNN model predicts it may be useful for **acromesomelic dysplasia, Campailla-Martinelli type**, a rare skeletal dysplasia. This prediction has **no clinical trials and no publications** supporting it, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rickets, osteomalacia, osteoporosis, vitamin deficiency and related bone and mineral disorders (relations recorded in the knowledge graph; the local licence records contain no approved indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Campailla-Martinelli type |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 5 of 14; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 14 (valid: 5, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ergocalciferol is a form of vitamin D that is part of calcium and phosphate regulation and bone mineralisation. Its link to rickets, osteomalacia and similar disorders is recorded in the knowledge graph.

Acromesomelic dysplasia is a rare, inherited skeletal growth disorder. The data compiled for this report show no plausible link between vitamin D2 signalling or calcium/phosphate balance and this condition. The high score reflects the model's network-based similarity only. It is not supported by any mechanistic or clinical evidence, and it should be treated as a hypothesis rather than a finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| T1101 | Calciferol oily | drops | Valid |
| 30/22.1/0201 | Vitalipid novum infant 10ml pdv00001l | infusion | Valid |
| G2667 (ACT 101/1965) | Gericomplex | capsule | Valid (status not confirmed by SAHPRA) |
| Z/22.1/236 | Vitalipid novum adult 10ml pdv00001a | infusion | Valid |
| H2053 | A-LENNON Calciferol | tablet | Valid |

Showing 5 of 14 registrations (valid registrations first).

<!-- licenses:end -->

The inhaler product name does not look like a typical ergocalciferol product, so the registration should be checked against the SAHPRA register before relying on it. Neither record includes approved-indication text, so no indication can be described as approved from the data compiled for this report.

<!-- review:begin za-lic-20261105-ergocalciferol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both records are listed as valid single-ingredient registrations. The inhaler product name does not look like a typical ergocalciferol product, so the registration should be checked against the SAHPRA register before relying on it." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 14 registrations for this drug, 5 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-ergocalciferol-1 -->

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication relations recorded in the knowledge graph** (not label text) include:
- Hypercalcaemia, hyperparathyroidism, nephrocalcinosis and phosphorus metabolism disorders
- Kidney disease, liver disease and sarcoidosis
- Hypertension, atrial fibrillation, diabetes mellitus and diabetic ketoacidosis
- Other conditions, including primary hyperoxaluria, iron overload disorders, Wilson disease, hyperlipidaemia, and breast and prostate cancer

**Drug interactions** (55 recorded in total):
- **Major:** other vitamin D products and analogues (cholecalciferol, calcifediol, calcitriol, doxercalciferol), because of additive effects and the risk of hypercalcaemia
- **Moderate:** thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone), digoxin, carbamazepine, barbiturates (amobarbital, butalbital), rifabutin, bile-acid binders (cholestyramine, colesevelam, colestipol), sevelamer, magnesium oxide and topical calcipotriol or calcitriol
- **Minor:** cimetidine

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There are no trials or publications for this indication, and no mechanistic rationale can be drawn from the data compiled. The evidence is limited to a model score (L5).
- Other predictions for this drug have more supporting data. For example, renal osteodystrophy has a Phase 4 trial ([NCT01799317](https://clinicaltrials.gov/study/NCT01799317), n=60, status unknown) and a randomised comparison of ergocalciferol with calcitriol ([PMID 27401037](https://pubmed.ncbi.nlm.nih.gov/27401037/)). It would be a more sensible candidate for further review.

**To proceed, the following is needed:**
- Mechanism of action data for ergocalciferol
- A literature review for any biological link between vitamin D pathways and this dysplasia
- SAHPRA Professional Information, covering warnings and contraindications, for the registered products
- Verification of the two registration records and of any Essential Medicines List status
- A separate evaluation of higher-evidence candidates such as renal osteodystrophy

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both records are listed as valid single-ingredient registrations" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

