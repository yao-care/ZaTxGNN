---
layout: default
title: Clobetasol Propionate
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 7
---

# Clobetasol Propionate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Clobetasol Propionate: From Topical Corticosteroid Therapy to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Clobetasol propionate is a super-potent topical corticosteroid, marketed in South Africa as a spray and an ointment. The TxGNN model predicts it may be useful for **vulvar inverted follicular keratosis**, a benign follicular skin lesion. Currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied SAHPRA data (approved indication text is blank) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clobetasol propionate is a potent topical corticosteroid, and mechanistically it may be applicable to this lesion.

A potent topical corticosteroid could plausibly reduce local inflammation in a benign follicular lesion. However, no mechanism-specific evidence supports this. This lesion is usually managed by excision or observation rather than drug therapy, which weakens the rationale for medical treatment. The high model score should therefore be treated as a hypothesis-generating signal, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvar inverted follicular keratosis. No SANCTR or PACTR entries were retrieved.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 46/13.4.1/0556 | Clobex 120ml | Spray | Not recorded |
| Reg. No. 27/13.4.1/0122 | Dovate | Ointment | Not recorded |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and the disease is usually treated by excision or observation. Safety information from the SAHPRA package insert has not yet been retrieved, so safety screening cannot start.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data (for example, from DrugBank)
- A targeted literature review of topical corticosteroid use in inverted follicular keratosis
- The original approved indication text for both registrations

**Other predictions in this pack (for context only):**

| Rank | Predicted Indication | Evidence Level | Note |
|------|------|------|------|
| 3 | Exanthem (disease) | L4 | 10 trials shown (21 listed, 11 not provided), mostly lichen sclerosus and oral lichen planus. Evidence is indirect because "exanthem" is too broad. Re-mapping to lichen planus or lichen sclerosus would likely raise the level to L2. |
| 4 | Acne keloid | L4 | One 2005 open-label study of clobetasol and betamethasone foams in acne keloidalis (20 patients). No controlled trial registered. |
| 2 | Acrodermatitis chronica atrophicans | L5 | Weak rationale: antibiotics are standard, and a corticosteroid could worsen skin atrophy. |
| 5–7 | Neonatal dermatomyositis, childhood connective-tissue-disease interstitial lung disease, amyopathic dermatomyositis | L5 | Prediction only. Neonatal use of a super-potent agent and lung disease are poor fits for a topical drug. |

Ranks 3 and 4 have the most evidence and would be the more productive candidates to investigate first. All results are for research reference only and are not medical advice. Any repurposing candidate requires clinical validation before use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

