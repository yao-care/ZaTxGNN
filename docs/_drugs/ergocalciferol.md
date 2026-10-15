---
layout: default
title: Ergocalciferol
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

# Ergocalciferol: From Vitamin D Deficiency and Bone Disorders to Renal Osteodystrophy

## One-Sentence Summary

Ergocalciferol (vitamin D2) was originally used for vitamin D deficiency disorders and related bone and calcium-metabolism conditions such as rickets, osteomalacia, osteoporosis and hypoparathyroidism.
The TxGNN model's top-ranked prediction is **familial isolated hypoparathyroidism due to impaired PTH secretion**, but this has **no supporting trials or publications**. The best-supported predictions are **renal osteodystrophy** (**1 clinical trial**, **20 publications**) and **hypophosphatemic rickets** (**15 publications**, no trials). Both are discussed below.

Note: the predictions are ranked by TxGNN score, not by strength of evidence. This report therefore presents the top-ranked prediction in the overview and then the better-supported candidates in detail.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indications | Vitamin D deficiency disorders, rickets, osteomalacia, osteoporosis, hypoparathyroidism, hereditary hypophosphatemic rickets (from the TxGNN knowledge graph; no approved indication text is available from the SAHPRA records) |
| Predicted New Indication (top-ranked) | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.85% |
| Evidence Level (top-ranked) | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision (top-ranked) | Hold |

