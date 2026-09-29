---
layout: default
title: Pyridoxine
parent: Model Prediction Only (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Pyridoxine
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

# Pyridoxine: From Vitamin B6 Replacement to Gonococcal Urethritis

## One-Sentence Summary

Pyridoxine (vitamin B6) is a widely marketed vitamin used to replace or supplement B6. The TxGNN model predicts it may be effective for **gonococcal urethritis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It is a model-only signal with no known mechanism, and no antibacterial activity against *Neisseria gonorrhoeae* is known.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (vitamin B6 replacement is inferred and should be checked against the product label) |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 93.87% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pyridoxine is a precursor of pyridoxal 5'-phosphate (PLP), a cofactor for enzymes involved in amino acid, neurotransmitter, homocysteine and haem metabolism. Its established role is correcting B6 deficiency, not treating infection.

The link between this role and gonococcal urethritis is weak. Gonococcal urethritis is a bacterial sexually transmitted infection treated with antibiotics, and pyridoxine has no known antibacterial activity against *N. gonorrhoeae*. The score of 0.9387 is identical to that of Ureaplasma urethritis (rank 2). This suggests the model is picking up a shared "urethritis" graph neighbourhood rather than a signal specific to this indication. The score should therefore be read as a hypothesis-generating flag, not as evidence of efficacy.

Among the other predictions, only "vitamin deficiency disorder" (rank 10) has meaningful supporting evidence. That is essentially replacement therapy, not true repurposing, and it is outside the scope of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Pyridoxine appears in 20 SAHPRA registrations, mainly as a component of multivitamin and vitamin B-complex products. The approved indication text was not provided for any of the listed products, and Essential Medicines List (EML) status was not included in the supplied data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2611 (ACT 101/1965) | Becoplex ido vial 10ml | Injection | Not stated in supplied data |
| T1012 (ACT 101/1965) | Beespan | Capsule | Not stated in supplied data |
| H2412 (ACT 101/1965) | A-lennon vitamin b co ampoule 2ml | Injection | Not stated in supplied data |
| H2975 (ACT 101/1965) | Vitamin b co 10ml | Injection | Not stated in supplied data |
| U/2.6/218 | Restin | Capsule | Not stated in supplied data |

Available dosage forms across all registrations are injection, capsule, tablet, infusion and TPN.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No drug interaction records were found for pyridoxine in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score, with no clinical trials, no publications and no plausible antibacterial mechanism. The identical score for Ureaplasma urethritis points to a shared-neighbourhood artefact. Gonococcal urethritis also has effective standard antibiotic treatment, so there is no evidence-based reason to pursue pyridoxine here.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that pyridoxine has activity against *N. gonorrhoeae* or urethritis
- Mechanism of action data for pyridoxine and confirmation of the approved indications from the SAHPRA-approved PI
- SAHPRA package insert warnings and contraindications
- A route and formulation compatibility assessment for the proposed use

This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

