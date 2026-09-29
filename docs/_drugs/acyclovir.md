---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpesvirus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is an antiviral used against herpesvirus infections such as herpes simplex and herpes zoster.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but this is a graph-based prediction only, with **0 clinical trials** and **2 publications** that do not link acyclovir to the condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpesvirus infections (HSV/VZV). The registration records provided contain no approved-indication text. |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. From the mechanistic analysis, acyclovir is phosphorylated by viral thymidine kinase and then inhibits herpesvirus DNA polymerase. This is why it works against HSV and VZV.

The high score (0.997) most likely reflects graph proximity between acyclovir and eye-surface viral disease, not a proven mechanism. Punctate epithelial keratoconjunctivitis is often adenoviral or microsporidial. Neither pathogen is targeted by acyclovir. Adenovirus lacks the viral thymidine kinase needed to activate the drug, and microsporidia are intracellular parasites.

The mechanistic link is therefore weak. Efficacy would only be plausible if a specific case were herpetic in origin, which would be a different diagnosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case series | Am J Ophthalmol | Two AIDS patients treated for opportunistic infections developed drug-induced corneal lipidosis. No acyclovir link is evident. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Characteristics of microsporidial keratoconjunctivitis in an eastern Indian cohort. No acyclovir link is evident. |

Neither publication supports acyclovir as a treatment for this condition.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 28/20.2.8/0369 | Adco-acyclovir | Cream (topical) |
| Reg. No. 38/20.2.8/0129 | Acitab-200 dt | Effervescent tablet (oral) |

Approved-indication text was not captured for either product. Neither registration is an ophthalmic formulation, so route compatibility with an ocular indication has not been established.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no supporting literature, and the mechanism does not fit the likely causes (adenovirus, microsporidia). The evidence level is L5, model prediction only.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications, which are a blocking gap for safety screening
- Confirmed mechanism of action data, for example from DrugBank
- Evidence that a herpesvirus-driven subset of this condition exists and responds to acyclovir
- An ophthalmic route assessment, since no ocular formulation is registered in South Africa

Other predicted indications in this Evidence Pack are better supported. Common wart (L2) has several trials of intralesional acyclovir, though these are small and mostly unknown-status. These should be evaluated as separate candidates rather than through this one.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

