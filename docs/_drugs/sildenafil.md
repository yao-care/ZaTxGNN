---
layout: default
title: Sildenafil
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From Erectile Dysfunction to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Sildenafil is a PDE5 inhibitor, widely known for treating erectile dysfunction (the SAHPRA data supplied do not state the registered indication). The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** with a high score, but **no clinical trials and no publications** support this prediction, and the biology points the wrong way. Among the model's other predictions, only **genetic alopecia** has early supporting evidence (2 trials, 1 publication).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data supplied (generally erectile dysfunction) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 98.41% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Sildenafil is a phosphodiesterase type 5 (PDE5) inhibitor. It raises intracellular cGMP, which causes vasodilation.

The top prediction is **not convincing**. Ambras syndrome is a rare genetic developmental condition, linked to rearrangements near the *TRPS1* region, with no plausible PDE5 link. Sildenafil has also been reported to promote hair growth, so using it for a hair-excess disorder points in the opposite direction. The high score most likely reflects graph proximity (shared hair-phenotype nodes), not a therapeutic signal.

The same applies to the other high-scoring predictions: hypertrichosis, trichomegaly, congenital malformation syndromes, homozygous familial hypercholesterolaemia and hypoalphalipoproteinaemia. The pack found no clinical evidence and no mechanistic rationale for any of them.

## Clinical Trial Evidence

Currently no related clinical trials registered for Ambras type hypertrichosis universalis congenita.

## Literature Evidence

Currently no related literature available for Ambras type hypertrichosis universalis congenita.

## Other Predicted Indication with Early Evidence: Genetic Alopecia (Rank 9)

This is the only prediction in the pack with supporting studies. Its TxGNN score is lower (75.03%), and its evidence level is L3 (**Research Question**, not a treatment recommendation). The mechanism is plausible: PDE5 inhibition raises cGMP, increases perifollicular blood flow, and may prolong the anagen (growth) phase. This is a minoxidil-like vascular effect.

| Source | Phase / Type | Status | Enrollment | Key Findings |
|------|------|------|------|---------|
| [NCT05369481](https://clinicaltrials.gov/study/NCT05369481) | NA | Unknown | 50 | Topical sildenafil 2% vs topical minoxidil 5% in male androgenetic alopecia. No results available. |
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | Completed | 28 | Sildenafil lipid nanocarrier in alopecia areata (an autoimmune, not genetic, alopecia). Supports feasibility of topical use only. |
| [PMID 30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018, laboratory study | n/a | n/a | Reports a novel hair-growth effect of sildenafil on human hair follicles (*Biochem Biophys Res Commun*). |

These studies are small and early, come mostly from a single site, and mostly use topical formulations. Efficacy versus minoxidil and long-term safety are not established.

## South Africa Market Information

Sildenafil has 4 SAHPRA registrations. Approved indication text and manufacturer are not included in the supplied data.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 42/7.1.5/1071 | Dynafil | Tablet |
| Reg. No. 50/7.1.5/0062 | Lifaned 50 | Film-coated tablet |
| Reg. No. 43/7.1.5/0887 | Avigra | Tablet |
| Reg. No. 45/7.1.5/0874 | Raviag | Tablet |

All registered products are oral. No topical sildenafil product is registered, so any hair-loss use would require a new formulation.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

As general background not drawn from the Evidence Pack: PDE5 inhibitors are contraindicated with nitrates, so the PI must be checked before any use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (Ambras type hypertrichosis universalis congenita) rests on a graph score alone (L5). It has no trials or publications, and sildenafil's hair-promoting effect makes benefit unlikely. Genetic alopecia is the only prediction worth following up, as a research question.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) to complete safety screening
- Mechanism-of-action data from DrugBank
- For genetic alopecia: a larger randomised trial of topical sildenafil against minoxidil with reported results, plus topical safety data
- A topical formulation and route-compatibility assessment, since no topical product is registered in South Africa

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

