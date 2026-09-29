---
layout: default
title: Sertraline
parent: Moderate Evidence (L3-L4)
nav_order: 413
evidence_level: L4
indication_count: 8
---

# Sertraline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Sertraline: From an SSRI Antidepressant to Histrionic Personality Disorder

## One-Sentence Summary

Sertraline is a selective serotonin reuptake inhibitor (SSRI) marketed in South Africa as tablets.
The TxGNN model ranks **histrionic personality disorder** as its top-scoring prediction, but this is model output only: there are **no clinical trials** and **1 indirect publication**.
This candidate should be **held**, not advanced.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Histrionic personality disorder |
| TxGNN Prediction Score | 99.93% (shared with three other personality-disorder nodes) |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sertraline is an SSRI and is widely used in depressive and anxiety disorders, so a serotonergic rationale is plausible in principle. The registration records do not include approved-indication text, so the original indication cannot be quoted here.

The prediction is weak for three reasons:

- **The score is not specific to this disorder.** The same score (99.93%) appears for paranoid, schizoid and schizotypal personality disorders. It is probably inherited from a shared parent node in the knowledge graph.
- **The only publication is indirect.** It concerns depressive symptoms after drug treatment, not efficacy against histrionic personality disorder.
- **Any benefit would likely be indirect.** Sertraline may help comorbid depression or anxiety in people with personality-disorder traits. That is not evidence that it treats the personality disorder itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22075735](https://pubmed.ncbi.nlm.nih.gov/22075735/) | 2011 | Cohort | Psychiatria Danubina | Examined links between MMPI-2 "neurotic triad" scores (hypochondria, depression, hysteria) and depression levels after pharmacological treatment in depressive disorders. It does not test sertraline for histrionic personality disorder. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A40/1.2/0654 | Aurolift 50Mg | Tablet |
| Reg. No. A39/1.2/0308 | Sertra | Tablet |
| Reg. No. 36/1.2/0274 | Tralidep | Tablet |
| Reg. No. 36/1.2/0273 | Serlife | Tablet |

All four registrations are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score that appears to be inherited from a shared node, and the single publication is indirect. No trial has tested sertraline in histrionic personality disorder. SAHPRA safety data has also not been obtained, and that gap blocks progression to safety screening.

**To proceed, the following is needed:**
- Download and review the SAHPRA package insert (warnings, contraindications, approved indications). This is a blocking gap.
- Obtain mechanism of action data, for example from DrugBank.
- Find any direct clinical evidence of sertraline in histrionic personality disorder. None was retrieved.

**Note on other predictions in this pack:** the sixth-ranked prediction, **agoraphobia** (score 99.54%), has much stronger support, including a completed Phase 4 sertraline vs paroxetine trial in panic disorder (NCT00677352, n=321), network meta-analyses and RCTs. It is rated L1 with a "Proceed with Guardrails" recommendation. However, it is likely already covered by an on-label panic disorder indication, so it may be a label-mapping artifact rather than true repurposing. Verify it against the SAHPRA-approved label first.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

