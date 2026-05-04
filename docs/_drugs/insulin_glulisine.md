---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Rapid-Acting Insulin Analogue to Type 1 Diabetes Mellitus

---

## One-Sentence Summary

Insulin Glulisine (Apidra®) is a rapid-acting human insulin analogue developed to replace physiological mealtime insulin secretion in patients with diabetes mellitus — a drug with extensive global regulatory approvals (FDA, EMA, PMDA) that is currently **not registered with SAHPRA**.
The TxGNN model predicts it to be effective for **Type 1 Diabetes Mellitus (T1DM)**, the autoimmune condition causing absolute beta-cell loss and lifelong insulin dependence, with **multiple completed Phase 3 RCTs** and **19 publications** supporting this direction.
This evaluation is relevant for clinicians and regulators assessing a potential Section 21 authorisation or formal SAHPRA registration pathway.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in South Africa (no SAHPRA licence on record); globally approved for glycaemic control in diabetes mellitus (adults, adolescents, and children ≥6 years) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 (multiple completed Phase 3 RCTs) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin Glulisine is a recombinant human insulin analogue with two amino acid substitutions relative to regular human insulin: Asparagine at position B3 is replaced by Lysine, and Lysine at position B29 is replaced by Glutamic Acid. These changes reduce hexamer formation and slow self-aggregation in the subcutaneous depot, producing a markedly faster pharmacokinetic profile — onset within 5–15 minutes, peak activity at 55–65 minutes, and a duration of 3–4 hours. It acts principally by binding the insulin receptor (INSR), driving glucose uptake into skeletal muscle and adipose tissue and suppressing hepatic glycogenolysis and gluconeogenesis.

In Type 1 Diabetes Mellitus, autoimmune destruction of pancreatic beta cells leads to absolute endogenous insulin deficiency. External insulin replacement is the only life-sustaining intervention; no oral alternative exists. Insulin Glulisine's rapid-onset, short-duration profile directly mimics the physiological prandial insulin spike that beta cells can no longer generate, making it mechanistically ideal for basal-bolus regimens and continuous subcutaneous insulin infusion (CSII) in T1DM. This is not a speculative repurposing — it is a well-validated pharmacological application that has been formalised in FDA (2004), EMA, and PMDA approvals globally.

