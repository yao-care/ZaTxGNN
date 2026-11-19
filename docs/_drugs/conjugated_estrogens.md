---
layout: default
title: Conjugated Estrogens
parent: Model Prediction Only (L5)
nav_order: 147
evidence_level: L5
indication_count: 9
monitor_inn: "Conjugated estrogens"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis", "rheumatoid arthritis", "heparin cofactor 2 deficiency", "Prinzmetal angina", "hemoglobinopathy", "thrombophilia"]
last_modified_at: 2026-11-20
description: "Conjugated Estrogens: predicted new indication migraine disorder (evidence level L5). In South Africa: 1 SAHPRA registration (0 valid)"
---

# Conjugated Estrogens
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Conjugated estrogens: Estrogen receptor agonist → migraine disorder
{: .text-alpha }

## One-Sentence Summary

Conjugated estrogens are a mixed-estrogen hormone product. The TxGNN model predicts they may be relevant to **migraine disorder**, but there are **no registered clinical trials** and only **5 publications** (reviews and cohort studies on hormones and migraine), so the evidence is indirect and preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | migraine disorder |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| South Africa Market Status | Not marketed (no current registration: 1 of 1 cancelled by SAHPRA, or not on the SAHPRA register and discontinued in or absent from the current Medicine Price Registry) |
| Number of SAHPRA Registrations | 1 (valid: 0) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for conjugated estrogens: "Endogenous estrogens are largely responsible for the development and maintenance of the female reproductive system and secondary sexual characteristics. Although circulating estrogens exist in a dynamic equilibrium of metabolic interconversions, estradiol is the principal intracellular human estrogen and is substantially more potent than its metabolites, estrone and estriol, at the receptor level. […] Thus, estrone and the sulfate-conjugated form, estrone sulfate, are the most abundant circulating estrogens in postmenopausal women." ([DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5), label version 2025-05-30; accessed 2026-11-19.) Conjugated estrogens are a mixed-estrogen preparation that acts on oestrogen receptors.

Migraine is closely linked to oestrogen fluctuations, such as oestrogen-withdrawal migraine and perimenstrual or perimenopausal patterns. Stable oestrogen exposure may reduce attack frequency in some women. However, the effect is inconsistent: oral or fluctuating dosing can worsen migraine, so any response is likely to depend on dose, route and patient. Migraine with aura also carries an added ischaemic stroke risk with oestrogen exposure, which is a key safety concern.

The cited publications address hormones and migraine broadly (including hormone replacement therapy in postmenopausal women). None of them is a trial of conjugated estrogens specifically in migraine. For this reason the evidence level is L5 and not higher.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29521155](https://pubmed.ncbi.nlm.nih.gov/29521155/) | 2018 | Review | Climacteric | Hormonal fluctuations, especially around the menopausal transition, are important migraine triggers; hormone exposure can change the course of migraine with and without aura |
| [11306204](https://pubmed.ncbi.nlm.nih.gov/11306204/) | 2001 | Cohort | Maturitas | Evaluated how hormone replacement therapy influences the course of primary headaches in postmenopausal women |
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Cohort | Headache | Compared three oral HRT schemes and their differing effects on migraine in postmenopausal women |
| [8309263](https://pubmed.ncbi.nlm.nih.gov/8309263/) | 1994 | Review | Mayo Clin Proc | Compared transdermal and oral oestrogen therapy across groups of women; not specific to migraine |
| [14195735](https://pubmed.ncbi.nlm.nih.gov/14195735/) | 1964 | Case series | Medizinische Klinik | Early report on conjugated estrogens for climacteric disorders; not specific to migraine |

---

## South Africa Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| 27/21.8.2/0021 | Estracombi Tts | Pad | Not on SAHPRA register; discontinued in MPR |

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Most of those listed are moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, acetohexamide, albiglutide, dulaglutide), aprepitant, clarithromycin and clotrimazole. Cimetidine is a minor interaction.
- **Thrombotic risk**: Oestrogens are prothrombotic. Several lower-ranked model predictions (antithrombin deficiency, thrombophilia, factor V-related thrombosis) are safety signals and not therapeutic opportunities.
- **Migraine with aura**: Oestrogen exposure adds ischaemic stroke risk in this group.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No study directly tests conjugated estrogens in migraine disorder, and the available literature shows inconsistent effects, with worsening possible depending on dose and route. Stroke risk in migraine with aura is a significant safety concern.

**To proceed, the following is needed:**
- Controlled clinical studies of conjugated estrogens in migraine, defining dose, route and patient subgroup
- Mechanism of action data
- SAHPRA Professional Information warnings and contraindications for formal safety screening
- A stroke and thrombosis risk assessment, particularly for migraine with aura

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Premarin Vaginal (conjugated estrogens) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96609623-528e-4aba-cabe-7254aed816d5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

