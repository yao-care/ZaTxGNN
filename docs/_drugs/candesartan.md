---
layout: default
title: Candesartan
parent: Model Prediction Only (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Candesartan: predicted new indication Migraine disorder (evidence level L5). Approved use: Hypertension"
---

# Candesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Candesartan: From Hypertension to Migraine Disorder

## One-Sentence Summary

Candesartan is an angiotensin II receptor blocker (ARB) that is marketed in South Africa for cardiovascular use and is used to treat hypertension.
The TxGNN model predicts it may be effective for **migraine disorder** (migraine prevention),
with **4 linked clinical trials** (3 directly on migraine) and **20 publications** currently supporting this direction, including a 2025 randomised, placebo-controlled trial.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (from public pharmacology data; the SAHPRA registrations compiled for this report contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 (with a caveat: the direct randomised evidence includes a Phase 2/3 trial and a Phase 2 trial; see the Conclusion) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data show that candesartan blocks the angiotensin II type 1 (AT1) receptor (gene *AGTR1*) and is used for hypertension, alone or in combination with other agents.

Modulation of the renin-angiotensin system is thought to influence migraine through effects on cerebrovascular tone, neurogenic inflammation, oxidative stress and sympathetic activity. Candesartan is already used off-label for migraine prevention and is discussed in guideline-style reviews. Both hypertension and migraine involve vascular regulation, which supports the plausibility of the prediction.

The other predicted indications are much weaker. "Migraine with brainstem aura" and "migraine with or without aura, susceptibility to" are related migraine terms that inherit evidence from the main migraine indication, with no subtype-specific trials. Pulmonary hypertension has only preclinical support and an unrelated COVID-19 trial. The remaining predictions (Prinzmetal angina, kyphoscoliotic heart disease, atrophoderma vermiculata, ulerythema ophryogenesis, benign prostatic hyperplasia, alopecia) have no supporting trials or relevant literature and are model predictions only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04574713](https://clinicaltrials.gov/study/NCT04574713) | Phase 2 | Completed | 450 | Multicentre, binational, triple-blind, placebo-controlled trial of candesartan 8 mg and 16 mg for episodic migraine prevention |
| [NCT00884663](https://clinicaltrials.gov/study/NCT00884663) | Phase 2/3 | Completed | 72 | Double-blind, double-dummy, triple cross-over comparison of candesartan with propranolol and placebo for migraine prevention; small sample |
| [NCT04138316](https://clinicaltrials.gov/study/NCT04138316) | N/A (observational) | Completed | 85 | CandeSpartan study: response predictors and tolerability in patients who had failed three or more preventive drugs |
| [NCT07655440](https://clinicaltrials.gov/study/NCT07655440) | Phase 4 | Not yet recruiting | 120 | Comparison of migraine preventives and anti-CGRP therapies for tinnitus in people with migraine; only indirectly relevant |

No SANCTR or PACTR identifiers were available in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40975098](https://pubmed.ncbi.nlm.nih.gov/40975098/) | 2025 | RCT (Phase 2, triple-blind) | The Lancet. Neurology | Candesartan versus placebo for prevention of episodic migraine; evaluated safety, tolerability and efficacy |
| [37350141](https://pubmed.ncbi.nlm.nih.gov/37350141/) | 2023 | Systematic review/meta-analysis | Cephalalgia | Effect of blood pressure-lowering medications on episodic migraine prevention |
| [40571531](https://pubmed.ncbi.nlm.nih.gov/40571531/) | 2025 | Scoping review | Clinical Therapeutics | Candesartan, an ARB, has shown potential for migraine management |
| [39899861](https://pubmed.ncbi.nlm.nih.gov/39899861/) | 2025 | Clinical guideline | Annals of Internal Medicine | American College of Physicians guideline on pharmacological prevention of episodic migraine |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review with economic modelling | Health Technology Assessment | Clinical and cost-effectiveness of preventive drugs for chronic migraine |
| [38057728](https://pubmed.ncbi.nlm.nih.gov/38057728/) | 2023 | Systematic review/network meta-analysis | J Headache Pain | Ranking of preventive drugs for chronic migraine in adults |
| [38663908](https://pubmed.ncbi.nlm.nih.gov/38663908/) | 2024 | Observational study | Cephalalgia | CandeSpartan: effectiveness, tolerability and response predictors of candesartan; notes that two randomised trials already support its effectiveness |
| [38307673](https://pubmed.ncbi.nlm.nih.gov/38307673/) | 2024 | Review | Handbook of Clinical Neurology | Lists candesartan among non-specific oral agents for migraine prevention |
| [18759728](https://pubmed.ncbi.nlm.nih.gov/18759728/) | 2008 | Review | Medical Journal of Australia | Evidence for candesartan in migraine prophylaxis described as reasonably good but limited |
| [30600979](https://pubmed.ncbi.nlm.nih.gov/30600979/) | 2019 | Review | American Family Physician | Overview of migraine prophylaxis; preventive therapy reduces frequency, severity and distress |

## South Africa Market Information

Both registrations are valid, single-ingredient or single-kind entries. No approved indication text or manufacturer was available in the data compiled for this report, and Essential Medicines List (EML) status was not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/7.1.3/0472 | Ranepres 8 Mg | Tablet | Not available in the data compiled |
| Reg. No. 48/7.1.3/0514 | Ranepres Plus 16/12.5 Mg | Tablet | Not available in the data compiled |

Migraine prevention is not a registered indication for these products, so any use for this purpose would be off-label.

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only a pharmacology record (candesartan acting at the AT1 receptor). It contains no drug-drug interaction entries.
- **Guardrails from the repurposing assessment**: monitor blood pressure, renal function and potassium, and avoid use in pregnancy because of the fetotoxicity of ARBs. The literature compiled includes case reports of oligohydramnios and pulmonary hypoplasia associated with ARB exposure in pregnancy.

Warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, triple-blind, placebo-controlled randomised trial published in 2025 (PMID 40975098, linked to NCT04574713) and a completed Phase 2/3 trial (NCT00884663) directly address migraine prevention, and candesartan is already used off-label for this purpose. The L1 grade should be read cautiously: NCT04574713 is registered as Phase 2 and NCT00884663 is small (72 participants), so there are not clearly two completed Phase 3 trials. The other predicted indications are not supported at this level (migraine subtypes inherit evidence; pulmonary hypertension and the rest should be held).

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is currently missing and blocks a formal safety screen
- Verification of trial phase and efficacy results against the full publications (PMID 40975098 and NCT04574713)
- Mechanism of action data from DrugBank
- A monitoring plan for blood pressure, renal function and potassium, and a pregnancy-avoidance plan for women of child-bearing potential
- Confirmation of EML status and whether any South African product could be used or labelled for migraine prevention
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

