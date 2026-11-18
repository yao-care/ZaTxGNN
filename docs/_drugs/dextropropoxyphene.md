---
layout: default
title: Dextropropoxyphene
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-18
description: "Dextropropoxyphene: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the SAHPRA registration data"
monitor_inn: "DEXTROPROPOXYPHENE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Dextropropoxyphene
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

## Dextropropoxyphene: From Analgesia (Indication Not Recorded) to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Dextropropoxyphene is an opioid-class analgesic registered in South Africa, although the approved indication text is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 4 of 12) |
| Number of SAHPRA Registrations | 12 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Dextropropoxyphene is generally known as a weak mu-opioid agonist, with additional NMDA-antagonist and sodium channel effects.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2, R137C/L), or in some cases GNAS-related signalling. These produce constitutive receptor activity and water retention independent of vasopressin. Opioids can influence vasopressin release centrally, but this would not be expected to affect a receptor-autonomous, constitutively active V2 pathway.

**No established mechanistic link was identified.** The high TxGNN score (0.9946; model rank 3015) is a model-derived prediction, probably from network proximity or shared-gene relationships. No mechanistic or clinical data support it. It should be treated as a hypothesis only.

Dextropropoxyphene has also been withdrawn from several major markets (including the EU and US in 2010) because of cardiotoxicity (QT prolongation, arrhythmia) and overdose risk. The "Marketed" status for South Africa should therefore be verified.

<!-- review:begin za-lic-20261118-dextropropoxyphene-1 -->

> **Review note (2026-11-18)**: The Medicines Control Council resolved at its meeting of 14–15 April 2011 to withdraw all dextropropoxyphene-containing medicines from the South African market because of cardiac safety risks (named products: Distalgesic, Doloxene, Doloxene Co-65, Doxyfene, Lentogesic and Synap Forte), with a three-month transition period (MCC media statement, 3 May 2011). The four registrations in this data that appear only in the Medicine Price Registry and not on the SAHPRA register (Distalgesic E/2.8/0090, Doloxene Plain B0586, Doloxene Co-65 B0584, Lentogesic B1334 (Act 101/1965)) are therefore shown as withdrawn. The SAHPRA medicine register (product table retrieved 2026-11-17) still lists Doxyfene E/2.9/97 and Synap Forte J/2.8/252 as Registered and Lentogesic B1334 and Zomax B0882 as Old Medicine; the overview counts follow the SAHPRA register for those, and no SAHPRA cancellation notice was found for them. Source: [Withdrawal of dextropropoxyphene containing medicines from the South African market (Medicines Control Council media statement, 3 May 2011)](https://www.gov.za/news/media-statements/withdrawal-dextropropoxyphene-containing-medicines-south-african-market-03); [SAHPRA medicine register (medapps product table)](https://medapps.sahpra.org.za:6006/).

<!-- review:end za-lic-20261118-dextropropoxyphene-1 -->

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| B1334 | Lentogesic | capsule | Valid |
| E/2.9/97 | Doxyfene | capsule | Valid |
| J/2.8/252 | Synap Forte | tablet | Valid |
| B0882 | Zomax | capsule | Valid |
| B0586 (ACT 101) | Doloxene Plain | capsule | Withdrawn from the South African market (2011); not on SAHPRA register |

Showing 5 of 12 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) inclusion status is not available in the compiled data.

<!-- review:begin za-lic-20261105-dextropropoxyphene-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status is not available in the compiled data." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 12 registrations for this drug, 8 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-dextropropoxyphene-1 -->

## Safety Considerations

**Knowledge-graph contraindication signals** (from TxGNN/PrimeKG drug-disease edges, not label text). Diseases flagged include:
- **Cardiovascular:** long QT syndrome (including familial), sudden cardiac arrest, hypertension, hypotensive disorder, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
- **Hepatic, renal and pancreatic:** liver failure, liver disease, kidney disease, impaired renal function, pancreatitis, gallbladder disease
- **Respiratory and neurological:** COPD, epilepsy, insomnia
- **Psychiatric:** anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence
- **Haematological and other:** thrombocytopenia, anaemia (including macrocytic), haemophilia, peptic ulcer disease, gout, pyoureter

**Drug interactions:** 100 interactions were found in total; the first 20 are summarised below.
- **Major:** alvimopan, bupropion, morphine, dolasetron, dronabinol, eliglustat
- **Moderate:** famotidine, hyoscyamine, loperamide, atropine, lorcaserin, bisacodyl, glycopyrronium, chlorpropamide, cimetidine, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), dicyclomine, eluxadoline

For label-based warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature or mechanistic support (Evidence Level L5), and the proposed biology (constitutively active V2 receptor) does not fit an opioid's pharmacology. The drug's cardiotoxicity profile and its withdrawal in major markets add significant safety concerns.

**To proceed, the following is needed:**
- Verification of current SAHPRA registration status and the approved indications of Doxyfene and Lentogesic
- Download and review of the SAHPRA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) and a plausible mechanistic link to NSIAD
- Preclinical or in vitro evidence of any effect on the V2 receptor or its downstream signalling
- A cardiac safety assessment (QT/arrhythmia risk) before any further consideration

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both registrations are valid single-ingredient products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-18 | Annotated: MCC 2011 resolution withdrawing all dextropropoxyphene medicines from the South African market | Annotated | [Withdrawal of dextropropoxyphene containing medicines from the South African market (Medicines Control Council media statement, 3 May 2011)](https://www.gov.za/news/media-statements/withdrawal-dextropropoxyphene-containing-medicines-south-african-market-03); [SAHPRA medicine register (medapps product table)](https://medapps.sahpra.org.za:6006/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

