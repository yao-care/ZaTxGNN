---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia"]
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salicylic Acid
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

## Salicylic Acid: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salicylic acid is a long-established keratolytic and anti-inflammatory agent, used for skin conditions such as acne, seborrhoeic dermatitis and tinea, and for inflammatory joint conditions.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 31 of 38; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 38 (valid: 31, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Salicylic acid is proposed to act through inhibition of cyclooxygenase (COX) enzymes, which reduces prostaglandin synthesis and inflammation. However, no publicly available bioactivity data confirming this at a specific molecular target were found. Pharmacology data list ASIC3 as an associated target, but this is not confirmed as a primary mechanism.

The link to papillary conjunctivitis is plausible but indirect. Salicylic acid is already listed for allergic rhinitis, another allergic mucosal condition, and papillary conjunctivitis involves allergic or inflammatory irritation of the conjunctiva. Salicylic acid is also keratolytic and irritating to mucous membranes, so tolerability in the eye is a real concern. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

### Other Predictions Reviewed

Nine other predictions were also evaluated. All lack trials and literature.

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9978 | L5 | No credible mechanistic link; likely a TxGNN model (deep learning) artefact |
| Brachydactyly-syndactyly syndrome | 0.9973 | L5 | No credible mechanistic link |
| Brachyolmia-amelogenesis imperfecta syndrome | 0.9955 | L5 | No credible mechanistic link |
| Rosacea conjunctivitis | 0.9953 | L5 | Weak, speculative link via facial inflammatory skin disease; eye irritation concern |
| Acromesomelic dysplasia, Hunter-Thompson type | 0.9952 | L5 | No credible mechanistic link |
| Pseudoachondroplasia | 0.9951 | L5 | No credible mechanistic link |
| Myosclerosis | 0.9949 | L5 | Tenuous, speculative link; no evidence on fibrosis |
| Brachyolmia | 0.9944 | L5 | No credible mechanistic link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 48/2.7/0609 | Cancard | tablet | Valid |
| G1995 | Wart magic liquid (stx) | lotion | Valid |
| G2311 (ACT 101/1965) | Posalfilin | ointment | Valid (status not confirmed by SAHPRA) |
| H/13.4.1/32 | Diprosalic | ointment | Valid |
| H1494 | Pyralvex | Not recorded | Valid |

Showing 5 of 38 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status was not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-salicylic_acid-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both registrations are valid and are topical products. Essential Medicines List (EML) status was not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 38 registrations for this drug, 31 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-salicylic_acid-1 -->

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned one pharmacology entry, linking salicylic acid to the ASIC3 target. No drug-drug interactions with severity levels were identified.
- **Local tolerability** (from the mechanistic assessment): Topical salicylic acid is keratolytic and irritating to mucous membranes and the eye, which is a significant concern for any ocular use.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests only on a computational score, with no trials or literature, and ocular irritation is a major tolerability concern. Most other top-ranked predictions have no credible mechanism. The only one with a plausible class-level rationale is spondyloarthropathy, which is a research question rather than an actionable candidate.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A systematic literature search on salicylates in allergic and papillary conjunctivitis, and a separate review for spondyloarthropathy
- Assessment of ocular tolerability and of whether a suitable ophthalmic formulation exists, since the registered products are topical skin preparations (lotion and ointment) only
- Approved indication text for the registered Diprosalic products

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both registrations are valid and are topical products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

