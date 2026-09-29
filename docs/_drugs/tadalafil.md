---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From PDE5 Inhibitor to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor that is marketed in South Africa under 3 SAHPRA registrations. The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, a rare genetic condition. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Tadalafil is a PDE5 inhibitor, and PDE5 inhibition raises cGMP, which drives vasodilation. Its use in pulmonary arterial hypertension is established.

The mechanistic link to the predicted indication is weak. Ambras syndrome is a genetic disorder caused by a chromosomal position effect on regulation of the *TRPS1* gene. A cGMP-mediated vasodilatory effect is not expected to correct it. The very high score (99.98%) is most likely a knowledge-graph artefact, driven by graph proximity to other hair and rare-disease nodes, and it has no clinical support.

The other top-ranked predictions show the same pattern. Most are hair phenotypes or developmental malformation syndromes, and they include both hypertrichosis and hypotrichosis, which are opposite phenotypes. This suggests the scores reflect a generic hair-phenotype association rather than a real therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For a lower-ranked prediction (migraine disorder, rank 9), one report points toward harm rather than benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 52/7.1.5/0841.837 | Trado 10 | Fct |
| Reg. No. 51/7.1.5/0391 | Tidalis 20 | Fct |
| Reg. No. 41/7.1.5/0645 | Cialis Oad, 2.5Mg | Tablet |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it. The proposed mechanism does not fit a genetic, structural hair disorder. The only related signal in the retrieved literature (tadalafil-associated migraine aura) points toward possible harm. There is no basis to advance this candidate.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Any preclinical or clinical evidence linking PDE5 inhibition to the *TRPS1* or hair follicle pathway in Ambras syndrome
- A review of the other ranked predictions. Kyphoscoliotic heart disease (indirect plausibility via pulmonary hypertension) is the only one with a coherent, if unverified, rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

