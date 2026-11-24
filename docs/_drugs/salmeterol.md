---
layout: default
title: Salmeterol
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "SALMETEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: predicted new indication Respiratory malformation (evidence level L5). In South Africa: 43 SAHPRA registrations (38 valid)"
---

# Salmeterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Salmeterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Salmeterol is an inhaled long-acting beta2-agonist bronchodilator.
The TxGNN model predicts it may be useful for **respiratory malformation**, but no study directly examines this condition. The only support is **2 indirect clinical trials** (cystic fibrosis and asthma in pregnancy) and a small set of loosely related publications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 38 of 43; 1 of the valid not confirmed by SAHPRA) |
| Number of SAHPRA Registrations | 43 (valid: 38, of which 1 not confirmed by SAHPRA) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for salmeterol: "Salmeterol is a selective LABA. In vitro studies show salmeterol to be at least 50 times more selective for beta 2 -adrenoceptors than albuterol. Although beta 2 -adrenoceptors are the predominant adrenergic receptors in bronchial smooth muscle and beta 1 -adrenoceptors are the predominant receptors in the heart, there are also beta 2 -adrenoceptors in the human heart comprising 10% to 50% of the total beta-adrenoceptors." ([DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4), label version 2022-10-10; accessed 2026-11-19.) Salmeterol is a long-acting beta2-adrenergic agonist. Drugs of this class relax airway smooth muscle and may also raise ciliary beat frequency and support mucociliary clearance.

This gives a possible link to ciliary disorders such as primary ciliary dyskinesia. "Respiratory malformation" is a broad, structurally defined category, though. Bronchodilation or ciliary stimulation is not an established treatment mechanism for it.

The supporting trials concern cystic fibrosis and asthma in pregnancy, and the literature mostly addresses other airway conditions. The evidence is therefore indirect. The high TxGNN score is a model output and does not show that the drug works for this condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | Not applicable | Suspended | Not reported | Long-term salmeterol vs albuterol or placebo, inhaled twice daily for 6 months, in cystic fibrosis. This is a different disease. |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | Not stated | Completed | 1 | Asthma treatment in pregnancy and adverse pregnancy outcomes. It is not about respiratory malformation. |

No SANCTR or PACTR registrations were identified in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | RCT | JAMA Pediatrics | Inhaled corticosteroids alone and with long-acting beta2-agonists for reduced lung function in preterm-born children. This is the closest paediatric lung-development setting, but not a malformation. |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | Journal of Asthma | Review of a budesonide/formoterol inhaler in persistent asthma. Context for long-acting beta2-agonist use only. |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Case report | Arerugi | Primary ciliary dyskinesia in a girl previously treated as asthma. It illustrates the ciliary-disorder angle but gives no evidence of drug benefit. |

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 29/10.2.1/0350 | Serevent accuhaler 60dose | Acc | Valid |
| 55/21.5.4/0278 | Spirodisc 50/100 | inhaler | Valid |
| 55/21.5.4/0279 | Spirodisc 50/250 | inhaler | Valid |
| 55/21.5.4/0280 | Spirodisc 50/500 | inhaler | Valid |
| 42/21.5.4/0218 | Sereflo 25/50 hfa synchrobreathe 120 dos | inhaler | Valid |

Showing 5 of 43 registrations (valid registrations first).

<!-- licenses:end -->

Essential Medicines List status is not available in the data compiled for this report.

<!-- review:begin za-lic-20261105-salmeterol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "One further licence (Med-lemon flu & congestion hot medication, sachet, Reg. No. 27/5.8/0430) is cancelled. Essential Medicines List status is not available in the data compiled for this report." Removed: it said the registrations were cancelled, not registered, or not valid, which did not match the SAHPRA registration data as of 2026-11-05. The Quick Overview and the table under South Africa Market Information show the current figures. Source: [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/).

<!-- review:end za-lic-20261105-salmeterol-1 -->

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; main ones shown):
  - **Major:** clarithromycin.
  - **Moderate:** epinephrine, famotidine, isometheptene, diethylpropion, dolasetron, and glucose-lowering agents (acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, albiglutide, dulaglutide).
  - **Minor:** corticosteroids such as hydrocortisone, dexamethasone, budesonide, beclomethasone, betamethasone and triamcinolone.

Warnings and contraindications from the SAHPRA label are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study directly addresses respiratory malformation, so the evidence level is L5. The trials and publications concern other diseases, and the proposed mechanism is speculative for a structural condition.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer biological rationale linking beta2-agonist or ciliary effects to the specific malformation types of interest
- Studies directly in patients with respiratory malformation, such as case series or registry data
- The SAHPRA Professional Information, to complete warnings, contraindications and approved-use details
- A review of dosage-form and route suitability for the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against SAHPRA registration data (the SAHPRA medicine register export). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "One further licence (Med-lemon flu & congestion hot medication, sachet, Reg. No. 27/5.8/0430) is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [SAHPRA medicine register (medapps export)](https://medapps.sahpra.org.za:6006/DateSearch/ExportData); [SAHPRA](https://www.sahpra.org.za/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Serevent Diskus (salmeterol xinafoate) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12d9728e-6b5c-4aee-bfb0-745e542ed2e4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

