---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

---

## One-Sentence Summary

Insulin Lispro is a rapid-acting insulin analogue globally established for the management of Type 1 and Type 2 diabetes mellitus, though it is currently not registered with SAHPRA in South Africa.

The TxGNN model assigns its highest prediction score to **Autoimmune Oophoritis** (99.78%), however this is supported by **no clinical trials** and **no published literature**, and the model's own rationale flags this as likely non-specific knowledge graph co-occurrence rather than a genuine mechanistic link.

Across all 9 predicted indications in this Evidence Pack, **Pancreatic Agenesis** (Rank 7) emerges as the most biologically grounded candidate — the only indication with associated literature and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in South Africa; globally indicated for Diabetes Mellitus (Type 1 and Type 2) |
| Top TxGNN Predicted Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on established pharmacology, Insulin Lispro is a modified human insulin analogue in which the amino acids at positions B28 (lysine) and B29 (proline) are reversed, producing a molecule that dissociates more rapidly from hexamers to monomers after subcutaneous injection. It exerts its effect by binding to insulin receptors on skeletal muscle and adipose tissue, promoting glucose uptake, suppressing hepatic glucose output, and facilitating anabolic metabolism. Its entire pharmacological profile centres on glucose homeostasis.

The proposed link to **Autoimmune Oophoritis** is mechanistically unsupported. This condition is an organ-specific autoimmune disorder driven by autoreactive T-cells and autoantibodies targeting steroidogenic cells of the ovary. Insulin Lispro has no established immunomodulatory activity relevant to ovarian tissue, and no known signalling pathway connects insulin receptor binding to oophoritis pathogenesis.

The internal TxGNN rationale for this prediction explicitly acknowledges that the high score likely arises from non-specific co-occurrence of "autoimmune" nodes in the knowledge graph, a recognised limitation of graph neural network models where topologically adjacent nodes can receive elevated scores without genuine biological specificity. Clinicians should interpret this prediction with considerable caution — the model has detected a structural pattern in the knowledge graph, not a validated therapeutic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Insulin Lispro in Autoimmune Oophoritis.

---

## Literature Evidence

Currently no related literature available for Insulin Lispro in Autoimmune Oophoritis.

---

## All Predicted Indications — Summary Overview

Because the top-ranked TxGNN prediction carries a Hold recommendation and L5 evidence, the full landscape of 9 predicted indications is presented below to support informed prioritisation:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Notes |
|------|---------|-------------|---------------|----------|-----------|
| 1 | Autoimmune Oophoritis | 99.78% | L5 | Hold | Non-specific KG co-occurrence; no mechanistic support |
| 2 | Thiamine-Responsive Dysfunction Syndrome (TRMA) | 99.37% | L4 | Research Question | Manages DM phenotype in TRMA; indirect mechanism |
| 3 | Classic Stiff Person Syndrome | 99.36% | L4 | Research Question | Shares anti-GAD65 mechanism with T1DM; ~30% co-morbidity |
| 4 | Focal Stiff Limb Syndrome | 99.36% | L5 | Hold | Weaker anti-GAD65 association than classic SPS |
| 5 | Opsismodysplasia | 99.34% | L5 | Research Question | Highly speculative SHIP2/PI3K-Akt pathway connection |
| 6 | **Drug-Induced Localized Lipodystrophy** | 99.09% | L4 | ⚠️ **Hold — Known ADR** | **Insulin injection is the cause, not the treatment** |
| 7 | **Pancreatic Agenesis** | 99.09% | L4 | **Proceed with Guardrails** | Strongest mechanistic rationale; 2 literature references |
| 8 | Centrifugal Lipodystrophy | 99.04% | L5 | Hold | No known mechanistic link to insulin pharmacology |
| 9 | Pressure-Induced Localized Lipoatrophy | 99.03% | L5 | Hold | Insulin injection may itself be a contributing cause |

> ⚠️ **Critical Flag — Rank 6 (Drug-Induced Localized Lipodystrophy):** TxGNN has identified a causal relationship, not a therapeutic opportunity. Repeated subcutaneous injection of Insulin Lispro at the same site is a **known adverse drug reaction** causing localised lipohypertrophy or lipoatrophy. This should be documented as an ADR signal, not pursued as a repurposing candidate.

---

## Focus: Pancreatic Agenesis (Highest-Priority Candidate)

**Pancreatic Agenesis** represents the most clinically coherent repurposing signal in this Evidence Pack. Congenital absence of the pancreas results in complete absence of endogenous insulin secretion from birth, producing a phenotype of absolute insulin-dependent diabetes mellitus — physiologically indistinguishable from severe Type 1 DM in terms of insulin requirements. External insulin replacement is not merely reasonable; it is a biological necessity for survival.

### Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11727406](https://pubmed.ncbi.nlm.nih.gov/11727406/) | 2001 | Review | *Endocrinol Metab Clin North Am* | Comprehensive review of insulin therapy in Type 2 diabetes; discusses intensive glucose control, UKPDS outcomes, and the role of insulin analogues including rapid-acting formulations in managing post-prandial hyperglycaemia |
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | *J Am Pharm Assoc* | Reviews practical initiation of insulin therapy in Type 2 diabetes; principles directly applicable to absolute insulin-deficient states such as pancreatic agenesis |

> **Note on literature relevance:** Both publications address insulin therapy in Type 2 diabetes and are not specific to pancreatic agenesis. Their relevance is indirect — they document the clinical framework for insulin analogue use in absolute insulin deficiency states. Pancreatic agenesis-specific case series were not identified in the current search.

---

## South Africa Market Information

Insulin Lispro is **not currently registered with SAHPRA** and carries no recorded marketing authorisations in South Africa. There are no approved indications, dosage forms, registration numbers, or Essential Medicines List (EML) entries available from local regulatory data.

> **Note for clinicians:** Insulin lispro products (e.g., Humalog®, Admelog®) are registered in numerous jurisdictions including the USA (FDA), European Union (EMA), and many others. Prescribers in South Africa who require this product should consult SAHPRA regarding current registration status and Section 21 authorisation requirements for unregistered medicines. Alternative rapid-acting insulin analogues that may hold SAHPRA registration (e.g., insulin aspart, insulin glulisine) should be investigated as locally available substitutes.

---

## Safety Considerations

SAHPRA-specific safety data (warnings, contraindications) is not available in this Evidence Pack as the drug is not registered in South Africa (Data Gap DG001, classified as Blocking severity).

Please refer to the SAHPRA-approved Professional Information (PI) for safety information once registration is sought, or consult the manufacturer's current global prescribing information. Report adverse drug reactions to SAHPRA.

For reference, internationally recognised safety considerations include:

- **Hypoglycaemia** — the most common and potentially life-threatening adverse effect; risk is increased with dose errors, missed meals, or increased physical activity
- **Injection site reactions** — including lipohypertrophy and lipoatrophy with repeated injection at the same site (see ADR flag above)
- **Hypokalaemia** — insulin drives potassium intracellularly; monitor electrolytes particularly in hospitalised patients
- **Contraindicated** during active hypoglycaemic episodes

---

## Conclusion and Next Steps

**Decision: Hold** *(for Autoimmune Oophoritis — TxGNN Rank 1)*

**Rationale:**
The highest-ranked TxGNN prediction (Autoimmune Oophoritis) is assessed as a knowledge graph artefact with no clinical, mechanistic, or experimental support. The model's own analytical notes explicitly flag the prediction as non-specific co-occurrence. There is no biological rationale to advance this indication, and doing so would not represent sound use of research or clinical resources.

---

**Prioritised Decision Summary Across All Predictions:**

| Indication | Decision | Suggested Next Step |
|-----------|---------|-------------------|
| Pancreatic Agenesis | **Proceed with Guardrails** | Case series search; paediatric endocrinology consultation; Section 21 pathway |
| Classic Stiff Person Syndrome | Research Question | Targeted literature review of insulin use in anti-GAD65–positive SPS |
| Thiamine-Responsive Dysfunction Syndrome (TRMA) | Research Question | Review TRMA case reports for insulin management; consult metabolic medicine |
| Drug-Induced Localized Lipodystrophy | **Flag as ADR — Do Not Pursue** | Document as known adverse effect in pharmacovigilance system |
| Autoimmune Oophoritis | Hold | No action recommended |
| Remaining Hold indications | Hold | No action recommended |

---

**To proceed with Pancreatic Agenesis (highest-priority candidate), the following is needed:**

- Retrieve complete MOA data from DrugBank API to strengthen mechanistic justification (Data Gap DG002)
- Obtain SAHPRA-specific safety and contraindication data, or initiate Section 21 application for unregistered use (Data Gap DG001 — Blocking)
- Conduct targeted PubMed search specifically for pancreatic agenesis case series documenting insulin analogue use in neonatal/paediatric populations
- Determine whether this indication falls within the scope of existing neonatal diabetes management guidelines, as pancreatic agenesis may already be managed under standard insulin replacement protocols without requiring formal repurposing
- Consult paediatric endocrinology and metabolic disease specialists given the typically neonatal/infant presentation of this condition

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This report should be reviewed by a qualified healthcare professional before any clinical decision is made.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

