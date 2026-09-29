---
layout: default
title: Thiamine
parent: Moderate Evidence (L3-L4)
nav_order: 442
evidence_level: L3
indication_count: 10
---

# Thiamine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Thiamine: From Vitamin B1 Supplementation to Hyperthyroidism

## One-Sentence Summary

Thiamine (vitamin B1) is a vitamin used as a supplement and to correct thiamine deficiency, and it is marketed in South Africa in injectable, oral and other forms.
The TxGNN model predicts it may help in **hyperthyroidism** (score 99.44%), but the support is limited to **1 small pilot trial (n=12)** and **20 publications**, mostly case reports and old biochemical studies.
The likely benefit is correcting a secondary thiamine deficiency, not treating the thyroid disease itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA records provided (thiamine is a vitamin B1 supplement used for thiamine deficiency) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thiamine is a vitamin B1 supplement, and its efficacy in correcting thiamine deficiency is well established. Mechanistically, it may be applicable in hyperthyroidism because of the following link.

Thyrotoxicosis is a hypermetabolic state that increases thiamine use and turnover. This can lead to a functional thiamine deficiency, with reduced transketolase activity. In severe cases the deficiency shows up as Wernicke encephalopathy, or as high-output heart failure resembling beriberi. The case reports in the literature mostly describe pregnant women with hyperemesis and thyrotoxicosis who developed Wernicke encephalopathy.

Thiamine here is supportive correction of a secondary deficiency, not an antithyroid treatment. The high TxGNN score probably reflects this deficiency-related association rather than a disease-modifying effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | Not applicable (no phase designation) | Completed | 12 | Pilot study of thiamine supplementation in severe hyperthyroidism. It assessed the prevalence of thiamine deficiency and whether cardiovascular function improved. The endpoint is cardiovascular function, not thyroid disease control. |

No SANCTR or PACTR registrations were identified.

---

## Literature Evidence

No randomised controlled trials were found. The table lists the reviews and case reports first, then the older mechanistic studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9704251](https://pubmed.ncbi.nlm.nih.gov/9704251/) | 1998 | Review | Drug Safety | Review of when nausea and vomiting in pregnancy should be treated and which treatments are safe. Persistent hyperemesis can compromise hydration and nutritional status. |
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case report | Critical Care Nursing Clinics of North America | Thyrotoxicosis and wet beriberi (severe thiamine deficiency) as causes of high-output heart failure. |
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case report | Cureus | Wernicke encephalopathy associated with transient gestational hyperthyroidism and hyperemesis gravidarum. |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case report | Journal of General Internal Medicine | Thyrotoxicosis-associated Wernicke encephalopathy, caused by thiamine deficiency. |
| [32934066](https://pubmed.ncbi.nlm.nih.gov/32934066/) | 2020 | Case report | Clinical Medicine (London) | A pregnant woman with hyperemesis and thyrotoxicosis presented with confusion and ataxia. |
| [36593922](https://pubmed.ncbi.nlm.nih.gov/36593922/) | 2023 | Case report | Radiology Case Reports | Uncommon presentation of Wernicke encephalopathy in a pregnant woman with pre-gestational hyperthyroidism. |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case report | Cureus | Wernicke encephalopathy with hyperthyroidism, after persistent nausea, vomiting and weight loss. |
| [25148818](https://pubmed.ncbi.nlm.nih.gov/25148818/) | 2014 | Case report | Endocrine Practice | Gestational thyrotoxicosis and hyperemesis gravidarum associated with Wernicke encephalopathy. |
| [13305517](https://pubmed.ncbi.nlm.nih.gov/13305517/) | 1955 | Small physiological study | Endocrinologia e scienza della costituzione | Urinary thiamine after an intravenous cocarboxylase load in hyperthyroid and normal subjects. |
| [21064291](https://pubmed.ncbi.nlm.nih.gov/21064291/) | 1946 | Animal study | Federation Proceedings | Effect of thiamine deficiency and thyroid state on ATP content of rat heart muscle. |

---

## South Africa Market Information

Of the 20 registrations, 5 are shown below. The register extract does not list approved indication text or manufacturers. Other registered forms include tablet, infusion, TPN and inhaler.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Y/6.1/415 | Dopamine hcl fresenius 5ml 200mg/5ml | Injection | Not stated |
| H2611 (ACT 101/1965) | Becoplex ido vial 10ml | Injection | Not stated |
| T1012 (ACT 101/1965) | Beespan | Capsule | Not stated |
| H2412 (ACT 101/1965) | A-lennon vitamin b co ampoule 2ml | Injection | Not stated |
| H2975 (ACT 101/1965) | Vitamin b co 10ml | Injection | Not stated |

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is one small, completed pilot trial (n=12) with a cardiovascular endpoint, plus case reports and old biochemical studies. It supports correcting thiamine deficiency in severe thyrotoxicosis, not treating hyperthyroidism. The SAHPRA safety data is also missing, which blocks safety screening.

Of the other predicted indications, only pulmonary hypertension has comparable (L3) evidence. It comes from consistent case series and observational data on thiamine-responsive pulmonary hypertension in infants with thiamine deficiency. It is a deficiency-correction question in a defined subpopulation, not a general pulmonary hypertension indication. The remaining predictions have no supporting clinical evidence.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDF)
- Mechanism of action data (query the DrugBank API)
- Reframing the question as thiamine deficiency screening and supplementation in severe thyrotoxicosis, with thiamine status as a defined endpoint
- A larger controlled study, or a systematic review of thiamine status in thyrotoxicosis, to move beyond L3 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

