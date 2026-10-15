---
layout: default
title: Sibutramine
parent: Model Prediction Only (L5)
nav_order: 418
evidence_level: L5
indication_count: 4
---

# Sibutramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Sibutramine: From Obesity to Hypervitaminosis

## One-Sentence Summary

Sibutramine was originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but **no clinical trials and no publications** currently support this prediction. It is a model-only (in silico) result.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the SAHPRA registration entry contains no approved indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Sibutramine is generally described as a serotonin-norepinephrine reuptake inhibitor (SNRI) used for weight management, and its efficacy in obesity is the basis of its original indication.

For hypervitaminosis, however, no credible mechanistic link was identified. Hypervitaminosis is a state of nutrient excess, and it has no known dependence on monoamine reuptake. The very high TxGNN score (99.98%) reflects a knowledge-graph association only. It is not backed by any trial or publication.

**Other predictions from the same model (all L5, all Hold):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Proximal 16p11.2 microdeletion syndrome | 99.98% | The most biologically plausible. This syndrome is associated with syndromic obesity and hyperphagia, which overlaps with sibutramine's original obesity indication (appetite and satiety modulation). No efficacy evidence was provided, and the population may have neurodevelopmental and cardiac comorbidities. |
| Obsolete hypertelorism (disease) | 99.97% | A craniofacial structural anomaly, and the term is obsolete. A reuptake inhibitor cannot plausibly correct a developmental malformation. Likely a graph-association artefact. |
| Frontorhiny | 99.95% | A frontonasal dysplasia-type congenital malformation with no recognised pharmacological link. Likely a graph-association artefact. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypervitaminosis.

---

## Literature Evidence

Currently no related literature available for hypervitaminosis.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 41/11.3/0313 | Ciplatrim 15 | Capsule (oral) | Not stated in the registration data |

The registration is a valid single-ingredient product. The data compiled for this report do not show Essential Medicines List (EML) inclusion status.

---

## Safety Considerations

**Key points from the data compiled for this report:**

- **Cardiovascular risk (important context):** Sibutramine was withdrawn from many markets because of increased cardiovascular risk (SCOUT trial). This is relevant to any new use, especially in populations with cardiac comorbidities.
- **Contraindications (from knowledge-graph associations, not label text):** Hypertension and hypertensive disorders; coronary artery disease, myocardial infarction, heart disease, cardiovascular disease, heart conduction disease and sudden cardiac arrest; stroke, cerebrovascular disorder and cerebral infarction; liver failure; kidney disease, chronic kidney disease and chronic renal failure; epilepsy; diabetes mellitus and diabetic ketoacidosis; blood coagulation disease; hemoglobinopathy; angle-closure glaucoma; anorexia nervosa and bulimia nervosa; neuroleptic malignant syndrome and serotonin syndrome; pyoureter.
- **Drug interactions:** The query returned 100 interactions, and 20 are shown in the data compiled for this report. The following are **Major**:
  - Fentanyl
  - Dextromethorphan
  - Tramadol

  These are consistent with the risk of serotonergic toxicity. Moderate interactions include sympathomimetics (phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol), NSAIDs (ibuprofen, ketorolac), codeine, dihydrocodeine, acetazolamide, acarbose, abciximab, acalabrutinib, albiglutide, isometheptene, trastuzumab emtansine and abametapir (topical).

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for authoritative safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypervitaminosis rests only on a graph-based score, with no trials, no literature and no plausible mechanism. Sibutramine also carries a serious cardiovascular safety history and many contraindications, so the risk is not justified by the current evidence.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) to test any mechanistic link
- Any preclinical or clinical evidence for the predicted indication
- If a new indication is pursued, 16p11.2 microdeletion syndrome is the most biologically plausible candidate. It would need a dedicated cardiovascular and neurodevelopmental risk assessment before any further consideration.
- Confirmation of the registered indication and current regulatory status of Ciplatrim 15 in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

