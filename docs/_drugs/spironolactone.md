---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 427
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension, congestive heart failure, hyperaldosteronism"
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Spironolactone: From Hypertension and Heart Failure to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone is an anti-androgen and mineralocorticoid receptor antagonist, originally used for hypertension, congestive heart failure and primary aldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure, hyperaldosteronism (the SAHPRA registration data compiled for this report contain no approved indication text; these indications come from the TxGNN knowledge graph) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Spironolactone is generally known as a mineralocorticoid receptor antagonist with anti-androgen activity. Its efficacy in hypertension, heart failure and hyperaldosteronism is established.

A plausible but unverified rationale is that blocking androgen receptor signalling in hair follicles could help androgen-driven hair loss. Spironolactone is used off-label in female pattern hair loss.

However, hypotrichosis simplex of the scalp is a rare hereditary hair loss disorder caused mainly by genetic variants (for example CDSN, APCDD1, RPL21), not by androgen excess. The anti-androgen mechanism therefore has weak relevance to its underlying pathology. The prediction most likely reflects network proximity in the knowledge graph rather than a specific mechanistic link.

A second predicted indication, congenital hypotrichosis milia (score 99.04%), is similarly supported by no trials or literature. The same limitations apply.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Q/18.1/70 | Spironolactone 25 Kiara (was Sandoz Spir...) | Tablet | Not stated in the data compiled |
| H1945 (Act 101 of 1965) | Aldazide | Tablet | Not stated in the data compiled |

Both registrations are valid, single-ingredient entries for oral tablets. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

**Contraindications (from knowledge graph drug-disease edges, not label text):**
kidney disease, anuria, pancreatitis, systemic lupus erythematosus (including paediatric), potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, gout, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hepatic coma, hepatic encephalopathy, neonatal jaundice, pyoureter.

**Drug Interactions:** The interaction query identified 100 interacting drugs. The first 20 returned include:
- **Major:** Loperamide
- **Moderate:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, metformin, bupropion, morphine, bisacodyl, castor oil, dronabinol, exenatide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin
- **Minor:** doxycycline, acetylsalicylic acid, fidaxomicin

Label-based warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5), with no clinical trials or literature. The anti-androgen mechanism has weak relevance to a genetically driven hair disorder, and the label-based safety review has not been completed.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Obtain mechanism of action data from DrugBank
- Systematic literature search for spironolactone in hereditary hypotrichosis (none was found in the data compiled)
- Assess route compatibility, since a topical or oral route for scalp use has not been evaluated
- Clinical expert review of whether the proposed indication is biologically plausible before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

