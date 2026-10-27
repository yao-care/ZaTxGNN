---
layout: default
title: Oxetacaine
parent: Model Prediction Only (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Oxetacaine: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the SAHPRA registration data (oxetacaine is generally…"
monitor_inn: "Oxetacaine"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "uterine polyp", "polyp of vocal cord", "polyp of middle ear", "polyp of ureter", "polyp of frontal sinus", "polyp of external auditory canal", "epulis"]
---

# Oxetacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Oxetacaine: From Local Anaesthesia (Original Indication Not Recorded) to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Oxetacaine is a topical amide local anaesthetic. The South African registration data compiled for this report does not record an approved indication.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA registration data (oxetacaine is generally a surface anaesthetic used for symptomatic pain relief) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 97.89% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Oxetacaine is known as a topical amide local anaesthetic that blocks voltage-gated sodium channels, and it is used for symptomatic pain relief (for example in gastric and haemorrhoidal preparations).

**No plausible mechanistic link has been established** between this action and the predicted indication. Primary release disorder of platelets involves defective platelet granule release and signalling, and oxetacaine has no known effect on these processes. The high TxGNN score is a model-based prediction only, and no clinical or literature data support it.

The other top-ranked predictions have the same weakness. All ten are L5 (model prediction only) with no trials or publications:

| Rank | Predicted Indication | TxGNN Score | Mechanistic Assessment |
|------|------|------|------|
| 1 | Primary release disorder of platelets | 97.89% | No link to platelet granule release or signalling |
| 2 | Pseudo-von Willebrand disease | 97.43% | Disease is a platelet GPIb-alpha gain-of-function defect; sodium channel blockade is not relevant |
| 3 | Glanzmann thrombasthenia | 97.30% | Caused by integrin alpha-IIb/beta-3 deficiency or dysfunction; no known interaction |
| 4 | Uterine polyp | 97.29% | No antiproliferative or hormonal activity; at most procedural analgesia |
| 5 | Polyp of vocal cord | 97.16% | At most topical anaesthesia during procedures, which is not a repurposing indication |
| 6 | Polyp of middle ear | 97.14% | Inflammatory pathogenesis; anaesthesia would address symptoms only |
| 7 | Polyp of ureter | 97.09% | No effect on benign fibroepithelial proliferation |
| 8 | Polyp of frontal sinus | 97.08% | Driven by chronic inflammation; no anti-inflammatory action established |
| 9 | Polyp of external auditory canal | 97.05% | May relieve discomfort but would not affect the polyp |
| 10 | Epulis | 97.05% | Usually treated by surgical excision; at most a topical oral anaesthetic |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E/11.4.3/1223 | Mucaine | Suspension | Not recorded in the registration data |

The registration is a valid single-ingredient product. The Essential Medicines List (EML) status of oxetacaine could not be determined from the data compiled for this report.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found for oxetacaine in the data compiled for this report. This is an absence of data, not evidence that no interactions exist.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are supported only by the TxGNN model score (L5), with no registered trials, no publications and no plausible mechanism. Safety information from the SAHPRA package insert is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert for warnings, contraindications and the approved indication
- Obtain mechanism of action data for oxetacaine from DrugBank
- Establish a biologically plausible link between sodium channel blockade and the platelet disorders, or prioritise a different candidate indication
- Confirm route-of-administration compatibility, since the only registered form is a suspension and the formulation required for the predicted indications is unknown
- Find preclinical or clinical evidence before reconsidering this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

