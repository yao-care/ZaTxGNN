---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 235
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "Plasmodium falciparum malaria", "allergic urticaria", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "pneumocystosis", "blood group incompatibility", "premalignant hematological system disease", "papular urticaria"]
---

# Fluconazole
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

# Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is an oral azole antifungal, originally used to treat candidiasis (oral, oesophageal, vulvovaginal, disseminated) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, oesophageal candidiasis, vulvovaginal candidiasis, disseminated candidiasis, candidaemia, cryptococcal meningitis (SAHPRA indication text was not available in the data compiled for this report) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fluconazole is an azole antifungal whose efficacy in candidiasis and cryptococcal infection is established. Azoles generally act by inhibiting fungal CYP51 (lanosterol 14-alpha-demethylase), which disrupts ergosterol synthesis.

For punctate epithelial keratoconjunctivitis, no supporting mechanism is evident in the data compiled for this report. The condition is often viral (adenoviral) or inflammatory in origin, so an antifungal's mechanism has no clear relevance. The high TxGNN score is a computational prediction and should not be read as evidence of efficacy.

Other predictions for this drug were also reviewed. Only two had any supporting material, and neither is stronger than the lead prediction:
- **Plasmodium falciparum malaria**: in vitro activity of antifungals against field isolates has been reported (L4). Potency is generally weak relative to achievable plasma levels, and there are no clinical data.
- **Pneumocystosis**: the only trial found tests rezafungin, not fluconazole. *Pneumocystis* lacks ergosterol, the main azole target, so fluconazole is not a standard therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

## South Africa Market Information

Fluconazole is marketed in South Africa as an oral capsule. Essential Medicines List (EML) status and approved indication text were not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/20.2.2/0534 | Mycorest | Capsule | Not available |
| A38/20.2.2/0559 | Ralmient | Capsule | Not available |
| A38/20.2.2/0558 | Ralmient | Capsule | Not available |

No ophthalmic (topical) formulation is registered. Only oral capsules are available, which matters for any ocular surface indication.

## Safety Considerations

- **Contraindications and disease associations (knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, gallbladder disease.
- **Drug interactions** (100 interactions identified; selected examples):
  - **Major**: chlorpropamide.
  - **Moderate**: omeprazole, rabeprazole, famotidine, dexlansoprazole, dexamethasone, hydrocortisone, betamethasone, triamcinolone, budesonide, aprepitant, loperamide, saxagliptin, bisacodyl.
  - **Minor**: amphotericin B, clarithromycin.
- **Additional observation**: one cohort study in kidney transplant recipients reported that fluconazole raised tacrolimus trough levels, so tacrolimus dose adjustment and monitoring are needed.

Label warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanism, so it is evidence level L5. No topical or ophthalmic formulation is registered locally, and the data compiled for this report are incomplete on label safety.

**To proceed, the following is needed:**
- Download and review the SAHPRA Professional Information to complete the safety review (a blocking gap)
- Detailed mechanism of action data (e.g. from DrugBank)
- A literature search focused on azoles in adenoviral or other keratoconjunctivitis, and a clear rationale for any antifungal role
- An assessment of route and formulation feasibility, since only oral capsules are registered
- Re-evaluation of other candidate indications with better evidence before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

