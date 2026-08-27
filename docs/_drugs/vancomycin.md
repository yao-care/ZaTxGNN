---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 457
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic classically used against serious Gram-positive bacterial infections (its formal original-indication text is not present in this evidence pack). The TxGNN model's top-ranked prediction is **Diffuse Scleroderma**, with a very high raw score but **no clinical trials and only a single case report** — and that case report describes a vancomycin-induced drug reaction, not therapeutic efficacy. This is a low-confidence, likely spurious signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (drug.original_indications is empty; regulatory license data is also empty) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for vancomycin is flagged as a data gap in this pack (DG002). Based on information embedded elsewhere in the evidence pack's own analysis (see the rationale for the streptococcal pneumonia candidate), vancomycin's known mechanism is inhibition of Gram-positive bacterial cell wall synthesis via binding to the D-Ala-D-Ala terminus of peptidoglycan precursors — a purely antibacterial mechanism.

Diffuse scleroderma is an autoimmune fibrotic connective-tissue disease with no established pathophysiological link to bacterial cell-wall synthesis inhibition. The evidence pack's own repurposing rationale is explicit on this point: it states there is "no plausible mechanism" connecting the two, and that the single supporting publication is a case report of a vancomycin-induced drug eruption with eosinophilia — i.e., an adverse-reaction description, not efficacy evidence. The rationale concludes this is most likely a **TxGNN false positive**.

In short, the very high TxGNN score for this candidate is not corroborated by mechanistic or clinical evidence, and the underlying literature actually describes a harm signal rather than a benefit signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Describes a patient with diffuse exfoliative rash, sepsis, and eosinophilia after antibiotic exposure (including vancomycin-associated regimens) — an adverse drug reaction case, not evidence of efficacy against scleroderma |

## South Africa Market Information

Vancomycin has no registered products in this evidence pack (market status: Not Marketed; 0 SAHPRA registrations recorded).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no mechanistic rationale, no clinical trial support, and the only literature citation describes a drug-induced adverse reaction rather than therapeutic benefit. The evidence pack's own analysis independently flags this as a probable false positive.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for vancomycin (DG002)
- SAHPRA-equivalent/TFDA professional information covering warnings and contraindications (DG001)
- Any preclinical or mechanistic rationale specifically linking glycopeptide antibiotics to autoimmune fibrotic disease, before this candidate warrants further investment

---

**Note on other candidates in this evidence pack:** Of the 10 TxGNN predictions supplied, rank 9 (**streptococcal pneumonia**) is notably stronger — evidence level L3, decision stage S2, recommendation "Proceed with Guardrails" — because vancomycin's established Gram-positive cell-wall-synthesis-inhibition mechanism directly applies to *Streptococcus pneumoniae*, and it already has real-world use as an alternative for penicillin/cephalosporin-resistant pneumococcal infections. If a single indication must be prioritized for further work from this pack, streptococcal pneumonia — not diffuse scleroderma — is the more defensible candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

