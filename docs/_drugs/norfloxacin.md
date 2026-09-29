---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
---

# Norfloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Norfloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Norfloxacin is an oral fluoroquinolone antibacterial. The TxGNN model predicts it may be relevant to **hyperamylasemia**, a laboratory finding of raised blood amylase. There are **no clinical trials** and **no publications** supporting this prediction, and no plausible mechanism, so it looks like a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local registration records (norfloxacin is an antibacterial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available. Norfloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its usefulness is in treating bacterial infections.

Hyperamylasemia is a laboratory finding, not an infection. Its usual causes are pancreatic, salivary or renal, and an antibacterial has no known way to treat any of them. The high score (0.997) is identical to that of another unrelated candidate (polyclonal hyperviscosity syndrome), which points to a computational artifact. I found no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered. This includes ClinicalTrials.gov and the ICTRP registries (SANCTR and PACTR entries were not found in the data supplied).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/20.1.1/0657 | Utifloxa | Tablet | Not stated in the source data |
| Reg. No. 32/20.1.1/0377 | Floxin | Tablet | Not stated in the source data |

Only oral tablets are registered. Essential Medicines List (EML) status was not included in the data supplied and should be checked separately.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-interaction records were found. Fluoroquinolones as a class carry a peripheral neuropathy warning.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5). There are no trials or publications, and hyperamylasemia has no biological connection to norfloxacin's antibacterial action.

**Other candidates in this pack:** None of the other nine candidates is ready to advance either. Only two have any supporting literature, and both remain Research Questions at L4:
- **Punctate epithelial keratoconjunctivitis (rank 5):** two case reports on microsporidial keratoconjunctivitis. Full-text review is needed to establish whether norfloxacin was actually used and whether it worked.
- **Septicemic plague (rank 10):** animal and in vitro studies only, none specific to norfloxacin.

**To proceed, the following is needed:**
- The SAHPRA package insert, including warnings and contraindications (this blocks safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the rank 5 and rank 10 literature to see whether norfloxacin-specific data exist
- Confirmation of the approved indications for the two SAHPRA registrations

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

