---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

# Trimethoprim: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a dihydrofolate reductase (DHFR) inhibitor antibacterial agent, most widely known clinically for treating bacterial urinary tract and other susceptible infections. The TxGNN model's top-ranked prediction for this drug is **punctate epithelial keratoconjunctivitis**, but currently **no clinical trials and no published literature** support this specific link, and the drug is not registered in South Africa.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in this dataset (no SAHPRA-equivalent registration on file; trimethoprim is internationally used for susceptible bacterial infections, e.g. urinary tract infections) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trimethoprim is not available in this evidence pack. Based on general pharmacology knowledge, trimethoprim inhibits bacterial dihydrofolate reductase (DHFR), blocking folate synthesis and thereby inhibiting bacterial replication — an antibacterial mechanism, not an antiviral or immunomodulatory one.

Punctate epithelial keratoconjunctivitis is, per the evidence pack's own rationale, most commonly caused by viral pathogens (e.g. adenovirus) or by Thygeson's superficial punctate keratitis — neither of which is a bacterial process. There is therefore no direct mechanistic correspondence between trimethoprim's antibacterial action and the underlying pathology of this condition.

The TxGNN score (99.57%) reflects a strong graph-embedding association, but this is a knowledge-graph-derived signal only — it is not corroborated by any clinical trial or literature evidence in this dataset. This is why the evidence level is rated L5 (model prediction only) and the recommendation is **Hold**.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## South Africa Market Information

Trimethoprim currently has no SAHPRA registration on file and is not marketed in South Africa (0 registered licenses).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on a knowledge-graph model score, with no clinical trial or literature evidence, and the proposed mechanism (antibacterial) does not correspond to the typically viral/non-bacterial etiology of this condition. Combined with the absence of any South African market presence, there is currently no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (DrugBank query, per data gap DG002)
- SAHPRA-approved PI warnings and contraindications (per data gap DG001, currently blocking safety pre-screening)
- Any future clinical or observational evidence specifically linking trimethoprim to this ocular condition

**Note for reviewers:** This evidence pack also screened 9 other candidate indications for trimethoprim. Notably, **conjunctivitis (bacterial)** (rank 2, TxGNN score 99.17%) is supported by a completed Phase 4 head-to-head RCT ([NCT00581542](https://clinicaltrials.gov/study/NCT00581542), Polytrim [trimethoprim + polymyxin B] vs. moxifloxacin, n=124) and carries an L1 evidence level with a "Proceed with Guardrails" recommendation. Given its markedly stronger evidence base and mechanistic plausibility, that candidate may warrant a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

