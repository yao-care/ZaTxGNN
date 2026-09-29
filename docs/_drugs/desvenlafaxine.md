---
layout: default
title: Desvenlafaxine
parent: Model Prediction Only (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) and the active metabolite of venlafaxine. It is used internationally for major depressive disorder.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**.
The evidence is indirect: **2 clinical trials** and **4 publications** were retrieved, but none tests desvenlafaxine in OCD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record. Published literature describes major depressive disorder as its established use. |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (class-level and parent-compound support only; no desvenlafaxine OCD study) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Desvenlafaxine is an SNRI, and it is the O-desmethyl metabolite of venlafaxine. It is established for depression, and mechanistically it may be applicable to OCD.

Blocking serotonin reuptake is the core mechanism of OCD drug treatment, which relies on SSRIs and clomipramine. Desvenlafaxine's serotonergic action therefore gives the prediction a plausible biological basis.

There are two important limits. First, the support comes from the drug class and from the parent compound venlafaxine, not from desvenlafaxine itself. Second, SNRIs are less serotonin-selective than SSRIs, so efficacy in OCD is uncertain. The 99.91% score should be read as a model signal, not as evidence of efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Adjunctive troriluzole vs placebo in OCD patients with an inadequate response to an SSRI, clomipramine, venlafaxine or desvenlafaxine. The tested drug is troriluzole, so this is not direct evidence for desvenlafaxine. |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Pilot study of desvenlafaxine and functional recovery in postpartum depression. The disease is not OCD, so it is not direct evidence either. |

No SANCTR or PACTR registrations were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | J Clin Psychopharmacol | First randomised double-blind comparison of an SNRI (venlafaxine) with paroxetine in 150 OCD patients. It assessed efficacy and tolerability. This is parent-compound evidence, not desvenlafaxine. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Reviews double-blind studies of serotonergic antidepressants in OCD, supporting a key role for the serotonin system in OCD. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Review of postpartum depression. It notes that PPD can later lead to OCD and anxiety. This is only an indirect link. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical study | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder. Marginal relevance to desvenlafaxine in OCD. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/1.2/0505 | Deslafore Xr 50 | Tablet (oral) | Not stated in the available record |

Essential Medicines List (EML) status is not available in the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug interaction query returned no results. This means no data were found, not that no interactions exist.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial has tested desvenlafaxine in OCD. The supporting evidence is limited to the SNRI class and to venlafaxine, and the SNRI's weaker serotonin selectivity makes efficacy uncertain. The SAHPRA safety information is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert, to extract warnings and contraindications (a blocking gap).
- Mechanism of action data from DrugBank.
- Controlled data on desvenlafaxine itself in OCD, for example a systematic search or a pilot RCT.
- A check of local guidelines and EML status for OCD treatment.

**Other predictions in this pack:**
- Dysthymic disorder is the most actionable, with three related trials, two of them directly on desvenlafaxine (small, open-label or with no results provided).
- Melancholia is a subtype of major depressive disorder. Its L1 grade comes from the parent MDD evidence, so it is an overlap with the approved use rather than new repurposing.
- The personality disorder predictions all have the same score and no evidence. They are likely knowledge-graph artefacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

