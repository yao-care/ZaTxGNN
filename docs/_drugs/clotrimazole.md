---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 3
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis"]
last_modified_at: 2026-10-29
description: "Clotrimazole: predicted new indication acne (evidence level L5). Approved use: Not recorded in the local data"
---

# Clotrimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Clotrimazole: imidazole antifungal → acne
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is a topical azole antifungal that is marketed in South Africa.
The TxGNN model predicts it may be useful for **acne**, with a score of 0.9986.
Evidence is very thin: **1 clinical trial** (a suspended combination-product study) and **no publications** directly address this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acne |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 7 of 7) |
| Number of SAHPRA Registrations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Clotrimazole belongs to the azole antifungal class, which generally works by interfering with fungal ergosterol synthesis. Some anti-inflammatory activity has also been described.

The proposed link is indirect. Yeasts such as *Malassezia* or *Candida* may contribute to acne-like folliculitis, so an antifungal could help in a subset of patients. This is a hypothesis, not an established mechanism for acne vulgaris.

The only trial tests a fixed combination of beclomethasone, gentamicin and clotrimazole. The effect of clotrimazole alone cannot be separated out, and no published results support the idea.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a topical cream combining beclomethasone 0.025%, gentamicin 0.1% and clotrimazole 1% in contaminated dermatosis with bilateral symmetrical lesions. No results are available, and clotrimazole's contribution cannot be isolated. |

No related publications are available for this prediction. No SANCTR or PACTR registrations were identified in the data compiled for this report.

## South Africa Market Information

Clotrimazole is marketed in South Africa, and all of its registered single-ingredient products are currently valid. They are mainly topical creams, plus a kit and vaginal-cream presentations. No registered product text in the data compiled for this report supports use in acne.

## Safety Considerations

- **Drug Interactions:** Interaction screening returned a large number of entries. The following are rated **Major**:
  - fentanyl
  - alfentanil
  - hydrocodone
  - amiodarone

  Many **Moderate** interactions were also listed, including:
  - abemaciclib
  - paclitaxel
  - acalabrutinib
  - nifedipine
  - amlodipine
  - apixaban
  - alprazolam
  - estradiol
  - levonorgestrel
  - norethisterone

  Interactions with Minor ratings include dolutegravir and amphotericin B. The list shown is partial, so check a full interaction reference before any use, especially with systemic or high-exposure use.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only related trial is a suspended study of a three-drug combination with no results. No publications address clotrimazole in acne, so the high model score rests on prediction alone.
- The antifungal mechanism has no established link to typical acne.

**To proceed, the following is needed:**
- A controlled study of clotrimazole alone in a defined acne population, for example fungal (*Malassezia*) folliculitis versus acne vulgaris
- Results or a status update for NCT01244256
- Mechanism-of-action data and a topical safety review from the SAHPRA-approved PI
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

