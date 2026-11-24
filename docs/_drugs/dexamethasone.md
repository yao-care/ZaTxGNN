---
layout: default
title: Dexamethasone
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Dexamethasone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
description: "Dexamethasone: predicted new indication Alopecia mucinosa (evidence level L5). In South Africa: 50 SAHPRA registrations (37 valid)"
---

# Dexamethasone
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

## Dexamethasone: Alopecia mucinosa
{: .text-alpha }

## One-Sentence Summary

Dexamethasone is a corticosteroid with a long record of clinical use in several inflammatory and endocrine conditions.
The TxGNN model predicts it may be effective for **alopecia mucinosa**, but **no clinical trials and no publications** were found for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 37 of 50; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 50 (valid: 37, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dexamethasone: "Dexamethasone is a corticosteroid with anti-inflammatory effects and low mineralocorticoid activity. The precise mechanism of action in multiple myeloma is unknown. Dexamethasone induces apoptosis of multiple myeloma cells." ([DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129), label version 2026-01-09; accessed 2026-11-19.) Based on general pharmacology, dexamethasone is a glucocorticoid with strong anti-inflammatory and immunosuppressive effects, and it is used in many inflammatory conditions.

Alopecia mucinosa is an inflammatory follicular skin disorder, so an anti-inflammatory corticosteroid is conceptually plausible. This link is a hypothesis only. The very high TxGNN score (0.9999) is a computational output and does not replace clinical evidence. Topical and injectable corticosteroid products are already registered in South Africa, so formulation routes exist, but route suitability for this skin condition has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Dexamethasone-containing products are marketed in South Africa. Approved indication text is not recorded in the local data. Essential Medicines List status is not recorded in the data compiled for this report.

<!-- review:begin za-lic-20261105-dexamethasone-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Dexamethasone-containing products are marketed in South Africa, with 9 valid single-ingredient registrations and no cancelled registrations. Approved indication text is not recorded in the local data." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-dexamethasone-1 -->

<!-- review:begin za-lic-20261105-dexamethasone-2 -->

> **Review correction (2026-11-05)**: Originally stated: "The remaining four registrations are Spersadex comp 5ml (drops), Maxitrol 3.5g (eye ointment), Covomycin D and Tobradex 3.5g (eye ointment)." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-dexamethasone-2 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 44/15.2/0045 | Ozurdex intravitreal | Imp | Valid |
| 54/32/0323 | Neofordex | tablet | Valid |
| H1143 | Maxidex 5ml | drops | Valid |
| 33/21.5.1/0512 | Pharma-q dexamethasone phosphate ampoule | injection | Valid |
| 41/21.5.1/0814 | Tagalon | injection | Valid |

Showing 5 of 50 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

**Contraindications and warnings:** Label-based warnings and contraindications are not available in the data compiled for this report.

**Drug Interactions:** The interaction screening returned 100 entries. Examples of the main ones:
- **Major:** fentanyl, adalimumab
- **Moderate:** zidovudine, paclitaxel, isotretinoin, abemaciclib, acalabrutinib, acarbose, acebutolol, acetazolamide, codeine, dihydrocodeine, ketorolac, nifedipine, ibuprofen
- **Minor:** dolutegravir, lidocaine, formoterol

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for alopecia mucinosa is the model prediction. There are no trials or publications on this disease, so the evidence level is L5.

**To proceed, the following is needed:**
- Published case series or clinical studies of corticosteroids in alopecia mucinosa
- Mechanism of action data for dexamethasone
- Review of the SAHPRA Professional Information for warnings and contraindications
- Assessment of which route (topical, intralesional or systemic) would suit this condition, with a safety plan for long-term corticosteroid exposure

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "with 9 valid single-ingredient registrations and no cancelled registrations" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "The remaining four registrations are Spersadex comp 5ml (drops), Maxitrol 3.5g (eye ointment), Covomycin D and Tobradex 3.5g (eye ointment)" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

