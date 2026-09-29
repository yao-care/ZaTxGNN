---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From Obstructive Airway Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is an ultra-long-acting inhaled beta2-agonist, used in obstructive airway disease (COPD and asthma) and marketed in South Africa within combination inhalers.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a very high score (99.54%).
However, there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obstructive airway disease (COPD and asthma), inferred from trial and literature context. The SAHPRA registration data supplied contains no indication text. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, indacaterol is a long-acting beta2-adrenergic agonist that relaxes airway smooth muscle. Its efficacy in obstructive airway disease is well established, but this does not translate to NSIAD.

NSIAD is a rare condition caused by gain-of-function variants in the vasopressin V2 receptor. This leads to inappropriate water retention and low blood sodium. The review of this candidate found no plausible pathway linking beta2 agonism to V2-receptor over-activity. The high score most likely reflects the structure of the knowledge graph rather than a biological rationale.

The prediction should therefore be treated as a hypothesis-generating signal only. It is not a basis for clinical use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Both registered products are combination inhalers containing indacaterol. They are not indacaterol-alone products.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 54/10.2.1/0870.867 | Bemrist Breezhaler 150/80 | Capsule |
| Reg. No. 54/10.2.1/0875.873 | Zimbus Breezhaler 150/50/80 | Capsule |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NSIAD prediction has no supporting trials or publications and no identifiable mechanistic link. Indacaterol acts on beta2 receptors, while NSIAD is driven by V2-receptor gain-of-function. There is no basis to move this candidate forward.

Among the other predictions for this drug, only "bronchial disease" (rank 7) has substantial evidence (L1, several large Phase 3 RCTs). That evidence reflects indacaterol's established respiratory use, not a new repurposing opportunity. Most of those trials also test combination products, so effects cannot be attributed to indacaterol alone.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (PI), covering approved indications, warnings and contraindications
- Mechanism of action data from DrugBank
- A biologically plausible pathway linking beta2 agonism to NSIAD, supported by preclinical or clinical data
- Any published case reports or trials on indacaterol or other beta2-agonists in NSIAD
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

