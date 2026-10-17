---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "bacitracin"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical antibiotic, originally used for ophthalmic bacterial infections: keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis (from the TxGNN knowledge graph; the SAHPRA registration carries no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Bacitracin is known as an antibacterial peptide that is active mainly against Gram-positive bacteria such as Staphylococcus. Its use in bacterial infections of the eye is established.

The predicted indication is close to the original ones in the knowledge graph, which probably explains the very high score. However, punctate epithelial keratoconjunctivitis is frequently viral or non-infectious, and an antibacterial would not be expected to address those causes. Bacitracin could only plausibly help where there is a bacterial component or secondary infection.

The score therefore reflects proximity to existing indications, not demonstrated benefit.

### Other Predictions Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Exposure keratitis | 99.991% | L5 | Caused by corneal drying. An antibiotic may prevent secondary infection, but there is no evidence it treats the underlying condition. |
| 4 | Otitis externa | 99.969% | L4 | Only indirect or dated literature. Bacitracin does not cover *Pseudomonas aeruginosa*, the principal pathogen. |
| 3, 5, 6, 8 | Non-human animal disease; postinfectious vasculitis; post-bacterial disorder; post-infectious syndrome | 99.968%–99.970% | L5 | Non-specific or immune-mediated categories with no plausible mechanism. They are likely knowledge-graph artefacts. |
| 7 | Infective urethral stricture | 99.965% | L5 | A fibrotic, structural condition. Parenteral bacitracin was withdrawn for nephrotoxicity. |
| 9 | Infection-related haemolytic uraemic syndrome | 99.962% | L5 | Toxin-mediated. Antibiotics are generally avoided in STEC infection, and systemic bacitracin is nephrotoxic. |
| 10 | Chagas cardiomyopathy | 99.961% | L5 | Protozoal cause. Bacitracin has no known antiprotozoal activity. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No publications are available for the top-ranked prediction. The only literature in the data relates to the fourth-ranked prediction, otitis externa. It is shown here for completeness and does not support the primary prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Clinical comparison (possibly a controlled trial) | Eur Arch Otorhinolaryngol | 151 patients with acute bacterial otitis externa were randomised to a polymyxin B + bacitracin ointment with or without hydrocortisone acetate. This is a combination product, so bacitracin-specific efficacy cannot be separated out. |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In vitro study (veterinary) | Zentralbl Veterinarmed B | Antibiotic susceptibility of 46 bacterial isolates from chronic canine otitis externa, showing increased resistance compared with earlier reports. Not human data. |
| [14055264](https://pubmed.ncbi.nlm.nih.gov/14055264/) | 1963 | Review / practice article | Md State Med J | Practical treatment of otitis externa. No abstract available. |
| [14048629](https://pubmed.ncbi.nlm.nih.gov/14048629/) | 1963 | Clinical report (historical, combination product) | Z Laryngol Rhinol Otol | Local treatment of inflammatory, secretory ear conditions with a combination product. No abstract available. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2370 (Act 101/1965) | Cicatrin Powder 15G | Powder | Not available in the data compiled for this report |

Status: valid, single-ingredient product. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** The TxGNN knowledge graph links bacitracin to a large number of conditions as contraindications. These are model-derived associations and must be verified against the Professional Information. Those most relevant to a topical or ophthalmic use include:
- Eye conditions: herpes simplex virus keratitis, viral eye infection, fungal infection of the eye, open-angle glaucoma, ocular hypertension
- Neuromuscular: myasthenia gravis, neuromuscular junction disease
- Renal and hepatic: kidney disease, liver disease
- Others listed: epilepsy, diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, respiratory failure, atrioventricular block, peripheral vascular disease, and skin atrophy

Several of these appear to reflect labelling of other drug classes or of systemic use, so they should be interpreted cautiously.

**Drug interactions:** 84 interactions were identified. The major-level interactions in the data are:
- Aminoglycosides: kanamycin, neomycin, streptomycin
- Deferasirox
- Iodinated contrast agents: diatrizoate, iodipamide, iodixanol, iohexol

Moderate-level interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, exenatide and picosulfuric acid. These are most relevant to systemic exposure, which is limited with topical use.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please consult the PI before any use. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials or publications for punctate epithelial keratoconjunctivitis, and the usual causes are viral or non-infectious, which an antibacterial would not be expected to treat. Bacitracin is already marketed in South Africa, but the available data do not show added benefit.

**To proceed, the following is needed:**
- Review of the SAHPRA package insert for approved indications, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- Evidence on the aetiology of punctate epithelial keratoconjunctivitis and whether a bacterial component exists in which bacitracin could help
- Clinical or observational data on topical bacitracin in this condition
- Confirmation of route and formulation suitability (the registered product is a powder, and ophthalmic suitability is not established in the data)
- Review of the knowledge-graph contraindication signals, particularly those for herpes simplex virus keratitis, viral eye infection, fungal eye infection and glaucoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

