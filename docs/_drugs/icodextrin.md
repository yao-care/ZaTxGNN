---
layout: default
title: Icodextrin
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Icodextrin
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

# Icodextrin: From Peritoneal Dialysis to Irritable Bowel Syndrome

## One-Sentence Summary

Icodextrin is a high-molecular-weight glucose polymer used as an osmotic agent in peritoneal dialysis.
The TxGNN model predicts it may be effective for **irritable bowel syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritoneal dialysis (osmotic agent). The registration data supplied contain no approved indication text. |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 98.53% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Icodextrin is an osmotic agent in peritoneal dialysis. It is not known to act on gut motility, visceral sensation or the gut-brain axis.

No mechanistic link to irritable bowel syndrome has been established. Any gut-related effect would be speculative. The high score reflects a knowledge-graph association and not pharmacological evidence.

The other nine top-ranked predictions (scores 95.8% to 97.4%) are also L5 with no supporting data. They include esophageal malformation, C1 inhibitor deficiency, hereditary angioedema, potassium deficiency, serpinopathy, renal tubular acidosis and vitamin deficiency. Several look like graph-topology artefacts, for example the overlapping C1 inhibitor deficiency and hereditary angioedema predictions. The prediction list as a whole should be treated with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 38/34/0172 | Extraneal 2L twinbag system 2 | Infusion | Not stated in supplied data |
| Reg. No. 38/34/0172 | Extraneal 2L | Solution | Not stated in supplied data |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated in supplied data |

**Data-source caveat:** The three entries share one registration number, so they appear to be presentations of a single registration. The Evidence Pack lists its regulatory input as "tfda", and the number format may not be a SAHPRA one. The SAHPRA registration status and the approved indication should be verified directly on the SAHPRA register. Essential Medicines List (EML) status is not available in the supplied data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no mechanistic support, and safety and mechanism data are missing. The prediction should not be acted on until supporting evidence exists.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Confirmation of the SAHPRA registration status and number
- Mechanism of action data from DrugBank
- A plausible pharmacological rationale for irritable bowel syndrome, supported by preclinical or clinical evidence
- Assessment of route compatibility, since icodextrin is given intraperitoneally and irritable bowel syndrome is managed with oral or other gut-directed therapy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

