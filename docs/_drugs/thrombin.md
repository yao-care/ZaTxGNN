---
layout: default
title: Thrombin
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Thrombin
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

# Thrombin: From Haemostatic Sealant Component (Tisseel) to Primary Release Disorder of Platelets

## One-Sentence Summary

Thrombin is the clotting enzyme that turns fibrinogen into fibrin, and in South Africa it is registered as a component of the fibrin sealant Tisseel.
The TxGNN model predicts it may be useful for **primary release disorder of platelets**, but this is a model prediction only, with **no directly relevant clinical trials** and **no literature** among the 50 trials retrieved.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

The SAHPRA indication text for the registered product is not recorded in the data, so the original indication cannot be quoted.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, thrombin is a strong platelet agonist that acts through the PAR1 and PAR4 receptors and triggers granule release. This is why the graph links it to a platelet release disorder.

That link describes how platelets normally work. It does not show that thrombin treats the disorder. A platelet that cannot release its granules would not be corrected by giving more thrombin, so the relationship is diagnostic or mechanistic, not therapeutic. None of the retrieved trials tests thrombin in this condition, and the trial hits look like keyword noise.

## Clinical Trial Evidence

None of the 50 retrieved trials tests thrombin in platelet release disorders. All graded trials were rated "C" (unrelated). The table shows the few that touch on haemostasis; they are context only, not supporting evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00043940](https://clinicaltrials.gov/study/NCT00043940) | Phase 3 | Completed | 50 | Bivalirudin (a thrombin inhibitor) for PCI in heparin-induced thrombocytopenia. It blocks thrombin, so it does not support thrombin as a treatment. |
| [NCT02593877](https://clinicaltrials.gov/study/NCT02593877) | Phase 2 | Completed | 412 | Viscoelastic assay-guided versus conventional resuscitation in bleeding trauma patients. General haemostasis, not thrombin. |
| [NCT03341156](https://clinicaltrials.gov/study/NCT03341156) | Phase 3 | Terminated | 14 | Prothrombin complex concentrate versus standard transfusion in heart transplantation. Different product and disease. |
| [NCT04684719](https://clinicaltrials.gov/study/NCT04684719) | Phase 3 | Completed | 1020 | Low-titre whole blood in prehospital haemorrhagic shock. Different intervention and disease. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/30.3/0263 | Tisseel | Powder | Not recorded in the data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interactions were found. The evidence pack also flags embolic and thrombotic risk as needing formal safety review before any new use, since thrombin is a procoagulant.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction with no supporting trials or literature. The proposed mechanism is diagnostic, not therapeutic, and exogenous thrombin would not correct a platelet release defect.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- Any direct evidence that thrombin has a therapeutic role in this disorder

**Other predictions worth a separate review:**
- **Esophageal disease** is the strongest signal in the pack, at evidence level L3. Endoscopic and EUS-guided thrombin injection is already used for bleeding gastric varices. There is a systematic review and meta-analysis of observational data, several cohort studies, and a small TachoSil feasibility study on esophageal anastomoses (NCT02105506). Extrapolating from gastric varices to esophageal disease is uncertain, and controlled evidence is lacking.
- **Glanzmann thrombasthenia** has indirect mechanistic evidence at level L4 (thrombin generation and bypassing agents such as rFVIIa). No study tests exogenous thrombin as therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

