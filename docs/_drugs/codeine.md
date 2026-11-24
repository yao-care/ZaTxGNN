---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 3
monitor_inn: "CODEINE"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-11-24
description: "Codeine: predicted new indication nasal cavity disease (evidence level L5). In South Africa: 269 SAHPRA registrations (152 valid)"
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Codeine: opioid analgesic → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid analgesic that is currently marketed in South Africa in several single-ingredient products. The TxGNN model predicts it may be relevant to **nasal cavity disease**, but no clinical trials and only **1 publication** (a case report) are linked to this prediction, and that report describes an incidental finding rather than a treatment benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 152 of 269; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 269 (valid: 152, of which 5 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for codeine: "Codeine sulfate is an opioid agonist relatively selective for the mu-opioid receptor, but with a much weaker affinity than morphine. The analgesic properties of codeine have been speculated to come from its conversion to morphine, although the exact mechanism of analgesic action remains unknown." ([DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293), label version 2026-01-16; accessed 2026-11-19.) No mechanism can be proposed for nasal cavity disease. Codeine is an opioid analgesic and cough suppressant, and the SAHPRA records compiled for this report include syrups, tablets, capsules, a suspension and an injection.

The single publication linked to this prediction (PMID 17315836) is a case report of a rhinolith that formed around a foreign body made of codeine and opium wrapped in nylon. It describes an unusual incidental event and does not show any therapeutic effect of codeine on nasal disease. The high score is therefore best read as a statistical association from the model, not as evidence of benefit. Because no cited study directly examines codeine as a treatment for nasal cavity disease, the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a unilateral rhinolith formed around an impacted foreign body, a hardened mixture of codeine and opium ("opioma"). The report is not evidence of therapeutic benefit. |

## South Africa Market Information

The approved indication text is not recorded for these registrations. The first five are shown below.

<!-- review:begin za-lic-20261105-codeine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The data compiled for this report list 20 valid single-ingredient registrations, and the list may be partial. The approved indication text is not recorded for these registrations." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-codeine-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| B1192 | Codeine | tablet | Valid |
| 27/10.1/0536 | Trifen expect paediatric | syrup | Valid |
| 27/10.1/0537 | Trifen expect adult | syrup | Valid |
| 27/2.8/0137 | Astrapain forte | tablet | Valid |
| 27/2.8/0139 | Astrapain | syrup | Valid |

Showing 5 of 269 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Contraindication-related conditions (not from label text):** The data compiled for this report flag the following conditions as potential contraindications. They should be checked against the approved Professional Information (PI):
- Hypertensive disorder, hypertension, liver failure, liver disease, kidney disease
- Epilepsy, insomnia, anxiety disorder, psychotic and other mental disorders
- Chronic obstructive pulmonary disease
- Porphyria, pancreatitis, gallbladder disease, thrombocytopenia
- Hypothyroidism, peptic ulcer disease, inflammatory bowel disease, gastritis, dermatitis herpetiformis

**Drug Interactions:** The interaction query returned 100 entries. Examples:
- **Major:** Alvimopan, Bupropion
- **Moderate:** Atropine, Cimetidine, Dexamethasone, Dicyclomine, Glycopyrronium, Granisetron, Hyoscyamine, Loperamide and others

Label warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the only linked publication is a case report of a foreign-body rhinolith and shows no therapeutic effect. No trials exist, and the mechanism data and label safety information are missing.

**To proceed, the following is needed:**
- Mechanism of action data for codeine
- SAHPRA Professional Information (warnings, contraindications and approved indications)
- Studies that directly assess codeine for a defined nasal cavity condition, with a clear clinical rationale
- A risk-benefit review covering opioid dependence and the flagged contraindicated conditions

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The data compiled for this report list 20 valid single-ingredient registrations, and the list may be partial" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available for this drug, so n" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

