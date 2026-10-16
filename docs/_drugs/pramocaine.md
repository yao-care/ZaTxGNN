---
layout: default
title: Pramocaine
parent: Model Prediction Only (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pramocaine: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not stated in the SAHPRA registration data. The knowledge graph lists…"
monitor_inn: "Pramocaine"
predicted_indications: ["papillary conjunctivitis", "acne keloid", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "vernal conjunctivitis", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "atopic conjunctivitis", "rosacea conjunctivitis"]
---

# Pramocaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pramocaine: From Topical Skin and Anorectal Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Pramocaine is a topical local anaesthetic, originally used for symptom relief in skin conditions (such as dermatitis, burns and tinea infections), ear conditions and haemorrhoids.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but this is a computational prediction only, with **no clinical trials** and **no publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. The knowledge graph lists tinea pedis, dermatitis, burns, haemorrhoids, otitis externa and related conditions. |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Pramocaine is generally understood to be a topical local anaesthetic that blocks voltage-gated sodium channels, which would give temporary relief of pain and discomfort at the site of application.

Its original uses are surface-level symptom relief on skin, ear and anorectal tissue. In papillary conjunctivitis, a sodium channel blocker could at most numb ocular surface discomfort. There is no evidence that it affects the allergic or mechanical causes of the disease. Ocular use of pramocaine is also not an established route, and prolonged use of topical anaesthetics on the eye can damage the cornea.

The prediction is therefore best viewed as a statistical signal from the knowledge graph, not a mechanistically supported hypothesis. Other highly ranked predictions include vernal, atopic and rosacea conjunctivitis, which suggests the model may be picking up a general ocular or inflammatory cluster rather than a pramocaine-specific effect.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Acne keloid | 98.53% | L5 | Possible symptom relief only; no effect on fibrosis expected |
| 3 | Acrodermatitis chronica atrophicans | 98.43% | L5 | Antibiotic-treated infection; no antimicrobial role |
| 4 | Neonatal dermatomyositis | 98.28% | L5 | Autoimmune; neonatal absorption and methaemoglobinaemia concerns |
| 5 | Vernal conjunctivitis | 98.15% | L5 | Allergic disease; anaesthetic does not address it |
| 6 | Hydroa vacciniforme, familial | 98.12% | L5 | Symptomatic relief at most |
| 7 | Secondary childhood interstitial lung disease (connective tissue disease) | 97.99% | L5 | No plausible mechanism; likely graph artefact |
| 8 | Amyopathic dermatomyositis | 97.87% | L5 | Symptom relief only |
| 9 | Atopic conjunctivitis | 97.81% | L5 | Allergic mechanism not targeted; chronic ocular anaesthetic use unsafe |
| 10 | Rosacea conjunctivitis | 97.79% | L5 | No activity against underlying processes |

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
| E512 | Anugesic | Suppository | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not taken from label text, and to be verified against the Professional Information): hypertension, kidney disease, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, adrenocortical insufficiency, open-angle glaucoma, osteoporosis, benign prostatic hyperplasia, coronary artery disease, sudden cardiac arrest, psychotic and other mental disorders, contact and occupational dermatitis, and several viral and fungal infections (measles, varicella zoster, herpes simplex including herpes simplex keratitis, dermatophytosis). Many of these look like entries inherited from other drugs or drug classes, so they should be interpreted cautiously.
- **Context-specific concerns**: topical anaesthetics can cause corneal toxicity with prolonged ocular use. Use in neonates raises concerns about systemic absorption and methaemoglobinaemia.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings, contraindications and drug interaction information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials, no literature and no supporting mechanism. The ocular route is not established for this product, and the only registered South African product is a suppository.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to establish approved indications, warnings and contraindications
- Detailed mechanism of action data
- A systematic literature search to check for any ocular or conjunctival use of pramocaine
- Route and formulation compatibility assessment (an ophthalmic formulation would be required)
- Ocular safety data, including corneal toxicity risk
- Preclinical or mechanistic evidence that pramocaine affects the pathology of papillary conjunctivitis, beyond transient symptom relief
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

