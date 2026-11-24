---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 234
evidence_level: L5
indication_count: 1
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-24
description: "Fluconazole: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). In South Africa: 83 SAHPRA registrations (65 valid)"
---

# Fluconazole
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

## Fluconazole: Azole antifungal (CYP51 inhibitor) → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fluconazole is an oral azole antifungal. The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** in the data compiled for this report support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 65 of 83; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 83 (valid: 65, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fluconazole: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), label version 2026-04-02; accessed 2026-11-19.) Fluconazole is a member of the azole antifungal class, which generally acts by inhibiting fungal CYP51 (lanosterol 14-alpha-demethylase), a step in fungal ergosterol synthesis.

Punctate epithelial keratoconjunctivitis is most often viral (for example adenoviral) or inflammatory in origin. Fluconazole's antifungal action therefore has no clear relevance to it, and the data provide no supporting mechanism. The high TxGNN score is a model output only. No similarity analysis between the original and predicted indications has been completed, and route compatibility (oral and intravenous products in South Africa versus the likely need for ocular exposure) has not been assessed.

<!-- review:begin za-lic-20261124b-fluconazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "route compatibility (oral capsules in South Africa versus the likely need for ocular exposure)" Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-fluconazole-1 -->

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Fluconazole is currently marketed in South Africa, with valid single-ingredient registrations in oral capsule form. Approved indication text is not recorded in the local data. Essential Medicines List status was not provided in the data.

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 28/20.2.2/0151 | Diflucan | capsule | Valid |
| 36/20.2.2/0261 | Fluzol | capsule | Valid |
| 36/20.2.2/0262 | Rucintix | capsule | Valid |
| 36/20.2.2/0263 | Fluzol | capsule | Valid |
| 36/20.2.2/0265 | Fluconazole unicorn | capsule | Valid |

Showing 5 of 83 registrations (valid registrations first).

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; examples shown):
  - **Major:** chlorpropamide
  - **Moderate:** famotidine, rabeprazole, omeprazole, dexlansoprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, loperamide, aprepitant, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol 3350 with electrolytes
  - **Minor:** amphotericin B, clarithromycin
- **Conditions flagged for caution in the data compiled for this report** (not taken from label text): long QT syndrome, familial long QT syndrome, kidney disease, liver disease, gallbladder disease, pyoureter.

SAHPRA package insert warnings and contraindications have not yet been retrieved. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial or publication addresses punctate epithelial keratoconjunctivitis, and no plausible mechanism is evident. Evidence is at L5 (model prediction only). The safety data from the package insert are also missing.

**To proceed, the following is needed:**
- A literature and trial search specifically for fluconazole (including topical/ocular use) in punctate epithelial keratoconjunctivitis
- A plausible mechanistic rationale, including the likely cause (viral, inflammatory or fungal) in the target population
- Assessment of route compatibility, since only oral and intravenous products are registered
- Retrieval of the SAHPRA package insert warnings and contraindications
- Confirmed mechanism of action data
- A review of QT-prolongation and interaction risks for any intended population

<!-- review:begin za-lic-20261124b-fluconazole-2 -->

> **Review correction (2026-11-24)**: Originally stated: "since only oral capsules are registered" Corrected: the dosage forms or product types described here did not match the SAHPRA registration data as of 2026-11-23 (checked against the product name, dosage form and ingredient fields of every registration compiled for this report). The table under South Africa Market Information lists the registrations. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261124b-fluconazole-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |
| 2026-11-24 | Corrected: "route compatibility (oral capsules in South Africa versus the likely need for ocular exposure)" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-24 | Corrected: "since only oral capsules are registered" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

