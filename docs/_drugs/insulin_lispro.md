---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 266
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue used to control blood glucose in diabetes, and the South African registration record supplied here carries no indication text.
The TxGNN model predicts it may be effective for **autoimmune oophoritis** (score 99.78%).
This is a model prediction only: **0 clinical trials** and **0 publications** support this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (the registration record has no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.78% (model rank 1557) |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting insulin analogue. Its efficacy in glycaemic control is well established, but no data supplied here links it mechanistically to autoimmune oophoritis.

The high score most likely reflects associations in the knowledge graph, such as shared autoimmune features. It does not show that insulin treats ovarian autoimmune inflammation. No supplied trial, publication or mechanistic analysis supports a therapeutic effect, so this prediction should be treated as a hypothesis only.

Other candidates in the same prediction set show the same pattern:
- **Pancreatic agenesis** (rank 7, evidence level L4, "Research Question") is biologically plausible, because insulin replaces the missing hormone. The only supplied literature concerns insulin therapy in type 2 diabetes, so it is indirect evidence, and this would be replacement therapy rather than a new mechanism.
- **Stiff person syndrome** and **focal stiff limb syndrome** likely reflect the autoimmune and GAD-antibody overlap with type 1 diabetes. Insulin would treat the comorbid diabetes, not the neurological condition.
- **Drug-induced localized lipodystrophy**, **pressure-induced localized lipoatrophy** and **centrifugal lipodystrophy** probably reflect known injection-site adverse effects of insulin. They are not plausible therapeutic targets.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For reference, two general reviews were supplied under the lower-ranked candidate pancreatic agenesis. They cover insulin therapy in type 2 diabetes and are only indirect evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11727406](https://pubmed.ncbi.nlm.nih.gov/11727406/) | 2001 | Review | Endocrinol Metab Clin North Am | Insulin therapy in type 2 diabetes; intensive glucose control delays microvascular disease progression (UKPDS) |
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Practical aspects of starting insulin therapy in type 2 diabetes |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 29/21.1/0785 | Humalog vial 10ml | Injection | Not stated in the supplied record |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Injection-site lipodystrophy (lipohypertrophy and lipoatrophy) is a known adverse effect of injected insulin. Any exploration of lipodystrophy-related indications should treat it as a safety signal, not a therapeutic opportunity.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. No clinical trials, literature or supported mechanism exist for autoimmune oophoritis. Safety information for the South African product is also missing, and this blocks progression to safety screening.

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings and contraindications), so safety screening can begin
- Mechanism of action data for insulin lispro, for example from DrugBank
- Indication text from the SAHPRA registration to confirm the original indication
- Targeted searches for autoimmune oophoritis literature and trial registrations (ClinicalTrials.gov, SANCTR, PACTR)
- A separate review of pancreatic agenesis as the only candidate with a plausible replacement-therapy rationale

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

