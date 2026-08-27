---
layout: default
title: Folic Acid
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Folic Acid: From Vitamin B9 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

> Folic acid (vitamin B9) is a water-soluble vitamin classically used to treat folate deficiency and megaloblastic anaemia; detailed original-indication and mechanism-of-action data were not available in the current evidence pack.
> The TxGNN model predicts a possible link to **Biotin Metabolic Disease** with a very high score (99.49%),
> but the supporting evidence — **13 clinical trials** and **20 publications** — is largely indirect, and the model's own rationale flags this as a likely false-positive driven by knowledge-graph clustering of "vitamin/coenzyme" entities rather than a genuine drug–disease mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the current evidence pack (drug is not SAHPRA-registered; generally used for folate/vitamin B9 deficiency and megaloblastic anaemia) |
| Predicted New Indication | Biotin Metabolic Disease (e.g., biotinidase deficiency and related inborn errors) |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 (mechanistic/preclinical reasoning only — no direct trial evidence) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, folic acid is a water-soluble B-vitamin that serves as a coenzyme for one-carbon (methyl-group) transfer reactions, essential for nucleotide synthesis and homocysteine metabolism. Its established clinical role is treating folate deficiency and related megaloblastic anaemia.

Biotin metabolic disease (e.g., biotinidase deficiency, holocarboxylase synthetase deficiency) is a distinct inherited disorder of a **different coenzyme system** — biotin acts as a cofactor for carboxylase enzymes, not for one-carbon/folate metabolism. There is no established biochemical pathway linking folic acid supplementation to correction of biotin-dependent enzyme deficiencies.

The model's own repurposing rationale explicitly cautions that this high score likely reflects the knowledge graph clustering folic acid with other "vitamin/coenzyme metabolite" nodes, rather than capturing a specific, validated mechanistic relationship. The standard and accepted treatment for biotin metabolic disease is biotin itself, not folic acid. This mechanistic gap is the primary reason for a cautious (Hold) recommendation despite the high prediction score.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | RCT of Q10 ubiquinol + multivitamin B/E in autism (idiopathic and Phelan-McDermid syndrome); metabolic support, not specific to folic acid or biotin disease |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Pilot comparing natural vs synthetic vitamin B-complex bioavailability; small study, not disease-specific |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6824 | Newborn genomic screening for 126 treatable genetic diseases; screening context only, no treatment data |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient palliative intervention in congestive heart failure; unrelated indication |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | N/A | Active, not recruiting | 20 | Gut microbiome and prebiotic study for alcohol addiction recovery; unrelated to biotin metabolic disease |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin/mineral supplementation for diabetic neuropathy/nephropathy; unrelated indication |
| [NCT04586348](https://clinicaltrials.gov/study/NCT04586348) | Phase 4 | Active, not recruiting | 794 | Prenatal iodine supplementation and neurodevelopment; unrelated to folic acid or biotin disease |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | Transdermal vitamin absorption post-bariatric surgery; unrelated indication |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Targeted nutritional intervention for oxidative stress in autism; unrelated indication |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completed | 202 | Multivitamin/mineral and fatty acid supplementation on impulsivity/aggression; unrelated indication |

**None of the identified trials directly evaluate folic acid for treatment of biotin metabolic disease.** All are broader micronutrient/vitamin studies in unrelated populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Review | Movement Disorders | Reviews movement disorders in treatable inborn errors of metabolism, including biotin-responsive conditions |
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders of cobalamin, folate, biotin, B1 and E — discusses folate and biotin as distinct pathways |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Reviews vitamin B12 deficiency and nervous system effects, referencing folate/biotin as separate cofactors |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Reviews relationship between vitamins (including biotin) and type 2 diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Reviews vitamins, including biotin, in type 2 diabetes mellitus |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | Reviews B-vitamin roles in cellular metabolism and dermatology |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterol Clin North Am | Reviews vitamin/mineral deficiencies in inflammatory bowel disease |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Reviews vitamins in metabolic diseases generally, including vitamin-dependent syndromes |
| [36197290](https://pubmed.ncbi.nlm.nih.gov/36197290/) | 2022 | Cohort | Microbiology Spectrum | Gut microbiota and metabolomics changes in seafarers; not disease-specific |
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Other | J Chem Technol Biotechnol | Reviews industrial production of vitamins/coenzymes including biotin and folic acid; not clinical |

**The literature consists mainly of general reviews on B-vitamin metabolism; no publication directly studies folic acid as a treatment for biotin metabolic disease.**

---

## South Africa Market Information

Folic acid is **not currently registered with SAHPRA** under this evidence pack (0 licenses, market status: Not Marketed). No product-level registration details are available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: This evidence pack flags a Blocking data gap (DG001 — SAHPRA/TFDA-equivalent PI warnings and contraindications) that must be resolved before any formal safety (S1) evaluation can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the model's own mechanistic rationale, the absence of any trial or publication directly testing folic acid in biotin metabolic disease, and the biochemical distinction between folate and biotin coenzyme pathways together indicate this is likely a knowledge-graph clustering artifact rather than a genuine repurposing signal. The drug is also not currently marketed in South Africa.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications, DDI) — currently a Blocking data gap
- Confirmed mechanism of action data for folic acid (DrugBank or equivalent)
- Dedicated preclinical or clinical evidence directly testing folic acid's effect on biotin-dependent carboxylase activity or biotinidase/holocarboxylase synthetase deficiency
- Clarification of registration pathway if market entry to South Africa is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

