---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Superficial Skin and Inflammatory Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is a long-established keratolytic and anti-inflammatory agent, used for skin conditions such as acne, seborrhoeic dermatitis and tinea, and for inflammatory joint conditions.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. The knowledge graph lists tinea pedis, acne, seborrhoeic dermatitis, rheumatoid arthritis, allergic rhinitis and others |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Salicylic acid is proposed to act through inhibition of cyclooxygenase (COX) enzymes, which reduces prostaglandin synthesis and inflammation. However, no publicly available bioactivity data confirming this at a specific molecular target were found. Pharmacology data list ASIC3 as an associated target, but this is not confirmed as a primary mechanism.

The link to papillary conjunctivitis is plausible but indirect. Salicylic acid is already listed for allergic rhinitis, another allergic mucosal condition, and papillary conjunctivitis involves allergic or inflammatory irritation of the conjunctiva. Salicylic acid is also keratolytic and irritating to mucous membranes, so tolerability in the eye is a real concern. The very high TxGNN score reflects model proximity in the knowledge graph, not clinical evidence.

### Other Predictions Reviewed

Nine other predictions were also evaluated. All lack trials and literature.

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.78% | L5 | No credible mechanistic link; likely a knowledge-graph artefact |
| Brachydactyly-syndactyly syndrome | 99.73% | L5 | No credible mechanistic link |
| Brachyolmia-amelogenesis imperfecta syndrome | 99.55% | L5 | No credible mechanistic link |
| Rosacea conjunctivitis | 99.53% | L5 | Weak, speculative link via facial inflammatory skin disease; eye irritation concern |
| Acromesomelic dysplasia, Hunter-Thompson type | 99.52% | L5 | No credible mechanistic link |
| Pseudoachondroplasia | 99.51% | L5 | No credible mechanistic link |
| Myosclerosis | 99.49% | L5 | Tenuous, speculative link; no evidence on fibrosis |
| Brachyolmia | 99.44% | L5 | No credible mechanistic link |
| Spondyloarthropathy, susceptibility to | 99.34% | L4 | Plausible class-level rationale: NSAIDs are first-line symptomatic therapy. Treated as a research question needing a dedicated literature review |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| L13.4.1/66 | Diprosalic | Lotion | Not available in the data compiled for this report |
| H/13.4.1/32 | Diprosalic | Ointment | Not available in the data compiled for this report |

Both registrations are valid and are topical products. Essential Medicines List (EML) status was not available in the data compiled for this report.

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned one pharmacology entry, linking salicylic acid to the ASIC3 target. No drug-drug interactions with severity levels were identified.
- **Local tolerability** (from the mechanistic assessment): Topical salicylic acid is keratolytic and irritating to mucous membranes and the eye, which is a significant concern for any ocular use.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis rests only on a computational score, with no trials or literature, and ocular irritation is a major tolerability concern. Most other top-ranked predictions have no credible mechanism. The only one with a plausible class-level rationale is spondyloarthropathy, which is a research question rather than an actionable candidate.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank
- A systematic literature search on salicylates in allergic and papillary conjunctivitis, and a separate review for spondyloarthropathy
- Assessment of ocular tolerability and of whether a suitable ophthalmic formulation exists, since the registered products are topical skin preparations (lotion and ointment) only
- Approved indication text for the registered Diprosalic products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

