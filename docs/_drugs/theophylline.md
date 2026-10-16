---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 445
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma (also bronchitis…"
---

# Theophylline
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

# Theophylline: From Asthma to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator used for asthma and other chronic airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **no clinical trials** are registered for this use and none of the **19 publications** retrieved tested theophylline for thrombosis, so the prediction is not yet supported by real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (also bronchitis, pulmonary emphysema and other bronchial or lung disease) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

*The original indications come from the TxGNN knowledge graph. The SAHPRA records compiled for this report do not include approved-indication text.*

---

## Why is This Prediction Reasonable?

Theophylline is a non-selective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. In the airways, these actions relax smooth muscle and dampen inflammation, which underlies its use in asthma and COPD.

A theoretical argument can be made for thrombosis. PDE inhibition raises cAMP inside platelets, and higher cAMP generally reduces platelet aggregation. However, adenosine normally also inhibits platelets, so blocking adenosine receptors works against any antiplatelet effect. No study in the compiled data shows a direct link between theophylline and thrombosis prevention or treatment.

The retrieved literature does not fill this gap. Most papers concern platelet biomarker assays, ticlopidine pharmacokinetics (a different drug), or theophylline detection methods. The high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the 19 publications tested theophylline in thrombotic disease. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone (a different PDE inhibitor) reduced human platelet aggregation by raising cAMP and interacted with adenosine's effect. Mechanistically relevant, but not theophylline. |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Thromboxane A2 and prostacyclin in platelets and atherosclerosis. Prostacyclin acts through adenylate cyclase and cAMP. |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Pharmacokinetic review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet drug. Not about theophylline. |
| [8318681](https://pubmed.ncbi.nlm.nih.gov/8318681/) | 1993 | Case report/review | J Am Soc Nephrol | Treatment of posttransplant erythrocytosis. Only loosely related. |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Assay method | British Journal of Haematology | Platelet factor 4 radioimmunoassay. Theophylline is only a component of the blood collection anticoagulant. |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Clinical report | Minerva Cardioangiologica | A theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy. No abstract available. |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Clinical report | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinic ester in cerebral and peripheral angiopathies. No abstract available. |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | Clinical report | Annali di Ottalmologia | Theophylline nicotinate in retinal vascular disease, assessed by electroretinography. No abstract available. |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observational | Cor et Vasa | T-lymphocyte subsets in vascular disease, using theophylline-resistance as a cell marker. Not a treatment study. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical method | Analytica Chimica Acta | Aptasensor for detecting theophylline. Not relevant to efficacy. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| G721 (OM) | Alcophyllin | Syrup | Not stated in the data compiled |
| S/10.2/126 | Nuelin liquid | Syrup | Not stated in the data compiled |
| M/10.2/0533 | Theophen | Syrup | Not stated in the data compiled |
| G892 (OM) | Adco-Metaxol | Suspension | Not stated in the data compiled |
| N/10.1/98 | Theophen Compound Elixir | Syrup | Not stated in the data compiled |

All 8 registrations are valid single-ingredient products, and none are cancelled. Only the first 5 are shown above. The other 3 are Alcophyllex (G720 (OM)), Diatussin/biotussin (G1276 (OM)) and Actophlem (W/10.1/0194). All registered forms are oral liquids (syrup or suspension).

---

## Safety Considerations

- **Contraindications (knowledge-graph data, not label text):** The TxGNN knowledge graph links theophylline to the following conditions as possible contraindications. These should be checked against the SAHPRA Professional Information (PI).
  - Cardiovascular: hypertension.
  - Hepatic and renal: liver failure, liver disease, kidney disease, gallbladder disease.
  - Neurological and psychiatric: epilepsy, anxiety and neurotic disorders, dysthymic disorder, psychotic disorders (including schizophreniform and schizoaffective disorder).
  - Haematological: thrombocytopenia, neutropenia, agranulocytosis.
  - Endocrine and metabolic: hypothyroidism (including myxedema), diabetes mellitus, diabetic ketoacidosis, porphyria.
  - Other: peptic ulcer disease, open-angle glaucoma, benign prostatic hyperplasia, dermatitis herpetiformis, pyoureter.
- **Drug Interactions:** 100 interactions were found. Of the 20 listed in the data:
  - **Major:** bupropion.
  - **Moderate:** the H2 blockers famotidine, ranitidine and cimetidine; the proton pump inhibitors omeprazole and rabeprazole; the corticosteroids hydrocortisone, dexamethasone, betamethasone, triamcinolone and budesonide; the antibiotics clarithromycin, doxycycline, tetracycline and minocycline; activated charcoal; and the bowel preparations picosulfuric acid and polyethylene glycol with electrolytes.
  - **Minor:** ephedrine, including nasal ephedrine.
- Theophylline has a narrow therapeutic index, and its clearance varies with smoking, age and comorbidity. Serum level monitoring is generally needed.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (L5). There are no clinical trials and no publications testing theophylline for thrombosis. The adenosine-antagonist action may also work against any antiplatelet benefit. Theophylline's narrow therapeutic index and its many drug interactions add risk to any new use, especially alongside antithrombotic drugs.

**To proceed, the following is needed:**
- Laboratory data showing whether theophylline at tolerable serum concentrations inhibits platelet aggregation or thrombus formation.
- Clinical safety and efficacy data in thrombotic patients, starting with early-phase studies.
- SAHPRA Professional Information (warnings, contraindications and approved indications) to start safety screening.
- Detailed mechanism of action data to support the analysis.

Of the other predictions generated for theophylline, only obstructive lung disease has substantial trial evidence, including Phase 3 studies. That is an existing use of theophylline rather than true repurposing, so it should be assessed separately.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

