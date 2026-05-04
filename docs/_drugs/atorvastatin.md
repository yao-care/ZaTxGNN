---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 6
---

# Atorvastatin
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

# Atorvastatin: From Dyslipidaemia to Familial Hypercholesterolaemia

## One-Sentence Summary

Atorvastatin is a widely used HMG-CoA reductase inhibitor (statin) indicated globally for the treatment of dyslipidaemia and prevention of atherosclerotic cardiovascular disease.
The TxGNN model predicts it may be highly effective for **Familial Hypercholesterolaemia (FH)**, with **35 clinical trials** and **19 publications** currently supporting this direction.
Evidence strength is rated **L1**, and the recommended decision is **Proceed with Guardrails**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-approved indication on record in this dataset |
| Predicted New Indication | Familial Hypercholesterolaemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| South Africa Market Status | Not registered (0 SAHPRA licences recorded) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **⚠ Data Quality Note:** This Evidence Pack records zero SAHPRA licences for atorvastatin. Given that atorvastatin (Lipitor® and multiple generic products) is widely used in South Africa and appears in national Standard Treatment Guidelines and the Essential Medicines List, this almost certainly reflects a data collection gap rather than true absence from the South African market. Direct verification with the [SAHPRA online register](https://www.sahpra.org.za) is essential before any regulatory or formulary decision.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, atorvastatin inhibits HMG-CoA reductase — the rate-limiting enzyme in hepatic cholesterol biosynthesis. By blocking this step, atorvastatin reduces intracellular cholesterol in liver cells, which triggers compensatory upregulation of LDL receptors on the hepatocyte surface and accelerates clearance of LDL-C from the bloodstream. Its prolonged half-life (20–30 hours) and active metabolites sustain this effect throughout the dosing interval.

Familial Hypercholesterolaemia is a monogenic disorder caused by loss-of-function mutations in the LDL receptor gene (*LDLR*), apolipoprotein B (*ApoB*), or gain-of-function mutations in *PCSK9* — all of which impair the liver's ability to clear LDL-C from circulation. Despite this receptor-level defect, atorvastatin remains clinically effective because it amplifies the expression of any remaining functional LDL receptors and concurrently reduces hepatic LDL production, achieving LDL-C reductions of 20–60% even in FH patients. This mechanistic pathway forms the direct pharmacological rationale for atorvastatin's primary global indication.

Multiple completed Phase 3 trials confirm clinical benefit in both heterozygous FH (HeFH) and the more severe homozygous form (HoFH), and international guidelines from the AACE/ACE, ESC/EAS, and local South African lipid societies uniformly recommend high-intensity statin therapy — with atorvastatin and rosuvastatin as the preferred agents — as first-line pharmacotherapy for FH. The extremely high TxGNN prediction score of 99.42% therefore directly mirrors this well-established mechanistic and clinical evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | Completed | 30 | Forced-titration study of torcetrapib/atorvastatin in HoFH; torcetrapib arm discontinued Dec 2006 due to safety signals, but study design provides atorvastatin monotherapy dose-escalation data in HoFH |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | Double-blind RCT evaluating carotid intima-media thickness (IMT) regression with torcetrapib/atorvastatin vs atorvastatin monotherapy over 24 months in HeFH; atorvastatin control arm provides a large-scale monotherapy benchmark |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | Completed | 400 | Double-blind RCT comparing torcetrapib/atorvastatin vs maximally tolerated atorvastatin alone in HeFH over 6 months; atorvastatin arm is the primary active comparator |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term open-label safety study (up to 24 months) of ezetimibe co-administered with atorvastatin or simvastatin in HoFH; supports combination therapy in severe FH |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Double-blind RCT evaluating ezetimibe 10 mg added to atorvastatin vs atorvastatin alone in HeFH or high-CV-risk patients with LDL-C not controlled on atorvastatin 10 mg |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | 12-month open-label extension evaluating long-term safety of ezetimibe + atorvastatin 10–80 mg in HeFH and coronary heart disease patients uncontrolled on atorvastatin monotherapy |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | 3-year prospective open-label study of atorvastatin in paediatric HeFH (from age 6); characterised growth, pubertal development, and sustained LDL-C reduction over 36 months — key safety dataset for paediatric use |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Double-blind RCT comparing alirocumab vs ezetimibe added to atorvastatin vs atorvastatin dose escalation vs switch to rosuvastatin in high-CV-risk patients with nonfamilial or HeFH not controlled on atorvastatin |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | Pharmacokinetic/pharmacodynamic study evaluating safety and tolerability of atorvastatin in children and adolescents with HeFH; supports paediatric dose selection |
| [NCT02460159](https://clinicaltrials.gov/study/NCT02460159) | Phase 3 | Completed | 135 | Long-term safety and tolerability of ezetimibe/atorvastatin fixed-dose combination (10/10 mg and 10/20 mg) in Japanese patients with hypercholesterolaemia uncontrolled on monotherapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Study | J Am Coll Cardiol | First study to quantify the statin-induced reduction in coronary artery disease events and all-cause mortality specifically in heterozygous FH patients; confirms substantial survival benefit |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidaemia management and cardiovascular prevention; endorses high-intensity statins (including atorvastatin) as first-line pharmacotherapy for FH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical Review | Ann Pharmacother | Foundational review of atorvastatin efficacy and safety in primary hypercholesterolaemia and mixed dyslipidaemias; establishes dose-response relationship and LDL-C reduction benchmarks |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Curr Atheroscler Rep | Up-to-date review of novel pharmacological therapies for HoFH; contextualises atorvastatin's established role alongside PCSK9 inhibitors, inclisiran, and lomitapide |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical Study | J Clin Lipidol | 3-year study of atorvastatin in children and adolescents (from age 6) with HeFH; confirms sustained LDL-C lowering and no adverse effects on growth, BMI, or Tanner staging over extended paediatric use |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical Study | Echocardiography | Atorvastatin treatment improves myocardial and peripheral blood flow reserve in FH patients without overt coronary atherosclerosis; demonstrates early pleiotropic vascular benefit beyond LDL-C lowering |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Clinical Study | Nutr Metab Cardiovasc Dis | Head-to-head comparison of atorvastatin vs simvastatin in HeFH; atorvastatin achieves NCEP LDL-C targets more frequently and was also associated with reductions in fibrinogen |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic Epidemiology | Pharmacogenomics J | Integrates FH genetic diagnosis with pharmacogenomic statin prescribing using NGS; supports personalised atorvastatin dosing and addresses adherence through genotype-guided strategy |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | J Am Coll Cardiol | Highlights persistent underdiagnosis and undertreatment of FH globally; calls for systematic cascade screening and optimal statin (including atorvastatin) utilisation |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Clinical Review | Rev Med Bruxelles | Characterises atorvastatin's mechanism of action, prolonged half-life of active metabolites (20–30 hours), and superior LDL-C reduction compared to contemporaneous statins; provides pharmacological foundation |

---

## South Africa Market Information

No SAHPRA-registered products were found for atorvastatin in this Evidence Pack (total licences: 0).

> **Important:** This data reflects a collection gap. Atorvastatin is a widely prescribed medicine in South Africa, available under the brand name **Lipitor®** (Pfizer) and numerous generic formulations. It is listed on the **South African Essential Medicines List (EML)** for ambulatory and hospital care, and it appears in Standard Treatment Guidelines for primary and secondary cardiovascular prevention. Healthcare professionals should consult the [SAHPRA online register](https://www.sahpra.org.za) directly to confirm current registration numbers, approved dosage forms, strengths, and full approved indication text.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for complete safety information. Report adverse drug reactions to SAHPRA via the **MedSafety** portal or the **MedSafety App**.

> **Prescriber Alert — Drug Interactions in HIV-Positive Patients:** South Africa carries a significant burden of HIV co-morbidity. When atorvastatin is prescribed alongside antiretroviral therapy — particularly ritonavir-boosted or cobicistat-boosted protease inhibitors — CYP3A4-mediated drug–drug interactions can substantially increase atorvastatin plasma exposure, elevating the risk of myopathy and rhabdomyolysis. In such cases, **atorvastatin should not exceed 20 mg/day**. Consult the current atorvastatin PI and applicable HIV treatment guidelines for full interaction management guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting atorvastatin for familial hypercholesterolaemia is exceptionally robust — multiple completed Phase 3 RCTs demonstrate LDL-C reductions of 20–60% in both HeFH and HoFH, international guidelines uniformly endorse atorvastatin as first-line therapy, and the mechanistic rationale (HMG-CoA reductase inhibition → LDL receptor upregulation) is direct and well established. The TxGNN model prediction score of 99.42% reflects this existing evidence base rather than a speculative repurposing leap.

**To proceed, the following is needed:**

- **Verify SAHPRA registration status** directly via the SAHPRA online register; retrieve approved indication text, registered dosage forms (10 mg, 20 mg, 40 mg, 80 mg tablets), and current regulatory standing for all registered atorvastatin products in South Africa
- **Obtain the current SAHPRA-approved Professional Information (PI)** to confirm key warnings, contraindications, approved dose ranges, and pregnancy/lactation restrictions
- **Establish a clinical monitoring plan** covering: fasting lipid profile at baseline and 4–12 weeks post-initiation (with LDL-C target documented), liver function tests at baseline, and creatine kinase (CK) measurement if myalgia is reported
- **Implement structured DDI screening** for all FH patients co-prescribed antiretroviral therapy (particularly boosted PI regimens) given South Africa's high HIV prevalence — dose capping at 20 mg/day where applicable
- **Consider formal paediatric FH pathway** establishment: existing Phase 3 data (including 3-year safety data from age 6) supports use in children with HeFH; confirm SAHPRA paediatric indication status and align with South African paediatric lipid guidelines
- **Confirm EML listing and formulary inclusion** for familial hypercholesterolaemia as a specific indication in both public sector (Standard Treatment Guidelines) and private formularies

---

**Additional TxGNN Predictions — Summary**

| Rank | Disease | Evidence Level | Recommendation |
|------|---------|---------------|----------------|
| 1 | Familial Hypercholesterolaemia | L1 | **Proceed with Guardrails** ← *primary report* |
| 2 | HIV Infectious Disease (cardiovascular comorbidity) | L2 | Research Question |
| 3 | Brain Stem Infarction | L3 | Research Question |
| 4 | Cholesterol-Ester Transfer Protein Deficiency | L4 | Hold |
| 5 | Hypercholesterolaemia due to CYP7A1 Deficiency | L5 | Hold |
| 6 | Neurodevelopmental Disorder with Ataxic Gait | L5 | Hold |

The HIV infectious disease prediction (Rank 2) is of particular relevance in the South African context: atorvastatin has demonstrated immunomodulatory and cardioprotective benefits in people living with HIV on ART, including reductions in T-cell activation and subclinical atherosclerosis progression. A dedicated evaluation report for this indication is recommended.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. Healthcare professionals should exercise independent clinical judgement and refer to current SAHPRA-approved prescribing information. All adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

