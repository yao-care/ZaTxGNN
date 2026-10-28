---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-23
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
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. Based on known information, ofloxacin is a fluoroquinolone antibacterial that acts on bacterial DNA gyrase and topoisomerase IV. Its use in the infections listed above is recorded in the knowledge graph.

On the available evidence, the link to hyperamylasemia is weak. Hyperamylasemia is a raised blood amylase level, a laboratory finding rather than an infectious disease. No antibacterial mechanism explains how ofloxacin would treat it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it should be read as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/20.1.1/0149 | Ofloxacin 200 mg austell | Tablet (oral) | Indication text not available in the data compiled for this report |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

