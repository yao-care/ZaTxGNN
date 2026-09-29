---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Clarithromycin: From Bacterial Infections to Hyperamylasemia (Top Prediction) and Monoclonal Gammopathy (Best-Supported Candidate)

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, registered in South Africa as oral tablets. The registration data supplied does not state its approved indications.
The TxGNN model's top-ranked new indication is **hyperamylasemia**, supported by only **1 case report** that does not show a treatment effect.
The best-supported candidate among the 10 predictions is **monoclonal gammopathy**, with **1 completed Phase 2 trial** and **20 publications**. The evidence there comes mostly from multiple myeloma combination regimens, so it is adjacent rather than direct.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied |
| Predicted New Indication | Hyperamylasemia (rank 1); monoclonal gammopathy (rank 7) has the strongest evidence |
| TxGNN Prediction Score | 99.35% (hyperamylasemia); 98.81% (monoclonal gammopathy) |
| Evidence Level | L4 (hyperamylasemia); L2 (monoclonal gammopathy) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Clarithromycin is a macrolide antibiotic, and its efficacy against bacterial infections is well established. Whether it is mechanistically applicable to the predicted indications depends on the disease.

**Hyperamylasemia (rank 1): not supported.** The only linked paper (PMID 15228140) is a 2004 case report of *Mycobacterium abscessus* lung infection with primary macroamylasemia. Clarithromycin was probably given as an antimycobacterial agent, not to treat the raised amylase. The high TxGNN score is a graph prediction, not clinical support.

**Monoclonal gammopathy (rank 7): plausible but indirect.** In multiple myeloma, clarithromycin is used as an add-on to lenalidomide, pomalidomide or thalidomide plus dexamethasone. Proposed contributions are:
- inhibition of autophagy in plasma cells;
- immunomodulation;
- CYP3A4 inhibition, which raises dexamethasone exposure.

The only disease-specific evidence is one Phase 2 trial in monoclonal gammopathy of undetermined significance (MGUS). It combines clarithromycin with DHEA, so the effect of clarithromycin alone cannot be isolated. Most of the papers concern symptomatic myeloma or Waldenström macroglobulinemia, which are more advanced diseases than MGUS. Whether a benefit exists in a low-risk premalignant population that would normally not be treated is unestablished.

**Other predictions.** The remaining seven predictions have no supporting evidence or only off-topic papers. They are:
- polyclonal hyperviscosity syndrome;
- congenital analbuminemia;
- blood group incompatibility;
- premalignant hematological system disease;
- septicemic plague;
- hematological disease associated with an acquired peripheral neuropathy;
- congenital hematological disorder.

Punctate epithelial keratoconjunctivitis has a plausible but indirect macrolide rationale (ocular surface inflammation). Its single 2024 paper (PMID 38472959) has a truncated title that does not show whether clarithromycin was studied, so it needs full-text review.

## Clinical Trial Evidence

The only registered trial found relates to monoclonal gammopathy (rank 7), not to hyperamylasemia, which has no trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006219](https://clinicaltrials.gov/study/NCT00006219) | Phase 2 | Completed | Not reported | Randomized trial comparing DHEA with clarithromycin (Biaxin) in MGUS and borderline-significance patients at high risk of progressing to myeloma. No results were supplied, and the regimen confounds the effect of clarithromycin alone. |

No SANCTR or PACTR registrations were retrieved.

## Literature Evidence

Papers below relate to monoclonal gammopathy and myeloma (rank 7), plus the single hyperamylasemia paper (rank 1). Twenty papers were linked to monoclonal gammopathy, and the 9 most relevant are shown.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34021118](https://pubmed.ncbi.nlm.nih.gov/34021118/) | 2021 | RCT (Phase 3) | Blood Cancer J | 286 transplant-ineligible myeloma patients received lenalidomide + dexamethasone with or without clarithromycin. The truncated abstract suggests no significant PFS difference, which needs full-text confirmation. |
| [30792190](https://pubmed.ncbi.nlm.nih.gov/30792190/) | 2019 | Phase 2 | Blood Adv | Clarithromycin + pomalidomide + dexamethasone in 120 relapsed/refractory myeloma patients with prior lenalidomide exposure. |
| [34424561](https://pubmed.ncbi.nlm.nih.gov/34421561/) | 2021 | Phase 2 | Am J Hematol | Carfilzomib/dexamethasone induction, then lenalidomide/clarithromycin/dexamethasone consolidation and lenalidomide maintenance in newly diagnosed myeloma. |
| [24576165](https://pubmed.ncbi.nlm.nih.gov/24576165/) | 2014 | Phase 2 | Leuk Lymphoma | T-BiRD (thalidomide, clarithromycin, lenalidomide, dexamethasone) in 26 newly diagnosed symptomatic myeloma patients. |
| [24723438](https://pubmed.ncbi.nlm.nih.gov/24723438/) | 2014 | Retrospective cohort | Am J Hematol | Clarithromycin added at progression on lenalidomide/dexamethasone in 24 heavily pretreated myeloma patients. |
| [17989313](https://pubmed.ncbi.nlm.nih.gov/17989313/) | 2008 | Trial | Blood | BiRD as first-line therapy in symptomatic myeloma. The title reports high complete- and overall-response rates. |
| [12720150](https://pubmed.ncbi.nlm.nih.gov/12720150/) | 2003 | Phase 2 | Semin Oncol | Waldenström macroglobulinemia. Single-agent thalidomide was tested in 20 patients, then a clarithromycin, thalidomide and dexamethasone combination. |
| [36394758](https://pubmed.ncbi.nlm.nih.gov/36394758/) | 2022 | Meta-analysis | Eur Rev Med Pharmacol Sci | Efficacy and safety of pomalidomide/dexamethasone-based triplet regimens in relapsed/refractory myeloma. |
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | Rank 1 (hyperamylasemia). A 76-year-old man with *M. abscessus* lung infection and primary macroamylasemia. It does not show a clarithromycin effect on amylase. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 51/20.1.1/0193 | Claribax | Tablet | Not stated in the data supplied |
| Reg. No. A38/20.1.1/0631 | Mylan clarithromycin | Tablet | Not stated in the data supplied |

Both products are oral tablets. Only the oral route is registered.

## Safety Considerations

- **Drug Interactions:** No interaction records were retrieved, and this should be read as missing data, not as an absence of interactions. Clarithromycin is a strong CYP3A4 inhibitor and prolongs the QT interval. This matters for any combination regimen, such as with dexamethasone, lenalidomide or pomalidomide.

For key warnings and contraindications, please refer to the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperamylasemia, rests on one case report that does not show a treatment effect. The best-supported candidate, monoclonal gammopathy, has only one Phase 2 trial with a confounded regimen and no results, and its literature comes mostly from symptomatic myeloma. The safety review is also blocked, because SAHPRA package-insert warnings and contraindications have not been obtained.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications, approved indications), which is the blocking gap for safety screening
- Mechanism of action data (DrugBank)
- Results or publications from NCT00006219, and the full-text outcome of the randomized myeloma trial (PMID 34021118)
- A structured interaction review, including QT risk and CYP3A4 effects, for any combination regimen
- Full-text review of PMID 38472959 to confirm whether clarithromycin was studied for punctate epithelial keratoconjunctivitis
- Justification that treatment benefit is plausible in low-risk premalignant MGUS

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

