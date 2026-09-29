---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
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

# Meloxicam: From an Unrecorded Original Indication to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is an oral NSAID (COX-2 inhibitor) registered in South Africa as Melflam tablets. The SAHPRA record supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available SAHPRA data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Meloxicam is an NSAID that inhibits COX-2 and so reduces prostaglandin synthesis. It is used for pain and inflammation.

On mechanism, this prediction is **not plausible**. Hunter-Thompson type acromesomelic dysplasia is a genetic skeletal dysplasia caused by disruption of the GDF5/CDMP1 pathway. COX-2 inhibition does not act on this pathway and would not correct the underlying defect. At most, an NSAID could relieve joint pain, and no data support even that here.

The high score (99.92%) is a graph-based association from the TxGNN knowledge graph. It is not evidence of clinical benefit. Scores across all ten predictions for this drug are similarly high (99.4–99.9%), which suggests the score alone does not separate credible candidates from implausible ones.

## Clinical Trial Evidence

Currently no related clinical trials registered. No ClinicalTrials.gov, SANCTR, PACTR or ICTRP entries were found for this prediction.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 35/3.1/0329 | Melflam | Tablet (oral) | Not listed in the registration record supplied |

Essential Medicines List (EML) status was not provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, trial or literature support, and the proposed mechanism is not biologically credible for a GDF5-pathway genetic skeletal dysplasia. The prediction is a model output only (L5) and should not guide clinical use.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (package insert), to confirm the approved indication and obtain warnings and contraindications
- Mechanism of action data (e.g. from DrugBank)
- Any credible preclinical or clinical evidence linking meloxicam to this condition, which is currently absent

**Other predictions for meloxicam:**
Of the ten predictions, the most notable is *rheumatoid factor-positive polyarticular juvenile idiopathic arthritis* (score 99.44%). It has one indirect publication, a Phase 4 registry on NSAID safety in JIA, which may not include meloxicam-specific data. This is rated L4 and "Research Question". Its mechanism is plausible for symptom relief only, not disease modification. It is worth verifying against the SAHPRA label, since the empty original-indication field looks like a data gap. Spondyloarthropathy (rank 6) also has a class-level NSAID rationale, but the listed entity is a genetic susceptibility term rather than a treatable condition.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

