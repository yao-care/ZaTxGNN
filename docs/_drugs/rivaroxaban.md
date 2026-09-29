---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is a Factor Xa inhibitor anticoagulant, and it is registered and marketed in South Africa.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but there are **no clinical trials** and only **3 indirect publications** (none testing rivaroxaban in rheumatoid arthritis), so this remains a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L4 (indirect mechanistic literature only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known information, rivaroxaban is a Factor Xa inhibitor, its role in preventing and treating thrombosis is established, and mechanistically it may be applicable to rheumatoid arthritis only through an indirect route.

The proposed link is a hypothesis. Factor Xa and thrombin signal through PAR receptors, which may connect coagulation to synovial inflammation. Thrombin generation is also altered in autoimmune disease, and a 2021 review of thrombin generation assays in autoimmune disease supports this general point. Autoimmune disease is also regularly associated with cardiovascular and thrombotic risk.

No study shows that rivaroxaban changes rheumatoid arthritis disease activity. The high model score reflects knowledge-graph similarity and is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity venous thromboembolism diagnosis and treatment. Background on thrombosis only, not rheumatoid arthritis. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay is useful for assessing hypercoagulability in autoimmune disease. Supports the mechanistic hypothesis only. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation. Not relevant to rheumatoid arthritis efficacy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 55/8.2/0140 | Axolta 10 Mg | Film-coated tablet (Fct) |
| Reg. No. 55/8.2/0719 | Rexarav 20 Mg | Film-coated tablet (Fct) |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no rheumatoid arthritis-specific studies. The only support is an indirect mechanistic hypothesis, and this is not enough to justify moving forward. The other nine model predictions (gout, HIV infectious disease and others) also have no supporting efficacy evidence and are on Hold.

**To proceed, the following is needed:**
- Preclinical or translational data showing that Factor Xa or thrombin inhibition affects synovial inflammation or disease activity in rheumatoid arthritis
- Mechanism of action data from DrugBank
- The SAHPRA package insert (warnings and contraindications) for a safety screen. This is a blocking gap.
- Registered indication text for the two SAHPRA products
- A risk-benefit assessment of bleeding, especially with rheumatoid arthritis co-medications such as NSAIDs and corticosteroids

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

