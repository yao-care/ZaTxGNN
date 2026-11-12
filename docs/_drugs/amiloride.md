---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 24
evidence_level: L5
indication_count: 5
monitor_inn: "AMILORIDE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-12
description: "Amiloride: predicted new indication malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiloride
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

## Amiloride: potassium-sparing diuretic (ENaC blocker) → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that is marketed in South Africa. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** in the data compiled for this report address this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 14; 3 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 14 (valid: 11, of which 3 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Amiloride is generally known as a potassium-sparing diuretic that blocks epithelial sodium channels, and it has a blood-pressure-lowering effect. This makes a link to hypertension-related kidney disease plausible in theory.

The prediction looks like a neighbour of the hypertension-related uses of the drug. Malignant hypertensive renal disease is a severe, acute form of kidney damage from very high blood pressure. No study in the compiled data tests amiloride in this condition. Its potassium-retaining effect is also a concern when kidney function is impaired, because of the risk of hyperkalaemia.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 28/18.1/0684 | Dezretic 5mg/50mg | tablet | Valid |
| C/18.1/215 | Moduretic | tablet | Valid (status not confirmed by SAHPRA) |
| L/18.1/396 | Amiloretic 50mg/5mg | tablet | Valid |
| Q/18.1/168 | Sandoz Co-Amilozide | tablet | Valid (status not confirmed by SAHPRA) |
| R/18.1/200 | Moduretic Hs | tablet | Valid (status not confirmed by SAHPRA) |

Showing 5 of 14 registrations (valid registrations first).

<!-- licenses:end -->

The product is available as an oral tablet. The approved indication text is not recorded in the local data. Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-amiloride-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All four registrations are currently valid, and the product is available as an oral tablet. The approved indication text is not recorded in the local data." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 14 registrations for this drug, 11 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amiloride-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. Examples at moderate level include hydrocortisone, betamethasone, dexamethasone, budesonide, metformin, bupropion, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Doxycycline, amoxicillin and cimetidine are listed as minor.
- **Potassium and renal caution**: Hyperkalaemia in patients with impaired kidney function is the main safety concern for this prediction, since the predicted disease involves the kidney.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9982), but there are no trials or publications on this disease, so the evidence level is L5. The hyperkalaemia risk in renal impairment adds a safety concern.

**To proceed, the following is needed:**
- Published or registered studies of amiloride in malignant hypertensive renal disease, or a well-supported mechanistic rationale
- Mechanism-of-action data
- SAHPRA Professional Information warnings and contraindications, to complete safety screening
- A potassium and renal-function monitoring plan for patients with kidney impairment

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All four registrations are currently valid, and" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

