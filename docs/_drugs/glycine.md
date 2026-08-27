---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Glycine
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

# Glycine: From No Registered SAHPRA Indication to Predicted Nasal Cavity Disease Treatment

## One-Sentence Summary

> Glycine currently has **no SAHPRA-registered product and no documented original indication or mechanism of action** in this evidence pack. The TxGNN model predicts a possible role in **Nasal Cavity Disease** (score 99.85%), but the only supporting clinical trial and literature identified are unrelated to glycine's pharmacology — this is a **low-confidence, model-only signal**, not a clinically supported repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA licence and no original indication data on file |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glycine is not available in this evidence pack, and no original indication is on record — so the usual "original MOA → new indication" reasoning chain cannot be built here.

Reviewing the actual evidence retrieved for this prediction, the link appears weak. The one associated clinical trial (NCT01806675) studies a PET imaging tracer (¹⁸F‑FPPRGD2) for integrin expression in cancer patients and does not involve glycine as a therapeutic agent — it only shares an anatomical search term with "nasal cavity." The two literature hits are similarly tangential: a 1995 veterinary histochemistry study of bovine nasal mucosa, and a 2018 study of oligoarginine-polymer mucosal adjuvants — neither investigates glycine's pharmacological effect on nasal disease.

The evidence pack's own analysis concludes there is **no clear mechanistic rationale** connecting glycine (an inhibitory neurotransmitter / NMDA receptor co-agonist) to nasal cavity disease. This pattern is consistent with a TxGNN embedding-space artefact rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Completed | 25 | Evaluated ¹⁸F-FPPRGD2 PET/CT/MRI imaging of αvβ3 integrin expression in glioblastoma, gynaecological cancer, and renal cell carcinoma patients on antiangiogenic therapy. **Does not involve glycine as a treatment**; trial relevance to nasal cavity disease is coincidental (imaging biomarker study only). |

No SANCTR or PACTR-registered trials were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Veterinary histochemistry | Veterinary Pathology | Lectin histochemistry of bovine nasal mucosa in herpesvirus infection and *Pasteurella haemolytica* adhesion; **no glycine intervention studied**. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preclinical (polymer adjuvant) | Chemical & Pharmaceutical Bulletin | Oligoarginine-conjugated polymer as a nasal mucosal vaccine adjuvant; **glycine not the study agent**. |

Neither publication provides direct pharmacological evidence for glycine in nasal cavity disease.

---

## South Africa Market Information

Currently no SAHPRA registrations are on file for glycine as a marketed pharmaceutical product (market status: **Not marketed**, 0 licences recorded in this evidence pack).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: key warnings, contraindications, and drug interaction data are currently unavailable for glycine in this evidence pack — this is flagged as a blocking data gap for any safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical trial and literature identified for the Nasal Cavity Disease prediction are pharmacologically unrelated to glycine, and the model itself provides no plausible mechanistic link. Combined with L5 evidence (prediction-only) and the absence of any SAHPRA registration or PI safety data, this candidate does not currently support further evaluation.

**To proceed, the following is needed:**
- SAHPRA/TFDA Professional Information (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- A clinical trial or literature search specifically targeting glycine (not tracer/adjuvant studies that merely share search terms) before this indication is reconsidered
- If further evaluation is desired, the evidence pack's rank-5 candidate (**dyspepsia**, L4 evidence, "Research Question" stage) has a more coherent mechanistic rationale (glycine as NMDA receptor co-agonist affecting gastric accommodation) and may be a more productive direction than nasal cavity disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

