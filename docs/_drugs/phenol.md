---
layout: default
title: Phenol
parent: Model Prediction Only (L5)
nav_order: 369
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-29
monitor_inn: "PHENOL"
predicted_indications: ["acrodermatitis chronica atrophicans", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "dry eye syndrome"]
description: "Phenol: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Phenol: Acrodermatitis chronica atrophicans
{: .text-alpha }

## One-Sentence Summary

Phenol was originally used for dermatitis. The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but there are **0 clinical trials** and **0 publications** supporting this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenol is a known tissue irritant and protein denaturant, and its use in dermatitis comes from the TxGNN model (deep learning) rather than from approved label text. The prediction may reflect similarities the model learned between related diseases, not biological evidence.

The top prediction is not supported by mechanistic reasoning. Acrodermatitis chronica atrophicans is a chronic skin condition associated with *Borrelia* infection and is treated with antibiotics. Phenol has no known antimicrobial or anti-atrophic role in this disease. The high score (0.9995) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical evidence.

Other top-ranked predictions have the same weakness: neonatal and amyopathic dermatomyositis, childhood connective-tissue-disease-related interstitial lung disease, familial hydroa vacciniforme, and severe nonproliferative diabetic retinopathy. All have no trials or publications. Phenol is also dermally absorbed and toxic in neonates, and its tissue toxicity raises ocular safety concerns.

The only prediction with a plausible link is **acne keloid** (rank 5). Phenol is used as a chemical peeling agent that causes controlled dermal injury and remodelling. However, this is indirect, and phenol peeling may worsen hypertrophic scarring.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication (acrodermatitis chronica atrophicans). No trials were found for any of the other predicted indications either.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the data compiled for this report contain literature for two lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17204096](https://pubmed.ncbi.nlm.nih.gov/17204096/) | 2007 | Cohort/Case series (inferred) | J Dermatol | Modified phenol peel (Exoderm) evaluated for facial wrinkles, acne scars and other skin problems in Asian patients. It was designed to reduce side-effects such as arrhythmia, hypopigmentation, hypertrophic scar and keloid. This relates to acne scars (rank 5, acne keloid), not keloid itself. |

For dry eye syndrome (rank 8), the 20 retrieved papers are preclinical or epidemiological studies of dry eye pathophysiology and other compounds (berberine, evodiamine, chrysin and others). None involve phenol, and they do not support its use.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2011 (OM) | Biohist | Syrup | Not stated in the data compiled |

No Essential Medicines List (EML) status was available in the data compiled. The only registered product is a syrup, an oral form. This does not match the topical or local use of phenol in the predicted skin and scarring indications, so route compatibility is unresolved.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (drug–disease contraindication edges, not SAHPRA label text):
- **Cardiac:** sudden cardiac arrest, heart conduction disease, atrioventricular block and dissociation
- **Haematological:** neutropenia, agranulocytosis
- **Metabolic and hepatic:** diabetes mellitus, diabetic ketoacidosis, liver disease, gallbladder disease
- **Respiratory and vascular:** respiratory failure, peripheral vascular disease, intermittent claudication, peripheral arterial disease
- **Infections and skin:** herpes simplex, herpes zoster, cytomegalovirus infection, anogenital HPV infection, common wart, dermatitis
- **Gastrointestinal:** appendicitis, active peptic ulcer disease
- **Neurological and malignant:** epilepsy, progressive multifocal leukoencephalopathy, cancer, embryoma, lymphoma, primary CNS lymphoma, lymphosarcoma

These come from a computational knowledge graph and should be verified against the product label.

**Drug interactions:** No interaction records were found.

**Clinical concerns from the prediction review:** systemic toxicity with dermal absorption (especially in neonates), arrhythmia risk with phenol peels, and ocular tissue toxicity.

The SAHPRA package insert warnings and contraindications have not been reviewed. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a model score, with no trials, no literature and no plausible mechanism. The only registered South African product is an oral syrup, and the label safety review is incomplete.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A route and formulation compatibility assessment, since the registered product is a syrup
- If anything is pursued, **acne keloid** is the only candidate worth a research question. It would need keloid-specific evidence and an assessment of scarring risk from phenol peeling.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

