---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Threonine: From an Amino Acid Nutrition Ingredient to Gastroparesis

## One-Sentence Summary

Threonine is an essential amino acid. In South Africa it appears as an ingredient in registered products such as parenteral nutrition and peritoneal dialysis solutions, but no approved indication text is recorded for it.
The TxGNN model predicts it may be useful for **gastroparesis**, but there are **0 registered clinical trials** and only **1 publication**, which does not test threonine itself.
This is a model-only signal and not yet a supported lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data; the registered products are mainly nutrition and dialysis solutions |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for threonine. It is a nutritional amino acid that appears in several registered products. No approved indication is recorded, so the link between its original use and gastroparesis cannot be assessed directly.

The one retrieved paper (PMID 28627597) describes disease biology in a rat model of diabetic gastroparesis. It reports gastric smooth muscle cell apoptosis and changes in PI3K-AKT-mTOR and AMPK-mTOR signalling. The title is truncated, so this reading is inferred. The paper does not appear to test threonine.

A speculative link is that amino acids can influence mTOR signalling. No data in this pack show that threonine affects these pathways in gastric smooth muscle. The very high TxGNN score comes from graph-based prediction and should not be read as clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR, PACTR or ICTRP entries were found.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Preclinical animal study (inferred, not verified) | Molecular Medicine Reports | Examined gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR and AMPK-mTOR signalling in diabetic rats with gastroparesis. Threonine does not appear to be tested. |

## South Africa Market Information

There are 13 registrations in total; the five below are the main ones listed. The SAHPRA indication text is not recorded for any of them. EML inclusion status is not available in the data provided.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2370 (ACT 101/1965) | Cicatrin Powder 15G | Powder | Not recorded |
| 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not recorded |
| 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not recorded |
| 38/34/0172 | Extraneal 2L single bag | Infusion | Not recorded |
| 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not recorded |

The ingredient-to-product mapping should be checked. The Adco-ipratropium entry is not an obvious threonine-containing product.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no registered trials, and the single paper covers disease biology without testing threonine. Safety data are missing, so the case cannot move to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDFs)
- Mechanism of action data for threonine (for example from DrugBank)
- The approved indications for the registered products, and confirmation that each registration actually contains threonine
- Evidence that threonine acts on gastric motility or the relevant signalling pathways (mechanistic or preclinical studies)
- Assessment of route compatibility, since the registered forms are powder and infusions and no required route for gastroparesis has been defined

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

