---
layout: default
title: Cocaine
parent: Model Prediction Only (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Cocaine
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

# Cocaine: From Local Anaesthetic Use to Cauda Equina Syndrome

## One-Sentence Summary

Cocaine is a local anaesthetic and sympathomimetic agent, and the registered product in the dataset is a liquid toothache preparation.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are **no clinical trials** and only **1 publication** (a 2019 case report of the disease itself, not of cocaine treatment).
The high graph score is not supported by any evidence of benefit, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anaesthesia (drug class use; the registration carries no approved indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 (see the source caveat in the market section) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cocaine is known to act as a local anaesthetic and a sympathomimetic, but this pack has no formal MOA record.

Cauda equina syndrome is caused by compression of the lumbosacral nerve roots. It presents with urinary retention or incontinence, faecal incontinence, saddle anaesthesia and lower-limb weakness. Treatment is urgent surgical decompression.

Cocaine's anaesthetic and sympathomimetic actions do not address this compressive pathology. The high score appears to be a knowledge-graph artefact, and the only retrieved article is a case report of the disease that does not involve cocaine treatment. Mechanistic support is currently absent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31528422](https://pubmed.ncbi.nlm.nih.gov/31528422/) | 2019 | Case report | Surgical Neurology International | Distal cauda equina syndrome from lumbosacral disc pathology, with a literature review. It describes the disease and its diagnostic difficulty and reports no cocaine therapy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2815 | Toothache Essence (Dozen) | Liquid | Not stated in the record |

**Source caveat:** The evidence pack lists TFDA as its regulatory input, and the number "G2815" does not follow the usual SAHPRA "Reg. No." format. Confirm on the SAHPRA register that this product is registered in South Africa before relying on the "Marketed" status or the count of 1. Essential Medicines List status is not available in the pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points from the retrieved material apply regardless of indication:
- The literature on cocaine is dominated by harm, including mucosal necrosis, airway injury and cardiovascular effects.
- Cocaine is a controlled substance with abuse liability.

No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no supportive literature, and no plausible mechanism for a compressive neurological condition. Cocaine's abuse liability and safety profile weigh further against repurposing.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Verification that registration G2815 exists on the SAHPRA register
- Preclinical or clinical evidence of benefit in cauda equina syndrome, which is currently absent

**Note on other predictions:** None of the other nine predicted indications (including rhinitis, anaphylaxis and pharyngitis) shows evidence of therapeutic benefit either. All are recommended Hold, and the retrieved literature is mostly case reports of cocaine-related harm. One of them, "obsolete neurogenic bladder", is an obsolete ontology term and needs mapping review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

