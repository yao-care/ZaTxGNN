---
layout: default
title: Gestodene
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
---

# Gestodene
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

# Gestodene: From Hormonal Contraception to Migraine Disorder

## One-Sentence Summary

Gestodene is a progestin used in combined oral contraceptives, and all three SAHPRA-registered products are contraceptive brands. The TxGNN model predicts it may be relevant to **migraine disorder**, but there are **0 clinical trials** and **3 publications**, none of which show a therapeutic benefit. The retrieved papers describe cardiovascular and thrombotic risk, which is a safety concern rather than support for repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormonal contraception (inferred from the drug class and registered product names; no approved indication text was supplied) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 (no studies of gestodene in migraine; the retrieved papers address risk, not benefit. The automated pack grade was L4.) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gestodene is a progestin component of combined hormonal contraceptives, and its role in contraception is established.

The prediction is not well supported. The high score (0.94) has no therapeutic evidence behind it. The retrieved literature covers thrombotic and cardiovascular risk with oral contraceptives. Migraine, especially with aura, is a known risk factor for ischaemic stroke and interacts with estrogen-containing contraceptives. The graph link is more likely a disease co-occurrence artefact than a treatment signal.

The other top predictions do not offer a stronger case:
- **Migraine with brainstem aura** (score 94.35%) raises the same stroke-risk concern.
- **Acne** (score 91.31%) is the only one flagged as a research question. Combined oral contraceptives can reduce androgen-driven sebum production, but this is class-level reasoning that applies mainly to estrogen-progestin combinations, and no gestodene-specific data were supplied.
- **Primary cutaneous T-cell lymphoma, seborrheic keratosis, vulvar inverted follicular keratosis, mycotic corneal ulcer and kyphoscoliotic heart disease** have no trials, no literature and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10342951](https://pubmed.ncbi.nlm.nih.gov/10342951/) | 1998 | Review | Prescrire International | Cardiovascular risk of oral contraceptives is low in non-smoking women under 35 with normal blood pressure. Smoking over 10 cigarettes a day and hypertension raise coronary risk substantially in women over 35. |
| [9093141](https://pubmed.ncbi.nlm.nih.gov/9093141/) | 1997 | Case-control | Acta Obstet Gynecol Scand | Examined whether oral contraceptives are prescribed preferentially according to thrombotic risk factors. |
| [8984464](https://pubmed.ncbi.nlm.nih.gov/8984464/) | 1996 | Review | The Practitioner | Oral contraceptives and the risk of deep vein thrombosis. |

None of these papers assess migraine treatment. They are safety-oriented.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 52/18.8/1019 | Dyolafem | Tablet |
| Reg. No. W/21.8.2/317 | Triodene Ed | Sct (as listed in the registration data) |
| Reg. No. W/18.8/11 | Minulette | Tablet |

Approved indication text and Essential Medicines List status were not supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Migraine with aura is generally a caution or contraindication for combined hormonal contraceptives because of stroke risk. Any use of gestodene-containing products in migraine patients would need careful specialist review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high model score is not backed by any trial or literature showing benefit. The available evidence points to a vascular safety concern in migraine, particularly migraine with aura.

**To proceed, the following is needed:**
- The SAHPRA package insert warnings and contraindications (a blocking gap, so safety screening cannot start without it)
- Mechanism of action data from DrugBank
- A targeted literature search on gestodene-containing contraceptives in migraine, including menstrual migraine, and separately in acne
- Confirmation of the registered indications for the three SAHPRA products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

