---
layout: default
title: Threonine
parent: 僅模型預測 (L5)
nav_order: 435
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the evidence pack directly (no skill applies — this is a self-contained report-writing task per the detailed format instructions already provided). Here is the report:

---

# Threonine: From Essential Amino Acid (No Approved Indication) to Gastroparesis

## One-Sentence Summary

> Threonine is an essential amino acid with no approved therapeutic indication and no SAHPRA market registration in South Africa — it is a nutritional component, not a registered medicine.
> The TxGNN model predicts a possible association with **Gastroparesis**, but on verification this is supported by **0 clinical trials** and only **1 preclinical animal study**, which itself does not actually investigate threonine and appears to be a keyword-matching artifact.
> **This prediction should be treated as unsupported until independently re-verified.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — no approved therapeutic indication is registered for THREONINE; it is classified as an essential amino acid / nutritional component |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for THREONINE is not available (original_moa: Data Gap), and no original approved indication is on record — THREONINE is not registered as a therapeutic drug in South Africa or elsewhere in this dataset; it functions as a nutritional/essential amino acid component.

On closer examination, the single literature record returned for this prediction (PMID 28627597) does **not** actually study threonine supplementation or pharmacology. It examines PI3K‑AKT‑mTOR and AMPK‑mTOR signaling in a diabetic rat model of gastroparesis — AKT and mTOR are *serine/threonine kinases*, a class named for the amino acid residues they phosphorylate. The most probable explanation is that the TxGNN knowledge graph and/or the literature-matching pipeline linked this paper to the drug entity "THREONINE" purely through this lexical overlap ("threonine kinase"), not because the paper studies the amino acid as a therapeutic agent.

Consequently, there is no credible mechanistic rationale connecting THREONINE to gastroparesis treatment. The high TxGNN score (99.32%, rank 3608) reflects graph-topological similarity within the model only, and is not corroborated by any genuine biological or clinical evidence in this evidence pack. This prediction should be flagged as a likely **false positive driven by keyword collision** rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Animal/Preclinical (Basic Research) | Molecular Medicine Reports | Examined gastric smooth muscle apoptosis and PI3K‑AKT‑mTOR / AMPK‑mTOR signaling in a diabetic rat model of gastroparesis. **Does not study threonine as an agent** — likely matched to this drug candidate only via the "serine/threonine kinase" term (AKT/mTOR), not genuine pharmacological evidence. |

**Caution:** This is the only literature record supporting the prediction, and it has been assessed as not directly relevant to THREONINE. Treat this evidence base as effectively empty pending independent literature re-screening.

---

## South Africa Market Information

THREONINE currently has **no SAHPRA registrations** (0 licenses on record) and is **not marketed** in South Africa as a registered pharmaceutical product. No approved Professional Information (PI) exists for this substance in a therapeutic context.

---

## Safety Considerations

Because THREONINE is not registered as a pharmaceutical product in South Africa, no SAHPRA-approved Professional Information (PI) exists for it, and no warnings, contraindications, or drug-interaction data are available in this evidence pack (flagged as a **Blocking** data gap — DG001: TFDA/SAHPRA label warnings and contraindications). Any clinical use for a novel indication would need to proceed without a regulatory safety baseline until this gap is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 — this is a model-generated prediction with no supporting clinical trials and only one literature record, which on review does not actually pertain to threonine's pharmacology.
- The drug has no approved indication, no mechanism-of-action data, no SAHPRA registration, and no safety/label data available (Blocking data gap DG001), so it cannot currently pass even an initial safety screening (S0/S1).

**To proceed, the following is needed:**
- Independent literature re-screening for genuine threonine–gastroparesis studies (the current single citation appears to be a false match)
- Resolution of Blocking data gap DG001 (SAHPRA/TFDA label warnings and contraindications) before any safety assessment can begin
- Resolution of High-priority data gap DG002 (verified mechanism of action) to establish a credible biological rationale
- Confirmation of whether THREONINE would be regulated as a drug or remain classified as a nutritional/dietary substance if this indication were pursued
- If re-screening surfaces no genuine supporting evidence, this candidate should be deprioritized rather than advanced further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

