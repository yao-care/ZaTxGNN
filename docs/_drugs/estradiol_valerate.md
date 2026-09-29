---
layout: default
title: Estradiol Valerate
parent: Model Prediction Only (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Estradiol Valerate
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

# Estradiol Valerate: From Estrogen Therapy to Symptomatic Fragile X Syndrome in Female Carriers

## One-Sentence Summary

Estradiol valerate is an estrogen medicine, marketed in South Africa in two SAHPRA-registered tablet products. The TxGNN model predicts it may be useful for **symptomatic fragile X syndrome in female carriers**, but **no clinical trials and no publications** currently support this prediction. It is a model-only signal and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data provided (indication text is empty for both registrations) |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carrier |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, estradiol valerate is an estrogen (a prodrug of estradiol) used for hormone replacement. Mechanistically it may be applicable where oestrogen deficiency is part of the disease.

The most plausible link is **fragile X-associated primary ovarian insufficiency (FXPOI)**, which affects some female carriers of the FMR1 premutation. In that setting, estrogen replacement would treat the resulting low oestrogen. This is not the same as treating fragile X syndrome itself. Estrogen would not be expected to act on the underlying genetic disorder or its neurodevelopmental features.

The prediction is unverified. No trials or literature were provided, and the pack rates its similarity to the original indication as pending. The score of 99.94% (model rank 582) reflects knowledge-graph proximity, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B/21.8.1/16 | Progynova | Tablet | Not recorded in the data provided |
| 43/18.8/0591 | Qlaira | Tablet | Not recorded in the data provided |

Both products are oral tablets. Manufacturer details were not supplied, and Essential Medicines List (EML) status could not be assessed from the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials, no literature and no mechanism-of-action data. The only sensible clinical reading, estrogen replacement for FXPOI, is a narrower and different indication from the one predicted.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- A defined target population, for example female FMR1 premutation carriers with FXPOI rather than fragile X syndrome broadly.
- Any clinical or observational evidence for estradiol valerate in that population.

**Other predictions for this drug:**
- **Ovarian dysfunction** (rank 10) is the only other prediction with a plausible therapeutic rationale, since estrogen replacement is established for hypoestrogenic states such as premature ovarian insufficiency. It is staged as a research question. Its one directly relevant Phase 3 trial (NCT02922348) was withdrawn with zero enrolment, and the subpopulation (for example POI vs PCOS) must be defined first.
- **Anovulation** (rank 8) is a concern rather than an opportunity. Estradiol valerate is used experimentally to induce anovulation and cystic ovaries in rodents.
- **Ovarian remnant syndrome and luteoma of pregnancy** (ranks 7 and 9) have no therapeutic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

