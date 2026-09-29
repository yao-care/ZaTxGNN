---
layout: default
title: Carbidopa
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Carbidopa
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

# Carbidopa: From Parkinson's Disease Therapy to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Carbidopa is a peripheral DOPA decarboxylase inhibitor, used alongside levodopa in Parkinson's disease therapy.
The TxGNN model predicts it may be relevant to **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** currently support this prediction. It is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied SAHPRA data. Carbidopa is known as a levodopa adjunct in Parkinson's disease. |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 98.43% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record. Carbidopa inhibits peripheral DOPA decarboxylase. It has no therapeutic effect of its own and is only useful alongside levodopa, where it reduces peripheral conversion of levodopa to dopamine.

Rasmussen encephalitis is a rare, immune-mediated inflammatory brain disease. No plausible link between DOPA decarboxylase inhibition and this immune pathology was found in the supplied data. The high score (98.43%) therefore reflects a knowledge-graph association rather than a demonstrated biological rationale, and it should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Approved indication text was not included in the supplied registry extract.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 30/5.4.1/0269 | Carbilev 25/250 | Tablet | Not stated in extract |
| Reg. No. 32/5.4.1/0081 | Teva Carbi-Levo 25/100 | Tablet | Not stated in extract |
| Reg. No. 45/5.4.1/0765 | Lecardop 25/100 | Tablet | Not stated in extract |
| Reg. No. 8/5.4.1/0138 | Stalevo 100/25 | Tablet | Not stated in extract |
| Reg. No. 38/5.4.1/0137 | Stalevo 150/37.5 | Tablet | Not stated in extract |

All registered products are oral tablets.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no trials, no literature and no plausible mechanism. Safety data from the SAHPRA package insert have not yet been obtained, so the candidate cannot pass the first safety screen.

Among the other predicted indications, the strongest signal is not for this disease. It is for X-linked intellectual disability-ataxia-apraxia syndrome (Allan-Herndon-Dudley/MCT8 deficiency), where 2025–2026 observational reports describe levodopa/carbidopa response (L3, Research Question). The disease-label mapping there is uncertain and should be verified first.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDFs)
- Mechanism of action data (e.g. from DrugBank)
- Approved indication text for the five registered products
- Any published or registered evidence linking carbidopa to Rasmussen encephalitis. Without it, further pursuit of this indication is not justified.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

