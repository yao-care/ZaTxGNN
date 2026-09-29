---
layout: default
title: Medroxyprogesterone Acetate
parent: Model Prediction Only (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
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

# Medroxyprogesterone Acetate: From Progestin Therapy to Amenorrhea

## One-Sentence Summary

Medroxyprogesterone acetate (MPA) is a synthetic progestin sold in South Africa as injectable and tablet products. The registered indication text is not available in the data reviewed.
The TxGNN model predicts it may be effective for **amenorrhea**, with **10 clinical trials** and **20 publications** retrieved.
However, none of these directly test MPA as a treatment for amenorrhea. Most trials and papers are indirect, or describe MPA *causing* amenorrhea.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 (the automated pipeline assigned L2, but no completed trial directly tests MPA for amenorrhea) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. MPA is a progestin, and it is plausible that it may be applicable to amenorrhea.

Progestins convert an estrogen-primed endometrium into a secretory state. When the progestin is stopped, withdrawal bleeding follows. This is the basis of the "progestin challenge" used to assess secondary amenorrhea. It also supports treating secondary amenorrhea when estrogen is present but ovulation is absent.

Two cautions apply:
- The registered indications in the data reviewed are blank, so amenorrhea may already be a labelled use. If so, this is confirmation of an existing use rather than true repurposing.
- Much of the evidence runs in the opposite direction. MPA, especially the depot injection, is a well-known *cause* of amenorrhea.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Phase 3 | Terminated | 60 | Post-ablation MPA to increase endometrial amenorrhea in heavy menstrual bleeding. It uses MPA to induce amenorrhea, not treat it. |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | Completed | 42 | Whether progestin-induced withdrawal bleeding is needed before clomiphene ovulation induction in oligo- or amenorrhea. |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Phase 2 | Completed | 29 | Cardiovascular risk markers in young women with functional hypothalamic amenorrhea. Indirect. |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Phase 4 | Completed | 184 | Timing of postpartum depot MPA and breastfeeding. This is a contraception study. |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Phase 3 | Completed | 1,886 | Bazedoxifene/conjugated estrogens in postmenopausal women, with MPA probably as an active control. Not about amenorrhea. |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Phase 2/3 | Completed | 79 | Tualang honey versus HRT safety in postmenopausal women. Indirect. |

Four other retrieved trials (NCT07020429, NCT06671548, NCT00392093, NCT02792153) are unrelated to MPA in amenorrhea and are omitted. No SANCTR or PACTR registrations were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9554247](https://pubmed.ncbi.nlm.nih.gov/9554247/) | 1998 | RCT | Contraception | 100 women with at least 6 months of DMPA-induced amenorrhea were randomised to switch to Cyclofem or continue DMPA. At 6 months, 82% of Cyclofem users had bleeding versus 10% of DMPA users. |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | Randomised trial (WHICH) | PLoS One | Compared DMPA-IM and NET-EN on estradiol levels and menstrual effects. This is a South African study, but it is about contraceptive side effects. |
| [842303](https://pubmed.ncbi.nlm.nih.gov/842303/) | 1977 | Clinical study | Acta Obstet Gynecol Scand | Endometrial histology and hormone levels in 11 women with DMPA-induced amenorrhoea, compared with 12 women with secondary amenorrhoea. |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Cochrane review | Cochrane Database Syst Rev | Combination injectable contraceptives are highly effective, but bleeding pattern changes may limit acceptability. |
| [8725701](https://pubmed.ncbi.nlm.nih.gov/8725701/) | 1996 | Review | J Reprod Med | Counselling and side-effect management for DMPA, including bleeding changes. |
| [6119259](https://pubmed.ncbi.nlm.nih.gov/6119259/) | 1981 | Review | Int J Gynaecol Obstet | Postpartum contraception, including the unpredictable return of ovulation after postpartum amenorrhea. |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Report | Am J Obstet Gynecol | Prolonged gynaecologic and endocrine effects after MPA given during pregnancy. |

Most of the 20 retrieved papers are older narrative reviews on contraception. The evidence is mainly about MPA-induced amenorrhea, not MPA as a treatment for it.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| 52/21.8.2/0991 | Mytricon | Injection |
| E/21.8.2/114 | Depo-provera 1ml | Injection |
| 32/21.8/0631 | Premelle Cycle-5 | Tablet |
| 36/21.8/0197 | Premelle Ld-0.3/1.5 | Tablet |

Two products are injectable and two are oral. Approved indication text and Essential Medicines List status were not available in the data reviewed. Whether the Premelle tablets are MPA alone or combination products should be confirmed from the PI.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found in the data reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the TxGNN score is very high. However, no completed trial directly tests MPA as a treatment for amenorrhea, and most of the evidence describes MPA causing amenorrhea. The safety data from the SAHPRA package insert is missing, which blocks safety screening. The automated pipeline suggested "Proceed with Guardrails", but I recommend holding until the items below are resolved.

**To proceed, the following is needed:**
- The SAHPRA package insert, covering approved indications, warnings and contraindications. This will show whether amenorrhea is already a labelled use.
- Confirmation that a registered oral MPA product suitable for this use is available in South Africa. The depot injection is not suitable, since it causes amenorrhea.
- Mechanism of action data from DrugBank.
- Direct clinical evidence, such as a trial or guideline, of MPA for secondary amenorrhea.
- A drug interaction check.

The other nine predictions (ranks 2–10) are weaker, with evidence at L3 or below. The renal hypoplasia predictions are likely knowledge-graph artefacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

