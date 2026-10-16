---
layout: default
title: Histidine
parent: Model Prediction Only (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Histidine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the registration data compiled for this report (markete…"
---

# Histidine
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

# Histidine: From Nutritional Amino Acid Supplementation to Gastroparesis

## One-Sentence Summary

Histidine is an essential amino acid used as a component of parenteral nutrition (infusion) products in South Africa. The TxGNN model predicts it may be effective for **gastroparesis**, but **no clinical trials** and **only 1 indirectly related publication** support this prediction, and that publication does not test histidine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (marketed as an amino acid component of parenteral nutrition and dialysis solutions) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, histidine is a component of amino acid and parenteral nutrition formulations, and it is the metabolic precursor of histamine. Histamine signalling plays a role in gastric function, so a connection to gastric motility is plausible, but it is not supported by direct data.

The only publication linked to this prediction (PMID 42668409) describes gastric amyloid pathology and mucosal denervation in hereditary ATTR amyloidosis. It does not test histidine or show a histidine-related mechanism. The high TxGNN score reflects a graph-based signal and not experimental or clinical confirmation.

Other top-ranked predictions are also weak:
- **Sclerosing cholangitis** (score 99.27%): preclinical studies suggest the histamine axis (mast cell-derived histamine, H1/H2 receptors, histidine decarboxylase) *promotes* biliary damage and fibrosis. Because histidine is the histamine precursor, supplementation could theoretically worsen disease. The direction of effect is uncertain or possibly adverse.
- **Dyspepsia and intestinal obstruction**: only indirect evidence (one small physiological study of amino acids and gastric emptying; a histidine decarboxylase biomarker study).
- **Congenital prothrombin deficiency, familial visceral myopathy, myopathic and unclassified intestinal pseudoobstruction, potassium deficiency, primary aldosteronism**: prediction only, or literature unrelated to histidine as a drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Mechanistic/pathology study (patients and mice) | Amyloid | Gastric amyloid pathology and mucosal denervation in ATTRv amyloidosis; histidine was not studied |

## South Africa Market Information

All nine registrations are single-ingredient-category entries with a valid status. The approved indication text was not available in the data compiled for this report, and Essential Medicines List (EML) status was not available either. The first five registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not available |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not available |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not available |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not available |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not available |

Four further registrations: Numeta G16E (52/25/0740), Smofkabiven (46/32.2/0518), Smofkabiven Peripheral (47/32.2/0036) and Nutriflex lipid special 625ml (41/25/0759). The listing of Adco-ipratropium under histidine should be verified, as it is not an amino acid product.

## Safety Considerations

The data compiled for this report include disease associations from the TxGNN knowledge graph (not label text) that flag possible contraindications or cautions. These should be checked against the approved Professional Information (PI):

- **Renal:** kidney disease, chronic kidney disease, chronic renal failure, end stage renal failure, acute urate nephropathy, nephrolithiasis, nephrocalcinosis
- **Calcium and phosphorus disorders:** hypercalcaemia, humoral hypercalcaemia of malignancy, sarcoidosis, phosphorus metabolism disease
- **Cardiac:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
- **Metabolic:** phenylketonuria and other disorders of phenylalanine metabolism

No drug-drug interaction records were found. Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5 for gastroparesis). There are no clinical trials, and the single linked paper does not involve histidine. For the next-ranked candidate, sclerosing cholangitis, the histamine-axis evidence suggests possible harm rather than benefit.

**To proceed, the following is needed:**
- Mechanism of action data and a documented rationale linking histidine to gastric motility
- Preclinical or clinical studies testing histidine in gastroparesis (including its effect on histamine levels)
- Review of the SAHPRA Professional Information for warnings and contraindications, particularly in renal and metabolic conditions
- Confirmation of approved indications for the registered products
- Assessment of route and formulation suitability, since the registered products are parenteral nutrition infusions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

