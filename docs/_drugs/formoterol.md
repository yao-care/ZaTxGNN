---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Formoterol: From Established Asthma/COPD Bronchodilator Therapy to Chronic Bronchitis

## One-Sentence Summary

Formoterol is a long-acting β2-adrenergic agonist (LABA) bronchodilator with an internationally established role in asthma and COPD maintenance therapy. Of the six candidate indications surfaced by TxGNN in this evidence pack, the only one that represents a genuinely *new* and *evidence-supported* signal — rather than an already-established use or a data artefact — is **chronic bronchitis / COPD-related airway obstruction**, backed by **28 registered clinical trials** and **20 publications**, including several large Phase 3 RCTs.

> **Note on this bundle:** This evidence pack (`TW-DB00983-multi`) contains six TxGNN-ranked predictions for formoterol. The top-ranked one by score, "respiratory malformation," was flagged by the evidence pipeline itself as an ontology-mapping error (the linked trials are all asthma/COPD studies unrelated to structural airway malformation). Two others ("obstructive lung disease," "asthma") are already-established indications, not novel repurposing candidates. Two others ("Rienhoff syndrome," "asthma-related traits, susceptibility to") have zero supporting evidence. Details for all six are in the addendum table at the end of this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented as structured data in this evidence pack; formoterol's established international indications (per embedded trial/literature context) are asthma and COPD maintenance bronchodilation |
| Predicted New Indication | Chronic Bronchitis (COPD-spectrum airway obstruction) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed (per this evidence pack) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Formoterol is a long-acting β2-adrenoceptor agonist (LABA). It activates β2-receptors on airway smooth muscle, raising intracellular cAMP and producing rapid, sustained bronchodilation — the same mechanism underlying its established use in asthma and COPD. This mechanism is a direct, causal fit for any disease defined primarily by reversible or partially reversible airflow obstruction.

"Bronchitis," however, is not a single clean disease entity in this dataset — the associated trials and literature span at least three distinct conditions: (1) chronic bronchitis as a COPD phenotype, where formoterol-containing combinations (aclidinium/formoterol, budesonide/formoterol, glycopyrronium/formoterol) have large Phase 3 RCT support for airflow and symptom improvement; (2) bronchiolitis obliterans after allogeneic haematopoietic stem cell transplantation, a distinct post-transplant fibrotic small-airway disease where formoterol/budesonide combinations have been trialled with more modest, Phase 2/cohort-level evidence; and (3) acute infectious bronchitis, for which no direct evidence appears in this bundle. The prediction is mechanistically plausible for the first two entities but requires disease-entity disambiguation before it can be treated as a single "new indication."

