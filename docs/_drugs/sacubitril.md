---
layout: default
title: Sacubitril
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Sacubitril
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

# Sacubitril: From Heart Failure to Brain Small Vessel Disease 1 (with or without Ocular Anomalies)

## One-Sentence Summary

Sacubitril is a neprilysin inhibitor, marketed in South Africa as a tablet (Vymada 50 mg) and used mainly for heart failure.
The TxGNN model ranks **brain small vessel disease 1 with or without ocular anomalies** as its top prediction, but this is a model output only, with **0 clinical trials** and **no publications that mention sacubitril**.
This prediction should not be pursued. The evidence supports only a Hold.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure (from the known use of sacubitril/valsartan; the SAHPRA indication text is not in the data provided) |
| Predicted New Indication | Brain small vessel disease 1 with or without ocular anomalies |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sacubitril inhibits neprilysin, which raises natriuretic peptide levels. It is normally combined with valsartan, which blocks the AT1 receptor.

This prediction is **not mechanistically supported**. The predicted disease is a monogenic disorder of the basement membrane and small vessels (COL4A1-related). Neprilysin inhibition and AT1 blockade have no established relevance to it. The high score most likely reflects a knowledge-graph association rather than a real biological link.

The 19 papers retrieved are general reviews of congenital ocular malformations, such as Axenfeld-Rieger syndrome, coloboma and optic disc anomalies. None mention sacubitril.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35882526](https://pubmed.ncbi.nlm.nih.gov/35882526/) | 2023 | Review | J Med Genet | Axenfeld-Rieger syndrome: anterior segment anomalies and systemic features. No drug data. |
| [39097141](https://pubmed.ncbi.nlm.nih.gov/39097141/) | 2024 | Not classified | Prog Retin Eye Res | Genotype-phenotype correlations in congenital anterior segment disorders. |
| [36926528](https://pubmed.ncbi.nlm.nih.gov/36926528/) | 2023 | Not classified | Clin Ophthalmol | Ophthalmological manifestations of Axenfeld-Rieger syndrome (FOXC1/PITX2). |
| [37468646](https://pubmed.ncbi.nlm.nih.gov/37468646/) | 2024 | Not classified | Pediatr Nephrol | Ocular manifestations of congenital kidney and urinary tract anomalies. |
| [30182440](https://pubmed.ncbi.nlm.nih.gov/30182440/) | 2018 | Review | Am J Med Genet C | Neuropathology of holoprosencephaly. |
| [33870948](https://pubmed.ncbi.nlm.nih.gov/33870948/) | 2022 | Review | J Neuroophthalmol | Optic nerve aplasia: ophthalmologic, systemic and genetic findings. |
| [22963965](https://pubmed.ncbi.nlm.nih.gov/22963965/) | 2012 | Not classified | Ann Dermatol Venereol | Branchio-oculo-facial syndrome, with a case report. |
| [35791156](https://pubmed.ncbi.nlm.nih.gov/35791156/) | 2022 | Not classified | Indian J Ophthalmol | Clinical features and orbital anomalies in Fraser syndrome. |
| [11581073](https://pubmed.ncbi.nlm.nih.gov/11581073/) | 2001 | Not classified | Ophthalmology | Ocular features of renal coloboma syndrome. |
| [36636984](https://pubmed.ncbi.nlm.nih.gov/36636984/) | 2023 | Not classified | Ophthalmic Genet | Two infants with congenital inner eyelid folds. |

These are the 10 most relevant of 19 retrieved papers. All are background papers on congenital eye anomalies. **None tests or discusses sacubitril.**

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/7.6/1019 | Vymada 50 Mg | Tablet | Not stated in the data provided |

Essential Medicines List (EML) status could not be determined from the data provided.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials, no relevant literature and no plausible mechanism. In addition, the SAHPRA package insert safety data, a blocking gap, has not been retrieved.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is currently blocking.
- Mechanism of action data from DrugBank.
- Any mechanistic or preclinical evidence linking neprilysin inhibition or AT1 blockade to COL4A1-related small vessel disease. Without it, no further work is justified.

**Note on other predictions:**
Among the 10 predicted indications, only **diabetic nephropathy** (rank 3, score 99.50%) has meaningful support. Its evidence level is L4, with several preclinical studies and one registered Phase 4 trial, [NCT06501651](https://clinicaltrials.gov/study/NCT06501651), which is not yet recruiting. It is worth evaluating separately as a research question. The other eight predictions have no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

