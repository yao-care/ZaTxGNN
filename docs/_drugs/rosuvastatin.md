---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hypercholesterolemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

> Rosuvastatin (DrugBank DB01098) is a globally established HMG-CoA reductase inhibitor (statin) used for hypercholesterolemia and mixed dyslipidemia. The TxGNN model's top-ranked prediction for this drug is **cholesterol-ester transfer protein (CETP) deficiency**, but this direction is currently supported by **0 clinical trials** and only **2 case-report publications that concern different diseases entirely**, and its underlying pathophysiology runs counter to how statins work — the evidence does not currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in local regulatory data (South Africa registration not on file); globally, rosuvastatin is an established treatment for hypercholesterolemia and mixed dyslipidemia |
| Predicted New Indication | Cholesterol-ester transfer protein (CETP) deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this specific product is not available in the evidence pack. Based on established pharmacological knowledge, rosuvastatin is a synthetic HMG-CoA reductase inhibitor that blocks the rate-limiting step of hepatic cholesterol synthesis and up-regulates LDL-receptor expression, lowering LDL-C and triglycerides. This is the mechanistic basis for its proven, globally recognised efficacy in hypercholesterolemia and mixed dyslipidemia.

CETP deficiency, however, is a rare genetic disorder characterised by markedly **elevated HDL-C and low-to-normal LDL-C** — a lipid profile that is essentially the inverse of what statins are designed to correct. There is no established rationale for using an LDL-lowering agent to treat a condition that does not present with LDL excess, and the mechanistic link here is weak.

This is reinforced by the supporting literature itself: the two publications returned are case reports of **Apo A-I deficiency** and **hepatic lipase deficiency** — genetically and clinically distinct lipid disorders — and neither study evaluates rosuvastatin or CETP deficiency directly. This pattern is consistent with a knowledge-graph adjacency artifact (both diseases cluster near "lipid/lipoprotein metabolism" nodes) rather than genuine mechanistic or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case Report | Journal of Clinical Lipidology | Describes complete Apo A-I deficiency in an Iraqi Mandaean family — a distinct genetic disorder, not CETP deficiency; does not evaluate rosuvastatin |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case Report | BMJ Case Reports | Describes hepatic lipase deficiency in a Middle-Eastern-Arabic male, incidentally reporting CETP activity/mass as a lab finding; not a treatment or outcomes study, and does not evaluate rosuvastatin |

---

## South Africa Market Information

No SAHPRA registrations are on file for this product in the evidence pack (0 licenses recorded; market status: Not marketed).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials support this indication, the two available publications concern unrelated lipid disorders and do not evaluate rosuvastatin, and the predicted disease's lipid profile (high HDL/low LDL) is mechanistically inconsistent with a statin's LDL-lowering action. This prediction should be treated as knowledge-graph noise rather than a genuine repurposing lead.

**To proceed, the following is needed:**
- Direct pharmacological or case evidence of rosuvastatin use specifically in CETP-deficient patients, if this hypothesis is to be revisited
- SAHPRA product registration and Professional Information data for rosuvastatin, currently unavailable locally
- Confirmed original mechanism of action (MOA) documentation, currently a data gap

**Note for reviewers:** This evidence pack contains multiple TxGNN predictions for rosuvastatin with substantially stronger evidence bases than the top-ranked candidate above, and may warrant separate evaluation:
- **Familial hypercholesterolemia** (L1, 24 clinical trials incl. multiple Phase 3 RCTs, 13 publications) — recommendation: Proceed with Guardrails. This reflects rosuvastatin's core, already-established statin-class indication rather than a novel repurposing hypothesis.
- **Hyperlipidemia** (L1, 50 clinical trials, 20 publications) — recommendation: Proceed with Guardrails, for the same reason.
- **HIV infectious disease** (L2, 19 clinical trials, 20 publications) — recommendation: Research Question. This is a genuine novel-mechanism hypothesis (anti-inflammatory/immunomodulatory reduction of chronic immune activation and cardiovascular risk in people with HIV), distinct from rosuvastatin's lipid-lowering original use, and may be a more productive repurposing direction than CETP deficiency.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

