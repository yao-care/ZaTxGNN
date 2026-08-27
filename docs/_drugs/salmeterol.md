---
layout: default
title: Salmeterol
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 7
---

# Salmeterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the report template directly — this is a content-generation task following the given evidence pack, not a coding/dev task, so no other skill applies.

# Salmeterol: From Asthma/COPD Maintenance Therapy to Bronchitis

## One-Sentence Summary

Salmeterol is a long-acting beta2-adrenergic agonist (LABA) bronchodilator, with published literature in this evidence pack documenting established use in asthma and chronic obstructive pulmonary disease (COPD). The TxGNN model predicts it may also be effective for **Bronchitis** (chronic bronchitis / COPD-associated bronchitis), with **16 clinical trials** and **20 publications** currently supporting this direction. Salmeterol is not currently registered with SAHPRA and has no marketed presence in South Africa.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Data unavailable — SALMETEROL has no SAHPRA license on file (market status: not marketed); pharmacological literature in this pack documents it as a LABA bronchodilator used in asthma/COPD |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (Data Gap DG002). Based on the literature evidence included in this pack, salmeterol is a selective, long-acting β2-adrenoceptor agonist (LABA) that activates bronchial smooth muscle β2 receptors, raises intracellular cAMP, and produces sustained bronchodilation (≥12 hours per dose). This mechanism is described repeatedly across the accompanying literature as the pharmacological basis for its use in asthma and COPD maintenance therapy (e.g., PMID 26051688, PMID 9257086, PMID 11419918).

Chronic bronchitis is one of the two classic phenotypes of COPD (the other being emphysema), and airflow obstruction plus impaired mucociliary clearance are central to its pathophysiology. Several trials and reviews in the evidence pack directly address salmeterol (often combined with fluticasone propionate) "for the treatment of COPD associated with chronic bronchitis" (PMID 15329047, PMID 16915216), and one mechanistic study specifically demonstrates that salmeterol improves mucociliary and cough clearance in patients with chronic bronchitis (PMID 15970448). This gives the TxGNN prediction a plausible, literature-supported pharmacological basis rather than being a purely data-driven artifact.

Because salmeterol lacks a SAHPRA license and formal DrugBank MOA/indication fields in this evidence pack (Data Gaps DG001, DG002), the "original indication" cannot be independently confirmed for the South African regulatory context — this should be resolved before any registration or prescribing decision is made.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | Completed | 130 | Salmeterol/fluticasone propionate 50/500mcg BID vs placebo — bronchial anti-inflammatory activity in COPD (13-week, multicentre) |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | Completed | 623 | Tiotropium vs salmeterol vs placebo — 6-month bronchodilator efficacy and safety in COPD |
| [NCT04655508](https://clinicaltrials.gov/study/NCT04655508) | Phase 3 | Terminated | 35 | Fluticasone/salmeterol vs placebo for post-HSCT pediatric bronchiolitis obliterans syndrome with declining FEV1 |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completed | 2000 | Large post-marketing use investigation of salmeterol/fluticasone in COPD (chronic bronchitis/emphysema); pneumonia flagged as priority safety signal |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | Bronchodilator effect and safety of long-acting beta agonist maintenance therapy over 12 weeks in COPD |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | Completed | 22155 | Large European drug-utilisation post-authorisation safety study in new users of LAMA/LABA combination therapy for COPD |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | Completed | 639 | Fluticasone/salmeterol vs salmeterol alone on rate of COPD exacerbations following hospitalization |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month chronic safety study of long-acting bronchodilator maintenance therapy in COPD |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Phase 4 | Completed | 249 | Fluticasone/salmeterol DISKUS 250/50mcg BID vs placebo — effect on arterial stiffness in COPD |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | Completed | 247 | Fluticasone/salmeterol HFA MDI 230/42mcg vs DISKUS 250/50mcg — efficacy/safety in COPD associated with chronic bronchitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | RCT | Pulmonary pharmacology & therapeutics | Salmeterol vs placebo improved mucociliary and cough clearance in mild-moderate chronic bronchitis patients |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | RCT | Clinical therapeutics | Inhaled salmeterol vs oral theophylline — efficacy, tolerability, and quality-of-life in mild-to-moderate COPD |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | Fluticasone/salmeterol combination vs placebo and individual agents — efficacy and safety in COPD |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | Cohort/Comparative | Therapeutic advances in respiratory disease | One-year safety and tolerance evaluation of salmeterol vs arformoterol in COPD |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & clinical pharmacology & toxicology | Finnish national COPD guideline — diagnosis, assessment, and pharmacotherapy of stable COPD |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | Review of salmeterol/fluticasone propionate DPI, approved for COPD associated with chronic bronchitis |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Meta-analysis | Respiratory research | Meta-analysis of salmeterol vs placebo/usual therapy showing improved outcomes in COPD |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Patient experience trial | MedGenMed | Management of COPD associated with chronic bronchitis with inhaled fluticasone/salmeterol (ADVAIR DISKUS 250/50) |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Comparative/Database | Current medical research and opinion | Healthcare utilization and costs in chronic bronchitis patients initiating fluticasone/salmeterol vs other maintenance therapies |
| [21225021](https://pubmed.ncbi.nlm.nih.gov/21225021/) | 2010 | Review | Drugs of today | Review of COPD/chronic bronchitis pathophysiology and inflammatory disease context relevant to bronchodilator therapy |

---

## South Africa Market Information

Salmeterol currently has **no SAHPRA registration on file** and is classified as **Not Marketed** in South Africa (0 licenses recorded in the evidence pack). No product, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug-interaction data were not available in this evidence pack — this is flagged as a Blocking data gap, see below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bronchitis is supported by L1 evidence — multiple completed Phase 3 trials plus real-world/post-marketing studies (n up to 22,155) — and the underlying LABA mechanism is well documented in the literature for COPD/chronic bronchitis. Two other candidate indications in this evidence pack (asthma, obstructive lung disease) show comparably strong L1 evidence, reinforcing that salmeterol's repurposing signal for obstructive airway disease is pharmacologically coherent rather than a model artifact. Conversely, low-scoring predictions in this pack (respiratory malformation, Rienhoff syndrome, asthma-related genetic susceptibility) have no mechanistic plausibility or supporting evidence and should be disregarded as knowledge-graph noise.

**To proceed, the following is needed:**
- Resolve Blocking Data Gap DG001: obtain TFDA/SAHPRA-equivalent Professional Information (PI) warnings, precautions, and contraindications before any S1 safety evaluation
- Resolve Data Gap DG002: confirm formal DrugBank MOA and original indication data to validate the mechanistic rationale independently of literature inference
- Confirm SAHPRA registration pathway, since salmeterol is not currently marketed in South Africa (0 licenses)
- Formal drug–drug interaction (DDI) review, since the current query returned no results
- Clinical/regulatory review of whether "bronchitis" as a predicted indication is already substantively covered by existing international COPD labeling, to determine if this represents a true label-extension opportunity or a labeling/therapeutic-area clarification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

