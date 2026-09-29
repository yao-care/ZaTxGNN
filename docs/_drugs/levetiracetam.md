---
layout: default
title: Levetiracetam
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is an antiseizure medication, marketed in South Africa as Keppra and Redilev. It is widely used for partial-onset seizures.
The TxGNN model predicts it may be effective for **visual epilepsy** (seizures triggered by visual stimuli, such as photosensitive epilepsy).
This prediction has **9 retrieved clinical trials** and **20 publications**, but none of them studied visual epilepsy directly, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial-onset seizures (from published literature; the SAHPRA registration data supplied contain no indication text) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (mechanism-based inference only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. In general pharmacology, levetiracetam binds the synaptic vesicle protein SV2A and reduces presynaptic neurotransmitter release.

Visual (photosensitive) epilepsy involves cortical hyperexcitability triggered by flickering light or patterns. Reducing excess neurotransmitter release is a plausible way to dampen this. Levetiracetam already treats other seizure types, so a link to reflex seizures is reasonable.

No retrieved study enrolled patients with visual reflex epilepsy. The rationale is therefore inferred from broad antiseizure evidence rather than shown directly.

## Clinical Trial Evidence

No SANCTR or PACTR entries were retrieved.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not yet recruiting | 1649 | Seizure prevention after traumatic brain injury (phenytoin vs levetiracetam, AED duration); no results yet |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not yet recruiting | 580 | Prophylactic levetiracetam in acute intracerebral haemorrhage; no results yet |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Cognitive and neuropsychological safety of adjunctive levetiracetam in children with refractory partial seizures |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Observational study of new antiepileptic drugs as first bitherapy in focal epilepsy |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Levetiracetam for neonatal seizures |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | Levetiracetam to reduce hippocampal hyperactivity in psychosis |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Hippocampal activity modulation (early termination) |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label levetiracetam for migraine prevention, with or without aura |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by invitation | 24 | Gene therapy for Canavan disease; link to levetiracetam unclear |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | Lancet Neurol | PEACH: prophylactic levetiracetam for early seizures after intracerebral haemorrhage |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with encephalitis |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Med J | Levetiracetam vs phenobarbital in childhood epilepsy |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocrit Care | Levetiracetam seizure prophylaxis in neurocritical care |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network meta-analysis | J Neurol | Antiseizure medications for idiopathic generalised epilepsies |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Meta-analysis | Epilepsy Behav | Levetiracetam for myoclonic seizures in idiopathic generalised epilepsy |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Network meta-analysis | Seizure | Treatments for benzodiazepine-resistant status epilepticus |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guideline | Neurocrit Care | Seizure prophylaxis in moderate-severe traumatic brain injury |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam in epilepsy, including its approved uses |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/2.5/0460 | Redilev | Tablet | Not stated in the data supplied |
| Reg. No. A40/2.5/0587 | Keppra | Solution | Not stated in the data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Visual epilepsy has a very high model score, but no retrieved trial or publication studied it directly. The link relies on general antiseizure pharmacology.

Status epilepticus, another prediction for this drug, has far stronger support: the completed Phase 3 ESETT trial (NCT01960075, n=478) found levetiracetam comparable to fosphenytoin and valproate. That indication may merit a separate evaluation.

**To proceed, the following is needed:**
- Visual-epilepsy-specific evidence, such as photosensitive-epilepsy studies with photoparoxysmal EEG response endpoints
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Approved indication text for the Keppra and Redilev registrations
- Any SANCTR or PACTR-registered trials, if they exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

