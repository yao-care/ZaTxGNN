---
layout: default
title: Bupropion Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 0
---

# Bupropion Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Bupropion Hydrochloride: Repurposing Evaluation — No TxGNN Prediction Available

---

## One-Sentence Summary

Bupropion hydrochloride is a norepinephrine-dopamine reuptake inhibitor (NDRI) with established use in major depressive disorder and smoking cessation.
The current evidence pack contains **no TxGNN repurposing predictions** for this drug, meaning a formal drug repurposing evaluation cannot be completed at this stage.
Multiple blocking data gaps — including absent mechanism of action data, missing safety information, and no SAHPRA registration records — must be resolved before this candidate can advance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder; smoking cessation (from published sources — not confirmed in this evidence pack) |
| Predicted New Indication | Not available — no TxGNN prediction generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not evaluable |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Evaluation Cannot Proceed

The evidence pack for bupropion hydrochloride was submitted with an **empty predicted indications list**. Without a TxGNN-predicted target indication, there is no mechanistic hypothesis to evaluate, no clinical trial evidence to retrieve, and no literature corpus to assess. The pipeline that generates repurposing candidates did not produce output for this drug — most likely because the DrugBank ID is missing, which is required to anchor the drug to the TxGNN knowledge graph.

From publicly available knowledge, bupropion acts by inhibiting the reuptake of norepinephrine and dopamine and weakly antagonising nicotinic acetylcholine receptors. These mechanisms have driven interest in repurposing bupropion for conditions such as attention-deficit/hyperactivity disorder (ADHD), weight management, and sexual dysfunction — however, **none of these directions can be formally evaluated here** because no TxGNN score or evidence pack was generated.

Two blocking data gaps are formally recorded in the evidence pack:

- **DG001 (Blocking):** Professional Information (PI) warnings and contraindications are missing. This prevents even a basic first-pass safety screen.
- **DG002 (High):** Mechanism of action data was not retrieved from DrugBank. This prevents mechanistic plausibility analysis.

Until these gaps are resolved and the prediction pipeline is re-run with a valid DrugBank ID, this report cannot progress beyond the hold decision.

---

## South Africa Market Information

No SAHPRA registrations were found for bupropion hydrochloride in the current evidence pack (total licences: 0).

> **Important verification note:** This result should be independently confirmed against the [SAHPRA online medicines register](https://www.sahpra.org.za/). Bupropion-containing products such as **Wellbutrin XL** (antidepressant) and **Zyban** (smoking cessation) are known to be available in South Africa under Section 21 authorisations or full registration in other markets. The absence of records in this pack most likely reflects a data retrieval failure rather than a definitive absence from the South African market.

---

## Safety Considerations

> Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA.
>
> Based on published pharmacological data (not from this evidence pack), clinicians should note the following pending PI confirmation:
> - **Seizure risk:** Bupropion carries a dose-dependent risk of seizures; the incidence increases at doses above 450 mg/day.
> - **Eating disorder contraindication:** Contraindicated in patients with a current or prior diagnosis of anorexia nervosa or bulimia nervosa.
> - **Seizure disorder contraindication:** Contraindicated in patients with a history of seizure disorders.
> - **MAO inhibitor interaction:** Contraindicated with concurrent or recent use of monoamine oxidase inhibitors (MAOIs).
>
> These points require formal verification from the approved PI before any clinical or repurposing decision is made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated for bupropion hydrochloride in this evidence pack, making a formal drug repurposing evaluation impossible. The absence of a DrugBank ID is the most likely root cause and must be resolved first.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Retrieve the approved Professional Information (PI) from SAHPRA or a recognised pharmacopoeia source; extract warnings and contraindications.
- **Resolve DG002 (High):** Query DrugBank API using the drug name "bupropion hydrochloride" or its synonyms (bupropion, amfebutamone) to obtain the DrugBank ID (expected: DB01156) and MOA data.
- **Re-run TxGNN pipeline:** With a confirmed DrugBank ID, re-run the knowledge graph prediction to generate repurposing candidates and populate `predicted_indications`.
- **Confirm SAHPRA status:** Manually verify the South African register for current or historical bupropion product registrations.
- **Generate a new evidence pack (v5):** Once the above steps are complete, re-submit for full evaluation.

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any clinical application. Report adverse drug reactions to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

