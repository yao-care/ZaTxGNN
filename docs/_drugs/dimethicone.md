---
layout: default
title: Dimethicone
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Dimethicone
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

The txgnn-pipeline skill confirms the workflow context. The report generation instructions are defined in the system prompt (v5). Proceeding to generate the full report now.

---

# Dimethicone: From Skin Protection to Insomnia

## One-Sentence Summary

Dimethicone is a synthetic silicone polymer widely used as a topical skin protectant and barrier agent, with secondary use as an antifoaming component in gastrointestinal products.
The TxGNN model predicts it may have activity in **Insomnia**, with broader predictions also spanning a cluster of cataract subtypes and diabetic retinopathy.
However, supporting evidence is extremely limited: **0 clinical trials** and **0 publications** directly address the insomnia indication, and the sole trial identified carries a Grade C (not relevant) rating — yielding an overall evidence level of **L5** for all predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Topical skin protectant / barrier agent; antifoaming agent (no SAHPRA-registered indication on record) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Dimethicone is a high-molecular-weight siloxane polymer whose clinical properties are entirely physical in nature: it forms a hydrophobic, lubricating film on biological surfaces, acting as a moisture barrier and protectant. It does not bind to biological receptors, enzymes, or ion channels in any established pharmacological sense. Its antifoaming action in the gut is similarly mechanical — it reduces surface tension of gas bubbles — rather than receptor-mediated.

Insomnia is a CNS condition managed through drugs targeting specific receptor systems: GABA-A receptors (benzodiazepines, Z-drugs), histamine H₁ receptors (doxylamine), melatonin MT₁/MT₂ receptors (ramelteon), and orexin OX₁/OX₂ receptors (suvorexant). There is no known pharmacological intersection between these CNS targets and Dimethicone's physicochemical properties. The TxGNN prediction most likely originates from an indirect knowledge graph pathway — for example, skin barrier dysfunction → systemic inflammation → sleep disruption — which represents a highly attenuated biological association rather than a direct mechanistic rationale.

Regarding the cataract predictions (Ranks 2–9): six distinct cataract subtypes share an identical TxGNN score (0.9271), which is a clear indicator of a **group effect** — the model is treating all cataract subtypes as a single node cluster rather than generating disease-specific predictions. This substantially reduces confidence in these as independent signals. Critically, the only established relationship between silicone-based compounds and cataract is **adverse in direction**: high-viscosity silicone oil used in vitreoretinal surgery can cause secondary cataract when it emulsifies and migrates to the anterior chamber. This biological contradiction argues strongly against pursuing any cataract indication for Dimethicone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Completed | 74 | Topical and oral skin health regimen (Inner Calm + Super Calm products). Dimethicone was used as a topical skin barrier component. **No insomnia endpoint** — study assessed skin redness, sensitivity, and reactionary skin appearance only. Grade C relevance: does not support insomnia indication. |

> **Important note:** This is the only trial identified across all 10 predicted indications combined. No trials were found for any cataract subtype or for severe nonproliferative diabetic retinopathy. The single trial found is not relevant to any predicted indication.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications (insomnia, all cataract subtypes, severe nonproliferative diabetic retinopathy).

---

## South Africa Market Information

Dimethicone (DB11074) is currently **not registered with SAHPRA** and has no approved products on the South African market.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No SAHPRA-registered products found | — | — |

> SAHPRA registration and an approved Professional Information (PI) document would be prerequisites before any clinical application in South Africa. The Essential Medicines List (EML) status cannot be assessed in the absence of any registration.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

> No drug-drug interaction data, key warnings, or contraindications were available in this evidence pack. A formal safety review using the full PI is mandatory before any clinical decision-making. Prescribers should note that the only currently available clinical safety data for Dimethicone relates to its use as a topical skin agent — systemic safety data for any new route of administration would need to be established de novo.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are rated **L5** (model prediction only), with no direct clinical trial support, no published literature, no plausible pharmacological mechanism, and no SAHPRA registration. The primary prediction (insomnia) lacks CNS receptor-level rationale for a physical barrier polymer; the cataract cluster (Ranks 2–9) displays identical prediction scores consistent with a model group-effect artefact; and the only known silicone–cataract relationship is adversarial. This candidate does not currently meet the threshold for further clinical development under any of the predicted indications.

**To proceed, the following is needed:**

- **MOA data retrieval** (Data Gap DG002): Query DrugBank API to determine whether any systemic biological targets have been identified for Dimethicone beyond its physical barrier properties
- **SAHPRA PI and safety data** (Data Gap DG001): Obtain and review the full product safety profile before any indication can advance to S1 safety evaluation
- **Model artefact investigation**: Reassess TxGNN predictions using disease-subtype-aware filtering to eliminate group-effect scores (the uniform 0.9271 cataract cluster)
- **Independent pharmacological review**: Engage a clinical pharmacologist to evaluate whether any indirect systemic pathway (e.g., microbiome, skin-gut-brain axis) could provide a biologically coherent rationale for CNS or ocular activity
- **Preclinical hypothesis generation**: If a mechanistic rationale is identified, define a targeted in vitro or in vivo study design before committing to clinical development resources

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. Data cut-off: 2026-04-20.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

