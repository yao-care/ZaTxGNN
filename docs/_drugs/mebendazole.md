---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mebendazole: From Anthelmintic Use to Acne

## One-Sentence Summary

Mebendazole is an oral anthelmintic (anti-worm) medicine. The TxGNN model predicts it may be effective for **acne**, with a very high score of 99.2%. However, there are **0 clinical trials** and **1 publication** (an unrelated case report), so the prediction rests on the model alone and has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data supplied (mebendazole is an anthelmintic) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Mebendazole is a benzimidazole anthelmintic that works by inhibiting tubulin in parasites. This is the basis for its use against worm infections.

Acne is a chronic inflammatory condition of the hair follicle and sebaceous gland. It involves excess sebum, follicular blockage, *Cutibacterium acnes* and inflammation. Inhibition of parasite tubulin has no established link to any of these processes, so we found no credible mechanistic link.

The high TxGNN score (0.992) is a graph-based prediction only. It should not be read as evidence of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report | Am J Trop Med Hyg | Case of proliferative sparganosis (a tapeworm larval infection) in Venezuela. The patient had acne-like skin lesions as part of the infection. It does not study acne vulgaris or mebendazole treatment. |

This is the only publication linked to this prediction. It does not support the acne indication.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 32/12/0538 | Cipex | Tablet | — |
| Reg. No. 27/12/0082 | Adco-wormex | Tablet | — |

Both products are oral tablets. The approved indication text was not included in the data supplied, so it should be checked against the current Professional Information (PI).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction is L5 (model prediction only). There are no trials, no relevant literature and no plausible mechanism. Safety data were also not available in the pack.

**Other predicted indications in the pack:**
Acne is the top-ranked prediction, but it is not the best supported. Of the 10 predictions, the alveolar echinococcosis and *Echinococcus granulosus* infection predictions are the most credible. Both are parasitic diseases in which benzimidazoles already play a recognised role.

| Predicted Indication | TxGNN Score | Evidence Level | Suggested Decision |
|------|------|------|------|
| Alveolar echinococcosis | 94.20% | L3 | Proceed with Guardrails |
| *Echinococcus granulosus* infection | 95.61% | L3 | Research Question |

- **Alveolar echinococcosis:** there is one completed observational study, [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) (50 patients, albendazole follow-up markers). There are also multiple reviews and a comparative study of mebendazole and albendazole. No RCT is available, and the effect of mebendazole is not separated from albendazole.
- **Guardrails for alveolar echinococcosis:** specialist-directed use, therapeutic drug monitoring, liver and blood count monitoring, and long-term follow-up.
- **Cystic echinococcosis (*E. granulosus*):** a 1989 series of 70 patients treated with mebendazole supports the prediction, but no RCT is available.
- **Leishmaniasis (diffuse cutaneous) and *Demodex* infestation:** only a class-level antiparasitic rationale exists, with no supporting studies.
- **Hordeolum, impetigo, botulism (both forms) and Sorsby's fundus dystrophy:** no plausible mechanism.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which block any safety screening (data gap DG001)
- Mechanism of action data from DrugBank (data gap DG002)
- The approved indication text for both registrations
- For the echinococcosis candidates: mebendazole-specific comparative data and a review of local specialist practice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

