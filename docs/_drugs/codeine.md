---
layout: default
title: Codeine
parent: Moderate Evidence (L3-L4)
nav_order: 144
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
---

# Codeine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Codeine: From Allergic Rhinitis and Related Upper Airway Conditions to Nasal Cavity Disease

## One-Sentence Summary

Codeine is an opioid medicine that the knowledge graph links to symptom relief in allergic rhinitis, vasomotor rhinitis, pharyngitis, the common cold and headache disorders.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but **no clinical trials** and only **1 publication** (a case report describing an adverse association, not a benefit) were found.
The prediction is therefore best viewed as a model signal that mostly reflects overlap with existing indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, headache disorder (from the knowledge graph; no approved indication text is available in the SAHPRA data) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Codeine is an opioid, and its use in rhinitis, the common cold and headache is established in the knowledge graph, but no mechanism-based argument for nasal cavity disease can be made from the data compiled for this report.

Nasal cavity disease is a broad category that already includes rhinitis and common-cold symptoms. The high score (99.93%) most likely reflects this overlap with existing indications rather than a new therapeutic effect.

The only publication retrieved describes a rhinolith (a stone in the nose) formed around a foreign body made of hardened codeine and opium. This is an incidental or adverse association, not evidence of benefit.

Other predictions were also generated for this drug. They were weaker or argue against repurposing:
- **Acute laryngopharyngitis** (score 99.92%): no trials or literature. It is closely related to the existing pharyngitis and common cold indications, so any benefit would be speculative.
- **Trigeminal autonomic cephalalgia** (score 99.43%): the two publications are descriptive and show no benefit from codeine. Opioids are generally not recommended in cluster headache because of dependence and medication-overuse headache.
- **Allergic urticaria** (score 99.37%): the literature shows that codeine causes mast-cell histamine release and urticaria, and it is used as a skin-test positive control. This points to harm, not treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | Unusual rhinolith formed around a foreign body of hardened codeine and opium ("opioma") in a 21-year-old man with nasal obstruction. It describes an incidental association, not a therapeutic effect. |

---

## South Africa Market Information

Twenty valid single-ingredient registrations were found. No approved indication text is recorded for any of them. The first five are listed below. Essential Medicines List (EML) status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| S/2.8/137 | Empacod | Tablet | Not available |
| B 1006 (ACT 101) | Omnopon 1ml Fresenius 20 | Injection | Not available |
| B1192 (ACT 101) | Codeine phos | Tablet | Not available |
| X/2.8/109 | Cogesic | Tablet | Not available |
| G1260 (ACT 101) | Codomil new formula | Syrup | Not available |

The remaining registrations include syrups, capsules, tablets and one suspension.

---

## Safety Considerations

- **Disease-level cautions (knowledge graph):** The knowledge graph lists many conditions in which codeine is contraindicated or requires caution. These come from graph relationships, not from label text. Examples include:
  - Respiratory: chronic obstructive pulmonary disease
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Neurological and psychiatric: epilepsy, anxiety disorder, psychotic disorder
  - Gastrointestinal: pancreatitis, gallbladder disease, peptic ulcer disease, inflammatory bowel disease
  - Endocrine and metabolic: hypothyroidism, porphyria
  - Other: hypertension, thrombocytopenia
- **Drug interactions:** The interaction query returned 100 interactions in total, of which 20 are shown here. Two are rated Major:
  - Alvimopan
  - Bupropion

  The listed Moderate interactions include:
  - Anticholinergics: atropine, glycopyrronium, hyoscyamine, dicyclomine, clidinium
  - Antidiarrhoeals: loperamide, kaolin, attapulgite
  - Antiemetics: granisetron, dolasetron
  - Others: cimetidine, dexamethasone, dronabinol, eliglustat, eluxadoline

For label warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and overlap with existing indications. There are no clinical trials, and the only publication describes an adverse association, not benefit. Opioid-related safety concerns and the lack of mechanism data further weaken the case.

**To proceed, the following is needed:**
- Mechanism of action data for codeine
- The SAHPRA package insert (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Clarification of what "nasal cavity disease" would mean as a distinct indication beyond existing rhinitis and common-cold use
- Any controlled clinical evidence of benefit in the predicted indication. None was found.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

