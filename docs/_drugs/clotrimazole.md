---
layout: default
title: Clotrimazole
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clotrimazole: predicted new indication Acne (evidence level L5). Approved use: Tinea pedis, tinea corporis, cutaneous candidiasis…"
monitor_inn: "Clotrimazole"
predicted_indications: ["acne (disease)", "vulvovaginitis", "postmenopausal atrophic vaginitis", "trichomonal vulvovaginitis", "Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease"]
---

# Clotrimazole
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

## Clotrimazole: From Superficial Fungal Infections to Acne (Top Prediction) and Vulvovaginitis (Best-Supported Prediction)
{: .text-alpha }

## One-Sentence Summary

Clotrimazole is a topical azole antifungal, originally used for tinea infections, cutaneous candidiasis, pityriasis versicolor, and oral and vulvovaginal candidiasis.
The TxGNN model's top-ranked prediction is **acne**, but this has very weak support (one suspended multi-drug trial and no publications). The best-supported prediction is **vulvovaginitis**, with **12 clinical trials** and **20 publications**. This indication largely overlaps with the existing labelled use for vulvovaginal candidiasis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, cutaneous candidiasis, pityriasis versicolor, oral candidiasis, vulvovaginal candidiasis (SAHPRA indication text is not available in the data compiled for this report) |
| Predicted New Indication | Acne (rank 1, TxGNN score 99.86%); vulvovaginitis (rank 2, TxGNN score 99.59%) is discussed as the best-supported prediction |
| TxGNN Prediction Score | Acne: 99.86%; Vulvovaginitis: 99.59% |
| Evidence Level | Acne: L4; Vulvovaginitis: L1 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 7 |
| Recommended Decision | Acne: Hold; Vulvovaginitis: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Clotrimazole is, however, a well-known azole antifungal. Azoles inhibit fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis and so inhibits fungal growth. Its efficacy in superficial fungal infections is established, and mechanistically it may be applicable to other conditions in which yeasts or dermatophytes play a role.

**Acne (rank 1).** Clotrimazole has some reported anti-inflammatory activity, and *Malassezia* or *Candida* may contribute to acne-like folliculitis. The link is weak. The only trial tests a fixed combination of beclomethasone, gentamicin and clotrimazole, so clotrimazole's own contribution cannot be separated out.

**Vulvovaginitis (rank 2).** This is essentially the same as the labelled vulvovaginal candidiasis use, so it is on-label rather than true repurposing. The mechanism applies directly, since *Candida* is the main pathogen. Evidence for non-*Candida* vulvovaginitis (bacterial, trichomonal) is weak.

**Other predictions (ranks 3 to 10).** Most are either dermatophyte infections involving hair or deeper tissue (tinea profunda, Majocchi granuloma, ectothrix and endothrix infections, scalp or beard dermatophytosis), which generally need systemic therapy, or have no mechanistic link (postmenopausal atrophic vaginitis, which is caused by oestrogen deficiency). Superficial mycosis (rank 9) largely overlaps with already approved uses.

---

## Clinical Trial Evidence

Trials for the top-ranked prediction (acne) and the best-supported prediction (vulvovaginitis).

### Acne

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Fixed combination of beclomethasone, gentamicin and clotrimazole cream in contaminated dermatosis. Clotrimazole's contribution cannot be isolated, and no results are available. |

