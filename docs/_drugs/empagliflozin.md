---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Empagliflozin: From SGLT2 Inhibitor Therapy to Focal Stiff Limb Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor that acts on renal glucose reabsorption and is marketed in South Africa.
The TxGNN model predicts it may be relevant to **Focal Stiff Limb Syndrome** with a very high score, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction is model output only and has no biological or clinical support at present.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

The registration records in the Evidence Pack do not include approved indication text, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

**It is not well supported.** Detailed mechanism-of-action data is not available in the Evidence Pack. Based on known information, empagliflozin is an SGLT2 inhibitor that lowers blood glucose by reducing renal glucose reabsorption.

Focal stiff limb syndrome is a rare disorder in the stiff-person spectrum. It is usually autoimmune (for example anti-GAD65 or anti-amphiphysin) and involves impaired GABAergic inhibition. SGLT2 inhibition has no established effect on this pathway.

The high score (0.99) is a graph-based prediction. It most likely reflects knowledge-graph neighbourhood effects, not biology. Diabetes is a common comorbidity in stiff-person-spectrum disorders because of GAD65 autoimmunity. This may inflate the predicted association without implying any therapeutic benefit.

**Other predictions for this drug** are equally weak:
- **Classic stiff person syndrome** (score 99.06%, identical to the focal form, which suggests the two disease nodes share the same graph neighbourhood). Standard therapy is GABA-enhancing agents plus immunotherapy, and SGLT2 inhibition has no known effect here.
- **Opsismodysplasia** (score 99.03%). This is a rare paediatric skeletal dysplasia caused by INPPL1 (SHIP2) loss of function. SHIP2 negatively regulates PI3K/insulin signalling, which may explain the graph link to glucose-metabolism drugs. No evidence shows that SGLT2 inhibition corrects the growth-plate defect. SGLT2 inhibitors also carry safety concerns in children (volume depletion, ketoacidosis).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 48/21.2/1380 | Jardiance | Tablet (oral) |
| Reg. No. 48/21.2/0411 | Jardiance | Tablet (oral) |
| Reg. No. 49/21.2/0915 | Synjardy 5/500 Mg | Tablet (oral) |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no clinical trials, no literature, and no plausible mechanistic link to the disease biology. The drug is widely available in South Africa, but that availability does not support this new use.

**To proceed, the following is needed:**
- Mechanism-of-action data (for example from DrugBank) and a re-assessment of any mechanistic link
- SAHPRA Professional Information (warnings and contraindications), which is required before any safety screening
- Preclinical or clinical evidence showing that SGLT2 inhibition affects stiff-person-spectrum pathology
- For the opsismodysplasia prediction, a paediatric safety assessment before any consideration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

