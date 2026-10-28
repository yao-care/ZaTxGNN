---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 33
evidence_level: L5
indication_count: 1
monitor_inn: "Ammonium chloride"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-29
description: "Ammonium Chloride: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
---

# Ammonium Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ammonium chloride: From Pharyngitis, Common Cold and Nasopharyngitis to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Ammonium chloride is recorded in the knowledge graph as being used for pharyngitis, common cold and nasopharyngitis. The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (relations recorded in the knowledge graph; the SAHPRA licence records compiled for this report contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 16 of 16) |
| Number of SAHPRA Registrations | 16 (valid: 16) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is used in oral cough and cold preparations. The nasal cavity disease prediction (score 0.9994) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (such as pharyngitis, common cold, nasopharyngitis), not biological evidence. Mechanistically it may be applicable to nasal cavity disease, but this has not been verified.

A plausible but unproven link is anatomical: the original indications and the predicted indication all involve the upper airway. Ammonium chloride is generally known as an expectorant that may thin mucus secretions. This reflects the proximity of the conditions rather than demonstrated efficacy in nasal cavity disease.

The term "nasal cavity disease" is also broad and non-specific, which limits how far the prediction can be interpreted. The high score is a computational result only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

All 16 registrations are single-ingredient records and are valid. The records compiled for this report contain no approved indication text and no manufacturer information, and Essential Medicines List (EML) status is not available. The 5 registrations below are a selection of the 16.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G830 (ACT101/1965) | Benylin & codeine | Syrup | Not stated in the records |
| 31/2.6/0241 | Coprax | Tablet | Not stated in the records |
| 28/10.1/0249 | Expectalin with cod | Syrup | Not stated in the records |
| 27/10.1/0529 | Dynalex | Syrup | Not stated in the records |
| G/10.1/1112 | Broncleer & cod unboxed | Syrup | Not stated in the records |

The other 11 registrations are mostly syrups (for example Tussilinct cough, Phenorant with codeine, Flutex cough linct, Mucosolv expectorant and Coughcod senior/junior).

---

## Safety Considerations

**Contraindications recorded in the knowledge graph (not label text):** the knowledge graph links ammonium chloride to contraindication relations with a range of conditions. These include:
- Renal and metabolic: anuria, impaired renal function, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
- Hepatic: liver failure
- Cardiovascular: hypertension, hypertensive disorder, myocardial ischemia, coronary artery disease, sudden cardiac arrest, heart conduction disease, pulmonary edema
- Endocrine: adrenocortical insufficiency, Addison disease, hyperthyroidism, Graves disease, thyrotoxicosis
- Eye, urinary and gastrointestinal: angle-closure glaucoma, ocular hypertension, benign prostatic hyperplasia, bladder neck obstruction, peptic ulcer disease, necrotizing enterocolitis
- Neurological and psychiatric: epilepsy, insomnia, anxiety disorder, agoraphobia, obsessive-compulsive disorder

These are database relations and should be checked against the SAHPRA-approved Professional Information (PI).

**Drug Interactions:** 21 interactions were found in the interaction database (the data lists 20 of them).
- **Moderate:** amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine
- **Minor:** ephedrine, pseudoephedrine, methadone, mexiletine, flecainide, and the tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin, imipramine, nortriptyline, protriptyline, trimipramine)

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). No clinical trials or publications address nasal cavity disease, the mechanism of action is not documented, and "nasal cavity disease" is too broad to define a clear target population.

**To proceed, the following is needed:**
- Mechanism of action data, for example from DrugBank
- The SAHPRA Professional Information, to obtain approved indications, warnings and contraindications, which blocks safety screening
- A narrower definition of the target condition (for example allergic rhinitis, rhinosinusitis, nasal congestion) and a search for studies on it
- Route and formulation compatibility assessment: the current products are mostly oral syrups, and the route for a nasal indication has not been assessed
- Review of the knowledge-graph contraindication relations, especially renal, hepatic and cardiovascular, against the PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

