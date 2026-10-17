---
layout: default
title: Leucovorin
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Leucovorin: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Megaloblastic anaemia"
monitor_inn: "Leucovorin"
predicted_indications: ["primary hyperoxaluria", "congenital intrinsic factor deficiency", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "hereditary hemochromatosis", "idiopathic eosinophilic myositis", "inflammatory myopathy with abundant macrophages", "focal myositis", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Leucovorin
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

# Leucovorin: From Megaloblastic Anaemia to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid) is a reduced folate, originally used to treat megaloblastic anaemia.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Megaloblastic anaemia (from the TxGNN knowledge graph; the SAHPRA registration does not list an approved indication text) |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

Other top-ranked predictions (scores 98.5%–99.3%) are summarised below.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Primary hyperoxaluria | 99.41% | L5 | Hold |
| 2 | Congenital intrinsic factor deficiency | 99.34% | L5 | Hold |
| 3 | Immune-mediated necrotizing myopathy | 98.85% | L5 | Hold |
| 4 | Antisynthetase syndrome | 98.79% | L5 | Hold |
| 5 | Hereditary haemochromatosis | 98.78% | L5 | Hold |
| 6 | Idiopathic eosinophilic myositis | 98.70% | L5 | Hold |
| 7 | Inflammatory myopathy with abundant macrophages | 98.70% | L5 | Hold |
| 8 | Focal myositis | 98.70% | L4 | Hold |
| 9 | Primary amyloidosis | 98.62% | L4 | Hold |
| 10 | Acquired amyloid peripheral neuropathy | 98.55% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leucovorin is a reduced folate (folinic acid) that supports one-carbon metabolism. It is already established for megaloblastic anaemia, as it bypasses the dihydrofolate reductase step in folate metabolism.

For **primary hyperoxaluria**, the data compiled for this report show no established link between folinic acid and oxalate or glyoxylate metabolism. The high score is a graph-based signal only and should not be read as a mechanistic rationale.

The more biologically plausible prediction is **congenital intrinsic factor deficiency** (rank 2). This condition causes vitamin B12 malabsorption and a megaloblastic blood picture similar to the original indication. Leucovorin may partially correct the haematological abnormality, but it does not correct B12 deficiency itself, and neurological damage may still progress. B12 replacement remains the standard of care.

Several other predictions (necrotizing myopathy, antisynthetase syndrome, eosinophilic myositis, inflammatory myopathy with abundant macrophages, focal myositis) are probably driven by network proximity to methotrexate-treated myositis. Leucovorin is used there to mitigate antifolate toxicity, not as a disease-modifying therapy. No plausible mechanism is supported for hereditary haemochromatosis or acquired amyloid peripheral neuropathy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction, primary hyperoxaluria.

The only trial retrieved for any of the top-ranked predictions concerns primary amyloidosis (rank 9), and it provides only indirect evidence:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003331](https://clinicaltrials.gov/study/NCT00003331) | Phase 1 | Completed | 30 | Topotecan with 5-fluorouracil and leucovorin in advanced malignancies. Leucovorin modulates 5-FU; the study does not evaluate leucovorin for amyloidosis and the population is probably oncologic. |

---

## Literature Evidence

Currently no related literature available for the lead prediction, primary hyperoxaluria.

Literature was retrieved only for focal myositis (rank 8). None of these items tests leucovorin as a treatment for the condition, and the abstracts are truncated.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8393509](https://pubmed.ncbi.nlm.nih.gov/8393509/) | 1993 | RCT | Medicine | Immunosuppressive therapy in inclusion body myositis (retrospective review and randomised crossover trial) |
| [9506565](https://pubmed.ncbi.nlm.nih.gov/9506565/) | 1998 | RCT | Arthritis Rheum | Randomised crossover study of two cytotoxic regimens in refractory myositis |
| [32649847](https://pubmed.ncbi.nlm.nih.gov/32649847/) | 2021 | Case report | Immunol Med | Severe oral stomatitis from HSV-1 reactivation in a methotrexate-treated dermatomyositis patient; leucovorin given for suspected MTX toxicity, but stomatitis worsened |
| [25963703](https://pubmed.ncbi.nlm.nih.gov/25963703/) | 2015 | Case report | Gan To Kagaku Ryoho | Polymyositis associated with transverse colon cancer, responding to tumour resection and chemotherapy |
| [9787292](https://pubmed.ncbi.nlm.nih.gov/9787292/) | 1998 | Case report | Dtsch Med Wochenschr | Paraneoplastic orbital disease in a patient with cardia carcinoma after leucovorin/5-FU chemotherapy |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 27/8.3/0151 | Abic leucovorin | Injection | Not listed in the data compiled for this report |

Only one valid single-ingredient registration is recorded, and it is an injectable formulation. Essential Medicines List (EML) status could not be confirmed from the data compiled for this report.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: vitamin B12 deficiency and pernicious anaemia. Folate can correct the blood picture while neurological damage progresses, which is especially relevant to the intrinsic factor deficiency prediction.
- **Drug Interactions**: 100 interactions were identified. The main ones with a graded severity are:
  - Pancrelipase (Moderate)
  - Sulfasalazine (Minor)

  Many others (e.g. metformin, omeprazole, pantoprazole, doxycycline, morphine, vancomycin) have an unclassified severity level.

Please also refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions rest on model scores alone, with no direct clinical trial or literature support. The lead prediction (primary hyperoxaluria) has no supported mechanism. The strongest mechanistic case (congenital intrinsic factor deficiency) is adjunctive at best, as B12 replacement remains the standard of care.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g. from DrugBank)
- A targeted literature search on leucovorin in primary hyperoxaluria and congenital intrinsic factor deficiency
- Clarification of whether the myositis predictions reflect toxicity rescue rather than therapy, in which case they should not be treated as new indications
- Confirmation of approved indications and EML status for the registered product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

