---
layout: default
title: Pantothenic Acid
parent: Model Prediction Only (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Pantothenic Acid
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

# Pantothenic Acid: From Vitamin Supplementation in Parenteral Nutrition to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (vitamin B5) is a nutrient used in vitamin infusions and parenteral nutrition (TPN) products in South Africa. The TxGNN model predicts it may be relevant to **congenital prothrombin deficiency**, but this rests on **1 loosely related clinical trial** and **0 publications**. The score is a graph-based prediction with no plausible biological link, so the prediction is not credible on current evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records. Registered products are vitamin infusion and TPN preparations (nutritional supplementation) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pantothenic acid is a precursor of coenzyme A (CoA), which supports energy and lipid metabolism. Its established role is correcting or preventing vitamin deficiency, mainly as part of multivitamin and parenteral nutrition products.

Congenital prothrombin deficiency is an inherited bleeding disorder caused by a shortage of clotting factor II. Pantothenic acid has no known role in prothrombin synthesis or in the vitamin K-dependent carboxylation pathway that activates it. The very high TxGNN score (99.96%) reflects patterns in the knowledge graph, not biological or clinical support. This prediction should be treated as a model artefact unless independent evidence emerges.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Randomised, double-blind, placebo-controlled cross-over study of a multi-ingredient supplement (L-arginine, Pycnogenol, vitamin K2, lipoic acid, B vitamins, folic acid) on endothelial function in mild-to-moderate hypertension. It does not address a clotting factor deficiency (relevance grade C) |

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Nine SAHPRA registrations were found. The five main ones are listed below. The pack contains no approved-indication text for these products, and no Essential Medicines List (EML) information.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. U/22.1.4/200 | Soluvit novum 10ml vials | Injection | Not stated |
| Reg. No. L/24/329 | Dextrose 20% in water 500ml | Infusion | Not stated |
| Exclusion under Section 36 & Section 14 | ITN neonatal TPN 150ml | TPN | Not stated |
| Exclusion under Section 36 & Section 14 | ITN baby 150ml | TPN | Not stated |
| Exclusion under Section 36 & Section 14 | ITN 8811a 1520ml | TPN | Not stated |

All listed products are injectable or parenteral nutrition preparations. Several are compounded TPN products under the Section 36 / Section 14 exclusion, not standard registered products.

---

## Safety Considerations

No drug interactions were found in the queried database. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. The single trial retrieved tests an unrelated multi-ingredient supplement in hypertension, and there is no literature or plausible mechanism linking pantothenic acid to prothrombin deficiency. Safety review against the SAHPRA package insert has also not yet been done.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a credible biological link to the coagulation pathway
- SAHPRA package insert warnings and contraindications for the registered products
- Any human or preclinical study testing pantothenic acid in a prothrombin or coagulation-factor deficiency

**Other predictions in the pack:** Among the other predicted indications, **folic acid deficiency anaemia** (L4) and **uterine inflammatory disease** (L4, one mouse study) are labelled "Research Question". The anaemia trials use multi-nutrient products, so pantothenic acid's own effect cannot be isolated. These are research questions only, not clinical recommendations.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

