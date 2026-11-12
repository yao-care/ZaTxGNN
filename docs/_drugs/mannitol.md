---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 9
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-11-12
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: No approved indication text is available for the local registration.…"
---

# Mannitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Mannitol: From Cardiac, Cerebral and Ocular Fluid Disorders to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Mannitol is an osmotic diuretic. It is recorded for conditions such as congestive heart failure, brain oedema, ocular hypertension and intracranial hypertension.
The TxGNN model predicts it may be useful for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials** and only **1 general review** support this direction, and that review does not study mannitol for NSIAD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is available for the local registration. The knowledge graph records congestive heart failure, brain oedema, ocular hypertension, pseudotumor cerebri, intracranial hypertension and cystic fibrosis (relations recorded in the knowledge graph, not approved indications) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 13) |
| Number of SAHPRA Registrations | 13 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Mannitol is generally known as an osmotic diuretic, so a theoretical link to water-handling disorders exists.

NSIAD, however, is caused by gain-of-function variants in the vasopressin V2 receptor. Its usual management is fluid restriction and urea or solute loading. Mannitol would add osmotic load, but it is not a recognised treatment for this condition. The only literature item is a general review of pitfalls in evaluating hyponatraemia, which does not assess mannitol. The high model score is therefore not backed by mechanistic or clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in evaluating and treating hyponatraemia. It does not evaluate mannitol for NSIAD. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 31/34/0163 | Mannitol fresenius irrigation solution | infusion | Valid |
| D/18.1/211 | Osmitrol  500ml (afd5633) | infusion | Valid |
| F0594 | Osmitrol  500ml (afd5633) | infusion | Valid |
| H1652 | Osmitrol (mannitol)  3000ml irrigation ( | solution | Valid |
| L/18.1/228 | Mannitol 20% fresenius solution for infu | infusion | Valid |

Showing 5 of 13 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-mannitol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "This registration is a single-ingredient, valid record for an injectable infusion. Its product name suggests use as a cardioplegic solution, so it should not be taken as evidence of approval for NSIAD or for other mannitol uses. Essential Medicines List status is not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 13 registrations for this drug, 11 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-mannitol-1 -->

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver failure, hepatic coma and encephalopathy, anuria, impaired renal function, pulmonary oedema, intracranial haemorrhage, porphyria, and blood disorders (thrombocytopenia, neutropenia, agranulocytosis, anaemia). Others include sleep apnoea syndromes, anxiety and related disorders, and substance-related disorders.
- **Drug interactions (100 recorded; examples):**
  - Major: amikacin.
  - Moderate: lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, cisatracurium, canagliflozin, dapagliflozin, desvenlafaxine, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid, diatrizoate, amifostine.
  - Minor: doxycycline.
- **Specific concern for this prediction:** mannitol expands intravascular volume and adds osmotic load, which could be unhelpful in a water-retention disorder.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials exist, the only cited paper is a general hyponatraemia review that does not study mannitol, and NSIAD has established non-mannitol management. The score reflects model output only, so the evidence level is L5.

**To proceed, the following is needed:**
- Direct clinical or mechanistic evidence that mannitol benefits NSIAD
- Mechanism of action data for mannitol
- SAHPRA package insert warnings and contraindications, to allow safety screening
- A risk assessment of osmotic load and volume expansion in patients with NSIAD

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "This registration is a single-ingredient, valid record for an injectable infusion. Its product name suggests use as a cardioplegic solution," | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

