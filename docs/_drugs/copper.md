---
layout: default
title: Copper
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Copper
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

# Copper: From Trace Element Supplementation in Parenteral Nutrition to Esotropia

## One-Sentence Summary

Copper is a trace element found in South African parenteral nutrition products (such as Peditrace and Nutryelt). The registration records supplied do not state an approved indication, so the original use is inferred from the product types. The TxGNN model predicts it may be effective for **Esotropia** (a strabismus disorder), but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; inferred as trace element supplementation from the parenteral nutrition products |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 96.25% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for copper. Copper is an essential cofactor for enzymes such as SOD1 (antioxidant defence), lysyl oxidase (collagen cross-linking) and tyrosinase. It is supplied in parenteral nutrition to prevent or correct deficiency.

For esotropia, an inward-turning eye misalignment, no plausible link to copper can be established from the supplied data. Esotropia is mainly a disorder of ocular motor control and binocular vision, and none of copper's known enzymatic roles points to it. The high TxGNN score (96.25%) reflects a pattern in the knowledge graph, not mechanistic or clinical support. It should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered for esotropia. No SANCTR or PACTR entries were retrieved.

## Literature Evidence

Currently no related literature available for esotropia.

## Other Predicted Indications With Retrieved Evidence

Other model predictions have some retrieved records. None shows copper working as a treatment.

| Predicted Indication | Score | Evidence Level | Retrieved Evidence |
|------|------|------|------|
| Dermatitis | 95.06% | L4 | 5 trials and 20 publications. The trials are mostly unrelated or non-therapeutic (a Phase 2 metal patch-test study, NCT02615249, tests copper as an allergen). One Phase 2/3 trial (NCT06726707) was withdrawn with 0 enrolled. The literature is mostly reviews, observational and veterinary studies. It points to copper hypersensitivity, a possible harm. |
| Dry eye syndrome | 93.28% | L4 | 1 trial (withdrawn, 0 enrolled) and 13 publications. These are mainly a preclinical copper-selenide nanoparticle hydrogel, nutrition reviews and Sjögren-related studies. There are no clinical efficacy data for copper itself. |
| Acne keloid | 93.33% | L5 | 1 publication, a 1985 occupational dermatoses survey with no treatment data |
| Bone Paget disease | 92.91% | L5 | 3 preclinical or biochemistry records, none evaluating copper as therapy |
| Acrodermatitis chronica atrophicans, familial hydroa vacciniforme, neonatal dermatomyositis, amyopathic dermatomyositis, childhood connective-tissue-disease interstitial lung disease | 93.3–93.8% | L5 | No trials or literature |

## South Africa Market Information

Five of the 20 registrations are listed below. Approved indication text was not provided in the records, and Essential Medicines List (EML) status is not available in the supplied data.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 29/24/0462 | Peditrace 10ml pdp100010 | Infusion |
| Reg. No. 52/24/0031 | Nutryelt | Infusion |
| Article 21B (N/A) | ITN 7009a 2520ml | TPN |
| Article 21B (N/A) | ITN 2000a 2010ml | TPN |
| Exclusion under Section 36 and Section 14 | ITN8011XA 1520ml adult | TPN |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

One point from the retrieved literature: copper is a recognised contact allergen (see the review "Copper hypersensitivity", PMID [25098945](https://pubmed.ncbi.nlm.nih.gov/25098945/)). Any dermatological repurposing would need to address this risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction rests on the model score alone (L5). There are no trials or publications, and no mechanistic link can be drawn from the data. The safety data needed for further screening are also missing.

**To proceed, the following is needed:**
- SAHPRA Professional Information (package insert) warnings and contraindications, currently a blocking gap
- Mechanism of action data, for example from the DrugBank API
- A documented mechanistic rationale connecting copper to esotropia, followed by a targeted literature search
- Approved indication text for the SAHPRA registrations, to confirm the original indication and EML status
- If a candidate is to be pursued at all, dermatitis and dry eye have more retrieved evidence, but that evidence is indirect and includes hypersensitivity concerns

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

