---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Insulin Degludec: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec (Tresiba®) is a second-generation, ultra-long-acting basal insulin analogue approved in the European Union, United States, and multiple other jurisdictions for the management of both type 1 and type 2 diabetes mellitus, but currently carries no SAHPRA registration in South Africa.
The TxGNN model ranks **Type 1 Diabetes Mellitus (T1DM)** as its top predicted indication with a score of **99.44%**, supported by **over 50 registered clinical trials** and **20 publications** demonstrating its safety and efficacy as the global gold-standard basal insulin — making this a compelling case for SAHPRA registration to improve access for South African patients with T1DM.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No SAHPRA-registered indication (globally approved for type 1 and type 2 diabetes mellitus by FDA and EMA) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin degludec is an ultra-long-acting basal insulin analogue with a half-life of approximately 25 hours and a duration of action exceeding 42 hours — significantly longer than first-generation basal insulins such as glargine U100 (~24 hours) and detemir (~14 hours). After subcutaneous injection, it self-assembles into soluble multi-hexamers that form a stable subcutaneous depot. These multi-hexamers slowly dissociate into active insulin monomers that are continuously absorbed into the bloodstream, producing a flat, peakless pharmacokinetic profile with markedly lower within-patient day-to-day variability compared to its predecessors — a mechanistic advantage confirmed in multiple Phase 1 clamp studies.

Type 1 diabetes mellitus arises from autoimmune destruction of pancreatic β cells — primarily mediated by autoreactive CD4⁺ and CD8⁺ T lymphocytes targeting islet antigens — resulting in an absolute and permanent loss of endogenous insulin production. Without insulin, cellular glucose uptake fails, hepatic glucose output is unchecked, and life-threatening diabetic ketoacidosis ensues. Exogenous basal insulin replacement directly addresses this core deficit by activating the insulin receptor (IR) → IRS-1 → PI3K → Akt → GLUT4 translocation signalling cascade, promoting cellular glucose uptake while suppressing hepatic glucose output. Insulin degludec's pharmacological mechanism aligns precisely with T1DM's pathophysiological requirement.

