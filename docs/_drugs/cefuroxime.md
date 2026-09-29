---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic that is marketed in South Africa as an injectable. The TxGNN model predicts it may be effective for **hyperamylasemia** (raised blood amylase), but there are **no clinical trials** and **no publications** supporting this prediction. It rests on the model score alone and should be treated as unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. Cefuroxime is a cephalosporin antibiotic used for bacterial infections (general drug knowledge, not taken from the data provided) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Cefuroxime is a beta-lactam antibiotic. It blocks bacterial cell wall synthesis by binding penicillin-binding proteins, and its established efficacy is against bacterial infections.

No plausible link has been identified between this antibacterial mechanism and amylase metabolism. Hyperamylasemia is a laboratory finding, most often related to pancreatic or salivary gland disease or reduced clearance, and an antibiotic would not be expected to treat it. The high TxGNN score most likely reflects proximity in the knowledge graph rather than a real biological relationship. Without trials or literature, the prediction cannot be considered mechanistically reasonable at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A38/20.1.1/0676 | Betaroxime | Injection |
| Reg. No. 42/20.1.1/0737 | Fksa cefuroxime vial powder for solution | Injection |
| Reg. No. 36/20.1.1/0296 | Sabax cefuroxime 250mg | Injection |
| Reg. No. L/20.1.1/0098 | Zinacef | Injection |

All four registrations are injectable products. The approved indication text was not available for these entries.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia has no supporting trials or literature and no plausible mechanism, so it does not justify further investment. Other predictions for cefuroxime are stronger, such as urinary tract infection (L2, Proceed with Guardrails). However, these appear to be established anti-infective uses rather than true repurposing. Suppurative otitis media has only susceptibility surveys and reviews (L4) and warrants at most a defined research question.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking cefuroxime to amylase metabolism, supported by preclinical or observational data
- Mechanism of action data (e.g., from DrugBank) to allow proper mechanistic-link analysis
- SAHPRA Professional Information (warnings and contraindications) to complete safety screening
- Approved indication text for the four SAHPRA registrations, to confirm the original indication and whether any listed prediction is already labelled use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

