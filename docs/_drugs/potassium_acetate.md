---
layout: default
title: Potassium Acetate
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "POTASSIUM ACETATE"
predicted_indications: ["renal tubular acidosis"]
description: "Potassium Acetate: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Potassium Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Potassium Acetate: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Potassium acetate is a potassium salt originally used to treat potassium deficiency.
The TxGNN model predicts it may be useful for **renal tubular acidosis (RTA)**,
but **no clinical trials or publications** were found for this direction, so the prediction currently rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 11) |
| Number of SAHPRA Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, potassium acetate supplies potassium, and the acetate is metabolised in the body to bicarbonate. In theory this could correct both low potassium (hypokalaemia) and metabolic acidosis, two features common in distal (type 1) and proximal (type 2) RTA.

Potassium citrate and potassium bicarbonate, which are also alkali-potassium salts, are already used clinically in RTA. This analogy is indirect and has **not been verified for potassium acetate itself**.

Caution is needed in type 4 RTA (hypoaldosteronism). Hyperkalaemia is typical there, so potassium supplementation could be harmful. The prediction rests only on the TxGNN score, with no supporting clinical or published evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Approved indication text was not available for any of them. Potassium acetate in these products is a component of parenteral nutrition or infusion preparations, not a standalone potassium product. Essential Medicines List (EML) status could not be determined from the data compiled for this report.

<!-- review:begin za-lic-20261105-potassium_acetate-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All five registrations are valid single-ingredient products. Approved indication text was not available for any of them." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 11 registrations for this drug, 11 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-potassium_acetate-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 41/25/0756 | Nutriflex lipid plus 2500ml | Tpn | Valid |
| 41/25/0757 | Nutriflex lipid peri 2500ml | Tpn | Valid |
| 41/25/0759 | Nutriflex lipid special 2500ml | Tpn | Valid |
| 49/25/0065 | Nutriflex Omega Specialized | infusion | Valid |
| 49/25/0066 | Nutriflex Omega Plus | infusion | Valid |

Showing 5 of 11 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 40 interactions are recorded. Examples of the main ones:
  - **Major**: amiloride (a potassium-sparing diuretic), and the ACE inhibitor/ARB drugs benazepril, olmesartan, valsartan and azilsartan medoxomil. These combinations raise the risk of hyperkalaemia.
  - **Moderate**: aliskiren.
  - **Minor**: multiple insulin preparations (for example insulin aspart, degludec, detemir, glargine, glulisine, lispro and human insulin).
- **Type 4 RTA**: Hyperkalaemia is typical in this subtype, so potassium supplementation could be harmful (see the mechanism section above).

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or publications for renal tubular acidosis, and the mechanism data and PI safety information are missing. The five local registrations are infusion or parenteral nutrition products, whose compatibility with RTA treatment has not been assessed. Potassium supplementation may be harmful in type 4 RTA.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI) warnings and contraindications, which are a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank)
- A literature and trial search for potassium acetate, or related alkali-potassium salts, in RTA subtypes
- An assessment of whether an appropriate oral or other suitable formulation is available in South Africa, since current registrations are parenteral
- A safety review of the hyperkalaemia-related interactions (potassium-sparing diuretics, ACE inhibitors, ARBs) and of RTA subtype selection

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All five registrations are valid single-ingredient products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

