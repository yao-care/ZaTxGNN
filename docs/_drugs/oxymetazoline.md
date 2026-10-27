---
layout: default
title: Oxymetazoline
parent: Moderate Evidence (L3-L4)
nav_order: 361
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Oxymetazoline: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Pharyngitis, common cold"
monitor_inn: "OXYMETAZOLINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "headache disorder"]
---

# Oxymetazoline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Oxymetazoline: From Pharyngitis and Common Cold to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Oxymetazoline is a topical nasal decongestant, originally used for pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but there are **no registered clinical trials** and only **5 publications** (mostly indirect) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold (from the knowledge graph; the SAHPRA registration carries no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, oxymetazoline is a topical alpha-adrenergic agonist (alpha-1 and partial alpha-2). It constricts blood vessels in the nasal mucosa, which reduces swelling and congestion. Receptor-binding data compiled for this report also list activity at several alpha-1 and alpha-2 adrenoceptor subtypes and at 5-HT1B, 5-HT1D and 5-HT2C receptors.

The predicted indication is very close to the existing use. Nasal congestion in the common cold is already a nasal cavity condition, so this prediction is largely an extension of the current indication rather than a true repurposing. The high score is therefore plausible, but it does not by itself show new benefit.

The other two predictions are weaker:
- **Acute laryngopharyngitis** (score 99.95%, L5): This is a computational prediction only, with no trials or literature. Topical nasal delivery does not reliably reach the pharynx or larynx. The score is probably driven by the link to the original pharyngitis indication.
- **Headache disorder** (score 99.04%, L4): One small study reports intranasal tetracaine plus oxymetazoline in status migrainosus (PMID 31919839). Oxymetazoline cannot be separated from the local anaesthetic in that combination, so its own contribution is unknown.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for nasal cavity disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Clinical physiology study | Ann N Y Acad Sci | Effects of the common cold on olfactory function in 36 subjects, using evoked potentials, psychophysical tests and acoustic rhinometry |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal study | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops in rabbit acute sinusitis; tested the effect on early local tissue defence in bacterial infection |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Observational | J Plast Surg Hand Surg | Nasal patency by acoustic rhinometry after cleft lip and palate repair; oxymetazoline likely used as a decongestant for measurement |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Procedural report | Am J Rhinol Allergy | Coblation of nasal telangiectasias in hereditary haemorrhagic telangiectasia; oxymetazoline likely incidental or adjunctive |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Glob Pediatr Health | Rhinoscleroma in a 9-year-old boy; not directly relevant to oxymetazoline therapy |

None of these is a randomised trial of oxymetazoline in nasal cavity disease, so the evidence is indirect.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H1501 (OM) | Nazene Z 20ml | Spray | Not stated in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

---

## Safety Considerations

- **Contraindications and cautions flagged in the knowledge graph** (these are drug-disease associations, not label text): hypertension, heart disease, cardiovascular disease, coronary artery disease, arteriosclerosis and atherosclerosis, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hyperthyroidism (Graves disease, thyrotoxicosis), angle-closure glaucoma, vision disorders, and eye infections including conjunctivitis.
- **Drug interactions:** The interaction query returned receptor-level pharmacology only (5-HT1B, 5-HT1D, 5-HT2C, alpha-1A/1B/1D and alpha-2A/2B/2C), and no drug-drug interaction entries. Literature related to the headache prediction raises a hypertensive risk with monoamine oxidase inhibitors.
- **Prolonged use:** Rebound congestion is a recognised risk with extended use (noted in the literature compiled for the headache prediction).

The SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mostly a restatement of the existing nasal decongestant use. There are no clinical trials, and the literature is indirect (physiology, animal and case-level studies). Safety review also cannot be completed because the SAHPRA package insert data is missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication) for Nazene Z.
- Detailed mechanism of action data from DrugBank.
- Controlled clinical evidence in a defined nasal cavity condition, to show a benefit beyond current decongestant use.
- For the headache prediction, a study that isolates oxymetazoline from the tetracaine combination.
- For the acute laryngopharyngitis prediction, evidence that topical nasal delivery reaches the target tissue.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

