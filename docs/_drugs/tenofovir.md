---
layout: default
title: Tenofovir
parent: Model Prediction Only (L5)
nav_order: 435
evidence_level: L5
indication_count: 3
---

# Tenofovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tenofovir: From HIV Antiviral Therapy to Feline Acquired Immunodeficiency Syndrome (Veterinary Prediction)

## One-Sentence Summary

Tenofovir is a nucleotide reverse transcriptase inhibitor. The Evidence Pack does not record an original indication, but the clinical trials matched here concern HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary disease.
Support is limited to **4 HIV-1 clinical trials (indirect evidence)** and **2 animal studies in cats**, so no direct human evidence exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (SAHPRA licence entries contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical animal studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Tenofovir is known to be a nucleotide reverse transcriptase inhibitor, and it is part of several fixed-dose HIV regimens (for example with emtricitabine).

FIV is a lentivirus that causes an AIDS-like illness in cats. Its reverse transcriptase is homologous to that of HIV-1, so a mechanistic rationale exists. A cat study (PMID 37112803) has tested a combination of dolutegravir, tenofovir and emtricitabine, and an earlier study (PMID 24782459) tested the tenofovir-related compound PMPA in naturally FIV-infected cats.

The very high TxGNN score most likely reflects tenofovir's established use against HIV-1 in humans, rather than new information about cats. FIV is a veterinary disease, so this prediction has little direct relevance for human medicine in South Africa. The same score is also given to simian immunodeficiency virus infection (rank 2), where extensive macaque data exist. These serve as a model of HIV prevention and treatment rather than a new human indication. The third prediction (a rare neurodevelopmental disorder, score 99.96%) has no plausible mechanistic link, no trials and no literature, and is probably a model artifact.

## Clinical Trial Evidence

All trials below were run in HIV-1 patients. Tenofovir is a background or comparator component, so none addresses FIV directly.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01228824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, with TDF/FTC or ABC/3TC as background, in treatment-naive HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs boosted darunavir + tenofovir-containing regimens in naive HIV-1 patients |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir dose selection with ABC/3TC or TDF/FTC in treatment-naive HIV-1 adults |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs efavirenz/tenofovir/emtricitabine (Atripla) in treatment-naive HIV-1 adults |

No SANCTR or PACTR identifiers are available in the Evidence Pack.

## Literature Evidence

Only the two FIV-specific publications are listed here; the SIV/SHIV macaque literature is a separate prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal study | Viruses | Pharmacokinetics and clinical outcomes of dolutegravir, tenofovir and emtricitabine combination therapy in FIV-infected cats |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Animal study | J Feline Med Surg | PMPA (tenofovir) treatment of six naturally FIV-infected cats; the abstract notes serious adverse effects with some human antivirals used experimentally in cats |

## South Africa Market Information

Essential Medicines List (EML) inclusion status is not provided in the Evidence Pack. The licences below carry no indication text.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 44/20.2.8/0307 | Zefin | Tablet | Not stated |
| Reg. No. 47/20.2.8/0188 | Emtroc 200mg/300mg | Tablet | Not stated |
| Reg. No. 47/20.2.8/0328 | Trivenz | Tablet | Not stated |
| Reg. No. 47/20.2.8/0327 | Rizene | Tablet | Not stated |
| Reg. No. 47/20.2.8/0326 | Triploco | Film-coated tablet | Not stated |

Six registrations are recorded in total; five are shown.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for the lead prediction is indirect HIV-1 human trials and two small cat studies. FIV is a veterinary disease with no relevance as a human indication, and the high score likely reflects tenofovir's known HIV use. Safety data for the SAHPRA products is also missing.

**To proceed, the following is needed:**
- Clarify whether the intended scope is human or veterinary use; a veterinary programme would need a separate regulatory pathway
- SAHPRA Professional Information (warnings and contraindications), which is a blocking gap
- Original indications and mechanism of action from DrugBank
- Controlled efficacy and safety data in FIV-infected cats, if the veterinary direction is pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

