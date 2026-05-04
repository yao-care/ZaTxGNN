---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic topical vitamin D₃ analogue used globally for the treatment of psoriasis vulgaris, though it currently holds no SAHPRA registration in South Africa.
The TxGNN model predicts it may be effective for **Seborrheic Keratosis**, with **0 registered clinical trials** and **6 published studies** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriasis vulgaris (globally approved; no SAHPRA registration in South Africa) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, calcipotriol is a synthetic vitamin D₃ analogue that binds to the **vitamin D receptor (VDR)** on keratinocytes, promoting their **terminal differentiation** and **apoptosis** while suppressing aberrant proliferation. These properties underpin its well-established efficacy in psoriasis — a condition defined by hyperproliferating, poorly differentiated keratinocytes.

Seborrheic keratosis is a benign neoplasm arising from the same target cell type: the epidermal keratinocyte. The biological case for calcipotriol is therefore directly transferable — the drug acts on the very cell population responsible for lesion formation. Crucially, the apoptosis mechanism has been explicitly proposed in published clinical literature (PMID 16043912), moving this beyond pure mechanistic extrapolation. Since seborrheic keratosis is a surface lesion, topical application also ensures targeted drug delivery with negligible systemic exposure, mitigating the hypercalcaemia risk associated with systemic vitamin D analogues.

Among the 10 TxGNN-predicted indications reviewed, seborrheic keratosis stands out as the most evidence-supported candidate: it combines mechanistic plausibility, an anatomically appropriate route of administration, a consistent track record across multiple small studies spanning two decades, and reports of durable long-term remission following treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Prospective case series | Australasian Journal of Dermatology | 12 patients with solitary facial seborrheic keratosis treated with 0.005% calcipotriol ointment for 3–8 months; complete lesion regression achieved in all cases; remission sustained 6–10 years at follow-up |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Small clinical study with mechanistic hypothesis | Journal of Dermatology | Topical vitamin D₃ ointments (including calcipotriol) applied to senile warts (seborrheic keratosis) in 116 cases; 30.2% complete response at 3–12 months; apoptosis explicitly proposed as the therapeutic mechanism |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Clinical case series | Clinical Calcium | Japanese case series reporting efficacy of topical vitamin D₃ ointments (tacalcitol, calcipotriol, maxacalcitol) for senile warts (seborrheic keratosis); once or twice daily application; consistent lesion reduction observed |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative study | International Journal of Dermatology | Head-to-head comparison of topical calcipotriol, tazarotene, and imiquimod versus standard cryosurgery for seborrheic keratoses in patients seeking non-procedural therapy |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case report | Journal of Dermatology | Marked clinical response of keratosis lichenoides chronica — a related refractory keratotic dermatosis — to calcipotriol ointment, lending indirect mechanistic support |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Clinical vignette / brief review | JAAPA | Clinical vignette describing seborrheic keratosis presentation and management context |

---

## South Africa Market Information

Calcipotriol currently holds **no SAHPRA registrations** and is **not marketed in South Africa**. Healthcare professionals wishing to use this agent would need to explore the Section 21 (unregistered medicine) authorisation pathway through SAHPRA.

Calcipotriol is, however, widely registered and marketed in other jurisdictions (including European Union, United Kingdom, United States, Japan, and Australia) under brand names such as **Daivonex** and **Dovonex**, available as 0.005% cream, ointment, and scalp solution formulations for psoriasis.

---

## Safety Considerations

Please refer to the manufacturer's Professional Information (PI) document for complete safety information, as no SAHPRA-approved PI is available for this unregistered product. Practitioners should note the well-documented class-level risk of **local skin irritation** and **hypercalcaemia with excessive use** that applies to topical vitamin D analogues. Report any adverse drug reactions to SAHPRA via the MedSafety reporting system.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple small published studies spanning over two decades consistently demonstrate that topical calcipotriol achieves complete regression of seborrheic keratosis lesions, with one prospective series reporting remission of up to 10 years — an unusually durable outcome for a benign but cosmetically troublesome condition. The mechanism is biologically coherent and directly supported by published evidence, qualifying this for L3 evidence with a guarded recommendation to advance.

**To proceed, the following is needed:**
- A formal randomised controlled trial (ideally vs. cryosurgery as the standard of care) to confirm efficacy, optimal treatment duration, and relapse rates
- **SAHPRA Section 21 authorisation** for use in South Africa, as the product is currently unregistered
- Retrieval and review of the manufacturer's full Professional Information document for contraindications, warnings, and drug interactions
- Formal VDR expression profiling in seborrheic keratosis tissue to confirm the mechanistic target is present
- Clarification of optimal formulation (cream vs. ointment) and frequency of application for the facial subtype specifically

---

> ⚠️ **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be interpreted in conjunction with current SAHPRA guidelines and the prescriber's clinical judgement.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

