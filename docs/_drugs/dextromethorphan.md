---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 172
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "DEXTROMETHORPHAN"
predicted_indications: ["faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Allergic Rhinitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a cough suppressant, and the knowledge graph lists it for allergic rhinitis, vasomotor rhinitis, pharyngitis, the common cold, nasopharyngitis and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; the SAHPRA registrations carry no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Dextromethorphan is generally known as a centrally acting antitussive that acts as an NMDA receptor antagonist and sigma-1 receptor agonist. This general pharmacology is not drawn from the data compiled for this report.

The predicted indication, nasal cavity disease, is closely related to the existing rhinitis and common cold indications. The high score (99.98%) most likely reflects proximity to these known upper-respiratory indications in the knowledge graph, rather than a new mechanism. Any benefit would be symptomatic (for example, cough relief), not disease-modifying. In combination cold and flu products, other ingredients usually provide nasal symptom relief.

Other predictions in the list are weaker still:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Acute laryngopharyngitis | 99.98% | L5 | Close to the existing pharyngitis and common cold indications; symptomatic relief only |
| Faucial diphtheria | 99.36% | L5 | No plausible direct mechanism; likely a graph artefact. Treatment is antitoxin and antibiotics |
| Trigeminal autonomic cephalalgia | 99.32% | L5 | Hypothetical link via NMDA antagonism and central pain sensitisation |
| Cervical disc degenerative disorder | 99.30% | L5 | Weak link; no disease-modifying rationale |
| Allergic urticaria | 99.25% | L5 | Dextromethorphan is not an antihistamine; likely derived from the allergic rhinitis link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

All 5 registrations are valid single-ingredient products. The data compiled for this report has no approved indication text, manufacturer or Essential Medicines List (EML) information for these products.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 28/5.8/0231 | Flustat | Syrup | Not available |
| H/10.1/140 | Vicks Medinite | Syrup | Not available |
| 28/20.2.2/0119 | Medaspor topical | Cream | Not available |
| 28/5.8/0304 | Kiddyflu | Syrup | Not available |
| Y/5.8/308 | Demazin Flu | Effervescent tablet | Not available |

## Safety Considerations

**Contraindication signals from the knowledge graph** (not label text; to be verified against the SAHPRA Professional Information): the graph links dextromethorphan to contraindications in the following conditions:
- Cardiovascular: hypertension, hypertensive disorder, hypotensive disorder, long QT syndrome (including familial), torsades de pointes
- Neurological and respiratory: epilepsy, chronic obstructive pulmonary disease, bronchitis
- Hepatic, renal and gastrointestinal: liver failure, liver disease, kidney disease, gallbladder disease, pancreatitis, gastric ulcer, peptic ulcer disease, inflammatory bowel disease
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism (including myxedema and congenital hypothyroidism), adrenocortical insufficiency, Addison disease, potassium deficiency
- Other: thrombocytopenia, benign prostatic hyperplasia, pyoureter, dermatitis herpetiformis

**Drug Interactions:** 100 interactions were recorded (DDInter). The main ones listed are:
- **Major:** dexfenfluramine, fenfluramine, lorcaserin, sibutramine (serotonergic agents); dolasetron, granisetron, ondansetron, palonosetron (5-HT3 antagonists)
- **Moderate:** bupropion, cimetidine, morphine (including liposomal), opium, dronabinol, nabilone, eliglustat, glycerol phenylbutyrate, mazindol, metoclopramide, phentermine

The SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). It most likely reflects overlap with indications that already exist (rhinitis and common cold), and no trials or publications support a distinct new use. Safety screening cannot proceed without the package insert data.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications and approved indications) for the 5 registered products
- Mechanism of action data (DrugBank)
- Targeted literature and trial searches for nasal cavity disease, and for trigeminal autonomic cephalalgia if that direction is pursued
- Clarification of what "nasal cavity disease" would add beyond the existing rhinitis indications
- Route compatibility assessment (not yet done)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

