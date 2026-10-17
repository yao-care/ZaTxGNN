---
layout: default
title: Brompheniramine
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Brompheniramine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, common cold…"
---

# Brompheniramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Brompheniramine: From Allergic Rhinitis and Related Allergic Conditions to Allergic Urticaria

## One-Sentence Summary

Brompheniramine is a first-generation antihistamine, originally used for allergic rhinitis, the common cold, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria** (and, as a second prediction, **cold urticaria**),
but **no clinical trials or publications** were found in the data compiled for this report, so the prediction currently rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, common cold, allergic conjunctivitis (atopic, papillary, vernal), familial dermatographia, urticaria, angioedema (from the knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Brompheniramine is a first-generation H1-receptor antagonist. Detailed mechanism-of-action data were not available in the data compiled for this report, but this is its established pharmacology. In allergic urticaria, histamine released from mast cells causes the wheal-and-flare reaction, so blocking H1 receptors is mechanistically plausible.

The knowledge graph already lists urticaria and angioedema among brompheniramine's original indications. The high score for allergic urticaria therefore probably reflects this existing link. This is largely an on-label or near-label use, not a true repurposing opportunity.

The second prediction, **cold urticaria** (score 99.55%), is a physical urticaria triggered by cold exposure. H1 antihistamines are first-line therapy for it, so the mechanism fits. However, guidelines generally prefer second-generation non-sedating antihistamines (such as cetirizine, desloratadine or rupatadine), often up-titrated, over first-generation agents. The reasons are sedation and anticholinergic burden. There is no direct evidence for brompheniramine in this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C769 (ACT 101/1965) | Ilvico | Syrup | Not available in the data compiled |
| C770 (ACT 101/1965) | Ilvico | Tablet | Not available in the data compiled |

Both registrations are valid single-ingredient products. No Essential Medicines List (EML) status was available in the data compiled for this report.

---

## Safety Considerations

**Contraindications / conditions of concern (from knowledge-graph drug–disease links, not label text):**
Hypertension, coronary artery disease and myocardial infarction, liver disease and liver failure, kidney disease, epilepsy, COPD, peptic ulcer disease and gastric ulcer, inflammatory bowel disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hypothyroidism, ocular hypertension, pancreatitis, gallbladder disease, substance abuse/dependence, hypotension, and others. These need confirmation against the SAHPRA-approved Professional Information (PI).

**Drug Interactions (100 interactions recorded; examples):**
- **Major:** Potassium chloride, potassium citrate
- **Moderate:**
  - Anticholinergics: atropine, hyoscyamine, scopolamine, dicyclomine, glycopyrronium, propantheline
  - Opioids: morphine, opium
  - Loperamide, metoclopramide
  - Cannabinoids: dronabinol, nabilone
  - Eluxadoline

Additive anticholinergic and sedative effects are the main concern with these combinations.

The SAHPRA package insert warnings were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (Evidence Level L5), with no trials or publications. Allergic urticaria is largely an existing indication, and for cold urticaria, non-sedating second-generation antihistamines are preferred. The package insert safety data are also missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (indications, warnings, contraindications) for both Ilvico registrations
- Mechanism-of-action data from DrugBank
- Clinical evidence for brompheniramine in allergic and cold urticaria, including comparison with second-generation antihistamines
- A review of the knowledge-graph contraindications against the PI, and a plan for the anticholinergic and sedation burden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

