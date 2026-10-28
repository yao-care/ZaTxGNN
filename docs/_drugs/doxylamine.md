---
layout: default
title: Doxylamine
parent: Model Prediction Only (L5)
nav_order: 203
evidence_level: L5
indication_count: 1
monitor_inn: "DOXYLAMINE"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-29
description: "Doxylamine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Doxylamine
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

## Doxylamine: H1-receptor antagonist (antihistamine with anticholinergic activity) → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Doxylamine is a sedating antihistamine with anticholinergic activity that is marketed in South Africa.
The TxGNN model predicts it may be useful for **nasal cavity disease**, with a prediction score of **0.9936**.
No clinical trials or publications were found in the data compiled for this report, so the support is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 11) |
| Number of SAHPRA Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Doxylamine is known as a first-generation H1-receptor antagonist with anticholinergic properties. Blocking histamine H1 receptors and muscarinic receptors can reduce sneezing, rhinorrhoea and nasal secretions, which is a plausible route to symptomatic relief of nasal conditions.

"Nasal cavity disease" is a very broad category. It covers many different conditions, such as allergic, vasomotor and infective rhinitis, and the term is too non-specific to support a defined repurposing hypothesis. The mechanistic argument is therefore indirect and rests on general pharmacology, not on any study of this disease.

No clinical trials or publications were provided that directly study nasal cavity disease, so the evidence level is L5 (model prediction only).

---

## South Africa Market Information

Eleven single-ingredient SAHPRA registrations are currently valid and none are cancelled. The records carry no approved-indication text. Essential Medicines List status is not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 33/7.1.3/0452 | Hypace | Tablet | Not recorded |
| Reg. No. 33/2.8/0098 | Doxy co | Tablet | Not recorded |
| Reg. No. H/10.1/140 | Vicks medinite | Syrup | Not recorded |
| Reg. No. 36/2.8/0271 | Alpha-Dol | Tablet | Not recorded |
| Reg. No. 29/2.6/0182 | Azor | Tablet | Not recorded |

The list shows 5 of the 11 registrations.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Major-level interactions include:
  - Potassium chloride
  - Potassium citrate

  Moderate-level interactions include:
  - Anticholinergics and antispasmodics (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, propantheline)
  - Opioids and antidiarrhoeals (morphine, opium, loperamide, eluxadoline)
  - Cannabinoids (dronabinol, nabilone)
  - Metoclopramide

  These reflect additive anticholinergic and sedative effects, and a risk of gastrointestinal mucosal injury with solid potassium preparations.

- **Conditions of concern**: Conditions listed as of concern for this drug include:
  - Angle-closure glaucoma
  - Benign prostatic hyperplasia and bladder neck obstruction
  - Peptic ulcer disease
  - Liver disease
  - Hyperthyroidism
  - Cardiovascular disease (hypertension, coronary artery disease, ventricular tachycardia)
  - Diabetes
  - Substance abuse or dependence

  These come from a drug-disease relation source and are not taken from approved label text, so they must be checked against the SAHPRA-approved Professional Information (PI).

Please refer to the SAHPRA-approved Professional Information (PI) for formal warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9936), but the predicted indication is very broad, no trials or publications address it, and the supporting reasoning is indirect. The safety review is also incomplete, because the SAHPRA package insert warnings have not been retrieved.

**To proceed, the following is needed:**
- Narrow the hypothesis to a specific nasal condition, such as allergic or vasomotor rhinitis
- Retrieve and review the SAHPRA Professional Information, including approved indications, warnings and contraindications
- Obtain detailed mechanism of action data
- Search for clinical trials and publications that directly study the chosen condition
- Review the interaction and contraindication profile for the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

