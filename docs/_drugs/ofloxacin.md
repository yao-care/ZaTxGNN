---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-20
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections . The local licence text does not state an appro…"
---

# Ofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ofloxacin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial. The TxGNN model (deep learning) predicts it may be useful for **hyperamylasemia** (score 0.9991), but **no clinical trials and no publications** directly study this link, so the prediction rests on the model score alone. The score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (relations recorded in the knowledge graph, e.g. typhoid fever, urinary tract infection, bronchitis, bacterial pneumonia). The local licence text does not state an approved indication. |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 10 of 10; 2 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 10 (valid: 10, of which 2 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ofloxacin: "Ofloxacin exerts its antibacterial activity by inhibiting DNA gyrase, a bacterial topoisomerase. DNA gyrase is an essential enzyme which controls DNA topology and assists in DNA replication, repair, deactivation, and transcription." ([DailyMed: Ofloxacin Otic (ofloxacin) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=42366170-e536-46a1-9735-d76e5820a9de), label version 2026-10-23; accessed 2026-11-19.) Based on known information, ofloxacin is a fluoroquinolone antibacterial that acts on bacterial DNA gyrase and topoisomerase IV. Its use in the infections listed above is recorded in the knowledge graph.

On the available evidence, the link to hyperamylasemia is weak. Hyperamylasemia is a raised blood amylase level, a laboratory finding rather than an infectious disease. No antibacterial mechanism explains how ofloxacin would treat it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it should be read as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 34/20.1.1/0209 | Zanocin 200 Tablets | tablet | Valid |
| 34/20.1.1/0210 | Zanocin 400 Tablets | tablet | Valid |
| 35/20.1.1/0174 | Tafloc | tablet | Valid |
| 35/20.1.1/0175 | Tafloc | tablet | Valid |
| A39/20.1.1/0149 | Ofloxacin 200 mg austell | tablet | Valid |

Showing 5 of 10 registrations (valid registrations first).

<!-- licenses:end -->

This is a single-ingredient product with valid status. Its Essential Medicines List status is not covered by the data compiled for this report.

---

## Safety Considerations

The following information comes from knowledge-graph relations and interaction databases. It is not SAHPRA label text.

- **Contraindication relations recorded in the knowledge graph** (30 conditions in total). Key examples:
  - Cardiac: long QT syndrome (including familial), torsades de pointes.
  - Liver and kidney: liver failure, liver disease, drug-induced liver injury, kidney disease, impaired renal function.
  - Nervous system and muscle: epilepsy, myasthenia gravis, peripheral neuropathy, rhabdomyolysis.
  - Tendon disorders: tendinitis, periarthritis.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency.
  - Blood: thrombocytopenia, leukopenia, anaemia.
  - Gut: *Clostridium difficile* colitis.
- **Drug interactions** (100 recorded; the first 20 reviewed are summarised here):
  - **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone (systemic corticosteroids), bupropion, chlorpropamide.
  - **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, and calcium and potassium salts.

Please refer to the SAHPRA-approved Professional Information (PI) for authoritative safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no supporting trials or publications and no plausible mechanism, and hyperamylasemia is a laboratory finding rather than a treatable infection. The evidence level is L5.

**To proceed, the following is needed:**
- A clear clinical definition of what would be treated, since hyperamylasemia is a finding and not a disease.
- A mechanistic rationale and any direct studies of ofloxacin in this setting.
- The SAHPRA Professional Information (warnings, contraindications and approved indications) for the registered product.
- Mechanism of action data for the drug.
- If the aim is to explore other predictions, the **septicemic plague** prediction (rank 8) is the most biologically plausible, supported by in vitro susceptibility studies and animal models. It remains preclinical (no human trials) and falls close to the existing antibacterial use, so it would be a research question rather than a decision-ready indication.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ofloxacin Otic (ofloxacin) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=42366170-e536-46a1-9735-d76e5820a9de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

