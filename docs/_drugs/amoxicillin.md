---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-30
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
| South Africa Market Status | Marketed (valid licences: 12 of 14) |
| Number of Registrations | 14 (valid: 12) |
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

Amoxicillin is marketed in South Africa, with 14 valid SAHPRA registrations, all single-ingredient records. The licence records contain no approved indication text. Essential Medicines List status could not be determined from the data compiled for this report. The 5 main registrations are listed below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36/20.1.2/0115 | Zaloxy | Suspension | Not stated in the records |
| Z/20.1.2/327 | Spectramox C 250 | Capsule | Not stated in the records |
| J/20.1.2/0437 | Suprapen 500 | Capsule | Not stated in the records |
| 41/20.1.2/0532 | Bindoclav | Tablet | Not stated in the records |
| 41/20.1.2/0977 | Gulf amoxy co powder for injection vial | Injection | Not stated in the records |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

