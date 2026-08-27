---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Phenytoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Phenytoin: From Epilepsy to Audiogenic Seizures

## One-Sentence Summary

> Phenytoin is a voltage-gated sodium channel blocker originally used to control generalized tonic-clonic and partial seizures in epilepsy.
> The TxGNN model predicts it may also be effective for **Audiogenic Seizures** (a reflex epilepsy subtype triggered by sound),
> with **0 clinical trials** but **19 supporting publications** (mostly preclinical/animal pharmacology studies plus one clinical case report) currently backing this direction.

**Note on candidate selection:** TxGNN's top-ranked prediction ("trigeminal nerve neoplasm") was excluded from this report. The evidence pack itself flags it as a likely knowledge-graph artifact — a probable confusion between "trigeminal neuralgia" and "trigeminal nerve neoplasm" — with no mechanistic, trial, or literature support (Evidence Level L5, recommendation Hold). Among the remaining candidates, **audiogenic seizures** has by far the strongest and most direct body of evidence, so it is presented here instead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic and partial seizures) — not present in the structured `taiwan_regulatory` data, based on well-established pharmacology referenced throughout the evidence pack |
| Predicted New Indication | Audiogenic Seizures |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (preclinical/mechanistic studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for phenytoin was not returned from DrugBank in this evidence pack (`original_moa: [Data Gap]`). However, the repurposing rationale fields consistently identify phenytoin as a **voltage-gated sodium channel blocker**, the same mechanism underlying its established anticonvulsant effect in epilepsy.

Audiogenic seizures are a reflex epilepsy subtype in which sound stimuli trigger abnormal, excessive cortical and subcortical (periaqueductal gray / pontine reticular formation) electrical activity. Because phenytoin's sodium-channel-blocking action raises the seizure threshold broadly, rather than acting on a disease-specific target, it is mechanistically plausible that this effect extends to reflex seizure subtypes such as audiogenic seizures — not just to spontaneous epilepsy.

This is not purely theoretical: multiple animal-model studies (e.g. PMID 10719079, 12948620, 7211184) directly test phenytoin's anticonvulsant activity against audiogenic seizures in genetically epilepsy-prone rodents (GEPR, DBA/2 mice), and a human case report (PMID 21561835) describes phenytoin used successfully for a different reflex seizure subtype (micturition/defecation-induced seizures), supporting cross-subtype extrapolation of phenytoin's efficacy within the broader reflex epilepsy category.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21561835](https://pubmed.ncbi.nlm.nih.gov/21561835/) | 2011 | Case Report | Epileptic Disorders | Reflex seizures induced by micturition and defecation successfully treated with clobazam and phenytoin — clinical evidence of phenytoin efficacy in a related reflex-epilepsy subtype |
| [10719079](https://pubmed.ncbi.nlm.nih.gov/10719079/) | 2000 | Animal Study | Brain Research | Phenytoin administration alters pontine reticular formation and periaqueductal gray neuronal firing in genetically epilepsy-prone rats, directly linked to suppression of audiogenic seizure behavior |
| [12948620](https://pubmed.ncbi.nlm.nih.gov/12948620/) | 2003 | Animal Study | Epilepsy Research | A static magnetic field modulates audiogenic seizure severity and the anticonvulsant effects of phenytoin in DBA/2 mice |
| [7211184](https://pubmed.ncbi.nlm.nih.gov/7211184/) | 1981 | Animal Study | Acta Neurologica Scandinavica | Withdrawal from long-term phenytoin (diphenylhydantoin) treatment increases susceptibility to audiogenic and electroshock-induced seizures in rats |
| [9592113](https://pubmed.ncbi.nlm.nih.gov/9592113/) | 1998 | Animal Study | J Neuroscience | Magnesium-deficiency-dependent audiogenic seizure model used for discriminatory anticonvulsant drug screening |
| [22107891](https://pubmed.ncbi.nlm.nih.gov/22107891/) | 2012 | Animal Study | Pharmacological Research | ACE inhibitors potentiate the anticonvulsant activity of antiepileptic drugs, including phenytoin, against audiogenic seizures in DBA/2 mice |
| [27663280](https://pubmed.ncbi.nlm.nih.gov/27663280/) | 2016 | Animal Study | European J Pharmacology | Cannabinoid receptor agonists modulate the anticonvulsant activity of AEDs, including phenytoin, against audiogenic seizures in DBA/2 mice |
| [11284448](https://pubmed.ncbi.nlm.nih.gov/11284448/) | 2001 | Animal Study | Naunyn-Schmiedeberg's Arch Pharmacol | Retigabine potentiates the anticonvulsant activity of AEDs, including phenytoin, against audiogenic seizures in DBA/2 mice |
| [10863138](https://pubmed.ncbi.nlm.nih.gov/10863138/) | 2000 | Animal Study | Epilepsy Research | D-cycloserine potentiates the anticonvulsant activity of AEDs, including phenytoin, against audiogenic seizures in DBA/2 mice |
| [3418335](https://pubmed.ncbi.nlm.nih.gov/3418335/) | 1988 | Animal Study | J Neural Transmission | Clinical, pharmacological, and EEG characterization of the audiogenic seizure model in Wistar rats, foundational to subsequent anticonvulsant screening studies |

---

## South Africa Market Information

Phenytoin has no SAHPRA registrations recorded in this evidence pack (`total_licenses: 0`, market status: Not Marketed). No product-level registration or Essential Medicines List data is available to report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for audiogenic seizures is currently limited to animal pharmacology studies (L4) plus one human case report for a different reflex-epilepsy subtype; there are no clinical trials, and phenytoin has no current SAHPRA registration in South Africa, so there is no regulatory pathway to act on immediately.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent professional information (warnings, contraindications) — currently a blocking data gap (DG001)
- Formal DrugBank-sourced mechanism-of-action data (DG002)
- A feasibility assessment for a Phase 1/2 proof-of-concept trial in audiogenic or other reflex epilepsy subtypes
- Confirmation of any existing SAHPRA registration pathway, since phenytoin is currently not marketed in South Africa under this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

