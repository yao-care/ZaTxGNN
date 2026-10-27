---
layout: default
title: Methylprednisolone Aceponate
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methylprednisolone Aceponate: predicted new indication Gout (evidence level L5). Approved use: Not stated in the registration data compiled for this report (a topic…"
monitor_inn: "Methylprednisolone aceponate"
predicted_indications: ["gout", "Raynaud disease", "allergic asthma", "diabetic nephropathy", "brain small vessel disease 1 with or without ocular anomalies", "intrinsic asthma", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "congestive heart failure", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Methylprednisolone Aceponate
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

## Methylprednisolone aceponate: From Topical Corticosteroid Use to Gout (Predicted)
{: .text-alpha }

## One-Sentence Summary

Methylprednisolone aceponate is a topical glucocorticoid (marketed in South Africa as an ointment) with anti-inflammatory activity. The TxGNN model predicts it may be effective for **gout**, but **no clinical trials and no publications** currently support this prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (a topical corticosteroid for inflammatory skin conditions is the usual use of this class) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, methylprednisolone aceponate is a topical glucocorticoid ester with anti-inflammatory activity, and mechanistically this class may be relevant to inflammatory conditions.

Systemic corticosteroids are used for acute gout flares because they suppress the inflammatory response to urate crystals. However, this compound is a topical dermatological ester, and there is no documented systemic use in gout. The link is a model prediction only, and the data compiled for this report contain no trials or publications supporting it.

**Other predictions** (all Hold, none supported by clinical trials):

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Raynaud disease | 98.54% | L5 | No clear mechanistic rationale |
| Allergic asthma | 98.33% | L4 | Class-level rationale only. One 2002 review of topical corticosteroids in dermatology; no asthma data |
| Diabetic nephropathy | 98.29% | L5 | Corticosteroids are not established therapy and may worsen glycaemic control |
| Brain small vessel disease 1 (with or without ocular anomalies) | 98.28% | L5 | Rare monogenic disorder; likely a graph artefact |
| Intrinsic asthma | 98.25% | L5 | Class-level inference only |
| Autosomal dominant familial haematuria-retinal arteriolar tortuosity-contractures syndrome | 98.24% | L5 | Ultra-rare genetic disorder; no plausible mechanism |
| Congestive heart failure | 97.90% | L5 | Corticosteroids cause sodium and fluid retention; theoretical safety concern |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 97.79% | L5 | Only an indirect link via underlying lung inflammation |
| Pulmonary hypertension with unclear multifactorial mechanism | 97.79% | L5 | Identical score to the entry above, suggesting a shared graph neighbourhood rather than independent signal |

## Clinical Trial Evidence

Currently no related clinical trials registered for gout.

## Literature Evidence

Currently no related literature available for gout.

For the third-ranked prediction (allergic asthma), one publication was linked. It is indirect, class-level evidence only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11817968](https://pubmed.ncbi.nlm.nih.gov/11817968/) | 2002 | Review | American Journal of Clinical Dermatology | Review of the pharmacology and use of new and established topical corticosteroids in dermatology; does not address asthma |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| X/13.4.1/385 | Advantan | Ointment | Not available in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: no drug interaction records were found, and no contraindication edges were found in the knowledge graph. This should not be read as evidence of safety. Corticosteroids as a class may cause sodium and fluid retention and may worsen glycaemic control, which is relevant to some of the predicted indications (heart failure, diabetic nephropathy).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction has a high model score but no supporting clinical trials or publications (L5). The drug is a topical ester with no documented systemic use, and the SAHPRA label warnings and contraindications could not be reviewed, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (PI) for approved indications, warnings and contraindications
- Mechanism of action data from DrugBank
- Evidence on systemic exposure and a feasible route of administration for gout (the current product is an ointment)
- Preclinical or clinical studies of this compound in gout, or a literature search for related evidence
- Route compatibility assessment between available formulations and the requirements of the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

