---
layout: default
title: Gestodene
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Gestodene
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

# Gestodene: From Contraception to Acne

## One-Sentence Summary

Gestodene is a progestin used in combined oral contraceptives (always together with an estrogen).
The TxGNN model predicts it may be effective for **acne**, which is the most plausible of the top-ranked predictions. There are **no registered clinical trials**, and the evidence rests on **about 15 publications**, most of them from the 1990s.

The model's top two predictions (migraine disorder, migraine with brainstem aura) are not therapeutic signals. The literature points to a **safety concern**: migraine with aura raises stroke risk in users of estrogen-containing contraceptives.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hormonal contraception (inferred from the products and literature; the SAHPRA records compiled for this report contain no indication text) |
| Predicted New Indication | Acne (the top-ranked prediction, migraine disorder, is a safety signal rather than a therapeutic one; see below) |
| TxGNN Prediction Score | 91.31% for acne (94.35% for migraine disorder) |
| Evidence Level | L3 for acne (L5 for the other top predictions) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold (acne is flagged as a research question only) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for gestodene. Based on the literature compiled for this report, gestodene is a potent progestin with low androgenic activity. In combination with ethinylestradiol, it suppresses ovulation and gonadotropin release.

For acne, the link is biologically plausible. Combined with ethinylestradiol, gestodene-containing pills raise sex hormone-binding globulin (SHBG) and lower free androgens, and androgens drive acne. Papers on progestin androgenicity (PMID 7825629, 8520092) and on androgen changes with low-dose contraceptives (PMID 8689882) support this mechanism.

Important limitations:
- Gestodene is only used with an estrogen, so its independent contribution to any acne benefit cannot be separated.
- The acne data are small and old (an open study of 19 patients; acne was mostly a secondary outcome).
- The predictions for migraine are not repurposing opportunities. Migraine with aura is generally a contraindication to estrogen-containing contraceptives because of stroke risk.
- Predictions for cutaneous T-cell lymphoma, seborrheic keratosis, vulvar inverted follicular keratosis, mycotic corneal ulcer and kyphoscoliotic heart disease have no trials, no literature and no evident mechanism. Allergic asthma has only one indirect epidemiological study.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Studies relevant to acne (predicted indication, rank 4):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8689881](https://pubmed.ncbi.nlm.nih.gov/8689881/) | 1996 | Clinical study | Contraception | Ethinylestradiol with gestodene vs desogestrel in 19 young women with non-severe acne vulgaris; effects on acne lesions and androgen markers (SHBG, free androgen index) |
| [8222658](https://pubmed.ncbi.nlm.nih.gov/8222658/) | 1993 | RCT | Contraception | Triphasic gestodene vs norethindrone pills: both effective; gestodene superior for cycle control and general tolerance (not an acne trial) |
| [8689882](https://pubmed.ncbi.nlm.nih.gov/8689882/) | 1996 | Clinical study | Contraception | Androgen changes in 100 healthy women on four low-dose contraceptives over six months |
| [8521763](https://pubmed.ncbi.nlm.nih.gov/8521763/) | 1995 | Review | Drugs | Pharmacology, efficacy and tolerability of gestodene in combined contraceptives |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Androgenicity of progestins and its structural basis |
| [8520092](https://pubmed.ncbi.nlm.nih.gov/8520092/) | 1995 | Review | Ann Pharmacother | Comparison of desogestrel, norgestimate and gestodene (chemistry, pharmacokinetics, efficacy, tolerability) |
| [8616979](https://pubmed.ncbi.nlm.nih.gov/8616979/) | 1995 | Review | Clin Obstet Gynecol | Gestodene-containing contraceptives: potent progestogen with strong anti-estrogenic and progestogenic effects |
| [10652979](https://pubmed.ncbi.nlm.nih.gov/10652979/) | 1999 | Cohort/case-control | Hum Reprod Update | UK database analyses of venous thromboembolism by individual combined pill formulation (safety) |

Studies retrieved for the migraine predictions (safety context, not treatment evidence):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30389542](https://pubmed.ncbi.nlm.nih.gov/30389542/) | 2018 | Guideline | Gynecol Obstet Fertil Senol | CNGOF guidelines: venous and arterial vascular risk persists with combined hormonal contraceptives |
| [25227335](https://pubmed.ncbi.nlm.nih.gov/25227335/) | 2014 | Review | Expert Opin Drug Saf | Thrombosis risk with different hormonal contraceptives by age |
| [11929641](https://pubmed.ncbi.nlm.nih.gov/11929641/) | 2002 | Case-control | Contraception | Danish five-year study of oral contraceptives and cerebral thromboembolic attacks |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 52/18.8/1019 | Dyolafem | Tablet | Not available in the data compiled |
| W/21.8.2/317 | Triodene Ed | Sct | Not available in the data compiled |
| W/18.8/11 | Minulette | Tablet | Not available in the data compiled |

All three registrations are valid. The data compiled for this report do not show Essential Medicines List (EML) status.

## Safety Considerations

- **Thrombosis and vascular risk:** The literature compiled for this report consistently describes venous thromboembolism and arterial ischaemic events with combined hormonal contraceptives, including gestodene-containing products.
- **Migraine, especially with aura:** This is a recognised stroke risk factor in users of combined oral contraceptives. The high TxGNN scores for migraine most likely reflect this contraindication context, not a therapeutic effect.
- **Drug interactions:** No interaction data were found.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine predictions reflect a safety signal rather than a treatment opportunity. Acne is biologically plausible, but the evidence is limited to small, dated studies of gestodene combined with ethinylestradiol, and no trials are registered. Safety data are incomplete and thrombosis risk remains a concern. Acne is best treated as a research question, not a basis for a change in practice.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings, contraindications, approved indications) for the three registered products
- Mechanism of action data for gestodene
- Modern, controlled acne trials that separate gestodene's effect from the estrogen component and compare it with established acne-indicated contraceptives
- A risk-benefit assessment covering thrombotic risk, and migraine with aura as a contraindication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

