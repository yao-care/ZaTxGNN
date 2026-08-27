---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Sacubitril
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

## One-Sentence Summary

Sacubitril is the neprilysin-inhibitor component of the Sacubitril/Valsartan (ARNI) combination, whose approved use is heart failure with reduced ejection fraction. Among 10 TxGNN-predicted indications for this candidate, only **Diabetic Nephropathy** is backed by real clinical and mechanistic evidence — **2 clinical trials** and **17 publications** — while the model's top-ranked hit is flagged in the evidence pack itself as a likely false-positive match. Sacubitril (DB09292) as a single entity is currently **not registered with SAHPRA** and has no South African market presence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in South African registration data (0 SAHPRA licenses); per the evidence pack, Sacubitril is a component of Sacubitril/Valsartan (Entresto), approved elsewhere for heart failure with reduced ejection fraction |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed (未上市) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Sacubitril is flagged as a data gap at the drug level. However, the evidence pack's own literature-derived rationale indicates that Sacubitril (activated to LBQ657) inhibits neprilysin, reducing degradation of natriuretic peptides (ANP/BNP/CNP). This enhances natriuretic-peptide signalling, promoting natriuresis, lowering intraglomerular pressure, and counteracting excessive RAAS activation and renal fibrosis — mechanisms with direct relevance to diabetic kidney disease pathophysiology.

Heart failure and diabetic nephropathy frequently co-exist and share overlapping haemodynamic and neurohormonal pathways (RAAS overactivation, sodium retention, glomerular hyperfiltration). The approved use of Sacubitril/Valsartan in heart failure — a condition with well-documented renal cross-talk — provides a plausible mechanistic bridge to a renoprotective effect in diabetic nephropathy, consistent with the multiple preclinical and clinical observations in the evidence pack.

**Note on TxGNN ranking:** the single highest-scoring prediction (brain small vessel disease with ocular anomalies, score 99.58%) was reviewed and found to have no supporting literature — the 19 retrieved publications are unrelated case/review reports on congenital ophthalmic and genetic syndromes, none mentioning Sacubitril or neprilysin. The evidence pack classifies this as a TxGNN embedding similarity artefact ("noise match") and assigns it Evidence Level L5 / Hold. The same applies to 7 other ranked candidates (autosomal dominant familial hematuria syndrome, rheumatoid arthritis, hemoglobinopathy, sclerosing cholangitis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, homozygous familial hypercholesterolemia, chromosome 16p deletion, beta-thalassemia), all L5/Hold with zero supporting trials or literature. Diabetic Nephropathy (rank 3, score 99.50%) is therefore the only candidate in this pack with a credible evidence base and is used as the basis for this report.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A | Completed | 268 | Non-interventional, retrospective real-world EMR analysis of Sacubitril/Valsartan prescribing patterns in Indian HFrEF patients over 1.5 years; not designed around diabetic nephropathy as a primary endpoint, so provides only indirect renal-outcome signal |
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | Prospective, randomized, controlled multicentre study comparing Sacubitril/Valsartan vs Valsartan in patients with mild-to-moderate essential hypertension and Type 2 diabetic nephropathy, 12-week treatment, 2:1 randomization; no data generated yet |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT (PARADIGM-HF) | Lancet Diabetes Endocrinol | Neprilysin inhibition assessed for renal function effects in Type 2 diabetic patients with chronic HF on target-dose RAAS inhibitors; the strongest clinical-trial-derived evidence in this pack |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Clinical/comparative cohort | Int Immunopharmacol | Sacubitril/Valsartan + nifedipine combination improved renal function outcomes vs valsartan + nifedipine in 112 diabetic nephropathy patients with hypertension |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Clinical cohort (BOLD-MRI) | Diabetes Metab Syndr Obes | Imaging-based (BOLD-MRI) evaluation of renal protective effects of Sacubitril/Valsartan in Type 2 diabetic patients |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on therapeutic pillars slowing diabetic kidney disease progression, situates neprilysin inhibition among newer mechanism-based options |
| [34441977](https://pubmed.ncbi.nlm.nih.gov/34441977/) | 2021 | Review | J Clin Med | Reviews diabetes-heart failure pathophysiology, including diabetic nephropathy as a shared comorbidity pathway |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Curr Hypertens Rep | Reviews newer antihypertensive drug classes, including ARNI, for mitigating hypertensive target-organ (renal) damage |
| [34734359](https://pubmed.ncbi.nlm.nih.gov/34734359/) | 2023 | Review | Heart Fail Rev | Reviews disease-modifying drugs, including Sacubitril/Valsartan, in diabetic HFrEF patients |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Rev Med Suisse | Reviews the potential role of Sacubitril/Valsartan in Type 2 diabetes, including renal effects |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preclinical (rat) | Diabetes Metab Syndr Obes | Sacubitril/Valsartan slowed early diabetic nephropathy progression via NLRP3 inflammasome pathway inhibition |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preclinical (rat) | PeerJ | LCZ696 (Sacubitril/Valsartan) reduced oxidative stress, NF-κB-mediated inflammation and glomerulosclerosis in diabetic rats |

## South Africa Market Information

Sacubitril (DB09292) currently has **no SAHPRA registrations** and is not marketed in South Africa as a single entity. No product listings, dosage forms, or approved indication text are available in the evidence pack for this drug in the South African market.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. Key warnings, contraindications, and drug-drug interaction data for Sacubitril are marked as an unresolved (Blocking-severity) data gap in this evidence pack, meaning a preliminary safety assessment cannot yet be completed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Sacubitril has no SAHPRA registration and no South African market presence, and the underlying Professional Information/safety data needed for even a preliminary safety review is an unresolved Blocking-severity gap.
- The only credible predicted indication (Diabetic Nephropathy) has supportive but not yet definitive evidence — no completed trial with diabetic nephropathy as a primary endpoint; the sole purpose-designed Phase 4 RCT (NCT06501651) has not yet started recruiting.

**To proceed, the following is needed:**
- SAHPRA-approved PI covering warnings, contraindications, and drug interactions (currently Blocking data gap, DG001)
- Confirmation of whether Sacubitril/Valsartan (Entresto) as a combination product holds separate SAHPRA registration in South Africa
- Full mechanism-of-action documentation for Sacubitril (currently High-severity data gap, DG002)
- Results from NCT06501651 once recruitment and follow-up are complete
- No further action needed on the 8 other TxGNN-ranked candidates in this pack (including the top-scoring "brain small vessel disease" prediction) — all lack any supporting trial or literature evidence and are assessed as low-confidence model artefacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

