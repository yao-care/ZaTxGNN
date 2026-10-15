---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Valproic acid is a broad-spectrum antiseizure medicine, originally used for epilepsy, manic episodes of bipolar disorder and absence epilepsy.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **no registered clinical trials** and only **1 publication**, a 1997 case series on Sturge-Weber syndrome that does not address this condition.
Among the other predictions, **visual epilepsy** has the strongest support, though it is better viewed as an extension of the existing epilepsy indication than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy; manic bipolar affective disorder; absence epilepsy (the SAHPRA registrations in the data have no indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

**Overview of the top 10 predictions**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Trigeminal nerve neoplasm | 99.97% | L5 | Hold |
| 2 | Visual epilepsy | 99.88% | L1 | Proceed with Guardrails |
| 3 | Trigeminal neuralgia | 99.83% | L4 | Research question |
| 4 | Eating seizures | 99.81% | L4 | Research question |
| 5 | Audiogenic seizures | 99.81% | L4 | Hold |
| 6 | Orgasm-induced seizures | 99.81% | L5 | Hold |
| 7 | Micturition-induced seizures | 99.81% | L4 | Hold |
| 8 | Thinking seizures | 99.81% | L4 | Hold |
| 9 | Startle epilepsy | 99.81% | L4 | Research question |
| 10 | Reading seizures | 99.79% | L4 | Research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Published literature describes valproic acid as acting through several mechanisms: enhancing GABAergic over glutamatergic transmission, blocking sodium channels and modulating T-type calcium channels. It is also a histone deacetylase inhibitor, which is a theoretical antitumour mechanism.

**Trigeminal nerve neoplasm (rank 1).** The high score is not backed by evidence. The only linked paper concerns Sturge-Weber syndrome, a neurocutaneous vascular disorder rather than a nerve tumour. Valproic acid may help control seizures in that syndrome, but this does not support antitumour activity. The histone deacetylase mechanism has no supporting data for this condition. The prediction is best treated as a model artefact until proven otherwise.

**Visual epilepsy (rank 2).** This prediction is mechanistically coherent. Photosensitive and reflex epilepsies fall within the generalised epilepsy syndromes, where valproate is a standard therapy. This is an extension within the existing epilepsy indication rather than genuine repurposing.

**Trigeminal neuralgia (rank 3).** Sodium channel blockade and GABAergic enhancement could plausibly reduce paroxysmal neuropathic pain. Valproate appears only in general reviews of anticonvulsants for this condition. Carbamazepine and oxcarbazepine are established first-line drugs, so valproate would at most be a later-line option.

**Other reflex and stimulus-induced seizures (ranks 4-10).** These predictions rest on shared seizure biology. The evidence is mostly case reports, animal models or non-specific reviews. One prediction (orgasm-induced seizures) has no literature at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications. No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

**Trigeminal nerve neoplasm (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | 14 cases of Sturge-Weber syndrome reviewed over 25 years. Not about trigeminal nerve tumours, so there is no direct support. |

**Visual epilepsy (rank 2), the best-supported prediction**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20200383](https://pubmed.ncbi.nlm.nih.gov/20200383/) | 2010 | RCT | N Engl J Med | Ethosuximide, valproic acid and lamotrigine compared as initial treatment in childhood absence epilepsy |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Curr Neuropharmacol | Valproic acid remains one of the most efficient antiepileptic drugs. Mechanisms range from ion channel regulation to GABAergic facilitation. |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arq Neuropsiquiatr | Review of status epilepticus diagnosis, monitoring and treatment |
| [39899098](https://pubmed.ncbi.nlm.nih.gov/39899098/) | 2025 | Review | Continuum | Evidence on first seizures, cluster seizures and status epilepticus |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Review | Future Oncol | Levetiracetam and valproic acid in glioma: antiseizure and potential antineoplastic effects |

**Trigeminal neuralgia (rank 3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1774173](https://pubmed.ncbi.nlm.nih.gov/1774173/) | 1991 | Review | Headache | Lists valproic acid among anticonvulsants reported to be efficacious in trigeminal neuralgia, alongside carbamazepine, phenytoin and clonazepam |
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs outside epilepsy. Evidence is mostly case series and small trials needing confirmation. |
| [11129121](https://pubmed.ncbi.nlm.nih.gov/11129121/) | 2000 | Review | Drugs | Anticonvulsants for neuropathic pain: mechanisms and place in therapy |

**Startle epilepsy (rank 9)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29262725](https://pubmed.ncbi.nlm.nih.gov/29262725/) | 2018 | Clinical study | Clin EEG Neurosci | Examined the effect of valproate on the auditory startle reflex in patients with epilepsy |
| [2496695](https://pubmed.ncbi.nlm.nih.gov/2496695/) | 1989 | Case report | Pediatr Neurol | Hyperekplexia (a distinct glycinergic disorder) resolved with valproic acid in one adolescent |

**Audiogenic seizures (rank 5)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23872084](https://pubmed.ncbi.nlm.nih.gov/23872084/) | 2013 | Animal study | Epilepsy Behav | Valproic acid tested in the GASH:Sal audiogenic seizure hamster. This is preclinical evidence only. |

For eating seizures, micturition-induced seizures, thinking seizures and reading seizures, the retrieved papers are case reports, general epilepsy reviews or valproate safety papers with no direct efficacy data. For orgasm-induced seizures, currently no related literature is available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/2.5/0094 | Eprolep CR | Sustained-release tablet (Srt) | Indication text not available in the data compiled for this report |
| Reg. No. 45/2.5/0412 | Eprolep CR | Sustained-release tablet (Srt) | Indication text not available in the data compiled for this report |
| Reg. No. 45/2.5/0411 | Navalpro CR | Sustained-release tablet (Srt) | Indication text not available in the data compiled for this report |

All three registrations are valid single-ingredient products, and none are cancelled. The data compiled for this report do not state Essential Medicines List (EML) status, so this should be checked separately.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph (not label text)**

The TxGNN knowledge graph links valproic acid to the following conditions as contraindications. These must be verified against the SAHPRA-approved Professional Information:
- Liver disease, pancreatitis, gallbladder disease
- Kidney disease, pyoureter
- Hematologic disease, thrombocytopenia
- Urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia)
- Inherited porphyria and other porphyrin metabolism diseases
- Cognitive disorder
- Anxiety disorder, neurotic disorder, dysthymic disorder

**Drug interactions**

The interaction screen returned 100 interactions. The most notable among those listed:
- **Major:** glycerol phenylbutyrate
- **Moderate:** bupropion, morphine (including liposomal), acetylsalicylic acid, clarithromycin, difenoxin, diphenoxylate, activated charcoal, dronabinol, nabilone, metoclopramide
- **Minor:** cimetidine, esomeprazole, and several antacids (magnesium oxide, aluminium hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide)

The literature also flags a clinically important interaction between valproic acid and carbapenem antibiotics (PMID 20408498).

**Other guardrails noted in the evidence review**
- Teratogenicity and neurodevelopmental risk in women of childbearing potential
- Hepatotoxicity, pancreatitis and hyperammonaemia

The SAHPRA package insert warnings and contraindications have not been retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, trigeminal nerve neoplasm)

**Rationale:**
- The highest TxGNN score does not correspond to real evidence. The single linked paper is unrelated to nerve tumours, and there are no trials.
- Visual epilepsy is the only prediction with strong support (L1, Proceed with Guardrails), but it largely falls within valproate's existing epilepsy use.
- Trigeminal neuralgia, eating seizures, startle epilepsy and reading seizures are research questions only. Audiogenic, orgasm-induced, micturition-induced and thinking seizures should be held.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Indication text for the three SAHPRA registrations, and EML status
- For trigeminal nerve neoplasm: preclinical or clinical evidence of antitumour activity in this tumour type, otherwise no further work
- For visual epilepsy: confirmation that photosensitive and reflex epilepsy are covered by the registered epilepsy indication, plus a pregnancy prevention and monitoring plan for women of childbearing potential
- For trigeminal neuralgia: a comparison against carbamazepine and oxcarbazepine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

