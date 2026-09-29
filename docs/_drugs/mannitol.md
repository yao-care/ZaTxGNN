---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From Cardioplegic Solution Component to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is registered in South Africa as a component of a cardioplegic infusion solution (the registration record does not state an approved indication).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a very high model score.
However, there are **0 clinical trials** and only **1 general review** on hyponatraemia, with no mannitol-specific evidence, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mannitol is generally known as an osmotic diuretic, but the Evidence Pack does not confirm an approved indication for the registered product, so no proven efficacy in an original indication can be cited.

NSIAD is caused by a gain-of-function change in the AVPR2 (vasopressin V2 receptor) gene. This leads to water retention and low blood sodium (hyponatraemia). An osmotic diuretic could in theory promote water excretion, but the evidence review found no clear mechanism linking mannitol to this condition. The high model score is not supported by clinical data. The only literature hit is a general review of hyponatraemia evaluation, whose title shows no mannitol-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | Eur J Intern Med | Describes ten common pitfalls in evaluating hyponatraemia. It is a general review with no mannitol-specific evidence. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SX/34/0266 | Cardioplegic soln a 1000ml sxa3020 | Infusion | Not stated in the registration record |

Essential Medicines List (EML) status for mannitol is not included in the Evidence Pack.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no clinical trials and no mannitol-specific literature, and no plausible mechanism was identified. The safety data needed to proceed are also missing.

The other nine top-ranked predictions for mannitol (for example acute pulmonary heart disease, nephrogenic diabetes insipidus, and the malignant hyperthermia-related conditions) were also rated Hold. Several appear to be artefacts of mannitol's role as an excipient in other products, such as intravenous dantrolene.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data, for example from DrugBank
- Mannitol-specific preclinical or clinical evidence in NSIAD
- The approved indication text for the registered product, and its EML status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