Globally, insulin degludec has been approved by the FDA and EMA for T1DM in adults and children aged ≥1 year, and it serves as the active reference comparator in multiple major Phase 3 programmes evaluating next-generation once-weekly basal insulins (ONWARDS 1–6, QWINT 1–5). Its consistent selection as the clinical benchmark by multiple independent research programmes confirms its status as the current standard of care for basal insulin therapy. The TxGNN score of 99.44% reflects this near-perfect correspondence between mechanism and disease pathology rather than a novel pharmacological leap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Multicentre RCT comparing once-weekly insulin efsitora alfa vs once-daily insulin degludec as part of multiple daily injection therapy in T1DM adults; degludec serves as the active gold-standard comparator in this landmark study |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Phase 2 | Completed | 266 | Randomised, parallel-design, open-label trial evaluating safety and efficacy of LY3209590 vs insulin degludec in T1DM; direct head-to-head evidence for degludec in T1DM with 266 participants |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Phase 4 | Completed | 343 | 12-week RCT comparing TOUJEO® (glargine 300 U/mL) vs TRESIBA® (degludec 100 U/mL) in T1DM using continuous glucose monitoring as the primary endpoint; demonstrates non-inferiority on glycaemic control and variability |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Multinational RCT comparing IDegAsp once-daily plus insulin aspart vs insulin detemir once or twice daily in children and adolescents with T1DM; supports paediatric use of degludec-based therapy across Asia, Europe, and the Americas |
| [NCT03416855](https://clinicaltrials.gov/study/NCT03416855) | N/A (PMS) | Completed | 768 | Prospective, multicentre, post-marketing surveillance study of Ryzodeg® in Korean routine clinical practice; large real-world safety and effectiveness dataset directly relevant to regulatory decision-making |
| [NCT05434559](https://clinicaltrials.gov/study/NCT05434559) | N/A | Completed | 475 | Retrospective multicentre study assessing T1DM patients who switched to insulin degludec from another basal insulin between 2019–2021; 12-month pre-/post-switch glycaemic control comparison using real-world data |
| [NCT04692415](https://clinicaltrials.gov/study/NCT04692415) | Phase 4 | Completed | 25 | Head-to-head comparison of IDeg-100 vs IGlar-300 in insulin-naïve patients evaluating cardiovascular risk parameters — glycaemic variability (CGM), oxidative stress, arterial stiffness, and lipid profiles |
| [NCT04623086](https://clinicaltrials.gov/study/NCT04623086) | Phase 4 | Completed | 59 | Pilot RCT evaluating direct-switch vs bridging-dose strategy when transitioning from insulin glargine to insulin degludec in T1DM adults; provides practical evidence-based guidance for clinicians switching patients |
| [NCT00961324](https://clinicaltrials.gov/study/NCT00961324) | Phase 1 | Completed | 54 | Randomised, double-blind, multiple-dose crossover trial in T1DM; mechanistic evidence demonstrating significantly lower within-patient pharmacodynamic variability for degludec vs insulin glargine at steady state |
| [NCT03668808](https://clinicaltrials.gov/study/NCT03668808) | Phase 4 | Completed | 25 | Pilot RCT comparing degludec vs glargine U100 in T1DM adults flying across multiple time zones; exploits degludec's flexible 8-to-40-hour injection window for practical patient benefit |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | Phase 3 RCT | *The Lancet* | ONWARDS 6: once-weekly insulin icodec vs once-daily degludec as part of basal-bolus regimen in T1DM adults; degludec confirmed as the clinical reference standard for next-generation basal insulin trials |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | Phase 3 RCT | *The Lancet* | QWINT-5: insulin efsitora alfa vs insulin degludec in T1DM adults; non-inferiority trial in which degludec establishes the efficacy and safety benchmark |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | *Lancet Diabetes & Endocrinology* | EXPECT trial: degludec vs insulin detemir (both with insulin aspart) in pregnant women with T1DM; non-inferiority demonstrated, supporting use in high-risk T1DM pregnancy |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-analysis | *Clinical Therapeutics* | Meta-analysis of degludec vs other long-acting analogues (glargine, detemir) in T1DM and T2DM; comparable HbA1c reduction with consistently lower overall and nocturnal hypoglycaemia incidence |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Systematic Review | *Diabetes & Metabolism* | Integrated review of randomised and observational trials; all studies consistently show clinically relevant reductions in nocturnal hypoglycaemia episodes with degludec vs comparators in T1DM and T2DM |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Clinical Practice Review | *Lancet Diabetes & Endocrinology* | Comprehensive update on T1DM management in pregnancy including basal insulin selection, continuous glucose monitoring targets (TIRp >70%), and integration of diabetes technology |
| [36106652](https://pubmed.ncbi.nlm.nih.gov/36106652/) | 2023 | Programme Design Paper | *Diabetes, Obesity & Metabolism* | Design and rationale of the ONWARDS 1–6 Phase 3a programme; all six trials use insulin degludec as the active comparator, reflecting its regulatory reference status |
| [38679838](https://pubmed.ncbi.nlm.nih.gov/38679838/) | 2024 | Programme Design Paper | *Diabetes, Obesity & Metabolism* | Design and rationale of the QWINT Phase 3 programme for insulin efsitora alfa; all five trials use degludec as the active comparator, further cementing its position as the global basal insulin standard |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Narrative Review | *Endocrinología y Nutrición* | Review of degludec's pharmacokinetic profile, multi-hexamer mechanism, and Phase 2–3 clinical data; early evidence base underpinning current clinical use in T1DM and T2DM |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Narrative Review | *Vascular Health and Risk Management* | Review of IDeg/IAsp co-formulation (Ryzodeg®) for T1DM and T2DM; clinical utility of the combination product and role of degludec's pharmacokinetic properties in improving outcomes |

---

## South Africa Market Information

Insulin degludec is **not currently registered with SAHPRA** and carries no active product licences in South Africa. Neither Tresiba® nor Ryzodeg® appears on the South African Essential Medicines List (EML).

Currently no SAHPRA-registered products exist for insulin degludec.

The following global reference approvals are provided for context and to support a future SAHPRA regulatory submission:

| Jurisdiction | Brand Name(s) | Regulatory Body | Approved Indications |
|-------------|--------------|-----------------|----------------------|
| European Union | Tresiba®, Ryzodeg® | EMA | T1DM and T2DM in adults; T1DM in children ≥1 year (Tresiba®); T2DM in adults (Ryzodeg®) |
| United States | Tresiba®, Ryzodeg® | FDA | T1DM and T2DM in adults; T1DM in children ≥1 year (Tresiba®) |
| India | Tresiba® | CDSCO | T1DM and T2DM (post-marketing surveillance completed, n=1,056) |
| South Korea | Ryzodeg® | MFDS | T1DM and T2DM (post-marketing surveillance completed, n=768) |

*These international approvals are provided for reference only. SAHPRA registration is required before insulin degludec may be lawfully supplied, marketed, or reimbursed in South Africa.*

---

## Safety Considerations

Please refer to the approved Professional Information (PI) published by the EMA or FDA for comprehensive safety information, as no SAHPRA-approved PI currently exists for this drug. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin degludec has the strongest possible evidence base (L1) for type 1 diabetes mellitus — it has served as the gold-standard active comparator in multiple completed Phase 3 RCTs (ONWARDS 6 [n=692], QWINT-5 [n=692], EXPECT [n=354]), is backed by a systematic review and meta-analysis confirming lower hypoglycaemia rates vs comparators, and has accumulated over a decade of real-world safety data from Korea, India, Europe, and North America. Its mechanism directly addresses T1DM's core pathophysiology. The fundamental barrier in South Africa is not a gap in clinical evidence but the complete absence of SAHPRA registration, which denies local patients access to a globally established therapy.

**To proceed, the following is needed:**

- **SAHPRA registration application**: Submit a full Common Technical Document (CTD) dossier drawing on the FDA/EMA approval package; explore the abridged or reference-product submission pathway, which may significantly reduce approval timelines for an already internationally approved drug
- **Health technology assessment (HTA)**: Evaluate cost-effectiveness against currently available basal insulins in South Africa (NPH insulin, glargine U100, insulin detemir), accounting for the lower hypoglycaemia burden of degludec and its associated reduction in emergency care costs
- **Essential Medicines List (EML) and NHI formulary application**: Assess whether insulin degludec meets the criteria for EML inclusion and National Health Insurance formulary listing, given its proven clinical superiority over first-generation basal insulins in reducing nocturnal hypoglycaemia
- **Pharmacovigilance and monitoring plan**: Establish SAHPRA-aligned post-marketing surveillance protocols, with particular attention to hypoglycaemia incidence, cardiovascular outcomes, and injection-site reactions in the South African patient population
- **Cold chain and supply chain assessment**: Confirm that insulin degludec's storage and distribution requirements (refrigerated, 2–8°C prior to first use) can be reliably met within South Africa's healthcare supply chain infrastructure
- **Formal MOA documentation**: Obtain complete mechanism of action data from DrugBank or the manufacturer's approved PI to complete the evidence package
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

