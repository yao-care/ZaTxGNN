---
layout: default
title: Diltiazem Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 0
---

# Diltiazem Hydrochloride
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

# Diltiazem Hydrochloride: Drug Repurposing Evaluation — Critical Data Gaps Identified

## One-Sentence Summary

Diltiazem Hydrochloride is an established cardiovascular agent; however, this Evidence Pack contains no mechanism of action data, no SAHPRA registration records, and — critically — no TxGNN-predicted repurposing indications.
Without these foundational inputs, no repurposing direction can be assessed at this stage.
This report documents the current data status and outlines the steps required before a full evaluation can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registration data available |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not applicable — no predictions exist |
| South Africa Market Status | Not Registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## South Africa Market Information

Diltiazem Hydrochloride currently has **no active SAHPRA registrations** in South Africa.

Practical implications for healthcare professionals:

- The product is not available through the formal medicines regulatory pathway.
- Any clinical or research use would require a **Section 21 authorisation** (unregistered medicine application) from SAHPRA before the product may be supplied or used.
- Prescribers and pharmacists should consult SAHPRA's online portal to confirm current registration status before sourcing this product.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Diltiazem Hydrochloride is incomplete in several critical areas: the TxGNN pipeline produced no repurposing predictions, no SAHPRA registrations exist, the mechanism of action is unresolved, and no safety profile (warnings or contraindications) has been retrieved. A repurposing evaluation cannot be meaningfully conducted in the absence of these inputs.

**To proceed, the following is needed:**

1. **Resolve Blocking Data Gap (DG001) — Prescribing Information:**
   Obtain the full PI/package insert (including key warnings and contraindications) from the originator's regulatory dossier or an equivalent approved national medicine authority (e.g., EMA, FDA, or TGA-sourced PI as a reference document). This is a blocking prerequisite for safety screening.

2. **Resolve High-Priority Data Gap (DG002) — Mechanism of Action:**
   Retrieve MOA data via the DrugBank API. A query was logged as successful (query log ID 1, result count: 1) but no DrugBank ID was returned — re-run the lookup to capture the correct DrugBank entry and full pharmacological profile.

3. **Re-run TxGNN Prediction Pipeline:**
   Once Diltiazem Hydrochloride is correctly mapped to a DrugBank ID, re-run both the knowledge graph (KG) and deep-learning (DL) prediction models to generate repurposing candidates with scored indications.

4. **SAHPRA Registration Pathway:**
   If a repurposing indication is confirmed with sufficient evidence, initiate the appropriate SAHPRA pathway — either a new registration application or a Section 21 unregistered medicine authorisation — depending on the urgency and clinical context.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

