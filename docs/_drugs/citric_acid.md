---
layout: default
title: Citric Acid
parent: Model Prediction Only (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Citric Acid
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

# Citric Acid: From an Unstated Original Indication to Stomach Disease

## One-Sentence Summary

Citric acid is registered in South Africa as an ingredient of one marketed product (Picolax 16.1g sachet). The registration data do not state an approved indication.
The TxGNN model predicts it may be relevant to **Stomach Disease** (score 99.74%). The retrieval returned **29 clinical trials** and **20 publications**, but none shows citric acid treating a stomach condition, so this is a **model-only signal**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 99.74% (TxGNN rank 1752) |
| Evidence Level | L4 (background and mechanism-type literature only; no trial tests citric acid for a stomach disease) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Citric acid is a common organic acid and a component of the marketed product Picolax. No therapeutic mechanism linking it to stomach disease has been established.

In the retrieved stomach literature, citric acid appears in two roles, and neither is a treatment effect:
- **Diagnostic aid:** a citric acid test meal used to slow gastric emptying and improve the 13C-urea breath test for *H. pylori*.
- **Biological marker or constituent:** a component of gastric juice, and a serum metabolite reported to be elevated before gastric cancer onset in a Korean cohort.

The high TxGNN score therefore most likely reflects network proximity in the knowledge graph. It is not supported by direct clinical data.

## Clinical Trial Evidence

Of the 29 trials retrieved, none tests citric acid as a treatment for a stomach disease. Most matched only on the disease term. The most relevant are listed below. No SANCTR or PACTR identifiers were retrieved.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Effervescent calcium magnesium citrate to avert complications of long-term proton pump inhibitor use (fracture, low magnesium, kidney disease). Citrate is a component of a supplement, not the treatment of stomach disease. |
| [NCT02830789](https://clinicaltrials.gov/study/NCT02830789) | NA | Completed | 38 | Calcium citrate vs calcium carbonate for secondary hyperparathyroidism after Roux-en-Y gastric bypass. Citrate is used as a calcium salt. |
| [NCT05196945](https://clinicaltrials.gov/study/NCT05196945) | Phase 4 | Unknown | 316 | Vonoprazan-amoxicillin for first-line *H. pylori* eradication. Citric acid is not an intervention (graded C). |
| [NCT06760065](https://clinicaltrials.gov/study/NCT06760065) | Phase 3 | Not yet recruiting | 316 | Keverprazan-amoxicillin dual therapy vs quadruple therapy for *H. pylori* rescue. Does not involve citric acid (graded C). |
| [NCT03342456](https://clinicaltrials.gov/study/NCT03342456) | Phase 4 | Completed | 184 | Ilaprazole/doxycycline bismuth quadruple therapy in *H. pylori*-infected duodenal ulcer. Citric acid is not an intervention. |
| [NCT04329494](https://clinicaltrials.gov/study/NCT04329494) | Phase 1 | Recruiting | 49 | Pressurized intraperitoneal aerosolized chemotherapy (PIPAC) in peritoneal carcinomatosis, including gastric cancer. Unrelated to citric acid (graded C). |
| [NCT05753306](https://clinicaltrials.gov/study/NCT05753306) | Phase 2 | Recruiting | 40 | Robotic cytoreduction plus hyperthermic intraperitoneal chemotherapy (HIPEC) in gastric cancer with limited peritoneal metastasis. Unrelated to citric acid. |
| [NCT03320538](https://clinicaltrials.gov/study/NCT03320538) | NA | Completed | 360 | Herbal product Hou Gu Mi Xi in peptic ulcer disease. Unrelated to citric acid. |

## Literature Evidence

No randomised trial of citric acid in stomach disease was found. The literature is diagnostic, metabolomic, observational or preclinical.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Diagnostic clinical study | Gut Liver | Whether a citric acid test meal improves the accuracy of the 13C-urea breath test in Asian populations. This is a diagnostic use, not a treatment. |
| [4000241](https://pubmed.ncbi.nlm.nih.gov/4000241/) | 1985 | Clinical physiology study | N Engl J Med | Calcium absorption in achlorhydria (absent stomach acid) was compared between calcium carbonate and a pH-adjusted citrate form. It concerns citrate as a calcium salt. |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Metabolomic cohort | Metabolomics | High serum L-carnitine and citric acid were detectable in Koreans before gastric cancer onset. Citric acid is a possible risk biomarker, not a therapy. |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Cohort/omics | Cell Rep | Metabolic signature subtypes of gastric cancer, including TCA cycle upregulation, with distinct prognosis. |
| [37477784](https://pubmed.ncbi.nlm.nih.gov/37477784/) | 2024 | Review | Clin Transl Oncol | Energy metabolism as a treatment target in gastric cancer. Citric acid is not a therapeutic agent here. |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Animal study | J Pharm Pharmacol | MX1, a salt of a roxatidine metabolite with a bismuth-citric acid complex, protected against stress ulcers in rats. The effect belongs to the novel combination compound. |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet in ulcer disease. Restrictive diets are not supported. |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Observational | Gastroenterology | Lactic, pyruvic, citric and uric acid and urea content of human gastric juice. |
| [9604442](https://pubmed.ncbi.nlm.nih.gov/9604442/) | 1998 | Review | Br Med Bull | Urea breath tests for detecting *H. pylori* colonisation. |
| [26088916](https://pubmed.ncbi.nlm.nih.gov/26088916/) | 2015 | Metabolomic study | Appl Biochem Biotechnol | LC/MS metabolomic analysis of gastric cancer for biomarker discovery. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/11.5/0058 | Picolax 16.1g | Sachet | Not stated in the registration data |

The Essential Medicines List (EML) status is not available in the evidence pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

A drug-interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no trial or publication shows citric acid treating a stomach disease. Citric acid appears only as a diagnostic aid, a metabolic marker or a salt component. No mechanism or approved indication is documented.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (package insert) for Picolax, covering the approved indication, warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank.
- Any direct clinical evidence, such as a controlled study of citric acid for a defined stomach condition.

For reference, among the other predictions, **thrombotic disease** (rank 9) has a real anticoagulant mechanism. Citrate chelates calcium and is used as regional citrate anticoagulation in renal replacement therapy and in catheter lock solutions. The strongest trial, [NCT04548713](https://clinicaltrials.gov/study/NCT04548713) (n=1449, completed), tests a multi-component lock solution. It is an existing use of citrate, not a new repurposing signal, and is classed as a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

