---
layout: default
title: Progesterone
parent: Model Prediction Only (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Progesterone: predicted new indication Amenorrhea (evidence level L5). Approved use: Endometriosis"
monitor_inn: "Progesterone"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "benign mammary dysplasia", "renal hypoplasia, bilateral", "cervix endometriosis", "renal hypoplasia (disease)", "endometriosis in cutaneous scar", "endometriosis of rectovaginal septum and vagina", "blunt duct adenosis of breast", "apocrine adenosis of breast"]
---

# Progesterone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Progesterone: From Endometriosis to Amenorrhea

## One-Sentence Summary

Progesterone is a natural steroid hormone, originally used for endometriosis, endometrial conditions, and menopause-related conditions such as postmenopausal osteoporosis and atrophic vaginitis.
The TxGNN model predicts it may be effective for **amenorrhea**,
with **4 clinical trials** and **19 publications** currently supporting this direction. The trials mainly test estrogen-based regimens, so the evidence for progesterone itself is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the SAHPRA registration does not list an approved indication text; original indications are taken from the TxGNN knowledge graph) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (as scored in the data compiled for this report; see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The data compiled for this report assigns L1, but only one completed Phase 3 trial (NCT00946192) was identified, and it tested estrogen rather than progesterone. Under the strict definition (at least 2 completed Phase 3 RCTs) the level would be lower, closer to L2. Read L1 as an upper bound.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, progesterone is the body's natural progestogen. It controls the cyclic changes of the endometrium, and its withdrawal triggers endometrial shedding.

Progesterone withdrawal is a standard diagnostic and therapeutic tool in secondary amenorrhea. It is used to induce a withdrawal bleed and to test whether the endometrium is oestrogen-primed. In hypoestrogenic amenorrhoea (for example in athletes or anorexia nervosa), the trials mainly use oestrogen, with or without cyclic progestogen. Progesterone's role there is endometrial protection and cycle induction. It does not correct the underlying hypothalamic dysfunction.

The use of progesterone in amenorrhoea is therefore already established clinical practice. This prediction is closer to a well-established use than to novel repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Completed | 121 | Young athletes with amenorrhoea. Compares body composition and hormones, and tests transdermal or oral oestrogen against none for bone density. Progesterone's own contribution is uncertain. |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Adolescents with anorexia nervosa. Tests whether oestrogen maintains bone development. The outcome is bone mass, which is indirect for amenorrhoea. |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Active, not recruiting | 120 | Transdermal oestradiol with cyclic progesterone vs placebo in hypoestrogenic young women with eating disorders. Cognitive and reward endpoints only. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Cardiovascular and inflammatory risk markers in young women with functional hypothalamic amenorrhoea. Indirect relevance to treatment. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Rev Endocr Metab Disord | Diagnostic and therapeutic use of oral micronised progesterone in endocrinology, including its role in the control of LH/FSH secretion and endometrial cycling |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Front Endocrinol | Aetiology, symptoms, and treatment of premature ovarian insufficiency |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | South Med J | Primary ovarian insufficiency; secondary amenorrhoea often needs hormone replacement therapy |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecol Endocrinol | Neuroendocrine control of ovulation; hypothalamic failure leads to anovulation and amenorrhoea |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | Review | Climacteric | Clinical management of vaginal bleeding in postmenopausal women |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | Am Fam Physician | Evaluation of amenorrhoea: exclude pregnancy first, then check prolactin and TSH |
| [7457308](https://pubmed.ncbi.nlm.nih.gov/7457308/) | 1980 | Review | Am Fam Physician | Stepwise evaluation of amenorrhoea, including withdrawal bleeding after a progesterone challenge |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Semin Reprod Med | Intrauterine adhesions (Asherman's syndrome), a cause of amenorrhoea |

No randomised controlled trials were identified in the literature set. It consists mostly of narrative reviews, and several older entries lack abstracts.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A40/21.8.2/0771 | Utrogestan | Capsule (oral) | Approved indication text not available in the data compiled for this report |

Essential Medicines List (EML) status is not available in the data compiled for this report. Only oral capsule forms are registered.

---

## Safety Considerations

SAHPRA package insert warnings and contraindications were not available for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Conditions flagged in the drug-disease knowledge graph (not label text, so verify against the PI):**
hypertension, liver failure and liver disease, epilepsy, anxiety and mood disorders, porphyria, kidney disease, gallbladder disease, hyperglycaemia and diabetes mellitus (including diabetic ketoacidosis), hypothyroidism, osteoporosis, systemic lupus erythematosus, asthma, hypertriglyceridaemia, and substance abuse/dependence.

**Drug Interactions:**
The interaction screen returned 100 interactions in total. The 20 shown are all graded Moderate. The main groups are:
- **Antidiabetic agents:** acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, repaglinide, DPP-4 inhibitors (alogliptin, saxagliptin), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), GLP-1 agonists (albiglutide, dulaglutide, liraglutide, semaglutide), and insulins (aspart, degludec, detemir). Glucose control may need closer monitoring.
- **Other:** aprepitant and clarithromycin.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Progesterone is already used in amenorrhoea as a withdrawal challenge and for cycle induction, and the prediction fits established practice. The trial evidence tests oestrogen-based regimens, so it does not show a benefit specific to progesterone. This is not a novel repurposing. It is a use that should be confirmed against the registered label.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to confirm the approved indication, warnings, and contraindications. This is currently a blocking data gap.
- Detailed mechanism of action data.
- A check of whether the registered Utrogestan oral capsule label covers amenorrhoea, or whether use would be off-label.
- Clarification of the type of amenorrhoea (primary vs secondary, hypothalamic vs ovarian) in which progesterone-specific benefit is expected.
- A review of the knowledge-graph contraindication flags (especially liver disease, porphyria, and diabetes) and the antidiabetic interactions for the target population.

---

## Other Predicted Indications (Lower Priority)

| Rank | Predicted Indication | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|
| 2 | Breast fibrocystic disease | L4 | Research question | Plausible luteal-insufficiency hypothesis; no registered trials, only older reviews and epidemiology |
| 3 | Benign mammary dysplasia | L4 | Research question | Essentially the same condition as rank 2; evidence is indirect and includes veterinary studies |
| 4 | Renal hypoplasia, bilateral | L5 | Hold | No clear mechanistic link; score likely reflects graph proximity |
| 5 | Cervix endometriosis | L4 | Hold | Literature focuses on antiprogestins; parent endometriosis indication already exists |
| 6 | Renal hypoplasia (disease) | L5 | Hold | One preclinical Pkd mouse study only; no clinical evidence |
| 7 | Endometriosis in cutaneous scar | L4 | Hold | Single case report; surgery is the usual treatment |
| 8 | Endometriosis of rectovaginal septum and vagina | L4 | Hold | Receptor expression study only; does not test treatment efficacy |
| 9 | Blunt duct adenosis of breast | L5 | Hold | No trials or literature retrieved |
| 10 | Apocrine adenosis of breast | L5 | Hold | Pathology and diagnostic literature only; progesterone not evaluated as treatment |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

