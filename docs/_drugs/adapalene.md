---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Adapalene
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

# Adapalene: From Acne Vulgaris to Elevated Plasma Zinc (Likely Model Artifact)

## One-Sentence Summary

Adapalene is a topical retinoid, and acne vulgaris is its established use. The SAHPRA registration records supplied do not state the approved indication.
The TxGNN model's top-ranked prediction is **elevated plasma zinc**, a laboratory finding rather than a treatable disease, and the input contains **0 clinical trials** and **0 publications** for it.
The high score is most likely a knowledge-graph artifact, so this prediction should not be acted on.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records provided (acne vulgaris is the established use, per the evidence pack's rationale) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on general knowledge, adapalene is a selective retinoic acid receptor (RAR-beta/gamma) agonist. It normalises follicular keratinisation and has anti-inflammatory activity in pilosebaceous units. This is the basis of its efficacy in acne vulgaris.

For **elevated plasma zinc**, no plausible mechanism was identified. It is a laboratory abnormality, not a disease with a therapeutic target, and topical adapalene has minimal systemic exposure. The score of 99.51% therefore appears to reflect a knowledge-graph artifact rather than a real therapeutic signal. The prediction should be treated as a modelling curiosity, not a repurposing lead.

### Other Predicted Candidates

The model produced nine further candidates. The table below summarises them; only two (ranks 8 and 9) have any retrieved evidence.

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|---|---|---|---|---|---|
| 2 | Isolated congenital adermatoglyphia | 98.80% | L5 | Hold | Genetic (SMARCAD1); no known retinoid link |
| 3 | Beare-Stevenson cutis gyrata syndrome | 98.78% | L5 | Hold | FGFR2 syndrome; speculative link only |
| 4 | Demodicidosis of sebaceous gland | 95.45% | L5 | Research Question | Plausible via pilosebaceous mechanism; no antiparasitic effect documented |
| 5 | Pyogenic arthritis-pyoderma gangrenosum-acne syndrome | 95.30% | L5 | Research Question | Topical use could at most address the acne lesions |
| 6 | Prolidase deficiency | 89.33% | L5 | Hold | No mechanistic path identified |
| 7 | Drug-induced osteoporosis | 87.21% | L5 | Hold | Systemic retinoids may harm bone; direction of effect uncertain |
| 8 | Seborrheic dermatitis | 86.28% | L4 | Research Question | Plausible mechanism, but all evidence is indirect (acne studies) |
| 9 | Sebaceous gland anomaly | 85.16% | L1 | Proceed with Guardrails | Supported by acne Phase 3 evidence; label-concordant, not a novel signal |
| 10 | Inherited skin tumour | 82.92% | L5 | Hold | Loose chemoprevention rationale; no evidence |

## Clinical Trial Evidence

For the top prediction (elevated plasma zinc): currently no related clinical trials registered.

The trials below were retrieved for the two candidates with evidence. All concern acne vulgaris, not the predicted conditions themselves.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00446043](https://clinicaltrials.gov/study/NCT00446043) | Phase 3 | Completed | 452 | Long-term (12-month) safety and efficacy of adapalene 0.1%/benzoyl peroxide 2.5% gel in acne vulgaris (rank 9; direct adapalene evidence) |
| [NCT02557399](https://clinicaltrials.gov/study/NCT02557399) | Phase 4 | Completed | 350 | Duac (clindamycin/benzoyl peroxide) vs adapalene + clindamycin combination in Japanese facial acne (rank 9; contextual only) |
| [NCT03076320](https://clinicaltrials.gov/study/NCT03076320) | Phase 1/2 | Completed | 82 | Zaxcell vs Effezel (adapalene/benzoyl peroxide) in inflammatory and scarring acne (rank 8; not a seborrheic dermatitis study) |
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | NA | Unknown | 40 | Platelet-rich plasma plus topical retinoids vs topical retinoids alone in acne (rank 8; wrong disease) |
| [NCT05497323](https://clinicaltrials.gov/study/NCT05497323) | Phase 1 | Unknown | 284 | Adjuvant combination cream vs adapalene 0.1% cream in mild-to-moderate acne (rank 8; wrong disease) |

No SANCTR or PACTR identifiers were included in the input.

## Literature Evidence

For the top prediction: currently no related literature available.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39069843](https://pubmed.ncbi.nlm.nih.gov/39069843/) | 2024 | RCT | Ital J Dermatol Venereol | Adapalene 0.3%/benzoyl peroxide 2.5% gel in Korean acne patients, with histopathological and immunohistochemical assessment |
| [25217865](https://pubmed.ncbi.nlm.nih.gov/25217865/) | 2014 | Animal study | J Dermatol Sci | 0.1% adapalene was effective in a non-inflammatory Kyoto Rhino Rat acne model |
| [36102580](https://pubmed.ncbi.nlm.nih.gov/36102580/) | 2022 | Clinical study | J Cosmet Dermatol | Moisturiser (not adapalene) and facial skin lipidome in seborrhoea; not relevant to adapalene |
| [27504089](https://pubmed.ncbi.nlm.nih.gov/27504089/) | 2016 | Case report | Case Rep Dermatol | Localised late-onset Darier's disease; not relevant to adapalene |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/13.11/0162 | Dapta Cream | Cream (topical) | Not stated in the registration record |
| Reg. No. 51/13.12/0911 | Deriva Co | Gel (topical) | Not stated in the registration record |

Essential Medicines List (EML) status could not be determined from the input.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. The drug-interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, elevated plasma zinc, is a laboratory finding with no plausible mechanism and no supporting trials or literature (L5). The only strong evidence (rank 9, Phase 3 in acne) is for adapalene's established acne use, so it is not a repurposing signal.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is currently blocking safety screening.
- Mechanism of action data from DrugBank.
- The approved indication text for both SAHPRA registrations, to confirm the original indication.
- If a repurposing question is pursued, prioritise the "Research Question" candidates (demodicidosis, seborrheic dermatitis, and the acne component of PAPA-like syndrome) rather than the top-scoring but implausible ones.
- Review of the "sebaceous gland anomaly" result against the acne label before making any claim.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

