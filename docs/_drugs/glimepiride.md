---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to stimulate pancreatic insulin secretion in type 2 diabetes mellitus. The TxGNN model's top prediction is **Classic Stiff Person Syndrome**, but this candidate has **no clinical trials** and **no supporting literature** — the score appears driven by a diabetes-comorbidity artefact in the knowledge graph rather than a genuine pharmacological link. Across nine candidates screened in this evidence pack, only one (pancreatic agenesis) shows a plausible — though still unconfirmed — mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (known drug class; not confirmed via SA dossier — glimepiride is unregistered in South Africa) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glimepiride is currently a data gap in this pack. Based on known pharmacology, glimepiride is a second-generation sulfonylurea that binds the SUR1 subunit of the pancreatic β-cell KATP channel, closing the channel and triggering insulin release — its efficacy in type 2 diabetes is well established.

Classic Stiff Person Syndrome (SPS) is an autoimmune neurological disorder driven by anti-GAD65 antibodies and GABAergic dysregulation. There is no known pharmacological overlap between insulin-secretagogue activity at KATP channels and GABAergic autoimmune neurotransmission. The most plausible explanation for the very high TxGNN score is an indirect knowledge-graph artefact: SPS frequently co-occurs with type 1 diabetes in the underlying data, and the model may be picking up this "diabetes comorbidity" node rather than a true treatment mechanism. The rank-2 candidate (focal stiff limb syndrome, a regional SPS variant) shows the identical pattern and score, reinforcing this interpretation.

Of the nine candidates evaluated in this batch, the only one with a biologically coherent rationale is **pancreatic agenesis** (rank 9, L4, decision stage S1, "Research Question"): certain forms of permanent neonatal diabetes involve KCNJ11/ABCC8 mutations directly affecting the same SUR1/Kir6.2 KATP channel that sulfonylureas target, and patients with these monogenic subtypes are known to respond better to sulfonylureas than to insulin. However, pancreatic agenesis itself is more commonly caused by GATA6/PTF1A developmental gene mutations — a different mechanism — and the single associated PubMed citation (PMID 12720536) is an unrelated case report on endosonographic pitfalls in insulinoma imaging, not evidence for glimepiride use in this condition. This candidate merits a subtype-classification check before any further evaluation; it is not yet actionable evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

No SAHPRA registrations were found for glimepiride in this evidence pack. Market status is recorded as **Not marketed**, with **0** registrations on file — glimepiride does not currently have a South African dossier to draw indication or dosage-form information from.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Classic Stiff Person Syndrome) has no clinical trial or literature support and lacks a credible mechanistic basis — it most likely reflects a knowledge-graph confounder (diabetes comorbidity) rather than a true drug effect. No candidate in this batch has reached a level of evidence (L1–L3) that would support active development.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent product information (labelled warnings and contraindications) — currently a **Blocking** data gap that prevents any safety (S1) evaluation
- Confirmed mechanism-of-action data via DrugBank API (currently a data gap)
- If pursuing the pancreatic agenesis lead: subtype-level genetic classification data (KATP-channel-related neonatal diabetes vs. GATA6/PTF1A-related pancreatic agenesis) and any primary literature on sulfonylurea use in monogenic neonatal diabetes
- Independent confirmation (e.g., pathway/network analysis) of whether the Stiff Person Syndrome and lipodystrophy signals are diabetes-comorbidity artefacts before allocating further review resources to them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

