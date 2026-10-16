---
layout: default
title: Proguanil
parent: Model Prediction Only (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Proguanil: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Plasmodium falciparum malaria"
---

# Proguanil
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

# Proguanil: From Malaria to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Proguanil is an antimalarial originally used to treat *Plasmodium falciparum* malaria and malaria prophylaxis.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasmodium falciparum malaria; malaria (from the knowledge graph, as no approved indication text is available for the SAHPRA registration) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 92.12% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, proguanil is a prodrug. Its metabolite, cycloguanil, inhibits dihydrofolate reductase (DHFR), and proguanil itself has reported effects on mitochondrial function. Its efficacy in malaria is established.

A link between these properties and mast cell proliferation (for example, KIT-driven disease) is speculative. The score of 0.92 appears to reflect the structure of the knowledge graph rather than a validated pharmacological target. Approved and investigational KIT inhibitors already exist for systemic mastocytosis, so any proguanil rationale would need to be clearly differentiated from them.

**Other predictions in the set** (all L5, all Hold, no trials or literature):

| Predicted Indication | Score | Comment |
|------|------|------|
| Lymphoadenopathic mastocytosis with eosinophilia | 90.45% | Rare mast cell/eosinophilic neoplasm; no established pathway to proguanil |
| Renal-hepatic-pancreatic dysplasia | 86.62% | Developmental ciliopathy-related disorder; unlikely to be reversible by a postnatal antimalarial |
| Systemic mastocytosis | 86.27% | Parent category of the two mastocytosis predictions above, so they are not independent |
| Polycystic kidney disease 3 (with or without polycystic liver disease) | 84.42% | Hypothetical link via mitochondrial and AMPK/mTOR signalling |
| Karyomegalic interstitial nephritis | 84.40% | Linked to FAN1 and DNA repair; no known connection to proguanil |
| Joubert syndrome with renal defect | 84.20% | Ciliopathy; score likely reflects network neighbours |
| Thoracic malformation | 84.09% | Structural congenital anomaly; no plausible pharmacological reversal |
| Adult familial nephronophthisis-spastic quadriparesia syndrome | 83.54% | Ultra-rare ciliopathy-spectrum disorder; no support found |
| Polycystic kidney disease | 71.09% | Lowest score; hypothetical; proguanil needs dose adjustment in renal impairment |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/20.2.8/0434 | Trizivar | Tablet | Indication text not available in the data compiled for this report |

Trizivar is a single-ingredient oral product with a valid registration. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from knowledge graph relationships, not from label text, and must be verified against the Professional Information):
- Liver failure
- Liver disease
- Gallbladder disease
- Hyperglycaemia
- Chronic diarrhoeal disease

**Drug Interactions:** 33 interactions were identified in total, and 20 are listed in the data compiled for this report.
- **Major:** auranofin, aurothioglucose
- **Moderate:** antacids and related agents (aluminium hydroxide, calcium carbonate, magnesium hydroxide, magaldrate, sodium bicarbonate, kaolin); anticoagulants (warfarin, dicoumarol, anisindione); artemether; fenofibrate; apalutamide; armodafinil; sapropterin; glucarpidase; radioiodine (iodide I-131, I-123)
- **Minor:** brivaracetam

Please refer to the SAHPRA-approved Professional Information (PI) for the full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or publications, and no credible mechanistic link between proguanil and mast cell disease. The related predictions are either not independent of each other or biologically implausible.

**To proceed, the following is needed:**
- Mechanism of action data for proguanil and cycloguanil, to test for any link to mast cell biology
- A literature and trial search specific to proguanil in mastocytosis, then preclinical testing (for example, in KIT-driven mast cell models) if a signal emerges
- A differentiated rationale against existing KIT-inhibitor therapy
- The SAHPRA package insert warnings and contraindications, which are still missing and block any safety screening
- A review of the interaction and renal dosing considerations for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

