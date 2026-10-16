---
layout: default
title: Dl-Alpha-Tocopherol
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dl-Alpha-Tocopherol: predicted new indication Immature cataract (evidence level L5). Approved use: Not available"
---

# Dl-Alpha-Tocopherol
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

# DL-alpha-Tocopherol: From Vitamin E Supplementation (No Indication Text on File) to Immature Cataract

## One-Sentence Summary

DL-alpha-Tocopherol is a form of vitamin E. The only South African registration found is Cernevit, an infusion product, and no approved indication text is available in the data compiled for this report.
The TxGNN model predicts it may be effective for **immature cataract** (and several other cataract types), but **no clinical trials and no directly relevant publications** currently support this direction.
This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration contains no approved indication text) |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

Other predicted indications, all with a TxGNN score of about 99.97–99.98% and all at evidence level L5 (Hold):

| Rank | Predicted Indication | Plausibility Comment |
|---|------|------|
| 2 | Mature cataract | Antioxidant protection is plausible, but a fully opacified lens is unlikely to be reversed |
| 3 | Tetanic cataract | Caused by low calcium or hypoparathyroidism, with no clear link to antioxidant action |
| 4 | Craniostenosis cataract | Link probably indirect, possibly an artefact of the knowledge graph |
| 5 | Diabetes mellitus type 2 associated cataract | Oxidative stress and polyol pathway activity make this plausible |
| 6 | Diabetic cataract | Plausible mechanism; one publication supplied, but it is not relevant clinically |
| 7 | Nuclear senile cataract | Age-related oxidative damage to lens proteins is plausible |
| 8 | Cortical cataract | Lipid peroxidation in lens membranes is a plausible target |
| 9 | Senile cataract | Oxidative stress is a recognised contributor |
| 10 | Antithrombin deficiency type 2 | No clear mechanistic link, likely a graph artefact |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, DL-alpha-Tocopherol is a lipid-soluble form of vitamin E with antioxidant properties, and it may limit oxidative damage to lens proteins and cell membranes.

Oxidative stress is recognised as a contributor to age-related and diabetic cataract. This gives the prediction biological plausibility, particularly for senile, nuclear, cortical and diabetes-associated cataract. The plausibility is weaker for mature cataract, where the lens is already fully opaque. It is weakest for tetanic cataract, craniostenosis cataract and antithrombin deficiency type 2, where the link is likely an artefact of the knowledge graph rather than a true pharmacological relationship.

This is a hypothesis only. The data compiled for this report contain no trial or literature evidence that vitamin E treats or prevents cataract, and any claim from earlier vitamin E cataract studies would need to be verified separately.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12770645](https://pubmed.ncbi.nlm.nih.gov/12770645/) | 2003 | Animal study (rat) | The Journal of Nutritional Biochemistry | Studied whether vitamin E (dl-alpha-tocopherol acetate) protects against oxidative stress caused by carbon tetrachloride. It did not examine cataract or diabetes, so it gives no direct clinical support. |

This is the only publication supplied, and it relates to diabetic cataract only through the general theme of oxidative stress.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/22.1/0508 | Cernevit | Infusion | Not available in the data compiled for this report |

Cernevit is an injectable (infusion) product. Its Essential Medicines List (EML) status is not available in the data compiled for this report. Whether an infusion product could serve a cataract indication has not been assessed, as route compatibility is still pending.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score and a plausible antioxidant mechanism. No clinical trials or relevant publications were found, and the original indication, mechanism of action and safety information are all missing, so no clinical conclusion can be drawn.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert for Cernevit to obtain the approved indication, warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic literature search on vitamin E and cataract (observational studies, RCTs and reviews) to establish whether any real evidence exists
- A search of clinical trial registries (ClinicalTrials.gov, SANCTR, PACTR) for cataract studies of vitamin E
- An assessment of route and formulation suitability, since the only registered product is an infusion
- Prioritising the age-related and diabetes-associated cataract predictions for any follow-up, as the rarer cataract types and antithrombin deficiency type 2 show little mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

