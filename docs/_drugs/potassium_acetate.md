---
layout: default
title: Potassium Acetate
parent: Model Prediction Only (L5)
nav_order: 376
evidence_level: L5
indication_count: 1
---

# Potassium Acetate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Potassium Acetate: From Parenteral Nutrition Electrolyte Supply to Renal Tubular Acidosis

## One-Sentence Summary

Potassium acetate is an electrolyte component in parenteral nutrition infusions marketed in South Africa. The registration records provided do not state an approved indication, so this use is inferred from the product names.
The TxGNN model predicts it may be useful for **renal tubular acidosis**, but **no clinical trials and no publications** currently support this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; products are parenteral nutrition infusions (inferred from product names) |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the input. The reasoning below is background pharmacology, not evidence from the Evidence Pack.

Potassium acetate supplies potassium, and acetate is metabolised in the body to bicarbonate. It could therefore act as an alkalinising agent and help correct potassium loss. This fits distal (type 1) renal tubular acidosis, where patients typically have metabolic acidosis with potassium depletion. Potassium citrate is the established agent in this setting and is the closest analogue.

The very high TxGNN score (99.90%) is a model prediction only. It may partly reflect the similarity of potassium acetate to other potassium salts and alkalinising agents in the knowledge graph. It does not replace clinical evidence.

The SAHPRA-registered products are multi-component parenteral nutrition infusions, not single-agent potassium acetate products. Whether a suitable formulation and route exist for renal tubular acidosis has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion |
| Reg. No. 52/25/0740 | Numeta G16E | Infusion |
| Reg. No. 49/25/0065 | Nutriflex Omega Specialized | Infusion |
| Reg. No. 41/25/0757 | Nutriflex lipid peri 1875ml | TPN |

The records show 6 registrations in total. The list above shows only 5 entries, and Reg. No. 41/25/0757 appears twice. Approved indication text and Essential Medicines List (EML) status were not provided in the input.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no registered trials or publications. The registered products are fixed-composition parenteral nutrition infusions, and no safety information was available for review. The pharmacological rationale is plausible but unverified.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data, for example from DrugBank
- A literature and trial search for potassium acetate or acetate-based alkalinisation in renal tubular acidosis, compared with potassium citrate
- Assessment of formulation and route suitability, since the registered products are intravenous multi-component infusions
- Approved indication text for each SAHPRA registration

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