### Vulvovaginitis (up to 10 most relevant)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Completed | 466 | Investigator-blinded non-inferiority study of a clotrimazole 500 mg ovule vs vaginal tablet in vaginal candidiasis |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Completed | 1,524 | Single-dose tinidazole plus fluconazole vs longer metronidazole plus clotrimazole courses for vaginal discharge in West African women (clotrimazole in the comparator regimen) |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | Recruiting | 264 | Clotrimazole plus lactulose vs clotrimazole alone (Canesten) in candidal vulvovaginitis; no results yet |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Completed | 150 | Head-to-head comparison of dequalinium chloride 10 mg with clotrimazole 100 mg in vulvovaginal candidiasis |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Completed | 240 | Clotrimazole vaginal tablet vs fluconazole in severe vulvovaginal candidiasis |
| [NCT03115073](https://clinicaltrials.gov/study/NCT03115073) | Phase 2/3 | Completed | 84 | Dose-escalation study of Candiplus vs 1% clotrimazole vaginal cream (clotrimazole as active control) |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Completed | 140 | Clotrimazole vaginal tablets with or without oral Lactobacillus to prevent recurrent vulvovaginal candidiasis |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | N/A | Completed | 1,033 | Post-marketing safety questionnaire study of Empecid L cream (clotrimazole 1%) |
| [NCT02248506](https://clinicaltrials.gov/study/NCT02248506) | Phase 4 | Completed | 56 | Epidemiological study of clinical and microbiological evolution after treatment of acute vulvovaginal candidiasis |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | Completed | 100 | Cumin seed extract vaginal suppositories in candidal vulvovaginitis (clotrimazole probably the comparator) |

A further two trials were identified for this indication (NCT03024502 and NCT04292704), in which clotrimazole is only a comparator or background therapy. One (NCT02907307) was withdrawn with no participants enrolled.

No SANCTR or PACTR identifiers are available in the data compiled for this report.

---

## Literature Evidence

Vulvovaginitis (up to 10 most relevant; randomised trials prioritised, then reviews and other studies).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | Am J Obstet Gynecol | Single 500 mg clotrimazole vaginal tablet vs 6-day 100 mg course in 199 women with candidal vulvovaginitis |
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complement Ther Med | *Prangos ferulacea* vaginal cream vs clotrimazole vaginal cream in vulvovaginal candidiasis |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | Probiotics and lactoferrin as maintenance treatment in recurrent vulvovaginal candidiasis |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | Clinical study | Obstet Gynecol | Double-blind study of 42 women: clotrimazole 500 mg suppositories weekly for 2 weeks achieved clinical remission in 90.4% of recurrent cases |
| [32992877](https://pubmed.ncbi.nlm.nih.gov/32992877/) | 2020 | Systematic review | Pharmaceuticals (Basel) | More than 45 years of clinical experience with clotrimazole for vulvovaginal candidosis |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Review | J Appl Microbiol | Clotrimazole as a pharmaceutical: past, present and future |
| [39432168](https://pubmed.ncbi.nlm.nih.gov/39432168/) | 2024 | Retrospective study | Mycopathologia | Retrospective analysis of 1,303 severe cases comparing clotrimazole and fluconazole regimens; a three-dose regimen improved efficacy |
| [41350226](https://pubmed.ncbi.nlm.nih.gov/41350226/) | 2025 | Cohort | Pharmacoepidemiol Drug Saf | Large claims database study of major congenital malformations after first-trimester topical antifungal exposure |
| [40886781](https://pubmed.ncbi.nlm.nih.gov/40886781/) | 2025 | In vitro/ex vivo | Pharmacol Res | Classic azole antifungals, including clotrimazole, affect steroidogenic activity in a human term placenta model |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | Boric acid for recurrent vulvovaginal candidiasis |

No publications were found for acne.

---

## South Africa Market Information

Clotrimazole has 7 valid SAHPRA registrations, all single-ingredient products. Approved indication text is not available in the data compiled for this report. Essential Medicines List (EML) inclusion status is also not available.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 28/20.2.2/0419 | Clomaderm | Cream | Refer to the Professional Information (PI) |
| Reg. No. 30/20.2.2/0416 | Fungispor | Cream | Refer to the PI |
| Reg. No. 30/20.2.2/0111 | Canesten Duopak | Kit | Refer to the PI |
| Reg. No. 27/20.2.2/0285 | Medaspor Vag | Vaginal cream (Vcr) | Refer to the PI |
| Reg. No. R/13.4.1/38 | Lotriderm | Cream | Refer to the PI |

Two further registrations are not listed above: Pinaspor V (Reg. No. 33/20.2.2/0267, vaginal cream) and Medaspor Topical (Reg. No. 28/20.2.2/0119, cream).

---

## Safety Considerations

**Contraindication-related disease associations (from the knowledge graph, not label text):** adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary haemorrhagic telangiectasia, peripheral vascular disease, intermittent claudication and peripheral arterial disease. These are likely to be driven by corticosteroid components in combination products and should be checked against the PI.

**Drug Interactions:** 100 interactions were found. The most notable **Major** interactions are with fentanyl, alfentanil, hydrocodone and amiodarone. **Moderate** interactions include abemaciclib, paclitaxel, acalabrutinib, nifedipine, amlodipine, apixaban, aprepitant, alprazolam, aliskiren, alfuzosin, estradiol, levonorgestrel and norethisterone. Minor interactions include dolutegravir and amphotericin B. These are likely to be most relevant when clotrimazole has meaningful systemic exposure.

**Pregnancy considerations:** A 2025 claims database study examined major congenital malformations after first-trimester topical antifungal exposure, and a 2025 placental model showed that azoles affect steroidogenic activity. First-trimester use therefore warrants attention.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (vulvovaginitis); Hold (acne and the other predictions)**

**Rationale:**
- Vulvovaginitis is supported by completed Phase 3 RCTs and Phase 4 trials, plus decades of clinical experience. It is essentially an on-label use, so it is not true repurposing.
- Acne (the top-ranked prediction) rests on a single suspended combination-product trial, with no publications and no way to isolate clotrimazole's effect. The deep or hair-based dermatophyte infections generally need systemic therapy. Postmenopausal atrophic vaginitis has no mechanistic link.

**To proceed, the following is needed:**
- Review of the SAHPRA Professional Information for warnings, contraindications and approved indications (the safety data compiled for this report are incomplete)
- Mechanism of action data
- For non-*Candida* vulvovaginitis (bacterial or trichomonal), controlled trials of clotrimazole as a single agent, since nitroimidazoles remain standard of care
- A pregnancy safety assessment, particularly for first-trimester use
- For acne, a trial isolating clotrimazole's effect from the steroid and antibiotic components, if this direction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

