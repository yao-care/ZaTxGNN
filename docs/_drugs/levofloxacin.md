---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In South Africa: 82 SAHPRA registrations (51 valid)"
---

# Levofloxacin
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

## Levofloxacin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a broad-spectrum fluoroquinolone antibiotic used against a range of bacterial infections.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are **0 registered clinical trials** and only **1 publication** (an outbreak report of microsporidial keratoconjunctivitis that does not test levofloxacin), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 51 of 82; 9 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 82 (valid: 51, of which 9 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for levofloxacin: "Levofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] Levofloxacin is the L-isomer of the racemate, ofloxacin, a quinolone antimicrobial agent. The antibacterial activity of ofloxacin resides primarily in the L-isomer. The mechanism of action of levofloxacin and other fluoroquinolone antimicrobials involves inhibition of bacterial topoisomerase IV and DNA gyrase (both of which are type II topoisomerases), enzymes required for DNA replication, transcription, repair and recombination." ([DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5), label version 2026-11-05; accessed 2026-11-19.) Based on general knowledge, levofloxacin belongs to the fluoroquinolone class, which kills bacteria by inhibiting bacterial DNA gyrase and topoisomerase IV. Because the drug is already used against bacterial eye-surface infections such as conjunctivitis, extending it to a related ocular surface condition looks plausible at first glance.

However, the one publication retrieved describes an outbreak of microsporidial keratoconjunctivitis linked to contaminated swimming-pool water in Taiwan. Microsporidia are not susceptible to fluoroquinolones, and the report gives no evidence that levofloxacin works. The high score most likely reflects the drug's known ocular uses rather than a true mechanistic link. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis linked to swimming-pool water contamination in Taiwan; no data on levofloxacin treatment |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 41/20.1.1/0008 | Tavaloxx 500 | tablet | Valid |
| 41/20.1.1/0009 | Tavaloxx | tablet | Valid |
| 41/20.1.1/1018 | Austell levofloxacin | tablet | Valid |
| 41/20.1.1/1019 | Austell levofloxacin | tablet | Valid |
| 42/20.1.1/0632 | Lintrip 250 | tablet | Valid |

Showing 5 of 82 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-levofloxacin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Three of the four registrations are valid and one is cancelled. Essential Medicines List status is not available in the data compiled for this report." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-levofloxacin-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Major-level examples include **tramadol** and **hydrocortisone**. Moderate-level examples include metformin, pioglitazone, acarbose, alogliptin, ibuprofen, ketorolac, famotidine, salbutamol, formoterol, adenosine, alfuzosin and ethinylestradiol.

Label-based warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9992) but no registered trials and no study testing levofloxacin for this condition. The only publication concerns a pathogen that fluoroquinolones do not cover, so the evidence level is L5.

**To proceed, the following is needed:**
- Studies of levofloxacin, preferably controlled, in punctate epithelial keratoconjunctivitis of confirmed bacterial cause
- Mechanism of action data and a clear mechanistic rationale for this ocular condition
- Review of ophthalmic formulation availability in South Africa, since the registered products are oral and intravenous, apart from one combination eye drop with dexamethasone (Voxidex)
- The SAHPRA-approved Professional Information (PI) for warnings and contraindications

<!-- review:begin za-lic-20261124b-levofloxacin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "since the registered products are oral and intravenous" Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-levofloxacin-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Three of the four registrations are valid and one is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5) |
| 2026-11-24 | Corrected: "since the registered products are oral and intravenous" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

