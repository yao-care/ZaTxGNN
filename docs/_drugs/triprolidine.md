---
layout: default
title: Triprolidine
parent: Moderate Evidence (L3-L4)
nav_order: 458
evidence_level: L4
indication_count: 7
---

# Triprolidine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Triprolidine: From Cough and Cold Preparations to Allergic Urticaria

## One-Sentence Summary

Triprolidine is a first-generation antihistamine. In South Africa it is registered mainly in syrup products, and the product names suggest cough and cold use. The TxGNN model predicts it may be effective for **allergic urticaria**. Support is weak: **0 registered clinical trials** and **6 publications**, almost all of which concern related drugs or general antihistamine reviews rather than triprolidine itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data. Product names (cough linctus, expectorant, paediatric syrups) suggest cough and cold symptom relief; this is an inference, so confirm against the Professional Information (PI). |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source data. Triprolidine is a first-generation H1 receptor antagonist. Blocking the H1 receptor is the standard approach for histamine-mediated urticaria, so the prediction is pharmacologically coherent.

The literature retrieved is indirect. Most items concern acrivastine, a triprolidine-derived analogue, or are general reviews of H1 antihistamines. The only triprolidine-specific paper is a 1965 study of skin response to ultraviolet radiation, not a urticaria efficacy trial. This is class-level plausibility, not direct evidence.

TxGNN also ranked six other indications, all with weaker support:

- **Cold urticaria:** one indirect acrivastine trial. Hold.
- **Pharyngitis:** one placebo-controlled trial of a pseudoephedrine/triprolidine combination in children with purulent nasopharyngitis. The abstract is truncated, so the result cannot be attributed to triprolidine. Hold.
- **Nasal cavity disease, acute laryngopharyngitis, recalcitrant atopic dermatitis and atopic IgE responsiveness:** model prediction only, with no literature or trials. Hold.

"Atopic IgE responsiveness" is a trait rather than a treatable condition. H1 antagonists block downstream histamine effects and do not change IgE production.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR and PACTR identifiers: none found in the data provided).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7911009](https://pubmed.ncbi.nlm.nih.gov/7911009/) | 1994 | RCT (acrivastine; indirect) | Allergy | Double-blind, placebo-controlled crossover in 10 pollen-allergic subjects. Studied how quickly acrivastine 8 mg suppresses skin-prick wheals. Acrivastine is a triprolidine derivative, so this does not test triprolidine. |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine was effective and well tolerated in chronic urticaria and allergic rhinitis in double-blind trials. |
| [8094649](https://pubmed.ncbi.nlm.nih.gov/8094649/) | 1993 | Review | Dermatologic Clinics | Newer low-sedating H1 antihistamines are first-line for urticaria and mild angioedema. |
| [2568212](https://pubmed.ncbi.nlm.nih.gov/2568212/) | 1989 | Review | Clinical Pharmacy | Reviews non-sedating H1 antagonists. Notes acrivastine is a side-chain-reduced metabolite of triprolidine. |
| [1983393](https://pubmed.ncbi.nlm.nih.gov/1983393/) | 1990 | Review/commentary | Drug and Therapeutics Bulletin | Commentary on three new non-sedative antihistamines. No abstract available. |
| [14283425](https://pubmed.ncbi.nlm.nih.gov/14283425/) | 1965 | Experimental human skin study | British Journal of Dermatology | Triprolidine and skin response to UV radiation. No abstract available, and not a urticaria efficacy study. |

For cold urticaria, the acrivastine versus cyproheptadine trial in 18 patients ([PMID 2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/), *Dermatologica*, 1988) is also indirect evidence.

## South Africa Market Information

There are 14 SAHPRA registrations in total. The main ones shown in the data are below. All are syrups. Approved indication text and manufacturer are not provided, and Essential Medicines List (EML) status is not stated in the data. A topical cream form appears in the route summary, but none of the registrations listed below is a cream.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 27/5.8/0260 | Adco-flupain | Syrup |
| Reg. No. Y/10.1.1/138 | Merck-Cough Linctus | Syrup |
| Reg. No. 27/10.1/0256 | Adco-tussend | Syrup |
| Reg. No. 31/5.8/0056 | Coryx paediatric | Syrup |
| Reg. No. Y/10.1.1/139 | Merck-Expectorant | Syrup |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible, but no registered trials exist and no retrieved paper tests triprolidine for urticaria. The safety data from the package insert is still missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking gap), and confirmation of the labelled indications
- Mechanism of action data, for example from DrugBank
- Triprolidine-specific evidence in urticaria, from a targeted literature search or a new study
- Comparison against low-sedating second-generation antihistamines, which are the standard first-line therapy for urticaria
- Verification of the intervention in the pharyngitis paper (PMID 6377256) before any upgrade of that indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

