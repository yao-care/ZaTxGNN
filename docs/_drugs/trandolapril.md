---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

# Trandolapril: From ACE Inhibitor Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

Trandolapril is an ACE inhibitor marketed in South Africa as part of the Tarka combination product; the SAHPRA data supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
There are **0 clinical trials** and **0 publications** supporting this prediction, so the model score is the only evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA data supplied (drug class: ACE inhibitor) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 entries (both carry the same registration number, so likely one unique product) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, trandolapril is an ACE inhibitor, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension is driven largely by activation of the renin-angiotensin-aldosterone system (RAAS). ACE inhibitors block this pathway, so the link is plausible. However, this reasoning rests on drug-class knowledge only. No trial or publication in the dataset examines trandolapril in this condition.

Caution is needed because ACE inhibitors carry recognised safety concerns in bilateral renal artery stenosis or a solitary kidney. The dataset does not address this, and it is directly relevant to the predicted indication.

Other predictions for this drug are also weakly supported:
- **Malignant hypertensive renal disease:** L5, prediction only.
- **Pulmonary hypertension (hypoxia-related and unclear multifactorial):** L5. The 20 retrieved records look like a keyword match on "hypoxia", and none of the 10 titles provided concerns trandolapril or pulmonary hypertension treatment. The other 10 records were not provided and are unassessed.
- **Braddock syndrome:** L5, no credible mechanistic link.
- **Chronic pulmonary heart disease:** L4. Only one 1996 rat study of long-term trandolapril in chronic heart failure exists (PMID 8989645), which is indirect preclinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR) for the predicted indication.

---

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A39/7.1.3/0508 | Tarka 180mg/2mg | Sustained-release tablet (recorded as "Srt") | Not listed in the data supplied |

The dataset lists this registration twice with identical details. Essential Medicines List (EML) status was not provided.

---

## Safety Considerations

- **Renal risk (from the prediction rationale):** ACE inhibitors carry safety concerns in bilateral renal artery stenosis or a solitary kidney. Acute renal function risk in malignant hypertension with renal involvement would need separate safety review.

No warnings, contraindications or drug interaction data were available. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or relevant publications. The available SAHPRA data does not include the approved indication or safety information. The safety concern in renal artery stenosis is unresolved for this population.

**To proceed, the following is needed:**
- The SAHPRA package insert (indication, warnings, contraindications), which blocks progression to safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search on trandolapril in renovascular and malignant hypertension
- A safety review for bilateral renal artery stenosis, solitary kidney and acute renal impairment
- Confirmation of the Tarka product composition (whether it is a fixed combination) and whether it suits the intended use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

