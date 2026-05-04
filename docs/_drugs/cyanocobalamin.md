---
layout: default
title: Cyanocobalamin
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Supplementation to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (vitamin B12) is an essential micronutrient used to treat vitamin B12 deficiency and pernicious anaemia. The TxGNN model predicts it may be effective for **Biotin Metabolic Disease**, but the evidence is weak — all **15 clinical trials** retrieved are only tangentially related (Grade C relevance), and the **20 publications** discuss general B-vitamin metabolism rather than direct therapeutic evidence. This prediction likely reflects pathway proximity in the knowledge graph rather than genuine therapeutic potential.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia (no SAHPRA registrations on file) |
| Predicted New Indication | Biotin Metabolic Disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 — Model prediction only, no direct clinical studies |
| South Africa Market Status | Not registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, cyanocobalamin (vitamin B12) is a water-soluble vitamin that serves as a cofactor for two key enzymes: methionine synthase (which converts homocysteine to methionine) and methylmalonyl-CoA mutase (which converts methylmalonyl-CoA to succinyl-CoA in the propionate metabolism pathway).

The mechanistic link to biotin metabolic disease lies in the **propionate metabolism pathway**: biotin-dependent propionyl-CoA carboxylase acts upstream (converting propionyl-CoA to methylmalonyl-CoA), while B12-dependent methylmalonyl-CoA mutase acts immediately downstream (converting methylmalonyl-CoA to succinyl-CoA). Both vitamins are essential for sequential steps in the same metabolic cascade. However, this is a **sequential dependency, not functional redundancy** — B12 cannot compensate for the loss of biotin-dependent carboxylase function. A patient with biotinidase deficiency or holocarboxylase synthetase deficiency requires biotin itself, not B12.

The high TxGNN score (99.60%) most likely reflects the **topological proximity** of cyanocobalamin and biotin metabolic disease nodes in the knowledge graph, owing to shared pathway annotations, co-occurrence in metabolic disease literature, and overlapping patient populations (e.g., organic acidaemias). This does not translate to therapeutic substitutability. The score should therefore be interpreted with considerable caution.

## Clinical Trial Evidence

All 15 retrieved clinical trials received a **Grade C relevance rating** — none directly test cyanocobalamin as a treatment for biotin metabolic disease. The most pathway-relevant trials are listed below:

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Carglumic acid (Carbaglu) in propionic acidaemia and methylmalonic acidaemia — related metabolic pathway but evaluates a different drug |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Universal genomic newborn screening for 126 treatable genetic diseases including inborn errors of metabolism — screening study, not therapeutic intervention |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Terminated | 5 | Fibre and biotin supplementation to improve gut microbiota post-bariatric surgery — terminated early with only 5 participants enrolled |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Enrolling by invitation | 30,000 | Early Check newborn screening programme for rare conditions — epidemiological, not interventional |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Metabolic support therapy (Q10 + vitamins B and E) in autism — status unknown, different indication |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamins and minerals for diabetic neuropathy/nephropathy — different indication entirely |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Nutritional intervention targeting oxidative stress in autism — tangential metabolic overlap only |

**Summary:** No clinical trial directly evaluates cyanocobalamin for the treatment of biotin metabolic disease. The retrieved trials involve multi-vitamin supplementation in unrelated conditions or screening programmes.

## Literature Evidence

Of 20 publications retrieved, none report clinical evidence of cyanocobalamin treating biotin metabolic disease. The most relevant publications discussing the shared metabolic pathways are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Comprehensive review of vitamin-responsive disorders including cobalamin, folate, and biotin — describes distinct inborn errors requiring specific cofactors, not interchangeability |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | B12 deficiency and the nervous system — notes B12 role in succinyl-CoA synthesis from methylmalonyl-CoA and biotin, but focuses on B12-specific neuronal mechanisms |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Observational | Pediatric Research | In vivo propionate metabolism in patients with propionic acidaemia, methylmalonic acidaemia, and multiple carboxylase deficiency — demonstrates distinct biochemical defects requiring specific cofactors |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Vitamins in metabolic diseases — reviews vitamin malabsorption, errors in vitamin metabolism, and vitamin-dependent syndromes; each vitamin treats its own dependent pathway |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatr Clin North Am | Megavitamin-responsive aminoacidopathies — B-complex cofactors activate specific apoenzymes; therapeutic trials are specific to each vitamin |
| [7015958](https://pubmed.ncbi.nlm.nih.gov/7015958/) | 1980 | Review | Ann NY Acad Sci | Interactions of B-complex vitamins in metabolic and catabolic reactions — describes interdependencies but not therapeutic substitutability |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Adv Clin Chem | Vitamin-responsive inborn errors of metabolism — catalogues distinct vitamin-responsive conditions |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Vitamins and type 2 diabetes — discusses biotin and B12 roles separately in glucose metabolism |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterol Clin North Am | Vitamins and minerals in inflammatory bowel disease — discusses micronutrient deficiencies in IBD, not biotin metabolic disease |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Observational | J Endocrinol | B12 deficiency induces glucose intolerance in rats — preclinical animal study unrelated to biotin metabolic disease |

**Summary:** The literature consistently describes cobalamin and biotin as cofactors for **distinct enzymes in a shared pathway**. No publication supports the use of cyanocobalamin as a treatment for biotin metabolic disease.

## South Africa Market Information

Cyanocobalamin does not currently have any SAHPRA registrations reflected in this evidence pack. However, cyanocobalamin products (vitamin B12 injections and oral supplements) are widely available internationally. Healthcare professionals should consult the SAHPRA database directly for the most current registration status of cyanocobalamin-containing products in South Africa.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> **Note:** Cyanocobalamin is generally well-tolerated as a water-soluble vitamin. Known safety considerations from international references include rare hypersensitivity reactions and the potential for polycythaemia vera exacerbation. However, the formal SAHPRA PI should be consulted for the authoritative safety profile applicable in South Africa.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.60%), but this almost certainly reflects **topological proximity in the knowledge graph** rather than genuine therapeutic potential. Cyanocobalamin and biotin operate on sequential but distinct enzymatic steps in the propionate pathway — B12 cannot substitute for biotin function. All 15 clinical trials are Grade C relevance, and none of the 20 publications support this repurposing hypothesis. The evidence level is **L5 (model prediction only)**, and the mechanistic rationale argues *against* rather than for this indication.

**To proceed, the following would be needed:**
- Preclinical evidence demonstrating that cyanocobalamin supplementation improves outcomes in biotin-deficient models (currently absent and mechanistically implausible)
- Clarification of SAHPRA registration status for cyanocobalamin products in South Africa
- Identification of any specific subgroup of biotin metabolic disease patients with concurrent B12 deficiency who might benefit from combined supplementation
- Expert consultation with a metabolic medicine specialist to evaluate whether any niche clinical scenario could justify further investigation

> **Disclaimer:** This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Report adverse drug reactions to SAHPRA.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

