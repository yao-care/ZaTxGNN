---
layout: default
title: Estradiol Valerate
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Estradiol Valerate: predicted new indication Symptomatic form of fragile X syndrome in female carrier (evidence level L5). Approved use: Primary ovarian failure"
monitor_inn: "Estradiol valerate"
predicted_indications: ["symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "ovarian remnant syndrome", "anovulation", "luteoma of pregnancy", "ovarian dysfunction"]
---

# Estradiol Valerate
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

## Estradiol Valerate: From Primary Ovarian Failure to Fragile X Premutation Carrier Symptoms (Top Prediction)
{: .text-alpha }

## One-Sentence Summary

Estradiol valerate is an oral oestrogen, originally used for **primary ovarian failure** (oestrogen replacement).
The TxGNN model's top-ranked prediction is **symptomatic fragile X syndrome in female carriers**, which has **no clinical trials and no publications** supporting it.
The only prediction in the top 10 with a registered clinical trial is **anovulation** (1 Phase 4 trial of unknown status), and that evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary ovarian failure |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carrier (rank 1 of 10 predictions reviewed) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

**Other predictions reviewed (all scores 99.9%+):**

| Rank | Predicted Indication | Evidence Level | Recommendation |
|---|---|---|---|
| 2 | Blepharophimosis-epicanthus inversus-ptosis (BPES) | L5 | Hold |
| 3 | Partial trisomy/tetrasomy of 5p | L5 | Hold |
| 4 | Partial trisomy/tetrasomy of 12p | L5 | Hold |
| 5 | BPES due to 3q23 rearrangement | L5 | Hold |
| 6 | Partial trisomy/tetrasomy of 18p | L5 | Hold |
| 7 | Ovarian remnant syndrome | L5 | Hold |
| 8 | Anovulation | L3 | Research question |
| 9 | Luteoma of pregnancy | L5 | Hold |
| 10 | Ovarian dysfunction | L4 | Research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Estradiol valerate is an ester prodrug of oestradiol, the main natural oestrogen. Its efficacy as replacement therapy in primary ovarian failure rests on restoring oestrogen levels.

**Rank 1 (fragile X carriers):** Female carriers of an FMR1 premutation can develop fragile X-associated primary ovarian insufficiency (FXPOI). This overlaps with the approved indication of primary ovarian failure, which probably explains the high score. Oestradiol would address the consequences of low oestrogen, not the underlying FMR1 defect.

**Ranks 2 and 5 (BPES):** BPES type I is linked to premature ovarian insufficiency (FOXL2 changes). Oestrogen replacement is rational only for the ovarian component and would not treat the eyelid malformations.

**Ranks 3, 4 and 6 (partial chromosome 5p, 12p and 18p trisomy/tetrasomy):** There is no clear mechanistic rationale. These predictions probably reflect proximity in the knowledge graph rather than an oestrogen-responsive pathway.

**Rank 7 (ovarian remnant syndrome) and rank 9 (luteoma of pregnancy):** Neither is an established oestradiol indication. In ovarian remnant syndrome, oestrogen could stimulate remnant tissue. Luteoma of pregnancy is hormone-driven, usually resolves after delivery, and oestradiol could be counterproductive.

**Rank 8 (anovulation):** Oestradiol has been tested as an add-on to clomiphene citrate in ovulation induction, to offset clomiphene's anti-oestrogenic effects on the endometrium and cervical mucus. This is plausible, but most of the supplied literature uses estradiol valerate to *induce* anovulation and polycystic ovaries in animals. That points to a drug-induced effect, not therapeutic benefit.

**Rank 10 (ovarian dysfunction):** Oestrogen replacement is conceptually relevant to hypo-oestrogenic ovarian dysfunction, but the term is broad and the supporting evidence is indirect.

---

## Clinical Trial Evidence

The top-ranked prediction has no registered clinical trials. The only trial found across the top 10 predictions is for rank 8 (anovulation):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | RCT of clomiphene citrate plus estradiol vs clomiphene alone for ovulation induction in infertile women (2014-06 to 2018-08). No results supplied, so efficacy is unconfirmed. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

---

## Literature Evidence

The top-ranked prediction has no publications. For the other predictions, the supplied literature is mostly preclinical (e.g. rat PCOS models induced by estradiol valerate) and does not support therapeutic benefit. The most relevant human publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36063826](https://pubmed.ncbi.nlm.nih.gov/36063826/) | 2022 | Randomised trial | Gynecol Endocrinol | Compared 4, 6 and 9 mg/day estradiol valerate in 88 women with unexplained recurrent abortion; looked at oestrogen receptor expression and ovarian function (anovulation prediction). |
| [33749482](https://pubmed.ncbi.nlm.nih.gov/33749482/) | 2021 | Clinical study | Gynecol Endocrinol | Estradiol valerate/nomegestrol acetate as first-line and rescue therapy for ovarian endometriomas and deep infiltrating endometriosis (ovarian dysfunction prediction; indirect support only). |
| [1472813](https://pubmed.ncbi.nlm.nih.gov/1472813/) | 1992 | Clinical series | J Assist Reprod Genet | Oocyte donation in women with ovarian failure: oral estradiol valerate 6 mg/day plus progesterone gave hormonal preparation for embryo transfer (13 women, 17 cycles). |
| [9024224](https://pubmed.ncbi.nlm.nih.gov/9024224/) | 1997 | Clinical study | J Clin Endocrinol Metab | Hormone replacement with estradiol valerate plus cyproterone or medroxyprogesterone acetate in postmenopausal women; effects on nitric oxide levels. |
| [40774400](https://pubmed.ncbi.nlm.nih.gov/40774400/) | 2025 | Review | J Steroid Biochem Mol Biol | Review of agents used to induce PCOS in animal models, including estradiol valerate. Not evidence of therapeutic benefit. |
| [12960066](https://pubmed.ncbi.nlm.nih.gov/12960066/) | 2003 | Animal study | Endocrinology | Prepubertal estradiol valerate disrupted cyclicity and caused cystic ovaries in adult rats. This is a harm signal, not a benefit. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| B/21.8.1/16 | Progynova | Tablet | Not available in the data compiled for this report |
| 43/18.8/0591 | Qlaira | Tablet | Not available in the data compiled for this report |

Both registrations are valid single-ingredient entries, and all dosage forms are oral. Essential Medicines List status was not available in the data compiled for this report.

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
The TxGNN knowledge graph links estradiol valerate to contraindications in the following conditions: hypertension, epilepsy, anxiety and neurotic disorders, dysthymic disorder, porphyria, kidney disease, liver disease, gallbladder disease, congestive heart failure, hypercalcaemia (including humoral hypercalcaemia of malignancy), hypothyroidism, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hypertriglyceridaemia, gynaecomastia and breast hypertrophy.

These come from graph relationships and must be verified against the approved label.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings, contraindications and drug interactions. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (fragile X carriers) rests on a computational score alone, and oestradiol would treat only the hypo-oestrogenic consequences, not the genetic condition. The only trial found (anovulation) is Phase 4 with unknown status and no results, and most supporting literature is animal work in which estradiol valerate *causes* ovarian pathology.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) to complete safety screening
- Mechanism of action data
- For FXPOI and BPES-related ovarian insufficiency: clinical literature on oestrogen replacement in these populations, framed as an extension of the existing primary ovarian failure indication
- For anovulation: results or a status update for NCT02186782, and a review of whether the add-on benefit holds in human data
- A review of the contraindication signals above against the label before any new-use evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

