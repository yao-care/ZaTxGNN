---
layout: default
title: Glycine
parent: Model Prediction Only (L5)
nav_order: 246
evidence_level: L5
indication_count: 10
---

# Glycine
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

# Glycine: From Amino Acid Component of Registered Products to Nasal Cavity Disease

## One-Sentence Summary

Glycine is an amino acid that appears in 12 SAHPRA-registered products in South Africa, but the supplied data give no approved indication text for it.
The TxGNN model predicts it may be effective for **nasal cavity disease**, with a very high model score.
The evidence is thin: **1 clinical trial** and **2 publications** were retrieved, and none of them tests glycine for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (the approved indication text is empty for all listed registrations) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Glycine appears as a component in products such as parenteral nutrition, peritoneal dialysis solutions and a topical powder, but no approved indication text was supplied, so a link to the original use cannot be drawn from these data.

The pack notes only a speculative link: glycine may have cytoprotective and anti-inflammatory effects on mucosal cells, which could be relevant to nasal mucosa. Nothing in the retrieved trials or literature supports this. The high score reflects a knowledge-graph prediction only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | PET/CT imaging of a new radiopharmaceutical (18F-FPPRGD2) in cancer patients. It is a diagnostic imaging study and does not test glycine as a treatment (relevance grade C). |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Basic research (bovine) | Veterinary Pathology | Lectin histochemistry of normal and herpesvirus-infected bovine nasal mucosa. It is not a glycine treatment study. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical | Chemical & Pharmaceutical Bulletin | Oligoarginine-polymer mucosal adjuvants for nasal vaccination in mice. It is not a glycine treatment study. |

## South Africa Market Information

Showing 5 of 12 registrations. The supplied data contain no approved indication text for these products.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| G2370 (ACT 101/1965) | Cicatrin Powder 15G | Powder |
| 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion |
| 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial |
| 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion |
| 41/25/0757 | Nutriflex Lipid Peri | Infusion |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. No drug-drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. The one trial is an unrelated imaging study, the two papers are unrelated preclinical work, and no mechanism of action or safety data are available. Glycine is a well-known nutritional and formulation component, but that does not support this new indication.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Approved indication text for the registered products, to define the original use
- Glycine-specific preclinical or clinical evidence in nasal or upper-airway mucosal disease
- A defined route and formulation for nasal use. The registered forms are powder, infusion and vial, and none is a nasal product.
- Dyspepsia (rank 5) is the only other predicted indication with any signal, and that is a single rat study on amino acids. It is a research question, not a candidate for advancement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

