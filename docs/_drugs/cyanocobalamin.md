---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 155
evidence_level: L5
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin is a synthetic form of vitamin B12, originally used to treat vitamin B12 deficiency and related anaemias (including pernicious anaemia).
The TxGNN model predicts it may be useful for **biotin metabolic disease**, but the supporting evidence is very limited: **0 clinical trials** and **1 publication** (a general review on vitamin production that does not address this use).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia, folic acid deficiency anaemia, iron deficiency anaemia and other deficiency anaemias (from the knowledge-graph indication list; SAHPRA indication text is not available) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for cyanocobalamin is not available in the data compiled for this report. Based on general knowledge, vitamin B12 is a cofactor in one-carbon metabolism and in propionate/methylmalonate metabolism. Its efficacy in B12 deficiency and pernicious anaemia is well established.

A plausible biological link exists. B12-dependent pathways share metabolic routes with biotin-dependent carboxylases such as propionyl-CoA carboxylase. Disorders of biotin metabolism could therefore affect B12-related pathways.

However, the prediction rests mainly on the high TxGNN score, which reflects network proximity in the knowledge graph rather than demonstrated clinical benefit. No direct evidence shows that cyanocobalamin treats biotin metabolic disease (for example biotinidase or holocarboxylase synthetase deficiency). Standard therapy for those conditions is biotin supplementation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | General review of biotechnological production of vitamins and coenzymes. It does not assess cyanocobalamin as a treatment for biotin metabolic disease, so its relevance is indirect. |

## South Africa Market Information

All 11 registrations are valid single-ingredient products. The approved indication text was not available for any of them, and Essential Medicines List (EML) status could not be determined from the data compiled. The five main registrations are listed below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2413 (ACT 101/1965) | A-lennon vitamin b12 1ml | Injection | Not available |
| T1012 (ACT 101/1965) | Beespan | Capsule | Not available |
| U/2.6/218 | Restin | Capsule | Not available |
| A/21.8.1/743 | Menoflush | Tablet | Not available |
| 36/22.1/0508 | Cernevit | Infusion | Not available |

Other registered products include Complenatal Ff, Dextrose 20% in water 500ml, ITN neonatal TPN, Gericomplex, Spiriva Respimat inhaler and Filibon. Available routes are injectable (injection, infusion), oral (capsule, tablet) and other (TPN, inhaler).

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The 20 shown are all Minor or Unknown severity, and none is rated higher in the data shown.
  - Minor: acid-suppressing drugs (famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors rabeprazole, esomeprazole, lansoprazole, dexlansoprazole, omeprazole, pantoprazole), and potassium chloride.
  - Unknown severity: metformin, glimepiride, rosiglitazone, acarbose, mesalazine, doxycycline, morphine and sucralfate.

Please refer to the SAHPRA-approved Professional Information (PI) for warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. There are no registered clinical trials, and the single publication is an indirect general review. Standard biotin therapy already exists for biotin metabolic disorders, and no evidence suggests cyanocobalamin adds benefit.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Targeted literature review for cyanocobalamin in biotinidase or holocarboxylase synthetase deficiency and related disorders
- The SAHPRA-approved Professional Information (PI), to complete the safety screening
- Clear clinical rationale and unmet need compared with standard biotin therapy
- Preclinical or early clinical evidence before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

