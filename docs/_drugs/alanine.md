---
layout: default
title: Alanine
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alanine: predicted new indication Gastroparesis (disease) (evidence level L5). Approved use: Not stated in the registration data compiled for this report (all app…"
monitor_inn: "Alanine"
predicted_indications: ["gastroparesis (disease)", "obsolete vitamin D deficiency", "dyspepsia", "congenital prothrombin deficiency", "hypophosphatemic rickets", "renal tubular acidosis", "sclerosing cholangitis", "potassium deficiency disease", "postmenopausal osteoporosis", "albinism-deafness syndrome"]
---

# Alanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Alanine: From Parenteral Nutrition Amino Acid Component to Gastroparesis

## One-Sentence Summary

Alanine is a non-essential amino acid. In South Africa it is registered only as a component of parenteral nutrition and infusion products.
The TxGNN model predicts it may be useful for **gastroparesis**, but **no clinical trials** and only **3 publications** were retrieved. None of these publications evaluates alanine as a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (all approved indication fields are empty) |
| Predicted New Indication | Gastroparesis (disease) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Alanine is a non-essential amino acid involved in glucose-alanine cycling and hepatic gluconeogenesis. It is supplied as a nutritional component in several parenteral nutrition products.

No credible mechanistic link to gastroparesis could be established from the data compiled for this report. The retrieved literature concerns gastrointestinal and hepatic complications in renal disease and diabetes. It mentions gastroparesis only as a comorbidity and does not address gastric motility or alanine as a therapy.

The high TxGNN score is a graph-based prediction only. It should be treated as a hypothesis, not as supporting evidence.

Other predicted indications were also reviewed. They are dyspepsia, hypophosphataemic rickets, renal tubular acidosis, sclerosing cholangitis, potassium deficiency, postmenopausal osteoporosis, congenital prothrombin deficiency, obsolete vitamin D deficiency and albinism-deafness syndrome. None has trial evidence, and none has a demonstrated therapeutic link to alanine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | Gastrointestinal and hepatic disorders in end-stage renal disease; gastroparesis is more common in chronic renal failure. Alanine is not evaluated. |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Review | Diabetic Medicine | Diabetic hepatosclerosis as a possible microvascular complication of diabetes. Not related to alanine therapy. |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Case report (classified as Review) | Cureus | Glycogen hepatopathy in a type 1 diabetic patient whose history included gastroparesis. Not related to alanine therapy. |

## South Africa Market Information

All nine registrations are valid single-ingredient registrations. No approved indication text is available for any of them, and no Essential Medicines List (EML) status could be determined from the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not available |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not available |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not available |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not available |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion | Not available |

Four more registrations are not listed above: Smofkabiven (46/32.2/0518), Smofkabiven Peripheral (47/32.2/0036), Nutriflex Omega Specialized (49/25/0065) and Nutriflex lipid special 625ml (41/25/0759).

The Adco-ipratropium entry looks inconsistent with an alanine-containing product. Its registration should be verified.

## Safety Considerations

- **Knowledge-graph contraindication signals** (computed from drug-disease links in a knowledge graph, not from label text): kidney disease (including chronic kidney disease and end-stage renal failure), nephrolithiasis and nephrocalcinosis, hypercalcaemia-related conditions, sarcoidosis, heart and cardiovascular disease, ventricular fibrillation, digitalis poisoning, phosphorus metabolism disorders, acute urate nephropathy, and phenylketonuria or other disorders of phenylalanine metabolism. These signals need confirmation against the product labels.
- **Drug interactions**: No interaction records were found.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. There are no clinical trials, and none of the retrieved literature evaluates alanine as a treatment for gastroparesis. The knowledge-graph contraindication signals for renal and cardiac disease, which overlap with the populations that develop gastroparesis, add further caution.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic rationale for gastric motility
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the registered products
- Preclinical or early clinical evidence of alanine in gastroparesis
- Confirmation of the route and formulation: all registrations are parenteral combination nutrition products, and no suitable single-agent product is evident
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

