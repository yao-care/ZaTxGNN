---
layout: default
title: Soybean Oil
parent: Model Prediction Only (L5)
nav_order: 426
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Soybean Oil: predicted new indication amenorrhea (disease) (evidence level L5). Approved use: Not stated in the SAHPRA registration data (the product is a parenter…"
monitor_inn: "Soybean oil"
predicted_indications: ["amenorrhea (disease)"]
---

# Soybean Oil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Soybean Oil: From Parenteral Nutrition to amenorrhea (disease) (Prediction Only)
{: .text-alpha }

## One-Sentence Summary

Soybean oil is a lipid emulsion used in parenteral nutrition, supplying energy and essential fatty acids such as linoleic acid. The TxGNN model predicts it may be effective for **amenorrhoea**, but there are **no clinical trials and no publications** supporting this prediction. The top-ranked prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (the product is a parenteral nutrition lipid emulsion) |
| Predicted New Indication | Amenorrhoea |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, soybean oil is a parenteral nutrition lipid emulsion and a dietary source of linoleic acid and phytosterols. Its established role is nutritional support, not treatment of a specific disease.

No plausible, evidence-supported link to the hypothalamic-pituitary-ovarian axis, which governs menstruation, was identified in the data compiled for this report. The high TxGNN score (0.9961) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.


---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was found for amenorrhoea. The only prediction with any publications is oesophageal disease (rank 4), shown here for context. None of these studies tests soybean oil as a treatment for oesophageal disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10024108](https://pubmed.ncbi.nlm.nih.gov/10024108/) | 1999 | Clinical study | Annals of Surgery | Perioperative soybean oil emulsion and EPA, and their effect on stress response and immune function after oesophageal cancer surgery |
| [22457418](https://pubmed.ncbi.nlm.nih.gov/22457418/) | 2013 | Clinical/ex vivo study | JPEN | Slow infusion of soybean oil emulsion and its effect on plasma cytokines and T-cell proliferation after oesophagectomy |
| [9646301](https://pubmed.ncbi.nlm.nih.gov/9646301/) | 1998 | Review | Nutrition | n-3 versus n-6 polyunsaturated fatty acids in critical illness, including patients with oesophageal cancer |
| [27716366](https://pubmed.ncbi.nlm.nih.gov/27716366/) | 2016 | Preclinical (rat) | Lipids in Health and Disease | Effect of n-3/n-6 PUFAs on acute reflux oesophagitis |
| [17868414](https://pubmed.ncbi.nlm.nih.gov/17868414/) | 2007 | Preclinical (rat) | Cancer Science | High animal-fat intake altered bile-acid composition and promoted Barrett's oesophagus and adenocarcinoma in a rat reflux model |
| [31795982](https://pubmed.ncbi.nlm.nih.gov/31795982/) | 2019 | Case report | BMC Pulmonary Medicine | Exogenous lipoid pneumonia associated with avocado/soybean unsaponifiables (an adverse event, not a benefit) |
| [105637](https://pubmed.ncbi.nlm.nih.gov/105637/) | 1979 | Clinical report | Am J Hosp Pharm | Essential fatty acid deficiency during fat-free parenteral nutrition (not relevant to the predicted indication) |

The n-6-rich profile of soybean oil may be pro-inflammatory, so the direction of any effect in oesophageal disease is uncertain.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 49/25/0065 | Nutriflex Omega Specialized | Infusion | Not available in the data compiled for this report |

Essential Medicines List (EML) inclusion status could not be confirmed from the data compiled for this report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-drug interaction records were found in the data compiled for this report, and no contraindication edges were identified in the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications for amenorrhoea, and no plausible mechanism was identified. The evidence level is L5, and the safety information needed for screening is missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A mechanistic rationale linking soybean oil or its fatty acids to menstrual function, with supporting preclinical or clinical studies
- Confirmation of route compatibility, since the only registered product is an intravenous infusion
- Reassessment of other predictions only if a credible mechanism emerges. Oesophageal disease (L4, indirect evidence only) would need human trials showing a therapeutic benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

