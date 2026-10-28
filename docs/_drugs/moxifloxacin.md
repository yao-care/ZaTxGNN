---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "MOXIFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "hematopoietic and lymphoid system neoplasm"]
description: "Moxifloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Moxifloxacin
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

## Moxifloxacin: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as streptococcal infection, bacterial pneumonia and peritonitis.
The TxGNN model predicts it may be effective for **hyperamylasemia** (raised serum amylase), but **no clinical trials and no publications** currently support this prediction.
It is a computational signal only, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Moxifloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial respiratory, abdominal and plague infections is established.

For hyperamylasemia, **no mechanistic link could be identified**. Hyperamylasemia is a laboratory finding, usually caused by pancreatic, salivary gland or renal conditions. An antibacterial has no known role in lowering serum amylase. The high TxGNN score (rank 236 among all predictions) appears to be a model artefact, not a pharmacological signal.

The other predictions for this drug show the same pattern. Most also have no supporting data, and some point toward safety concerns instead. For example, fluoroquinolones carry a known risk of peripheral neuropathy and dysglycaemia.

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
| Reg. No. 41/20.1.1/0777 | Numoxx | Tablet (oral) | Not stated in the data compiled |
| Reg. No. 49/20.1.1/0675 | Moxifloxacin 400Mg/250Ml Fresenius | Infusion (injectable) | Not stated in the data compiled |

Both registrations are valid single-ingredient products. No combination products and no cancelled registrations were found. Both oral and intravenous routes are therefore available locally.

---

## Safety Considerations

- **Contraindications and risk conditions (TxGNN model (deep learning) output, not label text):** The drug is linked to the following conditions. These links come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
  - Cardiac: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial ischaemia, coronary artery disease.
  - Neurological and neuromuscular: epilepsy, myasthenia gravis (including adult-onset), neuromuscular junction disease, peripheral neuropathy and other peripheral nervous system disease.
  - Tendon and joint: tendinitis, periarthritis, exostosis.
  - Hepatic: cirrhosis of the liver, drug-induced liver injury.
  - Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis.
  - Metabolic: potassium deficiency disease.
- **Drug interactions:** 100 interactions were identified. Those listed first are:
  - **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, which raise tendon-injury risk), bupropion, and chlorpropamide.
  - **Moderate:** several antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, and calcium and potassium salts. Fluoroquinolones can cause dysglycaemia, so combining them with antidiabetic drugs needs care.

Label warnings from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Hyperamylasemia has a high model score but no trials, no literature and no plausible mechanism, so the evidence level is L5.
- The drug's known safety profile does not support exploring this use without a rationale.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking moxifloxacin to amylase regulation, which is not currently available.
- The SAHPRA package insert (warnings, contraindications and approved indications), which should be obtained and reviewed before any safety screening.
- Detailed mechanism of action data from DrugBank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

