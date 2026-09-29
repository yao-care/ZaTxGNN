---
layout: default
title: Warfarin
parent: Moderate Evidence (L3-L4)
nav_order: 471
evidence_level: L4
indication_count: 10
---

# Warfarin
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

# Warfarin: From Anticoagulation for Thromboembolism to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, used to prevent and treat blood clots. The TxGNN model predicts it may be useful for **heparin cofactor 2 deficiency**, a rare inherited clotting tendency. Support is thin: **0 clinical trials** and **5 publications** (one general review, three case reports and one laboratory-method paper).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation for thromboembolic disease (general drug knowledge; the SAHPRA record supplied has no indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank field in this pack. Warfarin is known to reduce the vitamin K-dependent clotting factors II, VII, IX and X, and this is the mechanism relevant here.

Heparin cofactor 2 (HCII) deficiency is a rare inherited thrombophilia. Thrombin is inhibited less effectively (this inhibition normally depends on dermatan sulfate), which raises the risk of clots. Long-term anticoagulation after a clot is a standard approach in inherited thrombophilias. Warfarin lowers the clotting factors that drive thrombin generation, so the link is plausible.

This would be an extension of routine secondary prevention of venous thromboembolism, not a new mechanism. No study compares warfarin with any alternative specifically in HCII deficiency. The high score is therefore best read as a plausible fit and not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care STDs | Review of thrombosis in HIV infection. It lists hypercoagulable abnormalities, including deficiencies of natural anticoagulants. It is not specific to HCII deficiency. |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | A 14-year-old girl with familial HCII deficiency had a large thrombus in the right ventricular outflow tract. It was initially mistaken for a myxoma and removed surgically. |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Laboratory method | Arch Pathol Lab Med | A clinical laboratory assay for HCII was evaluated. Low levels were seen in liver disease, consumptive coagulopathy and preeclampsia. |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report | J UOEH | A family had multiple thromboses, including an infant death from inferior vena cava thrombosis. One sibling was started on warfarin at age 2 and had another thrombosis at age 7. |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | A 48-year-old woman with congenital antithrombin II (HCII) deficiency and recurrent thromboembolism, including pulmonary infarction, was treated with warfarin for 7 years. Low-dose heparin was given after warfarin was stopped. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 54/8.2/0676 | Segavin 5 Mg | Tablet (oral) | Not stated in the record supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a handful of old case reports and a general review, with no trials and no comparative data. Warfarin's use after thrombosis in this condition would be standard practice, not a validated repurposing signal. The SAHPRA package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data from DrugBank
- A structured review of registry or cohort data on anticoagulated HCII-deficient patients
- Explicit management of bleeding risk, INR monitoring, pregnancy (teratogenicity) and interacting drugs

Among the other predictions in this pack, **thrombophilia** (rank 4) has the strongest evidence (L3, Proceed with Guardrails). It is worth assessing first. Warfarin for **migraine disorder** (rank 10) is a separate research question supported only by case reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

