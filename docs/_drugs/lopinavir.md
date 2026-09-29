---
layout: default
title: Lopinavir
parent: Model Prediction Only (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor used in antiretroviral therapy.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary condition.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the SAHPRA indication text was not supplied in the Evidence Pack) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Lopinavir is known to inhibit the HIV-1 protease, an enzyme the virus needs to mature into infectious particles. Feline immunodeficiency virus (FIV) is also a lentivirus, so the prediction is plausible in principle.

There are important limits, however:
- FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so lopinavir activity against FIV is not assured.
- The very high score (99.90%) most likely reflects how close lentiviral immunodeficiency diseases sit to each other in the knowledge graph. It is not independent evidence of efficacy.
- This is a veterinary indication. It has no human clinical relevance beyond lopinavir's approved HIV use.

**Other predictions in the pack**
- **Simian immunodeficiency virus (SIV) infection** (rank 2, score 99.90%, evidence level L4) has three non-human primate studies. SIV in macaques is a standard preclinical model of HIV, so this is best read as a model-system finding, not a new indication.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (rank 3, score 99.90%, evidence level L5) has no plausible mechanistic link. Lopinavir targets a viral protease, and this disorder is genetic with no viral cause. Poor CNS penetration and lopinavir's metabolic and QT-related adverse effects weaken any rationale further.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For reference, the SIV prediction (rank 2) has three animal studies. These are indirect, preclinical, and do not support the FIV prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Viral decay in SIV-infected macaques given quadruple antiretroviral therapy |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model development | Microbes Infect | A SHIV carrying the HIV-1 protease gene, built to test protease inhibitors in rhesus macaques |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | J Virol Methods | Effect of oral HAART (AZT, 3TC, lopinavir/ritonavir) on the CD8 subset in SHIV-infected monkeys |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 43/20.2.8/0356 | Aluvia 100/25 | Tablet |
| Reg. No. 51/20.2.8/0123 | Lopimune 40/10 Oral Pellets | Capsule |
| Reg. No. 55/20.2.8/0388 | Quadrimune | Capsule |

Both dosage forms are oral. Approved indication text and Essential Medicines List status were not supplied for these registrations.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a graph score, with no trials or publications for feline immunodeficiency. FIV protease may not respond to lopinavir, and the indication is veterinary. Lopinavir's value is already established in human HIV treatment. The safety review also cannot proceed until the SAHPRA PI data is obtained.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the approved indication text for the three SAHPRA registrations
- Direct evidence of lopinavir activity against FIV protease (in vitro or veterinary studies), and a decision on whether a veterinary indication falls within the scope of this human-health repurposing programme

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

