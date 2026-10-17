---
layout: default
title: Colchicine
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Colchicine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: Gout"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans", "primary immunodeficiency due to a genetic defect in innate immunity", "sitosterolemia", "Smouldering systemic mastocytosis", "systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia", "hemoglobin H disease", "blepharo-cheilo-odontic syndrome"]
---

# Colchicine
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

# Colchicine: From Gout and Familial Mediterranean Fever to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an established anti-inflammatory drug, originally used for gout and familial Mediterranean fever (FMF).
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria** (the top-ranked prediction), but there are **0 registered clinical trials** and only **2 publications**, both indirect laboratory studies (one on curcumin, one on chloroquine and the pfmdr1 gene).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; familial Mediterranean fever (from the knowledge graph; no approved indication text is available in the SAHPRA registration data) |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Colchicine is generally known as a microtubule polymerisation inhibitor that suppresses neutrophil function and inflammasome-driven inflammation. That is the basis of its efficacy in gout and FMF.

The link to malaria is plausible but indirect. Microtubules are important in the malaria parasite's cell biology, and one retrieved laboratory study showed that another compound (curcumin) disrupts *P. falciparum* microtubules. The second paper concerns the parasite's pfmdr1 transporter, which belongs to the same family of efflux pumps (P-glycoprotein-like) that handle colchicine. Neither paper tested colchicine in malaria, and no human antimalarial efficacy has been shown. Colchicine's narrow therapeutic index is also a concern for any new use.

**Other predictions in the data (all Hold):**
- **Familial Mediterranean fever, autosomal dominant** (score 99.38%, 19 publications, mostly reviews): this is a subtype of colchicine's existing indication, not true repurposing. Colchicine is the established first-line FMF therapy, so it is better reclassified as an existing-indication subtype. The L4 level reflects only the data supplied, not the strength of colchicine evidence in FMF overall.
- **Systemic mastocytosis** (score 98.20%): one observational paper on histamine in FMF, which is not evidence of efficacy.
- **Dermatofibrosarcoma protuberans, primary immunodeficiency (innate immunity defect), sitosterolemia, smouldering systemic mastocytosis, lymphoadenopathic mastocytosis with eosinophilia, haemoglobin H disease and blepharo-cheilo-odontic syndrome**: computational predictions only, with no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro study | PLoS One | Curcumin (not colchicine) disrupts microtubules in *P. falciparum*, suggesting microtubules are a possible parasite target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / cell-based study | Mol Cell Biol | Expression of the parasite pfmdr1 gene in mammalian cells increased susceptibility to chloroquine; relevant to transporter and drug-resistance biology, not colchicine efficacy |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| C665 (ACT 101/1965) | Colchicine houde | Tablet | Not available in the compiled data |
| 41/3.3/0260 | Aspen colchicine ds | Tablet | Not available in the compiled data |
| C0822 (ACT 101) | Aspen colchicine | Tablet | Not available in the compiled data |

All three registrations are valid single-ingredient oral tablets. Essential Medicines List (EML) status is not available in the compiled data.

## Safety Considerations

SAHPRA package insert warnings and contraindications are not available in the data compiled for this report.

- **Contraindications and cautions from the knowledge graph** (drug-disease associations, not label text): liver failure, impaired renal function, haematological disorders (thrombocytopenia, leukopenia, neutropenia, agranulocytosis, aplastic anaemia and congenital neutropenia syndromes), peptic ulcer disease, diarrhoeal disease, muscle disorders (myopathy, rhabdomyolysis), familial periodic paralysis and acute urate nephropathy.
- **Drug interactions** (100 interactions recorded; examples shown):
  - **Major:** clarithromycin, cobicistat, aprepitant, rolapitant, eliglustat, deferiprone, rosuvastatin and simvastatin. Many of these involve CYP3A4 or P-glycoprotein inhibition, which raises colchicine levels, or additive muscle toxicity with statins.
  - **Moderate:** cimetidine, metronidazole, tinidazole, miconazole, chloroquine, ticagrelor, deferasirox, fostamatinib, disulfiram, benznidazole, eluxadoline and strontium-89 chloride.
  - Chloroquine is notable because it is a common antimalarial.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction rests on a computational score alone (L5). There are no trials, and the two papers are indirect laboratory studies that did not test colchicine. Colchicine's narrow therapeutic index and its many major interactions further argue against advancing without stronger evidence.

**To proceed, the following is needed:**
- Direct in vitro data on colchicine activity against *P. falciparum*, including selectivity versus host toxicity
- Detailed mechanism of action data
- SAHPRA package insert warnings and contraindications, and the approved indication text for each registration
- A safety and interaction assessment for the malaria setting, including co-administration with chloroquine and other antimalarials
- Reclassification of the FMF autosomal dominant prediction as an existing-indication subtype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

