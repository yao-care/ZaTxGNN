---
layout: default
title: Tretinoin
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoin: From Acne and Acute Promyelocytic Leukaemia to Rheumatoid Nodulosis

## One-Sentence Summary

Tretinoin (all-trans retinoic acid) was originally used to treat acne, acute promyelocytic leukaemia, acquired keratosis and palmoplantar keratoderma.
The TxGNN model predicts it may be effective for **rheumatoid nodulosis**, but this is a computational prediction only, with **no clinical trials** and **no relevant publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, acute promyelocytic leukaemia, acquired keratosis, palmoplantar keratoderma (from the knowledge graph; the SAHPRA licence records contain no indication text) |
| Predicted New Indication | Rheumatoid nodulosis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tretinoin is a retinoid (a vitamin A derivative) whose efficacy in acne and acute promyelocytic leukaemia is established, and mechanistically it may be applicable to inflammatory conditions through retinoic acid receptor (RAR) signalling.

One general hypothesis is that retinoid signalling influences immune balance (Th17/Treg regulation). This is not supported by any trial or publication for rheumatoid nodulosis. The high TxGNN score reflects patterns in a knowledge graph, not clinical validation.

Other top predictions are also joint or skeletal conditions with no supporting evidence. They include rheumatoid factor-positive polyarticular juvenile idiopathic arthritis, juvenile idiopathic arthritis, juvenile chronic polyarthritis, spondyloarthropathy susceptibility, osteoarthritis, pseudoachondroplasia and acromesomelic dysplasia. Several of these (especially in children) raise safety concerns, as retinoids are associated with teratogenicity and skeletal effects. The most biologically plausible prediction in the list is folliculitis decalvans (rank 10), because it resembles tretinoin's established dermatological actions. Even there, no evidence was retrieved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for rheumatoid nodulosis.

(Two publications were retrieved for the lower-ranked osteoarthritis prediction. Neither supports tretinoin use: one concerns platelet-rich plasma injections and the other is an arsenic trioxide toxicity case report in acute promyelocytic leukaemia.)

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| F/13.12/284 | Airol | Cream | Not available in the data compiled |
| 49/13.12/0499 | Treclin Gel | Gel | Not available in the data compiled |
| H/13.12/172 | Ilotycin-a | Gel | Not available in the data compiled |

All three registrations are valid, single-ingredient entries and all are topical formulations. This matters because the predicted systemic or joint-related indications would likely require a different route than the topical products currently registered. Essential Medicines List (EML) status could not be determined from the data compiled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Differentiating agent (retinoid) used in acute promyelocytic leukaemia; not a conventional cytotoxic. Systemic use only |
| Myelosuppression Risk | Please refer to the Professional Information (PI) warnings and precautions |
| Emetogenicity Classification | Please refer to the Professional Information (PI) warnings and precautions |
| Monitoring Items | Please refer to the PI; typically FBC, liver function and lipids for systemic retinoids |
| Handling Protection | Please refer to the PI. Retinoids are teratogenic, so pregnancy precautions apply |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text): sunburn, anxiety and neurotic disorders, dysthymic disorder, psychotic and schizophrenia-spectrum disorders, kidney disease, liver disease, pancreatitis, gallbladder disease, congestive heart failure, adrenocortical insufficiency/Addison disease, Crohn disease and inflammatory bowel disease, atopic eczema/dermatitis, osteoporosis, diabetes mellitus and diabetic ketoacidosis, and mycosis fungoides and related cutaneous T-cell lymphomas.
- **Drug Interactions** (100 interactions recorded; main ones listed):
  - **Major:** doxycycline, tetracycline, minocycline, vitamin A
  - **Moderate:** aprepitant, clarithromycin, naltrexone
  - **Minor:** levofloxacin
  - Many others have unclassified severity (e.g. metformin, prednisone, omeprazole, morphine).
- **Paediatric and skeletal concerns:** systemic retinoids are associated with premature epiphyseal closure, hyperostosis and teratogenicity. This is relevant to the predicted juvenile arthritis and skeletal dysplasia indications.

The SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a computational score, with no clinical trials, no relevant publications and no established mechanistic link to rheumatoid nodulosis. The registered South African products are topical only, and the package insert safety data are missing, so the evidence is insufficient to proceed.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications and approved indications), which is a blocking gap
- Mechanism of action data (e.g. from DrugBank)
- A systematic literature search for retinoids in rheumatoid nodulosis and related inflammatory arthritis
- A route-of-administration assessment, since the registered products are topical only
- Review of the dermatological prediction (folliculitis decalvans) as a possibly more plausible alternative candidate
- Paediatric and reproductive safety review before considering any juvenile arthritis indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

