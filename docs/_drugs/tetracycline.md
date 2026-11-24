---
layout: default
title: Tetracycline
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Tetracycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Bacterial infections, including urinary tract infection, bronchitis…"
monitor_inn: "Tetracycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
---

# Tetracycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Tetracycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Tetracycline is a broad-spectrum antibiotic, originally used for infections such as urinary tract infection, bronchitis, acne, pneumonia, gonorrhoea and conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **no registered clinical trials** and only **1 publication** (a two-patient case series) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including urinary tract infection, bronchitis, acne, pneumonia and conjunctivitis (SAHPRA indication text is not available for the registered product) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 7 of 14) |
| Number of SAHPRA Registrations | 14 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of tetracycline as: Bacterial 70S ribosome inhibitor ([ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, tetracycline is a tetracycline-class antibiotic. Its efficacy in bacterial infections, including chlamydial conjunctivitis, is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

Persistent superficial punctate keratitis can follow chlamydial follicular conjunctivitis, which tetracycline already treats. Tetracyclines are also reported to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects on the ocular surface, which could add a second plausible mechanism.

This prediction is largely an extension of the existing conjunctivitis indication rather than a distinct repurposing signal. In the single case report, the keratitis appeared *after* tetracycline or doxycycline had resolved the follicles, so it does not show that tetracycline treats the keratitis.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case series | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and the follicles resolved. Both then developed recurrent, bilateral punctate epithelial keratitis, so the report describes persistence of the problem after treatment rather than benefit. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| L/20.1.1/384 | Tetracycline Hci | tablet | Valid |
| 57/20.1.1/0164 | Lymevor 300 mg | capsule | Valid |
| 57/20.1.1/0165 | Lymedex 300 mg | capsule | Valid |
| B/20.1.1/201 | Capcycline Capsules | capsule | Valid |
| E/20.1.1/67 | Tetralysal 300 mg | capsule | Valid |

Showing 5 of 14 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions** (100 interactions were identified; main examples from the DDInter database):
- **Major:** isotretinoin, acitretin, aminolevulinic acid
- **Moderate:** ethinylestradiol, amoxicillin, ampicillin, aminophylline, atovaquone, aluminium hydroxide, bismuth subcitrate potassium, balsalazide, atracurium, sodium citrate, asparaginase (E. coli and Erwinia)
- **Minor:** acetazolamide, hydrochlorothiazide, amiloride

**Conditions flagged in the knowledge graph (not label text):** the drug-disease contraindication data flag, among others, liver failure and liver disease, kidney disease and kidney failure, uraemia, epilepsy, diabetes and diabetic ketoacidosis, neutropenia, agranulocytosis, G6PD deficiency, gout, blood coagulation disorders, *Clostridium difficile* colitis, atrioventricular block and respiratory failure. These are model-derived signals and should be checked against the approved label.

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is limited to one two-patient case series in which keratitis developed despite tetracycline treatment. There are no clinical trials, and the prediction overlaps with the existing conjunctivitis indication.

**To proceed, the following is needed:**
- Review of the SAHPRA-approved PI (indications, warnings, contraindications), as this safety information was not available
- Mechanism of action data
- Controlled clinical evidence in punctate epithelial keratoconjunctivitis, including whether an ocular formulation is needed, since the registered products are oral forms
- A comparison with the alternative candidates, which may have stronger evidence (see below)

<!-- review:begin za-lic-20261124b-tetracycline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "since the only registered product is an oral tablet" Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-tetracycline-1 -->

### Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 3 | Chronic rhinosinusitis | 0.9915 | L5 | Systematic reviews and a meta-analysis on doxycycline and other antibiotics, but no tetracycline-specific trials; class-level, indirect evidence |
| 2, 5, 9 | Chronic ethmoidal sinusitis, exposure keratitis, infective urethral stricture | 98.66–0.9915 | L5 | Indirect evidence only |
| 4, 6 | Paranasal sinus neoplasm | 0.9910 | L5 | Model prediction only |

Of these alternatives, only the post-treatment Lyme disease pilot (NCT05219929) offers direct tetracycline clinical data.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440) |
| 2026-11-24 | Corrected: "since the only registered product is an oral tablet" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

