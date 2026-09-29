---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Lamotrigine: From Epilepsy and Bipolar Disorder to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is an anticonvulsant used for seizure and bipolar mood disorders. The TxGNN model predicts it may help in **trigeminal neuralgia**, a severe facial nerve pain condition, and the evidence is small but direct, with **4 registered clinical trials** (3 testing lamotrigine) and **about 20 publications**. The model's top-ranked prediction, trigeminal nerve *neoplasm*, was set aside as a likely ontology artifact (see below).

> **Note on prediction selection:** The highest-scoring prediction (rank 1, "trigeminal nerve neoplasm", 99.97%) has no antitumour rationale. Its only retrieved papers are about trigeminal *neuralgia*, so the score most likely reflects graph proximity to that condition. This report therefore focuses on rank 2, trigeminal neuralgia, the first prediction with clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy and bipolar disorder (general drug knowledge; the SAHPRA registry extract supplied gives no indication text) |
| Predicted New Indication | Trigeminal neuralgia (rank 2; rank 1, trigeminal nerve neoplasm, excluded as a likely artifact) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 (one completed Phase 2/3 trial, n=21) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Lamotrigine is generally described as a use-dependent voltage-gated sodium channel blocker that also reduces glutamate release.

Trigeminal neuralgia is most often caused by vascular compression of the trigeminal nerve root, which leads to focal demyelination and abnormal, high-frequency nerve discharges. Sodium channel blockade suppresses this kind of discharge. This is the same mechanism as carbamazepine and oxcarbazepine, the established first-line drugs. Reduced glutamate release may add to the effect.

Lamotrigine appears in the trigeminal neuralgia literature as a second-line or add-on option. The direct trials are small, so this is a plausible, partly supported idea rather than a proven one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Lamotrigine vs carbamazepine in trigeminal neuralgia. This is the most direct evidence, but the sample is small. |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Not specified | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine in trigeminal neuralgia. Design is good, but the sample is small. |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | Not specified | Completed | 6 | fMRI study of lamotrigine in neuropathic facial pain. Exploratory, with no efficacy conclusion. |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Carbamazepine vs oxcarbazepine. Lamotrigine is not studied; included as context on first-line care. |

No SANCTR or PACTR registrations were identified in the data supplied.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative study (type not classified) | J Chin Med Assoc | Compared lamotrigine with carbamazepine for efficacy and side effects in trigeminal neuralgia. |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology recommendations for managing trigeminal neuralgia. |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic review | Biomedicines | Umbrella review of drug treatments for trigeminal neuralgia, covering efficacy and side effects. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Carbamazepine and oxcarbazepine work but often cause dose-limiting side effects. Newer anticonvulsants may be useful adjuncts. |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | Practical guide to diagnosis and to medical and surgical treatment. |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Overview from pathophysiology to drug treatment. |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Current and innovative drug options for typical and atypical trigeminal neuralgia. |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences (Riyadh) | Drug and surgical options for trigeminal neuralgia. |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case report | Mult Scler Relat Disord | Refractory trigeminal neuralgia in a patient with multiple sclerosis treated with pregabalin plus lamotrigine. |
| [25299564](https://pubmed.ncbi.nlm.nih.gov/25299564/) | 2014 | Review | BMJ Clin Evid | Evidence summary on trigeminal neuralgia treatment. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/2.5/0407 | Lamictin p2 | Effervescent tablet (oral) | Not stated in the registry extract |
| Reg. No. A38/2.5/0567 | Lamorola 25 | Tablet (oral) | Not stated in the registry extract |
| Reg. No. A39/2.5/0473 | Sandoz Lamotrigine 25 | Tablet (oral) | Not stated in the registry extract |

Essential Medicines List (EML) status is not stated in the data supplied.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug-interaction query returned no results. This does not mean there are none. The case for use in trigeminal neuralgia specifically flags the following guardrails: slow titration because of rash and Stevens-Johnson syndrome risk, and checking interactions with valproate and estrogen-containing contraceptives.

---

## Other Predictions (Lower Priority)

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Trigeminal nerve neoplasm | 99.97% | L5 | Likely artifact. No antitumour mechanism, and no relevant studies. Hold. |
| Startle epilepsy / audiogenic seizures | 99.38% | L4 | Small case reports (3 of 6 patients improved greatly in one series) and animal data. Research question. |
| Reading seizures | 99.30% | L4 | Only indirect evidence. Lamotrigine can worsen myoclonic seizures in some generalised epilepsies. Research question. |
| Thinking, micturition-induced, eating, orgasm-induced seizures | 99.38% | L4–L5 | No disease-specific evidence. Identical scores suggest propagation from a parent epilepsy node. Hold or research question. |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (trigeminal neuralgia only)

**Rationale:**
- Three small completed trials, including one Phase 2/3 comparison with carbamazepine, support the sodium-channel mechanism.
- Lamotrigine is marketed in South Africa and its safety profile is well known from epilepsy use.
- The samples are very small (n=6–21), so lamotrigine should be used only after or alongside first-line carbamazepine or oxcarbazepine.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) and confirmation of EML status. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Larger confirmatory randomised trials before any stronger recommendation.
- Local prescribing guidance covering titration, rash monitoring and interactions with valproate and estrogen-containing contraceptives.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

