---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 9
monitor_inn: "Famciclovir"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
last_modified_at: 2026-11-20
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). In South Africa: 6 SAHPRA registrations (6 valid)"
---

# Famciclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Famciclovir: nucleoside analogue antiviral (penciclovir prodrug) → post-infectious neuralgia
{: .text-alpha }

## One-Sentence Summary

Famciclovir is an oral antiviral prodrug of penciclovir that acts against herpesviruses.
The TxGNN model predicts it may be relevant for **post-infectious neuralgia**, but **no clinical trial or publication directly studies famciclovir for this condition**.
The only linked trial (**1 trial**) tests oxycodone rather than famciclovir, so the prediction rests mainly on an indirect rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Post-infectious neuralgia |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 6) |
| Number of SAHPRA Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for famciclovir: "Famciclovir is an orally administered prodrug of the anti-alpha herpes viral agent penciclovir." ([DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761), label version 2026-11-13; accessed 2026-11-19.) From general pharmacology, famciclovir is converted in the body to penciclovir, which inhibits herpesvirus DNA polymerase after activation by viral thymidine kinase.

Post-infectious neuralgia, in practice most often postherpetic neuralgia, is a complication that follows herpes zoster. The plausible link is that early antiviral treatment of acute zoster may reduce the risk or severity of the pain that follows. This is an indirect link through treating the preceding infection, not a demonstrated direct effect on nerve pain. The prediction should therefore be treated as a research question, not an established use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Not applicable | Unknown | 140 | Early oxycodone during acute herpes zoster to prevent postherpetic neuralgia. Famciclovir is not the studied intervention, so this is contextual evidence only. |

No SANCTR or PACTR registrations were identified in the data compiled for this report.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 29/20.2.8/0189 | Famvir | tablet | Valid |
| 30/20.2.8/0277 | Famvir | tablet | Valid |
| 42/20.2.8/0667 | Ciplafam | tablet | Valid |
| 42/20.2.8/0668 | Ciplafam | tablet | Valid |
| 45/20.2.8/1157 | Macleods Famciclovir Tablets 125 Mg | Fct | Valid |

Showing 5 of 6 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status is not available in the data compiled for this report.

## Safety Considerations

- **Drug Interactions**: 84 potential interactions were recorded, none with a severity level assigned. Examples include metformin, glimepiride, rosiglitazone, simvastatin, morphine, prednisone, omeprazole, pantoprazole and vancomycin. Clinical significance has not been graded and needs checking against the Professional Information (PI).

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) are not available in the data compiled for this report. Please refer to the PI for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly examines famciclovir for post-infectious neuralgia, and the only linked trial tests a different drug. The high model score and the indirect antiviral rationale are not enough to support progression.

**To proceed, the following is needed:**
- Studies that directly test famciclovir (or early antiviral therapy) for preventing or treating postherpetic neuralgia
- SAHPRA Professional Information review for warnings, contraindications and renal dose adjustment
- Detailed mechanism of action data
- Assessment of the clinical significance of the recorded drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

