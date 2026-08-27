---
layout: default
title: Pyridoxine
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Pyridoxine
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

# Pyridoxine: From Dietary Vitamin B6 Supplementation to Confirmatory Treatment of Vitamin B6 Deficiency Disorder

## One-Sentence Summary

Pyridoxine (Vitamin B6, DrugBank DB00165) is an essential coenzyme precursor for amino acid, neurotransmitter, and homocysteine metabolism. TxGNN generated 10 candidate indications for this drug, but the model's own rationale flags 9 of them (including the top-ranked "gonococcal urethritis") as likely **knowledge-graph artifacts with no plausible pharmacological mechanism**. The only candidate with real evidentiary support is **Vitamin Deficiency Disorder**, backed by **~50 clinical trials** and **20 publications** — though this represents confirmation of an already-known use rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No formal registration data on file; as a nutrient, pyridoxine is used for dietary supplementation and correction of Vitamin B6 deficiency |
| Predicted New Indication | Vitamin Deficiency Disorder (Vitamin B6 deficiency) |
| TxGNN Prediction Score | 85.50% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is not yet on file for this candidate (data gap DG002). Based on established pharmacology, pyridoxine is converted in the intestine to pyridoxal 5'-phosphate (PLP), the active coenzyme form required by enzymes throughout amino acid metabolism, neurotransmitter synthesis (GABA, serotonin), one-carbon/homocysteine metabolism, and mitochondrial function. Deficiency of this cofactor produces well-characterized clinical syndromes: peripheral neuropathy, pyridoxine-dependent epilepsy, sideroblastic anemia, and elevated homocysteine.

This predicted indication is therefore not a novel repurposing hypothesis in the classic sense — it is a **confirmatory match**: the drug is being "predicted" for the deficiency state it is already known to treat. The clinically meaningful open question is not mechanistic plausibility (which is well established) but why the product carries no current SAHPRA registration and "Not Marketed" status in South Africa, which should be clarified as a regulatory/commercial gap rather than an efficacy concern.

