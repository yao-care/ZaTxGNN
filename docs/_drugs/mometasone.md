---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Mometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
monitor_inn: "Mometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Mometasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Mometasone: From Allergic and Inflammatory Conditions to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Mometasone is a potent corticosteroid, marketed in South Africa as topical products (cream, ointment and lotion), nasal sprays and inhalers. The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**. Currently there are **no registered clinical trials** and only **2 case reports**, both indirectly relevant, so this remains a model prediction with little supporting evidence.

<!-- review:begin za-lic-20261124b-mometasone-3 -->

> **Review correction (2026-11-24)**: Originally stated: "marketed in South Africa as a topical cream and as nasal sprays." Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-mometasone-3 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (the drug's known uses are allergic rhinitis, asthma and nasal polyposis by the intranasal route, and allergic skin disorders by the topical route) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 46 of 50) |
| Number of SAHPRA Registrations | 50 (valid: 46) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mometasone: "Mometasone furoate is a corticosteroid demonstrating potent anti-inflammatory activity. The precise mechanism of corticosteroid action on asthma is not known. Inflammation is an important component in the pathogenesis of asthma." ([DailyMed: Asmanex Hfa (mometasone furoate) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0c6d63da-41bc-4894-bead-198e66c848ac), label version 2026-07-07; accessed 2026-11-19.) Mometasone is a synthetic glucocorticoid that acts on the glucocorticoid receptor (NR3C1). It is used intranasally for asthma, allergic rhinitis and nasal polyposis, and topically for allergic skin disorders.

Topical corticosteroids are an established skin-directed therapy for early-stage mycosis fungoides (patch/plaque-stage cutaneous T-cell lymphoma). They act through glucocorticoid receptor-mediated anti-inflammatory and pro-apoptotic effects on skin-infiltrating T cells. This gives a plausible mechanistic link, and the high TxGNN score is consistent with it.

However, no mometasone-specific clinical data are available. The two retrieved papers are only indirectly relevant: one is a pseudolymphoma case treated with tapinarof, and the other is a paediatric mycosis fungoides case report. The Evidence Level of L4 reflects mechanistic plausibility only, not demonstrated efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University. Medical Center) | Refractory cutaneous pseudolymphoma in a 62-year-old woman, which did not respond to mometasone and tacrolimus and was then treated with tapinarof. This does not support mometasone efficacy and concerns a pseudolymphoma, not a true lymphoma. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | Childhood CD8+ CD56+ mycosis fungoides with a cytotoxic immunophenotype, in an 11-year-old boy. It describes the disease and does not evaluate mometasone. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 32/21.5.1/0157 | Nasonex aqueous 140dose | Aqs | Valid |
| 33/21.5.1/0482 | Rinelon aqueous 140dose | Aqs | Valid |
| 34/21.5.1/0344 | Asmanex Twisthaler 400 Μg | inhaler | Valid |
| 46/21.5.1/0490 | Mometasone Clicks Nasal Spray | spray | Valid |
| 46/21.5.1/0491.490 | Zilfone 120dose | spray | Valid |

Showing 5 of 50 registrations (valid registrations first).

<!-- licenses:end -->

The cream, ointment and lotion are the topical formulations relevant to skin-directed therapy. Essential Medicines List (EML) status is not covered in the compiled data.

<!-- review:begin za-lic-20261124b-mometasone-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Only the cream is a topical formulation relevant to skin-directed therapy." Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-mometasone-2 -->

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned only a pharmacological target entry (glucocorticoid receptor, the intended site of action). No specific drug-drug interactions were listed.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (topical corticosteroids in early-stage mycosis fungoides) is plausible, but there are no trials and no mometasone-specific literature. The only publications are two indirectly relevant case reports, so the evidence is insufficient to support progression.

**To proceed, the following is needed:**
- Mometasone-specific clinical data in early-stage mycosis fungoides or cutaneous T-cell lymphoma (trials, series or comparative studies against other topical corticosteroids)
- Safety information from the SAHPRA Professional Information (warnings and contraindications), which is required before safety screening
- Approved indication text for the SAHPRA registrations
- Mechanism of action data from DrugBank
- Assessment of route compatibility, since only the topical cream is relevant to skin lymphoma

<!-- review:begin za-lic-20261124b-mometasone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Approved indication text for the three SAHPRA registrations" Corrected: this next-step item stated a fixed number of registrations that does not match the SAHPRA registration data as of 2026-11-23; the number was removed and the suggested step is unchanged. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-mometasone-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Asmanex Hfa (mometasone furoate) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0c6d63da-41bc-4894-bead-198e66c848ac) |
| 2026-11-24 | Corrected: "Approved indication text for the three SAHPRA registrations" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-24 | Corrected: "Only the cream is a topical formulation relevant to skin-directed therapy." | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-24 | Corrected: "marketed in South Africa as a topical cream and as nasal sprays." | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

