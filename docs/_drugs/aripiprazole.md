---
layout: default
title: Aripiprazole
parent: Model Prediction Only (L5)
nav_order: 44
evidence_level: L5
indication_count: 8
monitor_inn: "ARIPIPRAZOLE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "Phelan-McDermid syndrome", "amelocerebrohypohidrotic syndrome", "distal 17p13.3 microdeletion syndrome", "trichotillomania", "Malan overgrowth syndrome", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)"]
last_modified_at: 2026-11-24
description: "Aripiprazole: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). In South Africa: 87 SAHPRA registrations (69 valid)"
---

# Aripiprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Aripiprazole: Gaze palsy, familial horizontal, with progressive scoliosis
{: .text-alpha }

## One-Sentence Summary

Aripiprazole is an atypical antipsychotic that is currently marketed in South Africa mainly as tablets, with injectable products also registered.
The TxGNN model predicts it may be effective for **gaze palsy, familial horizontal, with progressive scoliosis**, with a score of 0.9960.
**No clinical trials or publications** in the compiled data support this prediction, so it rests on the model output alone.

<!-- review:begin za-lic-20261124b-aripiprazole-2 -->

> **Review correction (2026-11-24)**: Originally stated: "that is currently marketed in South Africa as an injectable product." Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-aripiprazole-2 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 69 of 87; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 87 (valid: 69, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aripiprazole: "The mechanism of action of aripiprazole in the treatment of schizophrenia and bipolar I disorder is unknown. The efficacy of aripiprazole could be mediated through a combination of partial agonist activity at dopamine D 2 and serotonin 5-HT 1A receptors and antagonist activity at 5-HT 2A receptors." ([DailyMed: Abilify Asimtufii (aripiprazole) prescribing information, Otsuka America Pharmaceutical, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da4c07fd-1130-4341-bb44-63acfa4162be), label version 2025-04-04; accessed 2026-11-19.) Aripiprazole is generally classed as an atypical antipsychotic, and its receptor pharmacology is usually described as dopamine D2 partial agonism with serotonin receptor modulation.

Familial horizontal gaze palsy with progressive scoliosis is a rare inherited neurological disorder. It involves impaired horizontal eye movements together with a progressive spinal curvature. No plausible mechanistic link between aripiprazole's receptor pharmacology and this condition is evident. The high score is not backed by any clinical or preclinical evidence, so it should be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 41/2.6.5/0493 | Abilify | tablet | Valid |
| 42/2.6.5/0179 | Abilify im 1.3ml vial | injection | Valid (status not confirmed by SAHPRA) |
| 46/2.6.5/0874 | Arizofy | tablet | Valid |
| 46/2.6.5/0875 | Arizofy | tablet | Valid |
| 46/2.6.5/0876 | Arizofy | tablet | Valid |

Showing 5 of 87 registrations (valid registrations first).

<!-- licenses:end -->

Aripiprazole is marketed in South Africa as single-ingredient tablets (including orally disintegrating tablets) and injections. Essential Medicines List status is not available in the compiled data.

<!-- review:begin za-lic-20261124b-aripiprazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Aripiprazole is marketed in South Africa as a single-ingredient injectable." Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-aripiprazole-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. The entries reviewed include:
  - **Major**: bupropion.
  - **Moderate**: acarbose, alogliptin, albiglutide, metformin, pioglitazone, acetohexamide, chlorpropamide and canagliflozin (glucose-lowering agents). Famotidine, cimetidine, epinephrine, atropine, hyoscyamine, clidinium, loperamide, aprepitant, cisapride, clarithromycin and clotrimazole are also listed.

Label warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the compiled data. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials, publications or plausible mechanistic rationale, so the evidence level is L5. There is no basis for clinical action.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that directly studies aripiprazole in this condition
- A defined mechanistic hypothesis linking aripiprazole's pharmacology to the disease biology
- Mechanism-of-action data and the SAHPRA Professional Information (warnings and contraindications) for a full safety review

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for aripiprazole are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Abilify Asimtufii (aripiprazole) prescribing information, Otsuka America Pharmaceutical, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=da4c07fd-1130-4341-bb44-63acfa4162be) |
| 2026-11-24 | Corrected: "Aripiprazole is marketed in South Africa as a single-ingredient injectable." | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-24 | Corrected: "that is currently marketed in South Africa as an injectable product." | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

