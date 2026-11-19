---
layout: default
title: Nystatin
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "Nystatin"
predicted_indications: ["disease of orbital region", "disease of orbital part of eye adnexa", "cystic teratoma", "spinal cord dermoid cyst", "postmenopausal atrophic vaginitis", "biotin metabolic disease", "vulvitis", "commissural lip fistula", "osteoradionecrosis of the mandible"]
description: "Nystatin: predicted new indication Disease of orbital region (evidence level L5). In South Africa: 20 SAHPRA registrations (7 valid)"
---

# Nystatin
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

## Nystatin: Disease of orbital region
{: .text-alpha }

## One-Sentence Summary

Nystatin is a polyene antifungal medicine marketed in South Africa. The TxGNN model predicts it may be relevant to **disease of orbital region**, but this rests on a model score alone: **1 clinical trial** was linked, and it tests a different compound in a different eye condition, and **no publications** were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Disease of orbital region |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 7 of 20) |
| Number of SAHPRA Registrations | 20 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for nystatin: "Nystatin acts by binding to sterols in the cell membrane of susceptible Candida species with a resultant change in membrane permeability allowing leakage of intracellular components. Nystatin exhibits no appreciable activity against bacteria, protozoa, or viruses." ([DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6), label version 2026-02-06; accessed 2026-11-19.) Nystatin is a polyene antifungal that is generally understood to bind ergosterol in fungal cell membranes, so any effect would be expected only where a fungal infection is involved.

No plausible mechanistic link between nystatin and disease of orbital region was identified. The only linked trial studies a different compound for a retinal condition, and fungal orbital infection, while possible in principle, is not an established indication for nystatin. The high score is therefore most likely a computational artefact rather than a signal of real benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03178149](https://clinicaltrials.gov/study/NCT03178149) | Phase 1 | Recruiting | 42 | Phase 1b dose-escalation safety study of ASP7317 (not nystatin) in geographic atrophy secondary to age-related macular degeneration; a retinal disease, so it gives no evidence for nystatin in orbital disease |

No SANCTR or PACTR registrations were found.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 31/20.1.7/0288 | Candacide | suspension | Valid |
| D/20.1.7/170 | Canstat | vaginal cream | Valid |
| 50/20.1.1/0250 | Polygynax® | Pvc | Valid |
| D/20.1.7/171 | Canstat oral | suspension | Valid |
| F/13.9.2/158 | Canstat | cream | Valid |

Showing 5 of 20 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List status could not be determined from the data compiled for this report.

<!-- review:begin za-lic-20261105-nystatin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All 4 registrations are currently valid. Essential Medicines List status could not be determined from the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 20 registrations for this drug, 13 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-nystatin-1 -->

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Drug interaction screening returned 100 potential interactions, all with an unclassified severity level. Examples include cyclosporine, fluconazole, erythromycin, azithromycin, bortezomib, tramadol and sildenafil. Their clinical significance has not been graded and should be checked against the PI before any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting evidence: the single linked trial concerns a different drug and a retinal disease, no publications were found, and there is no plausible mechanism. It does not justify further investment at this stage.

**To proceed, the following is needed:**
- Any published case series or studies of nystatin in orbital or periorbital fungal disease
- Mechanism of action data and a defined biological rationale for the orbital region
- Review of the SAHPRA Professional Information for warnings and contraindications
- Confirmation of a suitable route of administration for orbital use, as the registered forms are topical and vaginal/other

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All 4 registrations are currently valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nystatin Oral Suspension (nystatin) prescribing information, Xttrium Laboratories, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4a670371-d373-1ba6-e063-6394a90a13b6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

