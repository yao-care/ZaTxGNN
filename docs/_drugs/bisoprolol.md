---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 5
---

# Bisoprolol
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

# Bisoprolol: From a Registered Beta-Blocker (Indication Not Recorded) to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a beta-1 selective blocker registered in South Africa, mostly in fixed-dose tablet combinations, but the supplied record has no approved indication text.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model prediction only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all SAHPRA licence entries in the record have blank indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Bisoprolol is a beta-1 selective blocker. Its antihypertensive effect and its reduction of renin release make a link to severe hypertension with kidney involvement biologically plausible. This judgment rests on general pharmacology, not on supplied data.

There are important limits. Malignant hypertension is a hypertensive emergency, normally managed with titratable intravenous agents, so an oral beta-blocker is not a first-line option. The high graph score is not backed by any trial or publication.

The second-ranked prediction, malignant renovascular hypertension, has an identical score and is likely a near-duplicate of this one. Beta-1 blockade lowering renin is conceptually relevant, but it is a class effect and not evidence for bisoprolol in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 43/7.1.3/0059 | Bisozyd co 2.5mg/6.25mg | Tablet | Not recorded |
| Reg. No. 47/7.1.3/0710 | Emcor 5/5 Fdc | Tablet | Not recorded |
| Reg. No. 44/7.1.3/0561 | Zirinak Co 5/6,25 | Tablet | Not recorded |
| Reg. No. 51/7.1.3/0495 | Cosyrel 5/5 | Film-coated tablet | Not recorded |
| Reg. No. 37/7.1.3/0564 | Ziabeta 2.5/6.25mg | Tablet | Not recorded |

The record lists 9 registrations in total, and the table shows the first 5. All listed products are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or literature (L5). The clinical setting, a hypertensive emergency, is not one where an oral beta-blocker is normally used. The record also lacks safety information and the original indication.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indications), to allow a safety screen
- Mechanism of action data from DrugBank, to support a mechanistic-link analysis
- A targeted literature search on bisoprolol in malignant or severe hypertension with renal involvement
- Clinical expert review of whether an oral beta-blocker has any role in this setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

