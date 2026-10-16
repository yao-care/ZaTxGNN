---
layout: default
title: Cholecalciferol
parent: Model Prediction Only (L5)
nav_order: 118
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Cholecalciferol: predicted new indication Renal osteodystrophy (evidence level L5). Approved use: Osteoporosis, postmenopausal osteoporosis, rickets, osteomalacia…"
monitor_inn: "CHOLECALCIFEROL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cholecalciferol: From Osteoporosis and Rickets to Renal Osteodystrophy

## One-Sentence Summary

Cholecalciferol (vitamin D3) is originally used for vitamin D deficiency and bone and mineral disorders such as rickets, osteomalacia, osteoporosis and hypoparathyroidism.
The TxGNN model predicts it may be useful for **renal osteodystrophy**, the bone disease of chronic kidney disease.
Currently **2 clinical trials** and **20 publications** support this direction, and no trial results are available.

Note: the highest-scoring prediction by TxGNN is familial isolated hypoparathyroidism due to impaired PTH secretion (99.79%). It has no trials or relevant literature, and overlaps with an existing indication, so it is not taken forward. The most actionable prediction is renal osteodystrophy, the only candidate with clinical trial evidence, and this report focuses on it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis, postmenopausal osteoporosis, rickets, osteomalacia, vitamin D deficiency, hypoparathyroidism (from the knowledge graph; SAHPRA indication text is not available) |
| Predicted New Indication | Renal osteodystrophy |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L2 (see note below) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

Evidence level note: the only Phase 3 RCT (VITA-D) has an unknown status and no results, so it cannot support L1. A completed but small, non-phase trial supports L2 at best.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cholecalciferol is a pro-hormone. It is converted in the liver to 25-hydroxyvitamin D and in the kidney to the active 1,25-dihydroxyvitamin D (calcitriol). This regulates calcium and phosphate absorption and parathyroid hormone (PTH) production.

In chronic kidney disease (CKD), vitamin D deficiency is very common and contributes to secondary hyperparathyroidism and mineral-bone disorder, which together produce renal osteodystrophy. Replenishing native vitamin D stores may reduce PTH through extrarenal and residual renal 1-alpha-hydroxylation. This is closely related to the drug's established use in osteomalacia and rickets. Whether native cholecalciferol is sufficient in advanced CKD, where active analogues are often used, remains debated in the literature.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Phase 3 | Unknown | 200 | VITA-D: placebo-controlled RCT of cholecalciferol in vitamin D-deficient kidney transplant recipients, assessing graft function, rejection, infections and CRP in the first year. No results available. |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | Not designated | Completed | 55 | Cholecalciferol versus doxercalciferol for secondary hyperparathyroidism in CKD stages 3-4. |

No SANCTR or PACTR identifiers were found in the data compiled for this report.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Observational study | Biomedicines | Efficacy and safety of high-dose cholecalciferol in haemodialysis patients with 25(OH)D deficiency |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | Observational study | Medicina (Kaunas) | Haemodialysis patients may benefit from cholecalciferol targeting high 25(OH)D; effect on CKD-MBD |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Review | Nefrologia | Role of native vitamin D in pre-dialysis CKD remains unclear |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Review | Nutrients | Vitamin D effects on bone and cardiovascular system in CKD and renal transplant recipients |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Prospective controlled study | Clin Nephrol | Effect of vitamin D sterols on bone histology in pre-dialysis patients |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Workshop report | Am J Kidney Dis | National Kidney Foundation report on vitamin D in CKD stages 3-4; management remains controversial |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Review | Kidney Int Suppl | Kidney bone disease and mortality in CKD; role of vitamin D and minerals |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/22.1/0508 | Cernevit | Infusion | Not available in the data compiled for this report |

This is one valid single-ingredient registration, an injectable. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypercalcaemia, nephrocalcinosis, hyperparathyroidism, kidney disease, liver disease, sarcoidosis, phosphorus metabolism disorders, and primary hyperoxaluria, among others. Several of these are relevant to CKD populations, so calcium and phosphate monitoring is essential.
- **Drug interactions (56 recorded):** Major interactions with other vitamin D agents (calcifediol, calcitriol, dihydrotachysterol, doxercalciferol), which risk additive hypercalcaemia. Moderate interactions include thiazide diuretics (bendroflumethiazide, chlorothiazide, chlorthalidone), digoxin and digitoxin, barbiturates, carbamazepine, and bile acid sequestrants (cholestyramine, colestipol, colesevelam). Cimetidine is a minor interaction.
- **Literature safety signals:** vitamin D3 overdose has been reported in a child with distal renal tubular acidosis misdiagnosed as rickets, and hypercalciuria and nephrocalcinosis are risks of excessive dosing.

Please also refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications, which were not available in the data compiled for this report. Report adverse drug reactions to SAHPRA.

## Other Predictions Reviewed

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Familial isolated hypoparathyroidism (impaired PTH secretion) | 99.79% | L5 | Overlaps with an existing indication; no trials or literature. Hold. |
| Acromesomelic dysplasia, Campailla-Martinelli type | 99.78% | L5 | No clear mechanistic link; likely graph artefact. Hold. |
| Craniofacial conodysplasia | 99.75% | L5 | No established link to vitamin D pathways. Hold. |
| Dahlberg-Borer-Newcomer syndrome | 99.73% | L5 | Retrieved literature is non-specific. Hold. |
| Hypophosphataemic rickets | 99.20% | L4 | Reviews and case reports only; active analogues plus phosphate are standard, so native cholecalciferol has a limited role. Research question. |
| Renal tubular acidosis | 99.06% | L4 | Benefit limited to associated rickets and osteomalacia; overdose signal. Research question. |

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Renal osteodystrophy is the only prediction with trial-level evidence and a plausible mechanism (correcting vitamin D deficiency to limit secondary hyperparathyroidism). However, the sole Phase 3 trial has unknown status and no results, the completed trial is small, and the supporting literature is mostly reviews and observational studies.

**To proceed, the following is needed:**
- Results or status confirmation for NCT00752401, and ideally an adequately powered RCT in CKD with bone or PTH outcomes
- SAHPRA Professional Information for warnings, contraindications and approved indications of the registered product (Cernevit is a multivitamin infusion, so a suitable single-agent cholecalciferol product should be identified)
- Mechanism of action data from DrugBank
- A monitoring plan for calcium, phosphate, PTH and 25(OH)D, with avoidance of concurrent active vitamin D analogues
- Check for EML status and for local SANCTR/PACTR trial registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

