---
layout: default
title: Ipratropium
parent: Moderate Evidence (L3-L4)
nav_order: 269
evidence_level: L4
indication_count: 10
---

# Ipratropium
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ipratropium: From Established Bronchodilator Use to Obstructive Lung Disease

## One-Sentence Summary

Ipratropium is an inhaled anticholinergic bronchodilator, currently marketed in South Africa under 14 SAHPRA registrations.
The TxGNN model predicts it for **obstructive lung disease** (score 99.97%). This is essentially its established use in COPD, so it is a confirmation of an existing indication rather than a true repurposing finding.
The prediction is linked to **50 registered trials** (about a dozen name ipratropium, Atrovent or Combivent) and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied SAHPRA data (the literature describes use as a bronchodilator in COPD and asthma) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** L1 rests on two completed Phase 3 randomised trials that include ipratropium in COPD: NCT02177253 and NCT00274040. The second is filed under a different disease label ("respiratory malformation") in the source data but studies COPD.

---

## Why is This Prediction Reasonable?

The DrugBank mechanism-of-action field was not available for this report. The published literature describes ipratropium as a non-selective muscarinic receptor antagonist (a synthetic quaternary derivative of atropine). It blocks vagally mediated bronchoconstriction on airway smooth muscle (PMIDs 15987237, 2977109). Cholinergic tone is a major driver of airflow obstruction in COPD, so this mechanism directly fits obstructive lung disease.

The model is therefore recovering a known use, not finding a new one. Ipratropium is a well-established COPD bronchodilator, used alone and in combination with salbutamol or fenoterol (PMIDs 20163324, 15257628). It has also served as the active comparator in later trials of tiotropium and other newer agents.

The other nine predictions on the candidate list are weaker. The most mechanistically plausible is nasal cavity disease, where cholinergic blockade reduces secretions (rhinorrhoea). See the Conclusion for a summary.

---

## Clinical Trial Evidence

