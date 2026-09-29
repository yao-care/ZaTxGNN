---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Topical Retinoid Products to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (all-trans retinoic acid) is registered in South Africa only in topical products (cream and gels), and the SAHPRA indication text was not captured in the Evidence Pack.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (three topical products registered) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tretinoin is a retinoid, and retinoic acid signalling can modulate T-cell differentiation and inflammatory cytokines. That gives a general immunomodulatory rationale for inflammatory rheumatic conditions.

No supporting link between retinoic acid and rheumatoid nodulosis specifically was provided, and the similarity to the original indication has not been assessed. The high score therefore reflects a pattern in the knowledge graph, not confirmed biology.

Route compatibility is also unresolved. All registered South African products are topical, whereas a joint or systemic inflammatory disease would likely need systemic exposure. Systemic retinoids carry teratogenicity concerns.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Worth Noting

Nine other indications were predicted. Most are juvenile arthritis terms and rare skeletal dysplasias, and none has trials or literature. Two are worth noting:

- **Osteoarthritis** (score 99.44%, evidence level L4, "Research Question"). The 20 retrieved publications are preclinical or genetic, with no clinical trials. Key signals conflict:
  - [36542696](https://pubmed.ncbi.nlm.nih.gov/36542696/) (Sci Transl Med, 2022): ALDH1A2 variants, which affect retinoic acid synthesis, are linked to hand OA. The authors suggest retinoic acid is anti-inflammatory in OA.
  - [37418291](https://pubmed.ncbi.nlm.nih.gov/37418291/) (DNA Cell Biol, 2023): a GWAS-to-drug analysis pointing to retinoic acid metabolism blocking agents to suppress mechanoflammation.
  - [15946654](https://pubmed.ncbi.nlm.nih.gov/15946654/) (Biochem Pharmacol, 2005): retinoic acid blocked cytokine-induced MMP production in human chondrocytes.
  - [40564983](https://pubmed.ncbi.nlm.nih.gov/40564983/) (Int J Mol Sci, 2025): describes *retinoic acid-induced* OA, which suggests possible harm.
  
  The direction of effect is unresolved, and several other retrieved papers are tangential (ADAMTS biology, cartilage imaging, PRP).
- **Quinquaud's folliculitis decalvans** (score 99.30%, L4, Hold). The only publication is a single case report on folliculitis spinulosa decalvans ([27814407](https://pubmed.ncbi.nlm.nih.gov/27814407/), Cutis, 2016). It is a related but distinct entity and the title does not mention tretinoin, so it supports neither efficacy nor safety.

The juvenile idiopathic arthritis entries (ranks 2–4, 6) are overlapping ontology nodes and should not be counted as independent support. Pediatric skeletal safety concerns apply to the JIA entries and to the skeletal dysplasias (pseudoachondroplasia, Hunter-Thompson acromesomelic dysplasia).

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. F/13.12/284 | Airol | Cream |
| Reg. No. 49/13.12/0499 | Treclin Gel | Gel |
| Reg. No. H/13.12/172 | Ilotycin-a | Gel |

The approved indication text and manufacturer are not recorded for these registrations. All three are topical.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature and no mechanistic link, and it rests on a model score alone. The registered products are topical only, and systemic retinoids raise teratogenicity and pediatric skeletal safety concerns.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications). This is a blocking gap for safety screening.
- Mechanism of action data (e.g. from DrugBank) to assess the link to rheumatoid nodulosis.
- A plausible route and exposure rationale, since only topical products are registered locally.
- For osteoarthritis, preclinical work to resolve whether retinoic acid signalling helps or harms before any clinical consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

