---
layout: default
title: Iron Sucrose
parent: Model Prediction Only (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Iron Sucrose
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

# Iron Sucrose: From Hyperphosphatemia to Primary Hyperoxaluria

## One-Sentence Summary

Iron sucrose is an intravenous iron preparation, and the data compiled for this report list hyperphosphatemia as its original indication in the knowledge graph.
The TxGNN model predicts it may be effective for **primary hyperoxaluria** (score 98.8%), but there are **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction is model-derived only and has no mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperphosphatemia (from the knowledge graph; no approved indication text is available in the SAHPRA records compiled) |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the data compiled for this report. Iron sucrose is an intravenous iron replacement product used mainly for iron deficiency, particularly in chronic kidney disease (CKD) and dialysis populations.

Primary hyperoxaluria is a genetic disorder of hepatic glyoxylate metabolism (AGXT, GRHPR and HOGA1 defects) that causes oxalate overproduction. Iron sucrose does not act on these pathways, so **no mechanistic link is evident**. The high score reflects a graph-based association only and should not be read as evidence of efficacy.

For context, other predictions were also reviewed:
- **Hyperparathyroidism (rank 8)** is the only prediction with some indirect literature (L4), set in CKD and dialysis populations. It is a research question, not a treatment signal.
- **Pancreatitis (rank 2)**: the retrieved literature suggests a possible safety signal (iron-related pancreatic beta cell toxicity in vitro), not a benefit.
- **Familial hyperphosphatemic tumoral calcinosis (ranks 3 and 7)** likely appears because of its shared hyperphosphatemia association with the original indication. No evidence supports iron sucrose here, and some IV iron products are associated with hypophosphatemia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for primary hyperoxaluria. No SANCTR or PACTR identifiers were found.

---

## Literature Evidence

Currently no related literature available for primary hyperoxaluria.

For reference, the most relevant indirect literature for the rank 8 prediction (hyperparathyroidism) is below. It does not show that iron sucrose treats this condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34629085](https://pubmed.ncbi.nlm.nih.gov/34629085/) | 2021 | RCT protocol | Trials | Oral polysaccharide iron complex versus iron sucrose in haemodialysis patients (iron repletion, not hyperparathyroidism) |
| [35482713](https://pubmed.ncbi.nlm.nih.gov/35482713/) | 2022 | Clinical/animal study | Nephrol Dial Transplant | Ferric citrate versus IV iron sucrose on mineral, bone and iron markers in a rat CKD-MBD model |
| [32444112](https://pubmed.ncbi.nlm.nih.gov/32444112/) | 2020 | Review | Mol Aspects Med | Overview of intravenous iron therapy for iron deficiency |
| [11929146](https://pubmed.ncbi.nlm.nih.gov/11929146/) | 2002 | Clinical study | Perit Dial Int | Low-dose IV iron sucrose regimen in peritoneal dialysis patients |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A 50/2.6.5/0687 | Innofer Injection | Injection | Not available in the data compiled |
| 45/8.3/0550 | Zypiron 20 | Injection | Not available in the data compiled |

Both registrations are valid single-ingredient injectable products. Essential Medicines List (EML) inclusion status was not available in the data compiled.

---

## Safety Considerations

- **Drug Interactions**: 42 interactions were identified. The main ones are listed below.
  - **Major**: Dimercaprol.
  - **Moderate**:
    - Tetracyclines (doxycycline, minocycline, tetracycline) and chloramphenicol.
    - Vitamin D analogues (cholecalciferol, calcifediol, ergocalciferol, dihydrotachysterol, doxercalciferol).
    - Bisphosphonates (alendronic acid, risedronic acid, ibandronate).
    - ACE inhibitors (benazepril, captopril, enalapril).
    - Thyroid agents (levothyroxine, liothyronine, porcine thyroid).
    - Other iron products.
- **Prediction-specific signal**: Literature (PMID 24349622, in vitro) suggests that pharmacologically relevant concentrations of intravenous iron may cause pancreatic beta cell death. Iron-mediated oxidative stress could plausibly be unfavourable in pancreatic injury and for lipid and cardiovascular risk. This is preclinical evidence only.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary hyperoxaluria prediction is based only on a graph model score. There are no trials or publications, and no plausible mechanism, since iron sucrose does not act on hepatic glyoxylate metabolism. None of the other nine predictions has clinical support either. Hyperparathyroidism is the only one with indirect (L4) evidence.

**To proceed, the following is needed:**
- Retrieval of the SAHPRA package insert (warnings, contraindications and approved indications). This is a blocking gap for safety screening.
- Mechanism of action data (for example from DrugBank).
- For hyperparathyroidism, a focused review of PTH and FGF23 outcomes in CKD patients receiving iron sucrose, controlling for phosphate binder use.
- No further investment in primary hyperoxaluria unless a credible mechanistic hypothesis emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

