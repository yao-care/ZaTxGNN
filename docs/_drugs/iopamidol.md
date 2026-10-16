---
layout: default
title: Iopamidol
parent: Model Prediction Only (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Iopamidol: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the registration data (iopamidol is a diagnostic contra…"
---

# Iopamidol
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

# Iopamidol: From Diagnostic Contrast Imaging to Prinzmetal Angina

## One-Sentence Summary

Iopamidol is an iodinated, non-ionic contrast agent used for diagnostic imaging, not as a treatment.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this prediction rests on the knowledge graph alone, with **0 clinical trials** and **0 publications** supporting it.
The data compiled for this report therefore support **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (iopamidol is a diagnostic contrast agent) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopamidol is a non-ionic iodinated contrast medium that attenuates X-rays, and it has no known vasodilatory or anti-vasospastic pharmacology.

The high TxGNN score (98.57%) appears to be a graph-based inference. Contrast media are used diagnostically in coronary angiography, and that association may have driven the prediction, but it is a diagnostic use, not a therapeutic effect. No plausible mechanistic rationale for treating coronary vasospasm was identified.

**Other predictions reviewed (none supported by therapeutic evidence):**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Female breast carcinoma | 97.91% | L4 | Literature covers diagnostic use only (CT lymphography for sentinel node mapping, acidoCEST MRI pH imaging). No anticancer activity shown. |
| Migraine with brainstem aura | 97.41% | L5 | No mechanistic link or evidence. |
| Migraine disorder | 97.38% | L5 | No mechanistic link or evidence. Likely correlated with the prediction above. |
| Tendinitis | 96.70% | L5 | One imaging paper (graft visualisation). No therapeutic effect shown. |
| Myositis fibrosa | 96.60% | L5 | No mechanistic link or evidence. |
| Idiopathic granulomatous myositis | 96.60% | L5 | No mechanistic link or evidence. Identical score to myositis fibrosa suggests a shared graph neighbourhood. |
| Hemoglobinopathy | 96.43% | L4 | One 1982 in vitro study showing less red cell sickling with iopamidol than with an ionic agent. This is a safety finding, not a treatment benefit. |
| Pulmonary hypertension | 96.16% | L4 | Literature covers pulmonary angiography safety and haemodynamic effects. Diagnostic use, not treatment. |
| Fibromyalgia | 96.06% | L5 | No mechanistic link or evidence. |

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina. No clinical trials were found for any of the other top-ranked predicted indications either.

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For context, the literature found for the other predicted indications is diagnostic or safety-related, not therapeutic. Selected examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8539407](https://pubmed.ncbi.nlm.nih.gov/8539407/) | 1996 | Cohort | Radiology | Safety of pulmonary angiography with iopamidol in 1,434 patients, compared with ionic contrast media (pulmonary hypertension) |
| [3659354](https://pubmed.ncbi.nlm.nih.gov/3659354/) | 1987 | Clinical study | Radiology | Iopamidol was well tolerated and gave better image quality in pulmonary angiography (pulmonary hypertension) |
| [3436330](https://pubmed.ncbi.nlm.nih.gov/3436330/) | 1987 | Clinical study | Eur Heart J | Haemodynamic side effects of iopamidol versus an ionic agent in pulmonary hypertension |
| [14699178](https://pubmed.ncbi.nlm.nih.gov/14699178/) | 2004 | Cohort | Radiology | Sentinel lymph node mapping with CT lymphography using iopamidol in breast cancer (diagnostic) |
| [14976475](https://pubmed.ncbi.nlm.nih.gov/14976475/) | 2004 | Cohort | Surgery | Sentinel node biopsy guided by CT lymphography in breast cancer (diagnostic) |
| [26108564](https://pubmed.ncbi.nlm.nih.gov/26108564/) | 2015 | Preclinical | Contrast Media Mol Imaging | Iopamidol compared with iopromide as acidoCEST MRI agents for tumour extracellular pH (imaging) |
| [7089282](https://pubmed.ncbi.nlm.nih.gov/7089282/) | 1982 | In vitro | Radiology | Iopamidol caused less red cell sickling than an ionic agent (safety finding) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/28/200 | Jopamiron 200 10Ml | Injection | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interactions in total. The 20 listed in the data compiled for this report are all rated **Major**. Examples by group:

- **Corticosteroids:** hydrocortisone, dexamethasone, betamethasone, triamcinolone
- **Nephrotoxic or renally relevant agents:** metformin, vancomycin, amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide
- **Sympathomimetic, stimulant or appetite-suppressant agents:** bupropion, ephedrine, phentermine, diethylpropion, fenfluramine, dexfenfluramine
- **Others:** morphine, dronabinol

Metformin is of particular practical importance with iodinated contrast, because of the risk of contrast-associated kidney injury and lactic acidosis. Please check the SAHPRA-approved Professional Information (PI) for the specific management advice.

Warnings and contraindications from the product label were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction (98.57%) comes from the knowledge graph alone, with no clinical trials, no literature and no plausible mechanism for treating vasospasm. Iopamidol's published uses are diagnostic imaging, and the literature for other predicted indications likewise shows diagnostic or safety information, not therapeutic benefit.

**To proceed, the following is needed:**
- A credible pharmacological rationale for an anti-vasospastic or other therapeutic effect (none identified)
- Preclinical or clinical evidence of therapeutic benefit in Prinzmetal angina
- The SAHPRA Professional Information (warnings, contraindications and approved indication) for Jopamiron, which is a blocking gap for safety screening
- Mechanism of action data
- Confirmation that a therapeutic, rather than diagnostic, use is intended, since iopamidol is already a marketed diagnostic agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

