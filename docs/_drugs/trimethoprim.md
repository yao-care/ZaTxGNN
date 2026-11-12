---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Trimethoprim
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

## Trimethoprim: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infection, ear and eye infections, pneumocystosis and shigellosis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** were retrieved for this prediction, so the evidence rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 53 of 76; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 76 (valid: 53, of which 5 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trimethoprim is an antibacterial whose efficacy in bacterial infections is established, and it has been used in ophthalmic combinations (with polymyxin B) for bacterial conjunctivitis and blepharoconjunctivitis. These are already listed among its original indications.

The prediction therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The main limitation is that punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or non-infectious, and an antibacterial would be unlikely to help in those cases. The prediction is plausible only for a bacterial subset, and this has not been tested.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## South Africa Market Information

Approved indication text was not available in the data compiled for this report. Essential Medicines List (EML) status could not be confirmed from the data provided.

<!-- review:begin za-lic-20261105-trimethoprim-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All nine registrations are valid single-ingredient products. Approved indication text was not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 76 registrations for this drug, 53 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-trimethoprim-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 27/20.2/0077 | Xeroprim | tablet | Valid |
| 27/20.2/0302 | Pharma-Q Co Trimoxazole  Tablets | tablet | Valid |
| 27/20.2/0335 | Dynazole | suspension | Valid |
| 28/20.2/0389 | Xerazole Suspension | suspension | Valid |
| 28/20.2/0416 | Novatrim | tablet | Valid |

Showing 5 of 76 registrations (valid registrations first).

<!-- licenses:end -->

No ophthalmic formulation appears among the registrations listed, which matters for the predicted ocular indication.

<!-- review:begin za-lic-20261105-trimethoprim-2 -->

> **Review correction (2026-11-05)**: Originally stated: "The remaining four registrations are Purbac injection 5ml (L/20.2/336), Xerazole Suspension (28/20.2/0389), Co-Trimoxazole 960 Biotech (W/20.2.1/88) and Cotrizid (52/20.2/0208). No ophthalmic formulation appears among the registrations listed, which matters for the predicted ocular indication." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 76 registrations for this drug, 53 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-trimethoprim-2 -->

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** inherited porphyria and other porphyrias, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, G6PD deficiency, folic acid deficiency anaemia, and several others (glycogen storage disease, cystinuria, galactosaemia, perinatal necrotizing enterocolitis, pyoureter).

**Drug Interactions:** 100 interactions were identified. Major-level interactions are with potassium salts (potassium chloride, potassium citrate, potassium bicarbonate, potassium gluconate), reflecting a risk of raised potassium. Moderate-level interactions include metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid and sapropterin.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials or publications for punctate epithelial keratoconjunctivitis (Evidence Level L5). Many cases are viral or non-infectious, and no ophthalmic trimethoprim product was identified among the South African registrations.

**To proceed, the following is needed:**
- Clinical or literature evidence of trimethoprim (or polymyxin B/trimethoprim) in punctate epithelial keratoconjunctivitis, ideally stratified by bacterial versus viral cause
- Confirmation of whether an ophthalmic formulation is registered or obtainable in South Africa
- SAHPRA Professional Information warnings and contraindications
- Mechanism of action data to support the mechanistic link

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All nine registrations are valid single-ingredient products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-05 | Removed: "The remaining four registrations are Purbac injection 5ml (L/20.2/336), Xerazole Suspension (28/20.2/0389), Co-Trimoxazole 960 Biotech (W/20" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

