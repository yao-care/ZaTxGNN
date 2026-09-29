---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Depression and Anxiety to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant, used mainly for major depressive disorder, generalized anxiety disorder and chronic pain conditions.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data. The literature describes approvals for major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia and chronic musculoskeletal pain |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Duloxetine is an SNRI, and its efficacy in depression and anxiety is established. However, no plausible mechanism has been identified for this new indication.

Benign paroxysmal torticollis of infancy is a paroxysmal paediatric disorder, often linked to CACNA1A (a calcium-channel gene) and therefore likely a channelopathy. Serotonin and norepinephrine reuptake inhibition has no clear relevance to that pathology. The high TxGNN score most likely reflects proximity in the knowledge graph rather than a real biological link.

Duloxetine's safety in children is also a concern, which further weakens the case for this prediction.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 50/1.2/0849 | Duloxetine XR 30 Biotech | Capsule | Not stated in the registration data |
| Reg. No. 54/1.2/0590 | Duloxetine MR 60 Unicorn | Capsule | Not stated in the registration data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no registered trials, no literature and no plausible mechanism. The target population is paediatric, and duloxetine's paediatric safety is a concern.

Among the other top-10 predictions for duloxetine, **obsessive-compulsive disorder** has the most support. It has one completed small Phase 4 trial (NCT00464698, n=20) and a double-blind augmentation RCT (PMID 27811556). It is still only a research question, because there is no Phase 3 confirmation and first-line SSRIs and clomipramine remain the standard of care. Agoraphobia has only indirect evidence from panic disorder and GAD studies.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Any published preclinical or clinical evidence linking duloxetine to this condition
- A paediatric safety assessment before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

