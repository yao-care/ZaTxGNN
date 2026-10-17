---
layout: default
title: Cyclizine
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cyclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Cyclizine"
predicted_indications: ["acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "IgE responsiveness, atopic"]
---

# Cyclizine
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

# Cyclizine: From Allergic Rhinitis and Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Cyclizine is a first-generation H1 antihistamine with anticholinergic activity, originally used for allergic and vasomotor rhinitis, conjunctivitis, the common cold, pharyngitis and motion sickness.
The TxGNN model predicts it may be effective for **allergic urticaria**, but **no clinical trials and no publications** specific to this indication were found in the data compiled for this report, so the support is model prediction and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, allergic conjunctivitis, motion sickness (from the knowledge graph; the SAHPRA registration carries no indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cyclizine is a first-generation H1 antihistamine with anticholinergic activity. Its efficacy in allergic rhinitis and allergic conjunctivitis rests on blocking histamine at the H1 receptor.

Urticaria is also a histamine-mediated condition, and H1 antihistamines are the standard first-line treatment, so a class-level mechanistic link is plausible. Current guidance generally favours second-generation antihistamines because first-generation agents cause more sedation and anticholinergic effects. There is no cyclizine-specific evidence for urticaria in the data compiled for this report.

Other model predictions fall into three groups:
- **Overlap with existing uses:** rhinitis, nasal cavity disease and acute laryngopharyngitis largely restate existing indications rather than representing new uses.
- **Cold urticaria:** plausible by class, but with the same limitations as allergic urticaria.
- **Weak or non-actionable links:**
  - Rosacea conjunctivitis, trigeminal autonomic cephalalgia and the atopic IgE trait have weak or no clear mechanistic links.
  - Recalcitrant atopic dermatitis: antihistamines may help with sedation for itch-related sleep disturbance but do not treat the underlying disease.
  - Headache disorder has only indirect literature evidence (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

## Literature Evidence

No literature was found for allergic urticaria. The only literature retrieved for any of the top-ranked predictions relates to the lower-ranked prediction **headache disorder**, and it is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/) | 1985 | RCT | Cephalalgia | Naproxen sodium compared with an ergotamine–caffeine–cyclizine combination in 114 patients with acute migraine. Cyclizine was only one component of the comparator, so this does not show cyclizine efficacy. |
| [20420788](https://pubmed.ncbi.nlm.nih.gov/20420788/) | 2010 | Cohort | Int J Clin Pharmacol Ther | Pharmacy database analysis of migraine prescribing patterns and costs, focusing on triptans. Not specific to cyclizine. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B769 (ACT 101) | Cyclimorph 1ml | Injection | Not stated in the registration data |

Only one registration was found, an injectable single-ingredient product with valid status. The name suggests it may be a cyclizine–morphine combination, but the data compiled for this report list it as a single-ingredient product, so this should be verified against the SAHPRA record. Essential Medicines List status could not be determined from the data compiled for this report.

## Safety Considerations

**Contraindications and conditions of concern (from knowledge-graph drug–disease contraindication links, not label text):**
Conditions flagged include:
- Cardiovascular: hypertension, hypotension, coronary artery disease, myocardial infarction, atherosclerosis
- Neurological: epilepsy
- Renal, hepatic and biliary disease: kidney disease, liver disease, gallbladder disease, pancreatitis
- Endocrine: hypothyroidism and myxedema, adrenocortical insufficiency (Addison disease), diabetes mellitus and diabetic ketoacidosis
- Gastrointestinal: peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, necrotizing enterocolitis
- Urological and ocular: benign prostatic hyperplasia, ocular hypertension
- Other: hemoglobinopathy

These links should be confirmed against the approved Professional Information (PI).

**Drug Interactions:** 100 interactions were identified; the first 20 are shown here.
- **Major:** potassium chloride and potassium citrate.
- **Moderate:** other anticholinergic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate); opioids and related agents (morphine, opium, loperamide, eluxadoline); cannabinoids (dronabinol, nabilone); and prokinetic or antiemetic agents (metoclopramide, prucalopride).
- Additive anticholinergic and central nervous system depressant effects are the likely concern for the moderate interactions.

Label warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for allergic urticaria is high (99.98%), but there are no trials or publications for this indication, so the evidence level is L5. Many of the top predictions also overlap with existing indications, and current guidance favours second-generation antihistamines for urticaria.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data for cyclizine
- Confirmation of the composition and indication of the registered product (Cyclimorph) and whether other cyclizine products are available in South Africa
- A literature search for cyclizine in urticaria, including comparison with second-generation antihistamines
- A benefit–risk assessment of sedation and anticholinergic burden, especially in patients with the conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