By contrast, formoterol's own regulatory history in obstructive lung disease and asthma (ranks 4–5 in this bundle) is not a *new* prediction at all — it is formoterol's existing, guideline-endorsed use, which only appears here as a "prediction" because this evidence pack's `original_indications` field was not populated (data gap DG002 in the meta block).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01437397](https://clinicaltrials.gov/study/NCT01437397) | Phase 3 | Completed | 1,692 | Fixed-dose aclidinium bromide/formoterol vs. individual components and placebo, 24 weeks, moderate-to-severe stable COPD (chronic bronchitis phenotype) |
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | Completed | 2,443 | Aclidinium/formoterol fixed-dose combinations vs. components and placebo, maintenance bronchodilator treatment of COPD |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Phase 4 | Recruiting | 128 | Inhaled triple therapy vs. COPD and chronic bronchitis without obstruction secondary to biomass/wood-smoke exposure |
| [NCT01560689](https://clinicaltrials.gov/study/NCT01560689) | Phase 2 | Completed | 32 | Open-label inhaled budesonide/formoterol in bronchiolitis obliterans after allogeneic stem cell transplantation |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | Completed | 457 | Dose-finding trial, fluticasone propionate/formoterol fumarate in COPD |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | Completed | 741 | (R,R)-formoterol (arformoterol) bronchodilator effect and safety in COPD |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | Completed | 443 | Long-term safety, arformoterol tartrate inhalation solution in COPD |
| [NCT01049360](https://clinicaltrials.gov/study/NCT01049360) | Phase 2 | Completed | 128 | Aclidinium bromide/formoterol fixed-dose combinations, dose-ranging, stable moderate-to-severe COPD |
| [NCT02526758](https://clinicaltrials.gov/study/NCT02526758) | Phase 4 | Unknown | 90 | Evaluation and treatment of small airway disease (obstructive bronchitis) and emphysema in COPD |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | Unknown | 20 | Arformoterol vs. salmeterol, inspiratory capacity and HRCT comparison in COPD |

*28 formoterol/bronchitis trials are registered on ClinicalTrials.gov in total; the 10 above were prioritized for phase, sample size, and direct disease relevance.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27916620](https://pubmed.ncbi.nlm.nih.gov/27916620/) | 2017 | RCT | Chest | Glycopyrrolate/formoterol co-suspension MDI efficacy and safety in COPD (PINNACLE-1/2) |
| [20714376](https://pubmed.ncbi.nlm.nih.gov/20714376/) | 2010 | Review | Int J Chron Obstruct Pulmon Dis | Clinical efficacy and safety review of nebulized formoterol in COPD |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | Cohort | Respiratory Research | Budesonide/formoterol + montelukast + N-acetylcysteine for bronchiolitis obliterans syndrome post-HSCT |
| [37696312](https://pubmed.ncbi.nlm.nih.gov/37696312/) | 2023 | Cohort | Respiratory Medicine | Inhaled tiotropium add-on to budesonide/formoterol in bronchiolitis obliterans post-HSCT |
| [28821260](https://pubmed.ncbi.nlm.nih.gov/28821260/) | 2017 | Phase IIIb crossover | Respiratory Research | 24-hour bronchodilation with glycopyrrolate/formoterol MDI in COPD |
| [31920296](https://pubmed.ncbi.nlm.nih.gov/31920296/) | 2019 | Extension study | Int J Chron Obstruct Pulmon Dis | Long-term safety/efficacy of budesonide/glycopyrrolate/formoterol MDI in Japanese COPD patients |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | Comparative risks of budesonide/formoterol vs. placebo/monotherapies in stable COPD |
| [32606643](https://pubmed.ncbi.nlm.nih.gov/32606643/) | 2020 | Non-interventional study | Int J Chron Obstruct Pulmon Dis | Real-world effectiveness/tolerability of LABA/LAMA FDCs including aclidinium/formoterol (DETECT study) |
| [27143870](https://pubmed.ncbi.nlm.nih.gov/27143870/) | 2016 | Review | Int J Chron Obstruct Pulmon Dis | Scientific rationale for LAMA+LABA dual bronchodilator therapy in COPD |
| [41654451](https://pubmed.ncbi.nlm.nih.gov/41654451/) | 2026 | Pharmacovigilance study | Clinical Therapeutics | Real-world safety of budesonide/formoterol via FAERS, JADER, and CVAR databases |

---

## South Africa Market Information

This evidence pack records **no SAHPRA registration entries** for formoterol (0 licenses, market status "Not Marketed"). This is notable given formoterol is an internationally established respiratory medicine, and should be independently verified against SAHPRA's current registered products list before this is treated as a true market-access gap — it may instead reflect incomplete regulatory data extraction for this evidence pack (see data gap DG001 in the meta block).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Additional context from the evidence bundle's own analysis (not sourced from a formal safety database, verify against PI):** LABA monotherapy in asthma carries a well-recognised class-level boxed-warning concern — formoterol should not be used as monotherapy in asthma and must be combined with an inhaled corticosteroid. This is flagged explicitly in the mechanistic rationale for the "asthma" prediction within this same bundle and should be treated as a guardrail item regardless of which indication is pursued.

---

## Other Predicted Indications in This Evidence Bundle

Since this evidence pack bundles six TxGNN predictions for formoterol, the table below summarizes the other five for transparency:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Respiratory malformation | 99.92% | L5 | Hold | Flagged by the evidence pipeline as an ontology-mapping error — all 19 linked trials are asthma/COPD studies unrelated to structural airway malformation; no biological mechanism supports this link |
| 3 | Rienhoff syndrome | 99.90% | L5 | Hold | Rare connective-tissue disorder (TGFBR1/2 pathway); no mechanistic link to β2-agonism; zero trials, zero literature |
| 4 | Obstructive lung disease | 99.90% | L1 | Proceed with Guardrails | Not a novel prediction — this is formoterol's established indication; appears here only because `original_indications` was not populated in this evidence pack |
| 5 | Asthma | 99.74% | L1 | Proceed with Guardrails | Same as above — established indication, not a new repurposing signal |
| 6 | Asthma-related traits, susceptibility to | 99.50% | L5 | Hold | A genetic susceptibility trait, not a treatable clinical disease entity; zero trials, zero literature |

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Formoterol's bronchodilator mechanism is directly relevant to chronic bronchitis/COPD-spectrum airway obstruction, and this is supported by multiple large Phase 3 RCTs (e.g., NCT01437397, n=1,692; NCT01462942, n=2,443) — but the underlying disease-entity mapping ("bronchitis") mixes at least two clinically distinct conditions (COPD-associated chronic bronchitis and post-transplant bronchiolitis obliterans) that need to be disambiguated before this can be treated as a single, actionable indication.

**To proceed, the following is needed:**
- Disambiguation of "bronchitis" into its constituent clinical entities (chronic bronchitis/COPD vs. bronchiolitis obliterans) with entity-specific evidence review
- SAHPRA Professional Information (PI) retrieval to confirm South African registration status, warnings, and contraindications (currently a data gap)
- Confirmation of formoterol's actual original/registered indication in South Africa, since this field was empty in the source evidence pack
- Re-run of the TxGNN ontology mapping for "respiratory malformation" to correct the apparent knowledge-graph error before it is reused in future prediction cycles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

