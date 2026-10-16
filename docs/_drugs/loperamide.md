---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Loperamide: predicted new indication Acute contagious conjunctivitis (evidence level L5). Approved use: Diarrhoeal disease, dysentery"
---

# Loperamide
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

# Loperamide: From Diarrhoeal Disease to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is an antimotility drug originally used to treat diarrhoeal disease and dysentery symptoms. The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The prediction appears to be a knowledge-graph artefact rather than a pharmacological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhoeal disease, dysentery |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Loperamide is generally understood as a peripheral mu-opioid receptor agonist acting on gut myenteric neurons to reduce motility. Its efficacy in symptomatic diarrhoea is established.

For acute contagious conjunctivitis, no credible mechanistic link was identified. Loperamide has no known anti-infective or anti-inflammatory action in the eye. The high TxGNN score (ranked 366th overall) most likely reflects graph propagation and not a real pharmacological rationale. The other top-ranked predictions are also mostly conjunctivitis variants (conjunctivitis, pseudomembranous, chronic follicular, parasitic, serous, conjunctival folliculosis), plus Angelucci syndrome, which also lack supporting evidence.

Predictions closer to the original use fare no better. For **amebic dysentery** (score 99.95%), loperamide has no antiparasitic activity, and the literature points to harm (see below). For **gastroduodenitis** (score 99.77%), the only publication is a safety case report.

## Clinical Trial Evidence

Currently no related clinical trials registered for acute contagious conjunctivitis. No SANCTR or PACTR entries were identified in the data compiled for this report.

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

For context, literature found for other predicted indications consists of safety signals, not evidence of benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | J Travel Med | Fulminant amoebic colitis and toxic megacolon, possibly worsened by heavy loperamide use (amebic dysentery) |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Am J Med | Overview of non-fluid therapy for acute diarrhoea (amebic dysentery) |
| [41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/) | 2026 | Case report | Cureus | Loperamide-induced respiratory depression in severe chemotherapy-related GI inflammation (gastroduodenitis) |

## South Africa Market Information

Loperamide is registered in South Africa as a single-ingredient product under 4 valid registrations. Approved indication text and manufacturer details were not available in the data compiled for this report.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Y/11.9/0073 | Norimode | Tablet | Not available |
| V/11.9/0213 | Gastron | Tablet | Not available |
| 31/11.9.2/0402 | Imodium Plus | Tablet | Not available |
| 28/11.9/0649 | Loperastat | Syrup | Not available |

No ophthalmic formulation is registered; the available forms are oral tablets and syrup.

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text):** liver disease, gallbladder disease, paralytic ileus, intestinal obstruction, familial visceral myopathy, dysentery, diarrhoeal disease, infectious diarrhoeal disease, intestinal infectious disease.
- **Safety signals in the literature:** toxic megacolon with amoebic colitis (antimotility agents in invasive infection), and respiratory depression when gut barrier integrity is impaired and systemic exposure rises.
- **Drug interactions:** 100 interactions were recorded. Examples of **Major** interactions: abiraterone, ranitidine, fosamprenavir, gemfibrozil. Examples of **Moderate** interactions: codeine, dihydrocodeine, tramadol, chlorpheniramine, cetirizine, salbutamol, ethanol, galantamine, gemifloxacin, gilteritinib, alfuzosin.

Please refer to the SAHPRA-approved Professional Information (PI) for official warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature, and no plausible mechanism for an infectious ocular condition. The nearest alternative predictions (amebic dysentery, gastroduodenitis) show safety concerns rather than benefit.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) to allow a proper mechanistic assessment
- SAHPRA Professional Information, including warnings, contraindications and approved indications
- A credible biological rationale for ocular use, followed by preclinical evidence, before any clinical consideration
- An ocular-route formulation assessment, since only oral forms are registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

