---
layout: default
title: Progesterone
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
---

# Progesterone
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

# Progesterone: From Hormonal Therapy to Amenorrhea

## One-Sentence Summary

> Progesterone is a natural steroid hormone with long-established roles in reproductive endocrinology; this evidence pack does not contain a specific SAHPRA-registered indication for the drug in South Africa (it is currently **not marketed** here).
> The TxGNN model predicts it may be effective for **Amenorrhea**, ranked 14th among all predicted indications with a score of **99.9996%**.
> Evidence support is currently indirect: **49 clinical trials** and **18 publications** were retrieved, but none is a completed trial specifically testing progesterone's efficacy against amenorrhea — most evidence instead relates to the well-established use of progesterone/progestins for menstrual-cycle regulation and diagnostic withdrawal bleeding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this evidence pack (no SAHPRA license/indication text available — see South Africa Market Information below) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.9996% (rank 14 of all predicted indications) |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack. Based on the mechanistic rationale accompanying this prediction, progesterone acts on the hypothalamic-pituitary-ovarian (HPO) axis. The **progesterone withdrawal bleeding test** is a classic clinical method used to evaluate the etiology of amenorrhea, and progestogen therapy is already one of the standard interventions for secondary and anovulatory (ovulatory-disorder) amenorrhea.

This points to an important nuance for evaluators: rather than identifying a genuinely novel therapeutic application, the TxGNN model may largely be recovering progesterone's **already-established clinical role** in the amenorrhea diagnostic/treatment pathway (progestin challenge test, induction of withdrawal bleeding, and progestin support in anovulatory cycles). Several of the retrieved clinical trials reinforce this — e.g., studies of medroxyprogesterone acetate and progesterone-induced withdrawal bleeding directly in amenorrhea/oligomenorrhea populations — while most of the higher-graded trials (functional hypothalamic amenorrhea, bone density, eating disorders) study the *disease population* rather than progesterone itself, using estrogen, romosozumab, or kisspeptin as the actual intervention.

Consequently, the reasonableness of this "prediction" rests less on discovering a new mechanism and more on confirming a known, guideline-supported use — which still has value for standardizing practice in a market where the drug is not currently registered, but should not be framed to prescribers as a novel repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | Completed | 1845 | Prospective, randomized, double-blind, placebo-controlled trial of combined estradiol + progesterone for vasomotor symptoms in postmenopausal women with an intact uterus |
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT of post-endometrial-ablation medroxyprogesterone acetate on endometrial amenorrhea rates in women with heavy menstrual bleeding |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Evaluated whether progesterone-induced endometrial withdrawal bleeding is necessary before clomiphene-based ovulation induction in oligo-/amenorrhea |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | Unknown | 330 | Multicenter RCT comparing Zhenqi Buxue Oral Liquid, Progesterone Capsules, and their combination for menstrual disorders |
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | Completed | 300 | Single-blind comparative study of SJ-0021 vs. purified pituitary gonadotropin in amenorrhea I / anovulatory cycles |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | Recruiting | 114 | Romosozumab as adjunct to physiologic estrogen replacement (with cyclic progesterone) for bone density in functional hypothalamic amenorrhea |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | Completed | 110 | Effects of estrogen administration on bone development in adolescents with anorexia-nervosa-related amenorrhea |
| [NCT01674426](https://clinicaltrials.gov/study/NCT01674426) | N/A | Completed | 17 | Randomized pilot study of cognitive behavior therapy vs. observation for functional hypothalamic amenorrhea |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | Recruiting | 120 | RCT of transdermal estradiol with cyclic progesterone vs. placebo on cognitive/reward outcomes in hypoestrogenemic eating-disorder patients |
| [NCT02858336](https://clinicaltrials.gov/study/NCT02858336) | N/A | Completed | 38 | Studied effects of caloric restriction, diet and exercise on menstrual cycles in functional hypothalamic amenorrhea |

Note: no SANCTR or PACTR-registered trials were identified in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | Reviews diagnostic and therapeutic use of oral micronized progesterone in endocrinology, including its action on hypothalamic kisspeptin/neurokinin B/dynorphin neurons regulating LH/FSH |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Current Problems in Pediatric and Adolescent Health Care | Reviews etiology and management of amenorrhea in adolescent/young adult women, centered on hypothalamic-pituitary-ovarian axis dysfunction |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | Practical evaluation approach to amenorrhea, noting progesterone challenge as a key diagnostic step after ruling out pregnancy |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | Reviews etiology, symptomatology and treatment (including hormone therapy) for premature ovarian insufficiency, a cause of secondary amenorrhea |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | Review | Southern Medical Journal | Current concepts in primary ovarian insufficiency, including hormone replacement for resulting amenorrhea |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | Review | Gynecological Endocrinology | Describes neuroendocrine control of ovulation and how HPO axis failure results in anovulation/amenorrhea |
| [18756412](https://pubmed.ncbi.nlm.nih.gov/18756412/) | 2008 | Review | Seminars in Reproductive Medicine | Reviews intrauterine adhesions (Asherman's syndrome) presenting across a spectrum from amenorrhea to menstrual disturbance |
| [945033](https://pubmed.ncbi.nlm.nih.gov/945033/) | 1976 | Case series | Annals of Internal Medicine | Studied 15 patients with galactorrhea-amenorrhea syndromes, noting failure of luteinizing hormone and progesterone levels to show ovulatory/luteal patterns |
| [5388335](https://pubmed.ncbi.nlm.nih.gov/5388335/) | 1969 | Review | Clinical Obstetrics and Gynecology | Early general review of amenorrhea (abstract not available) |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | Meta-analysis | Frontiers in Oncology | Meta-analysis of risk factors and prognostic significance of chemotherapy-induced amenorrhea in premenopausal breast cancer patients |

---

## South Africa Market Information

No SAHPRA product registrations were found for progesterone in this evidence pack (market status: **not marketed**, total licenses: **0**). Prescribers should confirm current registration status directly with SAHPRA before considering clinical use, as unregistered products require Section 21 authorization for access in South Africa.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: this evidence pack flagged a **Blocking** data gap — TFDA/SAHPRA label warnings and contraindications are not yet available — which by itself prevents a full safety pre-assessment (S1) for this candidate.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No completed trial in this pack directly tests progesterone's efficacy specifically for treating amenorrhea (evidence level L4, mechanistic/indirect); most higher-relevance trials study the disease population using other interventions (estrogen, romosozumab, kisspeptin).
- The drug is not currently registered in South Africa (0 SAHPRA licenses), and a **Blocking** data gap on label warnings/contraindications prevents safety pre-assessment.
- The predicted indication substantially overlaps with progesterone's already-established diagnostic/therapeutic role in amenorrhea (progestin challenge test, withdrawal bleeding induction), so the incremental value of this "prediction" needs to be clarified before any development effort is prioritized.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI): warnings, contraindications, and drug interaction data (currently a Blocking gap)
- Confirmed mechanism-of-action documentation (DrugBank or equivalent)
- A clinical/regulatory assessment of whether this represents a genuinely new therapeutic use, or codification of existing off-label/diagnostic practice
- If pursued, a targeted trial or registry data directly evaluating progesterone (not estrogen/other progestins) as treatment for amenorrhea subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

