---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Meloxicam: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
---

# Meloxicam
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

# Meloxicam: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a COX-2-preferential non-steroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (the SAHPRA registration data compiled for this report contain no indication text, so these indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, meloxicam is a COX-2-preferential NSAID. It reduces prostaglandin-mediated inflammation and pain in arthritic conditions.

The predicted disease is a genetic skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene, resulting in a structural growth defect. Meloxicam might ease pain or inflammation, but it does not address the underlying pathology. We found **no clear mechanistic link**. The high TxGNN score is most likely a network-proximity artefact arising from shared musculoskeletal annotations in the knowledge graph.

**Other top-ranked predictions** (all with no clinical trials):

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.92% | No plausible mechanistic link; likely a graph artefact |
| 3 | Myosclerosis | 99.90% | Weak and speculative; no evidence that fibrosis can be modified |
| 4 | Brachyolmia | 99.89% | No plausible mechanistic link |
| 5 | Pseudoachondroplasia | 99.81% | Indirect at best; possible symptomatic pain relief only |
| 6 | Spondyloarthropathy, susceptibility to | 99.52% | Plausible, but already an original indication, so not true repurposing |
| 7 | Rheumatoid nodulosis | 99.51% | No known NSAID effect on nodule formation |
| 8 | Rheumatoid factor-positive polyarticular JIA | 99.44% | Strong mechanistic fit; an extension within the existing indication class; evidence level L4 |
| 9 | WHIM syndrome | 99.38% | No mechanistic link (CXCR4 gain-of-function) |
| 10 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.36% | No plausible mechanistic link |

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

**Contraindications / conditions of concern (from knowledge graph associations, not label text):** hypertension, congestive heart failure, cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, kidney disease and impaired renal function, active peptic ulcer disease, gastritis, blood coagulation disorders, anaemia, diabetes mellitus (including diabetic ketoacidosis), hyperlipidaemia, and substance abuse/dependence.

**Drug interactions** (100 interactions found; examples shown):
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, aprepitant, vancomycin, kanamycin, potassium citrate and bicarbonate, and bowel-preparation agents (sodium picosulfate, sodium sulfate, polyethylene glycol with electrolytes)
- **Minor:** linaclotide

Please refer to the SAHPRA-approved Professional Information (PI) for authoritative warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature, and no mechanistic link to the predicted disease. The score appears to be a knowledge-graph artefact. The only credible candidate in the list (polyarticular JIA) lies within meloxicam's existing indication class, so it is not a true repurposing opportunity.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- The SAHPRA package insert, including approved indications, warnings and contraindications
- For the JIA subtype, meloxicam-specific paediatric efficacy and safety data, and confirmation of whether the South African label covers JIA
- Independent expert review of why the model ranks skeletal dysplasias highly, before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

