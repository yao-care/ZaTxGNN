---
layout: default
title: Tenofovir Disoproxil
parent: Model Prediction Only (L5)
nav_order: 437
evidence_level: L5
indication_count: 4
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Tenofovir Disoproxil: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor, used in humans for HIV-1 and chronic hepatitis B. The SAHPRA registration data supplied does not state the approved indication, so this is taken from general knowledge. The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**. The support is **4 registered clinical trials**, all in human HIV and only indirectly relevant, and **2 animal-study publications** in cats. This is a veterinary research question, not a new human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection and chronic hepatitis B (general knowledge; the SAHPRA records supplied do not state it) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (animal studies only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Tenofovir disoproxil is a prodrug of tenofovir, a nucleotide analogue that inhibits viral reverse transcriptase. Its efficacy against HIV-1 is well established.

Feline immunodeficiency virus (FIV) is a lentivirus that causes progressive immune failure in cats, similar to HIV in humans. Its reverse transcriptase is homologous to HIV's, so an HIV reverse transcriptase inhibitor plausibly acts on it. Two feline studies support this. One tested the combination dolutegravir, tenofovir and emtricitabine in FIV-infected cats. The other tested PMEA, a compound closely related to tenofovir, in naturally infected cats.

The KG score largely reflects this HIV-like biology. The evidence is limited to a small number of experimental animal studies. No trial tests tenofovir in FIV, and no feline product is registered.

## Clinical Trial Evidence

The trials below are linked to this prediction, but all are human HIV-1 studies in which tenofovir was a background component. None studies FIV or cats, and all were graded low relevance (grade C).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, each with ABC/3TC or TDF/FTC, in treatment-naïve HIV-1 adults |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs Atripla (efavirenz/emtricitabine/TDF) in treatment-naïve HIV-1 adults |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs boosted darunavir + emtricitabine/tenofovir or lamivudine/tenofovir in naïve HIV-1 patients |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir once-daily dose selection with ABC/3TC or TDF/FTC in naïve HIV-1 adults |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Experimental animal study | Viruses | Pharmacokinetics and clinical outcomes of combination ART (dolutegravir 2.5 mg/kg, tenofovir 20 mg/kg, emtricitabine 40 mg/kg) in FIV-infected cats; the abstract notes there is no definitive therapy for FIV |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Experimental animal study | J Feline Med Surg | Treatment of six naturally FIV-infected cats with PMEA, a tenofovir-related compound; the abstract notes that no antiviral is registered for FIV and that human antivirals have caused serious adverse effects in cats |

The abstracts available to us were truncated, so efficacy results are not summarised here.

## South Africa Market Information

Approved indication text was not provided in the source data. The list below shows the distinct registrations among the first entries supplied (20 in total). One registration was listed twice.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. A40/20.2.8/0681 | Viread | Tablet |
| Reg. No. 42/20.2.8/0561 | Cipla Tenofovir 300 | Tablet |
| Reg. No. 44/20.2.8/0332 | Adco tenofovir | Tablet |
| Reg. No. 42/34/0496 | Imavec | Capsule |

The Imavec entry (a capsule under a different therapeutic category code) should be checked against SAHPRA records. It may be a mismatched record.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but the only support is a few experimental studies in cats. The linked clinical trials are all human HIV studies. The prediction is also veterinary, so it would not create a new human indication or change practice in South Africa.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI), to confirm the approved indications and safety information, including warnings and contraindications
- Mechanism of action data from DrugBank
- Full-text review of the two feline studies for efficacy and safety in cats, given the adverse effects reported with human antivirals in cats
- Veterinary regulatory and expert input (in South Africa, the Onderstepoort veterinary sector and relevant veterinary authorities), because any FIV use would be outside human medicine
- Confirmation of the registration data quality (duplicate and possibly mismatched entries)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

