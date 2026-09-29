---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic used against serious Gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but the model score is not backed by any clinical or mechanistic evidence: there are **0 clinical trials** and only **1 unrelated case report**.
This looks like a graph artifact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (general antibiotic use; the SAHPRA indication text was not captured in the data) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Vancomycin is known to inhibit cell wall synthesis in Gram-positive bacteria.

Diffuse scleroderma is an autoimmune, fibrotic disease. It is not a bacterial infection, and inhibiting bacterial cell wall synthesis has no plausible link to its pathology. The only retrieved paper is a case of erythroderma with sepsis, which does not concern scleroderma.

The very high score (99.92%, model rank 712) most likely reflects how the knowledge graph is connected rather than a real biological relationship. We do not consider this prediction mechanistically supported.

For context, of the 10 predicted indications in the pack, only **streptococcal pneumonia** (rank 9) is biologically plausible. Vancomycin is active against *Streptococcus pneumoniae*. That is an established antibacterial use rather than true repurposing, and it still has no efficacy trial. Most other predictions (typhoid, paratyphoid, salmonellosis) involve Gram-negative organisms that vancomycin does not treat. Several others (congenital analbuminemia, hyperviscosity syndrome, hyperamylasemia, premalignant haematological disease) have no rationale at all.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were identified for this indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | Am J Case Rep | Diffuse exfoliative rash (erythroderma) with sepsis and eosinophilia in a 56-year-old man. It does not concern scleroderma and gives no support for this prediction. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 29/20.1.1/0674 | Vancomycin-Faulding Pow F/Injection | Injection |
| Reg. No. 54/20.1.1/0295 | Cytovan 500Mg Iv | Infusion |
| Reg. No. 29/20.1.1/0675 | Vancomycin-Faulding 1G | Injection |

All three products are injectable or infusion forms. The approved indication text was not available in the data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials for scleroderma, and no plausible mechanism links a cell wall synthesis inhibitor to an autoimmune fibrotic disease. The only retrieved paper is unrelated. Vancomycin is already marketed in South Africa for its antibacterial use, and there is no reason to pursue it for scleroderma.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking data gap for safety screening
- Mechanism of action data from DrugBank
- Any mechanistic or preclinical evidence linking vancomycin to fibrosis or autoimmune pathology, which is unlikely to exist
- Consideration of streptococcal pneumonia (rank 9) instead, as a research question within established antibacterial use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

