---
layout: default
title: Vildagliptin
parent: Model Prediction Only (L5)
nav_order: 468
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Vildagliptin is a DPP-4 inhibitor used to lower blood glucose in type 2 diabetes. The SAHPRA records provided do not state an indication.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from drug class and the literature; the SAHPRA records provided leave indication text blank) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Vildagliptin is a DPP-4 inhibitor that raises active GLP-1 and GIP and suppresses glucagon. Its efficacy in type 2 diabetes is well established, but nothing in the supplied data shows a mechanism for neurological benefit.

Stiff person syndrome is an autoimmune neurological disorder. It is often associated with anti-GAD65 antibodies and coexisting type 1 diabetes. This overlap with diabetes may explain why the knowledge graph links it to a diabetes drug. It is a network association, not a demonstrated pharmacological link. The very high score is more likely a graph-proximity effect than a real therapeutic signal.

The next four predictions (focal stiff limb syndrome, opsismodysplasia and two similar lipodystrophy-type conditions) show the same pattern. They are prediction-only, with no plausible DPP-4 mechanism in the data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 57/21.2/0061 | Vileptin Co 50/1 000 | Tablet |
| Reg. No. 57/21.2/0060 | Vileptin Co 50/850 | Tablet |

Both products are oral tablets. The strengths are consistent with fixed-dose vildagliptin–metformin combinations, though the record does not state this. Approved indication text and Essential Medicines List (EML) status are not available in the record.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature and no plausible mechanism in the supplied data. Nothing supports moving stiff person syndrome forward.

**Other predictions in the pack:**
- **Type 1 diabetes mellitus** (rank 10, score 99.37%) has the strongest evidence at L3, marked "Research Question".
- It is supported by small human studies, including a glucagon counterregulation study (PMID 22855332), a randomized Ramadan adjunct trial (PMID 38057844), and rodent beta-cell studies.
- The rapamycin plus vildagliptin randomized trial (PMID 33124663) is confounded by the combination.
- The 50 registry trials matched to that term are mostly type 2 diabetes studies and should not be counted as type 1 evidence.
- Efficacy and safety with insulin, especially hypoglycaemia, remain unestablished.

**To proceed, the following is needed:**
- SAHPRA Professional Information (PI) warnings and contraindications. This is currently a blocking gap.
- Mechanism of action data from DrugBank, to enable mechanistic-link analysis.
- For stiff person syndrome, any clinical or mechanistic evidence at all. Without it, no further work is justified.
- If type 1 diabetes is pursued, a dedicated review of type 1-specific studies and a hypoglycaemia safety assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