The TxGNN prediction score of 99.55% reflects a robust knowledge-graph connection between the insulin receptor signalling pathway, T1DM pathophysiology, and the downstream metabolic targets of glulisine. The primary issue for South African healthcare is not clinical evidence but regulatory access: the absence of SAHPRA registration means that South African patients and clinicians currently cannot access this rapid-acting insulin analogue through standard channels, despite a mature international evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02688933](https://clinicaltrials.gov/study/NCT02688933) | Phase 4 | Completed | 638 | Randomised, active-controlled, parallel-group RCT in T1DM adults comparing morning Toujeo (glargine U300) vs Lantus with insulin glulisine as the prandial component; evaluated CGM-based glycaemic control, nocturnal hypoglycaemia rates, and end-of-dose glucose coverage |
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | Completed | 100 | Apidra (glulisine) + Lantus (glargine) basal-bolus regimen in Russian children and adolescents with T1DM (ages 6–17); primary endpoint HbA1c <8% at 12 months for ages 6–12 and HbA1c <7.5% for ages 13–17; directly evaluates glulisine in the paediatric T1DM population |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | Open-label randomised parallel-group non-inferiority study; insulin glulisine (HMR1964) vs insulin lispro in T1DM adults over 28 weeks; evaluated HbA1c change from baseline and comparative safety |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | Multicentre open-label Phase 3 study of subcutaneous glulisine + glargine in T1DM over 26 weeks; assessed HbA1c reduction from baseline, blood glucose parameters, hypoglycaemia incidence, and adverse events |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: 26-week open-label RCT (with 26-week extension) comparing inhaled Afrezza vs rapid-acting insulin analogues including glulisine plus a basal insulin in paediatric T1DM and T2DM; provides comparative prandial efficacy and safety data for glulisine in children |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | Multinational, multicentre, controlled, open, 1:1 randomised parallel trial comparing the safety of insulin glulisine (HMR1964) vs insulin aspart in CSII in T1DM over 12 weeks; assessed catheter occlusions, glycated haemoglobin, hypoglycaemia, and unexplained hyperglycaemia |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Multicentre open non-randomised Phase 4 study evaluating efficacy and safety of insulin glulisine in T1DM patients also using insulin glargine; assessed patient satisfaction, insulin doses, and clinical outcomes over 12 months |
| [NCT04124302](https://clinicaltrials.gov/study/NCT04124302) | Phase 4 | Completed | 76 | Randomised study comparing two insulin dose-calculation strategies on postprandial glycaemia after a mixed meal in T1DM children; evaluates optimal rapid-acting insulin dosing in a real-world paediatric setting |
| [NCT00489190](https://clinicaltrials.gov/study/NCT00489190) | Phase 4 | Completed | 45 | Open non-randomised observational data collection study for subcutaneous Apidra (glulisine) in T1DM patients over 12 weeks; provides real-world safety and tolerability data outside a controlled trial setting |
| [NCT02910518](https://clinicaltrials.gov/study/NCT02910518) | Phase 1 | Completed | 44 | Randomised, double-blind, single-dose, 2-way crossover bioequivalence study comparing insulin glulisine U300 vs Apidra U100 using euglycaemic clamp technique in T1DM; confirmed PK/PD equivalence across formulation concentrations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | RCT (Head-to-Head) | Acta Diabetologica | Registry-based comparison of glulisine vs lispro and aspart in T1DM patients on CSII; describes HbA1c effectiveness, fasting glucose, and rates of hyperglycaemia, hypoglycaemia, and diabetic ketoacidosis across analogue types |
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | Phase 3 RCT | Hormone and Metabolic Research | Multinational open-label RCT (n=683) comparing glulisine vs insulin lispro in T1DM adults; demonstrated non-inferiority in HbA1c reduction with comparable hypoglycaemia rates and adverse event profile |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic Review | Drugs of Today | Systematic review of insulin analogues for T1DM in children and adolescents; evaluates glulisine alongside lispro and aspart, comparing pharmacokinetic advantages over conventional insulin preparations |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | Comparative RCT | Diabetes Technology & Therapeutics | 26-week basal-bolus trial in paediatric T1DM; insulin glulisine vs lispro showed comparable HbA1c reduction, hypoglycaemia incidence, and safety in children and adolescents |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Comprehensive Review | Drugs | Comprehensive review of glulisine clinical pharmacology, efficacy, and safety across T1DM and T2DM populations; summarises Phase 3 data and establishes non-inferiority vs insulin lispro and regular human insulin |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | PK/PD Study | Clinical Pharmacokinetics | Detailed PK/PD characterisation of glulisine; confirmed faster absorption and shorter duration than regular human insulin, with stable pharmacological behaviour across multiple patient subgroups |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Prospective Clinical Study | Pediatrics International | Prospective 1-year evaluation of glulisine CSII in 20 T1DM children; demonstrated statistically significant improvements in post-breakfast and post-dinner blood glucose levels |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD RCT (Paediatric) | Diabetes Care | PK/PD comparison of glulisine vs regular human insulin administered pre-meal in paediatric T1DM; glulisine showed earlier onset and superior postprandial glucose control in children |
| [17703632](https://pubmed.ncbi.nlm.nih.gov/17703632/) | 2007 | Clinical Review | Vascular Health and Risk Management | Review of insulin combinations targeting normoglycaemia in T1DM and T2DM; focuses on glulisine's role in overcoming pharmacokinetic limitations of conventional insulin in basal-bolus therapy |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Drug Review | Drugs | Comprehensive drug review summarising large Phase 3 RCT evidence for glulisine in T1DM and T2DM; confirms rapid action, prandial glucose control, and non-inferiority vs regular human insulin across patient types |

---

## South Africa Market Information

Insulin Glulisine (Apidra®) currently has **no SAHPRA product registrations** on record and is not marketed in South Africa.

| Item | Detail |
|------|--------|
| SAHPRA Registration Status | Not registered |
| Number of Active Licences | 0 |
| Market Availability | Not marketed |
| Essential Medicines List (EML) | Not listed |

> **Regulatory note:** Insulin Glulisine holds full marketing authorisation from the US FDA (approved 2004 as Apidra®), the European Medicines Agency (EMA), and Japan's PMDA for use in adults, adolescents, and children ≥6 years with diabetes mellitus. In South Africa, access pending formal registration would require a **Section 21 (unregistered medicines) authorisation** from SAHPRA on a compassionate or clinical-need basis. Healthcare professionals should be aware that use under Section 21 requires documented clinical justification and annual renewal.

---

## Safety Considerations

As no SAHPRA-approved Professional Information (PI) exists for insulin glulisine, clinicians should consult the FDA-approved Prescribing Information or the EMA Summary of Product Characteristics (SmPC) for Apidra® (Sanofi). Report any adverse drug reactions to SAHPRA.

> **Key class-effect safety consideration for insulin therapy:**
> The primary risk of rapid-acting insulin analogues is **hypoglycaemia**, including severe and nocturnal episodes. Risk is highest at mealtimes, during physical activity, and when food intake is reduced or delayed. All patients and carers must receive education on recognition, prevention, and emergency management of hypoglycaemia. Dose individualisation based on carbohydrate intake, activity level, and renal function is essential — particularly in children and elderly patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin Glulisine is a globally well-established rapid-acting insulin analogue with an extensive body of Phase 3 and Phase 4 RCT evidence supporting its safety and efficacy in Type 1 Diabetes Mellitus across adult and paediatric populations. Its absence from the South African market represents a regulatory access gap rather than a clinical evidence gap. The risk-benefit profile is well-characterised and the drug meets L1 evidence criteria.

**To proceed, the following is needed:**
- **SAHPRA registration application** for Apidra® (insulin glulisine) — a formal dossier submission aligned with the South African medicines registration process, utilising the existing FDA/EMA-approved data package
- **Section 21 authorisation** as an interim access mechanism for patients with urgent clinical need while formal registration is pursued
- **Pharmacovigilance plan** for local adverse drug reaction monitoring and SAHPRA reporting, including a hypoglycaemia surveillance protocol
- **Cold-chain and storage logistics assessment** to ensure consistent insulin stability across South African distribution conditions (temperature-controlled supply chain from manufacturer to patient)
- **SAHPRA-approved Professional Information (PI)** adapted to South African clinical practice, including local dosing guidance for the basal-bolus and CSII contexts
- **Essential Medicines List (EML) submission** to support equitable access, particularly in the public sector where T1DM patients depend on state-supplied insulin products
- **Paediatric access pathway assessment**, given that T1DM disproportionately affects children and adolescents, and trial data support use from age 6 years

---

*This report is generated for research and regulatory decision-support purposes only. It does not constitute medical advice or a recommendation for individual patient treatment. Drug repurposing and market entry candidates require validation through appropriate regulatory and clinical pathways before clinical application. All adverse drug reactions should be reported to SAHPRA.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

