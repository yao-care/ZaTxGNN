---
layout: default
title: Tolnaftate
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tolnaftate: predicted new indication Majocchi granuloma (evidence level L5). Approved use: Tinea pedis, tinea corporis…"
---

# Tolnaftate
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

# Tolnaftate: From Tinea Infections to Superficial Mycosis

## One-Sentence Summary

Tolnaftate is a topical antifungal originally used for dermatophyte skin infections such as tinea pedis, tinea corporis and pityriasis versicolor.
The TxGNN model's top-ranked prediction is **Majocchi granuloma**, but it has no supporting studies. The best-supported prediction is **superficial mycosis** (TxGNN score 98.48%), which is essentially its existing approved use, with **15 publications** and **no registered clinical trials** in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, pityriasis versicolor and other dermatophyte infections (the SAHPRA record in the data compiled for this report has no indication text) |
| Predicted New Indication | Majocchi granuloma (rank 1, TxGNN); superficial mycosis (rank 5) is the best-supported prediction |
| TxGNN Prediction Score | 98.59% (Majocchi granuloma); 98.48% (superficial mycosis) |
| Evidence Level | L5 for Majocchi granuloma; L2 for superficial mycosis |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold for Majocchi granuloma; Proceed with Guardrails for superficial mycosis (on-label confirmation) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tolnaftate is a thiocarbamate antifungal that inhibits fungal squalene epoxidase, blocking ergosterol synthesis in dermatophytes. Its efficacy in dermatophyte infections is established, and the target is relevant to related fungal skin conditions.

**Majocchi granuloma (rank 1):** This is a deep follicular dermatophyte infection, usually caused by *Trichophyton rubrum*. Activity against the organism is plausible, but topical tolnaftate penetrates poorly into hair follicles and the dermis, and deep infection generally needs systemic antifungals. The same limitation applies to the related predictions of ectothrix infection, endothrix infection and tinea profunda. The high scores likely reflect similarity to the approved tinea indications rather than new evidence.

**Superficial mycosis (rank 5):** This is essentially the drug's approved use, so it is a confirmation of existing use and not true repurposing.

**Cutaneous candidiasis (rank 3):** Tolnaftate's activity against *Candida* is weak and inconsistent. Azoles or nystatin remain the standard of care.

**Viral and bacterial predictions** (ophthalmic herpes zoster, orbital cellulitis, infectious mononucleosis): there is no plausible mechanistic link, because tolnaftate's target is a fungal enzyme. These are likely graph-based artifacts and are not pursued further.

**Skin disease caused by infection (rank 9):** The signal is driven largely by on-label use. One in vitro study (PMID 32653607) shows tolnaftate inhibits ergosterol production in *Leishmania* sp., which may suggest a research question for cutaneous leishmaniasis, but this is preclinical only.

## Clinical Trial Evidence

Currently no related clinical trials registered. No NCT, SANCTR or PACTR records were found for any of the predicted indications.

## Literature Evidence

Literature for the best-supported prediction (superficial mycosis), prioritised by study design:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1090684](https://pubmed.ncbi.nlm.nih.gov/1090684/) | 1975 | RCT (placebo-controlled) | J Invest Dermatol | Griseofulvin vs tolnaftate vs placebo in topical therapy of superficial dermatophytoses |
| [4619464](https://pubmed.ncbi.nlm.nih.gov/4619464/) | 1974 | RCT (double-blind) | Postgrad Med J | Clotrimazole vs tolnaftate in superficial dermatophytoses |
| [10398626](https://pubmed.ncbi.nlm.nih.gov/10398626/) | 1999 | Systematic review | BMJ | Efficacy and cost-effectiveness of topical treatments for fungal infections of the skin and nails of the feet |
| [1379146](https://pubmed.ncbi.nlm.nih.gov/1379146/) | 1992 | Review | Drugs | Diagnosis and treatment recommendations for superficial fungal infections |
| [778288](https://pubmed.ncbi.nlm.nih.gov/778288/) | 1976 | Review | J Invest Dermatol | Tolnaftate described as a major advance for dermatophytosis |
| [38874607](https://pubmed.ncbi.nlm.nih.gov/38874607/) | 2024 | Review | Dermatologie | Lists tolnaftate among topical antifungals active against dermatophytes |
| [37415917](https://pubmed.ncbi.nlm.nih.gov/37415917/) | 2023 | Review | Drugs Context | Updated review of tinea pedis clinical features and management |
| [32653607](https://pubmed.ncbi.nlm.nih.gov/32653607/) | 2020 | In vitro | Bioorg Chem | Tolnaftate inhibits ergosterol production and cell viability in *Leishmania* sp. |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Randomised comparison | J Int Med Res | Two topical corticosteroid-antimicrobial creams, one containing tolnaftate, gave equivalent responses in infected eczema and cutaneous candidiasis (n=154) |
| [5844107](https://pubmed.ncbi.nlm.nih.gov/5844107/) | 1965 | Clinical study | Am J Dis Child | Tolnaftate in superficial fungal infections |

The randomised studies are small, old, and have limited phase labelling. The cutaneous candidiasis papers are mostly general antifungal reviews or studies of other drugs, so that evidence is indirect.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2331 (Act 101/1965) | Quadriderm | Cream (topical) | Not stated in the data compiled for this report |

Only one valid single-ingredient registration exists. Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Additional notes:
- No drug interactions were found in the data compiled for this report.
- Tolnaftate is not intended for ophthalmic use, which is relevant to any periocular indication.

## Conclusion and Next Steps

**Decision: Hold (Majocchi granuloma and the other deep or non-fungal predictions); Proceed with Guardrails (superficial mycosis, as on-label confirmation only)**

**Rationale:**
- The top TxGNN predictions (Majocchi granuloma, ectothrix and endothrix infection, tinea profunda) have no trials or literature, and topical tolnaftate is unlikely to reach deep or intrafollicular infection. The viral and bacterial predictions have no mechanistic basis. Superficial mycosis is supported by small, older RCTs and reviews but reflects existing use.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications and approved indications), since this is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Confirmation of the Quadriderm formulation, since the product name suggests a multi-ingredient cream, and the Tolnaftate-specific registration status
- For cutaneous candidiasis or leishmaniasis, controlled clinical data beyond the current in vitro and indirect evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

