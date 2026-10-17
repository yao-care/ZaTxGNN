---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 102
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Carvedilol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carvedilol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a beta-blocker (with additional alpha-1 blocking activity) originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. It is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the SAHPRA registration text on file contains no indication wording, so this comes from the knowledge-graph indication data |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carvedilol is a non-selective beta-blocker with alpha-1 blocking activity. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant renovascular hypertension.

Lowering peripheral vascular resistance (alpha-1 blockade) and reducing renin release (beta-1 blockade) are plausibly relevant to renovascular hypertension, where renin-angiotensin activation drives the blood pressure rise.

The high TxGNN score most likely reflects similarity to the already-approved hypertension indication rather than disease-specific evidence. No trials or publications were found for this severe, accelerated form of hypertension. Oral carvedilol is also not a standard acute therapy for hypertensive emergencies.

**Other predictions in the same list (all model predictions, none corroborated by clinical data):**

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.55% | L5 | Plausible via blood pressure lowering and renin suppression; largely overlaps with the existing hypertension indication; no trials or literature |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.54% | L5 | Beta-blockers are generally used cautiously in pulmonary arterial hypertension because of concerns about right ventricular function; no trials or literature |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.54% | L4 | Preclinical support only (see below) |
| Braddock syndrome | 99.37% | L5 | No mechanistic rationale evident; no trials or literature |

For pulmonary hypertension owing to lung disease and/or hypoxia, the indirect preclinical findings are:
- Carvedilol reversed hypertension induced by chronic intermittent hypoxia in rats (PMID 26291659).
- Carvedilol inhibited right ventricular hypertrophy induced by chronic hypobaric hypoxia (PMID 16639551).
- Adrenergic blockade reversed right heart remodelling in pulmonary hypertensive rats (PMID 20508210).

These findings concern animal models or systemic hypertension. They do not show pulmonary hypertension outcomes in humans.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (malignant renovascular hypertension) or for any of the other predictions listed above.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (malignant renovascular hypertension).

For the related prediction *pulmonary hypertension owing to lung disease and/or hypoxia*, the most relevant publications retrieved were:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Effects of beta-blockers on lung function in heart failure; the traditional view that they are unsuitable with impaired lung function has recently been challenged |
| [28862654](https://pubmed.ncbi.nlm.nih.gov/28862654/) | 2017 | Review | Nutrients | Antioxidant strategies for cardiovascular conditions linked to oxidative stress |
| [24798657](https://pubmed.ncbi.nlm.nih.gov/24798657/) | 2014 | Crossover study (11 patients) | J Clin Hypertens | Nighttime nifedipine vs carvedilol 20 mg on sleep blood pressure in hypertensive patients with sleep apnoea |
| [26291659](https://pubmed.ncbi.nlm.nih.gov/26291659/) | 2015 | Preclinical (animal) | Eur J Pharmacol | Carvedilol reversed hypertension induced by chronic intermittent hypoxia in rats |
| [16639551](https://pubmed.ncbi.nlm.nih.gov/16639551/) | 2006 | Preclinical (animal) | Pflugers Arch | Carvedilol inhibited right ventricular hypertrophy induced by chronic hypobaric hypoxia |
| [20508210](https://pubmed.ncbi.nlm.nih.gov/20508210/) | 2010 | Preclinical (animal) | Am J Respir Crit Care Med | Adrenergic receptor blockade reversed right heart remodelling and dysfunction in pulmonary hypertensive rats |
| [25187802](https://pubmed.ncbi.nlm.nih.gov/25187802/) | 2014 | Preclinical (in vitro) | Exp Ther Med | Carvedilol reduced cardiomyocyte apoptosis after simulated ischaemia/reperfusion via the TLR4/NF-κB pathway |
| [31200253](https://pubmed.ncbi.nlm.nih.gov/31200253/) | 2019 | Preclinical | Biomed Pharmacother | Cardioprotective effects of carvedilol on ischaemia/reperfusion injury via AMPK signalling |
| [10862260](https://pubmed.ncbi.nlm.nih.gov/10862260/) | 2000 | Review (toxicology) | Presse Med | Beta-blocker intoxication; carvedilol is among the more toxic agents in overdose |

Several other retrieved papers (indole neuroprotectants, cholangiocarcinoma, triple-negative breast cancer, uveal melanoma, miR-150 cardiac remodelling) are off-topic and are not listed.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/7.1.3/0281 | Carvedilol unicorn | Tablet (oral) | Not specified in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph (not label text):** these come from drug-disease contraindication links and must be confirmed against the SAHPRA Professional Information (PI).
- Respiratory: asthma (including intrinsic and allergic asthma), bronchitis, bronchial disease, pulmonary emphysema
- Cardiac conduction: atrioventricular block, sick sinus syndrome (including the familial form)
- Circulatory: hypotensive disorder, peripheral vascular disease, peripheral arterial disease, intermittent vascular claudication, Prinzmetal angina
- Metabolic: diabetes mellitus, diabetic ketoacidosis
- Other: liver failure, anaphylaxis, intraoperative floppy iris syndrome

The respiratory contraindications are particularly relevant to any use in pulmonary hypertension owing to lung disease.

**Drug interactions (100 recorded; examples from the interaction database):**
- **Major:** Epinephrine
- **Moderate:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, morphine, bupropion, atropine, hyoscyamine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate)
- **Minor:** acetylsalicylic acid, aluminium hydroxide, attapulgite

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or publications for malignant renovascular hypertension. The high score likely reflects similarity to the existing hypertension indication. The related pulmonary hypertension prediction has only indirect animal evidence (L4), and carvedilol's respiratory contraindications add caution.

**To proceed, the following is needed:**
- Disease-specific clinical or observational data in renovascular hypertension
- Mechanism of action data (MOA)
- SAHPRA package insert warnings and contraindications (this blocks safety screening)
- Approved indication text for the SAHPRA registration
- Clarification of whether oral carvedilol has any role in hypertensive emergency-type conditions
- For pulmonary hypertension: human data on right ventricular safety and respiratory tolerability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

