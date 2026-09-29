---
layout: default
title: Candesartan Cilexetil
parent: Model Prediction Only (L5)
nav_order: 96
evidence_level: L5
indication_count: 5
---

# Candesartan Cilexetil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker. The registration data supplied do not state its approved indication, but it is generally used for hypertension. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data; generally hypertension (general pharmacology knowledge, not from the Evidence Pack) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Candesartan is known from general pharmacology to block the angiotensin II AT1 receptor, which reduces vasoconstriction and aldosterone-driven effects. Blocking the renin-angiotensin system is biologically plausible for hypertensive kidney injury. Malignant hypertension damages the kidney, so a drug that lowers blood pressure and acts on this pathway could be relevant.

However, no trial or literature evidence for this specific indication was found. The very high score (99.68%) is a graph-model output and not clinical proof.

The second-ranked prediction, malignant renovascular hypertension, has the same score. This suggests shared graph neighbours rather than independent evidence.

### Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.68% | L5 | Mechanistically plausible through renin-angiotensin activation; ARB safety in renovascular disease (for example bilateral renal artery stenosis) needs review first |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.67% | L5 | No mechanistic link supported |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | L5 | The 20 retrieved papers are generic hypoxia biology, apparently a keyword match, and none concerns candesartan or ARBs |
| 5 | Braddock syndrome | 99.56% | L5 | Very rare condition; no mechanistic link can be established |

## Clinical Trial Evidence

Currently no related clinical trials registered. No ClinicalTrials.gov, SANCTR or PACTR records were identified for the leading predicted indication.

## Literature Evidence

Currently no related literature available for the leading predicted indication.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/7.1.3/0412 | Aterwin | Tablet | Not stated in the registration data |
| Reg. No. 44/7.1.3/0555 | Candepres plus 16mg/12.5mg | Tablet | Not stated in the registration data |
| Reg. No. 35/7.1.3/0098 | Atacand plus 16mg/12.5mg | Tablet | Not stated in the registration data |
| Reg. No. 45/7.1.3/0394 | Mylacand plus 16mg/12.5mg | Tablet | Not stated in the registration data |

All registered products are oral tablets. The "plus" products carry a 16 mg/12.5 mg strength, which suggests a fixed-dose combination.

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

For renovascular indications, ARB use in bilateral renal artery stenosis and similar conditions needs specialist review before any further step.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no relevant literature and no confirmed safety data. Safety screening cannot proceed without the SAHPRA package insert.

**To proceed, the following is needed:**
- SAHPRA package insert (PI) warnings, contraindications and approved indications, which are currently blocking
- Mechanism of action data from DrugBank
- A targeted literature search for candesartan or ARBs in malignant hypertensive nephropathy and renovascular hypertension
- Safety review for renal artery stenosis and other renal risks
- Registry checks (ClinicalTrials.gov, SANCTR, PACTR) for any relevant trials

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

