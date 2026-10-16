---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor, originally used to treat gout, hyperuricaemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but **no clinical trials** and only **2 publications** (one hypothesis paper and one animal study) relate to this prediction, and neither supports a benefit for allopurinol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout (also hyperuricaemia and acute urate nephropathy, per the knowledge graph; the SAHPRA registration entry has no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is known as a xanthine oxidase inhibitor that lowers uric acid, and its efficacy in gout is established.

Older preclinical work suggests allopurinol may degrade hepatic cytochrome P450 heme and affect heme metabolism, which could in theory modulate 5-aminolevulinate synthase (ALAS1), the rate-limiting enzyme of heme synthesis. However, allopurinol has also been described as a porphyrinogenic agent in experimental models, so the direction of effect is uncertain and may be harmful.

The two retrieved papers concern a hypothesis on metabolic targeting of ALAS1 and the effects of carbamazepine on rat liver heme metabolism. Neither provides clinical evidence for allopurinol in porphyria. The very high TxGNN score is a computational prediction only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes targeting liver ALAS1 with tryptophan or inhibitors of heme use by tryptophan 2,3-dioxygenase as therapy for acute hepatic porphyrias; does not study allopurinol directly |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | Carbamazepine, at a very small dose, exacerbated disturbances of heme metabolism in rat liver; relevant to drug-induced porphyria mechanisms, not to allopurinol |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| P/3.3/180 | Allopurinol 100 cipla | Tablet (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, and anti-glomerular basement membrane disease. Liver disease is directly relevant to the predicted hepatic indication.
- **Drug Interactions** (100 interactions recorded; main ones shown):
  - Moderate: aluminium hydroxide, attapulgite, kaolin, magaldrate, sucralfate
  - Minor: amoxicillin, chlorpropamide
  - Severity not classified: calcitriol, vitamin A, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, acarbose, morphine, metformin, omeprazole, rosiglitazone, palonosetron
- **Porphyria-specific concern**: preclinical literature describes allopurinol as potentially porphyrinogenic, which could worsen the very condition it is predicted to treat.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials and no supportive literature. Preclinical reports suggest allopurinol may be porphyrinogenic, so harm is a plausible risk. Other predicted indications (for example hepatoportal sclerosis, hepatopulmonary syndrome and inflammatory myopathies) also have no supporting evidence in the data.

**To proceed, the following is needed:**
- Review of the SAHPRA package insert for warnings and contraindications, which is currently missing and blocks safety screening
- Mechanism of action data (for example from DrugBank)
- Experimental or clinical evidence on whether allopurinol worsens, improves or has no effect on ALAS1 activity and porphyria attacks
- Review of existing case reports or pharmacovigilance data on allopurinol use in patients with acute hepatic porphyria
- Confirmation of the approved indication text for registration P/3.3/180, and of Essential Medicines List status, which is not stated in the data compiled for this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

