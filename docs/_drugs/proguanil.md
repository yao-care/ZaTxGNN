---
layout: default
title: Proguanil
parent: Model Prediction Only (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Proguanil
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

# Proguanil: From Malaria (Antimalarial Use) to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Proguanil is an antimalarial drug, registered in South Africa as the tablet product Trizivar. The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (proguanil is a known antimalarial) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 92.12% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Proguanil is known as an antimalarial prodrug. Its metabolite, cycloguanil, inhibits dihydrofolate reductase (DHFR), and it acts synergistically with atovaquone on mitochondrial function.

Smouldering systemic mastocytosis is a clonal mast cell disease, typically driven by KIT signalling. Established therapies target KIT. Neither the DHFR mechanism nor the mitochondrial mechanism is known to be relevant to KIT-driven mast cell proliferation.

The high score (0.92) is a graph-based prediction, and it probably reflects proximity to other mastocytosis nodes in the knowledge graph rather than a drug-specific mechanism. The same pattern appears for the related predictions "systemic mastocytosis" and "lymphoadenopathic mastocytosis with eosinophilia". No clinical or literature evidence corroborates any of them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/20.2.8/0434 | Trizivar | Tablet (oral) | Not stated in the registration data |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5): no trials or publications exist for proguanil in this disease, and no plausible link to KIT-driven mast cell biology is documented. Without the PI safety information, the candidate also cannot pass the first safety screen.

**To proceed, the following is needed:**
- The SAHPRA package insert for Trizivar, to obtain warnings, contraindications and the approved indication
- Mechanism of action data (for example from DrugBank) for a proper mechanistic-link analysis
- Preclinical testing (for example in mast cell lines) to show any activity in mastocytosis
- A route-compatibility and similarity assessment against the original indication (both currently pending)

The other nine predictions (including systemic mastocytosis and several polycystic kidney and liver disease entries) are also L5 with a Hold recommendation. The publications retrieved for polycystic kidney/liver disease are disease-level guidelines and reviews that do not mention proguanil as a treatment.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

