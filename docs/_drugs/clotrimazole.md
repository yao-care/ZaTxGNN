---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Clotrimazole
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

# Clotrimazole: From Topical Antifungal Use to Acne

## One-Sentence Summary

Clotrimazole is an azole antifungal, marketed in South Africa as creams and vaginal products.
The TxGNN model predicts it may be effective for **acne**, but only **1 clinical trial** supports this. That trial tested a three-drug combination and is suspended. No publications were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied. Clotrimazole is generally known as a topical and vaginal azole antifungal. |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (the evidence pack labelled it L4, but no study that can be attributed to clotrimazole exists) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Clotrimazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis. It also has weak antibacterial and anti-inflammatory activity.

A fungal contribution to acne is plausible, for example from *Malassezia*, but it is unproven. Acne is mainly driven by sebum, follicular blockage, *Cutibacterium acnes* and inflammation. The very high TxGNN score is a graph-proximity result, and the package contains no mechanistic evidence to back it.

Other predictions in the same run have much stronger support: vulvovaginitis (rank 2, including a completed Phase 3 trial, NCT00755053) and superficial mycosis (rank 9, Phase 2 and randomised comparisons). Both are consistent with clotrimazole's established antifungal use, so they are not novel repurposing. Acne is the weakest of the three.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Fixed combination of beclometasone 0.025% + gentamicin 0.1% + clotrimazole 1% cream (Glenmark) in contaminated dermatosis with bilateral symmetrical lesions. No results available. Any effect cannot be attributed to clotrimazole, and acne as the studied condition is not confirmed. |

No SANCTR or PACTR registrations were identified in the evidence pack.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Seven registrations were found. The five below are the main ones. The approved-indication text is empty in the data supplied. Essential Medicines List (EML) status was not included.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/20.2.2/0419 | Clomaderm | Cream | Not stated in the data supplied |
| Reg. No. 30/20.2.2/0416 | Fungispor | Cream | Not stated in the data supplied |
| Reg. No. 30/20.2.2/0111 | Canesten duopak | Kit | Not stated in the data supplied |
| Reg. No. 27/20.2.2/0285 | Medaspor vag | Vcr (as listed) | Not stated in the data supplied |
| Reg. No. R/13.4.1/38 | Lotriderm | Cream | Not stated in the data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only acne-linked trial tested a suspended combination product, so no effect can be attributed to clotrimazole. There is no literature or mechanistic evidence for acne, and the high TxGNN score alone is not enough to proceed.

**To proceed, the following is needed:**
- SAHPRA Professional Information (package insert) warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Controlled studies of clotrimazole monotherapy in acne, with a clear rationale such as a *Malassezia*-driven subtype.
- Confirmation of the original approved indications from SAHPRA registration data.
- Consider prioritising the label-concordant candidates, vulvovaginitis and superficial mycosis. Both are rated "Proceed with Guardrails" in the pack, although NCT00755053 needs confirmation that clotrimazole is the test arm.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

