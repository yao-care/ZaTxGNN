---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Benzoyl Peroxide
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

# Benzoyl Peroxide: From Acne Vulgaris to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Benzoyl peroxide is a topical agent widely used in anti-acne products. The registration data supplied here does not record an approved indication, so the acne use comes from general pharmacological knowledge.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but **0 clinical trials** and **0 publications** support this prediction. It is a graph-based signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA licence data supplied. Acne vulgaris is inferred from general knowledge (product name "Acneclear") |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.92% (model rank 723) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Benzoyl peroxide is generally known as a topical bactericidal (against *C. acnes*), comedolytic and mildly anti-inflammatory agent. This general knowledge is not drawn from the supplied data.

Inverted follicular keratosis is a benign follicular lesion. No link has been established between benzoyl peroxide's keratolytic or antibacterial action and this condition. The high score most likely reflects a graph association, not a demonstrated biological rationale.

Other candidates in the top 10 have somewhat more context (see "Other Predicted Candidates" below), but none is supported by direct clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 51/13.12/0911 | Deriva Co | Gel (topical) | Not stated in the registration record |
| Reg. No. X/13.12/292 | Acneclear | Cream (topical) | Not stated in the registration record |

---

## Other Predicted Candidates

Only the rank 1 prediction is assessed above. Of the other nine, two have some supporting material, and neither shows benefit for the predicted condition.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 4 | Acne keloid | 99.06% | L4 | Only plausible link: it overlaps with acne, a follicular inflammatory condition. One Phase 1/2 acne trial ([NCT07015931](https://clinicaltrials.gov/study/NCT07015931), n=23, completed) compares retinoids and does not clearly include benzoyl peroxide. Two reviews are indirect ([PMID 21034705](https://pubmed.ncbi.nlm.nih.gov/21034705/), [PMID 39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/)). No trial has tested benzoyl peroxide in this condition. Worth a research question, not a treatment recommendation. |
| 7 | Phototoxic dermatitis | 98.77% | L4 | The only publication ([PMID 25982754](https://pubmed.ncbi.nlm.nih.gov/25982754/), 2015 review) describes contact dermatitis from topical anti-acne drugs. It reports a low potential for phototoxic reactions but more frequent irritant dermatitis. This is a risk signal, not evidence of benefit. |
| 2 | 2-Hydroxyethyl methacrylate sensitization | 99.43% | L5 | Benzoyl peroxide is itself a contact sensitizer, so the association reflects a hazard, not a use. |
| 3, 5, 6, 8, 9, 10 | Acrodermatitis chronica atrophicans, dermatomyositis (neonatal and amyopathic), childhood connective-tissue interstitial lung disease, familial hydroa vacciniforme, neurodermatitis | 97.7–99.2% | L5 | No evidence and no plausible mechanism. Irritation is a concern in several of these (neonatal skin, photosensitive rashes, neurodermatitis). |

---

## Safety Considerations

- **Irritation and sensitization**: A 2015 review notes that irritant contact dermatitis is the more frequent problem with topical anti-acne drugs, including benzoyl peroxide, and that allergic contact sensitization and phototoxic potential are low ([PMID 25982754](https://pubmed.ncbi.nlm.nih.gov/25982754/)).
- **Drug interactions**: No interaction records were found for this drug.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (vulvar inverted follicular keratosis) has no trials, no publications and no plausible mechanism, so the 99.92% score is a graph-based signal only. The PI safety review is also incomplete, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Obtain the SAHPRA package inserts for both registered products (Deriva Co, Acneclear) to confirm approved indications, warnings and contraindications
- Add mechanism of action data from DrugBank (DB09096)
- Run a targeted literature search for benzoyl peroxide in inverted follicular keratosis and related follicular lesions
- Consider acne keloid (rank 4) as a separate research question, since it has the most plausible link to the original acne use, and reassess it with a dedicated evidence review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

