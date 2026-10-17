---
layout: default
title: Triprolidine
parent: Moderate Evidence (L3-L4)
nav_order: 462
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Triprolidine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis (other original indications: vasomotor rhinitis…"
monitor_inn: "TRIPROLIDINE"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
---

# Triprolidine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Triprolidine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Triprolidine is a first-generation H1-receptor antihistamine, originally used for allergic and vasomotor rhinitis, the common cold, allergic conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are **no registered clinical trials** and only **2 loosely related publications**, so the prediction rests mainly on mechanism and model score.
Much of this is an extension of an existing indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other original indications: vasomotor rhinitis, common cold, atopic conjunctivitis, urticaria, angioedema). No approved indication text is available in the SAHPRA records compiled for this report. |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, triprolidine is a first-generation H1-receptor antagonist. It blocks histamine at H1 receptors and also has anticholinergic and sedating effects.

Allergic urticaria is a histamine-mediated condition, so H1 blockade is mechanistically consistent. Triprolidine is already linked to urticaria (disease) and angioedema in the knowledge graph. The very high TxGNN score (0.9999) therefore probably reflects its close similarity to these existing indications rather than a new therapeutic signal.

Other predictions (cold urticaria, nasal cavity disease, pharyngitis, acute laryngopharyngitis, recalcitrant atopic dermatitis, atopic IgE responsiveness) have even weaker support. Most have no direct evidence, and some are mechanistically doubtful. For example, histamine is not the main driver of atopic dermatitis, and the drying effect could worsen throat irritation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2568212](https://pubmed.ncbi.nlm.nih.gov/2568212/) | 1989 | Review | Clinical Pharmacy | Review of non-sedating H1 antagonists (terfenadine, astemizole, loratadine, acrivastine). Acrivastine is a metabolite of triprolidine. Indirect relevance only. |
| [14283425](https://pubmed.ncbi.nlm.nih.gov/14283425/) | 1965 | Other (small experimental study) | British Journal of Dermatology | Triprolidine and the skin response to ultraviolet radiation. Not a urticaria efficacy study. |

Evidence for related predictions is also indirect:
- **Cold urticaria:** [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) (1988, Dermatologica) was a double-blind crossover RCT in 18 patients. Acrivastine, a triprolidine derivative, reduced weal areas more than cyproheptadine and placebo. Triprolidine itself was not tested.
- **Pharyngitis:** [6377256](https://pubmed.ncbi.nlm.nih.gov/6377256/) (1984, Pediatric Infectious Disease) was an RCT in 142 children with purulent nasopharyngitis. It tested cephalexin with or without a pseudoephedrine/triprolidine combination. The effect of triprolidine alone cannot be separated.

---

## South Africa Market Information

All 13 registrations are valid single-ingredient products. Approved indication text is not available in the data compiled for this report. Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 27/5.8/0260 | Adco-flupain | Syrup | Not available |
| Y/10.1.1/138 | Merck-Cough Linctus | Syrup | Not available |
| 27/10.1/0256 | Adco-tussend | Syrup | Not available |
| 31/5.8/0056 | Coryx paediatric | Syrup | Not available |
| Y/10.1.1/139 | Merck-Expectorant | Syrup | Not available |

Eight further syrup registrations exist. There is also one topical cream, Medaspor topical (28/20.2.2/0119).

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** hypertension, epilepsy, kidney disease, liver disease, pancreatitis, gallbladder disease, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, coronary artery disease and myocardial infarction, atherosclerosis, ocular hypertension, and heart conduction disease. The list also includes other conditions. These should be verified against the SAHPRA Professional Information (PI).

**Drug interactions:** 100 interactions were found, and 20 are listed in the data. Most are Moderate, and the main groups are:
- **Major:** potassium citrate and potassium chloride.
- **Moderate, anticholinergic additive effects:** hyoscyamine, atropine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate and clidinium.
- **Moderate, opioids and CNS or GI agents:** morphine, loperamide, dronabinol, nabilone, eluxadoline and metoclopramide.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is largely an extension of existing labelled uses. There are no clinical trials, and the literature is indirect (class-level or combination-product studies). Package insert warnings and contraindications are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications).
- Obtain mechanism of action data (for example, from DrugBank).
- Look for direct evidence on triprolidine in urticaria, since the available studies cover other antihistamines or combinations.
- Check the knowledge-graph contraindications against the label, and plan safety monitoring for the anticholinergic and sedative effects in vulnerable groups such as children and older adults.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

