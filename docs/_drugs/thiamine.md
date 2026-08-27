---
layout: default
title: Thiamine
parent: 僅模型預測 (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
---

# Thiamine
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

# Thiamine: From Vitamin B1 Deficiency to Hyperthyroidism

## One-Sentence Summary

Thiamine (Vitamin B1, DrugBank DB00152) is classically used to treat thiamine deficiency states such as beriberi and Wernicke's encephalopathy. The TxGNN model predicts it may also be effective for **Hyperthyroidism**, specifically for managing the cardiovascular consequences of the hypermetabolic thyrotoxic state, with **1 completed pilot clinical trial** and **20 related publications** currently supporting this direction — though the evidence base remains preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thiamine (Vitamin B1) deficiency (e.g., beriberi, Wernicke's encephalopathy) — no SAHPRA-approved indication text is on file, as the product is not currently registered in South Africa |
| Predicted New Indication | Hyperthyroidism (cardiovascular dysfunction associated with thyrotoxicosis) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (data gap DG002). Based on known pharmacology, thiamine is an essential water-soluble vitamin that functions as a cofactor for pyruvate dehydrogenase, alpha-ketoglutarate dehydrogenase, and transketolase — enzymes central to carbohydrate metabolism and cellular energy production. Its efficacy in correcting thiamine deficiency (beriberi, Wernicke's encephalopathy) is well established.

The proposed link between thiamine and hyperthyroidism is physiological rather than a shared disease category: thyrotoxicosis is a hypermetabolic state that increases tissue oxygen consumption and substrate turnover, which in turn raises the body's thiamine requirement. Older biochemical studies (1940s–1960s) documented altered thiamine turnover and tissue storage in hyperthyroid animals and patients, and multiple modern case reports describe hyperthyroid or thyrotoxic patients developing beriberi-like high-output heart failure or Wernicke's encephalopathy — conditions that are classically thiamine-responsive.

Mechanistically, this suggests that in a subset of severely hyperthyroid patients, a relative or functional thiamine deficiency may develop and contribute to cardiovascular strain, which could theoretically be improved by thiamine supplementation. This hypothesis has been tested directly in one small prospective pilot study, giving the prediction some early clinical grounding, though it does not establish thiamine as a treatment for hyperthyroidism itself (the underlying thyroid disease still requires standard antithyroid therapy).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | Phase NA | Completed | 12 | Pilot study evaluating prevalence of thiamine deficiency and thiamine supplementation's effect on cardiovascular function in patients with severe hyperthyroidism/thyrotoxicosis; small uncontrolled cohort. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21064291](https://pubmed.ncbi.nlm.nih.gov/21064291/) | 1946 | Mechanistic study | Federation proceedings | Thiamine deficiency, quinidine, hyper- and hypothyroidism alter cardiac muscle ATP content and ATPase activity in rats. |
| [13305517](https://pubmed.ncbi.nlm.nih.gov/13305517/) | 1955 | Clinical mechanistic study | Endocrinologia e scienza della costituzione | Urinary thiamine excretion after IV cocarboxylase loading differs in hyperthyroid vs. normal subjects. |
| [13934469](https://pubmed.ncbi.nlm.nih.gov/13934469/) | 1963 | Animal study | Annals of biochemistry and experimental medicine | Tissue thiamine storage and intestinal synthesis altered in hypo- and hyper-thyroid rats. |
| [13168067](https://pubmed.ncbi.nlm.nih.gov/13168067/) | 1954 | Mechanistic study | La Riforma medica | Behavior of free thiamine and thiamine ester differs across thyroid disease states. |
| [13588400](https://pubmed.ncbi.nlm.nih.gov/13588400/) | 1958 | Animal study | The Journal of nutrition | Thyroprotein and penicillin affect thiamine requirement and growth in hyperthyroid rats. |
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case report | Critical care nursing clinics of North America | High-output heart failure caused by thyrotoxicosis and beriberi (thiamine deficiency); reviews shared hemodynamic mechanism. |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case report | Journal of general internal medicine | Thyrotoxicosis-associated Wernicke's encephalopathy responsive to thiamine repletion. |
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case report | Cureus | Wernicke's encephalopathy associated with transient gestational hyperthyroidism and hyperemesis gravidarum. |
| [22436368](https://pubmed.ncbi.nlm.nih.gov/22436368/) | 2013 | Case report | Neurologia (Barcelona, Spain) | Wernicke's encephalopathy secondary to hyperthyroidism and ingestion of thiaminase-rich foods. |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case report | Cureus | Uncommon presentation of hyperthyroidism culminating in severe neurological (Wernicke-type) consequences. |

---

## South Africa Market Information

Thiamine currently holds **no SAHPRA registration** on record for this candidate (`taiwan_regulatory.total_licenses = 0`, market status: Not marketed). No licensed product entries are available to summarize dosage form or approved indication text in South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A Blocking data gap (DG001) has been identified — TFDA/SAHPRA label warnings and contraindications are not yet available, which prevents this candidate from completing the S1 safety pre-screen.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for thiamine in hyperthyroidism-related cardiovascular dysfunction is currently limited to one small, uncontrolled pilot study (n=12) supported mainly by historical mechanistic research and case reports of thiamine-responsive complications (beriberi-like heart failure, Wernicke's encephalopathy) occurring in thyrotoxic patients — this is suggestive but not yet actionable evidence. Combined with the product having zero SAHPRA registrations in South Africa and a Blocking safety data gap (no TFDA/SAHPRA label data available), the candidate is not ready to proceed.

**To proceed, the following is needed:**
- TFDA/SAHPRA-approved Professional Information (warnings, contraindications, dosing) to resolve the Blocking data gap (DG001)
- Confirmed mechanism of action data (DG002)
- Larger controlled trials directly testing thiamine supplementation for cardiovascular outcomes in hyperthyroid/thyrotoxic patients
- Clarification of target population (e.g., severe thyrotoxicosis vs. general hyperthyroidism) and dosing/route feasibility given the product is not currently marketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

