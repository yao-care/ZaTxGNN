---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 111
evidence_level: L5
indication_count: 8
monitor_inn: "Chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-12
description: "Chloramphenicol: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Chloramphenicol
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

## Chloramphenicol: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is an antibacterial drug that is currently marketed in South Africa in topical and ear/eye preparations. The TxGNN model predicts it may be relevant to **diffuse scleroderma**, but **no clinical trials** and only **4 in vitro laboratory publications** are linked to this prediction, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 21 of 36; 4 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 36 (valid: 21, of which 4 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for this drug. Chloramphenicol is a well-known antibacterial agent, and its established use is against bacterial and rickettsial infections. Nothing in the data compiled for this report links this activity to the biology of scleroderma, which is an autoimmune, fibrosing disease.

The four linked publications are laboratory studies of collagen gene regulation in scleroderma fibroblasts (COL1A1 promoter activity, Smad3/Sp1/p300 interactions, TGF-beta signalling). None of them tests chloramphenicol as a treatment. The association most likely arises because chloramphenicol acetyltransferase (CAT) reporter-gene assays are widely used in this type of laboratory work. This looks like a technical artefact rather than a pharmacological link. The high model score is therefore not supported by the available evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | In vitro / basic research | Arthritis and Rheumatism | Transcriptional regulation of the COL1A1 collagen gene in dermal fibroblasts from patients with diffuse systemic sclerosis; role of intronic sequences |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | In vitro / basic research | Arthritis and Rheumatism | Promoter elements and transcription factors behind up-regulated COL1A1 expression in systemic sclerosis |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | In vitro / basic research | Arthritis and Rheumatism | Blockade of TGF-beta signalling reduced excess collagen synthesis in scleroderma fibroblasts |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | In vitro / basic research | Rheumatology (Oxford) | Constitutively phosphorylated Smad3 interacts with Sp1 and p300 in scleroderma fibroblasts |

None of these studies evaluates chloramphenicol as a therapy.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| H1193 | Chloramex Opthalmic Ointment 3.5G | eye ointment | Valid |
| H1207 | Chlornicol  3.5G | eye ointment | Valid |
| H1217 | Chloromycetin | eye ointment | Valid |
| V/15.1/294 | Chlorphen 3.5g | eye ointment | Valid (status not confirmed by SAHPRA) |
| V/20.1.1/227 | Chlorphen 40ml | injection | Valid (status not confirmed by SAHPRA) |

Showing 5 of 36 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-chloramphenicol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All four registrations are single-ingredient products and currently valid. Essential Medicines List status is not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 36 registrations for this drug, 21 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-chloramphenicol-1 -->

## Safety Considerations

- **Haematological and organ-related cautions:** Chloramphenicol is associated with blood-related toxicity. Conditions on its caution list include thrombocytopenia, anaemia, aplastic anaemia, agranulocytosis and neutropenia, as well as kidney disease, liver disease, gallbladder disease, peripheral neuropathy, optic neuritis, acute intermittent porphyria and paroxysmal nocturnal haemoglobinuria. These are not taken from product label text and must be checked against the SAHPRA-approved Professional Information (PI).
- **Drug Interactions:** 100 interactions were found in total. Examples of major interactions are **cisapride** and **naloxegol**. Examples of moderate interactions include sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), repaglinide, saxagliptin, metronidazole, simvastatin, rosuvastatin, aprepitant, budesonide, iron, eliglustat, naldemedine and nitisinone.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on laboratory studies of scleroderma fibroblasts that do not test chloramphenicol, and a reporter-gene artefact is the likely explanation. There are no clinical trials and no plausible mechanism, and the drug's known blood toxicity is a further concern. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a credible pharmacological rationale for scleroderma
- Preclinical studies that directly test chloramphenicol in scleroderma models
- Safety information from the SAHPRA-approved Professional Information, including a risk assessment for blood toxicity in a chronic disease setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All four registrations are single-ingredient products and currently valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

