---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Mometasone
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

# Mometasone: From Inflammatory Skin and Nasal Conditions to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a corticosteroid marketed in South Africa as a cream and as nasal sprays. The TxGNN model predicts it may be useful for **primary cutaneous T-cell lymphoma**, but this is a computational prediction only. There are **0 clinical trials** and **2 case reports** (neither tests mometasone) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records provided (products are a cream and nasal sprays) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the records provided. Mometasone is a topical glucocorticoid, and this class has anti-inflammatory and immunosuppressive effects. In theory, these could reduce the T-cell infiltrate and symptoms in early patch or plaque skin disease. The supplied data does not document this, so it remains a hypothesis.

The two retrieved papers do not evaluate mometasone for this condition. One is a case of cutaneous pseudolymphoma, a benign mimic of lymphoma, treated with tapinarof after mometasone and tacrolimus failed. The other is a case report of childhood mycosis fungoides. The very high TxGNN score reflects proximity in the knowledge graph, not proof of benefit.

Nine other predictions (for example Crohn's colitis, myelodysplastic syndrome and cystic teratoma) have no trials or literature. They are all rated L5 and Hold. Several of them, such as the chromosome 5 deletion and the dermoid and teratoma entries, have no plausible glucocorticoid mechanism and are likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov, ICTRP, SANCTR or PACTR).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proc (Bayl Univ Med Cent) | Refractory cutaneous pseudolymphoma (a benign mimic of lymphoma) did not respond to mometasone and tacrolimus and was then treated with tapinarof. It gives no support for mometasone benefit. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | J Cutan Pathol | An 11-year-old boy with CD8+CD56+ mycosis fungoides, a primary cutaneous T-cell lymphoma. Mometasone was not evaluated. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. A38/13.4.1/0668 | Aspen mometasone | Cream | Not stated in the record |
| Reg. No. 52/21.5.1/0538 | Rhinimet | Spray | Not stated in the record |
| Reg. No. 53/21.5.1/0457 | Ryaltris | Spray | Not stated in the record |

Only the cream is a skin product. The two sprays are not suited to skin lymphoma, so any exploration would rely on the cream.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trial tests mometasone in cutaneous T-cell lymphoma, and the two case reports do not evaluate it. The safety information from the PI has not been reviewed, which blocks progression to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), so safety screening can begin
- Mechanism of action data from DrugBank
- A targeted literature search for topical corticosteroid use in early-stage mycosis fungoides and cutaneous T-cell lymphoma
- Confirmation of the approved indications for the three registered products
- Clinical input on whether topical corticosteroids already have an established supportive role in this disease, since this may make the prediction a known use rather than a new one

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

