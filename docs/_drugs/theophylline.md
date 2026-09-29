---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 441
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Bronchodilator Use (Asthma/COPD) to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator used in airway diseases such as asthma and COPD.
The TxGNN model predicts it may be effective for **thrombotic disease**, but this is a model prediction only, with **0 clinical trials** and **no publication that tests theophylline for thrombosis**.
The mechanistic link is unclear, and this indication is not recommended for further investment at this stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA licence records supplied. Theophylline's known use is as a bronchodilator in asthma and COPD, per the literature in the pack. |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is not available in this pack. Based on known pharmacology, theophylline is a phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. Its efficacy as a bronchodilator and anti-inflammatory agent in airway disease is well established.

The plausible link to thrombosis is through platelets. PDE inhibition raises platelet cAMP, which generally reduces platelet activation, and older platelet-biology papers show cAMP elevation opposing aggregation. However, adenosine normally has an antiplatelet effect, so blocking adenosine receptors could work against this. The net direction is therefore unclear.

The high TxGNN score is likely to reflect patterns in the knowledge graph rather than tested evidence. None of the retrieved papers tests theophylline as a treatment for thrombosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 18 retrieved papers are mostly indirect, and none is a trial of theophylline for thrombosis. The most relevant ones are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clin Pharmacokinet | Pharmacokinetics of ticlopidine, an antiplatelet drug. Background on antiplatelet therapy only, not theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostacyclin raises platelet cAMP and opposes aggregation. This supports the general cAMP rationale but does not test theophylline. |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | In vitro study | Gen Pharmacol | Milrinone (a different PDE inhibitor) raised platelet cAMP and reduced aggregation, and interacted with adenosine. Indirect support for the mechanism only. |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohort | Rheumatology (Oxford) | Platelet and neutrophil activation in Behçet's disease. Not a theophylline treatment study. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational | Cor Vasa | T-lymphocyte subsets in vascular disease. Theophylline was used as a laboratory marker, not as therapy. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory method | Br J Haematol | Theophylline was used as an additive in blood collection for a platelet factor 4 assay. It is not a therapeutic use. |
| [14231672](https://pubmed.ncbi.nlm.nih.gov/14231672/) | 1964 | Clinical article | Z Gesamte Inn Med | Chronic cor pulmonale from thromboembolic disease. No abstract available and no evidence for theophylline benefit. |
| [7307205](https://pubmed.ncbi.nlm.nih.gov/7307205/) | 1981 | Case series | Chir Ital | Diagnosis and treatment of Raynaud's phenomenon in 120 patients. No abstract-level link to theophylline efficacy. |

## South Africa Market Information

The record lists 9 registrations in total, but only 5 entries were supplied, and one of them (Alcophyllin) appears twice. No approved indication text was recorded for any product, and Essential Medicines List (EML) status is not available in the pack.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G721 (OM) | Alcophyllin | Syrup | Not stated in the supplied record |
| S/10.2/126 | Nuelin liquid | Syrup | Not stated in the supplied record |
| M/10.2/0533 | Theophen | Syrup | Not stated in the supplied record |
| G892 (OM) | Adco-Metaxol | Suspension | Not stated in the supplied record |

All supplied products are oral liquids (syrup or suspension).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Literature elsewhere in the pack describes theophylline as having a narrow therapeutic window, needing serum level monitoring and having notable interactions (for example CYP1A2 substrates and macrolides). These points should be confirmed against the PI.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.62% score is the only support for thrombotic disease. There are no trials, no direct studies, and an unclear net mechanism, because adenosine antagonism may oppose the cAMP-mediated antiplatelet effect.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which currently blocks any safety screening
- Detailed mechanism-of-action data from DrugBank
- Direct experimental evidence, such as in vitro platelet aggregation studies with theophylline and clinical data in thrombosis
- Confirmation that the empty original-indication field is a data gap, not a true absence of registered indications

**Other predictions in the same pack:**
- **Obstructive lung disease (L3, Proceed with Guardrails):** this appears to be an existing use rather than true repurposing. Guardrails are serum level monitoring, and CYP1A2 and macrolide interaction checks.
- **Nasal cavity disease (L2, Research Question):** this has one small completed Phase 2 trial of nasal theophylline irrigation (NCT03990766, n=27). Its randomisation and results still need confirmation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

