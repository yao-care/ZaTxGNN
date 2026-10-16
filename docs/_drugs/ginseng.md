---
layout: default
title: Ginseng
parent: Model Prediction Only (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ginseng: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not stated in the SAHPRA registration data"
monitor_inn: "Ginseng"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy", "amenorrhea (disease)", "mature cataract", "tetanic cataract"]
---

# Ginseng
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

# Ginseng: From Registered Use (Indication Not Stated) to Drug-Induced Osteoporosis

## One-Sentence Summary

Ginseng is a herbal product registered in South Africa, but the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, with a very high score.
However, there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ginseng is a botanical whose main active constituents are ginsenosides. Its original indication could not be determined from the registration data, so the link between the original and new indication cannot be assessed.

Ginsenosides have been proposed to influence bone remodelling. No supporting trials, publications or mechanistic data were found for drug-induced osteoporosis in the data compiled for this report. The score reflects a pattern found by the knowledge-graph model, not demonstrated clinical benefit. A high score alone should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (ACT 101/1965) | Gericomplex | Capsule | Not stated in the data compiled |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not stated in the data compiled |

Both registrations are valid and recorded as single-ingredient products. The Spiriva Respimat entry is an inhaler and is an unusual match for ginseng, so check this mapping against the SAHPRA register before relying on it. Essential Medicines List status could not be determined from the data compiled.

---

## Safety Considerations

- **Drug Interactions**: 83 interactions were identified. The 20 detailed entries are all rated **Moderate**.
  - **Glucose-lowering agents**: metformin, pioglitazone, acarbose, glimepiride, chlorpropamide, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, semaglutide, dulaglutide, albiglutide, lixisenatide, and insulins (aspart, degludec, detemir, glargine, glulisine). Monitor glucose when combining.
  - **Acetylsalicylic acid**.

For warnings, contraindications and other safety information, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis rests on the TxGNN score alone (L5). No trials or publications support it, and the original indication and mechanism are unknown. SAHPRA package insert safety information is also not yet available.

**Note on other predictions for ginseng:**
Diabetic retinopathy has a more developed evidence base (about 20 mostly preclinical publications, rated L4). A 2026 prospective, randomised, double-blind study of Korean red ginseng in diabetic retinopathy (PMID 42395017) is relevant to it. This is a stronger research direction than osteoporosis, though still preliminary.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI), to confirm the original indication, warnings and contraindications
- Verification of the SAHPRA registration entries, especially the inhaler product
- Mechanism of action data for ginseng and ginsenosides
- A systematic literature search on ginseng and bone metabolism or glucocorticoid-induced bone loss
- Any registered or published human studies in the predicted indication
- A review of interaction risks, especially with glucose-lowering medicines, in the likely target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

