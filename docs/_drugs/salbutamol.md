---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Asthma"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
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

# Salbutamol: From Asthma and Bronchial Disease to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol is a beta-2 adrenergic bronchodilator, originally used to treat **asthma and bronchial disease**.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, with a very high model score.
However, **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma; bronchial disease |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.996% (model rank 65) |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Salbutamol is a short-acting beta-2 agonist, and its efficacy in asthma and bronchial disease is well established through relaxation of airway smooth muscle.

For papillary conjunctivitis, the only available rationale is hypothetical. Beta-2 agonism may reduce mast cell mediator release in ocular tissue, which could matter in an allergic or irritative eye condition. No study retrieved for this report tests that idea in this disease. The link between airway disease and a conjunctival condition is indirect, and the high model score should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Salbutamol has 10 valid SAHPRA registrations, all classed as single-ingredient products and none cancelled. The approved indication text was not captured for any of them. The table shows five main registrations.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 30/10.2.2/0200 | Asthavent | Syrup | Not listed |
| 35/10.2/0142 | Vari-salbutamol syrup | Syrup | Not listed |
| A39/10.2.1/0482 | Asthavent Respules | Nebuliser | Not listed |
| 30/10.2.1/0032 | Airomir Autohaler | Inhaler | Not listed |
| 32/10.2.1/0344 | Ventolin inhaler 200 cfc-free | Inhaler | Not listed |

The remaining registrations are Combivent, Combivent UDV, Iprabut, Duolin respules and Trandate. Several of these names are usually associated with salbutamol/ipratropium combinations, yet they are classed as single-ingredient here. Trandate (J/7.1.3/52, tablet) is normally a labetalol brand, which is a beta-blocker with the opposite pharmacology. These entries should be verified against the SAHPRA register before the registration count is relied upon.

The registered forms are oral (syrup, tablet) and inhaled or nebulised. **No ophthalmic formulation** appears among them, which matters for a conjunctival indication.

---

## Safety Considerations

**Disease associations flagged in the knowledge graph (not label text):** the TxGNN knowledge graph links salbutamol to contraindication or caution signals in the following conditions:
- Cardiovascular: hypertension, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, myocardial ischaemia, coronary artery disease
- Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, acidosis (including metabolic), hyperthyroidism, Graves disease, thyrotoxicosis
- Neurological: epilepsy
- Eye and urinary: angle-closure glaucoma, ocular hypertension, benign prostatic hyperplasia, bladder neck obstruction

The glaucoma and ocular hypertension signals are relevant to any ophthalmic use.

**Drug interactions:** 100 interactions were recorded. Those shown include:
- **Moderate:** epinephrine, acarbose, famotidine, isometheptene, clarithromycin, cisapride, bisacodyl, castor oil, diethylpropion, and several antidiabetic agents (albiglutide, alogliptin, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin)
- **Minor:** corticosteroids (hydrocortisone, beclomethasone, betamethasone, budesonide, dexamethasone)

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis has a high model score but no supporting trials or publications. No ophthalmic formulation is registered in South Africa, and knowledge-graph signals for glaucoma and ocular hypertension call for caution.

**To proceed, the following is needed:**
- A literature and trial search specific to salbutamol or beta-2 agonists in papillary or allergic conjunctivitis, plus preclinical ocular data
- Mechanism of action data
- SAHPRA Professional Information (warnings and contraindications), and verification of the registration list, including the Trandate entry
- A route assessment, since only oral and inhaled forms are registered and a topical ocular product would be a new formulation
- A review of the higher-ranked alternatives in the same prediction set. Obstructive lung disease has the strongest evidence, with a completed Phase 3 trial of ipratropium/salbutamol in COPD of 1,118 patients, but it overlaps with the original indication and is not true repurposing. Anaphylaxis (a terminated Phase 3 trial with 24 patients) and bronchitis/bronchiolitis (mixed bronchodilator evidence) were also flagged as research questions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

