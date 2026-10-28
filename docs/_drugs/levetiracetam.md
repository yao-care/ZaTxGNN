---
layout: default
title: Levetiracetam
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-29
monitor_inn: "LEVETIRACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
description: "Levetiracetam: predicted new indication Beta-ketothiolase deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Levetiracetam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Levetiracetam: Beta-ketothiolase deficiency
{: .text-alpha }

## One-Sentence Summary

Levetiracetam is an antiseizure medication originally used for partial (focal) epilepsy.
The prediction currently rests on the general antiseizure mechanism and literature from other seizure populations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Beta-ketothiolase deficiency |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data set. The published literature describes levetiracetam as binding synaptic vesicle protein 2A (SV2A), which modulates neurotransmitter release and dampens neuronal hyperexcitability. This is the basis of its use in focal epilepsy.

Visual (photosensitive or reflex) epilepsy involves abnormal brain excitability triggered by visual stimuli. Reducing excitatory neurotransmitter release is therefore a plausible way to help. The link is indirect, because the retrieved literature covers general seizure populations (neonatal seizures, post-stroke seizures, neurocritical care prophylaxis) and does not address visual or photosensitive epilepsy specifically.

**Other predictions for this drug.** The model returned several other reflex-seizure and seizure-related predictions. Their evidence varies widely:

| Predicted Indication | Evidence Level | Comment |
|------|------|------|
| Status epilepticus | L1 | Strongest support: 2 completed Phase 3 trials (NCT01960075 ESETT, 478 patients; NCT01150331, 203 patients) plus several Phase 2 paediatric trials. Recommended decision: Proceed with Guardrails. |
| Startle epilepsy | L3 | Small uncontrolled add-on studies (2007, 2008) and case reports. No registered trials. |
| Audiogenic seizures | L3 | Mainly animal studies and a veterinary RCT in cats, so human translation is unproven. |
| Eating, thinking, micturition-induced and reading seizures | L4 | Only indirect literature. |
| Orgasm-induced seizures, beta-ketothiolase deficiency | L5 | Model prediction only. Beta-ketothiolase deficiency has no plausible mechanistic link and appears to be a prediction artefact. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visual epilepsy.

---

## Literature Evidence

No publication addresses visual epilepsy directly. The most relevant general seizure evidence is listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam versus phenobarbital for neonatal seizures |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | PEACH: prophylactic levetiracetam for early seizures after intracerebral haemorrhage |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (open label) | Seizure | Phenytoin versus levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Network meta-analysis | Neurology | Antiseizure medications in poststroke seizures |
| [40975024](https://pubmed.ncbi.nlm.nih.gov/40975024/) | 2025 | Meta-analysis | Clinical Neurology and Neurosurgery | Levetiracetam versus phenobarbitone for neonatal seizures |
| [39899098](https://pubmed.ncbi.nlm.nih.gov/39899098/) | 2025 | Review | Continuum | First seizures, acute repetitive seizures and status epilepticus |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam in epilepsy |
| [12915343](https://pubmed.ncbi.nlm.nih.gov/12915343/) | 2003 | Review | Epileptic Disorders | Safety profile of levetiracetam |
| [35848684](https://pubmed.ncbi.nlm.nih.gov/35848684/) | 2022 | Case report | Journal of Postgraduate Medicine | Levetiracetam-induced gingival hyperplasia (safety signal) |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/2.5/0460 | Redilev | Tablet | Not available in the compiled data |
| Reg. No. A40/2.5/0587 | Keppra | Solution | Not available in the compiled data |

Both registrations are valid single-ingredient products. Essential Medicines List status was not available in the compiled data. Please verify the approved indications in the SAHPRA Professional Information (PI).

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from drug-disease graph data, not from label text, and should be confirmed against the PI): anxiety and related disorders, neurotic disorder, dysthymic disorder, depersonalization disorder, psychotic disorders (including schizophreniform and schizoaffective disorder), mental disorder, kidney disease, pyoureter, liver disease, gallbladder disease, and blood disorders (neutropenia, agranulocytosis, leukopenia, pancytopenia).
- **Drug interactions:** the interaction screen returned 100 interactions. The ones rated Moderate are morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and sibutramine. Others, such as pantoprazole, metformin, omeprazole and doxycycline, appear with an unclassified severity level.
- **Literature safety signals** (individual reports, not label warnings): hyponatraemia, gingival hyperplasia, and seizure aggravation reported in a minority of users.

Please refer to the SAHPRA-approved Professional Information (PI) for the full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting literature concerns general seizure populations. By contrast, status epilepticus has Phase 3 RCT support and merits separate evaluation (Proceed with Guardrails).

**To proceed, the following is needed:**
- Condition-specific clinical evidence in photosensitive or visual reflex epilepsy (case series, controlled studies, or a registered trial)
- SAHPRA Professional Information, to confirm approved indications, warnings and contraindications
- Detailed mechanism-of-action data
- A separate evaluation of status epilepticus, including confirmation against current guidelines (ESETT showed no efficacy difference among levetiracetam, fosphenytoin and valproate), age- and renal-function-based dosing, and behavioural adverse effect monitoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

