---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease and related parkinsonian syndromes"
monitor_inn: "ENTACAPONE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
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

## Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor, originally used as an add-on to levodopa in Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration** (score 0.9976), but **no clinical trials and no publications** specifically support this prediction.
The evidence is model-based only, so this top prediction should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian syndromes (the SAHPRA registration entries in the data compiled for this report contain no indication text) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Entacapone is generally known as a peripheral COMT inhibitor. By slowing the breakdown of levodopa, it prolongs levodopa's effect. Both registered South African products are Stalevo tablets (see the market table below).

PLA2G6-associated neurodegeneration covers a spectrum of disorders, including infantile neuroaxonal dystrophy and an adult-onset dystonia-parkinsonism form. A plausible link is symptomatic relief of parkinsonism in the adult-onset form, by extending levodopa benefit. Entacapone would not address the underlying disease processes (disrupted phospholipid metabolism and brain iron accumulation).

This prediction is therefore supported only by its similarity to the original indication. It has no disease-specific evidence.

### Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Rasmussen subacute encephalitis | 0.9973 | L5 | No clear mechanistic rationale |
| 3 | Myelitis | 0.9963 | L5 | No relevant anti-inflammatory mechanism |
| 4 | Juvenile paralysis agitans (Hunt) | 0.9960 | L5 | Close to the original indication, but benefit would be extrapolated and the score may be inflated by ontology overlap |
| 5 | Transaldolase deficiency | 0.9943 | L5 | No plausible mechanism |
| 6 | Lethal infantile mitochondrial myopathy | 0.9928 | L5 | No mechanism; hepatotoxicity is an added concern |
| 7 | Lewy body dementia | 0.9925 | L5 | Indirect preclinical support only |
| 8 | Fructose-1,6-bisphosphatase deficiency | 0.9922 | L5 | No plausible mechanism |
| 9 | Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis | 0.9906 | L5 | Structural developmental disorder |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 0.9904 | L5 | Indirect evidence only |

Lewy body dementia (rank 7) and progressive supranuclear palsy-corticobasal syndrome (rank 10) have slightly more supporting material than the top prediction, but this material is background only and does not test entacapone.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication, PLA2G6-associated neurodegeneration.

For lower-ranked predictions, the only trials found are tangential, and none tests entacapone:

| Trial Number | Related Prediction | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Lewy body dementia | Phase 1 | Recruiting | 40 | [18F]F-DOPA PET imaging in autonomic failure (including synucleinopathies); a diagnostic study, not a test of entacapone |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | PSP-corticobasal syndrome | N/A | Active, not recruiting | 120 | Gait pattern analysis in neurological disease, including parkinsonian disorders; no entacapone intervention |

## Literature Evidence

Currently no related literature is available for the top predicted indication.

For Lewy body dementia (rank 7), two preclinical publications were identified:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC organoid model) | Science Advances | Cortical organoids with SNCA triplication reproduce alpha-synuclein pathology in Lewy body disease and were used to identify candidate therapeutic drugs |
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro study | J Neurosci Res | Examined antiparkinsonian agents for effects on beta-amyloid and alpha-synuclein oligomer formation; indirect preclinical support only |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 8/5.4.1/0138 | Stalevo 100/25 | Tablet (oral) | Indication text not available in the compiled data |
| Reg. No. 38/5.4.1/0137 | Stalevo 150/37.5 | Tablet (oral) | Indication text not available in the compiled data |

Both registrations are valid and none are cancelled. The data compiled for this report do not state Essential Medicines List (EML) status.

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Contraindication signals from the knowledge graph** (not label text, so they must be verified against the PI). They include:
- Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, postural orthostatic tachycardia syndrome
- Neurological and psychiatric: epilepsy, drug-induced dyskinesia, multiple system atrophy, psychotic disorder, schizoaffective disorder, schizophreniform disorder, anxiety disorder, neurotic disorder, dysthymic disorder, mental disorder
- Organ disease: liver disease, kidney disease, gallbladder disease
- Gastrointestinal: gastric ulcer, peptic ulcer disease, diarrhoeal disease
- Eye: open-angle glaucoma, angle-closure glaucoma
- Metabolic and other: diabetes mellitus, diabetic ketoacidosis, melanoma, haemoglobinopathy, pyoureter

**Drug interactions:** 82 interactions were recorded. Those listed below come from DDInter.
- Moderate severity: epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide, iron
- Severity unknown: pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin, potassium chloride

Hepatotoxicity has been noted as a concern in the mitochondrial disease prediction (by analogy with tolcapone). Liver safety would need particular attention in any metabolic or mitochondrial population.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, PLA2G6-associated neurodegeneration, rests on model score alone (L5), with no trials or literature. Any benefit would be limited to symptomatic parkinsonism and would be extrapolated from Parkinson disease. The safety data from the package insert are also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data (e.g. from DrugBank)
- Disease-specific clinical evidence (case series or trials) of entacapone with levodopa in PLA2G6-related dystonia-parkinsonism
- Review of whether the high score for juvenile parkinsonism reflects real signal or ontology overlap with the original indications
- If a follow-up is wanted, Lewy body dementia and PSP-corticobasal syndrome could be framed as research questions (L4). This would require direct clinical data and an assessment of psychosis risk in Lewy body dementia.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

