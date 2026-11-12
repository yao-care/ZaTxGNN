---
layout: default
title: Acetylsalicylic Acid
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 7
monitor_inn: "Acetylsalicylic acid"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-12
description: "Acetylsalicylic Acid: predicted new indication atrophoderma vermiculata (evidence level L5). Approved use: Not recorded in the local data"
---

# Acetylsalicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Acetylsalicylic acid: COX inhibitor and antiplatelet agent → atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a cyclooxygenase (COX) inhibitor with antiplatelet activity and is marketed in South Africa. The TxGNN model predicts it may be effective for **atrophoderma vermiculata**, a rare follicular atrophic skin disorder. The data compiled for this report contain **no clinical trials and no publications** supporting this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 108 of 160; 3 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 160 (valid: 108, of which 3 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this drug are not available in the data compiled for this report. In general, aspirin irreversibly inhibits COX enzymes. This reduces prostaglandin synthesis and, through platelet COX-1, thromboxane A2 formation and platelet aggregation.

No plausible mechanistic link has been established between COX inhibition or antiplatelet activity and atrophoderma vermiculata. This is a rare condition of follicular atrophy, mainly on the cheeks. The high score reflects a pattern found by the model, not pharmacological or clinical support. No trials or literature were found to test the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR records were identified in the data compiled for this report.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

The local records do not include approved-indication text. Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-acetylsalicylic_acid-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Four SAHPRA registrations are recorded as valid. The local records do not include approved-indication text." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 160 registrations for this drug, 108 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-acetylsalicylic_acid-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 29/2.7/0767 | Ecotrin | tablet | Valid |
| 31/2.8/0071 | Disprin Cardiocare | effervescent tablet | Valid |
| 31/8/0413 | Bayer aspirin cardio | tablet | Valid |
| 43/8/0830 | Soluspirin cv | effervescent tablet | Valid |
| 51/8/2010 | Coprin 100 Mg | tablet | Valid |

Showing 5 of 160 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 recorded interactions; the first 20 were available for review. Major-level interactions among them include:
  - Acalabrutinib
  - Acetazolamide
  - Ketorolac
  - Trastuzumab emtansine
  - Ibuprofen
  - Fondaparinux

  Moderate and minor interactions were also listed, for example with nifedipine, hydrocortisone, ethanol, alendronic acid, fluvoxamine, fosinopril and furosemide. Many of these combinations raise bleeding risk or affect renal function and blood pressure.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score of 0.9959. There are no trials or publications for atrophoderma vermiculata, and no plausible mechanistic link to aspirin pharmacology. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Mechanistic rationale linking COX inhibition or antiplatelet activity to the pathology of atrophoderma vermiculata
- Any case series, preclinical work or clinical studies in this condition
- Dermatology expert review of the clinical plausibility and a comparison with current management options
- Full mechanism-of-action data and the SAHPRA Professional Information warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Four SAHPRA registrations are recorded as valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

