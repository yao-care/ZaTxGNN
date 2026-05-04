---
layout: default
title: Cyclizine Tartrate
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 0
---

# Cyclizine Tartrate
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

# Cyclizine Tartrate: Drug Repurposing Evaluation — No Predicted Indication

## One-Sentence Summary

Cyclizine tartrate is an antihistamine (H1 receptor antagonist) of the piperazine class, traditionally used as an antiemetic for the prevention and treatment of nausea, vomiting, and motion sickness. The TxGNN model did **not generate any predicted new indications** for this compound, and **no clinical trial or literature evidence** was available in the evidence pack. This report documents the current data landscape and outlines steps needed before any repurposing assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (known use: antiemetic / motion sickness) |
| Predicted New Indication | **None** — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | **L5** (No model prediction, no clinical studies in pack) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Was No Prediction Generated?

Cyclizine tartrate is a first-generation antihistamine that acts as an H1 receptor antagonist with additional antimuscarinic properties. It is widely used internationally for the management of nausea, vomiting, and vertigo, particularly post-operative nausea and motion sickness. Although cyclizine has a well-established pharmacological profile, the TxGNN knowledge graph–based prediction pipeline returned an empty set of candidate indications.

There are several possible reasons for this outcome. First, cyclizine tartrate could not be mapped to a DrugBank identifier (`drugbank_id: null`), which is a prerequisite for linking the compound into the TxGNN knowledge graph. Without a valid node in the graph, the model cannot traverse drug–gene–disease relationships to generate repurposing hypotheses. Second, cyclizine is not currently registered with SAHPRA (0 licences), meaning there is no local regulatory anchor from which to build an indication profile.

To enable future predictions, the DrugBank mapping must be resolved. Cyclizine hydrochloride (the more common salt form) is listed in DrugBank as **DB01176** — it is possible that the tartrate salt was not matched due to salt-form variation. Re-running the mapping pipeline with the parent compound name "cyclizine" or the hydrochloride salt may resolve this gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in the evidence pack.

---

## Literature Evidence

Currently no related literature available in the evidence pack.

---

## South Africa Market Information

Cyclizine tartrate has **no current SAHPRA registrations**. The compound is not listed on the South African Essential Medicines List (EML).

> **Note:** Cyclizine hydrochloride (the hydrochloride salt form) is used in several countries and may be available through Section 21 applications in South Africa. Healthcare professionals requiring this medicine should consult SAHPRA's Section 21 (unregistered medicines) process.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information, where available. As cyclizine tartrate is not currently registered in South Africa, safety data should be sourced from international references (e.g., UK BNF, WHO). Report adverse drug reactions to SAHPRA.

> **General safety profile (from international references):**
> - Common adverse effects include drowsiness, dry mouth, blurred vision, and urinary retention (antimuscarinic effects)
> - Caution in patients with angle-closure glaucoma, prostatic hypertrophy, and pyloric stenosis
> - May potentiate CNS depressant effects of alcohol and sedatives

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN repurposing predictions were generated due to failure to map cyclizine tartrate to a DrugBank knowledge graph node. Without a valid drug–graph linkage, the prediction pipeline cannot operate. Additionally, the compound has no SAHPRA registration, no local safety data, and no mechanism of action data was provided in the evidence pack.

**To proceed, the following is needed:**
- **Resolve DrugBank mapping**: Re-attempt mapping using the parent compound "cyclizine" or the hydrochloride salt (DrugBank ID: DB01176) to establish a knowledge graph node
- **Obtain mechanism of action data**: Query DrugBank API for H1 antagonist / antimuscarinic MOA details
- **Re-run TxGNN prediction pipeline**: Once the DrugBank mapping is resolved, re-execute KG and DL predictions
- **Assess SAHPRA registration pathway**: Determine if cyclizine (any salt form) is accessible via Section 21 or if a registration application is warranted
- **Collect safety profile**: Obtain full safety data from international regulatory sources (MHRA, TGA, or EMA)

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All findings should be interpreted by qualified healthcare professionals.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

