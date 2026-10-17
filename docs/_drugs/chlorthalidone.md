---
layout: default
title: Chlorthalidone
parent: Model Prediction Only (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Chlorthalidone: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
monitor_inn: "chlorthalidone"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, but this is a model prediction only, with **0 clinical trials** and **0 relevant publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (from the knowledge graph; the registration records contain no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorthalidone is a thiazide-like diuretic. Its efficacy in hypertension and congestive heart failure is established, but a mechanistic link to glaucoma cannot be anchored to the drug's known pharmacology.

Thiazide-like diuretics are not an established glaucoma therapy. Any effect on aqueous humour dynamics or intraocular pressure is speculative. The high score (99.92%) reflects network-based model prediction, not clinical findings.

**Other predictions in the list:**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Open-angle glaucoma | 99.90% | L5 | Prediction only |
| 3 | Malignant hypertensive renal disease | 99.89% | L5 | Plausible as an extension of the existing hypertension indication, but no data; this condition usually needs urgent parenteral therapy |
| 4 | Malignant renovascular hypertension | 99.89% | L5 | Plausible, but diuretic monotherapy is not standard in the malignant phase |
| 5 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.88% | L5 | The only retrieved paper is an insect physiology study, irrelevant to humans |
| 6 | Pulmonary hypertension, unclear multifactorial mechanism | 99.88% | L5 | No data |
| 7 | Braddock syndrome | 99.85% | L5 | Rare condition, no data |
| 8 | Chronic pulmonary heart disease | 99.82% | L4 | The only prediction with indirect support (see below) |
| 9 | Acute pulmonary heart disease | 99.32% | L5 | No data |
| 10 | Congenital hypotrichosis milia | 99.19% | L5 | No plausible mechanism |

Chronic pulmonary heart disease (cor pulmonale) is the most biologically coherent candidate. Diuretics reduce fluid retention and right ventricular preload, which is consistent with chlorthalidone's existing congestive heart failure indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication or for any of the other nine predictions.

## Literature Evidence

No literature was found for primary hereditary glaucoma. For context, the publications retrieved for other predictions are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/) | 1967 | Clinical report (historical, likely uncontrolled) | La Clinica Terapeutica | Chlorthalidone diuretic therapy in congestive heart failure caused by chronic cor pulmonale (relevant to rank 8) |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Failure | Transition from hypertension to heart failure; only indirectly relevant (rank 8) |
| [14288313](https://pubmed.ncbi.nlm.nih.gov/14288313/) | 1965 | Basic research (insect physiology) | J Cell Comp Physiol | Ion transport in the Cecropia insect midgut; not relevant to human disease (rank 5) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. Y/7.1.3/24 | Sandoz Co-Tenidone 50/12.5 | Tablet | Not available in the data compiled for this report |
| Reg. No. Z/7.1.3/0096 | Tenchlor hs 50mg/12.5mg | Tablet | Not available in the data compiled for this report |

Both registrations are valid and recorded as single-ingredient products, and both are oral tablets. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are model-graph associations, not label text, and should be verified against the Professional Information): liver failure, kidney disease, anuria, gout, obsolete hyperuricaemia, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency, type 2 diabetes mellitus and diabetes mellitus, systemic lupus erythematosus (including paediatric), asthma (intrinsic and allergic), psoriasis and parapsoriasis, pancreatitis, peptic ulcer disease, pyoureter, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, myocardial infarction, coronary thrombosis, sudden cardiac arrest, and haemoglobinopathy.
- **Drug interactions:** 210 interactions were recorded. The 20 listed in the data compiled for this report include:
  - **Major:** cisapride, dolasetron.
  - **Moderate:** the antidiabetic agents acarbose, alogliptin, albiglutide and metformin; the corticosteroids hydrocortisone, dexamethasone, triamcinolone and beclomethasone; the proton pump inhibitors omeprazole and rabeprazole; amphotericin B (including the lipid complex); bupropion; morphine; and cholecalciferol.
  - **Minor:** doxycycline, hyoscyamine, atropine.

The SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary prediction (primary hereditary glaucoma) is supported only by a model score, with no trials, no relevant literature and no established mechanistic link. Evidence level is L5. Among the other predictions, chronic pulmonary heart disease (L4) is the only one with indirect support, and it is best treated as a research question rather than a candidate for adoption.

**To proceed, the following is needed:**
- Mechanism of action data for chlorthalidone, to assess any plausible link to intraocular pressure
- The SAHPRA package insert (warnings, contraindications, approved indications), as the safety review cannot proceed without it
- Preclinical or clinical evidence for glaucoma, such as intraocular pressure studies
- For chronic pulmonary heart disease, a structured literature review and, if warranted, a controlled study
- Review of the renal, metabolic and glycaemic cautions above before any new-population use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

