---
layout: default
title: Clopidogrel
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clopidogrel: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Acute coronary syndrome"
monitor_inn: "Clopidogrel"
predicted_indications: ["migraine with brainstem aura", "migraine disorder", "osteoarthritis", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "rheumatoid arthritis", "osteoarthritis susceptibility", "pseudoachondroplasia", "fibromyalgia"]
---

# Clopidogrel
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

# Clopidogrel: From Acute Coronary Syndrome to Migraine Disorder

## One-Sentence Summary

Clopidogrel is an antiplatelet (P2Y12 inhibitor) medicine, originally used for acute coronary syndrome, intracranial embolism and ST-elevation myocardial infarction.
The TxGNN model predicts it may be effective for **migraine disorder** (the top-ranked prediction, migraine with brainstem aura, is a subtype with no dedicated trials). Supporting this direction are **6 registered clinical trials** and **about 20 publications**, including a recent multicentre randomised trial. Most of this evidence comes from patients with patent foramen ovale (PFO) or atrial septal defect (ASD) closure, not from unselected migraine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome; intracranial embolism; ST-elevation myocardial infarction (SAHPRA indication text is not available in the data compiled for this report) |
| Predicted New Indication | Migraine with brainstem aura (rank 1, TxGNN); migraine disorder (rank 2) is evaluated in detail below because it has the strongest evidence |
| TxGNN Prediction Score | 99.44% (migraine with brainstem aura); 99.44% (migraine disorder) |
| Evidence Level | L2 (migraine disorder); L3 (migraine with brainstem aura) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Proceed with Guardrails (migraine disorder in PFO-related migraine, research setting only) |

**Other predictions in the top 10.** Osteoarthritis, tendinitis, idiopathic granulomatous myositis, myositis fibrosa, rheumatoid arthritis, osteoarthritis susceptibility, pseudoachondroplasia and fibromyalgia have little or no supporting evidence (L4–L5). All are rated **Hold**. For rheumatoid arthritis, the literature includes reports of clopidogrel-associated inflammatory arthritis, which is a safety signal against use. For osteoarthritis, a propensity-matched study suggests ticagrelor, not clopidogrel, is associated with lower risk.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Clopidogrel is known to be a P2Y12 platelet inhibitor. Its efficacy in preventing thrombotic events in acute coronary syndrome and ischaemic cerebrovascular disease is established.

The migraine link is based on a platelet and right-to-left shunt hypothesis. In people with PFO or a septal device, paradoxical microemboli or platelet-derived vasoactive substances (such as serotonin) may trigger cortical spreading depression. P2Y12 inhibition may reduce platelet activation and so reduce migraine attacks. Preclinical papers also describe P2Y12 receptor involvement in migraine models in mice.

This rationale applies mainly to migraine with aura in patients with PFO. It has not been shown for brainstem aura specifically, and effects in unselected migraine are unproven. Results across studies are heterogeneous.

## Clinical Trial Evidence

Trials below relate to migraine disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) (COMPETE) | Phase 2 | Completed | 1000 | Anticoagulation vs antiplatelet vs standard migraine medication in migraine with PFO; published as a BMJ trial |
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) (CANOA) | Phase 4 | Completed | 220 | Clopidogrel added to aspirin to prevent new-onset migraine after transcatheter ASD closure |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Clopidogrel prophylaxis in migraine with right-to-left shunt; small, status uncertain |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) (SPRING) | Phase 3 | Active, not recruiting | 440 | PFO closure vs medicine for migraine; indirect support only (device trial) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs anticoagulants vs antiplatelets for stroke recurrence; migraine is not the primary endpoint |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | Septal occluder device study, stopped after 7 participants; no clopidogrel-specific evidence |

No trials are registered for migraine with brainstem aura. No SANCTR or PACTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT (multicentre, open label) | BMJ | Antithrombotic treatment for migraine prevention in patients with PFO (COMPETE) |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | Clopidogrel plus aspirin vs aspirin alone for migraine after transcatheter ASD closure (CANOA) |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT follow-up | JAMA Cardiology | One-year CANOA results, including outcomes after clopidogrel was stopped at 3 months |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (pilot) | Cephalalgia | Pilot randomised study of clopidogrel as migraine prophylaxis |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic review | Headache | Reviews the role of antithrombotic drugs in migraine prevention |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systematic review | Indian J Thorac Cardiovasc Surg | Incidence and management of new-onset headache after transcatheter ASD closure |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | J Investig Med | Clopidogrel 75 mg/day added to existing prophylaxis in drug-refractory migraine with PFO |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective review | Neurology | Off-label thienopyridine therapy in migraineurs with PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospective review | Cephalalgia | Clopidogrel as primary therapy for migraineurs with right-to-left shunt |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohort | Heart | Clopidogrel reduced migraine with aura after closure of PFO and ASD |

The abstracts available in the data compiled for this report are truncated and do not give effect sizes. Please read the full papers before drawing conclusions about the size or direction of benefit in each study.

## South Africa Market Information

Three valid single-ingredient registrations are on record. Approved indication text and manufacturer details are not available in the data compiled for this report. Essential Medicines List (EML) status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/8.2/0146 | Mistro | Tablet | Not available |
| Reg. No. 47/8.2/0009 | Aviolix 75 | Film-coated tablet | Not available |
| Reg. No. 44/8.2/0657 | Clopiwin Plus 75/75 | Tablet | Not available |

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** acute liver failure, hepatitis, blood coagulation disease, injury, thrombocytopenic purpura, active peptic ulcer disease and intracranial haemorrhage.

**Drug interactions (100 recorded; examples):**
- **Major:** rabeprazole, omeprazole, esomeprazole (proton pump inhibitors, which may reduce clopidogrel activation), pioglitazone, loperamide, repaglinide.
- **Moderate:** acetylsalicylic acid, morphine, bupropion, cimetidine, clarithromycin, lansoprazole, pantoprazole, fenfluramine, dexfenfluramine, sibutramine, opium, eluxadoline.
- **Minor:** dexlansoprazole, glimepiride.

**Context-specific concerns:**
- Bleeding risk must be weighed against a non-life-threatening condition such as migraine.
- The literature includes case reports of bleeding with clopidogrel combinations (haemarthrosis, intracerebral haemorrhage with celecoxib) and of agranulocytosis with metamizole.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (migraine disorder in PFO-related migraine, within a research or specialist-supervised setting only). **Hold** for all other predicted indications.

**Rationale:**
- Migraine in patients with PFO or after ASD closure has randomised evidence, including CANOA, a pilot RCT and a recent multicentre trial. Results are heterogeneous, the populations are narrow, and benefit in unselected migraine is unproven.
- The top-ranked prediction, brainstem aura, has no dedicated trials, and the remaining predictions have little or no supporting evidence.
- Bleeding risk, and the fact that the SAHPRA label safety data is missing from the data compiled for this report, call for caution.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indications. These are currently missing, and the lack of them blocks formal safety screening.
- Mechanism-of-action data from DrugBank.
- Full-text review of the COMPETE and CANOA trials to confirm effect sizes and bleeding outcomes.
- Defined patient selection criteria (for example, migraine with aura and confirmed PFO) and a bleeding-risk assessment.
- A check of local relevance, including the prevalence of PFO-related migraine in South Africa, and review of any relevant SANCTR or PACTR registrations.
- Guidance on avoiding interacting drugs, especially proton pump inhibitors.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

