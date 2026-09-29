---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Lower Urinary Tract Symptoms to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is an alpha-1A/1D adrenergic antagonist used as a symptomatic treatment for lower urinary tract symptoms.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is model-only and has no plausible pharmacological basis, so it should be treated as a statistical artefact until proven otherwise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the SAHPRA data received (tamsulosin is an alpha-1A/1D antagonist for lower urinary tract symptoms) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% (rank 70) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tamsulosin is known to block alpha-1A/1D adrenergic receptors, which relaxes smooth muscle in the lower urinary tract. This is a symptomatic effect and does not modify disease biology.

Ambras syndrome is a genetic disorder caused by a chromosomal rearrangement affecting the MYC/TRPS1 region. No known mechanism connects alpha-1 blockade to this cause, or to the regulation of hair growth in general.

The high score most likely reflects proximity in the knowledge graph between hair-related phenotypes and the drug's neighbours, not real biology. The other top-ranked predictions show the same pattern. Most are hair disorders such as hypertrichosis, hair shaft abnormalities, hypotrichosis and alopecia. None has any trial or supporting efficacy literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR and PACTR entries were not found in the Evidence Pack).

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Tamsulosin is marketed in South Africa under 8 SAHPRA registrations. Five are shown below. The approved-indication text and Essential Medicines List status are not recorded in the data received.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 53/34/0057 | Uriwel | Capsule |
| Reg. No. 48/34/0855 | Pravlex SR 0,4 mg | Capsule |
| Reg. No. 56/34/0989 | Urilosin 0,4 | Capsule |
| Reg. No. A40/34/0317 | Prostaflo SR | SRC |
| Reg. No. 56/21.12/1063 | Firsoltam | MRT |

---

## Safety Considerations

Drug interaction search returned no records. Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The Evidence Pack notes that tamsulosin can cause orthostatic hypotension and dizziness. This matters for any repurposing in a population where those effects would be a concern.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no trials or supporting literature, and there is no plausible mechanism linking alpha-1 blockade to a genetic hypertrichosis syndrome. The SAHPRA safety documentation is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- SAHPRA Professional Information (warnings and contraindications), obtained by downloading and parsing the package insert
- Mechanism of action data from DrugBank
- A credible biological hypothesis linking tamsulosin to the MYC/TRPS1-related pathology, plus any preclinical evidence
- A review of whether the score reflects co-prescription or knowledge-graph artefacts rather than a therapeutic signal

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

