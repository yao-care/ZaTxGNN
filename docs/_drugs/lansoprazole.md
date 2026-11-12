---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 287
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Lansoprazole
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor, originally used for gastric and duodenal ulcers, gastroesophageal reflux disease, esophagitis and Zollinger-Ellison syndrome.
but there are **no registered clinical trials** and only **1 general review** supporting this direction, so the evidence is limited to model prediction and indirect literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 35 of 37; 8 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 37 (valid: 35, of which 8 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lansoprazole is a proton pump inhibitor that suppresses gastric acid by inhibiting the H+/K+ ATPase of gastric parietal cells. Its efficacy in acid-related disorders is well established.

Duodenogastric (bile) reflux is the backflow of duodenal contents into the stomach. Acid suppression may relieve symptoms of associated gastritis or oesophagitis, but it does not address the underlying bile reflux. The only supporting publication is a general review of PPIs, with no disease-specific data.

Other predicted indications were reviewed in the same way. None showed a distinct repurposing signal:
- The supporting literature is indirect, and several studies use lansoprazole only as a comparator to newer acid blockers.
- **Duodenal obstruction, abnormality of glucagon secretion, acne, smouldering systemic mastocytosis and leather-bottle stomach** have no plausible mechanistic link and no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General update on PPI clinical use and pharmacokinetics. It covers peptic ulcer, H. pylori infection, GERD, NSAID-related lesions and Zollinger-Ellison syndrome, and contains no duodenogastric reflux-specific data. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 31/11.4.3/0034 | Lanzor 15 Mg | capsule | Valid (status not confirmed by SAHPRA) |
| 37/11.4.3/0154 | Aspen lansoprazole | capsule | Valid |
| 37/11.4.3/0155 | Lansoloc | capsule | Valid |
| 37/11.4.3/0237 | Aspen lansoprazole | capsule | Valid |
| 37/11.4.3/0238 | Lansoloc 15 | capsule | Valid |

Showing 5 of 37 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List (EML) status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-lansoprazole-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Both registrations are valid single-ingredient oral products. Essential Medicines List (EML) status is not available in the data compiled for this report." Removed: the number or status of registrations stated here did not match the SAHPRA registration data as of 2026-11-05, after registrations were matched by ingredient. The SAHPRA data list 37 registrations for this drug, 35 valid; the Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-lansoprazole-1 -->

## Safety Considerations

**Contraindications flagged by the knowledge graph** (these are graph associations, not label text, and should be confirmed against the Professional Information): hypertension, long QT syndrome and torsades de pointes, liver failure and liver disease, porphyria, kidney disease, congestive heart failure, osteoporosis, blood coagulation disorders, stroke and cerebrovascular disorders, myocardial infarction, anaemia and haemoglobinopathy, *Clostridium difficile* colitis, necrotising enterocolitis, myasthenia gravis, gallbladder disease and substance abuse/dependence.

**Drug Interactions** (100 interactions recorded; examples from the first 20 shown):
- **Major:** acalabrutinib, atazanavir
- **Moderate:** hydrochlorothiazide, amphotericin B, amikacin, amphetamine, ampicillin, fenofibrate, apalutamide, aprepitant, atorvastatin, bosutinib, brigatinib, bromocriptine
- **Minor:** acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and one general PPI review. Acid suppression does not treat the underlying cause of bile reflux, and no clinical trials exist. Evidence is at level L4, which is insufficient to support repurposing.

**To proceed, the following is needed:**
- Disease-specific clinical studies of lansoprazole in duodenogastric reflux
- SAHPRA Professional Information (warnings, contraindications and approved indications), currently missing and blocking safety screening
- Mechanism of action data from DrugBank
- Confirmation of route and formulation compatibility for the proposed use
- Review of the knowledge-graph contraindication signals against the label

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Both registrations are valid single-ingredient oral products" | Corrected | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

