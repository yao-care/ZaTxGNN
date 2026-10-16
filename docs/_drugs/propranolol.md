---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Propranolol: predicted new indication Distal myopathy, Tateyama type (evidence level L5). Approved use: Not stated in the SAHPRA registrations compiled for this report. The…"
---

# Propranolol
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

# Propranolol: From Hypertension and Cardiac Disorders to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker, originally used for hypertension, atrial fibrillation, hypertrophic cardiomyopathy and infantile haemangioma.
The TxGNN model's top-ranked prediction is **distal myopathy, Tateyama type**, but there are **no clinical trials and no publications** supporting it.
Better-supported directions among the other predictions are **cardiomyopathy** (literature on hypertrophic cardiomyopathy) and **haemangioma subtypes** (literature on infantile haemangioma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registrations compiled for this report. The knowledge graph lists hypertension, atrial fibrillation, hypertrophic cardiomyopathy, haemangioma and related conditions |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, propranolol is a non-selective beta-adrenergic blocker. It is established in cardiovascular conditions (hypertension, arrhythmias, hypertrophic cardiomyopathy) and in infantile haemangioma. Its relevance to distal myopathy, Tateyama type, has not been demonstrated.

For the top-ranked prediction, no mechanistic link is established. Beta-adrenergic blockade has no known relevance to this rare distal myopathy. The high score (0.994) most likely reflects network proximity in the knowledge graph rather than biological rationale. The second-ranked prediction (congenital myopathy with excess of thin filaments) is likewise unsupported.

Predictions with a more plausible rationale, although still indirect:

- **Cardiomyopathy (rank 6):** Beta-blockade reduces heart rate, myocardial oxygen demand and adrenergic stimulation, and improves diastolic filling in hypertrophic cardiomyopathy. This is already an original indication.
- **Intramuscular, breast epithelioid and breast capillary haemangioma (ranks 7, 9, 10):** Propranolol is standard therapy for infantile haemangioma, but these are different or only related entities, so evidence is extrapolated.
- **Cirrhotic cardiomyopathy (rank 5):** One 2024 report suggests propranolol can correct prolonged QT in cirrhosis, but other studies show blunted cardiovascular effects and possible harm to circulatory and renal function in advanced disease.
- **Hypertrophic cardiomyopathy due to athletic training, chondroma, Maffucci syndrome (ranks 3, 4, 8):** Prediction only, with no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication (or for any of the top 10 predictions).

---

## Literature Evidence

Currently no related literature available for distal myopathy, Tateyama type.

For context, the literature for the better-supported predictions is summarised below (indirect evidence only).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35466712](https://pubmed.ncbi.nlm.nih.gov/35466712/) | 2023 | Systematic review / meta-analysis | Ann Otol Rhinol Laryngol | Propranolol vs atenolol in infantile haemangioma (relevant to haemangioma predictions) |
| [23266923](https://pubmed.ncbi.nlm.nih.gov/23266923/) | 2013 | Consensus report | Pediatrics | Guidance on initiating and monitoring propranolol for infantile haemangioma |
| [34719577](https://pubmed.ncbi.nlm.nih.gov/34719577/) | 2022 | Randomised, double-blind study | Biol Pharm Bull | Propranolol gel (0, 1, 5%) in infantile haemangioma over 24 weeks |
| [32662682](https://pubmed.ncbi.nlm.nih.gov/32662682/) | 2020 | Review | Expert Rev Clin Pharmacol | Propranolol is the mainstay treatment for problematic proliferating infantile haemangioma |
| [25962208](https://pubmed.ncbi.nlm.nih.gov/25962208/) | 2015 | Safety review | Pediatr Endocrinol Rev | Symptomatic hypoglycaemia with propranolol in infantile haemangioma, with prevention guidance |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Clinical haemodynamic study | Eur Heart J | Effects of propranolol and verapamil on diastolic stiffness in hypertrophic cardiomyopathy |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Clinical haemodynamic study | Br Heart J | Nifedipine plus propranolol appeared superior to nifedipine alone in hypertrophic obstructive cardiomyopathy |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Clinical study | Am J Cardiol | Propranolol and arrhythmia in hypertrophic cardiomyopathy |
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Clinical study | Front Pharmacol | Propranolol may correct prolonged QT intervals in cirrhosis |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Clinical study | J Hepatol | Non-selective beta-blockers impair circulatory and renal function in refractory ascites |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| L/5.2/192 | Pur-Bloka 10 | Tablet | Not available in the data compiled for this report |
| Q/5.2/158 | Sandoz Propranolol HCl 10 | Tablet | Not available in the data compiled for this report |

Both registrations are valid single-ingredient oral tablets. Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

**Knowledge-graph contraindication signals** (these come from drug-disease graph edges, not from label text) include:
- Respiratory: bronchitis
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, gout, hyperparathyroidism, hypercalcaemia, potassium deficiency, phosphorus metabolism disease
- Hepatic and renal: liver disease, hepatic coma and encephalopathy, kidney disease, anuria, gallbladder disease, pancreatitis
- Neuromuscular: myasthenia gravis, myopathy, muscular and skeletal muscle disease, familial periodic paralysis. These are directly relevant to the top-ranked myopathy predictions and warrant particular caution.
- Other: systemic lupus erythematosus, anxiety and neurotic disorders, dysthymic disorder, neonatal jaundice

**Drug interactions** (100 interactions recorded; the most notable listed):
- **Major:** Epinephrine
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, cimetidine, canagliflozin, chlorpropamide, lorcaserin, calcium salts
- **Minor:** aspirin, ascorbic acid, magnesium oxide

**Other signals from the literature:** propranolol-induced hypoglycaemia in infants treated for haemangioma (PMID 25962208), and possible circulatory and renal harm from non-selective beta-blockers in advanced cirrhosis with refractory ascites (PMID 32446716).

SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, distal myopathy Tateyama type, rests on a model score alone (Evidence Level L5). There is no trial or literature support and no plausible mechanism, and the knowledge graph flags myopathy-type conditions as contraindications. Predictions with literature support (cardiomyopathy, haemangioma subtypes) are largely extrapolations from existing indications and are better treated as research questions than as new repurposing candidates.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indications (currently a blocking gap for safety screening)
- Mechanism of action data
- For the top-ranked prediction: any preclinical or case evidence linking beta-blockade to the disease, plus a review of the myopathy contraindication signal
- For the more promising directions (cardiomyopathy subtypes, non-infantile haemangiomas): targeted literature review and, if warranted, a focused clinical study with safety monitoring (heart rate, blood pressure, blood glucose)
- Confirmation of EML status and route compatibility for any proposed new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

