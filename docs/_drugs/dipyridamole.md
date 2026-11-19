---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 188
evidence_level: L5
indication_count: 6
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cavernous sinus thrombosis", "lateral sinus thrombosis"]
last_modified_at: 2026-11-20
description: "Dipyridamole: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). In South Africa: 5 SAHPRA registrations (3 valid)"
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is an oral antiplatelet medicine that is registered and marketed in South Africa. The TxGNN model predicts it may be useful for **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** currently support this prediction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 3 of 5) |
| Number of SAHPRA Registrations | 5 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dipyridamole: "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), label version 2026-04-29; accessed 2026-11-19.) Dipyridamole is generally known to inhibit platelet aggregation and to have adenosine-related effects. However, no clear mechanistic link to this inherited rhythm disorder of the sinus node was identified.

The adenosine-related effects of dipyridamole could even worsen slow heart rhythms (bradyarrhythmia) in people with sinus node dysfunction. This raises a safety concern rather than supporting benefit. The high TxGNN score therefore reflects a pattern found by the model, not a demonstrated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered. No SANCTR or PACTR entries were found for this prediction either.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| K/8/297 | Plato | tablet | Valid |
| N/8/163 | Plato | tablet | Valid |
| H0535 | Persantin | injection | Valid |
| 27/8/0400 | Persantin 200 Retard | capsule | Not on SAHPRA register; discontinued in MPR |
| 31/8/0641 | Asasantin 200/25 Retard | capsule | Not on SAHPRA register; discontinued in MPR |

<!-- licenses:end -->

No Essential Medicines List information was available in the data compiled for this report.

<!-- review:begin za-lic-20261105-dipyridamole-1 -->

> **Review correction (2026-11-05)**: Originally stated: "This is one registration, status valid, for an oral capsule. No Essential Medicines List information was available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 5 registrations for this drug, 5 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-dipyridamole-1 -->

## Safety Considerations

- **Key warnings and contraindications:** The data compiled for this report contain no SAHPRA package insert warnings or contraindications.
- **Rhythm-specific concern:** The adenosine-related effects of dipyridamole could worsen bradyarrhythmia in sinus node dysfunction. This is the most relevant concern for the predicted use.
- **Conditions flagged in the compiled data (not label text):** hypotensive disorders, thrombocytopenia, peptic ulcer disease, haemophilia, and liver, kidney and gallbladder disease. Check these against the approved Professional Information (PI).
- **Drug interactions:** 100 interactions were recorded.
  - Moderate severity: dexfenfluramine, sibutramine and fenfluramine.
  - Severity not classified: among others, acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, lansoprazole, metformin, glimepiride, morphine, simvastatin and prednisone.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high (0.9989), but there are no trials or publications, and no plausible mechanism was identified. The adenosine-related effects could be harmful in sinus node dysfunction, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for dipyridamole and a clear pharmacological rationale for sinus node disease.
- Preclinical or clinical evidence that directly studies this condition.
- The SAHPRA package insert (warnings and contraindications) to complete safety screening.
- A cardiac safety assessment, with particular attention to bradyarrhythmia and conduction effects.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "This is one registration, status valid, for an oral capsule" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data are not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

