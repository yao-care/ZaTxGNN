---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amylmetacresol: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
monitor_inn: "Amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Amylmetacresol: From Throat Antiseptic Use to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is a mild antiseptic, typically used in throat lozenges. In South Africa it is registered as a single-ingredient oral tablet product.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (the drug is generally known as a throat antiseptic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amylmetacresol is a topical antiseptic used in throat lozenges. It has been reported to have weak local anaesthetic-like activity, possibly through sodium channel blockade.

Cauda equina syndrome is a surgical emergency caused by compression of the lumbosacral nerve roots. It requires urgent decompression. No plausible mechanistic link between a lozenge antiseptic and this condition has been identified. The high TxGNN score (0.9999) reflects graph-based proximity only, not biological or clinical evidence.

Other top-ranked predictions (all L5, all Hold) are also unsupported by any trial or publication:

| Rank | Predicted Indication | TxGNN Score | Comment |
|---|---|---|---|
| 2 | Obsolete neurogenic bladder | 99.96% | Obsolete ontology term, likely a knowledge-graph artefact |
| 3 | Irritable bowel syndrome | 99.89% | Speculative visceral neuron effect; minimal gut exposure from lozenges |
| 4 | Ciliary body disease | 99.70% | No support for ocular delivery |
| 5 | Panuveitis | 99.68% | No pharmacokinetic rationale for ocular exposure |
| 6 | Iris disease | 99.63% | Nonspecific term, no mechanistic link |
| 7 | Infectious anterior uveitis | 99.57% | A topical lozenge antiseptic would not reach the anterior chamber |
| 8 | Uveitis | 99.53% | Ocular anti-inflammatory effect not characterised |
| 9 | Ciliary body cancer | 99.46% | No antineoplastic activity reported |
| 10 | Benign neoplasm of ciliary body | 99.45% | No plausible mechanism, little therapeutic need |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| W/2.7/142 | Nurofen period pain (was Nurofen extra s...) | Tablet (oral) | Not stated in the data compiled |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug-drug interaction records were found for this drug in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials or publications, and no plausible mechanism links a topical oropharyngeal antiseptic to cauda equina syndrome or to any of the other top-ranked predictions. Systemic or target-tissue exposure is also unsupported. Because the safety documentation is missing, the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications, obtained by downloading and parsing the package insert
- Mechanism of action data (for example from DrugBank) to allow a proper mechanistic analysis
- Confirmation of the approved indication and active ingredients of the registered product, as the registration record lacks indication text
- Any preclinical or clinical evidence for the predicted indication, plus a route and exposure assessment showing the drug could reach the target tissue
- A review of whether the higher-ranked predictions (such as the obsolete neurogenic bladder term) are knowledge-graph artefacts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

