---
layout: default
title: Bimatoprost
parent: Model Prediction Only (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Glaucoma to Malformation Syndrome with Odontal and/or Periodontal Component

## One-Sentence Summary

Bimatoprost is a prostamide (prostaglandin F2-alpha analogue) eye drop, registered in South Africa as ophthalmic drops. The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**, with a very high score (99.997%). However, there are **0 clinical trials** and **0 publications** that mention bimatoprost for this condition, so the prediction is unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (general pharmacology; the SAHPRA indication text is not in the data provided) |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, bimatoprost is a prostamide/prostaglandin F2-alpha analogue that lowers intraocular pressure. Its known effects on the hair cycle (prolonging anagen, stimulating follicles) are the basis of its eyelash use.

We could not identify a plausible link between this pharmacology and a malformation syndrome involving the teeth or periodontium. The 20 papers retrieved for this prediction are general periodontitis literature: guidelines, reviews, and diabetes-periodontitis links. None mentions bimatoprost. The high TxGNN score is a network-proximity output, not evidence of benefit. It should be treated as a likely artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were provided.

## Literature Evidence

None of these papers studies bimatoprost. They are general periodontal literature, retrieved by the disease term only, and their relevance is still marked "pending".

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guideline | J Clin Periodontol | EFP clinical practice guideline for treating stage IV periodontitis |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic review | Cochrane Database Syst Rev | Treating periodontitis for glycaemic control in people with diabetes |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Systematic review | Cochrane Database Syst Rev | Supportive periodontal therapy for maintaining dentition after periodontitis treatment |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | Two-way relationship between periodontitis and diabetes |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontol 2000 | Complications and treatment errors in regenerative periodontal surgery |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontol 2000 | Sleep disorders as an emerging risk factor for periodontal health |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dent Res | Role of gingival fibroblasts in periodontitis pathogenesis |
| [12010523](https://pubmed.ncbi.nlm.nih.gov/12010523/) | 2002 | Review | J Clin Periodontol | Evidence-based view of scaling and root planing |
| [29193334](https://pubmed.ncbi.nlm.nih.gov/29193334/) | 2018 | Review | Periodontol 2000 | Peri-implant vs periodontal soft tissues in health and disease |
| [9495612](https://pubmed.ncbi.nlm.nih.gov/9495612/) | 1998 | Observational microbiology study | J Clin Periodontol | Microbial complexes in subgingival plaque |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 56/15.4/0781 | Glauptico | Drops |
| Reg. No. 54/15.4/0389.388 | Timpromat | Drops |

The approved indication text and Essential Medicines List status were not available in the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is L5 (model score only), with no trials, no bimatoprost-specific literature, and no mechanistic link. Bimatoprost is a hair-growth-promoting eye drop, and nothing in the data connects it to a periodontal malformation syndrome.

**Better-supported prediction in the same pack:** The pack ranks **alopecia** 8th (score 99.993%, evidence level L2). It has 11 registered trials, including completed Phase 2 studies in androgenetic alopecia:
- [NCT01904721](https://clinicaltrials.gov/study/NCT01904721): men, n=244
- [NCT01325337](https://clinicaltrials.gov/study/NCT01325337): men, n=307
- [NCT01325350](https://clinicaltrials.gov/study/NCT01325350): women, n=306
- [NCT02170662](https://clinicaltrials.gov/study/NCT02170662): androgen-dependent scalp follicles, n=33

Efficacy outcomes are not in the pack, and no Phase 3 evidence is listed. I recommend re-running this report with alopecia as the primary indication. The two South African registrations are ophthalmic drops, so any scalp use would be off-label and would need a suitable formulation.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications, approved indication text)
- Mechanism of action data from DrugBank
- Outcome data from the alopecia Phase 2 trials
- For the periodontal prediction, any biological rationale at all, before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

