---
layout: default
title: Dicyclomine
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 2
---

# Dicyclomine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Using the report structure directly (no specialized skill needed — this is a self-contained templated write-up task from the Evidence Pack already provided).

A note before the report: the Evidence Pack itself flags **rank 1 (cauda equina syndrome)** as a likely spurious/false-positive association (the `repurposing_rationale.mechanistic_link` explicitly says this). I'm following the prompt's instruction to build the report around `predicted_indications[0]`, but I'm reporting that caveat transparently rather than presenting it as a strong signal — that's the honest reading of the data, and inventing confidence that isn't there would misrepresent the evidence pack.

---

# Dicyclomine: From Irritable Bowel Syndrome (Antispasmodic Use) to Cauda Equina Syndrome

## One-Sentence Summary

> Dicyclomine is an antimuscarinic (anticholinergic) antispasmodic drug, internationally used for irritable bowel syndrome and functional bowel/spastic colon disorders — it is **not currently registered or marketed in South Africa**.
> The TxGNN model's top-ranked prediction links it to **Cauda Equina Syndrome**, but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the link as a probable indirect artifact rather than a genuine treatment mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from SAHPRA data (drug is unregistered in South Africa). Internationally, Dicyclomine is used as an antispasmodic for irritable bowel syndrome / functional bowel disorders. |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (flagged as a High-severity data gap, DG002). Based on known pharmacological information, Dicyclomine is a non-selective antimuscarinic (anticholinergic) antispasmodic. Its established mechanism is blockade of muscarinic (M1/M3) receptors on gastrointestinal smooth muscle, which relieves spasm in conditions such as irritable bowel syndrome — this is the basis for its original indication.

Cauda equina syndrome, by contrast, is a **surgical emergency** caused by mechanical compression of the lumbosacral nerve roots, typically from a herniated disc, tumour, or trauma. The standard of care is urgent surgical decompression; there is no established pharmacological treatment for the underlying nerve compression. The Evidence Pack's own mechanistic rationale is explicit about this mismatch: it states that the only plausible link is *indirect* — cauda equina syndrome can cause **neurogenic bladder** as a secondary complication (from sacral nerve root damage), and Dicyclomine's antimuscarinic effect could theoretically ease *secondary* bladder symptoms. It does **not** treat the nerve compression itself, which is the actual disease process.

In other words, this prediction most likely reflects the model learning a "cauda equina syndrome → neurogenic bladder" association path rather than a direct drug–disease treatment relationship. Consistent with this, the Evidence Pack's second-ranked prediction, **neurogenic bladder** (obsolete disease term, score 99.50%), has a mechanistically more coherent rationale — antimuscarinic blockade of detrusor M2/M3 receptors is the same mechanism used by approved neurogenic bladder / overactive bladder drugs (e.g. oxybutynin, tolterodine). That prediction is scored by the pack itself as a "Research Question" rather than a candidate for clinical evaluation, again due to zero direct trial or literature support and an outdated disease ontology label requiring disambiguation.

**No clinical trials or publications exist for either predicted indication**, so this section should be read as a hypothesis-generation signal only, not as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Dicyclomine (DB00804) has **no SAHPRA registrations** and is **not marketed** in South Africa (0 licenses on file). No product, dosage form, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/SAHPRA label warnings and contraindications are a Blocking data gap (DG001) in this Evidence Pack — no safety review can be completed until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only — zero clinical trials, zero publications for the top-ranked indication).
- The Evidence Pack's own mechanistic analysis suggests the top prediction (cauda equina syndrome) is likely an indirect/false-positive association rather than a genuine drug–disease treatment relationship, since the drug has no mechanism addressing the underlying nerve compression.
- Dicyclomine is not registered or marketed in South Africa, so there is no existing regulatory or safety base to build on locally.

**To proceed, the following is needed:**
- SAHPRA/TFDA-approved Professional Information (label warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action data from DrugBank or primary literature — currently a High-severity data gap (DG002)
- Disambiguation of the "obsolete neurogenic bladder (disease)" ontology term to its current equivalent, to properly evaluate the more mechanistically plausible rank-2 prediction
- Preclinical or mechanistic studies specifically testing antimuscarinic therapy for neurogenic bladder secondary to cauda equina syndrome, before this moves beyond a research hypothesis
- Regulatory pathway assessment, since the drug currently has no South African market presence at all
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

