---
layout: default
title: Nomegestrol Acetate
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nomegestrol Acetate: predicted new indication Candidiasis (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Nomegestrol acetate"
predicted_indications: ["candidiasis", "antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "plasma cell myeloma", "gout", "indolent plasma cell myeloma", "heart neoplasm", "thrombotic disease", "rheumatoid arthritis"]
---

# Nomegestrol Acetate
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

# Nomegestrol Acetate: From Hormonal Contraception to Candidiasis

## One-Sentence Summary

Nomegestrol acetate is a progestin, registered in South Africa as a component of an oral hormonal product (Zoely 2.5mg/1.5mg).
The TxGNN model predicts it may be effective for **candidiasis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction, and the other nine predicted indications are likewise unsupported by trial evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the SAHPRA registration entry has no indication text) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 98.78% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nomegestrol acetate is a progestin, so it acts on progesterone-receptor pathways. No established mechanism links it to antifungal activity.

The high TxGNN score appears to be a graph-based association only. Progestogen-containing hormonal therapy has, if anything, been associated with altered vaginal susceptibility to candidiasis, so any therapeutic link is speculative.

**Other predicted indications (all Hold):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Antithrombin deficiency type 2 | 98.53% | L5 | No known effect on antithrombin; a thrombophilia in which hormonal agents are a safety concern |
| 3 | Heparin cofactor 2 deficiency | 98.49% | L5 | No plausible direct mechanism; likely a coagulation-pathway graph association |
| 4 | Factor 5 excess with spontaneous thrombosis | 98.45% | L5 | Hormonal therapy modifies thrombosis risk, so there is a safety concern; likely a graph artefact |
| 5 | Plasma cell myeloma | 97.75% | L5 | No established role for progesterone-receptor signalling; minimal glucocorticoid activity |
| 6 | Gout | 97.60% | L5 | No known link to urate metabolism or gouty inflammation |
| 7 | Indolent plasma cell myeloma | 97.53% | L5 | Likely correlated with the parent disease node; no evidence |
| 8 | Heart neoplasm | 97.37% | L5 | No hormone-receptor-driven therapeutic pathway established |
| 9 | Thrombotic disease | 97.37% | L4 | One publication, which concerns VTE risk (a safety issue), not benefit |
| 10 | Rheumatoid arthritis | 97.36% | L5 | Sex hormones modulate immunity, but no direct evidence |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (candidiasis), currently no related literature available.

The only publication retrieved across the predicted indications relates to thrombotic disease (rank 9):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36254131](https://pubmed.ncbi.nlm.nih.gov/36254131/) | 2022 | Cohort/Observational (inferred from title) | Przeglad Menopauzalny (Menopause Review) | Reviews recent studies of VTE risk with oral oestrogen-progestogen therapies, including a large prospective cohort (PRO-E2) of a combined contraceptive containing 17β-estradiol 1.5 mg and nomegestrol acetate 2.5 mg. This is a safety/risk assessment, not evidence of therapeutic benefit. |

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 45/18.8/0064 | Zoely 2.5mg/1.5mg | Tablet (oral) | Not available in the data compiled for this report |

Essential Medicines List (EML) status was not available in the data compiled for this report.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Points relevant to the predicted indications:
- Several predictions (antithrombin deficiency, factor 5 excess with spontaneous thrombosis, thrombotic disease) involve thrombotic conditions, where hormonal therapy is generally a safety concern rather than a treatment.
- No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for candidiasis is supported only by the TxGNN graph score (L5), with no trials, no literature, and no plausible antifungal mechanism. The same applies to the other nine predictions. Several are in prothrombotic conditions, where a hormonal agent raises safety concerns.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), which is a blocking gap for safety screening
- Detailed mechanism of action data
- Approved indication text for the SAHPRA registration
- Any preclinical or clinical evidence supporting a biological rationale for the predicted indication
- Route and formulation compatibility assessment (currently only an oral tablet is registered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

