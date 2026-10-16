---
layout: default
title: Doxylamine
parent: Model Prediction Only (L5)
nav_order: 204
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Doxylamine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis (other listed indications include vasomotor rhiniti…"
monitor_inn: "DOXYLAMINE"
predicted_indications: ["allergic urticaria", "nasal cavity disease", "acute laryngopharyngitis", "cold urticaria"]
---

# Doxylamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Doxylamine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Doxylamine is a first-generation H1-antihistamine, originally used for allergic rhinitis, the common cold, urticaria and related allergic conditions.
The TxGNN model predicts it may be effective for **allergic urticaria**, but this is largely a subtype of an indication it already has. There are currently **no clinical trials** and **no publications** supporting this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other listed indications include vasomotor rhinitis, pharyngitis, common cold, conjunctivitis, urticaria and angioedema) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

Note: the data compiled for this report assigned a level of L4 (mechanistic reasoning only). Under the stated grading rules, a prediction with no actual trials or publications falls at L5. Either way, no direct clinical evidence exists.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, doxylamine is a first-generation H1-antihistamine with anticholinergic activity. Blocking the H1 receptor directly counters histamine-mediated wheal and flare, which drives urticaria.

Urticaria and angioedema are already among doxylamine's listed indications. Allergic urticaria is a subtype of urticaria, so the high TxGNN score (0.998) mostly reflects an existing use rather than a true repurposing opportunity.

Other predictions from the model follow the same pattern:

- **Nasal cavity disease** (99.36%): a broad category overlapping with allergic rhinitis, vasomotor rhinitis and the common cold. It is too non-specific to form a defined hypothesis.
- **Acute laryngopharyngitis** (99.34%): closely related to the existing pharyngitis and nasopharyngitis indications. Doxylamine may ease symptoms such as postnasal drip and throat irritation but has no known effect on the underlying infection.
- **Cold urticaria** (99.26%): an inducible urticaria driven by mast-cell histamine release, so H1 blockade is rational. However, guidelines favour second-generation non-sedating antihistamines, which makes a sedating first-generation agent less attractive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Doxylamine has 11 valid SAHPRA registrations (all single-ingredient entries, none cancelled). No approved indication text, manufacturer or Essential Medicines List (EML) information was available in the data compiled for this report. The 5 registrations below are a selection.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 33/7.1.3/0452 | Hypace | Tablet | Not available |
| 33/2.8/0098 | Doxy co | Tablet | Not available |
| H/10.1/140 | Vicks Medinite | Syrup | Not available |
| 36/2.8/0271 | Alpha-Dol | Tablet | Not available |
| 33/2.8/0187 | Resdol | Tablet | Not available |

Available dosage forms are oral tablets and syrup.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (taken from drug-disease relationships in the TxGNN knowledge graph, not from label text, so they must be checked against the SAHPRA Professional Information):

- **Cardiovascular:** hypertension, coronary artery disease, myocardial infarction, atherosclerosis, ventricular tachycardia
- **Hepatic and pancreatic:** liver failure, liver disease, pancreatitis, gallbladder disease
- **Gastrointestinal:** peptic ulcer disease
- **Metabolic and endocrine:** diabetes mellitus, diabetic ketoacidosis, hyperthyroidism (Graves disease, thyrotoxicosis)
- **Genitourinary:** benign prostatic hyperplasia, bladder neck obstruction
- **Ocular:** angle-closure glaucoma, ocular hypertension
- **Other:** substance abuse or dependence, hemoglobinopathy, paracetamol poisoning

**Drug interactions** (100 interactions identified; the most notable are below):

- **Major:** potassium citrate and potassium chloride
- **Moderate (additive anticholinergic or CNS effects):** hyoscyamine, atropine, scopolamine, glycopyrronium, dicyclomine, clidinium, propantheline, methscopolamine and mepenzolate
- **Moderate (opioids and CNS depressants):** morphine, opium, loperamide, dronabinol, nabilone and eluxadoline
- **Moderate (other):** metoclopramide

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction largely restates an existing indication (urticaria). The other predictions are either too broad or already covered by current use, and there are no clinical trials or publications for any of them. For cold urticaria, a sedating first-generation antihistamine is also a poor fit compared with second-generation agents.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which block safety screening
- Mechanism of action data (for example, from DrugBank)
- Approved indication text for the registered South African products
- Published or registered clinical evidence for doxylamine in specific urticaria subtypes, such as cold urticaria
- A comparison with second-generation non-sedating antihistamines, with attention to sedation and anticholinergic burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

