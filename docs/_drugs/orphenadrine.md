---
layout: default
title: Orphenadrine
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Orphenadrine: From an Undocumented Original Indication to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Orphenadrine's original approved indication could not be established from the current evidence pack (no SAHPRA registrations, no mechanism-of-action record). The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but this candidate is supported by **0 clinical trials** and **15 publications that are topically unrelated to orphenadrine** (general ophthalmology reviews/case reports with no drug mention) — the evidence pack itself flags this as co-occurrence noise rather than drug-specific signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — orphenadrine has no SAHPRA registrations and no recorded original indication in this evidence pack |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 (model prediction only, no supporting clinical or drug-specific literature) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for orphenadrine is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the literature retrieved for a different candidate indication in this same pack (schizophrenia, rank 5), orphenadrine is known pharmacologically as an antimuscarinic agent historically used to manage parkinsonism and to counteract neuroleptic-induced extrapyramidal symptoms — but this is background context, not a confirmed original indication.

For the rank-1 candidate, retinal dystrophy with or without extraocular anomalies, there is **no mechanistic rationale connecting orphenadrine's known anticholinergic/weak NMDA-antagonist pharmacology to this rare inherited ophthalmic disorder**. All 15 retrieved publications discuss general ophthalmology topics (orbital infection, diplopia, congenital ptosis, lens anomalies, extraocular muscle fibrosis syndromes) and do not mention orphenadrine at all — this is co-occurrence noise from the disease-side vocabulary, not drug-specific evidence. The TxGNN score of 99.29% should therefore be read as a knowledge-graph proximity signal, not as clinical plausibility.

Note for reviewers: a lower-ranked candidate in this same evidence pack (schizophrenia, rank 5, TxGNN score 99.13%) is considerably better grounded — it has 20 literature hits including a Cochrane review and several small RCTs/cohort studies describing orphenadrine's real-world use as an adjunct to antipsychotics for extrapyramidal side effects. That candidate is scored L3/S1 ("Research Question") in the underlying data and may warrant separate evaluation, but is outside the scope of this report's rank-1 candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections/cellulitis staging; no mention of orphenadrine or retinal dystrophy |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Diagnostic approach to diplopia from ocular/neurologic/muscle causes; no drug relevance |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Clinical features of congenital ptosis; no drug relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies; no drug relevance |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome vitreoretinal degeneration description; no drug relevance |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging classification of pediatric orbital/ocular pathologies; no drug relevance |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia; no drug relevance |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis case; no drug relevance |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case; no drug relevance |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case report | Archives of Ophthalmology | Orbital arteriovenous malformation case series; no drug relevance |

None of the retrieved publications mention orphenadrine; all were captured via disease-term overlap only.

## South Africa Market Information

Orphenadrine currently has no SAHPRA registrations on file (Market Status: Not Marketed, 0 licenses recorded).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/SAHPRA warning and contraindication data for this drug is currently a Blocking data gap (DG001) — this must be resolved before any safety-stage evaluation can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (retinal dystrophy with or without extraocular anomalies) has no clinical trials, no drug-specific literature, and no known mechanistic link — the 15 retrieved publications are disease-term co-occurrence noise, not evidence about orphenadrine. Evidence level is L5 (model prediction only), which does not support progression past initial screening.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001 (TFDA/SAHPRA PI warnings and contraindications) before any safety review
- Resolve High-severity data gap DG002 (mechanism of action) to properly assess biological plausibility
- Original/approved indication documentation for orphenadrine (currently absent from this evidence pack)
- If this indication is to be pursued further, drug-specific (not just disease-specific) literature or preclinical mechanistic studies connecting orphenadrine to retinal/ophthalmic pathways
- Separately, consider evaluating the better-evidenced rank-5 candidate (schizophrenia/antipsychotic-adjunct use, L3) as a more promising research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

