---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mupirocin: predicted new indication Pleural empyema (evidence level L5). Approved use: Impetigo, bullous impetigo"
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "cutaneous candidiasis", "vaginal discharge", "exposure keratitis", "leukoplakia of vagina", "non-human animal disease", "staphylococcal scalded skin syndrome", "bacterial vaginosis"]
---

# Mupirocin
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

## Mupirocin: From Impetigo to Pleural Empyema
{: .text-alpha }

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo and bullous impetigo.
The TxGNN model's top-ranked prediction is **pleural empyema**, but **no clinical trials and no publications** support it.
The best-supported of the ten predictions in the data compiled for this report is **staphylococcal scalded skin syndrome (SSSS)**, with **12 publications**, mostly observational.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo, bullous impetigo (the SAHPRA registration carries no indication text) |
| Predicted New Indication | Pleural empyema (rank 1 of 10 predictions) |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

**Other predictions in the data compiled for this report:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 2 | Punctate epithelial keratoconjunctivitis | 99.10% | L5 | Hold |
| 3 | Neurotrophic keratopathy | 98.48% | L5 | Hold |
| 4 | Cutaneous candidiasis | 98.27% | L4 | Research Question |
| 5 | Vaginal discharge | 96.01% | L5 | Hold |
| 6 | Exposure keratitis | 95.89% | L4 | Hold |
| 7 | Leukoplakia of vagina | 95.81% | L5 | Hold |
| 8 | Non-human animal disease | 95.66% | L5 | Hold |
| 9 | Staphylococcal scalded skin syndrome | 95.57% | L3 | Research Question |
| 10 | Bacterial vaginosis | 95.19% | L4 | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Mupirocin is a topical antibacterial that is generally known to inhibit bacterial isoleucyl-tRNA synthetase, with activity against Gram-positive organisms such as *Staphylococcus aureus*. Its efficacy in impetigo is established.

**Pleural empyema (rank 1):** *S. aureus* is a common cause of empyema, so an antibacterial link exists on paper. However, mupirocin is a topical agent with no meaningful systemic or pleural exposure. The link is therefore only a model prediction, and no trials or literature support it.

**Staphylococcal scalded skin syndrome (rank 9, the best-supported):** SSSS is caused by exfoliative toxin-producing *S. aureus*. This is the same pathogenic mechanism as bullous impetigo, which is already an original indication of mupirocin. The data show mupirocin used as adjunctive topical care alongside systemic antibiotics, not as standalone therapy.

**Other predictions:** Most have weak or no plausible mechanistic links. Neurotrophic keratopathy and leukoplakia of vagina are not primarily infectious. Punctate epithelial keratoconjunctivitis is often viral or inflammatory. Bacterial vaginosis is anaerobe-dominated, which mupirocin does not target well. "Non-human animal disease" is a non-specific category that cannot be evaluated.

## Clinical Trial Evidence

Currently no related clinical trials registered for pleural empyema. No clinical trials were found for any of the other nine predicted indications either.

## Literature Evidence

No literature is available for pleural empyema (rank 1). Publications exist for several lower-ranked predictions; the most relevant are listed below.

**Staphylococcal scalded skin syndrome (rank 9)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Comparative clinical study | Clin Cosmet Investig Dermatol | Compared treatment duration, influencing factors and costs of different IV antibiotics combined with 2% mupirocin ointment in paediatric SSSS |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Rev Anti Infect Ther | Treatment of bullous impetigo and SSSS in infants; both arise from staphylococcal exfoliative toxin |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case series | Adv Neonatal Care | SSSS identification and wound care in neonates with MSSA infection |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case report | Dermatopathology (Basel) | SSSS in an adult receiving chemotherapy for leukaemia |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Epidemiological study | J Med Microbiol | Emergence of SSSS from a methicillin-susceptible *S. aureus* clone that is **mupirocin- and fusidic acid-resistant** |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Microbiology study | J Clin Microbiol | *S. aureus* clone resistant to mupirocin and fusidic acid causing mainly skin infections |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Epidemiological study | Pediatr Infect Dis J | Rising SSSS cases caused by ST121 in Houston, Texas |

**Other predictions**

| PMID | Year | Type | Journal | Indication | Key Findings |
|------|-----|------|------|------|---------|
| [1678836](https://pubmed.ncbi.nlm.nih.gov/1678836/) | 1991 | Clinical study (design unclear) | Lancet | Cutaneous candidiasis | Reports efficacy of mupirocin; no abstract available |
| [24021363](https://pubmed.ncbi.nlm.nih.gov/24021363/) | 2013 | Case report | Dermatol Online J | Cutaneous candidiasis | Perianal and periumbilical dermatitis from group G streptococcus in one patient |
| [8222720](https://pubmed.ncbi.nlm.nih.gov/8222720/) | 1993 | In vitro study | Curr Eye Res | Exposure keratitis | Antimicrobial activity of mupirocin and other agents against Gram-positive corneal pathogens, with corneal epithelial toxicity flagged |
| [1815427](https://pubmed.ncbi.nlm.nih.gov/1815427/) | 1991 | Case report | DICP | Bacterial vaginosis | Intravaginal mupirocin eradicated MRSA vaginitis in one patient (a different condition from bacterial vaginosis) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 49/20.1.6/0587 | Supiroban Cream | Cream (topical) | Not available in the data compiled for this report |

Mupirocin is registered as a single-ingredient topical product only. No oral, injectable, intrapleural or ophthalmic formulations are registered, so the route does not match pleural empyema or the ocular predictions. The data compiled for this report do not state Essential Medicines List (EML) status.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** dermatitis is listed as a contraindicated disease.
- **Resistance:** several publications above (PMIDs 30418106 and 28592549) describe mupirocin-resistant *S. aureus* clones, which is relevant to any expanded use.
- **Ocular use:** an in vitro study (PMID 8222720) flagged possible corneal epithelial toxicity, which is a concern for the eye-related predictions.
- **Drug interactions:** the interaction screen returned 100 entries; the 20 shown, such as calcitriol, clotrimazole, vancomycin and triamcinolone, have no severity level assigned, so their clinical significance is unknown.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications, which were not available for this report. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, pleural empyema)

**Rationale:**
- Pleural empyema has no clinical trials or literature, and a topical agent is unlikely to reach the pleural space, so the prediction rests on the model score alone (L5).
- Staphylococcal scalded skin syndrome is the only prediction with clinical-level support (L3, "Research Question"). That support is observational, and mupirocin acts only as an adjunct to systemic antibiotics.

**To proceed, the following is needed:**
- The SAHPRA package insert, to confirm approved indications, warnings and contraindications (a blocking data gap).
- Detailed mechanism of action data from DrugBank.
- For SSSS: controlled comparative data on adjunctive topical mupirocin, and local mupirocin resistance surveillance in South Africa.
- For pleural empyema: evidence of a feasible route of delivery, or a decision to drop this prediction.
- Clinical review of whether the ocular and vaginal predictions merit any further work, given the safety signal and lack of mechanistic fit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