By contrast, the other 9 TxGNN candidates for this drug (gonococcal urethritis, Ureaplasma urethritis, urinary tract infection, uterine inflammatory disease, xanthogranulomatous pyelonephritis, congenital prothrombin deficiency, toxocariasis, toxascariasis, anisakiasis) have no supporting mechanism — pyridoxine has no known antimicrobial, antiparasitic, or coagulation-factor activity — and the model's own annotations describe these as probable graph-proximity artifacts (e.g., confusion between "vitamin"-class nodes and Vitamin K–dependent clotting, or urethritis/inflammation node adjacency). These should be treated as **Hold**, not evaluated further without independent evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01795170](https://clinicaltrials.gov/study/NCT01795170) | N/A | Withdrawn (enrollment 0) | 0 | Directly targeted pyridoxine-dependent epilepsy via dietary lysine restriction; withdrawn before enrollment, no data generated |
| [NCT01128244](https://clinicaltrials.gov/study/NCT01128244) | Phase 2/3 | Completed | 13 | Direct study of Vitamin B6 effects on one-carbon metabolism; established PLP cutoffs for nutritional adequacy vs. marginal deficiency |
| [NCT04054505](https://clinicaltrials.gov/study/NCT04054505) | N/A | Completed | 275 | Nutraceutical supplementation shown to raise circulating serum vitamin, mineral, and amino acid levels |
| [NCT03720249](https://clinicaltrials.gov/study/NCT03720249) | N/A | Unknown | 100 | Compound nutrients (folic acid, B6, B12, betaine, zinc) tested for lowering plasma homocysteine in hyperhomocysteinemic adults |
| [NCT00642408](https://clinicaltrials.gov/study/NCT00642408) | Phase 4 | Completed | 1,370 | Micronutrient supplementation including pyridoxine for prevention of intrauterine growth retardation, Burkina Faso |
| [NCT00004495](https://clinicaltrials.gov/study/NCT00004495) | N/A | Completed | 84 | Folic acid therapy for hyperhomocysteinemia in hemodialysis patients; assessed need for co-supplementation with pyridoxine and B12 |
| [NCT00626223](https://clinicaltrials.gov/study/NCT00626223) | N/A | Completed | 341 | 5-methyltetrahydrofolate vs. oral folate in ESRD patients; B6/B12 levels monitored alongside survival and inflammation outcomes |
| [NCT06772220](https://clinicaltrials.gov/study/NCT06772220) | N/A | Recruiting | 150 | Open-label B-vitamin therapy for homocysteine correction in levodopa-treated Parkinson's disease patients |
| [NCT03004807](https://clinicaltrials.gov/study/NCT03004807) | N/A | Completed | 41 | Multivitamin/mineral supplement (Centrum Silver) evaluated for improving micronutrient status in older men |
| [NCT04160767](https://clinicaltrials.gov/study/NCT04160767) | Phase 4 | Unknown | 90 | Probiotic supplementation evaluated against Vitamin B6, B12, folate and homocysteine status in celiac disease patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30671974](https://pubmed.ncbi.nlm.nih.gov/30671974/) | 2019 | Review | J Inherit Metab Dis | Comprehensive review of disorders affecting Vitamin B6 metabolism and the central role of PLP as an enzyme cofactor |
| [24035968](https://pubmed.ncbi.nlm.nih.gov/24035968/) | 2013 | Review | Pak J Pharm Sci | Reviews Vitamin B6 deficiency diseases (seizures, epileptic encephalopathy) and analytical detection methods |
| [25137514](https://pubmed.ncbi.nlm.nih.gov/25137514/) | 2014 | Review | J Clin Neuromuscul Dis | Systematic review of neuropathy evidence from both pyridoxine deficiency and excess |
| [23622403](https://pubmed.ncbi.nlm.nih.gov/23622403/) | 2013 | Review | Handb Clin Neurol | Describes four inborn errors leading to Vitamin B6-dependent seizures, incl. antiquitin deficiency |
| [38703598](https://pubmed.ncbi.nlm.nih.gov/38703598/) | 2024 | Review | Seizure | Reviews increased functional pyridoxine deficiency and seizure risk in Parkinson's disease |
| [30267523](https://pubmed.ncbi.nlm.nih.gov/30267523/) | 2018 | Cohort | Psychiatr Danub | Serum homocysteine, pyridoxine, folate and B12 evaluated in children with ADHD |
| [32443822](https://pubmed.ncbi.nlm.nih.gov/32443822/) | 2020 | Cohort | Medicina (Kaunas) | Vitamin deficiencies (incl. B6) linked to co-occurring GI/behavioral symptoms in autism spectrum disorder |
| [33958192](https://pubmed.ncbi.nlm.nih.gov/33958192/) | 2021 | Case Report | Am J Med Sci | Isolated pyridoxine deficiency presenting as muscle spasms in a Type 2 diabetes patient |
| [27810990](https://pubmed.ncbi.nlm.nih.gov/27810990/) | 2017 | Case Report | Nutr Clin Pract | Thiamin, pyridoxine, Vitamin D and carotene deficiency in a malnourished patient after Billroth II gastrectomy |
| [2192608](https://pubmed.ncbi.nlm.nih.gov/2192608/) | 1990 | Review | Ann N Y Acad Sci | Review of pyridoxine's neurobiological roles |

---

## South Africa Market Information

Pyridoxine currently holds **no SAHPRA registrations** on file (0 licenses; market status: Not Marketed). No registered product name, dosage form, or approved indication text is available to summarize.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between pyridoxine and Vitamin B6 deficiency disorder is well established and not in scientific dispute; the evidence base (L2, multiple relevant trials and reviews) supports confirmatory use. However, guardrails are needed because this drug is not currently marketed or registered in South Africa, and safety/labelling documentation is missing.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information / package insert, including warnings and contraindications (currently a Blocking data gap — DG001)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (High-priority data gap — DG002)
- Clarification of why pyridoxine has no current SAHPRA registration despite established therapeutic use (regulatory gap vs. commercial decision)
- No further action recommended on the other 9 TxGNN-predicted indications for this drug (gonococcal urethritis, Ureaplasma urethritis, urinary tract infection, uterine inflammatory disease, xanthogranulomatous pyelonephritis, congenital prothrombin deficiency, toxocariasis, toxascariasis, anisakiasis) — each lacks a plausible mechanism and is flagged by the model itself as likely a knowledge-graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

