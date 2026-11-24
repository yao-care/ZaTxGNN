---
layout: default
title: Erythromycin
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 4
monitor_inn: "Erythromycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "lymphogranuloma venereum", "necrotizing ulcerative gingivitis"]
last_modified_at: 2026-11-24
description: "Erythromycin: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). In South Africa: 58 SAHPRA registrations (32 valid)"
---

# Erythromycin
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

## Erythromycin: Macrolide antibiotic (50S ribosomal subunit inhibitor) → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with antibacterial and anti-inflammatory properties.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **no registered clinical trials** and only **1 publication** (a paediatric management review of chronic blepharokeratoconjunctivitis) that touches on this direction, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 32 of 58) |
| Number of SAHPRA Registrations | 58 (valid: 32) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for erythromycin: "Erythromycin acts by inhibition of protein synthesis by binding 50S ribosomal subunits of susceptible organisms. It does not affect nucleic acid synthesis." ([DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd), label version 2018-12-04; accessed 2026-11-19.) Based on general pharmacological knowledge, erythromycin is a macrolide that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit, and it is also reported to have anti-inflammatory effects.

In ocular surface disease, a macrolide could plausibly act by lowering the bacterial load on the lid margin and by dampening inflammation. This is a mechanistic rationale only. The single publication retrieved concerns chronic blepharokeratoconjunctivitis in children, which is a related but different condition from punctate epithelial keratoconjunctivitis, and it does not study erythromycin for the predicted disease itself. For this reason the evidence level is L5, even though the model score is very high.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review | Journal of Pediatric Ophthalmology and Strabismus | Describes the history, symptoms, clinical signs and treatment of chronic blepharokeratoconjunctivitis in children; a related condition, not the predicted disease itself |

---

## South Africa Market Information

The approved indication text is not recorded for any of them in the local data, and Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-erythromycin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Four single-ingredient SAHPRA registrations are valid. The approved indication text is not recorded for any of them in the local data, and Essential Medicines List status is not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-erythromycin-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 28/20.1.1/0386 | Xeramel | capsule | Valid |
| 36/20.1.1/0221 | Etocin | tablet | Valid |
| 36/20.1.1/0222 | Eryko | tablet | Valid |
| 41/20.1.1/0976 | Racemin | tablet | Valid |
| L/20.1.1/145 | Purmycin | capsule | Valid |

Showing 5 of 58 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

**Drug Interactions** (100 interactions were found in total; selected examples are listed):
- **Major**: Loperamide, Clarithromycin
- **Moderate**: Famotidine, Hydrocortisone, Pioglitazone, Alosetron, Aprepitant, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Chlorpropamide, Cimetidine, among others
- **Minor**: Amoxicillin

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and full interaction guidance. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9989), but no clinical trials exist and the only publication is a general review of a related paediatric condition. No cited study directly addresses punctate epithelial keratoconjunctivitis, so the evidence is limited to the model prediction.

**To proceed, the following is needed:**
- Studies (ideally controlled trials) of erythromycin, including ocular formulations, in punctate epithelial keratoconjunctivitis
- Confirmation of whether a suitable ophthalmic product is available in South Africa, since the registered forms are suspension, capsule, powder and lotion
- Detailed mechanism of action data
- The SAHPRA Professional Information, to review warnings and contraindications
- A comparison against established treatments for this condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Four single-ingredient SAHPRA registrations are valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ery-Tab (erythromycin) prescribing information, Arbor Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fda44eb6-7901-4b80-ba0b-216f6cacf3fd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

