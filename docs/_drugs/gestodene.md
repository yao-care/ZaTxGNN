---
layout: default
title: Gestodene
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Gestodene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Gestodene: From Contraception to Migraine Disorder

## One-Sentence Summary

Gestodene is a third-generation progestin used as a component of combined oral contraceptives (together with ethinylestradiol), and is not currently marketed in South Africa. The TxGNN model predicts it may be effective for **Migraine Disorder**, but the only supporting literature (**3 publications**, **0 clinical trials**) discusses cardiovascular/thromboembolic safety of oral contraceptives rather than migraine treatment efficacy — and combined hormonal contraceptives are in fact a relative contraindication in migraine with aura.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from South African registration data (component of combined oral contraceptives, per known pharmacology) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for Gestodene (MOA: Data Gap). Based on known pharmacology, Gestodene is a third-generation progestin, clinically used almost exclusively as part of combined oral contraceptive (COC) formulations containing ethinylestradiol. Its own market presence and indication history in South Africa could not be confirmed — there are no active SAHPRA registrations for this product.

The TxGNN prediction linking Gestodene to migraine disorder likely reflects a knowledge-graph association between "oral contraceptives" and "migraine" as frequently co-occurring clinical entities (e.g., migraine as a comorbidity or adverse effect discussed alongside OC use), rather than a genuine therapeutic mechanism. All three retrieved publications discuss cardiovascular and venous thromboembolic (VTE) risk associated with oral contraceptive use — they are safety literature, not efficacy literature.

Importantly, combined hormonal contraceptives containing estrogen are a well-recognized **relative contraindication** in patients with migraine with aura, due to an increased risk of ischemic stroke (per ACOG/WHO Medical Eligibility Criteria, Category 4). This directly contradicts the repurposing hypothesis rather than supporting it, and the same caution applies to the related "migraine with brainstem aura" prediction (rank 2).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10342951](https://pubmed.ncbi.nlm.nih.gov/10342951/) | 1998 | Review | Prescrire international | Cardiovascular risk of oral contraceptives is generally low, but rises with age >35, smoking, and hypertension — not related to migraine treatment |
| [9093141](https://pubmed.ncbi.nlm.nih.gov/9093141/) | 1997 | Case-control | Acta obstetricia et gynecologica Scandinavica | Examined how thrombotic risk factors influence oral contraceptive prescribing decisions |
| [8984464](https://pubmed.ncbi.nlm.nih.gov/8984464/) | 1996 | Review | The Practitioner | Discusses oral contraceptives and risk of deep vein thrombosis (DVT) |

None of the retrieved literature evaluates Gestodene for migraine treatment efficacy; all address contraceptive-related thromboembolic/cardiovascular safety.

---

## South Africa Market Information

No SAHPRA product registrations were found for Gestodene (market status: Not marketed; 0 total licenses).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: as a component of combined estrogen-progestin contraceptives, this drug class carries a known thromboembolic and ischemic stroke risk that is clinically relevant to the predicted indication (migraine with aura) — this should be treated as a safety flag pending confirmed PI data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The supporting literature addresses contraceptive safety risk rather than migraine treatment efficacy, and combined hormonal contraceptives are a recognized relative contraindication in migraine with aura — the evidence base does not support this repurposing hypothesis, and there is no clinical trial evidence.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) including warnings/contraindications (currently a Blocking data gap)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Literature or trial evidence directly evaluating a progestin/estrogen-progestin combination for migraine treatment efficacy (not just comorbidity/safety association)
- Clarification of TxGNN knowledge-graph path driving this prediction, to rule out a comorbidity-association artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

