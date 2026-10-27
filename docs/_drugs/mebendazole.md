---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mebendazole: predicted new indication Acne (evidence level L5). Approved use: Enterobiasis, ascaridiasis, trichuriasis"
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)", "leishmaniasis, diffuse cutaneous", "echinococcus granulosus infectious disease", "hordeolum", "alveolar echinococcosis", "inhalational botulism", "toxin-mediated infectious botulism", "impetigo", "Sorsby's fundus dystrophy", "demodicidosis of sebaceous gland"]
---

# Mebendazole
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

## Mebendazole: From Enterobiasis, Ascariasis and Trichuriasis to Acne
{: .text-alpha }

## One-Sentence Summary

Mebendazole is an anthelmintic, originally used to treat intestinal worm infections (enterobiasis, ascaridiasis and trichuriasis).
The TxGNN model's top-ranked prediction is **acne**, but there are **no clinical trials** and only **1 publication** (an unrelated case report) behind it, so this prediction is model-only.
By contrast, the best-supported predicted use is **alveolar echinococcosis** (rank 5), with **20 publications** (mostly reviews, a WHO guideline and observational studies) and no registered trials. Benzimidazoles are already used for this infection, so this is largely confirmation of existing use rather than a new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Enterobiasis, ascaridiasis, trichuriasis (from the knowledge graph; the SAHPRA records compiled for this report contain no indication text) |
| Predicted New Indication | Acne (rank 1 prediction) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

For comparison, the other predictions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Diffuse cutaneous leishmaniasis | 98.38% | L5 | Hold |
| 3 | Echinococcus granulosus infection (cystic echinococcosis) | 95.61% | L4 | Research question |
| 4 | Hordeolum | 94.88% | L5 | Hold |
| 5 | Alveolar echinococcosis | 94.20% | L3 | Research question |
| 6 | Inhalational botulism | 93.82% | L5 | Hold |
| 7 | Toxin-mediated infectious botulism | 93.52% | L5 | Hold |
| 8 | Impetigo | 93.22% | L5 | Hold |
| 9 | Sorsby's fundus dystrophy | 93.13% | L5 | Hold |
| 10 | Demodicidosis of sebaceous gland | 92.99% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, mebendazole is a benzimidazole anthelmintic that binds parasite beta-tubulin, disrupting microtubule formation and glucose uptake in worms. Its efficacy in intestinal nematode infections is established.

**Acne (rank 1):** No credible mechanistic link was identified. The only publication retrieved is a 1982 case report of proliferative sparganosis (a parasitic infection) in Venezuela, in which the patient had acne-like skin lesions. It is unrelated to acne treatment. The high model score is not backed by clinical or mechanistic evidence, and this should be read as a likely artefact of the knowledge-graph prediction.

**Echinococcosis (ranks 3 and 5):** These predictions are biologically plausible. Larval tapeworm stages (*Echinococcus granulosus* and *E. multilocularis*) are susceptible to benzimidazoles that target beta-tubulin. The WHO 1996 guidelines list mebendazole and albendazole as chemotherapy options, alone or around surgery. In alveolar echinococcosis, benzimidazoles are mainly parasitostatic (they halt growth rather than kill), and the parasite can resume growth when treatment stops. One case report describes possible parasitocidal effects after 13 years of continuous mebendazole. In practice, albendazole is generally preferred.

**Other predictions:** For diffuse cutaneous leishmaniasis and demodicidosis, an antiparasitic rationale is conceivable but unsupported by any data provided. For hordeolum and impetigo (bacterial infections), botulism (toxin-mediated) and Sorsby's fundus dystrophy (a genetic macular disease), no plausible mechanistic link to mebendazole is evident.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (acne), nor for any of the other nine predictions, in the data compiled for this report. No SANCTR or PACTR identifiers were available.

---

## Literature Evidence

**Acne (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | First reported case of human proliferative sparganosis in the southern hemisphere, with acne-like skin lesions. Not related to acne treatment or to mebendazole. |

**Best-supported prediction: alveolar echinococcosis (rank 5), selected publications**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8789923](https://pubmed.ncbi.nlm.nih.gov/8789923/) | 1996 | Guideline | Bull World Health Organ | WHO guidance on cystic and alveolar echinococcosis; benzimidazoles (albendazole or mebendazole) are used as chemotherapy alongside surgery and PAIR |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Comparative study | J Antimicrob Chemother | Open-label observational study of 35 patients with alveolar echinococcosis on long-term mebendazole or albendazole, comparing regimens |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Cohort/clinical observation | J Hepatol | Single non-resectable patient treated with mebendazole for 13 years; findings suggest possible parasitocidal effect |
| [15532108](https://pubmed.ncbi.nlm.nih.gov/15532108/) | 2004 | Long-term analysis | J Hepatol | Immunosurveillance within the Swiss chemotherapy trial (1976-2001) of benzimidazoles in alveolar echinococcosis |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Benzimidazoles are the only recommended compounds but are parasitostatic and can cause liver dysfunction |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | Current status of drug therapy for alveolar echinococcosis |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Albendazole and mebendazole, and the search for further options |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Trop | No non-surgical option yet replaces albendazole or mebendazole |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Management of liver echinococcosis; surgery is the cornerstone of treatment |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Pharmacology study | Eur J Clin Pharmacol | Plasma mebendazole concentrations in infected animals and humans; high oral doses only partly effective |

**Cystic echinococcosis (rank 3), key item**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2585032](https://pubmed.ncbi.nlm.nih.gov/2585032/) | 1989 | Clinical study (design unverified) | J Chemother | 70 patients with 150 hydatid cysts treated with mebendazole under WHO protocols; morphological and/or volumetric changes seen in 64.3% of cysts. Follow-up of 6 months to 5 years |

Note: the other retrieved items for ranks 3 and 5 are preclinical studies or concern other agents, and are not listed here. No Phase 2/3 RCT was identified for any prediction.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/12/0538 | Cipex | Tablet (oral) | Not available in the compiled data |
| Reg. No. 27/12/0082 | Adco-wormex | Tablet (oral) | Not available in the compiled data |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report. Neither registration is for acne or echinococcosis based on available information, so any such use would be off-label.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** liver disease and gallbladder disease are flagged. This is consistent with the literature note that benzimidazoles can cause liver dysfunction during prolonged use.
- **Drug Interactions (10 identified, DDInter):**
  - *Moderate:* metronidazole, iodide I-131, iodide I-123, ritonavir, and the anticonvulsants phenobarbital, carbamazepine, fosphenytoin, phenytoin and primidone.
  - *Minor:* cimetidine.

  Enzyme-inducing anticonvulsants are of particular practical relevance in patients needing prolonged or high-dose therapy.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, acne)

**Rationale:**
- The acne prediction rests on model score alone. The only retrieved publication is unrelated, there are no trials, and no mechanistic link is evident (Evidence Level L5).
- Of the ten predictions, only alveolar and cystic echinococcosis have meaningful support (L3 and L4), but these reflect existing use of benzimidazoles rather than a new repurposing opportunity. They are best framed as research questions, for example on parasitocidal activity or improved formulations.

**To proceed, the following is needed:**
- Mechanism of action data and SAHPRA Professional Information (warnings, contraindications and approved indications), which are currently missing
- For acne or other L5 predictions: preclinical or case-level evidence of a plausible mechanism before any further consideration
- For echinococcosis: confirmation of the design and size of the key studies, comparison against current guidance (albendazole generally preferred), and a hepatic monitoring plan
- Confirmation of EML status and the registered indications for Cipex and Adco-wormex
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

