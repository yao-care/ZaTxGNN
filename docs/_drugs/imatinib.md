---
layout: default
title: Imatinib
parent: Model Prediction Only (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: From Chronic Myeloid Leukaemia and GIST to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor first marketed for chronic myeloid leukaemia and some gastrointestinal stromal tumours (GIST).
The TxGNN model predicts it may be effective for **heart fibrosarcoma**, but there are **0 clinical trials** and only **1 publication** (a 2008 drug-bulletin commentary that itself calls the evidence "not robust"), with no cardiac-specific data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic myeloid leukaemia and GIST (from PMID 18623899; the SAHPRA indication text was not supplied) |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (mechanistic plausibility only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, imatinib inhibits PDGFRA, PDGFRB and KIT, and its efficacy in leukaemia and GIST has been established. Mechanistically, these targets are plausible in fibroblastic sarcomas, which is presumably why the model links it to fibrosarcoma.

However, the link to the **heart** specifically is weak. The only linked publication is a general commentary on imatinib's expanding indications, and it contains no cardiac data. The high graph score is therefore not backed by clinical evidence for this site.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Imatinib's indications have expanded over the years, but the evidence for the new ones is described as not robust. In Ph+ acute lymphoblastic leukaemia (55 patients), the haematological response rate was higher with imatinib than with chemotherapy. No cardiac or fibrosarcoma data. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 42/34/0496 | Imavec | Capsule (oral) | Not stated in the data supplied |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |

For myelosuppression risk, emetogenicity, monitoring items and handling protection, please refer to the Professional Information (PI) warnings and precautions.

## Safety Considerations

- **Literature signal:** A case report (PMID 30096127) describes imatinib-induced DRESS (drug reaction with eosinophilia and systemic symptoms) in a patient with a solid tumour. This should be kept in mind in any later safety review.
- **Drug Interactions:** No interaction records were found in the query.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only a model prediction and one non-specific commentary support this indication. There are no trials and no cardiac-specific evidence.

**To proceed, the following is needed:**
- Case-level or trial evidence for cardiac fibrosarcoma, ideally with PDGFR/KIT dependence confirmed on tumour testing
- The SAHPRA Professional Information (warnings, contraindications, approved indications)
- Detailed mechanism of action data (MOA)
- A decision on other candidates in this drug's list. Liposarcoma has three completed imatinib Phase 2 or Phase 1/2 soft tissue sarcoma trials (evidence level L2, results not supplied). Fibroblastic neoplasm is supported mainly by dermatofibrosarcoma protuberans (DFSP) literature, including a 2025 European guideline (evidence level L3). Both are better supported than heart fibrosarcoma.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

