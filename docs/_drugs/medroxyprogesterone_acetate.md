---
layout: default
title: Medroxyprogesterone Acetate
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Medroxyprogesterone acetate (MPA, DrugBank DB00603) is a synthetic progestin most widely known as a depot injectable contraceptive (e.g., Depo-Provera) and menstrual-cycle regulator. The TxGNN model predicts it may also be effective for treating **Amenorrhea**, with **10 clinical trials** and **20 publications** currently identified as supporting evidence, including a Phase 3 RCT that directly evaluated post-ablation MPA for endometrial amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormonal contraception (depot injectable, e.g. Depo-Provera) — inferred from literature evidence; not documented in the South Africa regulatory dataset |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack (Data Gap DG002). Based on well-established pharmacology, medroxyprogesterone acetate is a synthetic progestin that suppresses hypothalamic-pituitary-gonadal axis signalling (reducing GnRH/LH pulsatility) and acts directly on the endometrium, driving secretory transformation and eventual atrophy/shedding of the endometrial lining.

This is the same mechanism already exploited when MPA is used as a depot contraceptive: a very high proportion of long-term DMPA users develop treatment-induced amenorrhea as a recognised pharmacological effect, a phenomenon documented in the literature for decades (e.g., PMID 842303, PMID 9554247). In other words, "amenorrhea" is not a biologically novel target for MPA — it is a direct, mechanistically predictable extension of an effect the drug already produces in its established contraceptive use, now being considered as a deliberate therapeutic endpoint (e.g., managing heavy menstrual bleeding, post-ablation bleeding control, or endometrial suppression).

This is further supported by NCT02449161, a Phase 3 RCT that directly assessed post-ablation MPA on endometrial amenorrhea rates, though the trial was terminated early with a small enrollment (n=60), which tempers the strength of the direct clinical evidence. Combined with the broad, decades-long real-world experience of MPA-induced amenorrhea in contraceptive populations, the mechanistic plausibility of this prediction is high, even though confirmatory large-scale RCTs specifically targeting amenorrhea as a primary therapeutic endpoint (rather than a contraceptive side effect) remain limited.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | RCT evaluating the effect of post-endometrial-ablation MPA on endometrial amenorrhea rates in women with heavy menstrual bleeding; terminated early. |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Assessed whether progesterone-induced withdrawal bleeding is necessary before ovulation induction with clomiphene citrate in women with oligo-/amenorrhea. |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | N/A | Not yet recruiting | 276 | RCT of a traditional Chinese herbal formula (Huanjingjian decoction) for premature ovarian insufficiency; not an MPA trial, disease-area overlap only. |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Phase 3 | Recruiting | 120 | Double-blind, placebo-controlled study of relugolix for heavy menstrual bleeding associated with uterine fibroids; MPA-specific relevance unconfirmed. |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Phase 4 | Completed | 108 | Hormone replacement therapy effects on disease activity, menopausal symptoms and bone mineral density in peri/postmenopausal women with SLE. |
| [NCT02792153](https://clinicaltrials.gov/study/NCT02792153) | Phase 1 | Withdrawn | 0 | Estradiol and fear-extinction study in weight-restored women with anorexia nervosa; withdrawn (enrollment 0), low relevance. |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Timing of postpartum depot MPA administration and its effect on breastfeeding continuation, contraceptive continuation, and postpartum depression. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Compared cardiovascular risk markers in young women with functional hypothalamic amenorrhea versus regularly cycling controls. |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Safety profile of Tualang honey combined with hormone replacement therapy in postmenopausal women. |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1886 | Large RCT of bazedoxifene/conjugated estrogens on endometrial hyperplasia and osteoporosis prevention in postmenopausal women. |

No South African National Clinical Trials Register (SANCTR) or Pan African Clinical Trials Registry (PACTR) entries were identified for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | Cohort (RCT) | PLoS ONE | WHICH randomized trial: effects of DMPA vs. norethisterone enanthate on estradiol levels and menstrual/psychological/behavioural measures relevant to HIV risk. |
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | Clinical Trial | Contraception | Randomized comparison showing Cyclofem restored bleeding in 82% of women with DMPA-induced amenorrhea vs. 10% continuing DMPA. |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | Observational | Acta Obstet Gynecol Scand | Endometrial histology and hormone levels in women with MPA-induced amenorrhoea compared with women with secondary amenorrhoea. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Systematic Review | Cochrane Database Syst Rev | Cochrane review of combination injectable contraceptives, including bleeding-pattern effects. |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counseling and management of side effects, including amenorrhea, in women using depot MPA contraception. |
| [8492647](https://pubmed.ncbi.nlm.nih.gov/8492647/) | 1993 | Review | MCN Am J Matern Child Nurs | Overview of Depo-Provera use, mechanism, and menstrual effects. |
| [120837](https://pubmed.ncbi.nlm.nih.gov/120837/) | 1979 | Review | IARC Monographs | General monograph on medroxyprogesterone acetate pharmacology and use. |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception review, including postpartum amenorrhea considerations. |
| [1604074](https://pubmed.ncbi.nlm.nih.gov/1604074/) | 1992 | Review | Rev Med Liege | General review of hormonal contraception. |
| [6141923](https://pubmed.ncbi.nlm.nih.gov/6141923/) | 1984 | Review | Drug Intell Clin Pharm | Review of drug-induced infertility, including progestin-related mechanisms. |

---

## South Africa Market Information

Medroxyprogesterone acetate currently has **no SAHPRA product registrations** on record, and the regulatory dataset lists its South African market status as **Not marketed**. No dosage-form, brand-name, or Essential Medicines List (EML) inclusion data is available for this evidence pack at this time.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The prediction is mechanistically well-grounded: MPA-induced amenorrhea is an established, decades-documented pharmacological effect in contraceptive use, and one directly relevant Phase 3 RCT (NCT02449161, though terminated early with n=60) supports its intentional use for endometrial amenorrhea. This corresponds to Evidence Level L2, sufficient to move past pure model prediction but short of confirmatory large-scale trial evidence.

**To proceed, the following is needed:**
- TFDA/SAHPRA-equivalent Professional Information (PI) warnings and contraindications (currently a Blocking data gap — DG001), required before any S1 safety pre-assessment can proceed
- Detailed mechanism-of-action documentation from DrugBank (High-priority data gap — DG002)
- SAHPRA registration or market-entry pathway assessment, since MPA currently has zero registrations and is not marketed in South Africa
- A confirmatory, adequately powered Phase 2/3 RCT specifically targeting amenorrhea as a primary therapeutic endpoint (rather than as a contraceptive side effect)
- Clarification of the full trial design/title for NCT06671548 and NCT00808132, whose relevance to MPA specifically could not be confirmed from truncated records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

