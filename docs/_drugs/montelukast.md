---
layout: default
title: Montelukast
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Montelukast
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

# Montelukast: From Asthma to Bronchitis

## One-Sentence Summary

Montelukast is a cysteinyl leukotriene receptor (CysLT1) antagonist globally established for the treatment of asthma and allergic rhinitis. The TxGNN model predicts it may also be effective for **Bronchitis**, with **23 clinical trials** and **20 publications** currently supporting this direction — though the "bronchitis" label spans several distinct disease entities (post-transplant bronchiolitis obliterans syndrome, pediatric viral/obstructive bronchitis, and eosinophilic bronchitis) that require separate evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (standard global indication; not captured in the source registry's `original_indications` field) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source drug record for this evaluation. Based on well-established pharmacology, montelukast is a selective, orally active cysteinyl leukotriene (CysLT1) receptor antagonist. Its efficacy in asthma — where it blocks LTD4-mediated bronchoconstriction, eosinophilic airway inflammation, and mucus hypersecretion — has been proven for decades and is its approved global indication.

The "bronchitis" prediction is mechanistically plausible because several bronchitis-spectrum conditions share leukotriene-driven inflammatory pathways with asthma: eosinophilic bronchitis (elevated cysLT activity), post-hematopoietic-stem-cell-transplant/lung-transplant bronchiolitis obliterans syndrome (BOS, where montelukast has been studied as part of the FAM regimen — fluticasone/azithromycin/montelukast), and viral-induced bronchiolitis in infants (RSV-associated leukotriene release). However, these are pathophysiologically distinct entities from ordinary chronic bronchitis, and the evidence base is fragmented across them rather than concentrated on a single, well-defined target population.

A separate caveat: "asthma" itself also appears in this candidate list with a high evidence level (L1). That is **not** a genuine repurposing signal — it reflects montelukast's already-approved indication appearing because the source database's `original_indications` field was empty, not a new discovery. It is retained here for context but should not be treated as a repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01307462](https://clinicaltrials.gov/study/NCT01307462) | Phase 2 | Completed | 36 | Fluticasone+Azithromycin+Montelukast (FAM) in bronchiolitis obliterans after stem cell transplant |
| [NCT04613180](https://clinicaltrials.gov/study/NCT04613180) | Phase 4 | Unknown | 100 | Montelukast in children with recurrent obstructive bronchitis |
| [NCT00863317](https://clinicaltrials.gov/study/NCT00863317) | N/A | Completed | 141 | Double-blind placebo RCT of daily montelukast for viral bronchiolitis |
| [NCT00076973](https://clinicaltrials.gov/study/NCT00076973) | Phase 3 | Completed | 1125 | MK0476 (montelukast) vs placebo for RSV-induced bronchiolitis symptoms in children |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | DB placebo RCT of montelukast for bronchiolitis obliterans syndrome after lung transplant |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Multi-institutional montelukast for bronchiolitis obliterans after allogeneic/autologous SCT |
| [NCT03072849](https://clinicaltrials.gov/study/NCT03072849) | N/A | Completed | 23 | Early detection/management of BOS after pediatric HSCT using FAM therapy |
| [NCT01121016](https://clinicaltrials.gov/study/NCT01121016) | Phase 4 | Unknown | 63 | Add-on montelukast to budesonide in nonasthmatic eosinophilic bronchitis (DB RCT) |
| [NCT00394160](https://clinicaltrials.gov/study/NCT00394160) | Phase 2 | Completed | 12 | Safety/tolerability/PK of montelukast oral granules in infants 1–3 months with bronchiolitis |
| [NCT00524693](https://clinicaltrials.gov/study/NCT00524693) | N/A | Completed | 51 | Double-blind placebo RCT of montelukast in acute RSV bronchiolitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26475726](https://pubmed.ncbi.nlm.nih.gov/26475726/) | 2016 | RCT/Cohort | Biol Blood Marrow Transplant | Phase II FAM (fluticasone/azithromycin/montelukast) trial for new-onset BOS after HCT (NCT01307462 report) |
| [25563311](https://pubmed.ncbi.nlm.nih.gov/25563311/) | 2015 | RCT | Chinese Medical Journal | Add-on montelukast improves airway inflammation, cough, and quality of life in nonasthmatic eosinophilic bronchitis |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Cohort/RCT | Respiratory Research | Budesonide/formoterol + montelukast + N-acetylcysteine for BOS after HSCT |
| [24118637](https://pubmed.ncbi.nlm.nih.gov/24118637/) | 2014 | Systematic Review | Pediatr Allergy Immunol | Systematic review of montelukast's efficacy for preventing post-bronchiolitis wheezing |
| [38504551](https://pubmed.ncbi.nlm.nih.gov/38504551/) | 2024 | Review | Ther Adv Respir Dis | Review of montelukast's therapeutic potential and mechanisms in BOS after transplantation |
| [38485149](https://pubmed.ncbi.nlm.nih.gov/38485149/) | 2024 | Guideline/Review | Eur Respir J | ERS/EBMT clinical practice guidelines on pulmonary chronic GVHD treatment |
| [35114411](https://pubmed.ncbi.nlm.nih.gov/35114411/) | 2022 | Prospective Phase II | Transplant Cell Ther | Phase II trial of montelukast for BOS after HCT, with investigation into BOS pathogenesis |
| [22819521](https://pubmed.ncbi.nlm.nih.gov/22819521/) | 2012 | Pilot Study | Respiratory Medicine | Add-on montelukast vs double-dose budesonide in nonasthmatic eosinophilic bronchitis |
| [28545478](https://pubmed.ncbi.nlm.nih.gov/28545478/) | 2017 | Animal Study | J Cardiothorac Surg | LTB4 and montelukast in transplantation-related bronchiolitis obliterans (rat model) |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review | BMJ Clinical Evidence | General overview of bronchiolitis management in infants |

---

## South Africa Market Information

Montelukast currently has **no SAHPRA registration on record** in this evidence pack — market status is **Not Marketed**, with 0 licenses identified. As a result, there is no locally approved Professional Information (PI), dosage form, or approved indication text to reference for the South African market at this time.

---

## Safety Considerations

Source safety data (key warnings, contraindications, drug interactions) contains no usable entries for this evaluation. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Notable safety signal from literature evidence (not part of the formal safety dataset, but recurring across the evidence pack):** Multiple recent publications ([37758273](https://pubmed.ncbi.nlm.nih.gov/37758273/), [39836401](https://pubmed.ncbi.nlm.nih.gov/39836401/), [36948487](https://pubmed.ncbi.nlm.nih.gov/36948487/), [35608857](https://pubmed.ncbi.nlm.nih.gov/35608857/)) discuss the FDA boxed warning on montelukast-associated neuropsychiatric adverse events. This should be factored into any safety monitoring plan, particularly for pediatric use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap in TFDA/SAHPRA warnings and contraindications prevents even an initial (S1) safety review, and the drug is currently unregistered and not marketed in South Africa (0 SAHPRA licenses). In addition, "bronchitis" as predicted here bundles mechanistically distinct conditions — transplant-associated BOS, pediatric viral/obstructive bronchitis, and eosinophilic bronchitis — that need to be evaluated as separate, stratified indications rather than a single diagnosis before any development decision can be made.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (warnings, contraindications, DDI) to resolve the blocking safety data gap
- Confirmed mechanism-of-action documentation for this drug record
- Disease-entity stratification: separate evidence review for post-transplant BOS vs. pediatric viral/obstructive bronchitis vs. eosinophilic bronchitis
- Regulatory pathway assessment for South African market entry, since the product is not currently registered
- A defined neuropsychiatric-risk monitoring plan given the FDA boxed warning signal in the literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

