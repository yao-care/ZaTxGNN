---
layout: default
title: Caffeine
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From Headache and Cold-Related Conditions to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is widely used as an analgesic adjuvant in combination products for headache, migraine, allergic and vasomotor rhinitis, and cold and flu symptoms.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **0 clinical trials** and only **3 loosely related publications** (a bitter taste receptor review, a nasal gel formulation study and a rat study). None of these addresses a nasal disease outcome, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, migraine, headache disorders, pharyngitis, common cold (from the knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Caffeine blocks adenosine receptors and inhibits phosphodiesterase. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description reflects general pharmacology. Bitter taste receptors are present in the airways, including the nasal cavity, and may be modulated by caffeine. This could influence ciliary beating and local airway responses.

Caffeine is already part of combination products for allergic and vasomotor rhinitis and for cold and flu symptoms. This is a plausible bridge to a broader "nasal cavity disease" category. However, the high TxGNN score probably reflects closeness to these existing rhinitis indications rather than independent evidence. "Nasal cavity disease" is also a very broad category, and the prediction does not name a specific condition.

Other candidate indications were also screened. None has clinical trials, and the current recommendations are:

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Nasal cavity disease | 99.91% | L5 | Hold |
| Thrombotic disease | 99.90% | L4 | Hold |
| Acute laryngopharyngitis | 99.89% | L5 | Hold |
| Papillary conjunctivitis | 99.79% | L5 | Hold |
| Neuralgia | 99.34% | L4 | Research question |
| Glossodynia | 99.26% | L5 | Hold |
| Coccygodynia | 99.22% | L5 | Hold |
| Trigeminal autonomic cephalalgia | 99.21% | L4 | Research question |
| Hypnic headache | 99.17% | L3 | Research question |
| Vein disease | 99.06% | L5 | Hold |

Among these, hypnic headache has the most supportive evidence. Reviews describe caffeine, such as a cup of strong coffee on waking or at bedtime, as a first-line option based on case reports and small case series. There are no randomised trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction, nasal cavity disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are expressed in airway tissues, including the nasal cavity. Their role is still not fully clear. |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preclinical formulation study | Current Drug Delivery | Thermo-sensitive nasal caffeine gel developed to improve cognition after sleep deprivation. It is a delivery-route study, not a nasal disease study. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced lung tumours in rats exposed to a tobacco carcinogen. Not relevant to nasal disease. |

None of these publications addresses a nasal disease outcome in humans.

For the best-supported alternative, hypnic headache:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22072057](https://pubmed.ncbi.nlm.nih.gov/22072057/) | 2012 | Review | Current Treatment Options in Neurology | No placebo-controlled randomised trials exist. Caffeine is the preferred first-line option for acute treatment and prevention, based on case reports and small series. |
| [24942086](https://pubmed.ncbi.nlm.nih.gov/24942086/) | 2014 | Review | Cephalalgia | Review of clinical features, therapeutic options and outcomes in hypnic headache. |
| [25231430](https://pubmed.ncbi.nlm.nih.gov/25231430/) | 2014 | Review | Headache | Overview of hypnic headache as a rare, strictly sleep-related primary headache. |

---

## South Africa Market Information

All 20 registrations are valid single-ingredient registrations, and none is cancelled. SAHPRA indication text was not available in the data compiled for this report. The Essential Medicines List status of caffeine was also not available. The five main registrations are listed below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. X/5.8/383 | Adco-sinal ns | Capsule | Not available |
| Reg. No. 29/5.8/0782 | Sinuend | Tablet | Not available |
| Reg. No. 27/2.8/0574 | Adco-salterpyn | Tablet | Not available |
| Reg. No. 28/2.8/0383 | Tensodol | Tablet | Not available |
| Reg. No. C 810 (OM) | Colcleer (cold + flu) | Tablet | Not available |

The remaining registrations include tablets such as Spectrapain Forte T, Dynapayne, Syndol, Tensolve Tension Headache Tablets, Grippon cold and flu, Sinucon and Flusin, plus Colcleer paediatric syrup.

---

## Safety Considerations

**Contraindications and conditions flagged in the knowledge graph.** These come from drug-disease links in the knowledge graph, not from product label text. They include:
- **Cardiovascular:** hypertension, long QT syndromes, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- **Neurological and psychiatric:** epilepsy, insomnia, anxiety disorder, neurotic disorder, dysthymic disorder
- **Gastrointestinal and hepatic:** gastric and peptic ulcer disease, inflammatory bowel disease, pancreatitis, gallbladder disease, liver disease, liver failure
- **Other:** chronic obstructive pulmonary disease, kidney disease, porphyria, thrombocytopenia, hypothyroidism

**Drug interactions.** The interaction database lists 75 interacting drugs. The 20 reviewed include two **major** interactions, with nasal and topical cocaine. Moderate interactions include alosetron, adenosine, anagrelide, bendamustine, capmatinib, ciprofloxacin, cycloserine, dipyridamole, duloxetine and obeticholic acid. Minor interactions include acetylsalicylic acid, cimetidine, atazanavir and disulfiram.

**Other signals from the literature.**
- Caffeine-related insomnia and medication-overuse headache are noted, especially in older patients.
- Caffeine may reduce cerebral blood flow and interfere with vasodilator stress perfusion imaging.
- Stimulant-related cardiovascular harm has been reported.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings, as these were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for nasal cavity disease is a model output only (L5). There are no clinical trials, and the retrieved literature does not address a nasal disease outcome. The score likely reflects similarity to existing rhinitis and cold indications. Caffeine is already marketed in South Africa, so the practical question is whether a specific, well-defined nasal condition justifies further study.

**To proceed, the following is needed:**
- A specific target condition, since "nasal cavity disease" is too broad to evaluate
- Clinical or mechanistic evidence for caffeine in that condition
- SAHPRA package insert indications, warnings and contraindications, with the Professional Information reviewed
- Detailed mechanism-of-action data from DrugBank
- Safety review for patients with hypertension, arrhythmia, epilepsy, anxiety or insomnia
- Consideration of hypnic headache, the best-supported alternative, as a possible research question
- Caution regarding thrombotic disease, where the direction of effect is unclear and a possible cardiovascular risk signal needs review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

