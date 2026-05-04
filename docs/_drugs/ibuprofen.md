---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ibuprofen: From Pain & Inflammation Management to Acromesomelic Dysplasia, Hunter-Thompson Type

---

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), well established for the relief of pain, fever, and inflammation via inhibition of cyclooxygenase (COX) enzymes — though formal approved indication text was not available in this Evidence Pack.
The TxGNN model predicts it may have potential efficacy in **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare skeletal dysplasia caused by GDF5 gene mutations.
However, this prediction is currently supported by **0 clinical trials** and **0 publications**, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain relief, fever reduction, and anti-inflammatory use (NSAID class; formal indication text not available in this Evidence Pack) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 — Model prediction only; no actual studies identified |
| South Africa Market Status | Not registered / Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on well-established pharmacological knowledge, ibuprofen is a non-selective COX-1/COX-2 inhibitor that reduces the synthesis of prostaglandins — particularly PGE₂ — which mediate pain, fever, and inflammation. This anti-inflammatory mechanism is the foundation for evaluating its potential relevance to other conditions.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the **GDF5** gene, which encodes Growth Differentiation Factor 5, a member of the BMP (Bone Morphogenetic Protein) signalling family. The COX-2/PGE₂ pathway is known to participate in bone remodelling and growth plate regulation, and there is theoretical cross-talk between prostaglandin signalling and BMP pathways during skeletal development.

However, the mechanistic link between ibuprofen's COX inhibition and the correction of GDF5 deficiency is extremely tenuous. There is no known mechanism by which reducing prostaglandin synthesis can compensate for absent or dysfunctional GDF5 protein. The repurposing rationale has been assessed at **1 out of 5** for mechanistic plausibility. This prediction most likely reflects indirect network proximity within the TxGNN knowledge graph rather than a clinically actionable mechanistic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ibuprofen in Acromesomelic Dysplasia, Hunter-Thompson Type.

---

## Literature Evidence

Currently no related literature available for Ibuprofen in Acromesomelic Dysplasia, Hunter-Thompson Type.

---

## South Africa Market Information

Ibuprofen (DrugBank ID: DB01050) has **no registered products** in the SAHPRA database at the time of this evidence pack (data cutoff: 2026-04-04). No SAHPRA licence records were retrieved.

> **Note:** This absence of registration data may reflect a gap in the data collection pipeline rather than a true regulatory absence, given that ibuprofen is a globally ubiquitous OTC and prescription NSAID. Healthcare professionals should verify current SAHPRA registration status directly via the [SAHPRA online register](https://www.sahpra.org.za) and check Essential Medicines List (EML) inclusion.

---

## Safety Considerations

Specific safety data — including key warnings, contraindications, and drug-drug interactions — was not available in this Evidence Pack.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Ibuprofen in this Evidence Pack are ultra-rare genetic or developmental disorders with no supporting clinical trials or published literature, and all are rated L5. The top prediction — Acromesomelic Dysplasia, Hunter-Thompson Type — has a mechanistic plausibility score of only 1/5, with no established pathway by which COX inhibition could address the underlying GDF5 deficiency. There is insufficient scientific basis to advance this candidate at this time.

**To proceed, the following would be needed:**

- **Preclinical evidence**: In vitro or animal model studies demonstrating any effect of ibuprofen (or COX inhibition generally) on GDF5 signalling deficiency or skeletal dysplasia phenotype
- **Mechanistic clarification**: A published hypothesis or pathway analysis linking the COX/PGE₂ axis to GDF5/BMP signalling in bone development
- **MOA data gap resolution**: Retrieval of the full DrugBank mechanism-of-action record for ibuprofen to support formal mechanistic analysis
- **Safety data gap resolution**: Download and parse the relevant Professional Information (PI) to complete the safety evaluation (currently Blocking — DG001)
- **SAHPRA registration verification**: Confirm current market status through the SAHPRA register to ensure completeness of regulatory data

> ⚠️ *This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

