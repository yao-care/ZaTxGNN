---
layout: default
title: Cilazapril
parent: Model Prediction Only (L5)
nav_order: 121
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Cilazapril: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertension (hypertensive disorder). The registration record in th…"
monitor_inn: "CILAZAPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Cilazapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cilazapril: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Cilazapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
supported by **4 preclinical publications** (animal and in vitro studies) and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder). The registration record in the data compiled for this report has no approved indication text, so this comes from the knowledge graph. |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia (the best-supported of the predictions, ranked 2nd by TxGNN; the top-ranked prediction, pulmonary hypertension with unclear multifactorial mechanism, has no supporting studies) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold (treat as a research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cilazapril is known to be an ACE inhibitor: it blocks angiotensin-converting enzyme and so lowers angiotensin II. Its efficacy in hypertension is established, and mechanistically it may be applicable to pulmonary hypertension linked to lung disease or low oxygen levels.

The renin-angiotensin system acts in the lung blood vessels as well as in the systemic circulation. Four preclinical publications from 1991 to 1997 support this link:
- In rats exposed to chronic hypoxia, cilazapril reduced the thickening of the pulmonary artery wall.
- In a second rat study, cilazapril protected against the rise in mean pulmonary arterial pressure and the fall in arterial oxygen (PaO2) under chronic hypoxia.
- A study of local pulmonary arterial ACE suggests it plays a role in developing hypoxic pulmonary hypertension.
- In cultured heart muscle cell aggregates, cilazapril and captopril sped up recovery from hypoxia.

All of this evidence comes from animals or cell cultures. Whether it applies to patients is untested. Two further predictions, malignant renovascular hypertension and malignant hypertensive renal disease, are mechanistically plausible but largely overlap with the existing hypertension use. They are better seen as extensions of the current indication than as new repurposing opportunities.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1708054](https://pubmed.ncbi.nlm.nih.gov/1708054/) | 1991 | Preclinical animal study | J Cardiovasc Pharmacol | Studied whether cilazapril prevents thickening of the pulmonary artery wall in rats exposed to chronic hypoxia (8% oxygen for 4 weeks) |
| [7712584](https://pubmed.ncbi.nlm.nih.gov/7712584/) | 1994 | Preclinical animal study | Zhonghua Jie He He Hu Xi Za Zhi | Cilazapril protected against the rise in mean pulmonary arterial pressure and the fall in PaO2 in rats with chronic hypoxic pulmonary hypertension |
| [10072805](https://pubmed.ncbi.nlm.nih.gov/10072805/) | 1997 | Preclinical animal study (mechanistic) | Zhonghua Jie He He Hu Xi Za Zhi | Examined the role of the local pulmonary arterial renin-angiotensin system in hypoxic pulmonary hypertension |
| [1378120](https://pubmed.ncbi.nlm.nih.gov/1378120/) | 1992 | In vitro study | J Cardiovasc Pharmacol | Cilazapril and captopril accelerated recovery from hypoxia in cultured myocardial cell aggregates |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/7.1.3/0022 | Inhibace plus 5mg/12.5mg | Tablet (oral) | Not available in the data compiled for this report |

The Essential Medicines List (EML) inclusion status of cilazapril is not stated in the data compiled for this report.

## Safety Considerations

**Drug Interactions**: The interaction data compiled for this report only record the pharmacological target of cilazapril (angiotensin-converting enzyme, ACE). No specific drug-drug interactions are listed.

**Points raised in the repurposing assessment (not from label text):**
- Systemic hypotension and effects on hypoxic pulmonary vasoconstriction would need consideration in patients with lung disease or hypoxia.
- For the renal-related predictions, ACE inhibitors can cause acute decline in renal function in bilateral renal artery stenosis, as well as hyperkalaemia and acute kidney injury.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold (treat as a research question)**

**Rationale:**
The TxGNN score is high (99.2%), and animal studies support a plausible effect in hypoxic pulmonary hypertension. However, there are no human studies, the evidence is more than 25 years old, and safety information from the SAHPRA label has not been reviewed. The other predictions (multifactorial pulmonary hypertension, malignant renovascular hypertension, malignant hypertensive renal disease) rest on computational prediction alone.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI) warnings and contraindications. This gap blocks the safety screening step.
- Detailed mechanism of action data (for example from DrugBank).
- The approved indication text and Essential Medicines List status for the registered product (Inhibace plus is a combination-strength product name, so the active ingredients should be confirmed).
- Human evidence: a literature search for clinical studies, and ideally a pilot or Phase 2 study in pulmonary hypertension associated with lung disease or hypoxia.
- A safety plan covering blood pressure, renal function and potassium monitoring in patients with chronic lung disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

