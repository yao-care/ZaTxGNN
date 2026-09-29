---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is a long-established anti-seizure medicine. The SAHPRA records supplied do not state an approved indication, but it is generally used for focal and tonic-clonic seizures.
The TxGNN model predicts it may be useful for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records supplied (approved indication text is empty). Generally used for focal and tonic-clonic seizures. |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, phenytoin is a use-dependent blocker of voltage-gated sodium channels. It dampens repetitive neuronal firing, which is why it works in seizures. It has no established antitumour mechanism.

The prediction is probably not a real tumour-related effect. The very high score most likely reflects the drug's closeness, in the model's knowledge graph, to trigeminal neuralgia and seizure nodes. These are neighbours of "trigeminal nerve neoplasm" but are not the same disease. Sodium channel blockade is a credible mechanism for paroxysmal nerve pain, not for shrinking or controlling a nerve tumour.

Because this candidate is a nerve tumour, it is not a plausible use for phenytoin. The related predicted indication **trigeminal neuralgia** (TxGNN rank 9 for this drug, score 99.97%) is biologically much more credible. It also has no supporting trials or literature in this package.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B0884 (ACT 101) | Phenytoin sod | Tablet (oral) | Not stated in the record supplied |
| B1624 (OLD MEDICNE) | Epanutin Ready Mixed Parenteral | Injection | Not stated in the record supplied |

Both oral and injectable routes are registered. Essential Medicines List (EML) status is not included in the data supplied.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data supplied. Phenytoin has a narrow therapeutic index. Other literature retrieved for this drug in the pack describes paradoxical seizures, blood dyscrasias and thrombocytopenia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it, and phenytoin has no known antitumour mechanism. The high TxGNN score most likely reflects graph proximity to trigeminal neuralgia and seizure nodes.

**To proceed, the following is needed:**
- Retrieve the SAHPRA package insert warnings and contraindications (a blocking data gap that prevents safety screening).
- Obtain mechanism of action data from DrugBank.
- Run a targeted literature and trial search for phenytoin in trigeminal nerve tumours and, as the more credible candidate, trigeminal neuralgia.
- Confirm whether the prediction label reflects a true neoplasm or a neuralgia-related graph artifact before any further evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

