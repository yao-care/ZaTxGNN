---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Antipsychotic Use to Retinal Dystrophy (Top-Ranked Prediction, Not Supported by Evidence)

## One-Sentence Summary

Quetiapine is an atypical antipsychotic with five SAHPRA registrations in South Africa. The approved indication text is not included in the Evidence Pack.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and no relevant publications supporting it.
The only prediction among the top 10 with a plausible rationale is **trichotillomania**, which is backed by case reports and reviews only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available registration data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies (rank 1) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Quetiapine is generally understood as a dopamine D2 and serotonin 5-HT2A receptor antagonist.

For the top prediction, **no plausible mechanism was identified**. Retinal dystrophy is an inherited retinal degeneration, and quetiapine has no established role in it. The high score (99.57%) is a model output only. Antipsychotic-associated retinal toxicity has also been reported, so a safety concern is possible.

The other nine top-10 predictions are also model-only, with no supporting studies. They are mostly rare genetic or structural conditions (glycosylation disorder, hydranencephaly, 17p13.3 microdeletion, polymicrogyria, X-linked myopia variants, Charcot-Marie-Tooth type 1G). Trichotillomania (rank 8, score 99.38%) is the exception. It is an OCD-spectrum disorder, and the 5-HT2A/D2 antagonism of quetiapine is the same rationale used for atypical antipsychotic augmentation in OCD and related conditions. The clinical evidence for it is limited to case reports and narrative reviews, so this remains a research question rather than a treatment recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR) for the top-ranked prediction, or for trichotillomania.

## Literature Evidence

**Rank 1: retinal dystrophy.** The 15 retrieved publications concern extraocular muscle, orbital and congenital eye anomalies. **None of them studies quetiapine**, so they do not support this prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Not classified | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles; no drug data |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex (vitreoretinal degeneration); no drug data |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging of paediatric ocular pathologies; no drug data |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Not classified | Am J Ophthalmol | Pathogenesis of maculopathy with cavitary optic disc anomalies; no drug data |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Not classified | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders; no drug data |

**Rank 8: trichotillomania (the only prediction with quetiapine-specific literature).**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12405081](https://pubmed.ncbi.nlm.nih.gov/12405081/) | 2002 | Case report/Review | Psychiatry | Overview of trichotillomania treatment; favourable response to quetiapine in one patient |
| [19142421](https://pubmed.ncbi.nlm.nih.gov/19142421/) | 2008 | Case report | Rev Bras Psiquiatr | Quetiapine used to treat trichotillomania |
| [11212595](https://pubmed.ncbi.nlm.nih.gov/11212595/) | 2001 | Case report/Review | J Psychiatry Neurosci | Quetiapine exacerbated obsessive-compulsive symptoms in one patient with OCD and trichotillomania, a counter-signal |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review | Int J Dermatol | Pharmacological treatment of trichotillomania; no treatment guidelines exist |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/2.6.5/1085 | Truvalin Xr 150 | Tablet | Not listed in the data |
| Reg. No. 43/2.6.5/0429 | Dopaquel 25 | Fct | Not listed in the data |
| Reg. No. 45/2.6.5/0642 | Kizofrin | Tablet | Not listed in the data |
| Reg. No. 45/2.6.5/0212 | Quetiapine biotech | Tablet | Not listed in the data |
| Reg. No. 36/2.6.5/0070 | Seroquel | Tablet | Not listed in the data |

All products are oral formulations. Essential Medicines List status is not provided in the data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Two points from the evidence are relevant. Antipsychotic-associated retinal toxicity has been reported, which matters for any retinal indication. For trichotillomania, metabolic and sedation risks must be weighed against a non-life-threatening condition.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction rests on a model score alone (L5), with no plausible mechanism, no trials and no relevant literature. Possible retinal toxicity adds a safety concern. Trichotillomania (L4) is the only lead worth follow-up, but its evidence is limited to case reports.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications), which is a blocking gap for any safety screening
- Mechanism of action data from DrugBank
- For trichotillomania, a systematic review of the existing case reports and, if warranted, a controlled trial design
- For the retinal prediction, no action is recommended unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

