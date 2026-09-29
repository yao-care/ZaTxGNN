---
layout: default
title: Clopidogrel
parent: Moderate Evidence (L3-L4)
nav_order: 137
evidence_level: L4
indication_count: 10
---

# Clopidogrel
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Clopidogrel: From Antiplatelet Therapy to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is an oral antiplatelet drug (P2Y12 inhibitor) marketed in South Africa. The SAHPRA registration data supplied do not state an approved indication.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are **0 clinical trials** and **16 publications** for this exact subtype, and none of them test it directly.
The evidence is indirect and comes mainly from the broader migraine and PFO/ASD (patent foramen ovale / atrial septal defect) literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (clopidogrel is generally used as an antiplatelet agent in atherothrombotic disease; verify against the PI) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the source data. On general pharmacology, clopidogrel is an irreversible P2Y12 receptor antagonist that inhibits platelet activation.

One hypothesis links migraine with aura to right-to-left shunts such as PFO or ASD. In this model, platelet-derived vasoactive substances or microemboli may trigger aura, so blocking platelet activation could reduce attacks. A second, preclinical hypothesis involves P2Y12 signalling in trigeminal microglia. It is supported by mouse work, but that work is in the parent migraine entry, not this subtype.

The retrieved papers cover migraine with aura in PFO/ASD patients and migraine in general, not the brainstem aura subtype specifically. The link to this subtype is therefore indirect. It is better treated as a subgroup question under the broader **migraine disorder** prediction (TxGNN score 99.44%, evidence level L2).

## Clinical Trial Evidence

Currently no related clinical trials are registered for migraine with brainstem aura.

For context, the parent entry "migraine disorder" lists these trials that directly involve clopidogrel or antithrombotic strategies. No SANCTR or PACTR identifiers were found in the data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | CANOA: clopidogrel added to aspirin to prevent new-onset migraine after transcatheter ASD closure |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Clopidogrel for migraine prophylaxis with right-to-left shunt; no results available |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1000 | COMPETE: anticoagulation vs antiplatelet vs migraine medication in migraine with PFO; no results available |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | RCT (PFO closure, not a drug) | Eur Heart J | PRIMA trial of percutaneous PFO closure in migraine with aura refractory to medical treatment; supports the PFO-migraine association, not clopidogrel |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | Cephalalgia | Pilot randomised trial of clopidogrel as migraine prophylaxis (general migraine population) |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Reviews the evidence on antithrombotic drugs for migraine prevention |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Clinical study | J Investig Med | Clopidogrel 75 mg/day added to existing prophylaxis in drug-refractory migraine with PFO, assessed at 3 and 6 months |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective review | Cephalalgia | Clopidogrel as primary therapy in migraineurs with right-to-left shunt |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after transcatheter closure of PFO/ASD |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot (ticagrelor) | Neurology | Tests ticagrelor, a non-thienopyridine P2Y12 inhibitor, in refractory migraine with PFO |
| [15966922](https://pubmed.ncbi.nlm.nih.gov/15966922/) | 2005 | Case series | J Interv Cardiol | Severe migraine in 5 of 13 patients after ASD closure, with rapid relief after clopidogrel 300 mg |
| [22992406](https://pubmed.ncbi.nlm.nih.gov/22992406/) | 2012 | Case report | Cephalalgia | De novo migraine after ASD closure; ticlopidine (a clopidogrel analogue) was effective |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/8.2/0146 | Mistro | Tablet | Not provided in the data supplied |
| Reg. No. 47/8.2/0009 | Aviolix 75 | Fct | Not provided in the data supplied |
| Reg. No. 44/8.2/0657 | Clopiwin Plus 75/75 | Tablet | Not provided in the data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The DDI query returned no records. This looks like a data gap, not evidence of no interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials for the brainstem aura subtype, and the evidence for migraine with aura comes from PFO/ASD-associated settings. The best support is in the parent migraine disorder entry, where it applies mainly to shunt-associated migraine, and it is not established for migraine in general.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications), which is currently blocking safety screening
- Mechanism of action data from DrugBank
- Safety review for migraine use, especially bleeding risk and CYP2C19 prodrug activation, plus a proper interaction check
- Results from NCT02938182 and NCT05546320, or a decision to evaluate brainstem aura as a subgroup within the migraine disorder entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