### Summary of the Ten Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|---|---|---|---|---|
| 1 | Familial isolated hypoparathyroidism (impaired PTH secretion) | 99.85% | L5 | Hold |
| 2 | Acromesomelic dysplasia, Campailla-Martinelli type | 99.83% | L5 | Hold |
| 3 | Renal tubular acidosis | 99.81% | L4 | Hold |
| 4 | Craniofacial conodysplasia | 99.81% | L5 | Hold |
| 5 | Dahlberg-Borer-Newcomer syndrome | 99.81% | L5 | Hold |
| 6 | Hypophosphatemia | 99.72% | L3 | Hold (research question) |
| 7 | **Renal osteodystrophy** | 99.67% | L2 | **Proceed with Guardrails** |
| 8 | **Hypophosphatemic rickets** | 99.67% | L3 | **Proceed with Guardrails** |
| 9 | Calcium-alkali syndrome | 99.46% | L5 | Hold (safety concern) |
| 10 | Vitamin D-dependent rickets | 99.39% | L4 | Hold (research question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ergocalciferol is a form of vitamin D (vitamin D2). It is converted in the liver and kidney to active 1,25-dihydroxyvitamin D, which regulates calcium and phosphate absorption and bone mineralisation. Its efficacy in vitamin D deficiency and rickets is established, and mechanistically it may be applicable to other disorders of calcium, phosphate and bone metabolism.

**Top-ranked prediction (familial isolated hypoparathyroidism).** Ergocalciferol is already listed for hypoparathyroidism in general, so the mechanism (restoring calcium balance through vitamin D activation) is plausible. However, there are no trials or publications specific to this familial form. The high score probably reflects closeness to the existing hypoparathyroidism indication rather than new evidence.

**Renal osteodystrophy (rank 7).** In chronic kidney disease (CKD), nutritional vitamin D repletion raises 25-OH vitamin D, which can support calcitriol production. It may help control secondary hyperparathyroidism and bone mineral disturbance. Supporting material includes a paediatric comparison of calcitriol versus ergocalciferol, a randomised comparison in CKD stages 3 to 5, and consensus documents on native vitamin D in CKD.

**Hypophosphatemic rickets (rank 8).** This is closely related to the existing indication of hereditary hypophosphatemic rickets. Vitamin D, usually combined with oral phosphate, improves bone mineralisation. Active analogues such as calcitriol, and burosumab, are now generally preferred over native ergocalciferol.

**Predictions with weak or no mechanistic support.**
- Acromesomelic dysplasia and craniofacial conodysplasia: no mechanistic link or evidence was identified. Treat these as computational signals only.
- Dahlberg-Borer-Newcomer syndrome: the retrieved papers concern vitamin D in general and appear to be keyword matches.
- Renal tubular acidosis: vitamin D may support bone complications, but the two retrieved papers do not test ergocalciferol.
- Vitamin D-dependent rickets: type I involves a defect in conversion to calcitriol, so native ergocalciferol is generally inadequate at standard doses.
- Calcium-alkali syndrome: this condition is driven by hypercalcaemia, which vitamin D would be expected to worsen. The high score is likely spurious.

---

## Clinical Trial Evidence

Only one of the ten predicted indications has a registered trial (renal osteodystrophy). No trials are registered for the top-ranked indication. No SANCTR or PACTR identifiers were available.

| Trial Number | Indication | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT01799317](https://clinicaltrials.gov/study/NCT01799317) | Renal osteodystrophy | Phase 4 | Unknown | 60 | Tests whether vitamin D2 (ergocalciferol) combined with doxercalciferol, or doxercalciferol alone, corrects the mineralisation defect in paediatric patients with secondary hyperparathyroidism on peritoneal dialysis. No results are available, and it is unclear whether ergocalciferol is the central intervention. |

---

## Literature Evidence

Publications are listed for the better-supported indications. Reviews and cohort studies dominate; no Phase 3 RCT evidence was provided for any predicted indication.

### Renal osteodystrophy

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27401037](https://pubmed.ncbi.nlm.nih.gov/27401037/) | 2016 | RCT (open-label, n=204) | Eur J Pharmacol | Ergocalciferol versus calcitriol for controlling CKD mineral bone disorder in stage 3 to 5 CKD |
| [3877585](https://pubmed.ncbi.nlm.nih.gov/3877585/) | 1985 | Comparative clinical study | Clin Nephrol | Childhood renal osteodystrophy treated with calcitriol (8 children) or ergocalciferol (7 children); mixed bone histology outcomes |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Expert consensus | Am J Kidney Dis | National Kidney Foundation workshop on vitamin D in CKD stages 3 to 4; management remains controversial |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D (including ergocalciferol) in pre-dialysis CKD remains unclear |
| [28873969](https://pubmed.ncbi.nlm.nih.gov/28873969/) | 2017 | Recommendations | Nephrol Dial Transplant | Practice recommendations for native vitamin D therapy in children with CKD stages 2 to 5 |

### Hypophosphatemic rickets

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Comparative clinical study (11 children) | N Engl J Med | Bone response to phosphate salts alone, or combined with ergocalciferol or calcitriol, in vitamin D-resistant rickets |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Rickets types and treatment with vitamin D and analogues |
| [38365463](https://pubmed.ncbi.nlm.nih.gov/38365463/) | 2024 | Review | Best Pract Res Clin Endocrinol Metab | Vitamin D deficiency or resistance and hypophosphatemia |
| [1464657](https://pubmed.ncbi.nlm.nih.gov/1464657/) | 1992 | Case series | J Clin Endocrinol Metab | Severe tertiary hyperparathyroidism in three girls on high-dose phosphate plus ergocalciferol or calcitriol |

### Other indications (limited evidence)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7452873](https://pubmed.ncbi.nlm.nih.gov/7452873/) | 1981 | Case report | JAMA | Hypophosphatemia: tumour-induced osteomalacia did not respond to ergocalciferol until the tumour was removed |
| [21503197](https://pubmed.ncbi.nlm.nih.gov/21503197/) | 2011 | Review | Korean J Pediatr | Vitamin D-dependent rickets type I |
| [233695](https://pubmed.ncbi.nlm.nih.gov/233695/) | 1978 | Case series | J Clin Endocrinol Metab | Familial syndrome of reduced sensitivity to 1,25-dihydroxyvitamin D |

Renal tubular acidosis has only two indirect papers (a 2026 case report on juvenile nephronophthisis and a 1964 report on schistosomal uropathy), neither of which tests ergocalciferol. The publications retrieved for Dahlberg-Borer-Newcomer syndrome are general vitamin D papers, not disease-specific evidence. No literature was found for the other predicted indications.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G2667 (Act 101/1965) | Gericomplex | Capsule | Not available in the data compiled for this report |
| 41/10.2.1/0849 | Spiriva Respimat inhaler 60 doses | Inhaler | Not available in the data compiled for this report |

Both registrations are valid single-ingredient entries. The registration record for Spiriva Respimat, an inhaler, should be verified against the SAHPRA register, because it is an unexpected match for an oral vitamin D agent. Essential Medicines List (EML) status could not be determined from the available data.

---

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from drug-disease relationship data, not from the product label):
- Calcium and vitamin D-related: hypercalcaemia, hyperparathyroidism, osteitis fibrosa, nephrocalcinosis, phosphorus metabolism disorders, sarcoidosis, primary hyperoxaluria
- Organ disease: kidney disease, liver disease, gallbladder disease, gastritis
- Cardiometabolic: hypertension, atrial fibrillation, diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia (including familial)
- Haematological and iron-related: blood coagulation disorders, sickle cell anaemia, hereditary persistence of fetal haemoglobin, hereditary haemochromatosis, haemosiderosis, iron metabolism disorders, Wilson disease
- Cancers: female breast carcinoma, prostate cancer

Several of these (for example kidney disease and hypercalcaemia) overlap with the proposed new uses, which makes careful monitoring essential.

**Drug interactions** (55 recorded in total; main ones shown):
- **Major**: other vitamin D agents (cholecalciferol, calcifediol, calcitriol, doxercalciferol), with a risk of additive hypercalcaemia
- **Moderate**: thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone), barbiturates (amobarbital, butalbital), carbamazepine, rifabutin, bile acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer, magnesium oxide, digoxin, topical calcipotriol and calcitriol
- **Minor**: cimetidine

**Product label information:** warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available for this report. Please refer to the PI and report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction; Proceed with Guardrails for renal osteodystrophy and hypophosphatemic rickets**

**Rationale:**
- The top-ranked prediction (familial isolated hypoparathyroidism) has no trials or publications and is plausible only because ergocalciferol is already used for hypoparathyroidism in general, so it stays at Hold.
- Renal osteodystrophy (L2) has one randomised comparison, one Phase 4 trial of unknown status and several consensus documents, but no confirmed Phase 3 RCT, and findings on hard bone outcomes are mixed. Hypophosphatemic rickets (L3) rests on older clinical studies and reviews, and active vitamin D analogues and burosumab are now generally preferred. Both can proceed only with guardrails.
- Hypophosphatemia and vitamin D-dependent rickets remain research questions. Calcium-alkali syndrome carries a safety concern, and the remaining predictions have no supporting evidence.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Confirmation of the SAHPRA registration details, including approved indications and EML status
- For renal osteodystrophy: the outcome and status of NCT01799317, and comparative evidence against active vitamin D analogues in South African CKD populations
- For hypophosphatemic rickets: a comparison with current standard care, and a monitoring plan covering calcium, phosphate, PTH and urinary calcium to avoid hypercalcaemia, nephrocalcinosis and tertiary hyperparathyroidism
- A review of interacting medicines, particularly other vitamin D products and thiazide diuretics
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

