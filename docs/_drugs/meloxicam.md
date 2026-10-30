---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Meloxicam"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Meloxicam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Meloxicam: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Meloxicam is a COX-2-preferential non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed (licences cancelled: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 0) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, meloxicam is a COX-2-preferential NSAID. It reduces prostaglandin-mediated inflammation and pain in arthritic conditions.

The predicted disease is a genetic skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, resulting in a structural growth defect. Meloxicam might ease pain or inflammation, but it does not address the underlying pathology. We found **no clear mechanistic link**. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other top-ranked predictions** (all with no clinical trials):

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9992 | No plausible mechanistic link; the score comes from the TxGNN model (deep learning) and may reflect similarities learned between related diseases, not biological evidence |
| 3 | Myosclerosis | 0.9990 | Weak and speculative; no evidence that fibrosis can be modified |
| 4 | Brachyolmia | 0.9989 | No plausible mechanistic link |
| 5 | Pseudoachondroplasia | 0.9981 | Indirect at best; possible symptomatic pain relief only |
| 7 | Rheumatoid nodulosis | 0.9951 | No known NSAID effect on nodule formation |
| 9 | WHIM syndrome | 0.9938 | No mechanistic link (CXCR4 gain-of-function) |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9936 | No plausible mechanistic link |

Of these, only rank 8 (rheumatoid factor-positive polyarticular JIA) has any supporting literature and a credible mechanistic rationale. It is closer to the existing indication than to a genuinely new one.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For the rank 8 prediction (rheumatoid factor-positive polyarticular JIA), one paper is available:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/) | 2014 | Safety registry (Phase 4) | Pediatric Rheumatology Online Journal | Long-term safety and developmental data for celecoxib versus non-selective NSAIDs in JIA. This is indirect evidence, as it does not study meloxicam specifically. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 35/3.1/0329 | Melflam | Tablet | Not available in the data compiled for this report |

Only one valid single-ingredient registration exists, and the route of administration is oral. Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

**Contraindications / conditions of concern (from the drug's associations with these conditions, not label text):** hypertension, congestive heart failure, cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, kidney disease and impaired renal function, active peptic ulcer disease, gastritis, blood coagulation disorders, anaemia, diabetes mellitus (including diabetic ketoacidosis), hyperlipidaemia, and substance abuse/dependence.

**Drug interactions** (100 interactions found; examples shown):
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, aprepitant, vancomycin, kanamycin, potassium citrate and bicarbonate, and bowel-preparation agents (sodium picosulfate, sodium sulfate, polyethylene glycol with electrolytes)
- **Minor:** linaclotide

Please refer to the SAHPRA-approved Professional Information (PI) for authoritative warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature, and no mechanistic link to the predicted disease. The score appears to be a TxGNN model (deep learning) artefact. The only credible candidate in the list (polyarticular JIA) lies within meloxicam's existing indication class, so it is not a true repurposing opportunity.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- The SAHPRA package insert, including approved indications, warnings and contraindications
- For the JIA subtype, meloxicam-specific paediatric efficacy and safety data, and confirmation of whether the South African label covers JIA
- Independent expert review of why the model ranks skeletal dysplasias highly, before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

