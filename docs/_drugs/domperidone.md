---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Domperidone: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the SAHPRA registration data. Pharmacology data describ…"
---

# Domperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Domperidone: From Upper Gastrointestinal Symptoms to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist used to manage dyspepsia, heartburn, epigastric pain, nausea and vomiting.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. Pharmacology data describe use for dyspepsia, heartburn, epigastric pain, nausea and vomiting |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for domperidone is not available in the data compiled for this report. Domperidone is generally known as a peripheral D2/D3 dopamine receptor antagonist and prokinetic agent, and the pharmacology data confirm binding to the D2 (DRD2) and D3 (DRD3) receptors.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2) or, in some cases, in GNAS. These mutations cause water retention and low blood sodium (hyponatraemia) even though vasopressin is undetectable. No established mechanism links dopamine D2/D3 antagonism to V2 receptor signalling or to renal water handling. One speculative link is that domperidone raises prolactin and may influence the hypothalamic-pituitary axis. This is unlikely to affect constitutively active V2 receptors in the kidney.

The high score (rank 4550) may reflect network proximity in the knowledge graph, such as shared hyponatraemia, electrolyte or neuroendocrine nodes, rather than real pharmacological relevance. The prediction should be regarded as a hypothesis only. Similarity between the original and predicted indications has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/5.7.2/0563 | Domperidone Cipla | Orally disintegrating tablet (ODT) | Not recorded in the data compiled for this report |

Essential Medicines List (EML) inclusion status was not available in the data compiled for this report.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease. These should be confirmed against the approved Professional Information (PI).
- **Pharmacological targets**: dopamine D2 receptor (DRD2) and D3 receptor (DRD3). No drug-drug interaction entries with a severity level were returned.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings, contraindications and interaction information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). No clinical trials or publications support it, and there is no plausible pharmacological link between D2/D3 antagonism and the V2 receptor mechanism of NSIAD. The knowledge-graph QT-related contraindication signals add a safety concern, and NSIAD is a rare condition often driven by a genetic cause.

**To proceed, the following is needed:**
- Retrieval and review of the SAHPRA package insert (PI) for warnings, contraindications and the approved indication
- Confirmed mechanism of action data for domperidone
- Preclinical or mechanistic evidence for any effect on AVPR2/GNAS signalling or renal water handling
- A systematic literature search for case reports or studies in NSIAD or related hyponatraemia
- Assessment of QT-prolongation risk in the target population, which is likely to include children, since NSIAD often presents in infancy
- Route compatibility assessment, which is still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

