---
layout: default
title: Cilazapril
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cilazapril: From Hypertension to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Cilazapril is an ACE inhibitor marketed in South Africa. The registration data supplied do not state its approved indication, but it is understood to be used as an antihypertensive. The TxGNN model predicts it may be useful for **pulmonary hypertension with unclear multifactorial mechanism**, but there are currently **0 clinical trials** and **no drug-specific publications** supporting this direction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data supplied (cilazapril is understood to be an antihypertensive; the approved label must be verified) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available for this drug. Cilazapril is an ACE inhibitor, a class that lowers angiotensin II and reduces vasoconstriction. Its efficacy in systemic hypertension is class-established, and mechanistically it might be applicable to pulmonary vascular disease.

However, none of the supplied data link cilazapril to pulmonary vascular disease. ACE inhibitors are not an established therapy for pulmonary arterial hypertension. The high TxGNN score (0.992) reflects a pattern in the knowledge graph, not confirmed pharmacology. The predicted disease group also spans several different mechanisms, which makes a single drug rationale harder to justify.

Two other predictions for this drug are closer to its known pharmacology. They are malignant renovascular hypertension and malignant hypertensive renal disease, both RAAS-dependent conditions. Both are classed as research questions (L4, class-level reasoning only) and are worth a separate review.

## Clinical Trial Evidence

Currently no related clinical trials registered. This applies to ClinicalTrials.gov and to the ICTRP search, and no SANCTR or PACTR records were supplied.

## Literature Evidence

No drug-specific literature is available. The retrieval returned 20 publications for the related predicted condition, pulmonary hypertension owing to lung disease and/or hypoxia. They are keyword matches on "hypoxia" and cover general hypoxia biology in neurology, oncology, fibrosis and altitude physiology. Based on the titles and available abstracts, none mentions cilazapril or ACE inhibitors. No publications were retrieved for the top-ranked indication itself. These papers should not be counted as supporting evidence.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/7.1.3/0022 | Inhibace plus 5mg/12.5mg | Tablet (oral) | Not stated in the data supplied |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

No interaction records were found in the DDI query. Two class-level concerns from the assessment need attention before any use in this setting:
- Systemic vasodilators can worsen ventilation-perfusion matching in hypoxic lung disease.
- ACE inhibitors carry a risk of renal function decline and hyperkalaemia in patients with compromised kidneys.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials and no drug-specific literature. The mechanistic link is unproven, and there is a plausible safety concern, since systemic vasodilation may worsen oxygenation in hypoxic lung disease. Key regulatory and safety data are also missing.

**To proceed, the following is needed:**
- The SAHPRA package insert (PI) to confirm the approved indication, warnings and contraindications. This is currently a blocking gap.
- Mechanism-of-action data for cilazapril, for example from DrugBank.
- A literature search for class-level evidence on ACE inhibitors in pulmonary hypertension, especially hypoxia-related forms.
- A separate review of the malignant renovascular hypertension and malignant hypertensive renal disease predictions, which are more plausible.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

