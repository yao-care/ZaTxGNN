---
layout: default
title: Valsartan
parent: Model Prediction Only (L5)
nav_order: 464
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II type 1 receptor blocker (ARB), a class established for treating hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, a kidney injury caused by severe hypertension.
Evidence is very thin: **0 clinical trials** and **1 publication**, and that publication is a preclinical study of a different drug (avosentan), not valsartan.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (based on the ARB class; approved indication text is not captured in the South African registration records supplied) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical/indirect evidence only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, valsartan blocks the angiotensin II type 1 (AT1) receptor. Angiotensin II is a key driver of blood pressure elevation and of injury to the small vessels of the kidney. Blocking this pathway is a plausible way to protect the kidney in severe hypertension.

The predicted indication is essentially a severe, organ-damaging form of the hypertension that valsartan already treats. This suggests the model is picking up a close disease relationship, and that the original-indication field in the source data is incomplete. The high score is a graph-based prediction only and is not confirmed by any human data.

The one linked paper studies avosentan, an endothelin antagonist, in a rat model of hypertensive kidney disease. It supports the general idea that blocking neurohormonal pathways may protect the kidney, but it does not test valsartan or any ARB. The evidence is therefore class-level and indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical (animal study) | Pharmacological Research | Avosentan, an endothelin antagonist and not an ARB, protected against hypertensive nephropathy in double transgenic rats at doses that did not cause fluid retention. |

## South Africa Market Information

Valsartan has 20 SAHPRA registrations in total. The first 5 are listed below. Approved indication text was not available in the supplied records.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 43/7.1.3/0773 | Diolo 80 | Tablet |
| Reg. No. 51/7.1.3/1106 | Calsar 5/80 Mg | Tablet |
| Reg. No. 51/7.1.3/0610 | Valvasc 5/160 | Film-coated tablet |
| Reg. No. 50/7.6/1019 | Vymada 50 Mg | Tablet |
| Reg. No. 48/7.1.3/0567 | Niosar Co 80/12,5 Mg | Film-coated tablet |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, and the only linked paper studies a different drug in animals. The evidence is not enough to support moving this indication forward.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is currently missing and blocks any safety screening
- Detailed mechanism of action data from DrugBank
- Direct evidence for valsartan or other ARBs in malignant hypertension with kidney involvement, for example a structured literature review or human studies
- A safety review of renal function risks with ARBs in patients with severe hypertensive kidney disease

**Related prediction worth reviewing:** For malignant renovascular hypertension (ranked 2nd), one 2001 preclinical study in *Circulation* reported that AT1 receptor blockade prevented lethal malignant hypertension and kidney inflammation. This is a more direct mechanistic match, though still animal-only. It carries a specific safety concern, because ARBs can worsen renal function in renal artery stenosis.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

