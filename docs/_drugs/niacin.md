---
layout: default
title: Niacin
parent: Model Prediction Only (L5)
nav_order: 340
evidence_level: L5
indication_count: 1
---

# Niacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Niacin: From Hyperlipidaemia to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Niacin (vitamin B3) is originally used to treat hyperlipidaemia, including familial forms, and vitamin deficiency disorders.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolaemia (HoFH)**,
but currently there are **0 registered clinical trials** and **17 publications** (mostly general reviews on lipid management, not niacin-specific trials) linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia, hyperlipidaemia, familial hyperlipidaemia, vitamin deficiency disorder (the SAHPRA registration record contains no approved indication text) |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only, no direct clinical studies of niacin in HoFH) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, niacin lowers LDL-cholesterol, VLDL and triglycerides and raises HDL-cholesterol. This is thought to occur by inhibiting hepatic diacylglycerol acyltransferase-2, which reduces hepatic VLDL/apoB secretion, and by suppressing adipose tissue lipolysis through the GPR109A receptor.

HoFH is an extreme form of familial hyperlipidaemia, which is already within niacin's original indication family. The prediction is therefore a close extension within the same disease family, not a new mechanism. However, HoFH is characterised by absent or severely impaired LDL receptor function, and niacin's effect does not depend on LDL receptor upregulation. Its LDL-lowering effect in HoFH is therefore expected to be modest and, at best, adjunctive to established therapies.

The very high TxGNN score most likely reflects network proximity to the existing hyperlipidaemia and familial hyperlipidaemia indications. It should not be read as independent clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications retrieved are mostly general reviews of familial hypercholesterolaemia management. None is a niacin-specific trial in HoFH. Several concern other agents (atorvastatin, ezetimibe, lomitapide) and are included only as context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26376908](https://pubmed.ncbi.nlm.nih.gov/26376908/) | 2015 | Scientific statement/Review | Arterioscler Thromb Vasc Biol | Reviews non-statin LDL-lowering therapies; notes placebo-controlled trials showed niacin as monotherapy reduced CVD end points |
| [24506448](https://pubmed.ncbi.nlm.nih.gov/24506448/) | 2014 | Review | Expert Rev Cardiovasc Ther | Critical review of non-statin options (fibrates, ezetimibe, bile acid sequestrants, n-3 fatty acids, niacin) for residual risk and statin intolerance |
| [23959229](https://pubmed.ncbi.nlm.nih.gov/23959229/) | 2013 | Review | Nat Rev Cardiol | Lipid-modifying agents beyond statins for severe hypercholesterolaemia or mixed dyslipidaemia |
| [26370207](https://pubmed.ncbi.nlm.nih.gov/26370207/) | 2015 | Review | Drugs | Challenges in diagnosing and treating HoFH |
| [27797643](https://pubmed.ncbi.nlm.nih.gov/27797643/) | 2016 | Review | Metab Syndr Relat Disord | Modern management of familial hypercholesterolaemia (HoFH and HeFH) |
| [25257073](https://pubmed.ncbi.nlm.nih.gov/25257073/) | 2014 | Review | Atheroscler Suppl | Current achievements and unmet needs in HoFH, including apheresis and lipid-lowering drugs |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Review | Medicina (Kaunas) | Literature analysis of familial hypercholesterolaemia diagnostics and treatment |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Lomitapide (approved for HoFH) pharmacokinetic interactions with several lipid-lowering drugs, including niacin |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | Clinical study | Arteriosclerosis | Drug treatment of familial hypercholesterolaemia in children (30 HeFH, 3 HoFH) |
| [19947811](https://pubmed.ncbi.nlm.nih.gov/19947811/) | 2009 | Case report | Pharmacotherapy | Xanthomas in an 18-year-old with HoFH |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2062 (ACT 101) | Filibon | Capsule (oral) | Not recorded in the data compiled for this report |

Essential Medicines List (EML) inclusion status is not available in the data compiled for this report.

## Safety Considerations

**Drug Interactions**: An interaction screen returned 100 interacting drugs. The entries reviewed are mainly Moderate-level interactions with glucose-lowering agents, which warrants glycaemic monitoring when niacin is combined with them:
- Metformin, acarbose
- Sulphonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide)
- SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
- GLP-1 receptor agonists and related agents (albiglutide, dulaglutide, exenatide) and alogliptin
- Insulins (human, aspart, degludec)

A Minor-level interaction with acetylsalicylic acid was also listed.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring and proximity to niacin's existing lipid indications, with no registered trials and no niacin-specific HoFH studies. Because HoFH involves absent or impaired LDL receptor function, niacin's expected benefit is modest and adjunctive at best. Established HoFH therapies already exist.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications and approved indication), which is currently missing and blocks safety screening
- Confirmed mechanism of action data (for example from DrugBank)
- Direct clinical evidence of niacin in HoFH, such as trials or case series showing LDL-C effect as an add-on to statins, ezetimibe or apheresis
- A review of niacin's place relative to current HoFH therapies, given its limited benefit in cardiovascular outcome trials and its tolerability issues (e.g. flushing)
- Confirmation of EML status and whether the single registered product (Filibon) is a suitable formulation and strength for lipid-lowering use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

