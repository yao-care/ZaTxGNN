---
layout: default
title: Azelastine
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Azelastine
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

# Azelastine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Azelastine is an H1-receptor antagonist (antihistamine). In South Africa it is registered as a component of Dymista Nasal Spray, and the trial data supplied are all in allergic rhinitis. The TxGNN model predicts it may be effective for **rosacea conjunctivitis** with a high score (98.6%). However, **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (inferred from the Dymista product and related trials; the SAHPRA record supplied has no indication text) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azelastine is a second-generation H1-receptor antagonist. Its efficacy in allergic rhinitis is well documented by the trials supplied, and mechanistically it may relieve histamine-driven eye symptoms.

The link to rosacea conjunctivitis is weak, however. Ocular disease in rosacea is driven mainly by meibomian gland dysfunction and inflammation, not by histamine. The high score reflects a pattern found by the model in the knowledge graph. It is not supported by biological or clinical evidence, and on its own it does not justify action.

## Clinical Trial Evidence

Currently no related clinical trials registered for rosacea conjunctivitis.

## Literature Evidence

Currently no related literature available for rosacea conjunctivitis.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 55/21.5.1/0573 | Dymista Nasal Spray | Spray |

Dymista is a nasal spray combining azelastine and fluticasone. Only the nasal route is registered, so an ophthalmic use would need a different formulation or route. No indication text or Essential Medicines List status was supplied.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model prediction only (L5). There are no trials or publications, the mechanistic rationale is unclear, and the only registered product is a nasal spray. The high score alone is not enough to move forward.

**To proceed, the following is needed:**
- Evidence that H1 blockade helps ocular rosacea (for example, mechanistic or clinical studies)
- The original indications and mechanism of action, to complete the mechanistic analysis
- The SAHPRA Professional Information, to complete safety screening
- An assessment of route compatibility (nasal spray versus an ophthalmic formulation)

**Note on other predictions for this drug:** Two lower-ranked predictions have more supporting data and are better candidates for follow-up as research questions (both L4).
- **Allergic urticaria** (score 96.2%): H1 blockade is the standard basis for urticaria treatment. The 10 supplied Phase 3/4 trials are all in allergic rhinitis, so the evidence is indirect. It supports safety and H1-class activity, but not efficacy in urticaria.
- **Conjunctivitis** (score 91.1%): Only the allergic subtype is plausible. One Phase 3 trial (NCT06212973) may involve azelastine eye drops, but this needs verification. Azelastine ophthalmic products may already be marketed for allergic conjunctivitis, so check labelling before counting this as repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

