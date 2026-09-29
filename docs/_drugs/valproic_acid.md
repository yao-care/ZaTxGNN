---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 463
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

Valproic acid is an established antiseizure medicine, and it is marketed in South Africa as extended-release products. The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but the only supporting item is **1 publication**, a Sturge-Weber syndrome case series that is not about a tumour, and there are **no registered clinical trials**. The prediction is best read as a model artefact rather than a real lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. The supplied literature describes valproic acid as an antiseizure drug (epilepsy). |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Valproic acid is known to act as a histone deacetylase (HDAC) inhibitor, and this has drawn preclinical interest in cancer. No data supplied shows this effect in trigeminal nerve tumours.

The only linked paper is a case series on Sturge-Weber syndrome. This is a vascular neurocutaneous disorder, not a neoplasm, so it does not support the predicted indication. The high score most likely reflects graph proximity to other neurological conditions rather than a genuine biological link. On the current evidence, the prediction is not mechanistically supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years at one centre, covering clinical features, course and treatment response. It concerns a vascular disorder, not a tumour, so it is not direct evidence for this prediction. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 45/2.5/0094 | Eprolep CR | Sustained-release tablet (SRT) | Not listed in the data supplied |
| Reg. No. 45/2.5/0412 | Eprolep CR | Sustained-release tablet (SRT) | Not listed in the data supplied |
| Reg. No. 45/2.5/0411 | Navalpro CR | Sustained-release tablet (SRT) | Not listed in the data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials, and the single linked paper is about a non-neoplastic condition. A Hold is appropriate.

Other predicted indications for this drug have stronger support. Visual epilepsy (evidence level L3) is close to an existing use and could be reviewed separately with guardrails. Startle epilepsy and trigeminal neuralgia (both L3) are framed as research questions.

**To proceed, the following is needed:**
- Preclinical or clinical evidence linking valproic acid to trigeminal nerve tumours
- Mechanism of action data
- SAHPRA package insert warnings and contraindications, needed before any safety screening
- The approved indication text for the three registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

