---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 87
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Calcifediol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Not stated in the SAHPRA registration data. The knowledge graph lists…"
---

# Calcifediol
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

# Calcifediol: From Hypercalcaemia and Vitamin D-Related Bone and Mineral Disorders to Obsolete Vitamin D Deficiency

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D3) is the main circulating form of vitamin D. The data compiled for this report list its original indications as hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, hypophosphataemia, rickets, osteomalacia and renal osteodystrophy.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency** (a flagged-obsolete ontology term), with **no clinical trials** and **no publications** supporting this specific prediction.
Evidence is limited to model prediction only (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. The knowledge graph lists hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphataemia, rickets, osteomalacia and renal osteodystrophy |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, calcifediol is the direct circulating precursor of calcitriol (the active hormonal form of vitamin D) and the main marker of vitamin D status. Repletion in vitamin D deficiency is therefore mechanistically plausible.

There is an important caveat. The predicted disease term is flagged as obsolete in the ontology. The very high TxGNN score (0.9999) probably reflects ontology proximity to the drug's existing indications (rickets, osteomalacia) rather than new, independent insight. No trials or literature were available, so this prediction should not be treated as clinical evidence.

### Other Predictions Considered

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Renal tubular acidosis | 99.86% | L5 | Indirect and speculative. Vitamin D metabolites might help secondary bone disease, but there is no evidence that calcifediol corrects the underlying tubular defect. |
| Hereditary hypophosphataemic rickets | 99.76% | L4 | Standard care is phosphate plus active vitamin D (calcitriol or alfacalcidol), or burosumab. Calcifediol may help maintain 25-OH vitamin D sufficiency but is not a primary therapy. |
| Vitamin D-dependent rickets | 99.18% | L4 | The most mechanistically credible. In type 1B (CYP2R1 25-hydroxylase deficiency), calcifediol bypasses the enzyme block. Type 1A (1α-hydroxylase deficiency) would not benefit in the same way, because calcitriol is required. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no literature is available for the top predicted indication. Two publications were identified for lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Overview of rickets types and treatment with vitamin D and its analogues. Indirect evidence for hereditary hypophosphataemic rickets, with no calcifediol-specific efficacy data. |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Case report/Review | J Bone Miner Res | Describes 7 patients from 2 families with vitamin D-dependent rickets type 1B (25-hydroxylase deficiency). Supports biological plausibility but is descriptive, not a controlled study. |

## South Africa Market Information

Both registrations are valid single-ingredient oral capsules. Approved indication text and manufacturer details were not available in the data compiled for this report. Essential Medicines List (EML) status could not be confirmed.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2466 | Complenatal Ff | Capsule | Not available |
| H2062 (ACT 101) | Filibon | Capsule | Not available |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** kidney disease, pyoureter, sarcoidosis, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, nephrolithiasis (including susceptibility caused by SLC26A1), acute urate nephropathy, hyperphosphataemia, hypervitaminosis, arteriosclerosis obliterans. Some of these overlap with the drug's listed indications, which reflects the graph's structure, so they need clinical interpretation against the approved PI.
- **Drug interactions:** 57 interactions were identified, and the main ones are listed below.
  - **Major:** cholecalciferol, calcitriol and burosumab. Combining with other vitamin D agents risks additive hypercalcaemia. Burosumab is a particular concern in X-linked hypophosphataemia.
  - **Moderate:**
    - Thiazide and thiazide-like diuretics (hydrochlorothiazide, bendroflumethiazide, benzthiazide, chlorothiazide, chlorthalidone)
    - Enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butalbital, butabarbital)
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
    - Aluminium hydroxide
    - Topical calcipotriol and calcitriol
    - Digitoxin

Warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on an obsolete ontology term and a model score alone, with no trials or literature. The package insert safety information, which is a blocking gap, is also missing. Of the predictions, vitamin D-dependent rickets type 1B has the strongest mechanistic rationale, but only descriptive evidence.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications and approved indications) for both registered products
- Mechanism of action data (for example from DrugBank)
- Mapping of the obsolete "vitamin D deficiency" term to a current ontology term, and a re-evaluation of the prediction
- Controlled or systematic evidence for calcifediol in vitamin D-dependent rickets type 1B, the most credible candidate
- A monitoring plan for serum calcium, phosphate and 25-OH vitamin D, particularly with renal impairment and with concomitant vitamin D agents or thiazides
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

