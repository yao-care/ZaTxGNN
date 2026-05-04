---
layout: default
title: Codeine Phosphate
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 0
---

# Codeine Phosphate
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

# Codeine Phosphate: Repurposing Evaluation — No TxGNN Prediction Generated

## One-Sentence Summary

Codeine Phosphate is a well-established opioid analgesic and antitussive, historically used for mild-to-moderate pain relief and cough suppression.
The TxGNN model **did not generate a repurposing prediction** for this candidate — the predicted indications array is empty, likely due to unresolved data gaps in drug identity and regulatory linkage.
This report documents the current evaluation status and outlines the remediation steps required before a prediction can be assessed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain relief (mild-to-moderate); cough suppression — based on pharmacological class knowledge; no formal regulatory text available in this pack |
| Predicted New Indication | None generated |
| TxGNN Prediction Score | Not applicable |
| Evidence Level | L5 — Model prediction not available; no supporting studies retrievable |
| South Africa Market Status | Not marketed (no SAHPRA registration on record) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN knowledge-graph pipeline requires a valid **DrugBank ID** to anchor a drug node within the heterogeneous knowledge graph. For this candidate:

- `drugbank_id` is **null** — the drug could not be linked to a graph node.
- `original_indications` is empty — no approved-indication text was available to seed the disease-mapping step.
- The MOA field is absent — mechanistic edges within the graph could not be traversed.

Without these inputs, TxGNN cannot compute a drug–disease similarity score, and the predicted indications array remains empty. This is a **pipeline failure**, not a finding of no repurposing potential.

**What is known from pharmacology:**
Codeine Phosphate is a phenanthrene-class opioid prodrug. After oral administration, approximately 5–10% is O-demethylated by **CYP2D6** to morphine, which produces analgesia via agonism at μ-opioid receptors in the CNS and peripheral tissues. The remaining compound undergoes glucuronidation. Its antitussive effect is mediated centrally in the cough centre of the medulla.

This mechanism is relevant to potential repurposing discussions (e.g., opioid-induced constipation, palliative breathlessness, diarrhoea-predominant IBS), but no formal TxGNN score exists to guide this evaluation at present.

> **South Africa-specific note:** African populations have a higher prevalence of the CYP2D6 ultra-rapid metaboliser phenotype compared to European populations. This significantly affects codeine's safety profile and would be a critical consideration in any repurposing pathway.

---

## Clinical Trial Evidence

Currently no related clinical trial evidence is retrievable — no predicted indication was generated to drive the evidence query.

---

## Literature Evidence

Currently no related literature is retrievable for the same reason.

---

## South Africa Market Information

Codeine Phosphate has **zero active SAHPRA product registrations** on record in this Evidence Pack. No registration table can be produced.

> Note: Codeine-containing compound preparations have historically been available in South Africa under various schedules. The absence of registrations in this dataset may reflect a data linkage gap (e.g., the active ingredient is registered under brand-name compound products not yet mapped) rather than a true absence from the South African market. This should be verified directly against the SAHPRA online register before drawing regulatory conclusions.

---

## Safety Considerations

No SAHPRA-approved Professional Information text was retrievable for this candidate. Please refer to the **SAHPRA-approved Professional Information (PI)** for all warnings, contraindications, and precautions. Report adverse drug reactions to **SAHPRA** via the MedSafety online reporting portal.

> **Clinician reminder:** Codeine is a controlled substance (Schedule 4 in South Africa). Key risks include respiratory depression, dependence, and unpredictable toxicity in CYP2D6 ultra-rapid metabolisers. It is **contraindicated in children under 12** and in breastfeeding mothers. These are general pharmacological considerations — not derived from the Evidence Pack data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline could not generate a repurposing prediction because the DrugBank identifier is missing, leaving the drug unlinked in the knowledge graph. Without a prediction score or predicted indication, there is no repurposing candidate to evaluate, and a Go/Guardrails decision cannot be responsibly made.

**To proceed, the following is required:**

- [ ] **Resolve DrugBank ID** — Codeine Phosphate maps to DrugBank ID `DB00318`; this should be populated in the pipeline's drug master record and the prediction re-run
- [ ] **Retrieve SAHPRA-registered product list** — Search the SAHPRA online register for codeine-containing products to establish the true local regulatory baseline
- [ ] **Download and parse the SAHPRA-approved PI** — Required to populate safety warnings and contraindications (currently a Blocking data gap per DG001)
- [ ] **Confirm CYP2D6 pharmacogenomics policy** — Given the South African population's metaboliser profile, any repurposing pathway must include a pharmacogenomics risk assessment
- [ ] **Re-run TxGNN prediction** after DrugBank linkage is confirmed, then generate a new Evidence Pack (v5+) for formal review

---

*This report was generated from Evidence Pack v4 (data cut-off: 2026-04-05). Results are for research purposes only and do not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

