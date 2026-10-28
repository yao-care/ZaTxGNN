---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 408
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "ROSUVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
description: "Rosuvastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Rosuvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Rosuvastatin: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Rosuvastatin is a statin used to lower cholesterol in hyperlipidaemia, familial hypercholesterolaemia and atherosclerotic disease.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but there are **no clinical trials and no publications** for this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 5 of 5) |
| Number of SAHPRA Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available in the data compiled for this report. Rosuvastatin is a statin (HMG-CoA reductase inhibitor). It lowers LDL-cholesterol by reducing hepatic cholesterol synthesis and increasing LDL clearance, and this is established in its existing lipid indications.

CETP deficiency raises HDL-cholesterol and lowers LDL-cholesterol, so it sits in the same lipid pathway. That is why the model links the two conditions.

However, CETP deficiency is usually a benign or even favourable lipid phenotype. No clinical rationale for treating it with a statin has been established. The prediction is a plausible pathway association, not a recognised treatment need.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Reviewed

The data compiled for this report include other predictions with far more evidence than the top-ranked one. They are summarised here for context.

| Predicted Indication | Evidence Level | Assessment |
|------|------|------|
| Familial hypercholesterolaemia | L1 | Several completed Phase 3 trials, including paediatric heterozygous and homozygous FH (e.g. [NCT00355615](https://clinicaltrials.gov/study/NCT00355615), [NCT01078675](https://clinicaltrials.gov/study/NCT01078675), [NCT02226198](https://clinicaltrials.gov/study/NCT02226198)). This overlaps with existing labelled use and confirms an established indication rather than a new one. Proceed with Guardrails. |
| Hyperlipidaemia | L1 | Large Phase 3 programme, including [NCT00653744](https://clinicaltrials.gov/study/NCT00653744) (n=1,700) and the STELLAR RCT ([PMID 12860216](https://pubmed.ncbi.nlm.nih.gov/12860216/)). This is also an established use. Proceed with Guardrails. |
| HIV infectious disease | L2 | The use is cardiometabolic and inflammation risk reduction, not antiviral. One placebo-controlled Phase 2 trial ([NCT01218802](https://clinicaltrials.gov/study/NCT01218802)) exists. Results are mixed: a 2024 report found no benefit on arterial stiffness ([PMID 39088828](https://pubmed.ncbi.nlm.nih.gov/39088828/)) and a 2015 RCT found worsened insulin resistance ([PMID 26157049](https://pubmed.ncbi.nlm.nih.gov/26157049/)). Protease-inhibitor interactions are a key concern. This is a research question. |
| Brain stem infarction, hypoalphalipoproteinaemia, hypercholesterolaemia due to CYP7A1 deficiency | L5 | Only indirect or preclinical evidence. Hold. |
| Hepatic lipase deficiency, ABri amyloidosis, a rare neurodevelopmental disorder | L5 | Prediction only. Hold. |

## South Africa Market Information

Rosuvastatin is marketed in South Africa. All five SAHPRA registrations are valid single-ingredient products, and none are cancelled. Approved indication text was not available for these registrations.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 46/7.5/0222 | Rostor | Tablet |
| Reg. No. 47/7.5/0900 | Rosuvastatin 5 Pharmc | Film-coated tablet |
| Reg. No. 55/7.5/0563 | Lypovas 5 | Tablet |
| Reg. No. 55/7.5/0779 | Lypstaplus 10 Mg/10 Mg | Tablet |
| Reg. No. 54/7.5/0693 | Reguchole 10/5Mg | Tablet |

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the SAHPRA-approved Professional Information (PI) for these. Report adverse drug reactions to SAHPRA.

- **Contraindication associations (knowledge graph, not label text):** liver disease, gallbladder disease, hypothyroidism and myxoedema, myopathy and other muscle disease, rhabdomyolysis, familial periodic paralysis, substance abuse/dependence, proteinuria, and injury. These should be checked against the PI.
- **Drug interactions:** 100 interactions were identified, and the first 20 were available for review.
  - **Major:** fenofibrate and atazanavir.
  - **Moderate:** atorvastatin, ezetimibe, bempedoic acid, amiodarone, paclitaxel, zidovudine, adalimumab, alpelisib, apalutamide, ethanol and others.
  - **Minor:** hormonal contraceptives (levonorgestrel, norethisterone, desogestrel).
  - Pharmacokinetic studies also show that HIV protease inhibitors raise rosuvastatin exposure.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (CETP deficiency) rests on a model score alone, with no trials or publications. CETP deficiency is typically not a condition that needs lipid-lowering treatment. Rosuvastatin's strongest evidence lies in indications it already covers, such as familial hypercholesterolaemia and hyperlipidaemia.

**To proceed, the following is needed:**
- A clinical rationale showing that treating CETP deficiency with a statin offers patient benefit
- Case series, registry data or mechanistic studies in CETP-deficient patients
- Detailed mechanism of action data
- SAHPRA Professional Information (warnings, contraindications and approved indications) for safety review
- If the HIV cardiometabolic use is pursued as a research question, a protease-inhibitor interaction management plan and consideration of the insulin-resistance signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

