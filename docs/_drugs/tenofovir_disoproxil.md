---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tenofovir Disoproxil: From Undocumented Original Indication to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir disoproxil (DrugBank DB00300) — the original approved indication for this specific evaluation is not documented in the current evidence pack (Data Gap). The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome (FIV/feline AIDS)** — a **veterinary**, not human, disease — supported by only **2 animal-study publications** and **4 clinical trials that, on relevance review, all involve different drugs and are not applicable**. Given the veterinary nature of the top prediction and a Blocking safety data gap, this candidate is not suitable to advance in a human drug-repurposing pathway at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA/registry license data or original indication text on file (Data Gap) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (veterinary — not a human disease) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for this evaluation is not available (Data Gap DG002 — original_moa unretrieved from DrugBank). Based on the repurposing rationale embedded in the evidence pack, tenofovir disoproxil is described as a nucleotide reverse transcriptase inhibitor (NRTI) prodrug — the active metabolite, PMPA, has documented antiretroviral activity against lentiviruses.

The mechanistic plausibility for the top prediction rests on the fact that Feline Immunodeficiency Virus (FIV) and Human Immunodeficiency Virus (HIV) are both lentiviruses with structurally conserved reverse transcriptase enzymes. Two published animal studies directly evaluated tenofovir (as PMPA) in FIV-infected cats, giving this a genuine — if narrow — mechanistic and empirical basis. However, this is a **veterinary indication**, not a human clinical indication. The four clinical trials returned alongside this prediction all involve different drugs (dolutegravir, darunavir/lamivudine) in human HIV-1 populations, and were flagged internally as low relevance (Grade C) — likely knowledge-graph false positives triggered by semantic proximity of the term "immunodeficiency."

The second-ranked prediction, simian immunodeficiency virus (SIV/SHIV) infection, is mechanistically similar (tenofovir is genuinely used as PrEP against SIV/SHIV in macaque models as a translational proxy for human HIV prevention research), but again describes a non-human infection model rather than a human clinical indication. The third and fourth predictions (a rare neurodevelopmental disorder and an obsolete hyperlipidemia term) have no clinical trials, no literature, and no mechanistic rationale, and are already flagged "Hold" within the evidence pack itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Human HIV-1 trial of dolutegravir vs raltegravir; tenofovir/emtricitabine only a background NRTI option. Not a tenofovir-specific or feline-relevant trial (Grade C relevance). |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Human HIV-1 trial comparing darunavir/lamivudine regimens; tenofovir/emtricitabine used only as a comparator arm. Not relevant to the predicted feline indication (Grade C). |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Human HIV-1 dose-selection trial for dolutegravir, not tenofovir. Not relevant (Grade C). |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Human HIV-1 trial of dolutegravir + abacavir/lamivudine vs Atripla (which contains tenofovir DF). Study drug is dolutegravir, not tenofovir; likely a knowledge-graph mismatch (Grade C). |

**Note:** All four trials above were evaluated as low relevance by the evidence pipeline — they involve different primary study drugs and human (not feline) populations, and appear to have been matched due to shared "immunodeficiency" terminology rather than genuine drug-disease relevance.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Animal Study | Journal of Feline Medicine and Surgery | Direct treatment of FIV-infected cats with PMPA (tenofovir's active metabolite); reports on antiviral treatment outcomes in naturally infected cats. |
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Cohort/Review | Viruses | Evaluated a combination antiretroviral regimen (dolutegravir + tenofovir + emtricitabine, dosed for cats) in FIV-infected domestic cats; assessed pharmacokinetics and immunophenotype outcomes. |

---

## South Africa Market Information

No SAHPRA registrations are on file for this product in the current evidence pack (`total_licenses: 0`, `licenses: []`). Market status is recorded as **not marketed**.

---

## Safety Considerations

Safety data for this evaluation is currently incomplete. Per the evidence pack, the Professional Information (PI) warnings/contraindications (Data Gap DG001) have not yet been retrieved and are flagged as a **Blocking** gap — this evaluation cannot proceed to an initial safety assessment (S1) until PI data is obtained from the relevant regulatory source. No drug-drug interaction data was found in the current query.

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (feline acquired immunodeficiency syndrome) is a veterinary disease, not a human clinical indication, and therefore falls outside the scope of a human drug-repurposing evaluation despite genuine mechanistic plausibility. The supporting clinical trials are not actually relevant to this drug-disease pair (wrong study drugs, Grade C), and a Blocking safety data gap (PI warnings/contraindications) prevents even an initial safety screen. The evidence pack's own scoring already labels this "Research Question" at decision stage S1, not a Go-ready candidate.

**To proceed, the following is needed:**
- Retrieve SAHPRA/TFDA-equivalent Professional Information (PI) to resolve the Blocking safety gap (DG001)
- Retrieve confirmed DrugBank MOA and original approved human indication for this drug record (DG002)
- If pursuing a human-relevant angle, re-scope the research question toward the rank-2 candidate (SIV/SHIV infection), which reflects an established translational model for human HIV pre-exposure prophylaxis, rather than the feline indication
- Disregard rank-3 and rank-4 predictions (neurodevelopmental disorder, obsolete hyperlipidemia term) — no supporting evidence exists for either
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

