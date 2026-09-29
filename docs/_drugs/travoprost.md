---
layout: default
title: Travoprost
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a topical prostaglandin F2-alpha (FP receptor) agonist eye drop, used to lower eye pressure in glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **visceral calciphylaxis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma / ocular hypertension (taken from the trial and literature record, because the SAHPRA indication text is blank) |
| Predicted New Indication | Visceral calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, travoprost is a topical prostaglandin FP receptor agonist. Its efficacy in glaucoma is well established, but the record contains no data linking it to visceral calciphylaxis.

**No established mechanistic link supports this prediction.** The high score most likely reflects proximity to vascular terms in the knowledge graph, not a validated biological mechanism. Two further points weaken the case:

- Travoprost is given as eye drops, so systemic exposure is very low. It is unlikely to reach the vessels involved in visceral calciphylaxis at an effective level.
- Visceral calciphylaxis is a systemic vascular calcification disorder, and no preclinical or clinical work connects FP receptor signalling to it.

The other top-ranked predictions (thoracic outlet syndromes, angiodysplasia of the stomach, blue toe syndrome, spontaneous coronary artery dissection, lymphangiectasis and others) are also L5, Hold, and computational only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for visceral calciphylaxis.

**Note on other predictions.** The "vascular disease" prediction (rank 5) lists 15 trials. All of them are glaucoma or ocular hypertension studies, or ocular surface tolerability and conjunctival hyperemia studies. They do not test any vascular therapeutic benefit and appear to be keyword matches, so they are not counted as supporting evidence here.

---

## Literature Evidence

Currently no related literature available for visceral calciphylaxis.

**Note on other predictions.** The 20 publications listed under "vascular disease" are also about glaucoma treatment or conjunctival hyperemia. For "hemangioendothelioma" (rank 10), there is one case report of uveal effusion caused by topical travoprost in a patient with Sturge-Weber syndrome ([PMID 19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/)) and one review of glaucoma in that syndrome ([PMID 21524602](https://pubmed.ncbi.nlm.nih.gov/21524602/)). The case report describes an adverse event, so it is a safety signal, not evidence of benefit.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 51/15.4/0099 | Ocutra Co | Drops | Not provided in the record |
| Reg. No. A40/15.4/0511 | Duotrav 2.5ml | Drops | Not provided in the record |

Both registrations are ophthalmic drops only. There is no systemic formulation on the South African market.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The following adverse-effect signals appear in the collected literature and trials (they are not from the PI):

- **Conjunctival hyperemia** is common with topical prostaglandin analogues. One review reports it in up to 50% of patients on travoprost. A study in healthy African subjects found moderate hyperemia in 15 of 20 (70%) after a single dose ([PMID 17874490](https://pubmed.ncbi.nlm.nih.gov/17874490/)).
- **Iris pigmentation change** has been followed in a dedicated five-year safety study of patients on the branded product ([NCT00047554](https://clinicaltrials.gov/study/NCT00047554)).
- **Uveal effusion** with exudative retinal detachment was reported in a patient with Sturge-Weber syndrome ([PMID 19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/)).

No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trial or publication (L5), no plausible mechanism, and a route mismatch: an eye drop is being proposed for a systemic vascular disease. The trials and literature attached to related predictions are all on-label glaucoma or adverse-effect studies.

**To proceed, the following is needed:**
- SAHPRA package insert warnings, contraindications and approved indication text. This is a blocking gap for safety screening.
- Mechanism of action data, for example from DrugBank.
- A stated biological hypothesis linking FP receptor signalling to calcification or vascular pathology in calciphylaxis, with supporting preclinical data.
- A route and exposure assessment showing whether any formulation could reach the target tissue.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

