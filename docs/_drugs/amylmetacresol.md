---
layout: default
title: Amylmetacresol
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Throat Antisepsis to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is a topical antiseptic used in throat lozenges. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on knowledge-graph proximity alone and is not backed by any mechanistic or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Throat antisepsis (lozenge use); the SAHPRA record provides no indication text |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amylmetacresol is a topical antiseptic used in throat lozenges. Weak sodium channel blockade has been suggested in vitro, but this is unconfirmed.

**The prediction is not mechanistically supported.** Cauda equina syndrome is a compressive neurological emergency that needs urgent surgical decompression. An oropharyngeal antiseptic with minimal systemic exposure has no plausible role in treating it. The high TxGNN score (0.9999) reflects proximity in the knowledge graph, not evidence of benefit.

The other top predictions show the same pattern. They include irritable bowel syndrome, uveitis and other ocular conditions, and an obsolete neurogenic bladder term. None has clinical or preclinical data, and none has a supported mechanistic link. The ocular predictions are particularly weak, because the product is formulated for oropharyngeal use and no ocular safety data exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. W/2.7/142 | Nurofen period pain (was Nurofen extra s… (name truncated in source record) | Tablet (oral) | Not listed in the source record |

Essential Medicines List (EML) status was not provided in the source record.

The source record lists only one registration, and it is a tablet. Amylmetacresol is normally a lozenge ingredient, so the product name and formulation should be checked against the SAHPRA register.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The DrugBank interaction query returned no records for this drug. That does not mean no interactions exist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials, publications or plausible mechanism. It is a knowledge-graph output only (L5). The intended condition needs surgical decompression, so an oropharyngeal antiseptic is not a credible candidate.

**To proceed, the following is needed:**
- The SAHPRA package insert, to obtain warnings and contraindications. Safety screening cannot start without it.
- Mechanism of action data (for example from DrugBank) to test whether any link to the predicted indication exists.
- Confirmation of the registered product, formulation and approved indication (see the note under South Africa Market Information).
- Any preclinical or clinical evidence for the predicted indication. Without it, the candidate should not advance beyond S0.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

