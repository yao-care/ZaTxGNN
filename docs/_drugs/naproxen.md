---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 335
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From NSAID Pain and Inflammation Relief to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a widely marketed non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation. The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation. There are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA registration data. Naproxen is generally used as an NSAID for pain and inflammation (general knowledge). |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% (model rank 3482) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Naproxen is generally known as a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin production. This is general knowledge, not taken from the supplied data.

Brachydactyly-syndactyly syndrome is a rare congenital malformation driven by developmental limb-patterning pathways. Naproxen has no established link to these pathways. The high score most likely reflects proximity in the knowledge graph (for example, shared gene or phenotype neighbours) rather than a plausible pharmacological effect. At most, an NSAID could relieve pain or inflammation symptomatically. It would not modify the disease, and no clinical evidence supports even that.

The same pattern appears in the other top predictions for this drug: colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.22%), acromesomelic dysplasia, Hunter-Thompson type (99.17%), and brachyolmia-amelogenesis imperfecta syndrome (99.06%). All are ultra-rare genetic malformation syndromes with no trials or publications, and all are likely knowledge-graph artefacts.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Six SAHPRA registrations are recorded, but only five are itemised in the supplied data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. X/3.1/156 | Adco-naproxen | Tablet | Not listed in supplied data |
| Reg. No. 31/2.7/0145 | Aleve | Tablet | Not listed in supplied data |
| Reg. No. 28/3.1/0038 | Napinflam | Tablet | Not listed in supplied data |
| Reg. No. 28/3.1/0044 | Naproscript | Tablet | Not listed in supplied data |
| Reg. No. 45/3.1/0179 | Vimovo 500/20mg | Tablet | Not listed in supplied data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and no plausible mechanistic link between COX inhibition and a developmental limb malformation. At this stage the evidence does not justify further investment.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications) for the registered naproxen products
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- A biological rationale connecting naproxen to the disease pathway, plus any preclinical or case-level evidence
- Route compatibility and similarity-to-original-indication assessments, both currently pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

