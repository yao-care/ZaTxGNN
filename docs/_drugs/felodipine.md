---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 7
---

# Felodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is an L-type calcium channel blocker that lowers blood pressure by vasodilation. The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, but there are **0 clinical trials** and **no publications that study felodipine in this condition**, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data (hypertension inferred from the drug class) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% (model rank 748) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank record. Felodipine belongs to the L-type calcium channel blocker class. It relaxes vascular smooth muscle and has both systemic and pulmonary vasodilatory activity. On paper, this makes a pulmonary hypertension indication plausible.

However, the mechanism is also the main safety concern. In hypoxic lung disease, vasodilators can worsen ventilation-perfusion matching by removing hypoxic pulmonary vasoconstriction. This could lower blood oxygen levels rather than help.

The 99.91% score is a graph-based prediction. The related entry "pulmonary hypertension with unclear multifactorial mechanism" has an identical score. This suggests the two share graph neighbours rather than carrying independent signal.

The pack contains a much better-supported candidate for this drug: **Prinzmetal (vasospastic) angina**. It is rated L2 with "Proceed with Guardrails", based on several small human studies of felodipine from 1989 to 1995. It is not the primary indication evaluated here, but it is worth a separate evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

The 19 retrieved publications are general hypoxia biology papers. None studies felodipine or pulmonary hypertension treatment, and all are still pending relevance review. The main ones are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respir Care Clin N Am | Describes the four basic mechanisms of hypoxemia, including ventilation-perfusion mismatch. Background only; relevant to the vasodilator safety concern. |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cell Biochem | Cellular responses to low oxygen and links to vascular disease and cancer. No drug data. |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annu Rev Immunol | Role of hypoxia in innate immunity and inflammation. No drug data. |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metab Brain Dis | Cognitive impairment caused by hypoxia. Not related to felodipine. |
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Res Rev | Hypoxia and brain ageing. Not related to felodipine. |

The remaining retrieved papers cover tumour hypoxia, keloid fibroblasts, multiple sclerosis and high-altitude physiology. They add nothing to this evaluation.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 31/7.1/0677 | Tri-plen 2.5mg/2.5mg | Tablet (oral) | Not stated in the available data |

The manufacturer and the approved indication text are not recorded, and Essential Medicines List status is not stated in the data.

## Safety Considerations

- **Key concern from the rationale analysis**: Vasodilators such as felodipine can worsen ventilation-perfusion matching and blood oxygen levels in hypoxic lung disease. This is a class-specific risk for this indication.

No SAHPRA package insert warnings, contraindications or drug interaction records were retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-model score, with no trials and no drug-specific literature. The class carries a plausible risk of harm in hypoxic lung disease, and the SAHPRA safety data has not been reviewed.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications). This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Any felodipine-specific haemodynamic or oxygenation data in pulmonary hypertension due to lung disease. The 1988 COPD haemodynamic study (PMID 2838319) appears in the pack under a different indication, chronic pulmonary heart disease, and its design should be verified.
- A separate evaluation of the Prinzmetal angina candidate (L2), which has stronger evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

