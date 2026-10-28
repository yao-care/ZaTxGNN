---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
monitor_inn: "Norfloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-23
description: "Norfloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, typhoid fever and other bacterial infections"
---

# Norfloxacin
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

## Norfloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic used for infections such as urinary tract infection, typhoid fever, bronchitis and diarrhoeal disease. The TxGNN model (deep learning) predicts it may be useful for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction, so it remains a model-only signal. The score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, typhoid fever and other bacterial infections (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Norfloxacin belongs to the fluoroquinolone class, which is generally known to act by inhibiting bacterial DNA gyrase and topoisomerase IV.

Polyclonal hyperviscosity syndrome is driven by elevated serum immunoglobulins, not by a bacterial process. No plausible mechanistic link between norfloxacin and this condition was identified. The high score (0.9970) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not backed by trials or literature.

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

**Contraindication relations recorded in the knowledge graph** (not label text) include:
- Cardiac: long QT syndrome, familial long QT syndrome, torsades de pointes
- Hepatic and renal: liver failure, liver disease, cirrhosis of liver, kidney disease, gallbladder disease
- Neurological and psychiatric: epilepsy, peripheral neuropathy, peripheral nervous system disease, anxiety disorder, psychotic disorder, mental disorder
- Musculoskeletal: tendinitis, rhabdomyolysis, periarthritis
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency
- Haematological: thrombocytopenia, anaemia

**Drug interactions** (100 recorded; the 20 retrieved include these):
- **Major:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion, chlorpropamide
- **Moderate:** antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, and calcium and potassium salts

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/20.1.1/0657 | Utifloxa | Tablet | Not stated in the records compiled |
| Reg. No. 32/20.1.1/0377 | Floxin | Tablet | Not stated in the records compiled |

Both are single-ingredient, valid registrations for oral use. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications on this disease, and no plausible mechanism links an antibacterial DNA gyrase inhibitor to an immunoglobulin-driven hyperviscosity state.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence on norfloxacin in polyclonal hyperviscosity syndrome
- A mechanistic rationale, and mechanism of action data from DrugBank
- SAHPRA Professional Information (warnings and contraindications) to complete safety screening

---

## Other Predictions Reviewed

Nine further predictions were reviewed. None has a supported mechanism or direct clinical evidence.

| Rank | Predicted Disease | Score | Evidence Level | Decision | Comment |
|---|---|---|---|---|---|
| 2 | Hyperamylasaemia | 0.9970 | L5 | Hold | A laboratory finding with no known link to norfloxacin |
| 3 | Congenital analbuminaemia | 0.9967 | L5 | Hold | Genetic albumin synthesis disorder; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 4 | Blood group incompatibility | 0.9955 | L5 | Hold | Alloimmune reaction, no relevant mechanism |
| 5 | Punctate epithelial keratoconjunctivitis | 0.9954 | L5 | Hold | Two case series (PMIDs 12867402, 22959880) concern microsporidial keratoconjunctivitis and do not study norfloxacin. They do not directly address the predicted disease or the drug. |
| 6 | Premalignant haematological system disease | 0.9948 | L5 | Hold | No link or evidence |
| 7 | Diffuse scleroderma | 0.9944 | L5 | Hold | No antifibrotic mechanism, and fluoroquinolones carry tendon and connective tissue safety signals |
| 8 | Monoclonal gammopathy | 0.9942 | L5 | Hold | The one paper (PMID 8834911) reports fluoroquinolone-resistant *E. coli* in cancer patients on prophylaxis, not treatment of the disease |
| 9 | Haematological disease with acquired peripheral neuropathy | 0.9938 | L5 | Hold | Fluoroquinolones carry a peripheral neuropathy warning, so the safety direction is unfavourable |
| 10 | Septicaemic plague | 0.9937 | L5 | Hold | See below |

**Septicaemic plague** is the only biologically plausible candidate, because *Yersinia pestis* is susceptible to fluoroquinolones. The two retrieved papers (PMIDs 10987101, 11057367) are animal and in vitro studies, one on plague prophylaxis combined with vaccine and one on cholera resistance. Neither studies norfloxacin as a treatment for septicaemic plague, so the evidence level is L5 and not higher. Norfloxacin's limited systemic exposure, as it is used mainly for urinary and intestinal infections, makes it a poor fit for bacteraemic disease. Better-established agents are available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

