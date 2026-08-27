---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 5
---

# Rilpivirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

使用 txgnn-pipeline 技能相關工作流程不適用於此任務（純粹是依既定 evidence pack 產出報告，非執行預測/訓練流程），故直接依 prompt 規格產出。

---

# Rilpivirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) with an established role in HIV-1 antiretroviral therapy (referenced repeatedly within this evidence pack's rationale fields, though not confirmed via South Africa regulatory records). The TxGNN model's top-ranked prediction points to **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, non-human indication — supported by only **1 preclinical publication** and **0 clinical trials**.

> **Note for reviewers:** This same evidence pack also contains two far stronger, clinically relevant candidates — *AIDS related complex* and *congenital HIV* — each backed by L1-level evidence (multiple completed Phase 3 RCTs). These represent extensions of rilpivirine's already-established antiretroviral role rather than a genuinely new indication, and warrant separate consideration from the FIV signal discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in South Africa regulatory data (no SAHPRA licenses on record); evidence pack rationale text repeatedly references HIV-1 infection / antiretroviral therapy as rilpivirine's established use |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap requiring a DrugBank API query). Based on the information available in this evidence pack, rilpivirine is an NNRTI that inhibits the reverse transcriptase enzyme of HIV-1.

FIV (feline immunodeficiency virus) causes a lentiviral, AIDS-like syndrome in cats that is structurally related to HIV. The single supporting publication (PMID 38031646) performed biochemical and structural comparisons of NNRTIs — including nevirapine, efavirenz, and rilpivirine — against both feline and human reverse transcriptase, exploring whether human NNRTIs could bind and inhibit the feline enzyme.

This is a cross-species mechanistic hypothesis, not a human therapeutic indication. The evidence itself is explicit that FIV "is not a human disease, and only in-vitro structural-level evidence exists — no in-vivo animal or clinical data." As such, this prediction has no direct bearing on human formulary or clinical decisions in South Africa, and should be understood as a research signal (potential veterinary application) rather than a repurposing candidate for SAHPRA review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical | Journal of Veterinary Science | Biochemical/structural comparison of NNRTIs (nevirapine, efavirenz, rilpivirine) against feline vs. human reverse transcriptase, exploring potential for treating FIV-infected cats; no effective FIV treatment currently exists |

## South Africa Market Information

Rilpivirine is currently not marketed in South Africa. No SAHPRA registrations are on record (0 licenses), and no approved indication text is available from South Africa regulatory data.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A Blocking-severity data gap (TFDA product-label warnings/contraindications) currently prevents even a preliminary safety screen (S1 stage) for this candidate.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (feline AIDS) is a non-human, veterinary indication supported by a single preclinical structural-comparison study with no clinical trial evidence and no confirmed South African market presence — it does not meet the threshold to advance past initial screening. The evidence level (L4) and TxGNN decision stage (S0) both confirm this is model-signal-only, not repurposing-ready evidence.

**To proceed, the following is needed:**
- Clarify with the requesting team whether this evaluation should target the FIV/veterinary signal, or be redirected to the two substantially stronger human-relevant candidates in the same pack (AIDS related complex; congenital HIV — both L1 evidence, "Proceed with Guardrails")
- Product label / warnings and contraindications data (currently a Blocking data gap)
- Detailed mechanism of action data from DrugBank
- Confirmation of rilpivirine's South Africa registration/market status, since 0 SAHPRA licenses are currently on record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

