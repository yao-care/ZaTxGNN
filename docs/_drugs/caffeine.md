---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 8
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
last_modified_at: 2026-11-20
description: "Caffeine: predicted new indication nasal cavity disease (evidence level L5). In South Africa: 205 SAHPRA registrations (136 valid)"
---

# Caffeine
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

## Caffeine: adenosine receptor antagonist and phosphodiesterase inhibitor → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Caffeine is a methylxanthine stimulant that is marketed in South Africa mainly as a component of analgesic, cold and flu, and sinus products.
The TxGNN model predicts it may be useful for **nasal cavity disease**, but **no clinical trials** and **3 publications** were found, none of which study a nasal cavity disease itself.
This is therefore a model prediction without direct supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 136 of 205; 5 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 205 (valid: 136, of which 5 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for caffeine: "Caffeine is structurally related to other methylxanthines, theophylline, and theobromine. It is a bronchial smooth muscle relaxant, a CNS stimulant, a cardiac muscle stimulant, and a diuretic. Although the mechanism of action of caffeine in apnea of prematurity is not known, several mechanisms have been hypothesized." ([DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a), label version 2026-07-29; accessed 2026-11-19.) From general pharmacology, caffeine blocks adenosine receptors and inhibits phosphodiesterase. Bitter taste receptors are also expressed in the airways, including the nasal cavity, and a review describes their pharmacology. Whether caffeine acts on them in a way that matters clinically is not shown.

Caffeine is registered in South Africa within cold, flu and sinus products, which suggests a plausible link to nasal conditions. The high score is probably driven by this proximity to existing nasal and cold-related uses rather than by independent evidence.

The retrieved literature does not address a nasal cavity disease outcome:
- a review of bitter taste receptors in human airways
- a preclinical study of a nasal caffeine gel for cognition after sleep deprivation, which concerns the delivery route rather than a nasal disease
- a rat study of black tea and caffeine in lung carcinogenesis

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are found in airway tissues, including the nasal cavity; their pharmacology and role in human airways are reviewed. |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | A nasal thermo-sensitive in situ caffeine gel was developed to enhance cognition after sleep deprivation; it is a delivery study, not a nasal disease study. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced NNK-induced lung tumours in rats; unrelated to nasal disease. |

## South Africa Market Information

The list may be partial. No approved indication text is recorded in the local data. The Essential Medicines List status is not available in the data compiled for this report. Up to five main registrations:

<!-- review:begin za-lic-20261105-caffeine-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Twenty valid registrations are recorded, all for single-ingredient products. The list may be partial." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 205 registrations for this drug, 138 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-caffeine-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 29/5.8/0782 | Sinuend | tablet | Valid |
| 34/2.8/0489 | Codoxol | tablet | Valid |
| B675 (ACT 101/1965) | Syndol | tablet | Valid (status not confirmed by SAHPRA) |
| 27/2.8/0137 | Astrapain forte | tablet | Valid |
| 27/2.8/0231 | Vacudol Forte | tablet | Valid |

Showing 5 of 205 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 75 interactions are recorded. Major-level examples are nasal and topical cocaine. Moderate-level examples include alosetron, obeticholic acid, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole and duloxetine.
- **Conditions of concern**: Caffeine is recorded as potentially problematic in hypertension, orthostatic hypotension, long QT syndrome, epilepsy, insomnia, anxiety disorders, liver and kidney disease, peptic ulcer disease, pancreatitis, porphyria, thrombocytopenia, hypothyroidism, COPD and inflammatory bowel disease. These come from relationship data, not from label text, so confirm them against the SAHPRA-approved Professional Information (PI).

Please refer to the SAHPRA-approved PI for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication directly studies caffeine in a nasal cavity disease, so the evidence level is L5. The high score is not supported by clinical data.

**To proceed, the following is needed:**
- Studies that directly assess caffeine in a defined nasal cavity condition
- Mechanism of action data and the approved indication text from the SAHPRA Professional Information
- Review of the SAHPRA package insert warnings and contraindications, and a safety assessment for people with cardiovascular conditions

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Twenty valid registrations are recorded, all for single-ingredient products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

