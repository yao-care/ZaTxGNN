---
layout: default
title: Levonorgestrel
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 5
monitor_inn: "LEVONORGESTREL"
predicted_indications: ["acne (disease)", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "apocrine adenosis of breast", "blunt duct adenosis of breast"]
last_modified_at: 2026-10-29
description: "Levonorgestrel: predicted new indication acne (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Levonorgestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Levonorgestrel: progestin → acne (disease)
{: .text-alpha }

## One-Sentence Summary

Levonorgestrel is a progestin used in hormonal contraception and is marketed in South Africa in several oral tablet products.
The TxGNN model predicts it may be useful for **acne (disease)**, with a score of 0.9988.
No clinical trials are registered for this prediction, and the 20 publications compiled for this report are mostly reviews of contraception, with only one randomised trial on acne, which tested a combination pill rather than levonorgestrel alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acne (disease) |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 11 of 11) |
| Number of SAHPRA Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Levonorgestrel is a progestin, and the literature describes it as having some residual androgenic activity (PMID 7825629). This makes it a less favourable choice for acne than anti-androgenic progestins.

Combined hormonal contraceptives can improve acne by raising sex hormone-binding globulin and lowering free testosterone. This benefit is mainly attributed to the oestrogen component and to anti-androgenic progestins such as chlormadinone acetate (PMID 21895044). Levonorgestrel-releasing intrauterine systems and implants are progestin-only, and acne has been reported with them as a side effect rather than a treatment effect.

The high TxGNN score is therefore plausible at most for combination products. It is not supported for levonorgestrel as a single agent.

Evidence level L5 applies because no cited study evaluates levonorgestrel on its own for acne. The one acne trial (PMID 12196750) tested ethinyl estradiol plus levonorgestrel, a combination product.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | Randomised placebo-controlled trial | J Am Acad Dermatol | Low-dose oral contraceptive (ethinyl estradiol 20 µg + levonorgestrel 100 µg) in moderate acne; a combination product, so the effect of levonorgestrel alone cannot be separated |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | Ethinylestradiol/chlormadinone acetate was more effective than ethinylestradiol/levonorgestrel for mild-to-moderate papulopustular acne |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | Dermatological benefits of an anti-androgenic combined pill in acne, hirsutism and seborrhoea |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | Androgenic properties of progestins, including 19-carbon progestins such as levonorgestrel |
| [30088446](https://pubmed.ncbi.nlm.nih.gov/30088446/) | 2018 | Review | Curr Drug Targets | Steroid interactions in sebum production and the role of hormones in acne |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | Levonorgestrel-releasing intrauterine systems: contraception and endometrial effects |
| [11091988](https://pubmed.ncbi.nlm.nih.gov/11091988/) | 2000 | Review | Obstet Gynecol Clin North Am | Levonorgestrel contraceptive implants |
| [8489751](https://pubmed.ncbi.nlm.nih.gov/8489751/) | 1993 | Review | Ann Med | Hormonal intrauterine devices releasing levonorgestrel |

---

## South Africa Market Information

Levonorgestrel is marketed in South Africa. All 11 SAHPRA registrations found are valid single-ingredient oral tablets. The records carry no approved-indication text.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/21.8.2/0808 | Medilevo 1,5 Mg | Tablet | Not recorded |
| Reg. No. 51/21.8.2/0584 | Femilevo 1,5Mg | Tablet | Not recorded |
| Reg. No. 49/21.8.2/0574 | Vonel | Tablet | Not recorded |
| Reg. No. 33/18.8/0054 | Loette 28 | Tablet | Not recorded |
| Reg. No. 36/21.8.2/0212 | Plan B | Tablet | Not recorded |

---

## Safety Considerations

Product warnings and contraindications from the label are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Conditions for which caution is indicated in the compiled safety data** (not label text) include:
- Hypertension and other cardiovascular risk
- Liver disease and gallbladder disease
- Kidney disease
- Diabetes mellitus and hyperglycaemia
- Blood coagulation disorders
- Hypertriglyceridaemia
- Epilepsy
- Asthma
- Systemic lupus erythematosus
- Hypothyroidism
- Porphyria
- Hypercalcaemia
- Anxiety and related mood disorders

**Drug interactions:** 100 interactions were found, mostly of moderate severity. Examples include:
- **Antidiabetic agents:** acarbose, canagliflozin, dapagliflozin, ertugliflozin, exenatide, liraglutide, linagliptin, nateglinide, and several insulins
- **Other:** aprepitant, clotrimazole, glycerol phenylbutyrate, linaclotide

Blood glucose monitoring is advisable when levonorgestrel is combined with antidiabetic drugs.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by direct evidence. No trials exist for levonorgestrel alone in acne, and the available literature suggests a benefit, if any, comes from the oestrogen component or from anti-androgenic progestins. Levonorgestrel's residual androgenic activity argues against its use for this purpose.

**To proceed, the following is needed:**
- Studies that isolate the effect of levonorgestrel from combination products in acne
- Mechanism-of-action data
- Label warnings and contraindications from the SAHPRA Professional Information
- A risk-benefit comparison against established acne treatments, including anti-androgenic hormonal options
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

