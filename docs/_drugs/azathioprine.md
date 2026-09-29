---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppression to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is an immunosuppressant that inhibits purine synthesis, and it is marketed in South Africa as tablets.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.999% (model rank 19) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on the mechanism summarised in the pack, azathioprine inhibits purine synthesis and suppresses the immune system.

This prediction has no plausible mechanistic link. The target condition is a rare developmental malformation syndrome with no known immune-mediated component for azathioprine to act on. The very high score most likely reflects graph-model proximity rather than biology. The score alone should not be read as a treatment signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 37/26/0692 | Azathioprine 50 pch | Tablet |
| Reg. No. D/26/98 | Imuran | Tablet |

Both products are oral tablets. The approved indication text and Essential Medicines List (EML) status are not recorded in the Evidence Pack. Please check the SAHPRA-approved Professional Information (PI) for these.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible mechanism. The target is a congenital malformation syndrome that immunosuppression is not expected to treat.

**Other candidates in the same Evidence Pack:** two other predicted indications have much stronger support. Both are rated L1 and "Proceed with Guardrails" in the pack.
- **Inflammatory bowel disease** (rank 5, score 99.52%) has Phase 3 trials, including NCT00094458 and NCT00098111 in Crohn's disease.
- **Ulcerative colitis** (rank 9, score 99.33%) has Cochrane reviews and the 2025 ACTIVE randomised trial.

Thiopurines are already established guideline therapy for these conditions, so they are better treated as established use than as new repurposing signals. Suggested guardrails from the pack are TPMT/NUDT15 testing, FBC and liver enzyme monitoring, and infection and lymphoma risk screening. A separate report focused on these two indications is recommended.

**To proceed with the rank 1 indication, the following is needed:**
- Any published or registered clinical evidence, or a credible mechanistic rationale, for azathioprine in this syndrome
- SAHPRA package insert warnings and contraindications (for any future safety screening)
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

