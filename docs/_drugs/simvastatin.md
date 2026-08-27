---
layout: default
title: Simvastatin
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 8
---

# Simvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Simvastatin: From Hypercholesterolemia to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is an HMG-CoA reductase inhibitor (statin) originally developed for hypercholesterolemia and cardiovascular risk reduction. The TxGNN model predicts it may be effective for **Familial Hypercholesterolemia (FH)**, with **19 clinical trials** and **18 publications** currently supporting this direction — though this largely reflects an already-established, guideline-endorsed use of statins in FH rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (statin class) — no formal indication text available in this evidence pack |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank MOA lookup flagged as a High-severity data gap). Based on known pharmacology, simvastatin belongs to the statin (HMG-CoA reductase inhibitor) class, its efficacy in hypercholesterolemia/dyslipidemia has been proven, and mechanistically it is directly applicable to familial hypercholesterolemia: by inhibiting hepatic cholesterol synthesis, statins trigger compensatory upregulation of LDL receptors, which is the core therapeutic mechanism used to lower LDL-C in FH patients.

Familial hypercholesterolemia is a genetic disorder of LDL receptor function that causes markedly elevated LDL-C from birth, with high risk of premature coronary artery disease. Statins, including simvastatin, are already first-line or foundational background therapy for both heterozygous and homozygous FH in international treatment guidelines, often used alone or combined with ezetimibe or PCSK9 inhibitors.

Because of this, the TxGNN prediction here should be read as **strong confirmatory evidence of an established use** rather than a novel repurposing hypothesis — the mechanistic link and clinical evidence are robust, but the "new indication" largely overlaps with simvastatin's existing therapeutic role in lipid disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | SUPREME study: niacin ER + simvastatin vs atorvastatin for HDL-C elevation in hyperlipidemia/mixed dyslipidemia |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin efficacy/safety/tolerability in adolescents with heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in Fredrickson Type IIa/IIb dyslipidaemia incl. heterozygous FH |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: ezetimibe + high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term safety/tolerability of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in children/adolescents with homozygous FH; simvastatin as background therapy |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | Completed | 194 | Colesevelam added to stable statin (incl. simvastatin) therapy in pediatric heterozygous FH |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Alirocumab (SAR236553/REGN727) RCT in heterozygous FH not controlled on lipid-modifying therapy |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab RCT in heterozygous FH inadequately controlled on lipid-modifying therapy |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | Completed | 216 | Alirocumab as add-on to stable statin therapy in heterozygous FH / high cardiovascular risk patients |

*Note: SANCTR/PACTR identifiers were not present in the source evidence pack for these trials.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | The New England Journal of Medicine | Ezetimibe + simvastatin vs simvastatin alone; effect on progression of atherosclerosis in FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opinion on Drug Safety | Benefits and risks assessment of simvastatin in familial hypercholesterolaemia |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Benefits and risks of simvastatin in patients with familial hypercholesterolaemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Statins for children with familial hypercholesterolemia |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort | Journal of the American College of Cardiology | Statin-induced reduction of CAD events and mortality in heterozygous FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative Study | Nutrition, Metabolism and Cardiovascular Diseases | Atorvastatin vs simvastatin in heterozygous FH: lipid-lowering efficacy comparison |
| [1346327](https://pubmed.ncbi.nlm.nih.gov/1346327/) | 1992 | Cohort | Lancet | Simvastatin and lipoprotein(a) |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | Journal of Clinical Medicine | Cellular immunity parameters in children with FH treated with simvastatin |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Review | The Pharmacogenomics Journal | Combining FH and statin genetic studies for pharmacogenomics implementation |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline/Review | Circulation | 2026 ACC/AHA dyslipidemia management guideline (replaces 2018 blood cholesterol guideline) |

---

## South Africa Market Information

No SAHPRA registrations are currently on file for simvastatin in this evidence pack (0 licenses), and market status is recorded as **Not marketed**. Given simvastatin is a long-established, widely genericized statin marketed in many jurisdictions globally, this "not marketed" status should be independently verified against the current SAHPRA product register before relying on it for decision-making — it may reflect a data collection gap rather than true absence from the South African market.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and long-standing clinical practice guidelines support simvastatin's efficacy in familial hypercholesterolemia, giving strong (L1) evidence — but this reflects confirmation of an already-recognized statin indication rather than a novel repurposing discovery, and key safety/regulatory data for South Africa remain unverified.

**To proceed, the following is needed:**
- SAHPRA-approved PI warnings, contraindications, and drug interaction data (currently a Blocking data gap)
- Confirmed mechanism of action documentation via DrugBank (currently a High-severity data gap)
- Verification of actual SAHPRA registration/market status, since 0 licenses on file is inconsistent with simvastatin's typical global availability
- A dedicated drug-drug interaction query, since the current DDI lookup returned no results (`not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

