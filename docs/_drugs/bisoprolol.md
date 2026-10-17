---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 74
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Bisoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a selective beta-1 blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

*Note: The SAHPRA records compiled for this report contain no approved-indication text, so the original indication is taken from the knowledge-graph indication data.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, bisoprolol is a beta-1 selective blocker, its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-related conditions.

Malignant hypertensive renal disease is a severe end-organ complication of hypertension, so the high score most likely reflects its close relationship to the approved indication rather than a new mechanism. Beta-1 blockade reduces heart rate, cardiac output and renin release, which may help lower blood pressure in general.

Important caveats: beta-blockers are not first-line treatment for hypertensive emergencies, and no data compiled for this report show a renal benefit. This prediction is essentially an extension of the existing antihypertensive indication.

Other predictions with similar scores were also generated (all Hold):
- **Malignant renovascular hypertension** (99.94%, L5): beta-1 blockade reduces renin release, which is plausible, but this emergency is generally managed with other agents and revascularisation.
- **Pulmonary hypertension, unclear multifactorial mechanism** (99.93%, L5): beta-blockade is not an established treatment, and there are concerns about right ventricular function and cardiac output. The prediction likely reflects the shared word "hypertension".
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.93%, L4): only indirect evidence (see below).
- **Braddock syndrome** (99.91%, L5): no clear mechanistic rationale, and the condition is rare and poorly characterised.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (or for any of the other four predictions).

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), eight publications were retrieved. None is a clinical study of bisoprolol in pulmonary hypertension, so they offer indirect context only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Clinical comparison | Int J Cardiol | CARNEBI trial: carvedilol vs nebivolol vs bisoprolol in moderate heart failure |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Effects of beta-blockers on lung function in heart failure; the traditional view that they are unsuitable with impaired lung function has been challenged |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Physiological study | Med Sci Sports Exerc | Beta-adrenergic blockade and chemoreflex contributions to exercise capacity |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Physiological study | J Am Soc Echocardiogr | Left ventricular adaptation to acute hypoxia, with and without beta-1 inhibition |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | Preclinical | Fundam Clin Pharmacol | Bisoprolol protects myocardial cells from ischaemia-reperfusion injury via PI3K/AKT/GSK3β |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | Preclinical (in vitro) | Nan Fang Yi Ke Da Xue Xue Bao | Bisoprolol pretreatment and hypoxia/reoxygenation injury in H9c2 cardiomyocytes |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Preclinical (animal) | Int Immunopharmacol | Diosmin plus bisoprolol attenuate cobalt chloride-induced cardiotoxicity |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Case report | Hypertens Res | Two cases of pheochromocytoma with tetralogy of Fallot |

None addresses pulmonary vascular pressure or outcomes in pulmonary hypertension.

---

## South Africa Market Information

Nine valid SAHPRA registrations exist, all listed as single-ingredient records (no cancelled registrations). Most listed products appear to be bisoprolol combination tablets (e.g. with hydrochlorothiazide or amlodipine, judging by the product names). Approved-indication text and Essential Medicines List status are not available in the data compiled for this report. The first five registrations are shown:

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 43/7.1.3/0059 | Bisozyd co 2.5mg/6.25mg | Tablet | Not available |
| 47/7.1.3/0710 | Emcor 5/5 Fdc | Tablet | Not available |
| 44/7.1.3/0561 | Zirinak Co 5/6,25 | Tablet | Not available |
| 51/7.1.3/0495 | Cosyrel 5/5 | Film-coated tablet (Fct) | Not available |
| 37/7.1.3/0564 | Ziabeta 2.5/6.25mg | Tablet | Not available |

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindications or cautions suggested by the knowledge graph (not label text):** the knowledge graph links bisoprolol to a range of conditions, including asthma, diabetes mellitus and diabetic ketoacidosis, kidney disease, liver disease and hepatic encephalopathy, anuria, pancreatitis, gallbladder disease, systemic lupus erythematosus, psoriasis, gout, myasthenia gravis, anxiety and dysthymic disorders, and several metabolic disorders (potassium deficiency, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease). These are graph associations and must be verified against the approved PI. Some may reflect partner drugs in combination products.

**Drug Interactions:** 100 interactions were identified (DDInter). Examples of **moderate** interactions include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, acetohexamide, and calcium salts (acetate, carbonate, citrate, gluconate). **Minor** interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no clinical trials or literature for malignant hypertensive renal disease. It largely overlaps with bisoprolol's existing antihypertensive indication, and beta-blockers are not first-line therapy for hypertensive emergencies. The pulmonary hypertension predictions show only indirect evidence and raise safety concerns. In addition, the SAHPRA safety information is missing, which blocks safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications) to complete safety screening
- Detailed mechanism of action data (e.g. from DrugBank)
- A targeted literature search for bisoprolol or beta-blockers in malignant hypertension and hypertensive nephropathy
- Clarification of whether the intended use differs meaningfully from the existing hypertension indication
- Review of the high-volume DDI list for clinically relevant interactions in the target population
- For pulmonary hypertension, specific assessment of right ventricular and haemodynamic safety before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

