---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the SAHPRA licence data compiled for this report. Pub…"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: From Obstructive Airway Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an ultra-long-acting inhaled beta-2 agonist (a bronchodilator) used in obstructive airway disease such as COPD and asthma. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data compiled for this report. Published literature describes use in COPD and asthma. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, indacaterol is an ultra-long-acting beta-2 agonist. It activates beta-2 receptors on airway smooth muscle, raises intracellular cAMP and causes bronchodilation.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2). This receptor signals through Gs and cAMP, so the signalling pathway overlaps with that of beta-2 agonists. This overlap is probably what drives the high network-based score.

**The mechanistic rationale is weak.** The direction of effect is unclear. Raising cAMP in a disorder of excessive V2 signalling could plausibly be neutral or unhelpful, and no plausible therapeutic mechanism has been established. This prediction should be treated as a hypothesis, not a treatment lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for nephrogenic syndrome of inappropriate antidiuresis.

---

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 54/10.2.1/0870.867 | Bemrist Breezhaler 150/80 | Capsule (oral inhalation) | Not listed in the data compiled |
| 54/10.2.1/0875.873 | Zimbus Breezhaler 150/50/80 | Capsule (oral inhalation) | Not listed in the data compiled |

Both registrations are valid and there are no cancelled registrations. The strengths in the product names (150/80 and 150/50/80) match the published indacaterol/mometasone and indacaterol/glycopyrronium/mometasone fixed-dose combinations. The registrations are nonetheless classified as single-entry products in the source data. No Essential Medicines List (EML) status is recorded.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease edges in the TxGNN knowledge graph, not SAHPRA label text):
  - Cardiovascular: hypertension, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, coronary artery disease
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, potassium deficiency, thyrotoxicosis, hyperthyroidism, Graves disease
  - Neurological: epilepsy
- **Drug interactions:** 100 interactions were recorded, and the 20 reviewed include:
  - *Moderate:* antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, saxagliptin, chlorpropamide), epinephrine, isometheptene, famotidine and clarithromycin
  - *Minor:* corticosteroids (hydrocortisone, dexamethasone, budesonide, beclomethasone, betamethasone, triamcinolone) and aprepitant

The SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information, and report adverse drug reactions to SAHPRA.

---

## Other Predictions in the Data

- **Bronchial disease** (score 99.18%) is the only other prediction with clinical evidence, and it is effectively an on-label use rather than true repurposing. It has 24 registered trials and 20 publications. The key ones are:
  - Phase 3 trial NCT02554786 (n=2,216), the 52-week QMF149 trial in asthma
  - Phase 3 trial NCT00529529 (n=805), a 26-week safety study against salmeterol
  - Phase 3 trial NCT01079130 (n=511), the 14-day efficacy trial against placebo and salmeterol
  - The IRIDIUM randomised Phase 3 study (PMID 32653074) of mometasone-indacaterol-glycopyrronium in asthma
  - Phase 3 trial NCT04206761, which was withdrawn with 0 enrolment and does not count as evidence
  - Most of the Phase 3 evidence is for fixed-dose combinations, not indacaterol alone. LABA use in asthma requires inhaled corticosteroid co-therapy.
- The remaining predictions have no clinical trials or literature: headache disorder, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, anaphylaxis and Ambras-type hypertrichosis.
  - Several are likely artefacts of neighbouring diseases in the knowledge graph.
  - Indacaterol must not be used in place of epinephrine in anaphylaxis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for NSIAD rests only on a network score and a shared cAMP pathway. There are no trials or publications, and the direction of effect is uncertain.
- The knowledge-graph contraindication signals (cardiovascular, metabolic) also argue against progressing without further evidence.

**To proceed, the following is needed:**
- The original indication and mechanism of action data, reconciled against the source database and SAHPRA licence text
- Preclinical or mechanistic studies of beta-2 agonism in AVPR2 gain-of-function models, to establish the direction of effect
- Retrieval of the SAHPRA package insert warnings and contraindications
- A safety review of cardiovascular, glycaemic and potassium effects in the target patient group
- Expert clinical input from nephrology and endocrinology on whether any therapeutic rationale exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

