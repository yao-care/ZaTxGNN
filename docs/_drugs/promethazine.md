---
layout: default
title: Promethazine
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Promethazine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Vasomotor rhinitis, allergic rhinitis…"
monitor_inn: "Promethazine"
predicted_indications: ["rosacea conjunctivitis", "recalcitrant atopic dermatitis", "Angelucci syndrome", "acute hemorrhagic conjunctivitis", "chronic follicular conjunctivitis", "parasitic conjunctivitis", "serous conjunctivitis except viral"]
---

# Promethazine
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

## Promethazine: From Allergic Conditions (Rhinitis, Conjunctivitis, Urticaria) to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Promethazine is a first-generation H1 antihistamine, originally used for allergic conditions such as allergic rhinitis, allergic conjunctivitis, urticaria and angioedema.
The TxGNN model gives its highest prediction to **rosacea conjunctivitis**, but **no clinical trials and no publications** were found for this condition, so the prediction rests on the model alone.
The more credible findings are in allergic urticaria and rhinitis, but these are on-label or near-label uses, not true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vasomotor rhinitis, allergic rhinitis, atopic/papillary/vernal conjunctivitis, urticaria, angioedema (the SAHPRA records compiled for this report contain no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 98.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Promethazine is a well-known H1 antihistamine, and its efficacy in histamine-mediated allergic eye, nose and skin conditions is long established. Histamine blockade is the plausible link to the predicted use.

For rosacea conjunctivitis, this link is **weak**. Ocular rosacea is driven mainly by meibomian gland dysfunction, innate immune activation, and microbial or *Demodex* factors, not by histamine. At most, an antihistamine might ease itch, and there is no disease-directed rationale.

The model also ranked other conditions. Some are mechanistically reasonable, while others are not:

| Predicted Condition | Score | Evidence Level | Assessment |
|------|------|------|------|
| Rosacea conjunctivitis | 98.94% | L5 | Weak histamine link; prediction only |
| Allergic urticaria | 98.13% | L4 | Matches the labelled use (on-label/near-label); literature indirect |
| Cold urticaria | 96.87% | L5 | Plausible, but second-generation antihistamines are preferred |
| Rhinitis | 94.16% | L4 | Already a labelled use; no modern efficacy data in this dataset |
| Recalcitrant atopic dermatitis | 93.24% | L5 | Sedation for itch-related sleep loss at most; not disease-modifying |
| Angelucci syndrome | 93.20% | L5 | Rare, poorly defined; indirect extrapolation |
| Acute haemorrhagic conjunctivitis | 92.96% | L5 | Viral cause; weak rationale |
| Chronic follicular conjunctivitis | 92.95% | L5 | Often infectious or toxic; uncertain relevance |
| Parasitic conjunctivitis | 92.95% | L5 | Treat the parasite; antihistamine adjunct only |
| Serous conjunctivitis (non-viral) | 92.95% | L5 | Likely graph proximity; nonspecific category |

Several of the lower-ranked conjunctivitis predictions probably reflect similarity to the allergic conjunctivitis indications already on the original list.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rosacea conjunctivitis. No trials were found for any of the other nine predicted conditions either.

---

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

For the closest conditions with literature, the retrieved items are indirect and none is a controlled efficacy trial:

**Allergic urticaria**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22130869](https://pubmed.ncbi.nlm.nih.gov/22130869/) | 2012 | RCT (healthy volunteers) | Arch Dermatol Res | Compared promethazine, fexofenadine and olopatadine on psychomotor function and histamine-induced wheal and flare; outcomes were sedation and psychomotor effects, not clinical efficacy |
| [26844217](https://pubmed.ncbi.nlm.nih.gov/26844217/) | 2016 | Retrospective audit | Asia Pac Allergy | Anaphylaxis management in an emergency department compared with guidelines |
| [19797416](https://pubmed.ncbi.nlm.nih.gov/19797416/) | 2010 | Case report | Jpn J Clin Oncol | Desensitization to sunitinib hypersensitivity; indirect relevance |
| [1453998](https://pubmed.ncbi.nlm.nih.gov/1453998/) | 1992 | Case series | Med J Aust | Scombroid poisoning in seven patients |

**Rhinitis**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12113215](https://pubmed.ncbi.nlm.nih.gov/12113215/) | 2002 | Review | Clin Allergy Immunol | H1 antihistamines, including promethazine, have antiallergic and anti-inflammatory properties |
| [24791618](https://pubmed.ncbi.nlm.nih.gov/24791618/) | 2014 | RCT | Clin Neurophysiol | Drowsiness and motor responses to repeat doses of promethazine vs loratadine; not efficacy |
| [22130869](https://pubmed.ncbi.nlm.nih.gov/22130869/) | 2012 | RCT (healthy volunteers) | Arch Dermatol Res | As above |
| [568438](https://pubmed.ncbi.nlm.nih.gov/568438/) | 1978 | Clinical review | Ann Allergy | Long-term promethazine use in 40 pre-school children with chronic rhinitis |
| [13593960](https://pubmed.ncbi.nlm.nih.gov/13593960/) | 1958 | Case series | AMA Arch Otolaryngol | 66 patients with secretory otitis media and nasal allergy treated with promethazine |
| [14175878](https://pubmed.ncbi.nlm.nih.gov/14175878/) | 1964 | Review | Can Med Assoc J | Historical overview of allergic rhinitis treatment |

---

## South Africa Market Information

Promethazine is marketed in South Africa with 17 valid single-ingredient registrations and no cancelled ones. The data compiled for this report do not include approved indication text, manufacturers, or Essential Medicines List status. The five registrations below are examples, and the full set is in the SAHPRA register.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 27/2.8/0242 | Goldgesic | Syrup | Not available in the compiled data |
| Reg. No. 27/2.8/0575 | Salterpyn | Syrup | Not available in the compiled data |
| Reg. No. X/2.8/298 | Pynmed Tablets | Tablet | Not available in the compiled data |
| Reg. No. F/2.8/8 | Propain | Tablet | Not available in the compiled data |
| Reg. No. R/5.7.1/155 | Receptozine | Tablet | Not available in the compiled data |

Available forms are syrup, tablet and suspension. No topical or ophthalmic formulation is registered, which matters for any ocular use.

---

## Safety Considerations

**Drug interactions:** 100 interactions were identified in the interaction database. The examples below are those listed in the data compiled for this report.
- **Major:** bupropion, potassium citrate
- **Moderate (examples):** morphine, atropine, hyoscyamine, glycopyrronium, loperamide, epinephrine, clarithromycin, famotidine, metformin, canagliflozin, dapagliflozin, acarbose, alogliptin, albiglutide, chlorpropamide, lorcaserin

Additive anticholinergic and sedative effects are likely with several of these. The literature also notes that promethazine is more sedating than newer antihistamines.

For warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, rosacea conjunctivitis, has only a model score. There are no trials or publications, and the histamine mechanism does not fit the disease.
- The better-supported predictions (allergic urticaria, rhinitis) are already near-label uses. They are research questions at best, with no modern controlled efficacy data in this dataset.

**To proceed, the following is needed:**
- Mechanism of action data for promethazine
- SAHPRA Professional Information, including warnings, contraindications and approved indications
- For rosacea conjunctivitis: a targeted literature search and a clinical rationale, preferably from ophthalmology or dermatology experts
- For urticaria and rhinitis: a review of controlled efficacy data against second-generation antihistamines, weighing sedation and anticholinergic burden
- Confirmation of route compatibility, since no ophthalmic or topical product is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

