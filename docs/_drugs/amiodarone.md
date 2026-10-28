---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
last_modified_at: 2026-10-27
description: "Amiodarone: predicted new indication catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Amiodarone: multichannel antiarrhythmic (class III) → catecholaminergic polymorphic ventricular tachycardia
{: .text-alpha }

## One-Sentence Summary

Amiodarone is an oral antiarrhythmic that blocks several cardiac ion channels and is already marketed in South Africa. The TxGNN model predicts it may be useful for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, with a score of 0.9978. **No clinical trials** and **no publications testing amiodarone in CPVT** were found. The available literature describes the disease itself, so this remains an early model-based hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Amiodarone is generally described as a multichannel blocker. It acts on potassium, sodium and calcium channels and has beta-adrenergic blocking activity, which allows it to suppress ventricular arrhythmias.

CPVT is an inherited rhythm disorder. Calcium leaks from the sarcoplasmic reticulum (RYR2 or CASQ2 mutations) during adrenergic stress and triggers ventricular tachycardia. Amiodarone's beta-blocking and partial calcium-channel effects could plausibly act on this pathway, but only indirectly.

Beta-blockers and flecainide are the established CPVT therapies. None of the literature supplied shows that amiodarone works specifically in CPVT. The prediction is therefore mechanistically plausible but unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below concern CPVT itself. None evaluates amiodarone as a treatment for it.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients from China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Clinical characteristics, genetic basis, healthcare use and costs of CPVT in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Overview of antiarrhythmic drug therapy for ventricular arrhythmias |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CPVT |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Ars | CPVT as a rare cause of sudden cardiac arrest in a 2-year-old |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed CPVT diagnosis (RYR2 variant) in a child |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT resolved by right cardiac sympathetic denervation after left-sided denervation |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child surviving cardiac arrest with recurrent VT/VF, and the diagnostic dilemma |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 32/6.2/0650 | Hexarone | Tablet | Not recorded in the local data |
| 56/6.2/0549 | Myorythm 100 | Tablet | Not recorded in the local data |

Both registrations are for single-ingredient oral products and are currently valid.

---

## Safety Considerations

**Drug Interactions:** 100 interactions were identified. Examples rated Major include:
- Agalsidase beta
- Amphotericin B (including its lipid and liposomal formulations)
- Cisapride
- Clarithromycin
- Clotrimazole
- Dexamethasone and hydrocortisone
- Dolasetron
- Eliglustat

Several others are rated Moderate, including famotidine, cimetidine, aprepitant and budesonide.

The supplied literature also describes known amiodarone toxicities: thyroid dysfunction, pulmonary toxicity and QT prolongation. Interaction-related rhabdomyolysis has also been reported.

Warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high, but no trial or publication tests amiodarone in CPVT. Established therapies (beta-blockers, flecainide) already exist, and amiodarone's own toxicity burden is considerable.

**To proceed, the following is needed:**
- Mechanism-of-action data for amiodarone
- The SAHPRA Professional Information (PI) warnings and contraindications
- Clinical or well-designed observational data on amiodarone in CPVT, ideally compared with beta-blockers and flecainide
- A risk assessment covering thyroid, hepatic and pulmonary toxicity, QT prolongation, and the main drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

