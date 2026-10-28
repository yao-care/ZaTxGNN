---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-29
description: "Rivaroxaban: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available"
monitor_inn: "Rivaroxaban"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
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

## Rivaroxaban: From Anticoagulation (Indication Not Listed in Registration Data) to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Rivaroxaban is a direct Factor Xa inhibitor and an oral anticoagulant. The registration data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **no registered clinical trials** and only **4 publications** (reviews, a cohort study and a case report), none of which show that rivaroxaban treats the disease.
This prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text in both SAHPRA registrations is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Rivaroxaban is a direct Factor Xa inhibitor. It blocks a key step in the coagulation cascade and thereby reduces thrombin generation. The data compiled for this report contain no detailed mechanism-of-action entry, so this description is based on the drug's known class.

Rheumatoid arthritis involves chronic inflammation and a prothrombotic state, with increased thrombin generation and a higher risk of venous thromboembolism (VTE). This gives a plausible but **indirect** link to anticoagulation. Rivaroxaban might address the thrombotic comorbidity, but there is no evidence it would treat the underlying autoimmune disease. The very high TxGNN score is a computational prediction and is not supported by clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered for rheumatoid arthritis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity VTE diagnosis and treatment. Recurrent VTE occurs in 20% to 36% of patients within 10 years. It is not specific to rheumatoid arthritis. |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de medecine interne | Thrombin generation assay can detect hypercoagulability in autoimmune diseases. It supports the thrombotic-risk link and does not evaluate rivaroxaban. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PloS one | Adherence to rivaroxaban vs apixaban in non-valvular atrial fibrillation. Not relevant to rheumatoid arthritis. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | An 88-year-old woman with rheumatoid arthritis on oral steroids had recurrent embolic events despite anticoagulation for atrial fibrillation. It is a comorbidity report, not evidence of efficacy. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 55/8.2/0140 | Axolta 10 Mg | Film-coated tablet (Fct) | Not available |
| 55/8.2/0719 | Rexarav 20 Mg | Film-coated tablet (Fct) | Not available |

Essential Medicines List (EML) status could not be determined from the data compiled for this report.

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not from label text): liver failure, kidney disease, pyoureter, liver disease, gallbladder disease and blood coagulation disease.

**Drug Interactions**: 100 interactions were recorded. Those listed below are from the first 20 reviewed.
- **Major**: acetylsalicylic acid (aspirin), cobicistat, deferasirox, ibritumomab tiuxetan, tositumomab (I-131).
- **Moderate**: aprepitant, dexamethasone, cimetidine, clarithromycin, eliglustat, miconazole, clotrimazole, dexfenfluramine, fenfluramine, rolapitant, sibutramine, troglitazone, iodide I-131, iodide I-123, sugammadex.

Patients with rheumatoid arthritis often take corticosteroids and NSAIDs or aspirin, so bleeding risk with concomitant use needs particular attention.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for rheumatoid arthritis is supported only by the model score (L5). There are no registered trials, and the literature does not show disease-modifying benefit. The only plausible role is managing thrombotic comorbidity, which is already covered by existing anticoagulant indications.

**To proceed, the following is needed:**
- SAHPRA Professional Information (approved indications, warnings and contraindications), which is currently missing
- Mechanism-of-action data
- Clinical or preclinical evidence of benefit in rheumatoid arthritis, beyond thrombosis prevention
- A bleeding-risk assessment for patients on concomitant corticosteroids, NSAIDs or aspirin

---

### Note on Other Predicted Indications

Other predictions for this drug were also reviewed and all are recommended as **Hold**:

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Gout | 0.9951 | L5 | No credible mechanistic link. The retrieved literature is unrelated. |
| HIV infectious disease | 0.9917 | L4 | Literature covers rivaroxaban as an anticoagulant in people with HIV and its interactions with ritonavir- or cobicistat-boosted antiretrovirals. There is no evidence of antiviral activity. The one registered trial (NCT00786422) is a VTE study, not an HIV study. This is highly relevant to South Africa because of HIV prevalence, and it is a safety concern, not a repurposing signal. |
| Brachydactyly-syndactyly syndrome | 0.9910 | L5 | No data. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

