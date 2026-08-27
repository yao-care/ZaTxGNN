---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Ezetimibe: From Hypercholesterolemia to Hyperlipoproteinemia

## One-Sentence Summary

Ezetimibe is a cholesterol absorption inhibitor used for hypercholesterolemia and mixed dyslipidemia. The TxGNN model predicts it may be effective for **Hyperlipoproteinemia**, with **50 clinical trials** and **19 publications** currently supporting this direction — though as detailed below, this is less a novel "repurposing" signal and more a confirmation of ezetimibe's already-established lipid-lowering pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / mixed dyslipidemia (based on established pharmacology; not verifiable against a SAHPRA-approved product text, as no license record exists in this evidence pack) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on established pharmacological knowledge, ezetimibe is a selective cholesterol absorption inhibitor that blocks the intestinal NPC1L1 transporter, reducing delivery of dietary and biliary cholesterol to the liver and lowering LDL-C. It is used as monotherapy or in fixed-dose combination with statins (e.g., simvastatin, atorvastatin, rosuvastatin), and its efficacy in hypercholesterolemia and mixed dyslipidemia is well established through decades of clinical use.

Hyperlipoproteinemia is a broad diagnostic category encompassing elevated LDL-cholesterol and/or triglyceride-rich lipoproteins — mechanistically, this is essentially the same lipid pathway ezetimibe already targets in its approved use. As the underlying repurposing rationale notes, this is **not a typical old-drug-new-use case**: the evidence base consists largely of existing Phase 3/4 trials and post-marketing surveillance for ezetimibe's core lipid-lowering activity, rather than trials in a mechanistically distinct disease.

The clinical trial record strongly supports this overlap: large placebo-controlled and active-comparator Phase 3/4 studies (e.g., ezetimibe/simvastatin plus fenofibrate, ezetimibe plus colesevelam, the ENHANCE trial) directly evaluate ezetimibe-based regimens in hyperlipidemic populations, reinforcing that the TxGNN signal reflects confirmatory rather than exploratory evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin + fenofibrate coadministration in mixed hyperlipidemia; cholesterol-lowering effects assessed |
| [NCT00655265](https://clinicaltrials.gov/study/NCT00655265) | Phase 4 | Completed | 86 | Colesevelam as add-on to statin + ezetimibe in familial hypercholesterolaemia not at LDL-C target |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in HeFH |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | Completed | 407 | Obicetrapib/ezetimibe fixed-dose combination on top of maximally tolerated therapy in HeFH/ASCVD |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate + ezetimibe coadministration efficacy/safety in mixed hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate + ezetimibe coadministration, safety and effectiveness in mixed hyperlipidemia |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin + extended-release niacin in Type IIa/IIb hyperlipidemia |
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | Completed | 11332 | Large Japanese post-marketing use investigation of Zetia (ezetimibe) mono/combination therapy, 12-week safety/efficacy |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Phase 3 | Completed | 450 | VICTORION-INITIATE: "inclisiran first" strategy vs usual care (including ezetimibe) on LDL-C in ASCVD |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Phase 1 | Completed | 18 | PK/drug-interaction study: Vytorin (ezetimibe/simvastatin) with Niaspan (extended-release niacin) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT | Lancet | TANDEM trial: fixed-dose obicetrapib + ezetimibe significantly reduces LDL-C |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab vs placebo in HeFH, with statin ± ezetimibe background therapy |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in HeFH patients not at LDL-C goal on existing therapy |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Comprehensive review of familial hypercholesterolaemia pathophysiology and treatment |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Pathophysiology, diagnosis, and treatment of postprandial hyperlipidemia |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Research advances in current drugs targeting hyperlipidemia |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovasc Pharmacol Ther | Comprehensive review of PCSK9 inhibitors as adjuncts to statin/ezetimibe therapy |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Consensus Statement | European Heart Journal | EAS consensus: FH is underdiagnosed/undertreated, guidance for CHD prevention |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C/ApoB-lowering therapies, positioning ezetimibe among treatment options |
| [25053660](https://pubmed.ncbi.nlm.nih.gov/25053660/) | 2014 | Consensus Statement | European Heart Journal | EAS position paper on homozygous FH detection and clinical management |

---

## South Africa Market Information

Ezetimibe currently has **no active SAHPRA product registrations** on file in this evidence pack (0 licenses), and the drug's market status is recorded as **not marketed** in South Africa. No product-level details (registration number, product name, dosage form, approved indication text) are available.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: retrieval of the PI/warnings and contraindications is flagged as a Blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is backed by an L1 evidence level (multiple completed Phase 3/4 RCTs), but this largely reflects ezetimibe's already-established lipid-lowering pharmacology rather than a genuinely novel indication. Two critical gaps prevent a stronger "Go" recommendation: the drug is not currently marketed in South Africa (0 SAHPRA registrations), and the SAHPRA-approved warnings/contraindications data needed for the safety screen (S1) is missing — a Blocking-severity gap.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, precautions, and contraindications (Blocking)
- DrugBank/MOA detail to formally substantiate the mechanistic link (High priority)
- Confirmation of South African market-entry pathway, since there are currently no active registrations
- Clarification of whether "hyperlipoproteinemia" represents a distinct label extension or falls within ezetimibe's existing approved indications elsewhere
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

