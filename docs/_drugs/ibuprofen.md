---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 7
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-20
description: "Ibuprofen: predicted new indication acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In South Africa: 150 SAHPRA registrations (128 valid)"
---

# Ibuprofen
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

## Ibuprofen: Non-selective NSAID (COX inhibitor) → acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Ibuprofen is a widely marketed non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, with a score of 0.9974.
Currently there are **no clinical trials and no publications** supporting this prediction, so it rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 128 of 150; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 150 (valid: 128, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ibuprofen: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), label version 2026-01-29; accessed 2026-11-19.) Ibuprofen is generally known as a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin production, but this was not supplied here.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia caused by loss-of-function mutations in the CDMP1/GDF5 gene, which disrupts cartilage and bone development. Blocking prostaglandin synthesis has no evident way of correcting this genetic defect.

The high score (0.9974) is a computational output only. No mechanistic link is supported by the available data, so the prediction should be treated as a hypothesis with weak biological plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Ibuprofen is marketed in South Africa. Indication text is not recorded in the local data. The table below lists five of the registrations.

<!-- review:begin za-lic-20261105-ibuprofen-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Ibuprofen is marketed in South Africa, and all 19 registrations are valid. Indication text is not recorded in the local data." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 151 registrations for this drug, 130 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-ibuprofen-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 27/2.7/0240 | Ibu | tablet | Valid |
| 29/3.1/0727 | Ibunate | tablet | Valid |
| 30/3.1/0440 | Unifen | tablet | Valid |
| 34/2.7/0193 | Advil liqui-gel | capsule | Valid |
| 34/2.7/0290 | Nurofen Express | tablet | Valid |

Showing 5 of 150 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records; the first 20 are summarised here.
  - **Major**: acetylsalicylic acid.
  - **Moderate**: acetohexamide, aprepitant, balsalazide, betamethasone, budesonide, chlorpropamide, dexamethasone, dexfenfluramine, exenatide, fenfluramine, glimepiride, glipizide, glyburide, hydrocortisone, kanamycin, levofloxacin.
  - **Minor**: famotidine, ranitidine, cimetidine.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanistic link to the underlying genetic cause of the disease. It remains a model prediction only (evidence level L5).

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking ibuprofen to GDF5-related skeletal development
- Preclinical or clinical evidence that directly studies this disease
- SAHPRA Professional Information, including warnings and contraindications
- A safety assessment for the target population, which would likely include children and pregnancy-related exposure

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "and all 19 registrations are valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

