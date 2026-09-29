---
layout: default
title: Allopurinol
parent: Moderate Evidence (L3-L4)
nav_order: 23
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Allopurinol: From Hyperuricaemia and Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor. It is generally used to lower uric acid in gout and hyperuricaemia; this is general knowledge, as the registered indication text is not in the data supplied.
The TxGNN model predicts it may be relevant to **hepatic porphyria**, but there are **no registered clinical trials** and only **2 indirect publications** (one hypothesis paper and one rat study). Neither shows a benefit of allopurinol.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data supplied (generally gout and hyperuricaemia) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Allopurinol is a xanthine oxidase inhibitor, and no mechanistic link to hepatic porphyria can be confirmed from the supplied data.

The only linked literature concerns heme biosynthesis, specifically regulation of 5-aminolevulinate synthase and drug effects on hepatic haem metabolism. These papers are indirect, hypothesis-level or preclinical, and do not demonstrate a therapeutic benefit of allopurinol.

Interference with hepatic heme metabolism could instead signal a **safety concern** in porphyria. This is not verified from the supplied data and needs a dedicated safety review before any further step. At present the prediction is best treated as a research question, not a treatment candidate.

Other predicted indications (hepatoportal sclerosis, primitive portal vein thrombosis, idiopathic copper-associated cirrhosis, hepatopulmonary syndrome, early-onset familial noncirrhotic portal hypertension, immune-mediated necrotizing myopathy, antisynthetase syndrome, inflammatory myopathy with abundant macrophages) rest on score alone. The disorder of phenylalanine metabolism prediction is unsupported by its off-topic literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of 5-aminolevulinate synthase (via tryptophan or inhibition of heme use by tryptophan 2,3-dioxygenase) as therapy for acute hepatic porphyrias. Does not test allopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (rat) | Biochemical Pharmacology | Acute carbamazepine administration altered haem metabolism in rat liver, in relation to how it exacerbates hepatic porphyrias. Not about allopurinol. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| P/3.3/180 | Allopurinol 100 cipla | Tablet (oral) | Not stated in the data supplied |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records. This does not mean there are no interactions.
- **Possible porphyria-specific risk (unverified)**: The rationale flags that interference with hepatic heme metabolism may be a safety issue in porphyria. This needs dedicated review.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and two indirect papers, with no trials and no demonstrated benefit. Blocking safety data (PI warnings and contraindications) are also missing, so the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, downloaded and parsed from the SAHPRA website
- Mechanism of action data (for example, from DrugBank) to test any link to heme biosynthesis
- A dedicated safety review of allopurinol in porphyria
- Direct preclinical or clinical evidence involving allopurinol and hepatic porphyria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

