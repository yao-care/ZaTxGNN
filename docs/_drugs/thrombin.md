---
layout: default
title: Thrombin
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Thrombin: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Thrombin"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "non-syndromic esophageal malformation", "esophageal disease", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "Scott syndrome", "HER2 positive breast carcinoma", "thrombocytopenia due to immune destruction"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Thrombin: From Its Registered South African Use to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Thrombin is registered in South Africa as a single-ingredient product (Tisseel), but the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be relevant to **primary release disorder of platelets**, a group of inherited platelet function defects.
There are **no registered clinical trials** and **20 publications** for this prediction, and the publications are general background reviews that do not test thrombin as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the registration record has no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Thrombin is a well-known strong platelet activator. It triggers platelet granule release, which is the process that is defective in release disorders of platelets. This shared biology is the most likely reason the model linked the two.

The link is mechanistic rather than therapeutic. Thrombin is a physiological activator of clotting, so giving it systemically would carry a major risk of thrombosis. The retrieved literature covers general topics (coagulation in cirrhosis, restenosis after angioplasty, heparin-induced thrombocytopenia, platelet gels). None of it tests thrombin as a treatment for this disorder. The prediction should therefore be read as a hypothesis, not as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomised trials were identified. The table lists reviews first, followed by other background papers.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Review (expert practice update) | Gastroenterology | Guidance on altered coagulation in cirrhosis, coagulation testing and the use of anticoagulants and pro-coagulants |
| [1321709](https://pubmed.ncbi.nlm.nih.gov/1321709/) | 1992 | Review | Disease-a-Month | Overview of platelet function disorders and how platelets support thrombin generation and fibrin clots |
| [33749992](https://pubmed.ncbi.nlm.nih.gov/33749992/) | 2021 | Review | Wound Repair and Regeneration | Platelet concentrates activated with thrombin or calcium form platelet gels used in chronic wound healing |
| [11079020](https://pubmed.ncbi.nlm.nih.gov/11079020/) | 2000 | Review | Archives of Pathology & Laboratory Medicine | Pathophysiology, diagnosis and treatment of heparin-induced thrombocytopenia |
| [12556215](https://pubmed.ncbi.nlm.nih.gov/12556215/) | 2003 | Review | Expert Opinion on Investigational Drugs | Thrombin signals through protease-activated receptors; therapeutic potential of PAR-1 antagonists |
| [14727968](https://pubmed.ncbi.nlm.nih.gov/14727968/) | 2002 | Review | American Journal of Cardiovascular Drugs | New targets for antithrombotic drugs, based on platelet adhesion and activation pathways |
| [35344028](https://pubmed.ncbi.nlm.nih.gov/35344028/) | 2022 | Review | Biochemical Journal | Immunothrombosis and tissue factor control by pyroptosis; prospects for new anticoagulants |
| [35226963](https://pubmed.ncbi.nlm.nih.gov/35226963/) | 2022 | Review | Hamostaseologie | Experience with routine genetic analysis of hereditary bleeding, thrombotic and platelet disorders |
| [22841202](https://pubmed.ncbi.nlm.nih.gov/22841202/) | 2012 | Review | Transplantation Proceedings | Coagulopathy management in liver transplantation |
| [26860124](https://pubmed.ncbi.nlm.nih.gov/26860124/) | 2016 | Commentary | International Journal of Stroke | Vorapaxar, a platelet thrombin receptor blocker, and the call for a stroke prevention trial |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/30.3/0263 | Tisseel | Powder | Not stated in the data compiled for this report |

This is the only registration (single-ingredient, valid). Essential Medicines List status could not be determined from the available data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The data compiled for this report show no recorded drug interactions. They also show no knowledge-graph contraindications for the predicted indication. This reflects missing data, not proven safety. The model-based rationale does flag a theoretical risk: because thrombin is a physiological clotting activator, systemic exposure could cause thrombosis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no registered trials, and the available literature is general background that does not evaluate thrombin as a therapy for platelet release disorders. The safety concern about thrombosis with systemic use, together with missing label safety data, argues against proceeding.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI), to confirm the approved indication, warnings and contraindications
- Detailed mechanism of action data
- Preclinical or clinical studies that test thrombin directly in platelet release disorders, with a defined route of administration
- A thrombosis risk assessment for any route beyond local application

**Note on other predictions:** In the same candidate list, the prediction for *esophageal disease* (rank 5) has stronger support than the main indication. It includes a Phase 3 randomised trial of thrombin versus Histoacryl injection in bleeding gastric varices ([NCT01717612](https://clinicaltrials.gov/study/NCT01717612), status unknown, 62 participants) and a systematic review and meta-analysis ([PMID 33728506](https://pubmed.ncbi.nlm.nih.gov/33728506/)). That evidence concerns gastric varices specifically, so it would need separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

