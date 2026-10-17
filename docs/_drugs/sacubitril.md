---
layout: default
title: Sacubitril
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sacubitril: predicted new indication Brain small vessel disease 1 with or without ocular anomalies (evidence level L5). Approved use: Not available"
monitor_inn: "Sacubitril"
predicted_indications: ["brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "rheumatoid arthritis", "hemoglobinopathy", "sclerosing cholangitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "homozygous familial hypercholesterolemia", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Sacubitril
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

# Sacubitril: From an Unspecified Original Indication to Brain Small Vessel Disease 1 (Top TxGNN Prediction)

## One-Sentence Summary

Sacubitril is a neprilysin inhibitor that is registered in South Africa as a single-ingredient tablet, but the data compiled for this report contain no approved indication text for it.
The TxGNN model's top-ranked prediction is **brain small vessel disease 1 with or without ocular anomalies**, supported by **0 clinical trials** and **1 publication**, and that publication does not address this disease.
The best-supported prediction in the data is **diabetic nephropathy** (rank 3), with **1 clinical trial** and **15 publications**. It is covered in detail below as a more informative alternative.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the SAHPRA registration data contain no approved indication text) |
| Predicted New Indication | Brain small vessel disease 1 with or without ocular anomalies (rank 1) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

**Other predictions in the data (top 10 by TxGNN score):**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|---|---|---|---|---|
| 1 | Brain small vessel disease 1 with or without ocular anomalies | 99.58% | L5 | Hold |
| 2 | Autosomal dominant familial haematuria-retinal arteriolar tortuosity-contractures syndrome | 99.57% | L5 | Hold |
| 3 | Diabetic nephropathy | 99.50% | L3 | Research question |
| 4 | Rheumatoid arthritis | 99.35% | L5 | Hold |
| 5 | Haemoglobinopathy | 99.18% | L5 | Hold |
| 6 | Sclerosing cholangitis | 98.92% | L5 | Hold |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.92% | L5 | Hold |
| 8 | Homozygous familial hypercholesterolaemia | 98.87% | L5 | Hold |
| 9 | Partial deletion of the short arm of chromosome 16 | 98.85% | L5 | Hold |
| 10 | Beta-thalassaemia with other manifestations | 98.83% | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available for sacubitril in the data compiled for this report. Sacubitril is a prodrug that inhibits neprilysin, an enzyme that breaks down natriuretic peptides, and it is used together with the angiotensin receptor blocker valsartan. The data compiled for this report do not describe its original approved indication.

**Rank 1 (brain small vessel disease 1):** No direct mechanistic link has been established. The only retrieved paper concerns sacubitril/valsartan in systemic right ventricular failure, not cerebral small vessel disease or COL4A1-related disease. The high score is a computational prediction only. Neprilysin inhibition and angiotensin receptor blockade could theoretically influence cerebrovascular function, but this is speculative.

**Rank 3 (diabetic nephropathy):** This is the one prediction with a plausible mechanism and supporting data.
- Neprilysin inhibition raises natriuretic peptides (ANP/BNP), promoting natriuresis, vasodilation and anti-fibrotic effects. Valsartan blocks the AT1 receptor and reduces pressure within the kidney's filtering units (glomeruli).
- Preclinical studies in diabetic rodent models report reduced oxidative stress, NF-κB-mediated inflammation and fibrosis, plus gut microbiota modulation.
- Heart failure data in patients with diabetes support renal tolerability. However, neprilysin inhibition may also affect the handling of other substrates, so renal outcomes in diabetic kidney disease need confirmation.

**Other predictions (ranks 2 and 4-10):** No credible mechanistic link or supporting studies were identified. These predictions are computational only.

## Clinical Trial Evidence

No clinical trials are registered for the rank 1 prediction (brain small vessel disease 1). For the rank 3 prediction (diabetic nephropathy), one trial was identified:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Unknown | 297 | Hyper-Save: randomised, controlled, multicentre study comparing sacubitril/valsartan with valsartan over 12 weeks in patients with mild to moderate essential hypertension and type 2 diabetic nephropathy. No results are available. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

## Literature Evidence

**Rank 1 (brain small vessel disease 1):** Only one paper was retrieved, and it does not address this disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37169551](https://pubmed.ncbi.nlm.nih.gov/37169551/) | 2023 | Cohort | Heart | Tolerability and effects of sacubitril/valsartan in adults with systemic right ventricular failure. This is not about cerebral small vessel disease. |

**Rank 3 (diabetic nephropathy), selected publications:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical study (randomised groups; design not confirmed) | Int Immunopharmacol | Nifedipine controlled-release plus sacubitril/valsartan versus plus valsartan in 112 diabetic nephropathy patients with hypertension. |
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT (PARADIGM-HF) | Lancet Diabetes Endocrinol | Effect of neprilysin inhibition on renal function in patients with type 2 diabetes and chronic heart failure. |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical study | Diabetes Metab Syndr Obes | BOLD-MRI evaluation of renal effects of sacubitril/valsartan in type 2 diabetes. |
| [34734359](https://pubmed.ncbi.nlm.nih.gov/34734359/) | 2023 | Review | Heart Fail Rev | Disease-modifying drugs in diabetic patients with heart failure with reduced ejection fraction. |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on the pillars of therapy that slow diabetic nephropathy progression. |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preclinical (rat) | Diabetes Metab Syndr Obes | Sacubitril/valsartan slowed early diabetic nephropathy in rats via inhibition of the NLRP3 inflammasome pathway. |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | Preclinical (mouse) | Front Endocrinol | Improved diabetic kidney disease and modulated gut microbiota in mice. |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Preclinical (mouse) | Am J Physiol Renal Physiol | Differential effects versus valsartan in db/db and KKAy mice. |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preclinical (rat) | PeerJ | LCZ696 reduced oxidative stress, NF-κB-mediated inflammation and glomerulosclerosis in diabetic rats. |
| [30909895](https://pubmed.ncbi.nlm.nih.gov/30909895/) | 2019 | Preclinical (rat) | Cardiovasc Diabetol | Sacubitril plus valsartan attenuated glomerular and tubular injury in the Zucker obese rat. |

A further 5 publications on this prediction were retrieved but are not listed here. Rheumatoid arthritis (rank 4) has one retrieved paper, a case report on golimumab-associated myocarditis that does not evaluate sacubitril.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/7.6/1019 | Vymada 50 Mg | Tablet (oral) | Not available in the data compiled for this report |

Status: valid, single-ingredient product. No information on Essential Medicines List (EML) inclusion was available in the data compiled for this report.

## Safety Considerations

**Drug Interactions** (6 moderate-level interactions identified in the DDInter database):
- Nitisinone
- Rosuvastatin
- Simvastatin
- Cobicistat
- Revefenacin
- Alpelisib

Statin co-prescription is particularly relevant in patients with diabetes or cardiovascular disease.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available in the data compiled for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, brain small vessel disease 1)

**Rationale:**
- The rank 1 prediction has no relevant clinical trials, only one unrelated publication and no identified mechanism, so it rests on the model score alone (L5).
- Diabetic nephropathy (L3) is the only prediction with a plausible mechanism and supporting data. It is best treated as a research question, because the sole trial is Phase 4 with unknown status and no results, and most supporting studies are preclinical.

**To proceed, the following is needed:**
- The SAHPRA Professional Information, to establish the approved indication, warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Results from NCT06501651, and ideally a Phase 3 RCT of sacubitril/valsartan in diabetic kidney disease with renal outcomes.
- Renal and potassium safety monitoring plans for patients with diabetes and chronic kidney disease.
- A review of the interactions with statins and other co-medications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

