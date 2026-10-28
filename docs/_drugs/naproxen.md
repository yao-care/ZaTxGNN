---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 337
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-29
monitor_inn: "NAPROXEN"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Naproxen: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for inflammatory and musculoskeletal conditions such as rheumatoid arthritis, osteoarthritis, gout, bursitis, tendinitis and migraine.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**,
but there are **no clinical trials and no publications** supporting this prediction, so it remains a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 6 of 6) |
| Number of SAHPRA Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Naproxen is generally known as a non-selective COX-1/COX-2 inhibitor, which reduces prostaglandin-mediated inflammation and pain. This general pharmacology is background knowledge and was not part of the supplied record.

Brachydactyly-syndactyly syndromes are congenital limb malformations with developmental or genetic origins. Reducing inflammation through prostaglandin inhibition would not be expected to correct a structural skeletal defect. **No mechanistic link is supported by the available data.**

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between this condition and related diseases, such as the musculoskeletal terms among naproxen's original indications, not biological evidence. Prenatal NSAID exposure is also a safety concern, not a therapeutic rationale.

Other top-ranked predictions show the same pattern (all L5, no trials, no literature, no mechanistic link):

| Rank | Predicted Disease | TxGNN Score |
|------|------|------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 0.9922 |
| 3 | Acromesomelic dysplasia, Hunter-Thompson type | 0.9917 |
| 4 | Brachyolmia-amelogenesis imperfecta syndrome | 0.9906 |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Naproxen is marketed in South Africa with 6 valid single-ingredient registrations. Approved indication text and manufacturer details were not available in the data compiled for this report. Essential Medicines List (EML) status was not available either.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| X/3.1/156 | Adco-naproxen | Tablet |
| 31/2.7/0145 | Aleve | Tablet |
| 28/3.1/0038 | Napinflam | Tablet |
| 28/3.1/0044 | Naproscript | Tablet |
| 45/3.1/0179 | Vimovo 500/20mg | Tablet |
| T/2.2/207 | Dormicum | Injection |

Note: Dormicum is listed under naproxen in the compiled registration data, but it is a brand name usually associated with midazolam and is an injection. This entry should be verified against the SAHPRA register before being relied upon.

Available routes: oral (tablet) and injectable (injection).

---

## Safety Considerations

Package-insert warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text):
- Cardiovascular: hypertension, congestive heart failure, coronary artery disease, myocardial infarction, stroke and cerebrovascular disorders
- Hepatic and renal: liver disease and failure, kidney disease
- Haematological: blood coagulation disease, anaemia, hemoglobinopathy
- Other: epilepsy, diabetes mellitus, diabetic ketoacidosis, osteoporosis, obesity, gallbladder disease, benign prostatic hyperplasia, substance abuse/dependence

**Drug interactions** (DDInter; 100 interactions recorded, the 20 shown below were all rated Moderate):
- Acid-suppressing agents: famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Antidiabetic agents: metformin, chlorpropamide
- Other NSAIDs and aminosalicylates: acetylsalicylic acid, mesalazine, balsalazide
- Others: aprepitant, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol (3350 with electrolytes)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score. There are no clinical trials or publications, and no plausible mechanism by which an NSAID would modify a congenital skeletal malformation. The safety profile also includes concerns, notably prenatal NSAID exposure.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Verified mechanism of action data from DrugBank
- A biological rationale linking COX inhibition to the pathology of brachydactyly-syndactyly syndrome
- Any preclinical or clinical evidence in the predicted condition
- Verification of the Dormicum registration entry against the SAHPRA register
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

