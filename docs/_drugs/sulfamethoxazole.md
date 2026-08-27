---
layout: default
title: Sulfamethoxazole
parent: 僅模型預測 (L5)
nav_order: 418
evidence_level: L5
indication_count: 10
---

# Sulfamethoxazole
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

# Sulfamethoxazole: From Bacterial Infections to Acute Contagious Conjunctivitis

## One-Sentence Summary

Sulfamethoxazole is a sulfonamide antibacterial, most commonly used in combination with trimethoprim (co-trimoxazole) for bacterial infections. The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis**, but this direction is currently supported by only **1 publication** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (sulfonamide antibacterial; typically combined with trimethoprim) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold (currently at "Research Question" stage) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this candidate is not currently available. Based on known information, sulfamethoxazole is a sulfonamide antibacterial that inhibits bacterial dihydropteroate synthase, blocking folate synthesis; it is most often used in combination with trimethoprim (co-trimoxazole/TMP-SMX) to treat systemic bacterial infections. Its efficacy in bacterial infections is well established, and mechanistically it may be applicable to acute contagious conjunctivitis, which is frequently bacterial in origin.

There is also topical precedent within the sulfonamide class: sulfacetamide, a related sulfonamide, has long been used as a topical ophthalmic antibiotic for bacterial conjunctivitis, with an antimicrobial spectrum covering common conjunctivitis pathogens. This gives the TxGNN prediction some mechanistic plausibility.

However, the only supporting literature for this specific indication is a single retrospective cohort study on the bacteriology of childhood conjunctivitis — it characterizes causative organisms and susceptibility patterns but does not directly test sulfamethoxazole efficacy. No clinical trials, no route/formulation data (sulfamethoxazole is an oral/IV drug, not a topical ophthalmic product), and no direct comparative evidence currently exist for this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohort | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Retrospective analysis of childhood acute bacterial conjunctivitis in Western Greece, characterizing causative bacteria and antimicrobial susceptibility patterns; supports the general rationale for antibacterial treatment but does not directly evaluate sulfamethoxazole. |

## South Africa Market Information

Sulfamethoxazole is not currently registered or marketed in South Africa (0 SAHPRA registrations for this evidence pack).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, including warnings, contraindications, and drug interactions. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is a single indirect cohort study rather than direct evidence of sulfamethoxazole efficacy in conjunctivitis, and no clinical trials exist for this indication. This does not meet the bar for "Go" or even "Proceed with Guardrails."

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data from DrugBank
- SAHPRA-approved Professional Information — warnings and contraindications (currently a blocking data gap)
- Direct evidence (in vitro, preclinical, or clinical) of sulfamethoxazole or sulfacetamide efficacy specifically in bacterial conjunctivitis
- Route/formulation feasibility assessment, since sulfamethoxazole is currently only available as an oral/IV product, not a topical ophthalmic formulation
- Note: a separate predicted indication in this evidence pack ("post-bacterial disorder," rank 6) has substantially stronger evidence (L1, multiple completed Phase 3 RCTs of TMP-SMX) and may warrant its own evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

