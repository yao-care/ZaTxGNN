---
layout: default
title: Triamterene
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 6
---

# Triamterene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Triamterene: From Diuretic Use (Oedema and Hypertension) to Malignant Renovascular Hypertension

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic. It is registered in South Africa as the tablet product Renezide, but the registration record does not list an indication.
The TxGNN model predicts it may be useful for **malignant renovascular hypertension**, with a very high model score.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record. Triamterene is generally used as a diuretic for oedema and hypertension (general pharmacology knowledge, not from the record). |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for triamterene was not available in the source data. Triamterene is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal kidney. This promotes sodium and water loss and lowers blood volume and blood pressure. The mechanism described here is therefore inferred, not verified from the data provided.

This gives a plausible but weak link to hypertension. Malignant renovascular hypertension is driven mainly by activation of the renin-angiotensin system, usually because of renal artery stenosis. A relatively weak diuretic is unlikely to control it on its own. The condition also often involves impaired kidney function, which raises the risk of dangerously high potassium (hyperkalaemia) with triamterene.

The model's score is very high, but no trial or publication supports it. The prediction should be treated as a hypothesis, not a treatment option.

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
| Reg. No. U/18.1/72 | Renezide | Tablet (oral) | Not stated in the record |

Essential Medicines List (EML) status could not be confirmed from the available data.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results, which reflects missing data and not proof of safety.
- **Prediction-related concerns** (from the model's rationale, not from the Professional Information):
  - Hyperkalaemia risk, especially with renal impairment.
  - Possible kidney harm when combined with NSAIDs or ACE inhibitors/ARBs.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature. The link between triamterene and this condition is only a general blood-pressure effect, and the renal and potassium risks are unfavourable in this patient group.

Other predicted indications, including malignant hypertensive renal disease, two forms of pulmonary hypertension and Braddock syndrome, also remain at L5 and Hold. One exception is chronic pulmonary heart disease. It has four older publications (1976–1991) on diuretic therapy in heart failure or congestion, which gives indirect L4 support and makes it a research question. Even there, none of the titles show triamterene-specific data.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for any safety screening.
- Confirmed mechanism-of-action data (for example from DrugBank).
- The registered indication for Renezide.
- A targeted literature search for triamterene in renovascular or malignant hypertension.
- A renal function and potassium monitoring plan, if any further evaluation is pursued.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

