---
layout: default
title: Magnesium Acetate
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 10
---

# Magnesium Acetate
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

# Magnesium Acetate: From Unregistered Electrolyte Product to Predicted Use in Hypertensive Disorder

## One-Sentence Summary

Magnesium acetate (DrugBank DB13996) has no SAHPRA registration in South Africa and no confirmed original indication or mechanism-of-action data on file. The TxGNN model predicts possible efficacy in **Hypertensive Disorder**, but of the **3 clinical trials** and **3 publications** currently retrieved, only one trial is even partially relevant to blood pressure and none directly studied magnesium acetate itself — so this remains an early, low-confidence research signal rather than an evidence-backed direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA/TFDA licenses on record |
| Predicted New Indication | Hypertensive disorder |
| TxGNN Prediction Score | 97.42% |
| Evidence Level | L3 (cohort/animal + mechanistic literature; trial evidence largely indirect) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for magnesium acetate is not available. Based on known information, magnesium acetate is the magnesium salt of acetic acid, generally used as an electrolyte/mineral source (e.g., in dialysis fluids and parenteral nutrition preparations); it is not registered for any indication in South Africa, so no formal original-indication text exists for comparison.

Mechanistically, magnesium ions act as natural calcium-channel antagonists that can relax vascular smooth muscle, and animal studies of the acetate moiety (a short-chain fatty acid) report antihypertensive effects mediated via gut microbiota metabolites. This gives a plausible — but only preclinical — biological rationale for exploring a blood-pressure-related indication.

However, the supporting evidence retrieved for this candidate is weak. Of the 3 clinical trials linked to "hypertensive disorder," only NCT07206524 (magnesium concentration in dialysate and hemodialysis-associated thromboinflammation) is mechanistically related to magnesium and blood pressure regulation — and its endpoint (preventing intradialytic hypotension) points in the opposite clinical direction from treating hypertension. The other two trials (an asthma/DASH-diet study and a steroid-induced glaucoma study) appear to be keyword mismatches on the word "acetate" rather than genuine evidence. The three literature citations are all animal/cohort studies of gut-derived acetate and hypertension programming, not studies of magnesium acetate as a drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05251402](https://clinicaltrials.gov/study/NCT05251402) | Phase 2/3 | Active, not recruiting | 323 | DASH diet trial in uncontrolled asthma; hypertension link is indirect (DASH = "Dietary Approaches to Stop Hypertension"), not a magnesium acetate study. Graded C relevance. |
| [NCT07206524](https://clinicaltrials.gov/study/NCT07206524) | N/A | Recruiting | 15 | Pilot study of magnesium concentration in citrate-enriched dialysate and hemodialysis-associated thromboinflammation; relevant to magnesium/hemodynamics but targets prevention of dialysis-related hypotension, not hypertension treatment. Graded B relevance. |
| [NCT00570479](https://clinicaltrials.gov/study/NCT00570479) | Phase 1 | Completed | 12 | Anecortave acetate for steroid-induced glaucoma; unrelated drug and indication, likely an "acetate" string match. Graded C relevance. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35887270](https://pubmed.ncbi.nlm.nih.gov/35887270/) | 2022 | Animal study | International Journal of Molecular Sciences | Maternal acetate supplementation reversed blood-pressure increases in offspring exposed to minocycline in utero; supports an antihypertensive effect of acetate in a rodent model. |
| [33087738](https://pubmed.ncbi.nlm.nih.gov/33087738/) | 2020 | Cohort/animal model | Scientific Reports | Dietary fibre and its metabolite acetate previously shown to protect against hypertension and heart disease in certain models; gut microbiota modulation did not override genetic predisposition to heart failure. |
| [31295767](https://pubmed.ncbi.nlm.nih.gov/31295767/) | 2019 | Review/mechanistic | Molecular Nutrition & Food Research | Reviews short-chain fatty acid (including acetate) supplementation to prevent maternal high-fructose-diet-induced hypertension programming in offspring. |

---

## South Africa Market Information

Magnesium acetate currently has **no SAHPRA registrations** and is **not marketed** in South Africa. No product listings, dosage forms, or approved indication text are available for review.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note:** Regulatory-labeled warnings, contraindications, and drug interaction data for magnesium acetate could not be sourced during this evaluation, which blocks any formal safety pre-assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The drug is unregistered and unmarketed in South Africa, its mechanism of action is unknown, and safety/PI data needed for even a preliminary risk assessment could not be sourced.
- The evidence base for the top predicted indication (Hypertensive Disorder) is thin and largely indirect — no trial directly tests magnesium acetate in hypertension, and supporting literature is limited to animal/cohort studies of the acetate moiety in general, not the drug itself.

**To proceed, the following is needed:**
- TFDA/SAHPRA-sourced Professional Information (PI): warnings, contraindications, drug interactions
- DrugBank or equivalent mechanism-of-action data for magnesium acetate specifically
- Direct clinical or preclinical evidence testing magnesium acetate (not acetate/magnesium generally) in hypertension
- Clarification of trial relevance for NCT05251402 and NCT00570479, which currently appear to be keyword-matching artifacts rather than genuine evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

