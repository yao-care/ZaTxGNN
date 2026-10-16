---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Moxifloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections"
---

# Moxifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Moxifloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic, originally used for bacterial infections such as streptococcal infection, bacterial pneumonia and peritonitis.
The TxGNN model predicts it may be effective for **hyperamylasemia** (raised serum amylase), but **no clinical trials and no publications** currently support this prediction.
It is a computational signal only, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal infection, bacterial pneumonia, peritonitis, staphylococcal infection, plague and others, per the knowledge-graph indication list; the SAHPRA indication text is not stated for the registered products) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Moxifloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial respiratory, abdominal and plague infections is established.

For hyperamylasemia, **no mechanistic link could be identified**. Hyperamylasemia is a laboratory finding, usually caused by pancreatic, salivary gland or renal conditions. An antibacterial has no known role in lowering serum amylase. The high TxGNN score (rank 236 among all predictions) appears to be a model artefact, not a pharmacological signal.

The other predictions for this drug show the same pattern. Most also have no supporting data, and some point toward safety concerns instead. For example, fluoroquinolones carry a known risk of peripheral neuropathy and dysglycaemia. The one exception is **bubonic plague** (prediction rank 10, score 99.41%). It is a close extension of the existing plague indications and is supported by preclinical studies. It is discussed in the conclusion.

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

- **Contraindications and risk conditions (knowledge-graph associations, not label text):** The drug is linked to the following conditions.
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
- Consideration of re-prioritising **bubonic plague** as the more credible candidate. It has L3 preclinical support from animal and in vitro pharmacodynamic studies and is close to the existing plague indications. It would still need human clinical evidence and a local regulatory review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

