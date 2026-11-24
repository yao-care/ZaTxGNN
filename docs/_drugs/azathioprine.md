---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 7
monitor_inn: "AZATHIOPRINE"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
last_modified_at: 2026-11-24
description: "Azathioprine: predicted new indication colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). In South Africa: 8 SAHPRA registrations (6 valid)"
---

# Azathioprine
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

## Azathioprine: purine-antimetabolite immunosuppressant → colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## One-Sentence Summary

Azathioprine is an oral immunosuppressant that acts as a purine antimetabolite and is marketed in South Africa.
The TxGNN model predicts it may be relevant to **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome.
No clinical trials or publications were found for this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 8) |
| Number of SAHPRA Registrations | 8 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of azathioprine as: Amidophosphoribosyltransferase inhibitor; DNA inhibitor ([ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542), CC BY-SA 3.0; accessed 2026-11-19.) Azathioprine is generally known as a purine-antimetabolite immunosuppressant that suppresses lymphocyte proliferation.

The predicted condition is a rare developmental syndrome affecting the eyes and skeleton. No mechanistic link between azathioprine and this condition is established. Immunosuppression is not expected to alter a developmental genetic disorder. The very high model score reflects a pattern in the model's training data, not biological or clinical support. On the available information, the prediction is not mechanistically plausible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 36/26/0006 | Azamun | tablet | Valid |
| 37/26/0692 | Azathioprine 50 pch | tablet | Valid |
| D/26/98 | Imuran | tablet | Valid |
| H2746 | Imuran vial powder for reconstitution | injection | Valid |
| L/26/413 | Azapress | tablet | Valid |

Showing 5 of 8 registrations (valid registrations first).

<!-- licenses:end -->

The data compiled for this report does not show Essential Medicines List status.

<!-- review:begin za-lic-20261105-azathioprine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both registrations are valid single-ingredient products for oral use. The data compiled for this report does not show Essential Medicines List status." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-azathioprine-1 -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. The main ones listed are:
  - **Moderate**: mesalazine, balsalazide, olsalazine, sulfasalazine.
  - **Minor**: zinc acetate, zinc gluconate, zinc sulfate.
  - Several other interactions are recorded with an unclassified severity (for example amphotericin B, acetylsalicylic acid, metformin, omeprazole and pantoprazole).

Azathioprine is myelosuppressive and immunosuppressive. Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5) and no plausible mechanism. A high model score alone is not enough to justify further work.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence linking azathioprine to this condition
- A plausible mechanistic rationale
- Mechanism-of-action data and the SAHPRA package insert safety information (warnings and contraindications)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both registrations are valid single-ingredient products for oral use" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism-of-action data for azathioprine is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

