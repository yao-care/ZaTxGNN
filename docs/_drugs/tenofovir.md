---
layout: default
title: Tenofovir
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 3
---

# Tenofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tenofovir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Tenofovir is a nucleotide reverse transcriptase inhibitor (NRTI) already established for human HIV treatment and pre-exposure prophylaxis (PrEP). The TxGNN model's top prediction — **feline acquired immunodeficiency syndrome (FIV)** — is a **veterinary, not a human, disease**, and the supporting clinical trial evidence (4 trials) is misattributed to unrelated human HIV drugs (dolutegravir, darunavir), leaving only 2 preclinical/animal literature reports as genuine support. This candidate is **not actionable for human drug repurposing** in its current form.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection (antiretroviral therapy) / Pre-exposure prophylaxis — referenced within the evidence pack's own rationale; not confirmed by South Africa registration data in this dataset |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (FIV) — a veterinary disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical/mechanistic only) |
| South Africa Market Status | Not Marketed (per this dataset) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap, severity: High). Based on known information, tenofovir is a nucleotide reverse transcriptase inhibitor (NRTI)-class antiretroviral; its efficacy in HIV infection treatment and PrEP is well established, and mechanistically this class of action (reverse transcriptase inhibition) is conserved across lentiviruses, including Feline Immunodeficiency Virus (FIV), the causative agent of feline AIDS.

However, this prediction differs fundamentally from a typical human drug-repurposing case: FIV is a **cat disease**, not a human condition, so it cannot itself be pursued as a new human indication. The one directly relevant literature report (PMID 24782459) confirms that tenofovir's prodrug (PMPA) has antiviral activity in FIV-infected cats — a veterinary pharmacology finding, not a signal for a new human indication.

The associated clinical trial evidence is weaker still: all 4 trials listed under this prediction were graded "C" (low relevance) by the source evidence pack itself, because they studied dolutegravir and darunavir-based regimens for **human HIV**, not tenofovir, and were likely surfaced through disease-keyword overlap (HIV/immunodeficiency) rather than genuine drug-disease relevance. The second-ranked prediction (simian immunodeficiency virus infection, score 99.96%) has the same structural problem — it is a macaque/primate model used in HIV PrEP translational research, not a standalone human indication. The third-ranked prediction (a rare neurodevelopmental disorder, L5, no supporting evidence) appears to be a false positive with no mechanistic plausibility. Taken together, none of the top three TxGNN predictions represent a viable new human indication for tenofovir as presented.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir with dual NRTI backbone in ART-naïve HIV-1 adults — **not a tenofovir trial** |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Darunavir/lamivudine vs darunavir/tenofovir combinations in naïve HIV-1 patients — tenofovir present only as comparator arm component |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-finding for dolutegravir combined with abacavir/lamivudine or tenofovir/emtricitabine — **not a tenofovir trial** |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs Atripla (contains tenofovir) — **not a tenofovir trial** |

**Note:** All four trials were graded "C" (low relevance) in the source evidence pack — they concern human HIV-1 treatment with other antiretrovirals, not tenofovir treatment of FIV, and were most likely surfaced by disease-keyword overlap rather than genuine drug-disease evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Cohort (preclinical, cats) | Journal of Feline Medicine and Surgery | Tenofovir prodrug (PMPA) showed antiviral activity in naturally FIV-infected cats; no registered antiviral compounds otherwise exist for FIV |
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Cohort (preclinical, cats) | Viruses | Combination antiretroviral therapy (dolutegravir/tenofovir/emtricitabine) evaluated for pharmacokinetics and immunophenotype in FIV-infected domestic cats |

---

## South Africa Market Information

Tenofovir is recorded as **not marketed** in this dataset, with **0 SAHPRA registrations**. No product-level registration data (registration number, product name, dosage form, approved indication) is available to report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-drug interaction data are not available in this dataset — this is flagged as a Blocking data gap, DG001, since it prevents a first-stage safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction targets a veterinary disease (FIV), not a human indication, and its supporting clinical trial evidence is misattributed to unrelated human HIV drugs. The remaining top predictions (SIV infection, a rare neurodevelopmental disorder) are similarly non-actionable — one is an animal PrEP research model, the other has no supporting evidence at all. No genuine new human indication has been identified for tenofovir from this evidence set.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank (DG002, High severity)
- SAHPRA-approved Professional Information / warnings and contraindications (DG001, Blocking severity)
- Re-run of the TxGNN disease-mapping step restricted to human-relevant disease ontology terms, to filter out veterinary/animal-model false matches
- Confirmation of current SAHPRA registration status for tenofovir/tenofovir-containing products in South Africa (the "not marketed, 0 registrations" status in this dataset should be verified against the actual SAHPRA register, given tenofovir's established global use in HIV treatment and PrEP)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

