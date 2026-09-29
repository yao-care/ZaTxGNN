---
layout: default
title: Dolutegravir
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir is an HIV-1 integrase strand transfer inhibitor, already marketed in South Africa for HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a cat lentivirus infection.
Support is indirect: **5 clinical trials** (all in human HIV-1, none in cats) and **1 veterinary publication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the SAHPRA indication text is blank in the record) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (preclinical/veterinary only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold (research question) |

---

## Why is This Prediction Reasonable?

Dolutegravir blocks the viral integrase enzyme, which inserts viral DNA into the host genome. FIV is a lentivirus related to HIV, and it causes progressive immune failure in cats that resembles AIDS. Blocking integration is therefore a plausible way to slow FIV. Related evidence from the simian model (SIV in macaques) shows that integrase inhibitors, including dolutegravir, act on a lentivirus outside humans.

Detailed mechanism of action data is not available in the record. Dolutegravir's efficacy in HIV-1 is well established, and mechanistically it may be applicable to FIV. However, the integrase sequences of FIV and HIV-1 differ, so activity in cats is not established by the data supplied.

The one veterinary study, from 2023, tested dolutegravir inside a three-drug regimen in FIV-infected cats. The provided abstract is truncated, so its clinical results cannot be summarised here.

---

## Clinical Trial Evidence

All trials below are in **human HIV-1**. They support the drug's antiviral efficacy and safety in its source disease, not efficacy in cats.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir vs raltegravir in treatment-experienced, integrase-inhibitor-naïve adults (48 weeks) |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir with dual NRTI backbone in treatment-naïve adults (96 weeks) |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs Atripla in treatment-naïve adults (96 weeks) |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Phase IIb once-daily dose selection with two NRTI backbones |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Single-arm study of plasma and cerebrospinal fluid pharmacokinetics with abacavir/lamivudine |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/veterinary | Viruses | Pharmacokinetics and clinical outcomes of combination ART (dolutegravir 2.5 mg/kg, tenofovir 20 mg/kg, emtricitabine 40 mg/kg) in FIV-infected domestic cats; abstract truncated in the record |

---

## South Africa Market Information

Twenty registrations are on file; the five main ones are shown. Approved indication text is not recorded for any of them.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 56/20.2.8/0018 | Odinsti Dispersible Tablets | Orally disintegrating tablet (ODT) |
| Reg. No. 51/20.2.8/1032.1031 | Dalimune | Tablet |
| Reg. No. 52/20.2.8/0002.001 | Hetvir 50 | Film-coated tablet |
| Reg. No. 54/20.2.8/0642.641 | Lomida | Tablet |
| Reg. No. 55/20.2.8/0301 | Daliduo | Film-coated tablet |

An effervescent tablet form is also listed among the registered dosage forms.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note for any neurodevelopmental use: neural tube defect signals in pregnancy (Tsepamo study, Botswana) have been reported with dolutegravir and would need careful review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is supported only by human HIV-1 trials and a single veterinary study whose results we could not review. Cross-species activity against FIV integrase is not established. Nothing in the record indicates a human clinical use for this prediction, so it remains a research question.

**To proceed, the following is needed:**
- Full review of the 2023 FIV cat study (PMID 37112803), including efficacy, dosing and safety outcomes
- Integrase sequence and in vitro susceptibility data for dolutegravir against FIV
- SAHPRA Professional Information (warnings and contraindications), currently missing and blocking safety screening
- Mechanism of action data from DrugBank
- Confirmation of the regulatory pathway for any veterinary use, since SAHPRA registrations cover human medicines

**Other predictions in the pack:**
- **Simian immunodeficiency virus infection (Hold, L4):** Macaque studies support the integrase mechanism. SIV is an animal model, so this backs the existing HIV-1 use rather than a new human target.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (Hold, L5):** There is no supporting trial or literature and no plausible mechanistic link. It is likely a knowledge-graph artifact and needs manual review.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

