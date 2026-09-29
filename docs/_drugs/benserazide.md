---
layout: default
title: Benserazide
parent: Model Prediction Only (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Benserazide
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

# Benserazide: From Parkinson's Disease Adjunct Therapy to Congenital Hypotrichosis Milia

## One-Sentence Summary

Benserazide is a peripheral AADC (DOPA decarboxylase) inhibitor, marketed in South Africa as a component of Madopar HBS. It is generally used alongside levodopa in Parkinson's disease, but the SAHPRA record provided does not state an approved indication.
The TxGNN model predicts it may be useful for **congenital hypotrichosis milia**, with a high score of 98.4%.
There are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record (generally levodopa co-therapy in Parkinson's disease, from general knowledge, not from the record) |
| Predicted New Indication | Congenital hypotrichosis milia |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from the source record is not available. Benserazide is known as a peripheral aromatic L-amino acid decarboxylase (AADC) inhibitor. It prevents the breakdown of levodopa outside the brain, which is why it is combined with levodopa.

No established link exists between AADC inhibition and hair follicle development in this rare genetic hypotrichosis. The high TxGNN score is a knowledge-graph prediction only. It likely reflects graph proximity to other hair-loss phenotypes rather than a shared biological pathway.

The other top predictions are equally unsupported. Hair-related predictions are hypotrichosis simplex of the scalp, diffuse alopecia areata and alopecia. The alopecia areata prediction has a particularly weak rationale, because that condition is autoimmune (JAK/T-cell-mediated) and AADC inhibition has no documented role in it. Neuroendocrine tumour predictions, such as pheochromocytoma and small intestine cancer, are mechanistically conceivable because AADC is expressed in those tissues. They remain untested.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for congenital hypotrichosis milia.

For the related prediction "alopecia" (rank 4), the only retrieved paper is a title-level commentary, [PMID 34900390](https://pubmed.ncbi.nlm.nih.gov/34900390/) (2021, *Tremor and Other Hyperkinetic Movements*). It describes alopecia areata as an adverse effect of tremor drugs. It has not been verified to contain any benserazide data, and if anything it points to hair loss as a harm, not a benefit.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/5.4.1/0194 | Madopar HBS 100mg/25mg | Capsule (oral) | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: The DDI query returned no results, which is not the same as no interactions. Please check the Professional Information (PI).
- **Migraine signal**: A 1979 clinical observation, [PMID 554794](https://pubmed.ncbi.nlm.nih.gov/554794/), reported typical migraine attacks in all 4 migrainous women given a single 125 mg oral dose of benserazide. This is a small, preliminary report, but it is a caution for any repurposing plan, and it also argues against the headache-related predictions.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supporting literature and no plausible mechanism. The only related safety signal, migraine induction, points the wrong way. Nothing in the data justifies further investment at this stage.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) warnings and contraindications, currently a blocking gap for safety screening
- Mechanism of action data from DrugBank, to test any biological link to hair follicle biology
- Full-text review of the retrieved papers, PMID 34900390 in particular, to confirm relevance
- Evidence of a plausible mechanism connecting AADC inhibition to hair follicle development, or a systematic literature review, before any re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

