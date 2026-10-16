---
layout: default
title: Dexchlorpheniramine Maleate
parent: Model Prediction Only (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexchlorpheniramine Maleate: predicted new indication Acute intermittent porphyria (evidence level L5). Approved use: Not stated in the SAHPRA registration data compiled for this report (…"
---

# Dexchlorpheniramine Maleate
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

# Dexchlorpheniramine Maleate: From Allergic Conditions to Acute Intermittent Porphyria (Prediction Only)

## One-Sentence Summary

Dexchlorpheniramine maleate is a first-generation H1-antihistamine, registered in South Africa as single-ingredient tablets and syrup.
The TxGNN model predicts it may be effective for **acute intermittent porphyria** (score 99.1%), but **no clinical trials and no publications** support this prediction.
The prediction is graph-based only, and first-generation antihistamines are listed as potentially unsafe in some porphyria drug databases.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data compiled for this report (a first-generation H1-antihistamine, generally used for allergic conditions) |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexchlorpheniramine is a first-generation H1-antihistamine with anticholinergic activity. It is used for allergic conditions, but the SAHPRA registration data compiled for this report contain no indication text.

**The prediction is not mechanistically supported.** Acute intermittent porphyria is caused by a deficiency of porphobilinogen deaminase (HMBS). H1-receptor antagonism does not act on this pathway. The high TxGNN score reflects graph-based associations, not pharmacological reasoning.

**There is also a safety concern.** First-generation antihistamines are listed as potentially unsafe in some porphyria drug databases, so safety must be reviewed before any further consideration.

### Other Predictions Reviewed

Nine further predictions were reviewed. Only one has a plausible mechanism.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Nephrogenic syndrome of inappropriate antidiuresis | 98.4% | L5 | No plausible mechanism (AVPR2/GNAS gain-of-function) |
| 3 | Porphyria | 97.7% | L5 | Parent category of rank 1; same safety concern |
| 4 | Schizophrenia | 97.2% | L5 | Weak and speculative; anticholinergic activity could worsen cognition |
| 5 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 97.1% | L5 | Genetic malformation; likely a graph artifact |
| 6 | Allergic urticaria | 97.0% | L4 | Biologically coherent, but likely within or adjacent to existing use, so not true repurposing |
| 7 | Syndromic myopia | 96.8% | L5 | Very indirect anticholinergic inference |
| 8 | Atypical glycine encephalopathy | 96.7% | L5 | No mechanistic link; sedating antihistamines may lower seizure threshold |
| 9 | Myopia 26, X-linked, female-limited | 96.7% | L5 | Monogenic; no mechanistic link |
| 10 | Myopia X-linked | 96.6% | L5 | Likely driven by shared graph neighbours |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (acute intermittent porphyria), currently no related literature available.

For rank 6 (allergic urticaria), one publication was retrieved. It is indirect, old, and not an RCT:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Case-based clinical/immunological study | Dermatologica | Single case of acquired heat contact urticaria in a young woman, with a minimum urtication temperature of 44 °C. Immunoglobulins and complement were normal and C1-inhibitor was slightly decreased. It does not test dexchlorpheniramine. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 48/21.5.4/0075 | Betadexamine Tablets | Tablet (oral) | Not available in the data compiled |
| Reg. No. A40/21.5.4/0623 | Betadexamine | Syrup | Not available in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status could not be determined from the data compiled.

## Safety Considerations

- **Porphyria:** First-generation antihistamines are listed as potentially unsafe in some porphyria drug databases. This must be checked before any consideration of use in porphyria.
- **Anticholinergic activity:** This could worsen cognition (relevant to the schizophrenia prediction).
- **Seizure threshold:** Sedating antihistamines may lower the seizure threshold in susceptible patients (relevant to the glycine encephalopathy prediction).

No drug interaction records were found. Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, no literature, and no plausible mechanism. A porphyria safety concern also exists for this drug class. The only biologically coherent prediction, allergic urticaria, falls within the drug's usual use as an antihistamine, so it is not true repurposing.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI), including approved indications, warnings and contraindications. This is currently a blocking data gap.
- Mechanism of action data (for example from DrugBank).
- A porphyria safety review (for example against recognised porphyria drug-safety databases) before any further work on the porphyria predictions.
- Direct clinical or literature evidence for any prediction that is to be pursued. For allergic urticaria, the question is whether it is genuinely new compared with the registered use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

