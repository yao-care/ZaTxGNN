---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is an antidepressant. The registration data supplied did not state an indication, so depression here is background knowledge. The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**, but **0 clinical trials** and **0 publications** currently support this direction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (depression is assumed from general drug knowledge) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, mirtazapine blocks alpha-2 adrenergic, 5-HT2, 5-HT3 and H1 receptors. This is background knowledge and is not confirmed by the supplied data.

Ohdo syndrome (KAT6B-related) is a neurodevelopmental disorder caused by faulty chromatin regulation. No plausible pathway connects mirtazapine's receptor targets to that biology, so the data support no mechanistic link. The high score of 0.994 comes from graph-based similarity alone. No trial or publication backs it.

Two other predictions share the same weakness:
- **Blepharophimosis–intellectual disability syndrome, Ohdo type** (score 99.11%) is closely related to the entry above, so the two predictions are probably not independent.
- **Benign paroxysmal torticollis of infancy** (score 99.11%) is a migraine-related episodic syndrome. Only a speculative link is possible, since serotonergic and antihistaminergic drugs have been discussed in migraine prophylaxis. Mirtazapine carries a paediatric suicidality warning and is not established for use in infants, so a safety assessment would be needed before any research use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/1.2/1005 | Mirtaneo 15 | Tablet | Not provided in the supplied data |
| Reg. No. 41/1.2/0529 | Ramure 15Mg | Tablet | Not provided in the supplied data |

Both products are oral tablets.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records, so no interactions could be listed. This is a search gap, not evidence that none exist.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score, with no trials, no publications and no supported mechanistic link. The safety review is also blocked, because the SAHPRA package insert has not yet been reviewed.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which block the safety screening
- Confirmed mechanism of action data (for example from DrugBank) and a documented biological link to Ohdo syndrome
- Any preclinical, case-report or trial evidence for mirtazapine in Ohdo syndrome or related disorders
- A specific safety assessment for paediatric use, including suicidality risk, if research in children is considered

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

