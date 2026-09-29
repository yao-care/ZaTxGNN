---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 153
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Cyanocobalamin: From Vitamin B12 Replacement to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin is the standard injectable and oral form of vitamin B12. It is registered in South Africa in 18 products, but the approved-indication text was not supplied in the source data.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, with a very high score (99.6%).
That score is not backed by clinical data: **15 trials** were retrieved, but none tests cyanocobalamin in this condition, and the **20 publications** are mostly older narrative reviews on vitamin-responsive disorders.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data supplied. Cyanocobalamin is generally used as vitamin B12 replacement. |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 (mechanistic and indirect evidence only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyanocobalamin is the pharmaceutical form of vitamin B12, a cofactor for essential enzymes. Mechanistically, it may be relevant to biotin-related disorders, but the link is indirect.

The two vitamins meet at propionate metabolism. The biotin-dependent enzyme propionyl-CoA carboxylase produces methylmalonyl-CoA. The cobalamin-dependent enzyme methylmalonyl-CoA mutase then converts it to succinyl-CoA. In biotin-related disorders such as biotinidase deficiency or holocarboxylase synthetase deficiency, cobalamin could plausibly influence how downstream metabolites are handled.

The standard therapy for these disorders is biotin itself, and no evidence shows that cobalamin corrects the primary defect. The high TxGNN score most likely reflects knowledge-graph proximity among vitamin-responsive disorders, not clinical findings. Because the labelled indications and mechanism of action are missing, this link cannot be checked against approved use.

---

## Clinical Trial Evidence

All trials were graded C (weak or indirect relevance) or were not yet graded. None studies cyanocobalamin as a treatment for biotin metabolic disease. No SANCTR or PACTR identifiers were provided, and no ICTRP trials were found.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | Completed | 6,824 | Genomic newborn screening for 126 treatable genetic diseases. A diagnostic programme that may detect biotin-related disorders. It does not test cyanocobalamin. |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | Completed | 33 | Randomised trial of carglumic acid (Carbaglu®) in propionic and methylmalonic acidaemia. The drug is not cyanocobalamin, so it does not support this indication. |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completed | 39 | Nutritional intervention for oxidative stress and methylation in autism. Vitamin B12 is one component, but the disease is different. |
| [NCT01474486](https://clinicaltrials.gov/study/NCT01474486) | N/A | Completed | 40 | Multi-micronutrient feasibility study in heart failure. B12's effect cannot be separated from the other components. |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | Completed | 30 | Cross-over pilot of natural versus synthetic B-complex bioavailability in healthy adults. A formulation comparison only. |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | Completed | 75 | Vitamin and mineral supplementation for neuropathy and nephropathy in type 2 diabetes. A different disease. |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Unknown | 200 | Randomised cross-over of Q10 ubiquinol with vitamin B and E in autism and Phelan-McDermid syndrome. The link to this indication is indirect. |
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | Terminated | 5 | Fibre plus biotin before bariatric surgery to improve the gut microbiome. Not a biotin metabolic disease and not cyanocobalamin. |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | Enrolling by invitation | 30,000 | Voluntary newborn screening for a panel of rare conditions. A screening programme, not a treatment trial. |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | Unknown | 1,000 | Fortified food versus milk in malnourished children. Serum B12 is one outcome measure. |

---

## Literature Evidence

No randomised trials were retrieved. Most items are narrative reviews, and many are more than 20 years old. Study types marked "Unclassified" were not classified in the source data.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Vitamin-responsive disorders of cobalamin, folate and biotin. Vitamins act as obligatory enzyme cofactors, and rare inborn errors of their metabolism are described. |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | B12 deficiency and the nervous system. B12 is a cofactor in the methylmalonyl-CoA to succinyl-CoA step, a pathway that also involves biotin. |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Unclassified | Pediatric Research | 13C-propionate metabolism in patients with propionate disorders. The group included four B12-responsive methylmalonic acidaemia patients and one with multiple carboxylase deficiency. |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Vitamins in metabolic disease. Covers malabsorption, errors of vitamin metabolism and vitamin-dependent syndromes, where pharmacological doses may be needed. |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review | Pediatr Clin North Am | Megavitamin-responsive aminoacidopathies. Notes it is hard to predict cofactor response, so therapeutic trials are advised. |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Series | Vitamin dependency syndrome (no abstract available). |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Unclassified | Adv Clin Chem | Vitamin-responsive inborn errors of metabolism (no abstract available). |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Vitamins and type 2 diabetes. Biotin is mentioned among the B vitamins studied. Not specific to biotin metabolic disease. |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Animal study | J Endocrinol | B12 deficiency in female rats caused glucose intolerance and promoted ketogenesis. Not relevant to this indication. |
| [29173522](https://pubmed.ncbi.nlm.nih.gov/29173522/) | 2017 | Review | Gastroenterol Clin North Am | Vitamins and minerals in inflammatory bowel disease. Not relevant to this indication. |

---

## South Africa Market Information

There are 18 registrations in total; five are shown. The approved-indication text was blank for all five, and Essential Medicines List (EML) status was not included in the data supplied.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2413 (ACT 101/1965) | A-lennon vitamin b12 1ml | Injection | Not recorded in the data supplied |
| T1012 (ACT 101/1965) | Beespan | Capsule | Not recorded in the data supplied |
| U/2.6/218 | Restin | Capsule | Not recorded in the data supplied |
| A/21.8.1/743 | Menoflush | Tablet | Not recorded in the data supplied |
| 36/22.1/0508 | Cernevit | Infusion | Not recorded in the data supplied |

Across all 18 registrations, the dosage forms include injectable, oral, infusion, TPN and inhaler presentations.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by any trial or publication that tests cyanocobalamin in biotin metabolic disease. The mechanistic link is indirect, and biotin, not cobalamin, is the established therapy. The SAHPRA safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), obtained by downloading and parsing the package insert PDFs
- Mechanism of action from DrugBank
- Labelled indications for the registered products
- Targeted evidence on whether cobalamin adds anything in biotinidase or holocarboxylase synthetase deficiency
- Route-compatibility and similarity-to-original-indication assessments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

