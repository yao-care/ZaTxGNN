---
layout: default
title: Cholecalciferol
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cholecalciferol (Vitamin D3): From Vitamin D Deficiency to Renal Osteodystrophy

## One-Sentence Summary

Cholecalciferol (Vitamin D3) is the naturally occurring, inactive prohormone form of vitamin D, serving as a precursor to calcitriol — the active hormone governing intestinal calcium absorption, phosphorus homeostasis, and parathyroid function.
The TxGNN model predicts potential new efficacy across 7 indications, all linked to calcium–phosphorus dysregulation; **renal osteodystrophy** (rank 6) carries the strongest evidence base with **32 clinical trials** and **20 publications**, including direct cholecalciferol supplementation studies in chronic kidney disease.
Evidence reaches **Level L2**, supporting a **Proceed with Guardrails** recommendation — the most actionable finding in this Evidence Pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D deficiency; prevention and treatment of rickets and metabolic bone disease |
| Featured Predicted Indication | Renal osteodystrophy *(see note below)* |
| TxGNN Prediction Score | 99.11% (rank 6 of 7 predictions) |
| Evidence Level | L2 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on indication selection:** The TxGNN rank 1 prediction is *familial isolated hypoparathyroidism due to impaired PTH secretion* (score 99.79%), but this carries no supporting clinical trials or publications (Evidence Level L5, Hold). This report focuses on **renal osteodystrophy** as the clinically most actionable and evidenced prediction. All seven predictions are summarised in the table below.

---

## Why is This Prediction Reasonable?

Cholecalciferol undergoes two sequential hydroxylations to become biologically active: first in the liver (producing 25-hydroxycholecalciferol, or calcidiol), then in the kidney (by 1α-hydroxylase, producing 1,25-dihydroxycholecalciferol — calcitriol). Calcitriol binds the vitamin D receptor (VDR) in the intestine to promote calcium and phosphorus absorption, in the parathyroid gland to suppress PTH secretion, and in bone to regulate osteoblast and osteoclast activity. While detailed mechanistic data from DrugBank is currently unavailable (Data Gap DG002), this activation pathway is firmly established in clinical pharmacology literature.

The core pathophysiology of renal osteodystrophy directly implicates this pathway. As chronic kidney disease (CKD) progresses, declining nephron mass impairs renal 1α-hydroxylase activity, reducing calcitriol production. The resulting calcitriol deficiency triggers hypocalcaemia, secondary hyperparathyroidism, and disordered bone mineralisation — giving rise to the spectrum of skeletal lesions (osteitis fibrosa, osteomalacia, adynamic bone disease) collectively termed renal osteodystrophy or CKD–Mineral and Bone Disorder (CKD-MBD). Cholecalciferol supplementation addresses this by replenishing the 25(OH)D substrate pool, supporting whatever residual 1α-hydroxylase capacity remains, and may additionally improve calcium absorption via direct intestinal 25(OH)D pathways.

The mechanistic logic is directly confirmed in clinical trial design: NCT00285467 directly compared **cholecalciferol** against active vitamin D analogue doxercalciferol in CKD stages 3–4 secondary hyperparathyroidism (n=55), and NCT00752401 (VITA-D, Phase 3, n=200) evaluated cholecalciferol supplementation in vitamin D-deficient kidney transplant recipients. It is important to note that in more advanced CKD (stages 4–5 or dialysis), the impaired renal 1α-hydroxylase step means **active analogues** (calcitriol, alfacalcidol) are often preferred over cholecalciferol — the specific CKD stage and residual kidney function are therefore critical determinants of cholecalciferol's clinical benefit.

---

## All TxGNN Predictions — Summary

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|----------------|----------------|
| 1 | Familial isolated hypoparathyroidism due to impaired PTH secretion | 99.79% | L5 | Hold |
| 2 | Acromesomelic dysplasia, Campailla Martinelli type | 99.78% | L5 | Hold |
| 3 | Craniofacial conodysplasia | 99.75% | L5 | Hold |
| 4 | Dahlberg-Borer-Newcomer syndrome (HDR syndrome) | 99.73% | L4 | Hold |
| 5 | Hypophosphatemic rickets | 99.20% | L3 | Research Question |
| **6** | **Renal osteodystrophy** | **99.11%** | **L2** | **Proceed with Guardrails** |
| 7 | Renal tubular acidosis | 99.06% | L4 | Research Question |

