---
layout: default
title: Sertraline
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 7
monitor_inn: "SERTRALINE"
predicted_indications: ["paranoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
last_modified_at: 2026-11-12
description: "Sertraline: predicted new indication Paranoid personality disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Sertraline
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

## Sertraline: Paranoid personality disorder
{: .text-alpha }

## One-Sentence Summary

Sertraline is a selective serotonin reuptake inhibitor (SSRI) antidepressant marketed in South Africa.
The TxGNN model predicts it may be effective for **paranoid personality disorder**, but **no clinical trials** and **no publications that directly study this disease** were found; the available literature concerns other personality disorders and depression.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Paranoid personality disorder |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 33 of 37; 4 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 37 (valid: 33, of which 4 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Sertraline is an SSRI, a class that increases serotonergic signalling. Serotonergic modulation may influence impulsivity, affective instability, irritability and comorbid depression or anxiety.

The link to paranoid personality disorder is indirect. The retrieved literature concerns borderline personality disorder and personality-disorder comorbidity in major depression, not paranoid personality disorder. Serotonergic effects on comorbid mood or anxiety symptoms do not establish efficacy for paranoid traits. The very high score (0.9993) is shared by several other personality disorders. This pattern suggests a class-level computational signal rather than disease-specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

<!-- review:begin za-lic-20261105-sertraline-1 -->

> **Review correction (2026-11-05)**: Originally stated: "All four registrations are single-ingredient products and all are valid." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 37 registrations for this drug, 33 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-sertraline-1 -->

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9817625](https://pubmed.ncbi.nlm.nih.gov/9817625/) | 1998 | RCT (secondary analysis) | Int Clin Psychopharmacol | 308 primary-care patients with major depression, treated with sertraline or citalopram for 24 weeks; examined personality-disorder comorbidity and the effect of treatment on personality-disorder diagnoses. Not specific to paranoid personality disorder. |
| [18848360](https://pubmed.ncbi.nlm.nih.gov/18848360/) | 2008 | Clinical trial | Psychiatry Res | Aripiprazole augmentation in 21 sertraline-resistant patients with borderline personality disorder; concerns a different personality disorder. |
| [36853245](https://pubmed.ncbi.nlm.nih.gov/36853245/) | 2023 | Review | JAMA | General review of borderline personality disorder; not specific to sertraline or paranoid personality disorder. |
| [11686052](https://pubmed.ncbi.nlm.nih.gov/11686052/) | 2001 | Review | L'Encephale | Psychiatric complications of alpha-interferon; low relevance. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 32/1.2/0381 | Zoloft | tablet | Valid |
| 36/1.2/0272 | Serlife | tablet | Valid |
| 36/1.2/0273 | Serlife | tablet | Valid |
| 36/1.2/0274 | Tralidep | tablet | Valid |
| 36/1.2/0275 | Tralidep | tablet | Valid |

Showing 5 of 37 registrations (valid registrations first).

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 interacting drugs in total. Major-level interactions include bupropion, lorcaserin, diethylpropion, dolasetron, eliglustat, palonosetron and phentermine. Moderate-level interactions include famotidine, loperamide, morphine, acetylsalicylic acid, clarithromycin, and the sulfonylureas chlorpropamide and glimepiride, as well as insulin aspart.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial and no publication directly studies sertraline in paranoid personality disorder. The prediction rests on a computational score that is identical across several personality disorders, so the evidence level is L5.

**To proceed, the following is needed:**
- Studies that directly assess sertraline in paranoid personality disorder
- Detailed mechanism-of-action data
- Review of the SAHPRA Professional Information for warnings and contraindications
- A safety review of the major drug interactions, especially with other serotonergic agents

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "All four registrations are single-ingredient products and all are valid" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

