---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "primitive portal vein thrombosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-10-23
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L5). Approved use: Gout"
---

# Allopurinol
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

## Allopurinol: From Gout to Hepatic Porphyria
{: .text-alpha }

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor whose relations recorded in the knowledge graph include gout, hyperuricaemia and acute urate nephropathy. The TxGNN model predicts it may be useful for **hepatic porphyria**, but **no clinical trials** and only **2 publications** were retrieved, and neither shows a benefit of allopurinol in this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout (relation recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 1 of 1) |
| Number of SAHPRA Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid, and its relation to gout, hyperuricaemia and acute urate nephropathy is recorded in the knowledge graph.

The link to hepatic porphyria is weak and may point in the wrong direction. Older literature reports that allopurinol can affect haem biosynthesis (destroying cytochrome P450 haem and inducing hepatic 5-aminolevulinate synthase in animal models). This suggests it may be porphyrinogenic rather than therapeutic. The two retrieved papers do not study allopurinol: one is a hypothesis paper on targeting 5-aminolevulinate synthase with tryptophan and haem-utilisation inhibitors, and the other is a rat study of carbamazepine. The high model score is therefore not backed by direct evidence.

The nine other predicted diseases, which include hepatopulmonary syndrome, portal hypertension and myopathies, have no trials and no relevant literature. Several share identical scores. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes lowering 5-ALAS activity with tryptophan or haem-utilisation inhibitors as therapy for acute hepatic porphyrias; does not study allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study (rat) | Biochemical Pharmacology | Carbamazepine at a very small dose worsened haem metabolism in rat liver, as an exacerbator of hepatic porphyria; does not study allopurinol |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| P/3.3/180 | Allopurinol 100 cipla | Tablet (oral) | No indication text available in the licence record |

Essential Medicines List status could not be determined from the data compiled for this report.

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph (not label text):** liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis and anti-glomerular basement membrane disease.
- **Drug interactions (100 recorded; examples):**
  - Moderate: aluminium hydroxide, attapulgite, kaolin, magaldrate, sucralfate.
  - Minor: amoxicillin, chlorpropamide.
  - Level unspecified: metformin, omeprazole, pantoprazole, morphine, doxycycline, glimepiride and others.
- **Disease-specific concerns:** allopurinol may worsen porphyria rather than treat it. It is also a known cause of eosinophilic hypersensitivity reactions such as DRESS, which argues against use in eosinophilic myositis. Hypersensitivity reactions may rarely involve muscle.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on model score alone. No trial or publication directly studies allopurinol in hepatic porphyria, and the available mechanistic information suggests it may be harmful. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Review of allopurinol's effects on haem synthesis and its porphyrinogenic potential, with a clear safety assessment in porphyria.
- Mechanism of action data and the SAHPRA Professional Information (warnings and contraindications).
- Any direct preclinical or clinical study of allopurinol in hepatic porphyria. Without such a study, the other nine predictions also remain on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

