---
layout: default
title: Solifenacin
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
---

# Solifenacin
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

# Solifenacin: From Overactive Bladder to Polycystic Kidney Disease 3 (with or without Polycystic Liver Disease)

## One-Sentence Summary

Solifenacin is a selective M3 muscarinic antagonist used for bladder symptoms. The TxGNN model predicts it may be effective for **polycystic kidney disease 3 with or without polycystic liver disease**, but there are **0 clinical trials** and **20 publications**, all disease-background reviews or guidelines. None of them evaluates solifenacin, so this prediction is a knowledge-graph association only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder (inferred from the drug's class and pharmacology; the SAHPRA registration record gives no indication text) |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 97.13% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not well supported. Currently, detailed mechanism of action data is not available in the record. Solifenacin is known to block M3 muscarinic receptors on bladder smooth muscle, which reduces involuntary detrusor contractions.

Polycystic kidney disease 3 with or without polycystic liver disease is a genetic disease (GANAB-related). Cyst formation is driven by defects in polycystin and ER glycoprotein processing. No plausible link exists between muscarinic receptor antagonism and these pathways.

The high score of 0.97 reflects a graph association, not a biological rationale or clinical signal. The 20 retrieved publications describe the disease's genetics, diagnosis and management, and none evaluates solifenacin.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No study among the retrieved publications tests solifenacin. All are background literature on the disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guideline | Am J Gastroenterol | ACG guideline on focal liver lesions, including hepatic cystic lesions and polycystic liver disease |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | J Hepatol | EASL guidelines on diagnosis and management of cystic liver diseases |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | ADPKD as a systemic disorder, with kidney and liver cysts and other extrarenal complications |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | Polycystic liver disease in ADPKD; tolvaptan slows renal function decline |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Review | J Am Soc Nephrol | Genetic overlap between ADPKD and polycystic liver disease (PKD1, PKD2, GANAB and others) |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Review | Adv Kidney Dis Health | Genetic spectrum of polycystic kidney and liver diseases and resulting phenotypes |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Review | Rev Med Suisse | Overview of polycystic liver disease (biliary hamartomas, ADPLD, ADPKD) |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Basic research | J Clin Invest | Genes of isolated polycystic liver disease as effectors of polycystin-1 function |
| [37266470](https://pubmed.ncbi.nlm.nih.gov/37266470/) | 2023 | Case report | Maedica | Polycystic kidney and liver disease associated with advanced gastric cancer |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 56/21.12/1063 | Firsoltam | Mrt | Not stated in the registration record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no drug-specific literature and no plausible mechanistic link, so it stays at L5 (model prediction only). The other nine predictions for this drug are also L5 and Hold, except rank 7, low compliance bladder. That one is biologically plausible, as it is close to solifenacin's existing bladder use and has neurogenic detrusor overactivity data (PMID 32007426). It is classed L3 as a research question and is better treated as an extension of the current indication than as true repurposing.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is needed before any safety screening
- Mechanism of action data from DrugBank
- Any preclinical or clinical study of solifenacin in polycystic kidney or liver disease; without one, this indication should not advance
- Consider redirecting effort to the low compliance bladder prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

