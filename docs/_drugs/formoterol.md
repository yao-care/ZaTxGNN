---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 238
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Formoterol: From Asthma and COPD Bronchodilation to Respiratory Malformation

## One-Sentence Summary

Formoterol is a long-acting beta2-agonist bronchodilator used in inhalers for asthma and chronic obstructive pulmonary disease (COPD). The TxGNN model predicts it may be effective for **respiratory malformation** with a very high score (99.92%), but none of the **19 registered trials** studies malformation and there are **no publications** for this indication. The prediction is therefore not supported by evidence and is most likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA record. Asthma and COPD are inferred from the trial evidence and the drug class |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no actual studies for this indication). The source data labels it L4, but no preclinical or mechanism studies were found |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 (one appears to be a data-linkage error, see below) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Formoterol is known to be a long-acting beta2-adrenoceptor agonist. It relaxes airway smooth muscle and produces bronchodilation. It has no known effect on the structural or developmental processes that cause malformations.

The original and predicted indications are not mechanistically related. Asthma and COPD are functional airflow-obstruction diseases, while a respiratory malformation is a structural, developmental defect. The very high TxGNN score most likely reflects general proximity of "respiratory tract" nodes in the knowledge graph, not a real pharmacological link.

The trials retrieved for this prediction are all asthma or COPD studies matched through a broad search term. They do not support a malformation indication.

---

## Clinical Trial Evidence

No trial in the evidence pack studies respiratory malformation. The trials below were returned by keyword matching and are all asthma or COPD studies. No SANCTR or PACTR identifiers are available.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1811 | Once-daily FF/UMEC/VI versus budesonide/formoterol in COPD. Not relevant to malformation |
| [NCT01566149](https://clinicaltrials.gov/study/NCT01566149) | Phase 3 | Completed | 49 | Safety and tolerability of mometasone/formoterol inhaler in persistent asthma |
| [NCT05421598](https://clinicaltrials.gov/study/NCT05421598) | Phase 2 | Completed | 446 | Amlitelimab add-on in moderate-to-severe asthma. Indirect keyword match |
| [NCT03573817](https://clinicaltrials.gov/study/NCT03573817) | Phase 3 | Completed | 122 | Safety of nebulized revefenacin with formoterol in COPD |
| [NCT00931385](https://clinicaltrials.gov/study/NCT00931385) | Phase 3 | Completed | 99 | 24-hour lung function profile of BI 1744 CL versus Foradil in COPD |
| [NCT03324607](https://clinicaltrials.gov/study/NCT03324607) | Phase 2/3 | Completed | 20 | Glycopyrrolate/formoterol effect on ventilation, assessed by 129Xe MRI in COPD |
| [NCT00130351](https://clinicaltrials.gov/study/NCT00130351) | Phase 3 | Completed | 155 | Patient use of a formoterol multi-dose dry powder inhaler in asthma |
| [NCT01577082](https://clinicaltrials.gov/study/NCT01577082) | Phase 3 | Completed | 542 | Beclomethasone/formoterol versus beclomethasone in uncontrolled asthma |
| [NCT03888131](https://clinicaltrials.gov/study/NCT03888131) | Phase 3 | Completed | 750 | Beclomethasone/formoterol versus budesonide/formoterol in COPD |
| [NCT02062463](https://clinicaltrials.gov/study/NCT02062463) | Phase 3 | Completed | 485 | Inhaler technique for budesonide/formoterol Spiromax versus Turbohaler in asthma |

---

## Literature Evidence

Currently no related literature available for respiratory malformation.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A39/21.5.1/0506 | Vannair 80/4.5mcg per inhalation 120 dos | Inhaler | Not stated in the record |
| Reg. No. 36/2.6.5/0070 | Seroquel | Tablet | Not stated in the record |

**Data-quality note:** Vannair (budesonide/formoterol) is consistent with formoterol. Seroquel is an oral tablet whose brand name is normally associated with quetiapine, not formoterol. This registration is probably linked to the wrong record and should be checked against SAHPRA before it is relied on. Essential Medicines List (EML) status is not included in the evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications for respiratory malformation, and there is no plausible link between beta2-agonism and developmental defects. The high score appears to be a knowledge-graph proximity artefact.

**To proceed, the following is needed:**
- Do not pursue this indication unless a mechanistic rationale and disease-specific evidence emerge.
- Correct the record: the original indication is missing, and the Seroquel registration appears mislinked.
- Obtain the SAHPRA package insert warnings and contraindications, and DrugBank mechanism of action data.
- Note that other predictions in the same pack are established uses of formoterol, not novel repurposing. Obstructive lung disease and asthma are both at evidence level L1 with a "Proceed with Guardrails" recommendation. Bronchitis is at L2, supported mainly by COPD trials. For asthma, long-acting beta2-agonists must not be used as monotherapy.
- Two other predictions have no evidence: Rienhoff syndrome (L5) and "asthma-related traits, susceptibility to". The latter is a genetic trait term, not a treatable clinical indication.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

