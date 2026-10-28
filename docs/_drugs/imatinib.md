---
layout: default
title: Imatinib
parent: Model Prediction Only (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
last_modified_at: 2026-10-27
description: "Imatinib: predicted new indication heart fibrosarcoma (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Imatinib: tyrosine kinase inhibitor (BCR-ABL, KIT, PDGFR) → heart fibrosarcoma
{: .text-alpha }

## One-Sentence Summary

Imatinib is an oral tyrosine kinase inhibitor that blocks the ABL, KIT and PDGFR kinases and is registered in South Africa as a single-ingredient capsule.
The TxGNN model predicts it may be effective for **heart fibrosarcoma**, with a prediction score of 0.9994.
For this specific disease there are **no registered clinical trials** and only **one general review** in the data compiled for this report, so the prediction rests on model output and indirect biological reasoning.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | heart fibrosarcoma |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Imatinib is known to inhibit the PDGFR, KIT and ABL kinases.

Some fibroblast-derived tumours, particularly dermatofibrosarcoma protuberans (DFSP) with the COL1A1-PDGFB fusion, depend on PDGFR signalling and respond to imatinib. The reasoning for heart fibrosarcoma is an extrapolation from this biology. There is no direct data on primary cardiac fibrosarcoma, and fibrosarcomas in general do not carry this fusion, so the mechanistic link is uncertain.

The only publication retrieved for this prediction is a 2008 general review of imatinib's expanding indications (*Prescrire International*). It does not study heart fibrosarcoma. No cited study directly addresses this disease, so the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Overview of imatinib's expanding indications, noting that the evidence for several newer uses is not robust. It does not address heart fibrosarcoma. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 42/34/0496 | Imavec | Capsule | Not recorded in the local data |

One valid single-ingredient registration is listed. Essential Medicines List status is not available in the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the Professional Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; haematological parameters (FBC), liver function and renal function are usually reviewed |
| Handling Protection | Please refer to the PI and local cytotoxic drug handling guidance |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs in total (the first 20 are available here). Two are rated **Major**: eliglustat and naloxegol. Most of the others are rated Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), clarithromycin, cimetidine, aprepitant, morphine, naltrexone, naldemedine, pioglitazone, glimepiride, saxagliptin, lansoprazole, dexlansoprazole and metreleptin.

Package-insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9994), but no clinical trial or publication directly studies imatinib in heart fibrosarcoma. The mechanistic link is extrapolated from DFSP biology, which does not apply to fibrosarcoma in general.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of imatinib activity in cardiac fibrosarcoma (for example case series or tumour molecular profiling for PDGFB/PDGFR dependence)
- Detailed mechanism-of-action data
- Review of the SAHPRA Professional Information for warnings and contraindications
- A safety and interaction-management plan for this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

