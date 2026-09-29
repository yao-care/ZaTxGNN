---
layout: default
title: Oseltamivir
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Oseltamivir
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

# Oseltamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

Oseltamivir is a neuraminidase inhibitor antiviral, originally used to treat influenza.
The TxGNN model predicts it may be effective for **pyelonephritis** (score 97.8%), but there are **0 clinical trials** and **1 publication** (a general review that does not support this use).
This is a computational prediction only, with no clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (based on the literature in the Evidence Pack; SAHPRA indication text was not provided) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Oseltamivir is known as a neuraminidase inhibitor that limits the release and spread of influenza virus, and its efficacy in influenza is established.

Pyelonephritis is a bacterial kidney infection, usually of the urinary tract. Neuraminidase inhibition has no plausible link to it. The only retrieved article is a narrative review of influenza in pregnancy, which does not address urinary infection at all.

The high TxGNN score most likely reflects proximity in the knowledge graph rather than a real pharmacological effect. Until independent evidence appears, this prediction should be treated as unsupported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26033556](https://pubmed.ncbi.nlm.nih.gov/26033556/) | 2015 | Review | Presse Medicale | Narrative review of influenza in pregnancy (higher risk of pneumonia and hospitalisation). It does not address pyelonephritis or urinary infection. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/20.2.8/0687 | Oseltamivir Adco 30 Mg | Capsule | Not stated in the data provided |
| Reg. No. 56/20.2.8/1086 | Ozetir | Suspension | Not stated in the data provided |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pyelonephritis prediction has no clinical trials, no supporting literature and no plausible mechanism. The score alone does not justify further investment.

**To proceed, the following is needed:**
- Any independent clinical or mechanistic evidence linking oseltamivir to urinary tract or kidney infection
- The SAHPRA Professional Information (indications, warnings, contraindications)
- Mechanism of action data from DrugBank

**Note:** Other predictions in this Evidence Pack are better supported. Pneumonia (rank 8) is the strongest, at evidence level L2 and "Proceed with Guardrails". Its support is indirect, coming from influenza-related pneumonia. Staphylococcus aureus infection and streptococcal pneumonia are research questions at L4. They should be evaluated in separate reports.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