---

## Clinical Trial Evidence — Renal Osteodystrophy

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | N/A | Completed | 55 | **Direct cholecalciferol trial**: Head-to-head comparison of cholecalciferol vs. doxercalciferol for secondary hyperparathyroidism in CKD stages 3–4; the only direct cholecalciferol comparator study in this disease area |
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: Randomised, placebo-controlled Phase 3 study of cholecalciferol substitution in vitamin D-deficient kidney transplant recipients — evaluates GFR, acute rejection rate, infection incidence, and CRP |
| [NCT00560300](https://clinicaltrials.gov/study/NCT00560300) | Phase 2 | Completed | 61 | Regulation of bone formation in renal osteodystrophy: calcitriol vs. doxercalciferol and two phosphate binders in children with kidney failure; results published |
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Phase 4 | Unknown | 60 | Vitamin D2 ± doxercalciferol to correct bone mineralisation defects in paediatric peritoneal dialysis patients with established secondary hyperparathyroidism |
| [NCT01149291](https://clinicaltrials.gov/study/NCT01149291) | Observational | Completed | 511 | Large post-marketing study (18 months, Turkey) evaluating selective VDR activators for secondary hyperparathyroidism in ESRD haemodialysis patients; PTH suppression trajectories documented |
| [NCT03063190](https://clinicaltrials.gov/study/NCT03063190) | Phase 4 | Withdrawn | 0 | Cholecalciferol supplementation in CKD patients with restless leg syndrome — withdrawn before enrolment, but confirms clinical community's recognition of this research direction |
| [NCT03960437](https://clinicaltrials.gov/study/NCT03960437) | Phase 2 | Completed | 22 | Etelcalcetide effects on bone tissue properties and calcification propensity in ESKD with hyperparathyroidism; vitamin D used as standard background treatment |
| [NCT00527085](https://clinicaltrials.gov/study/NCT00527085) | Phase 2 | Completed | 45 | Multicentre, randomised, double-blind, placebo-controlled, 12-month study of AMG 073 (calcimimetic) on renal osteodystrophy in haemodialysis patients with secondary hyperparathyroidism; bone biopsy endpoints |
| [NCT00859612](https://clinicaltrials.gov/study/NCT00859612) | N/A | Completed | 464 | Renal Osteodystrophy — A Fresh Approach: DXA vs QCT for bone loss diagnosis in CKD-5; prevalence of low bone turnover; large-scale diagnostic validation study |
| [NCT01675089](https://clinicaltrials.gov/study/NCT01675089) | Phase 4 | Completed | 34 | Zoledronic acid to prevent bone loss in the first year post-kidney transplantation; vitamin D as adjunct therapy |

---

## Literature Evidence — Renal Osteodystrophy

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9684690](https://pubmed.ncbi.nlm.nih.gov/9684690/) | 1998 | Review | Artificial Organs | Comprehensive diagnostic and treatment algorithms for all renal osteodystrophy subtypes; identifies native vitamin D deficiency as a direct cause of osteomalacia in CKD |
| [12944733](https://pubmed.ncbi.nlm.nih.gov/12944733/) | 2003 | Review | Blood Purification | Pathogenesis and treatment of osteitis fibrosa vs adynamic bone disease; documents calcitriol deficiency as central driver justifying vitamin D supplementation |
| [12386262](https://pubmed.ncbi.nlm.nih.gov/12386262/) | 2002 | Review | Nephrol Dial Transplant | Mechanisms of secondary hyperparathyroidism and renal osteodystrophy; decreased calcitriol and reduced VDR density identified as principal pathophysiological drivers |
| [2747771](https://pubmed.ncbi.nlm.nih.gov/2747771/) | 1989 | Review | N Engl J Med | Classic NEJM review establishing the spectrum of renal osteodystrophy and the foundational role of vitamin D metabolism in its pathogenesis |
| [3909812](https://pubmed.ncbi.nlm.nih.gov/3909812/) | 1985 | Review | Am J Med Sci | Early authoritative review linking altered vitamin D, calcium, phosphorus, and PTH metabolism in renal failure to uremic bone disease |
| [8512774](https://pubmed.ncbi.nlm.nih.gov/8512774/) | 1993 | Review | Curr Opin Rheumatol | Renal osteodystrophy and hypercalcaemia management; clinical guidance on selecting vitamin D supplementation strategies |
| [1338454](https://pubmed.ncbi.nlm.nih.gov/1338454/) | 1992 | Review | J Nutr Sci Vitaminol | Cellular mechanisms of hyperparathyroidism in uraemia; documents parathyroid resistance to physiological calcitriol concentration and the rationale for supplementation |
| [203416](https://pubmed.ncbi.nlm.nih.gov/203416/) | 1977 | Review | Clin Endocrinol | Foundational vitamin D metabolism review establishing the hepatic and renal hydroxylation pathway — mechanistic basis for understanding CKD-related cholecalciferol limitations |
| [3085581](https://pubmed.ncbi.nlm.nih.gov/3085581/) | 1986 | Review | Ann Rev Med | Aluminium accumulation and renal osteodystrophy; multifactorial CKD bone disease and the interplay with vitamin D supplementation |
| [16970258](https://pubmed.ncbi.nlm.nih.gov/16970258/) | 2006 | Review | Saudi J Kidney Dis Transplant | Modern overview of renal osteodystrophy spectrum and treatment options; vitamin D supplementation strategies for dialysis and pre-dialysis CKD patients |

---

## South Africa Market Information

Cholecalciferol (Vitamin D3, DrugBank DB00169) is currently **not marketed** in South Africa and has **zero SAHPRA registrations** on record.

Healthcare professionals should note:

- **Section 21 Access Pathway**: Unregistered medicines may be accessed for individual patients or institutional use via SAHPRA's Section 21 authorisation process.
- **OTC Supplement Availability**: Cholecalciferol is widely available as an over-the-counter nutritional supplement in many countries; the regulatory classification for clinical or hospital use in South Africa requires clarification.
- **Active Analogues**: Calcitriol (1,25(OH)₂D₃) and alfacalcidol (1α-hydroxyvitamin D₃) — which bypass the impaired renal hydroxylation step in CKD — should be checked separately for current SAHPRA registration status, as they are standard-of-care agents in CKD-MBD management.
- **WHO EML**: Cholecalciferol is included on the WHO Model List of Essential Medicines under nutritional products, which may support a regulatory or formulary motivation.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Formal safety data including SAHPRA-approved warnings, contraindications, and drug-drug interaction listings were not available in the current evidence pack (Data Gaps DG001 and DG002). A complete safety review is required prior to any clinical use.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(Renal Osteodystrophy, Evidence Level L2)*

**Rationale:**
Renal osteodystrophy is mechanistically linked to cholecalciferol through the well-characterised CKD-related impairment of renal 1α-hydroxylase activity, and direct cholecalciferol supplementation trials in CKD and kidney transplant populations confirm both clinical plausibility and research community interest. The remaining six predictions span Evidence Levels L5–L4 (Hold or Research Question only) and require further basic and clinical data before any actionable step can be taken.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001**: Obtain formal SAHPRA warnings and contraindications for cholecalciferol — essential before any safety screening
- **Resolve Data Gap DG002**: Retrieve full MOA data from DrugBank to confirm VDR-binding pharmacology and enzyme-pathway interactions
- **Define the target patient population**: Specify CKD stage thresholds (e.g., stages 3–4 vs. stages 5/dialysis) where native cholecalciferol supplementation is preferred over active analogues, based on residual 1α-hydroxylase capacity and baseline 25(OH)D levels
- **Registration pathway**: Assess feasibility of full SAHPRA marketing authorisation vs. ongoing Section 21 case-by-case access; engage Regulatory Affairs
- **South African clinical study**: Evaluate registering a locally relevant study with SANCTR (South African National Clinical Trials Register) or PACTR (Pan African Clinical Trials Registry) to generate South African-specific efficacy and safety data in CKD-MBD
- **Safety monitoring protocol**: Serial serum calcium, phosphate, iPTH, 25(OH)D, creatinine, and urinary calcium — establish local reference thresholds appropriate for South African CKD populations
- **Essential Medicines Committee engagement**: Evaluate potential inclusion in Standard Treatment Guidelines for CKD-MBD management alongside existing active vitamin D analogue recommendations

---

*This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. YMYL disclaimer: This content is generated for research purposes; clinical decisions must be made by qualified healthcare professionals in accordance with current SAHPRA-approved guidelines.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

