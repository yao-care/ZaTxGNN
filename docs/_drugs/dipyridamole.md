---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilator drug, listed in the knowledge graph used for this report under atrial fibrillation.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials** and only **10 publications** (mostly diagnostic-testing studies and case reports) exist for this indication, and the mechanism suggests possible harm rather than benefit.
The strongest-supported prediction for this drug is **stroke disorder / transient ischaemic attack (secondary prevention)**, which is already an established use rather than a new one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (from the knowledge graph; the SAHPRA registration carries no indication text) |
| Predicted New Indication | Prinzmetal angina (rank 1) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 for Prinzmetal angina (L1 for stroke disorder and TIA, rank 2 and 5) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold (Prinzmetal angina); Proceed with Guardrails (stroke disorder, TIA) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the literature, dipyridamole inhibits phosphodiesterase and adenosine reuptake. This raises cAMP, cGMP and extracellular adenosine, which reduces platelet aggregation and causes vasodilation.

**Prinzmetal angina (rank 1):** The high score is not supported by clinical evidence of benefit. Adenosine-driven coronary vasodilation is more likely to be harmful than helpful in vasospastic angina. The available publications describe dipyridamole as a diagnostic stress agent. One report describes coronary vasospasm triggered when aminophylline reversed dipyridamole stress in variant angina. A 1978 study of resting angina tested several drugs, including dipyridamole, but the data compiled for this report do not show a therapeutic benefit. This is a diagnostic or provocative association, not a therapeutic one.

**Stroke disorder and TIA (rank 2 and 5):** The mechanism fits well. Antiplatelet action, with possible anti-inflammatory and neuroprotective effects, is consistent with secondary stroke prevention. Aspirin plus extended-release dipyridamole is a recognised option for this use. This is an established indication, not a new repurposing finding.

**Other predictions (rank 3, 4, 6-10):** These are weaker. Thrombotic disease has only indirect evidence. The sinus node, genetic syndrome and muscular dystrophy predictions have no mechanistic rationale. Cavernous and lateral sinus thrombosis are plausible only in principle, and standard care is anticoagulation and treating infection.

## Clinical Trial Evidence

No clinical trials are registered for Prinzmetal angina. The trials below are for the best-supported predictions, stroke disorder and TIA.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) (ESPRIT) | Phase 4 | Completed | 4,500 | Aspirin plus dipyridamole or mild anticoagulation versus aspirin alone after cerebral ischaemia of arterial origin |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) (EARLY) | Phase 4 | Completed | 551 | Aspirin plus dipyridamole started within 24 hours versus after 7 days of aspirin in ischaemic stroke |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) (CADISS) | Phase 3 | Completed | 250 | Anticoagulants versus antiplatelets in cervical artery dissection; dipyridamole is part of the antiplatelet arm but not the focus |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure or anticoagulants versus antiplatelet therapy; dipyridamole not specifically tested |
| [NCT00738894](https://clinicaltrials.gov/study/NCT00738894) (REDUCE) | N/A | Completed | 664 | PFO closure device plus antiplatelets versus antiplatelets alone; dipyridamole is not the intervention of interest |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Completed | 240 | Oxidative stress and oxysterol profiling after carotid revascularisation (biomarker study) |
| [NCT06053021](https://clinicaltrials.gov/study/NCT06053021) | N/A | Unknown | 1,200 | Antiplatelet therapy in acute ischaemic stroke with thrombocytopenia; agent unclear |

## Literature Evidence

**Prinzmetal angina (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review/Observational | Jpn Circ J | Drug responses in 26 patients with resting angina, including 13 with Prinzmetal's variant angina; propranolol tended to aggravate attacks |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case report/Observational | Am J Cardiol | Aminophylline termination of dipyridamole stress triggered coronary vasospasm in variant angina |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Observational | Br Heart J | Reproducibility of exercise testing in patients with ST elevation and varied responses to the dipyridamole test |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Observational | Zhonghua Xin Xue Guan Bing Za Zhi | Clinical features of atypical coronary artery spasm |

**Stroke disorder and TIA (rank 2 and 5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-analysis | Stroke | Individual patient data meta-analysis of dipyridamole, with or without aspirin, after ischaemic stroke or TIA |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane review | Cochrane Database Syst Rev | Adding dipyridamole to aspirin was associated with a 22% risk reduction versus aspirin alone in one trial |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-analysis | BMJ | Antiplatelet therapy in high-risk patients |
| [31177983](https://pubmed.ncbi.nlm.nih.gov/31177983/) | 2019 | Network meta-analysis | Stroke | Efficacy and safety of antiplatelets after noncardioembolic stroke or TIA |
| [34399713](https://pubmed.ncbi.nlm.nih.gov/34399713/) | 2021 | Network meta-analysis | BMC Neurol | Antiplatelet drugs for secondary prevention after ischaemic stroke or TIA |
| [34211246](https://pubmed.ncbi.nlm.nih.gov/34211246/) | 2021 | Review | Aust Prescr | Aspirin, clopidogrel, or aspirin with dipyridamole are first-line options for secondary prevention in the absence of atrial fibrillation |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/8/0641 | Asasantin 200/25 Retard | Capsule (oral) | Not available in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links dipyridamole to the following contraindication-type conditions. These should be checked against the SAHPRA Professional Information (PI):
- Bleeding and haematological: thrombocytopenia, thrombocytopenic purpura, haemophilia, congenital prothrombin deficiency, vitamin K deficiency haemorrhagic disease, anaemia, haemoglobinopathy
- Gastrointestinal: peptic ulcer disease (including active), gastritis
- Cardiovascular: acute coronary syndrome, myocardial infarction, coronary thrombosis, hypotensive disorder
- Other: kidney disease, liver disease, gallbladder disease, gout, Reye syndrome, Alzheimer disease, nasal cavity polyp, substance abuse/dependence, and several electrolyte and metabolic disorders

**Drug Interactions:** 100 interactions were identified. The main ones with a rated severity are moderate interactions with dexfenfluramine, sibutramine and fenfluramine. Others, including acetylsalicylic acid, cimetidine, metformin, omeprazole, pantoprazole, morphine and simvastatin, are of unknown severity.

**Additional guardrails:** Monitor for bleeding and headache, and for vasodilation-related adverse effects. Adenosine-enhancing effects may worsen sinus node suppression or bradycardia (relevant to the sick sinus syndrome prediction).

Warnings and contraindications from the SAHPRA-approved PI were not available. Please refer to the PI for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold (Prinzmetal angina); Proceed with Guardrails (stroke disorder and TIA, as established uses only)**

**Rationale:**
- For Prinzmetal angina, the high TxGNN score is not backed by any trial or therapeutic evidence, and the mechanism may worsen vasospasm. Evidence level is L4.
- The stroke and TIA predictions are supported by ESPRIT and multiple meta-analyses (L1), but this is already established practice, not new repurposing. Newer regimens such as short-term dual antiplatelet therapy and cilostazol are also used and should be considered against current guidelines.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Approved indication text for the Asasantin 200/25 Retard registration, to confirm the original indication in South Africa
- For Prinzmetal angina: any controlled evidence of therapeutic benefit and a safety assessment of vasospasm risk before reconsidering
- For stroke and TIA: confirmation of the registered indication and alignment with current South African guidelines
- For the lower-ranked predictions (thrombotic disease and below): a defined, specific indication and supporting trials before evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

