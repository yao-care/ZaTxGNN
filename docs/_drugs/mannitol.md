---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Mannitol
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

Using the drug-repurposing evaluation report template (v5) to produce this report from the supplied Evidence Pack.

---

# Mannitol: From Osmotic Diuretic Therapy to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Mannitol's registered original indication is not documented in the available regulatory data (a flagged data gap); it is generically known as an osmotic diuretic.
> The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
> but this is currently supported by **0 clinical trials** and only **1 loosely related publication**, which does not itself study mannitol as a treatment for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the evidence pack (registration/indication data gap). Mannitol is generically known as an osmotic diuretic (e.g., cerebral oedema, raised intracranial/intraocular pressure, forced diuresis) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for mannitol is currently unavailable (data gap DG002). Based on known general pharmacology, mannitol is a sugar-alcohol osmotic agent that expands plasma volume and promotes water/solute diuresis; it is not part of a fixed combination product in this evidence pack, and its efficacy in a specific original indication cannot be confirmed here because no `original_indications` or approved indication text was returned.

NSIAD is a rare genetic disorder (typically caused by activating mutations in the vasopressin V2 receptor) that produces hyponatremia through inappropriate free-water retention, independent of ADH levels. There is no established mechanistic rationale linking osmotic diuresis with mannitol to correction of V2-receptor-driven water retention, and standard management of hyponatremic disorders instead relies on fluid restriction, urea, or vaptans. The single supporting publication (PMID 26706473) is a general review on pitfalls in evaluating hyponatremia and does not investigate mannitol as a therapeutic agent for NSIAD — it appears to have been retrieved on the basis of shared terminology ("hyponatremia") rather than a demonstrated drug–disease relationship.

Given this, the TxGNN score for this candidate should be interpreted as a knowledge-graph association rather than mechanistically or clinically validated evidence. Reviewers should also note that other high-scoring predictions in this same evidence pack for mannitol (e.g., malignant hyperthermia susceptibility, acute pulmonary heart disease) show a recurring pattern of likely knowledge-graph confounding — such as co-formulation overlap with dantrolene, or disease-ontology overlap between "acute pulmonary heart disease" and ARDS — and in at least one case (nephrogenic diabetes insipidus) the literature suggests mannitol may *worsen* rather than treat the condition. This overall pattern warrants added scrutiny for any mannitol repurposing signal derived from this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in diagnosing and managing hyponatremia; discusses risks of both under- and over-treatment, but does not evaluate mannitol as a treatment for NSIAD specifically |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A blocking data gap (DG001) has been identified — TFDA/SAHPRA-equivalent package insert warnings and contraindications have not yet been retrieved, and this must be resolved before any safety evaluation (Stage S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (NSIAD) has no clinical trial support and only one indirectly related publication that does not study mannitol itself; combined with the absence of mechanism-of-action data and the drug's "Not marketed" status in South Africa (0 SAHPRA registrations), the evidence level is L5 (model prediction only).
- Similar high-scoring predictions elsewhere in this evidence pack for mannitol appear to reflect knowledge-graph confounding (co-formulation and disease-ontology overlaps) rather than genuine pharmacological signals, reinforcing a cautious posture toward this candidate.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: retrieve TFDA/SAHPRA package insert warnings, contraindications, and drug interaction data
- Resolve data gap DG002: obtain confirmed mechanism of action data from DrugBank
- Obtain confirmed original indication/registration data for mannitol (currently absent from the evidence pack)
- Identify or commission dedicated pharmacological/mechanistic studies directly evaluating mannitol in NSIAD, rather than relying on general hyponatremia literature
- Re-review the TxGNN knowledge-graph edges for this candidate to rule out confounding from co-administered/co-formulated agents before any further advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

