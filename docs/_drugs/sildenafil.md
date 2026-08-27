---
layout: default
title: Sildenafil
parent: 僅模型預測 (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From Erectile Dysfunction to Genetic Alopecia

## One-Sentence Summary

Sildenafil is a PDE5 inhibitor best known for erectile dysfunction and pulmonary arterial hypertension. Among 10 candidate indications the TxGNN model surfaced for this drug, **Genetic Alopecia** is the only one backed by actual clinical and mechanistic evidence — **2 clinical trials** and **1 mechanistic publication** — while the other 9 candidates (highest TxGNN scores but zero supporting evidence, several mechanistically implausible) remain on Hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction / pulmonary arterial hypertension (general drug identity; not captured in this evidence pack — see Market Status below) |
| Predicted New Indication | Genetic Alopecia |
| TxGNN Prediction Score | 75.03% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed (unregistered) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

*Note: This candidate was selected from the 10 TxGNN-ranked predictions for sildenafil as the one with actual clinical/literature support. The single highest-scoring candidate by raw model score (Ambras type hypertrichosis, 98.4%) has no supporting evidence and a mechanistically questionable rationale — see "Other Predicted Indications" below.*

---

## Why is This Prediction Reasonable?

Sildenafil inhibits phosphodiesterase type 5 (PDE5), raising intracellular cyclic guanosine monophosphate (cGMP) levels. This causes vascular smooth muscle relaxation and increased local blood flow — the same mechanism responsible for its efficacy in erectile dysfunction and pulmonary hypertension.

Applied to hair follicles, increased local microvascular blood flow is a plausible route to stimulating follicular activity. This is directly analogous to minoxidil — a currently approved treatment for androgenetic alopecia — which works via a different vasodilatory pathway (K⁺-channel opening) but shares the same underlying strategy of increasing follicular blood supply. A published preclinical study (PMID 30292404) has directly investigated sildenafil's effect on human hair follicles, supporting this mechanistic link.

Because both trials identified use topical (not systemic) administration, systemic side effects such as hypotension are expected to be minimal, which further supports feasibility for this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05369481](https://clinicaltrials.gov/study/NCT05369481) | Phase NA | Unknown | 50 | Comparative study of topical sildenafil 2% vs. topical minoxidil 5% for male androgenetic alopecia; status/results not yet updated. |
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | Completed | 28 | Randomized study of sildenafil-loaded lipid nanocarrier for alopecia areata; completed early-phase feasibility/safety trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018 | Mechanistic/Preclinical | Biochemical and Biophysical Research Communications | First report demonstrating sildenafil's effect on human hair follicles via PDE5/cGMP-mediated vasodilation. |

---

## Other Predicted Indications (Lower Confidence — Hold)

The remaining 9 TxGNN candidates for sildenafil scored higher on raw model confidence but have **no clinical trial or literature support**, and several have mechanistically implausible or direction-reversed rationales:

| Rank | Disease | TxGNN Score | Evidence Level | Note |
|------|---------|-------------|-----------------|------|
| 1 | Ambras type hypertrichosis universalis congenita | 98.41% | L5 | No evidence; congenital genetic disorder, not vascular in origin. |
| 2 | Malformation syndrome (odontal/periodontal) | 98.23% | L5 | No known mechanistic link. |
| 3 | Dandy-Walker malformation syndrome | 98.03% | L5 | Developmental brain malformation, unrelated to PDE5/cGMP pathway. |
| 4 | Isolated genetic hair shaft abnormality | 97.86% | L5 | Structural genetic defect, not blood-flow responsive. |
| 5 | Hypertrichosis (disease) | 97.83% | L4 | Only literature found concerns glibenclamide (Cantú syndrome), not sildenafil. |
| 6 | Homozygous familial hypercholesterolemia | 93.77% | L5 | No known mechanistic link. |
| 7 | Hypoalphalipoproteinemia | 90.11% | L5 | No known mechanistic link. |
| 8 | Familial isolated trichomegaly | 79.78% | L5 | No evidence; direction of effect unclear. |
| 10 | Obsolete patella aplasia/coxa vara/tarsal synostosis | 70.00% | L5 | Obsolete disease classification; recommend exclusion. |

These should remain on **Hold** and are not pursued further in this report.

---

## South Africa Market Information

Sildenafil currently has **no SAHPRA registrations** on record in this evidence pack (market status: not marketed). No dosage forms or registered product data are available for South Africa at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Structured safety data — key warnings, contraindications, drug-drug interactions — was not available in this evidence pack for this candidate. This is flagged as a Blocking data gap (DG001): TFDA/SAHPRA label warnings and contraindications must be obtained before any safety pre-assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two small early-stage clinical trials plus a direct mechanistic study on human hair follicles support a plausible, mechanism-consistent role for topical sildenafil in genetic alopecia, paralleling the approved use of minoxidil. However, both trials are small (n=28, n=50), one has unknown/unreported status, and neither is a confirmatory Phase 2/3 RCT — evidence remains early-stage.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI profile (currently a Blocking data gap)
- Formal mechanism-of-action documentation for the regulatory record
- Completed/reported results from NCT05369481, and a larger confirmatory RCT of topical sildenafil vs. minoxidil in genetic alopecia
- Topical-formulation-specific safety and local tolerability data
- Confirmation of SAHPRA registration pathway, since sildenafil is currently unregistered in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

