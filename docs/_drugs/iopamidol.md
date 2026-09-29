---
layout: default
title: Iopamidol
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Iopamidol
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

# Iopamidol: From Diagnostic Contrast Imaging to Prinzmetal Angina

## One-Sentence Summary

Iopamidol is an iodinated, non-ionic contrast agent used in diagnostic imaging.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic contrast imaging (the registry record gives no approved indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopamidol is a non-ionic contrast medium used to visualise blood vessels and tissues on X-ray and CT imaging. It has no known vasodilatory or anti-vasospastic pharmacology.

Prinzmetal angina is caused by coronary artery vasospasm, so treating it would need a drug that relaxes or protects vascular smooth muscle. Nothing in the available data suggests iopamidol does this. The high score (0.986) most likely reflects how the drug is connected to cardiovascular terms in the knowledge graph. That connection probably comes from its use in cardiac and vascular imaging, not from any therapeutic effect. On this evidence, the prediction is not mechanistically plausible.

The other top-ranked predictions show the same pattern. Where any evidence exists, it concerns iopamidol as a diagnostic tool or its safety in specific patients, not treatment:
- **Female breast carcinoma:** one terminated early-phase feasibility trial of CEST MRI, [NCT02380209](https://clinicaltrials.gov/study/NCT02380209), enrolled 8 patients and used iopamidol as an imaging probe.
- **Pulmonary hypertension:** 18 records, mostly about angiography, image quality and haemodynamic tolerability. They include a 1,996 safety series of 1,434 patients ([PMID 8539407](https://pubmed.ncbi.nlm.nih.gov/8539407/)).
- **Tendinitis:** MR arthrography and imaging studies only.

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/28/200 | Jopamiron 200 10Ml | Injection | Not stated in the registry record |

Essential Medicines List (EML) status was not verified in the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible therapeutic mechanism. Iopamidol's known role is diagnostic. Evidence Level L5 does not justify further development for Prinzmetal angina.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is needed before any safety screening
- Mechanism of action data from DrugBank
- A credible pharmacological rationale for coronary vasospasm, followed by preclinical evidence
- A decision on whether the diagnostic-imaging findings (CEST MRI in breast cancer, pulmonary angiography) should be tracked as a separate diagnostic-use question rather than as therapeutic repurposing

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

