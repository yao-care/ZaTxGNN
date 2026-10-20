---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Fenofibrate: predicted new indication Homozygous familial hypercholesterolaemia (evidence level L5). Approved use: Hypertriglyceridaemia and hyperlipidaemia (including familial combine…"
monitor_inn: "FENOFIBRATE"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "hypercholesterolemia, autosomal dominant"]
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fenofibrate: From Hypertriglyceridaemia to Homozygous Familial Hypercholesterolaemia

## One-Sentence Summary

Fenofibrate is an oral lipid-lowering drug, originally used for hypertriglyceridaemia and mixed hyperlipidaemia.
The TxGNN model predicts it may be useful for **homozygous familial hypercholesterolaemia (HoFH)**, but this rests mostly on the model score. The only registered trial for this condition tests a different drug (alirocumab), and the supporting literature is **10 publications**, mainly reviews, guidelines and one small 1984 cohort study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridaemia and hyperlipidaemia (including familial combined hyperlipidaemia and low HDL-C), based on the knowledge-graph indication links; the registered product's indication text is not available in the data compiled for this report |
| Predicted New Indication | Homozygous familial hypercholesterolaemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (no fenofibrate trial in HoFH; evidence is mechanistic and indirect) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fenofibrate is generally described as a PPAR-alpha agonist. It lowers triglycerides and raises HDL-C, with a modest and variable effect on LDL-C.

The link to HoFH is weak. In HoFH the LDL receptor is severely impaired, so a drug acting mainly through PPAR-alpha is unlikely to give meaningful LDL-C lowering. The most that can reasonably be proposed is a role as an add-on when HoFH is accompanied by raised triglycerides.

A small 1984 study in type II hyperlipoproteinaemia included one patient with HoFH who showed the greatest fall in total and LDL cholesterol. This is an anecdotal signal and not enough to support the indication. The model prediction therefore has little clinical corroboration at present.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of **alirocumab** (not fenofibrate) on LDL-C in children and adolescents aged 8–17 with HoFH. It gives no direct evidence for fenofibrate. |

No fenofibrate trial in HoFH is registered. No SANCTR or PACTR trials were identified.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 patients with type II hyperlipoproteinaemia on fenofibrate 300 mg/day. LDL-C fell about 24%, and the one HoFH patient had the largest fall. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid-lowering drugs. Fenofibrate monotherapy is mainly indicated for fasting triglycerides above 500 mg/dl, to reduce pancreatitis risk. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guideline on dyslipidaemia management and cardiovascular prevention. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Treatment of dyslipidaemic children; fenofibrate is among the agents reported to reduce lipids in familial hypercholesterolaemia. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK study | Pharmacotherapy | Lomitapide (approved for HoFH) pharmacokinetic interactions, including with fenofibrate. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | Dyslipidaemia management in pregnancy. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL-C lowering with statins and PCSK9 inhibitors. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe pharmacology; general context only. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin in hyperlipidaemias; general context only. |
| [9627539](https://pubmed.ncbi.nlm.nih.gov/9627539/) | 1998 | Review | Can J Cardiol | Drug treatment of dyslipidaemia with a focus on atorvastatin; general context only. |

No randomised controlled trials of fenofibrate in HoFH were identified.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 52/7.5/0769 | Pravafen 40/160 mg | Capsule (oral) | Not available in the data compiled for this report |

Pravafen is a pravastatin/fenofibrate 40/160 mg fixed-dose product. Essential Medicines List status could not be confirmed from the data compiled.

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available in the data compiled for this report. The following comes from a drug-disease knowledge graph, not from label text.

- **Contraindication-related conditions (knowledge graph):** liver failure and liver disease, pancreatitis, gallbladder disease and gallstones, muscle disorders including myopathy and rhabdomyolysis, impaired renal function, and haematological conditions such as thrombocytopenia, anaemia, leukopenia, agranulocytosis and neutropenia.
- **Drug Interactions:** 100 interactions were found. The 20 shown in the compiled data are all moderate. They involve:
  - sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide) and many insulin preparations, where glucose monitoring is advisable
  - chenodeoxycholic acid
  - esomeprazole

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only registered HoFH trial tests alirocumab, not fenofibrate, and the fenofibrate-specific literature is a single small 1984 study that included one HoFH patient. In HoFH the LDL receptor is severely impaired, so fenofibrate is unlikely to lower LDL-C meaningfully. At most it may help as an add-on for associated hypertriglyceridaemia.

**To proceed, the following is needed:**
- Clinical data, ideally a controlled study, of fenofibrate in HoFH, with LDL-C and triglycerides as outcomes
- Clarification of the intended role, for example as an add-on to established HoFH therapies for raised triglycerides
- Detailed mechanism of action data and the SAHPRA Professional Information (warnings, contraindications and approved indication text)
- A review of drug interactions and monitoring (liver, renal, muscle, blood counts) for the intended patient group
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

