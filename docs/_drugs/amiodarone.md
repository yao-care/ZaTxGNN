---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 9
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-11-03
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amiodarone: Catecholaminergic polymorphic ventricular tachycardia
{: .text-alpha }

## One-Sentence Summary

Amiodarone is a multichannel-blocking antiarrhythmic drug (potassium, sodium and calcium channels, plus beta-adrenergic antagonism) that is used to suppress ventricular arrhythmias.
The TxGNN model predicts it may be useful for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, but this is a **model prediction only (L5)**: **no clinical trials** are registered and none of the publications supplied tested amiodarone in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, amiodarone blocks potassium channels (prolonging repolarisation), and also blocks sodium and calcium channels and has beta-adrenergic antagonist activity. These actions suppress ventricular arrhythmias.

CPVT is an inherited arrhythmia caused by catecholamine-triggered diastolic calcium leak (RYR2 or CASQ2 variants). The beta-blocking and partial calcium-channel effects of amiodarone make a benefit plausible, but the link is indirect. Beta-blockers and flecainide are the established therapies, and the publications supplied do not show amiodarone-specific efficacy in CPVT.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below describe CPVT itself or treatments other than amiodarone. None tests amiodarone in CPVT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients from China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Clinical characteristics, genetics, healthcare use and costs of CPVT in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | General review of drug treatment for ventricular arrhythmias |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CPVT |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT resolved with right cardiac sympathetic denervation after left denervation |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Delayed CPVT diagnosis in a child with an RYR2 variant |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | CPVT as a rare cause of sudden cardiac arrest in a 2-year-old |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 32/6.2/0650 | Hexarone | Tablet | Not recorded in the local data |
| 56/6.2/0549 | Myorythm 100 | Tablet | Not recorded in the local data |

Both registrations are valid single-ingredient oral products. Essential Medicines List status is not stated in the data compiled for this report.

## Safety Considerations

Safety information is limited. Label warnings and contraindications from the SAHPRA Professional Information (PI) are not available in the data compiled for this report; please refer to the PI and report adverse drug reactions to SAHPRA.

- **Conditions listed as contraindicated in drug–disease relations (not label text)**: long QT syndrome (including familial), torsades de pointes, atrioventricular block, sick sinus syndrome, hypothyroidism and hyperthyroidism (including myxedema, Graves disease, thyrotoxicosis), liver disease and drug-induced liver injury, interstitial lung disease, eosinophilic pneumonia, hypersensitivity pneumonitis, optic neuritis and optic nerve disease, peripheral neuropathy, potassium deficiency, gallbladder disease, corneal deposits.
- **Drug interactions**: 100 interactions were found. Major interactions include cisapride, clarithromycin, clotrimazole, dolasetron, eliglustat, agalsidase beta, amphotericin B (all formulations), and the corticosteroids hydrocortisone and dexamethasone. Moderate interactions include famotidine, cimetidine, aprepitant, bisacodyl, budesonide and castor oil. Fidaxomicin is minor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported by the model score alone (L5). No trial or publication tests amiodarone in CPVT, and established therapies (beta-blockers, flecainide) exist. The safety profile, including QT-related and conduction-related risks, needs careful weighing in an inherited arrhythmia population.

**To proceed, the following is needed:**
- Studies (preclinical or clinical) that directly test amiodarone in CPVT or in RYR2/CASQ2 models
- Comparison against beta-blockers and flecainide
- Professional Information warnings and contraindications from SAHPRA
- Mechanism of action data from DrugBank
- A safety plan covering QT, conduction, thyroid, liver, lung and drug-interaction risks

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

