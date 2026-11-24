---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 9
monitor_inn: "AMLODIPINE"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-24
description: "Amlodipine: predicted new indication brain stem infarction (evidence level L5). In South Africa: 318 SAHPRA registrations (287 valid)"
---

# Amlodipine
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

## Amlodipine: dihydropyridine calcium channel blocker → brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Amlodipine is a dihydropyridine calcium channel blocker that relaxes vascular smooth muscle and lowers blood pressure.
The TxGNN model predicts it may be useful for **brain stem infarction**, with a score of **0.9994**.
**No clinical trials and no publications** were found that directly study this disease, so the prediction currently rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | brain stem infarction |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 287 of 318; 12 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 318 (valid: 287, of which 12 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for amlodipine: "Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites." ([DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487), label version 2026-09-28; accessed 2026-11-19.) Amlodipine is a dihydropyridine calcium channel blocker. It reduces calcium entry into vascular smooth muscle, which lowers vascular resistance and blood pressure.

The proposed link to brain stem infarction is indirect. Blood pressure control and cerebrovascular protection are plausible mechanisms in ischaemic cerebrovascular disease. The high score probably reflects the model's closeness to other cerebrovascular conditions rather than disease-specific evidence.

No trial or publication in the data compiled for this report studies brain stem infarction, so this link is a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

---

## Literature Evidence

Currently no related literature available for brain stem infarction.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/7.1/0480 | Norcard | tablet | Valid |
| 36/7.1/0481 | Norcard | tablet | Valid |
| 37/7.1/0376 | Amlodipine 5 oethmaan | tablet | Valid |
| 37/7.1/0377 | Amlodipine 10 oethmaan | tablet | Valid |
| 37/7.1/0378 | Amlodipine 5 Biotech | tablet | Valid |

Showing 5 of 318 registrations (valid registrations first).

<!-- licenses:end -->

- Amlodipine is **marketed** in South Africa.
- Approved indication text is not recorded in the local data.
- Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-amlodipine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "The local data show 20 valid SAHPRA registrations and no cancelled ones. All are single-ingredient records, but the records may be partial. / Approved indication text is not recorded in the local data." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amlodipine-1 -->

<!-- review:begin za-lic-20261124b-amlodipine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The detailed registration table is added by the site programme from the licence records." Removed: it said the registration table is provided separately; the programme-generated registration table is now shown at the start of South Africa Market Information. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-amlodipine-1 -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. The first 20 shown are all rated Moderate:
  - Corticosteroids: hydrocortisone, betamethasone, budesonide, dexamethasone
  - Calcium salts: acetate, carbonate, chloride, citrate, glubionate, glucoheptonate, gluconate, lactate, phosphate
  - Others: aprepitant, acetylsalicylic acid, bupropion, canagliflozin, dapagliflozin, clarithromycin, clotrimazole
- **Conditions flagged for caution** (not taken from label text; to be verified against the Professional Information): liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, hypothyroidism, angioedema (including hereditary and ACE-inhibitor-type forms), systemic lupus erythematosus, myopathy and muscle disease, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, hypotension, and hyperparathyroidism.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trial or publication directly studies brain stem infarction (evidence level L5). Without disease-specific evidence, the mechanistic link is hypothetical.

**To proceed, the following is needed:**
- Disease-specific clinical or preclinical evidence in brain stem or posterior circulation infarction
- Detailed mechanism of action data
- Review of the SAHPRA Professional Information for warnings and contraindications
- A safety assessment for hypotension in acute ischaemic settings, plus a review of interactions with commonly co-prescribed medicines

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "The local data show 20 valid SAHPRA registrations and no cancelled ones. All are single-ingredient records, but the records may be partial" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |
| 2026-11-24 | Removed: "The detailed registration table is added by the site programme from the licence records." | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

