---
layout: default
title: Dienogest
parent: Model Prediction Only (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dienogest: predicted new indication Amenorrhoea (evidence level L4). Approved use: Not available in the data compiled for this report (the approved indi…"
monitor_inn: "Dienogest"
predicted_indications: ["amenorrhea (disease)", "primary ovarian failure", "breast fibrocystic disease", "isolated growth hormone deficiency", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "hypogonadotropic hypogonadism with or without anosmia", "partial trisomy/tetrasomy of the short arm of chromosome 5", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18"]
---

# Dienogest
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dienogest: From an Unspecified Original Indication to Amenorrhoea
{: .text-alpha }

## One-Sentence Summary

Dienogest is a selective progestin. The data compiled for this report do not state an approved indication for the registered South African product. The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **0 registered clinical trials** and only **7 publications** retrieved. These publications mostly describe amenorrhoea as an expected effect of treatment, not a condition that dienogest treats.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the approved indication text is blank) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dienogest is a selective progestin with strong antiproliferative activity on the endometrium and partial suppression of ovulation. It is widely used for endometriosis.

The literature links dienogest to amenorrhoea mainly as an on-treatment effect or adverse effect. This includes a systematic review of dienogest adverse effects and reviews of hormonal endometriosis treatment, where inducing amenorrhoea is a treatment goal. There is no evidence that dienogest treats amenorrhoea as a condition. Progestin therapy can be used in secondary amenorrhoea when oestrogen levels are adequate, but this is a class effect and not specific to dienogest.

The high TxGNN score most likely reflects the drug's association with amenorrhoea as an effect, not a therapeutic rationale. The prediction should be treated as a research question, not as a repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic review / Bayesian meta-analysis | BMC Pharmacol Toxicol | Summarises adverse events and their prevalence during dienogest treatment in endometriosis and adenomyosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective cohort (514 women) | Reprod Sci | Long-term (beyond 12 months) efficacy, safety and recurrence with dienogest 2 mg daily in ovarian endometrioma |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine basis of hormonal treatments for endometriosis, including dienogest |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Clinical / pharmacodynamic study | Eur J Contracept Reprod Health Care | Reports a high inhibition ratio and transformation index for dienogest 2 mg, supporting its use in endometriosis; amenorrhoea is described as a treatment aim |
| [42438810](https://pubmed.ncbi.nlm.nih.gov/42438810/) | 2026 | Case report | JCEM Case Rep | Primary hyperparathyroidism became overt after dienogest-altered oestrogen dynamics (started for menorrhagia) |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | J Pediatr Adolesc Gynecol | Advanced 3-D visualisation for Müllerian anomalies; indirect relevance only |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Ovarian granulosa cell tumour in a patient with polycystic ovarian syndrome; indirect relevance only |

None of these publications tests dienogest as a treatment for amenorrhoea.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/18.8/0591 | Qlaira | Tablet (oral) | Not available in the data compiled for this report |

Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are drug-disease links from the TxGNN knowledge graph, not label text, and must be checked against the approved Professional Information): hypertension, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, hypothyroidism, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridaemia, hypercalcaemia and related calcium or phosphorus disorders, female breast carcinoma, and thrombophlebitis.

**Drug interactions:** 37 interactions were identified. Examples of those graded **Major** are:
- Sugammadex
- Griseofulvin
- Bexarotene
- Brigatinib
- Dabrafenib
- Encorafenib

Examples graded **Moderate** include linaclotide, metreleptin, prucalopride, miltefosine, adalimumab, anakinra, certolizumab pegol, cladribine and enasidenib. Ethanol is graded **Minor**. Only 20 of the 37 interactions were available for review.

Please refer to the SAHPRA-approved Professional Information (PI) for the full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Amenorrhoea appears in the literature as an expected effect of dienogest and not as a condition it treats. No clinical trials exist, and the high TxGNN score is likely an artefact of this association.

**To proceed, the following is needed:**
- The approved indication and the SAHPRA Professional Information, including warnings and contraindications for Qlaira
- Detailed mechanism of action data
- Clarification of whether the goal is treating amenorrhoea or inducing it, which are opposite aims
- Any clinical studies of dienogest in amenorrhoea, which would be needed to move beyond a research question
- Review of the major drug interactions and the knowledge-graph contraindication signals

**Note on other predictions:** The remaining nine predicted indications, including primary ovarian failure, breast fibrocystic disease and hypogonadotropic hypogonadism, have no clinical trials. Most have no literature either, and several are mechanistically opposed to dienogest's action. They are not recommended for further evaluation at this stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

