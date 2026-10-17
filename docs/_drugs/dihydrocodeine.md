---
layout: default
title: Dihydrocodeine
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dihydrocodeine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Dihydrocodeine"
predicted_indications: ["acute laryngopharyngitis", "allergic urticaria", "papillary conjunctivitis", "faucial diphtheria", "cervical disc degenerative disorder", "headache disorder", "cold urticaria", "trigeminal autonomic cephalalgia", "atopic conjunctivitis"]
---

# Dihydrocodeine
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

# Dihydrocodeine: From Allergic Rhinitis and Upper Respiratory Tract Symptoms to Nasal Cavity Disease

## One-Sentence Summary

Dihydrocodeine is an opioid originally used for symptom relief in upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **no clinical trials** and **no publications** supporting this specific prediction.
The prediction is essentially a model output and largely overlaps with the drug's existing uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (from the knowledge graph; the SAHPRA registrations carry no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dihydrocodeine is an opioid analgesic and antitussive. It is already used for symptomatic relief in rhinitis and related upper respiratory conditions.

The very high TxGNN score most likely reflects similarity to its existing indications (allergic and vasomotor rhinitis) rather than a new mechanism. As an opioid, dihydrocodeine acts on central cough and pain pathways, not on nasal pathology itself. Because the mechanism data is missing, the link cannot be verified.

**Other predictions from the model (all Hold, mostly L5):**
- **Acute laryngopharyngitis** (99.99%): closely related to existing indications. Symptomatic relief of cough and throat pain is plausible, but the prediction is not independent of the labelled uses.
- **Allergic urticaria and cold urticaria**: opioids can cause histamine release, so any link is in the adverse-effect direction.
- **Papillary and atopic conjunctivitis**: likely graph proximity to allergic disease, with no plausible opioid mechanism.
- **Faucial diphtheria**: at most symptomatic relief; antitoxin and antibiotics are the treatment.
- **Cervical disc degenerative disorder**: symptomatic pain relief is plausible, but chronic opioid use carries risks of tolerance, dependence and respiratory depression.
- **Headache disorder** (L4, two weak publications) and **trigeminal autonomic cephalalgia**: opioids are generally discouraged because of medication-overuse headache risk and the availability of specific therapies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication (nasal cavity disease). For the lower-ranked prediction of headache disorder, only two weak publications were retrieved:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/) | 2002 | Case series / abuse study | Nihon Arukoru Yakubutsu Igakkai Zasshi | Clinical study of abuse of cough suppressant syrups in Japan. Methylephedrine and dihydrocodeine are linked to dependence. Not evidence of benefit in headache. |
| [28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/) | 2017 | Review (Cochrane listing) | J Pain Palliat Care Pharmacother | General listing of Cochrane reviews published January-March 2017. No specific evidence for dihydrocodeine. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B1041 ACT 101 OF 1965 | Paracodin | Syrup | Not available in the data compiled for this report |
| B730 (ACT 101) | Df 118 1ml | Injection | Not available in the data compiled for this report |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status was not available in the compiled data.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived associations, not label text): hypertension, liver failure and liver disease, epilepsy, insomnia, chronic obstructive pulmonary disease, kidney disease, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism and myxedema, peptic ulcer disease, inflammatory bowel disease, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hypotensive disorder, gout, substance abuse/dependence, hemophilia, coronary artery disease and myocardial infarction, hemoglobinopathy, and others.
- **Drug interactions:** 100 interactions were identified. The major-severity ones in the list shown are **alvimopan** and **bupropion**. Moderate interactions include anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine), antidiarrhoeals (loperamide, kaolin, attapulgite), 5-HT3 antagonists (granisetron, dolasetron), aprepitant, cimetidine, dexamethasone, dronabinol, eluxadoline, and fenfluramine and dexfenfluramine.
- **Class risks:** opioid-related histamine release, dependence and abuse potential (supported by PMID 11915306), and respiratory depression.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or publications. It largely restates the drug's existing use in rhinitis, and the mechanism is unverified. Opioids add dependence and respiratory risks, and in several lower-ranked predictions (urticaria, conjunctivitis, headache) the mechanism is implausible or the effect is adverse.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indication text (a blocking gap for safety screening)
- Mechanism of action data for dihydrocodeine
- Clarification of what "nasal cavity disease" covers, and whether it adds anything beyond the existing rhinitis indications
- Clinical or observational evidence for the proposed use, with a benefit-risk assessment against existing non-opioid options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

