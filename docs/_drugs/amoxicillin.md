---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-12
description: "Amoxicillin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections such as urinary tract infection…"
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Amoxicillin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic with relations recorded in the knowledge graph for urinary tract infection, otitis media, streptococcal and staphylococcal infections, and pneumonia.
The TxGNN model predicts it may be useful for **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** directly studying this condition, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections such as urinary tract infection, infectious otitis media, streptococcal infection and bacterial pneumonia (relations recorded in the knowledge graph; SAHPRA licence records contain no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 231 of 286; 38 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 286 (valid: 231, of which 38 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amoxicillin is known as a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, so its activity is directed at bacteria.

No mechanistic link to hyperamylasemia was identified. Amoxicillin has no known action on amylase metabolism or on pancreatic or salivary enzyme regulation. The high TxGNN score (0.9963) appears to be a network-based prediction without supporting clinical or literature data, and it should not be read as evidence of benefit.

The other top-ranked predictions show the same pattern. Of the seven, five (hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant haematological disease, and haematological disease with acquired peripheral neuropathy) have no trials or publications. The remaining two (blood group incompatibility and monoclonal gammopathy) have only indirect case reports or supportive-care studies, and septicaemic plague has only indirect laboratory and animal data. Septicaemic plague is the only one that is biologically plausible for an antibacterial, but beta-lactams are not first-line for plague, and in vitro data suggest limited activity against intracellular *Yersinia pestis*.

## Clinical Trial Evidence

Currently no related clinical trials are registered for hyperamylasemia.

## Literature Evidence

Currently no related literature is available for hyperamylasemia.

## South Africa Market Information

Amoxicillin is marketed in South Africa. The licence records contain no approved indication text. Essential Medicines List status could not be determined from the data compiled for this report. The 5 main registrations are listed below.

<!-- review:begin za-lic-20261105-amoxicillin-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Amoxicillin is marketed in South Africa, with 14 valid SAHPRA registrations, all single-ingredient records. The licence records contain no approved indication text." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 286 registrations for this drug, 231 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-amoxicillin-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 27/20.1.2/0325 | A-Lennon Amoxycillin | capsule | Valid (status not confirmed by SAHPRA) |
| 27/20.1.2/0439 | A-Lennon Amoxycillin | suspension | Valid (status not confirmed by SAHPRA) |
| 27/20.1.2/0440 | A-Lennon Amoxycillin | suspension | Valid (status not confirmed by SAHPRA) |
| 27/20.1.2/0472 | Saltermox s | suspension | Valid (status not confirmed by SAHPRA) |
| 27/20.1.2/0473 | Saltermox Sf 250 Mg | suspension | Valid (status not confirmed by SAHPRA) |

Showing 5 of 286 registrations (valid registrations first).

<!-- licenses:end -->

Other available forms in the records include drops (Amoxil D) and further injection, tablet and suspension products.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links amoxicillin to contraindication relations with several conditions. They include liver failure, liver disease, cholestasis, kidney disease, porphyria, myasthenia gravis, *Clostridium difficile* colitis, infectious mononucleosis, long QT syndrome and torsades de pointes, ventricular tachycardia, osteoporosis and bone fracture. These are not confirmed by SAHPRA label text and should be checked against the Professional Information (PI).
- **Drug Interactions (DDInter; 100 interactions recorded, examples shown):**
  - Major: methotrexate; live oral cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
  - Moderate: doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, dicoumarol, anisindione, mycophenolate mofetil, entecavir, balsalazide, and probiotic preparations (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*)
  - Minor: allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia is computational only, with no trials, no publications and no plausible mechanism. The evidence level is L5, so it does not support further development at this stage.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking amoxicillin to amylase regulation
- Any clinical or observational data on amoxicillin and serum amylase
- Mechanism of action data and SAHPRA Professional Information warnings and contraindications
- If a different indication is of interest, septicaemic plague could be considered as a research question only. It would need direct comparative efficacy data, given that beta-lactams are not first-line for plague.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "with 14 valid SAHPRA registrations, all single-ingredient records" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

