---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 5
---

# Metformin
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

# Metformin: From Original Indication Not Confirmed to Focal Stiff Limb Syndrome

## One-Sentence Summary

> Metformin is internationally recognized as a first-line oral therapy for Type 2 Diabetes Mellitus, but **this evidence pack contains no confirmed original-indication or regulatory record** for the drug — it is currently **Not Marketed** with **zero registered products**.
> The TxGNN model's top prediction links metformin to **Focal Stiff Limb Syndrome**, a rare autoimmune neuromuscular disorder, with a prediction score of **99.45%**.
> However, **no clinical trials and no publications** currently support this — or any of the four other candidate indications returned in this batch — making this an L5 (model-prediction-only) signal with no external validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap — see DG002; commonly known internationally as Type 2 Diabetes Mellitus, but unconfirmed here) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% (rank 3,083 of full candidate list) |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for metformin in this evidence pack (data gap DG002, High severity). This blocks a proper mechanistic-relevance assessment.

Based on the model's own rationale text, the proposed link is weak and largely theoretical. Focal stiff limb syndrome sits on the stiff-person-syndrome spectrum, driven by anti-GAD65 autoantibodies that impair GABAergic neurotransmission and cause sustained focal muscle rigidity. Metformin's established mechanism (AMPK activation, suppression of hepatic gluconeogenesis) has no direct, established connection to GABAergic signalling or GAD65-mediated autoimmunity. The only proposed bridge — that AMPK activation may have general anti-inflammatory/immunomodulatory effects — is speculative and is not supported by any preclinical or clinical data in this pack.

In short: the prediction should be read as a **hypothesis-generating signal from the knowledge graph**, not as a mechanistically substantiated candidate. It warrants further literature/mechanistic review before any resources are committed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Metformin has **no active SAHPRA registration** recorded in this evidence pack (market status: Not Marketed; 0 licenses on file). No product/dosage-form table can be generated from current data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note:** Full SAHPRA PI warnings and contraindications are currently a *Blocking* data gap (DG001) — this prevents any Stage 1 (S1) safety pre-screen for metformin. This must be resolved before further evaluation of any predicted indication for this drug.

---

## Other Model-Predicted Indications in This Batch

For transparency, four additional candidates were returned in the same prediction run, all at evidence level L5 (Hold) with zero trials and zero publications:

| Rank | Disease | TxGNN Score | Notable Consideration |
|------|---------|-------------|------------------------|
| 2 | Classic stiff person syndrome | 99.45% | Same GAD65-mediated mechanism gap as rank 1 |
| 3 | Opsismodysplasia | 99.40% | Rare skeletal dysplasia (INPPL1/PI3K-PTEN pathway); connection to metformin's AMPK/mTOR pathway is highly speculative, no supporting data |
| 4 | Thiamine-responsive dysfunction syndrome | 99.40% | **Mechanistic red flag**: metformin is a known substrate/inhibitor of thiamine transporters (THTR-1/THTR-2). This direction is *opposite* to the therapeutic need and could theoretically worsen thiamine-transport-deficiency symptoms. This should be treated as a caution, not a candidate, regardless of score. |
| 5 | Drug-induced localized lipodystrophy | 99.06% | Pathology relates to *injection-site* reactions from other drugs; metformin is oral with no plausible route of mechanistic action here |

All five scores cluster tightly (99.06%–99.45%) across clinically unrelated, mostly ultra-rare conditions — this pattern is consistent with low discriminative confidence in this region of the model's output and should temper how much weight is placed on the score alone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Zero clinical trials and zero publications support any of the five predicted indications; evidence level is L5 (model prediction only) across the board.
- Two Blocking/High severity data gaps — SAHPRA PI warnings/contraindications (DG001) and mechanism of action (DG002) — prevent even a basic S1 safety pre-screen.
- The rank 4 candidate (thiamine-responsive dysfunction syndrome) shows a plausible mechanistic *conflict* (metformin may inhibit thiamine transport), which is a safety caution rather than supporting evidence — a reminder that high TxGNN scores alone should not drive prioritization.
- Metformin is currently unregistered in South Africa (Not Marketed, 0 SAHPRA licenses), which is itself a prerequisite gap for any repurposing pathway.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications) for metformin (resolves DG001)
- Confirmed mechanism of action and original indication data from DrugBank or an authoritative source (resolves DG002)
- Targeted literature search (beyond automated PubMed/ClinicalTrials/ICTRP queries returning zero hits) for any case reports or mechanistic studies linking metformin to stiff-person-syndrome-spectrum disorders
- Specialist (neurology/rare disease) review of biological plausibility before considering any further evaluation stage
- Explicit safety review of the thiamine-transporter interaction before rank 4 is considered further, given the directionally conflicting mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

