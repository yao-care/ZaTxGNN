---
layout: default
title: Captopril
parent: Model Prediction Only (L5)
nav_order: 97
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
last_modified_at: 2026-11-12
description: "Captopril: predicted new indication malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Captopril
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

## Captopril: ACE inhibitor (angiotensin-converting enzyme inhibition) → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Captopril is an angiotensin-converting enzyme (ACE) inhibitor, marketed in South Africa as oral tablets.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a score of 0.9928.
There are currently **no clinical trials** and only **1 publication** (a diagnostic case report, not a treatment study), so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 19 of 31; 6 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 31 (valid: 19, of which 6 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Captopril belongs to the ACE inhibitor class, which lowers angiotensin II production and so reduces activity of the renin-angiotensin system (RAS).

Malignant hypertension involves strong RAS activation and acute kidney injury. Blocking ACE is therefore biologically plausible. However, this is a theoretical link only. The single linked publication describes captopril used as a diagnostic test (renography), not as a treatment. The high score is not backed by clinical data. In severe, rapidly progressing hypertensive renal disease, a sudden fall in blood pressure or a decline in kidney function with ACE inhibition would also be a practical concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | Positive captopril renography (a diagnostic test) in a patient with renin-dependent hypertension caused by a renal cell carcinoma rather than renal artery stenosis; hypertension resolved after nephrectomy. Not therapeutic evidence. |

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 27/7.1/0398 | Capace | tablet | Valid |
| 29/7.1/0228 | Mylan captopril | tablet | Valid |
| 31/7.1/0039 | Capto-Hexal 12.5 | tablet | Valid |
| 31/7.1/0040 | Captohexal 25 | tablet | Valid (status not confirmed by SAHPRA) |
| 31/7.1/0658 | Bio-captopril | tablet | Valid |

Showing 5 of 31 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status is not recorded in the data compiled for this report.

<!-- review:begin za-lic-20261105-captopril-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All three registrations are currently valid. Essential Medicines List (EML) status is not recorded in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 31 registrations for this drug, 19 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-captopril-1 -->

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

**Drug Interactions**: The interaction screen returned 100 records. Those listed are mostly of moderate severity:
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
- Glucose-lowering drugs (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide)
- Others: bupropion, morphine, acetylsalicylic acid, dronabinol
- Minor: aluminium hydroxide, calcium carbonate

The monitoring needs for these combinations should be checked against the PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9928), but there are no clinical trials and no therapeutic studies in this condition. The only publication is a diagnostic case report, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or observational studies of captopril as treatment in malignant hypertensive renal disease
- Detailed mechanism of action data
- Review of SAHPRA-approved Professional Information for warnings and contraindications
- Assessment of risks in this population, particularly hypotension and worsening kidney function

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All three registrations are currently valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

