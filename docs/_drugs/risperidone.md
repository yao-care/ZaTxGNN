---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 400
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Risperidone: From Registered Antipsychotic (Indication Text Not Available) to Gaze Palsy, Familial Horizontal, with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an atypical antipsychotic with 7 SAHPRA registrations, but the approved-indication text is not recorded in the supplied data.
The TxGNN model predicts it may be effective for **familial horizontal gaze palsy with progressive scoliosis** (an ultra-rare ROBO3-related disorder), with **0 clinical trials** and **0 publications** supporting this prediction.
It is a model-only signal with no plausible mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records supplied |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From general pharmacology, risperidone acts mainly by antagonising dopamine D2 and serotonin 5-HT2A receptors, and it is used for psychiatric conditions.

The predicted disease is a rare developmental disorder linked to ROBO3. It affects eye-movement pathways and the spine. Nothing in risperidone's D2/5-HT2A pharmacology points to a role in this condition. The very high TxGNN score most likely reflects proximity in the knowledge graph rather than a therapeutic rationale. This prediction should be treated as a computational artefact unless independent evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Showing 5 of 7 registrations. The approved-indication text is not included in the supplied records.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/2.6.5/0362 | Zoxadon ODT 0.5 mg | Orally disintegrating tablet | Not stated in supplied record |
| Reg. No. A40/2.6.5/0706 | Perizal | Tablet | Not stated in supplied record |
| Reg. No. 42/2.6.5/0792 | Risnia | Tablet | Not stated in supplied record |
| Reg. No. 44/2.6.5/0003 | Perida 0.5 mg | Tablet | Not stated in supplied record |
| Reg. No. 41/2.6.5/1056 | Rutra 1 mg/ml Solution | Oral solution | Not stated in supplied record |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no trials, no publications and no mechanistic rationale. The score reflects graph proximity only, so there is no basis to pursue it.

**To proceed, the following is needed:**
- An independent biological rationale linking risperidone to ROBO3-related pathways, and any supporting studies
- The SAHPRA Professional Information (PI), to confirm approved indications and safety data
- Mechanism of action data (MOA) from DrugBank

**Other predictions in the same Evidence Pack that merit review instead:**

| Predicted Indication | Evidence Level | Supporting Evidence | Pack Recommendation |
|------|------|------|------|
| Major affective disorder | L1 | Phase 3 RCTs in paediatric bipolar disorder (NCT00057681, NCT00221403) and several meta-analyses of antipsychotic augmentation in treatment-resistant depression | Proceed with Guardrails |
| Trichotillomania | L4 | Case reports and small case series (1997–2021) of risperidone added to SSRIs, with no RCT | Research Question |
| Phelan-McDermid syndrome | L4 | A review, a zebrafish study and a case study, with no controlled human data | Research Question |

Major affective disorder is likely already an approved use of risperidone, so it may not be true repurposing. The approved indications should be verified against the PI, and the sub-indication (bipolar mania, paediatric bipolar disorder or depression augmentation) should be specified. Any use would need metabolic, prolactin and extrapyramidal monitoring, with extra caution in children and older adults.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