The trials below were selected because they directly involve ipratropium or Combivent/Atrovent in COPD. Many other trials linked to this prediction test different drugs (for example indacaterol, losmapimod and umeclidinium/vilanterol) or are device or physiotherapy studies, so they are not listed. No SANCTR or PACTR identifiers were present in the evidence pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Completed | 1118 | 12-week double-blind study comparing ipratropium/salbutamol via Respimat with Combivent aerosol, ipratropium Respimat and placebo in COPD |
| [NCT00274040](https://clinicaltrials.gov/study/NCT00274040) | Phase 3 | Completed | 141 | Double-blind, double-dummy comparison of tiotropium 18 mcg once daily with ipratropium MDI (Atrovent) 4 times daily in COPD |
| [NCT02194205](https://clinicaltrials.gov/study/NCT02194205) | Phase 3 | Terminated | 360 | One-year comparison of Combivent HFA with Combivent CFC and placebo in COPD |
| [NCT00388882](https://clinicaltrials.gov/study/NCT00388882) | Phase 4 | Completed | 327 | 12-week comparison of tiotropium with Combivent CFC MDI in COPD patients already using Combivent |
| [NCT01243788](https://clinicaltrials.gov/study/NCT01243788) | Phase 4 | Unknown | 450 | Salmeterol/fluticasone twice daily compared with ipratropium/albuterol 4 times daily in Chinese patients with moderate-to-severe COPD |
| [NCT06040424](https://clinicaltrials.gov/study/NCT06040424) | Phase 3 | Unknown | 74 | Non-inferiority study of ipratropium/levosalbutamol fixed-dose combination versus the free combination with salbutamol in stable COPD |
| [NCT02238197](https://clinicaltrials.gov/study/NCT02238197) | N/A | Completed | 477 | Post-marketing surveillance of Atrovent 500 µg/2 ml inhalation solution in COPD (tolerability and efficacy in daily practice) |
| [NCT02238171](https://clinicaltrials.gov/study/NCT02238171) | N/A | Completed | 346 | Post-marketing surveillance of Atrovent Inhalets in COPD (tolerability and efficacy in daily practice) |
| [NCT01350128](https://clinicaltrials.gov/study/NCT01350128) | Phase 2 | Completed | 103 | Dose-finding study of PT001 with open-label Atrovent HFA as active control in moderate-to-severe COPD |
| [NCT04315558](https://clinicaltrials.gov/study/NCT04315558) | Phase 2 | Completed | 21 | Nebulised revefenacin versus nebulised ipratropium in COPD patients with acute respiratory failure on invasive ventilation |

Two caveats apply to this table:
- Most trials here use ipratropium as a comparator or as part of a combination, not as the single test drug.
- The listed summaries describe study designs, not results. Efficacy conclusions should come from the full publications.

---

## Literature Evidence

No randomised trial reports were classified in the pack. The list is led by systematic reviews, then reviews, then clinical studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Updated review comparing tiotropium with ipratropium in stable COPD |
| [16625543](https://pubmed.ncbi.nlm.nih.gov/16625543/) | 2006 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Ipratropium versus short-acting beta-2 agonists in stable COPD |
| [16856113](https://pubmed.ncbi.nlm.nih.gov/16856113/) | 2006 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Ipratropium versus long-acting beta-2 agonists in stable COPD |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Systematic Review | Expert Opin Drug Metab Toxicol | Mechanism, efficacy and safety of albuterol, ipratropium and their combination in COPD |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Efficacy and safety data on using ipratropium together with tiotropium in COPD |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Review | Treat Respir Med | Ipratropium HFA: non-selective muscarinic antagonist redesigned with a non-CFC propellant |
| [1835291](https://pubmed.ncbi.nlm.nih.gov/1835291/) | 1991 | Double-blind crossover study | Am J Med | Single-dose ipratropium (36 µg) versus titrated theophylline versus placebo in 21 stable COPD patients |
| [1835292](https://pubmed.ncbi.nlm.nih.gov/1835292/) | 1991 | Clinical study | Am J Med | Ipratropium (0.036 mg), albuterol (0.18 mg) and placebo compared on FEV1, FVC, heart rate and blood pressure in 72 patients with severe COPD |
| [28461224](https://pubmed.ncbi.nlm.nih.gov/28461224/) | 2017 | Clinical study | EBioMedicine | Sex-related differences in FEV1 response to ipratropium in mild-to-moderate COPD |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | Retrospective analysis | Medicine | Probiotics added to budesonide plus ipratropium in 118 COPD patients, assessing lung function and gut microbiota |

---

## South Africa Market Information

Five of the 14 registrations are shown below. The approved indication text was not captured in the supplied records, so please check the SAHPRA-approved Professional Information (PI) for each product.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 33/10.2.1/0214 | Ipvent-40 | Inhaler |
| Reg. No. 35/10.2.1/0004 | Adco-nebrafen 4ml | Vial |
| Reg. No. 37/10.2.1/0462 | Ipvent Respules | Nebuliser |
| Reg. No. 29/10.2.1/0015 | Combivent | Inhaler |
| Reg. No. 51/10.2.1/0153 | Iprabut | Nebuliser |

- Combivent is an ipratropium/salbutamol combination, according to the trial records above.
- The route listing also shows oral tablet and capsule forms. These are unusual for ipratropium and are not among the five registrations above, so please verify them against the registration records.
- Essential Medicines List (EML) status was not part of the supplied data. Check the current South African EML and Standard Treatment Guidelines.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The literature attached to this evidence pack (not the PI) reports two individual safety signals:
- **Anaphylaxis:** a case report of severe anaphylaxis after ipratropium inhalation (PMID 8449120).
- **Unilateral mydriasis:** a case in an infant with bronchiolitis after inhaled ipratropium, which can mimic serious neurological conditions (PMID 40069469).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For obstructive lung disease (COPD), the trials and reviews are substantial and the drug is widely marketed in South Africa. However, this is an established use, not a new repurposing opportunity. The SAHPRA safety information has not yet been reviewed.

**To proceed, the following is needed:**
- Download the SAHPRA PI for each registered product and extract the approved indications, warnings and contraindications. This is required before safety screening.
- Retrieve the DrugBank mechanism-of-action entry to complete the mechanistic analysis.
- Confirm the indications and dosage forms of the SAHPRA registrations, including the unexpected oral forms, and check the EML status.
- Check the full texts of the comparator-style trials to confirm ipratropium's role in each.

**Other predictions in the candidate list:**

| Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Nasal cavity disease | L4 | Research Question | Plausible antisecretory mechanism, but no trials. A specific indication such as rhinitis should be defined first. |
| Pharyngitis | L4 | Hold | Weak, indirect link. The attached trials do not test ipratropium. |
| Tracheal disease | L4 | Hold | Preclinical support only. The one trial is a withdrawn device study. |
| Respiratory malformation | L4 | Hold | The disease label appears mis-mapped, and the trials are COPD or other airway studies. |
| Anaphylaxis | L4 | Hold | Only animal data support it, and a case report of ipratropium-induced anaphylaxis argues against it. |
| Acute laryngopharyngitis, papillary conjunctivitis, Rienhoff syndrome, food-dependent exercise-induced anaphylaxis | L5 | Hold | No trials or literature, and no supported rationale. |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

