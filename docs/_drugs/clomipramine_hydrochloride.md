---
layout: default
title: Clomipramine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 0
---

# Clomipramine Hydrochloride
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

# Clomipramine Hydrochloride: Repurposing Assessment — Insufficient Evidence Pack Data

## One-Sentence Summary

Clomipramine hydrochloride is a tricyclic antidepressant (TCA) classically used for obsessive-compulsive disorder (OCD), major depressive disorder, and related conditions. The current Evidence Pack contains **no TxGNN predictions** and carries two unresolved data gaps of Blocking/High severity, preventing a meaningful repurposing evaluation from being completed. This report documents what is available, identifies what is missing, and recommends actions before any repurposing pathway can be assessed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Evidence Pack (see note below) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | Not available |
| Evidence Level | Unable to determine — no predictions present |
| South Africa Market Status | Not registered |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

> **Note:** While the Evidence Pack does not populate original indications, clomipramine hydrochloride is internationally recognised (DrugBank DB01242) as a TCA approved for OCD, major depressive disorder, panic disorder, phobias, and cataplexy associated with narcolepsy. This contextual background is drawn from published pharmacological sources, not from the Evidence Pack data.

---

## Why No Predictions Are Available

The TxGNN prediction pipeline did not return any repurposing candidates for this drug. Based on the Evidence Pack metadata, at least two factors likely prevented prediction generation:

**1. Missing DrugBank ID**
The `drugbank_id` field is null. TxGNN relies on DrugBank identifiers to anchor a drug within the knowledge graph (KG). Without a valid DrugBank node, no drug–disease links can be traversed or scored. The internationally assigned ID for clomipramine is **DB01242** — confirming this mapping in the pipeline should resolve this blocker.

**2. Missing Mechanism of Action**
MOA data is listed as unavailable. While MOA is not strictly required to *run* the KG prediction, its absence prevents downstream mechanistic plausibility analysis, which is a key step in the repurposing rationale narrative.

**3. No SAHPRA Registrations**
Zero active registrations with SAHPRA were found. Clomipramine is registered in numerous jurisdictions under brand names including *Anafranil*, and the absence of South African registration should be independently verified — it may reflect a data retrieval gap rather than a true absence from the South African market.

---

## South Africa Market Information

No SAHPRA-registered products were returned for clomipramine hydrochloride in the current Evidence Pack. A manual verification against the SAHPRA online register is recommended before concluding that no locally registered product exists.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety reporting system.

> **Note on known safety profile (international sources):** Clomipramine belongs to the tricyclic antidepressant class and carries well-characterised risks including QTc prolongation, anticholinergic effects (urinary retention, constipation, dry mouth), sedation, lowered seizure threshold, and black-box warnings around suicidality in paediatric and young adult populations. These are not drawn from the Evidence Pack and must be verified against the approved South African PI before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no TxGNN predictions were generated, the DrugBank mapping is absent, mechanism of action data is unavailable, and SAHPRA registration status is unconfirmed. There is insufficient evidence to evaluate any repurposing pathway at this time.

**To proceed, the following is needed:**

1. **Confirm DrugBank ID** — Map clomipramine hydrochloride to DrugBank DB01242 and re-run the TxGNN prediction pipeline
2. **Retrieve SAHPRA PI** — Download the approved Professional Information (PI) document from the SAHPRA website to populate warnings, contraindications, and indication text
3. **Verify South African market status** — Cross-check SAHPRA's online medicine register directly for clomipramine-containing products (including generics)
4. **Re-run predictions** — Once DrugBank mapping is confirmed, re-run KG and DL prediction modules to generate a ranked list of repurposing candidates
5. **Initiate evidence collection** — After candidates are generated, run ClinicalTrials.gov, PubMed, and SANCTR/PACTR searches for the top-ranked indication
6. **Check Essential Medicines List (EML) status** — Confirm whether clomipramine or its class appears on the South African EML, which would affect access and formulary planning

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

