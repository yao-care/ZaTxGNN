---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "L-Lysine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated"
monitor_inn: "L-Lysine"
predicted_indications: ["gastroparesis (disease)", "congenital prothrombin deficiency", "obsolete vitamin D deficiency", "dyspepsia", "familial visceral myopathy", "vitamin deficiency disorder", "hypophosphatemic rickets", "renal tubular acidosis", "biotin metabolic disease", "postgastrectomy syndrome"]
---

# L-Lysine
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

# L-Lysine: From an Unspecified Original Indication to Gastroparesis

## One-Sentence Summary

L-Lysine is an essential amino acid. In South Africa it is registered only as a component of parenteral nutrition and infusion products, and no approved indication text is available.
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 publication**, a preclinical stem-cell study that does not evaluate L-Lysine, so this prediction is based on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (the SAHPRA registration records compiled for this report contain no approved indication text) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. L-Lysine is an essential amino acid and a component of parenteral nutrition and infusion products. Its original indication could not be determined from the data compiled for this report.

No credible mechanistic link between L-Lysine and gastroparesis was identified. The only retrieved paper (PMID 29414870) concerns delivery of mesenchymal stem cells from gelatin-alginate hydrogels to the stomach lumen. It does not study L-Lysine. The high score (0.998) is therefore a computational prediction only, and it may reflect proximity in the knowledge graph rather than true biology.

The other top-ranked predictions are also unsupported or only weakly supported:
- **Congenital prothrombin deficiency, hypophosphatemic rickets, dyspepsia, familial visceral myopathy and postgastrectomy syndrome:** no trials or literature. The link to congenital prothrombin deficiency is purely speculative (lysine-analog antifibrinolytics act on a different mechanism).
- **Obsolete vitamin D deficiency:** the ontology term is deprecated, so the prediction may map to a duplicate node.
- **Vitamin deficiency disorder and biotin metabolic disease:** only indirect biochemical relevance (carnitine and biotin pathways), based on animal, in vitro or metabolomics studies. None tests L-Lysine as a treatment.
- **Renal tubular acidosis:** the one paper reports a transient proximal tubulopathy after amino acid infusion. This is a safety signal against this use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical/Biomaterial study | Bioengineering (Basel) | Delivery of mesenchymal stem cells from gelatin-alginate hydrogels to the stomach lumen as a possible gastroparesis therapy. L-Lysine was not evaluated. |

---

## South Africa Market Information

All five registrations are valid single-ingredient licences. No approved indication text is available for any of them. The Essential Medicines List (EML) status of these products could not be determined from the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not available |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not available |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml 3blog1r79sa | Infusion | Not available |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not available |
| Reg. No. 41/25/0759 | Nutriflex lipid special 625ml | TPN | Not available |

---

## Safety Considerations

Package insert warnings and contraindications could not be retrieved. No drug-drug interaction records were found.

- **Contraindication signals from the knowledge graph (not label text):** the TxGNN knowledge graph links L-Lysine to the following conditions, which should be treated as signals to verify, not confirmed contraindications:
  - **Renal and urinary:** kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, nephrolithiasis (including the SLC26A1-related susceptibility form), nephrocalcinosis, acute urate nephropathy, pyoureter
  - **Calcium and phosphorus:** hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - **Cardiac:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
  - **Metabolic:** phenylketonuria, disorder of phenylalanine metabolism
- **Renal signal in the literature:** one case report (PMID 31876733) describes a transient proximal tubulopathy after amino acid perfusion in peptide receptor radionuclide therapy.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a model score alone (Evidence Level L5). There are no clinical trials, the only retrieved paper does not evaluate L-Lysine, and no mechanistic link to gastroparesis was found.
- The safety data are incomplete. The package insert could not be retrieved, and the knowledge graph flags renal, cardiac and metabolic conditions.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking data gap)
- The original approved indication and mechanism of action from SAHPRA and DrugBank
- Any preclinical or clinical evidence that L-Lysine affects gastric motility or gastroparesis
- A review of whether the registered products (which are combination parenteral nutrition or infusion products) could even be used for this purpose
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

