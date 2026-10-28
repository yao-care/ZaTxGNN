---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-29
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis, staphylococcal infections, endocarditis"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Vancomycin: From Clostridium difficile Colitis to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic, originally used for Gram-positive infections such as *Clostridium difficile* colitis, staphylococcal infections and endocarditis.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but **no clinical trials** and only **1 unrelated case report** support this direction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis, staphylococcal infections, endocarditis (SAHPRA licence indication text is not available) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 3 of 3) |
| Number of SAHPRA Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, vancomycin inhibits cell wall synthesis in Gram-positive bacteria, and its efficacy in Gram-positive infections is well established.

Diffuse scleroderma (systemic sclerosis) is an autoimmune fibrotic disease, not a bacterial infection. There is no plausible mechanistic link between a cell wall–inhibiting antibiotic and this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only retrieved paper describes an erythroderma and sepsis case and does not address scleroderma treatment.

**Other predictions reviewed**

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Streptococcal pneumonia | 0.9960 | L4 | The only mechanistically plausible prediction. Vancomycin is already used for penicillin-resistant pneumococcal infections. This extends existing use and is not novel repurposing. Support is indirect (older reviews, no registered trials). |
| Paratyphoid fever, salmonellosis, typhoid fever | 99.75–0.9985 | L5 | Gram-negative organisms. The outer membrane blocks vancomycin, so no intrinsic activity is expected. |
| Congenital analbuminemia, polyclonal hyperviscosity syndrome, hyperamylasemia, blood group incompatibility, premalignant haematological disease | 99.54–0.9979 | L5 | No mechanistic rationale and no supporting evidence. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | Erythroderma with sepsis and eosinophilia in a 56-year-old man. It does not address scleroderma or vancomycin efficacy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/20.1.1/0674 | Vancomycin-Faulding Pow F/Injection | Injection | Not available |
| Reg. No. 54/20.1.1/0295 | Cytovan 500Mg Iv | Infusion | Not available |
| Reg. No. 29/20.1.1/0675 | Vancomycin-Faulding 1G | Injection | Not available |

All 3 registrations are valid single-ingredient products. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

**Contraindication-related diseases (from the knowledge graph, not label text):** kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder, auditory system disease.

**Drug Interactions** (100 interactions identified; 20 shown in the data compiled for this report):
- **Major:** human immunoglobulin G (intravenous), human botulinum neurotoxin A/B immune globulin, live *Vibrio cholerae* CVD 103-HgR vaccine.
- **Moderate (examples):**
  - Nephrotoxic or ototoxic agents: amphotericin B (including the lipid complex), amikacin, capreomycin, carboplatin, bacitracin.
  - NSAIDs: ketorolac, ibuprofen, diclofenac, celecoxib.
  - Others: metformin, estradiol, ethinylestradiol, mesalazine, balsalazide, ibandronate, cholestyramine.

SAHPRA package insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for diffuse scleroderma has no mechanistic basis, no clinical trials and no relevant literature (Evidence Level L5). Pursuing it is not justified. Among the other predictions, only streptococcal pneumonia is plausible, and it is an extension of established use rather than a new indication.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications and approved indications) to complete safety screening
- Mechanism of action data from DrugBank
- If any direction is pursued, streptococcal pneumonia (resistant organisms) is the only candidate. It would need a targeted literature review and a check against local antimicrobial stewardship guidance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

