---
layout: default
title: Dl-Alpha-Tocopherol
parent: Moderate Evidence (L3-L4)
nav_order: 188
evidence_level: L3
indication_count: 10
---

# Dl-Alpha-Tocopherol
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# DL-alpha-Tocopherol: From No Recorded Indication to Immature Cataract

## One-Sentence Summary

DL-alpha-Tocopherol is a synthetic form of vitamin E. It is registered in South Africa as a component of an infusion product, and no original indication is recorded in the data.
The TxGNN model predicts it may be relevant to **immature cataract**.
Support is thin: **0 registered clinical trials** and **1 publication** (a 1999 human study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (no approved indication text in the SAHPRA record or DrugBank) |
| Predicted New Indication | Immature cataract |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Alpha-tocopherol is a lipid-soluble antioxidant that limits lipid peroxidation in cell membranes. That property is the basis for the predicted link to cataract.

Oxidative damage to lens membranes and proteins is a recognised contributor to cataract formation. An antioxidant could therefore plausibly play a protective role. This link has not been tested in this evidence pack. Because no original indication is on record, no similarity between an original and a new indication can be assessed.

The score should be read with caution. TxGNN gave nearly identical scores (about 99.97%) to many cataract subtypes, including mature, tetanic, craniostenosis-associated and diabetic cataract. It also gave a similar score to antithrombin deficiency type 2, which has no plausible link to this drug. This pattern suggests the score reflects proximity in the knowledge graph rather than a signal specific to immature cataract.

The antioxidant rationale applies mainly to prevention or slowing of lens opacity. It is unlikely to reverse an already opacified lens.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10749028](https://pubmed.ncbi.nlm.nih.gov/10749028/) | 1999 | Human study (randomised, placebo-controlled per abstract; classified as observational, inferred from title only) | Annals of Nutrition & Metabolism | 50 patients with idiopathic immature senile cataract (25 cortical, 25 nuclear) received vitamin E or placebo for 30 days. Lens glutathione, vitamin E, malondialdehyde and glutathione peroxidase were measured. The abstract available here is truncated, so full results are not confirmed. |

This is a small, single study of about 50 patients. It measured biochemical markers in the lens, not vision or cataract progression. It is not evidence of a confirmed treatment effect.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 36/22.1/0508 | Cernevit | Infusion | Not recorded |

The only registered form is an injectable infusion. Whether an infusion suits a cataract-related use has not been assessed. The route of administration in the 1999 study is not shown in the available abstract.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and one small 1999 study of biochemical markers. No clinical trials are registered, and the near-identical scores across unrelated cataract subtypes point to graph artefact rather than a specific signal. Safety data from the SAHPRA package insert is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI PDF from the SAHPRA website)
- Mechanism of action data (query the DrugBank API)
- Full-text review of PMID 10749028 to confirm study design, outcomes and route of administration
- A systematic literature search for vitamin E and cataract, including randomised trials and meta-analyses
- Assessment of whether the registered infusion route is compatible with a cataract use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

