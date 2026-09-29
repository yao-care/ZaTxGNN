---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol is an opioid analgesic that is currently marketed in South Africa. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder. There are **no clinical trials and no publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain (general pharmacological knowledge; the SAHPRA records provided do not include indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the Evidence Pack. Tramadol is generally described as a mu-opioid receptor agonist that also inhibits serotonin and norepinephrine reuptake, and it is used for symptomatic pain relief.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia linked to the CDMP1/GDF5 pathway. **No established mechanistic link** connects tramadol to this condition. At most, tramadol could offer symptomatic analgesia and would not change the course of the disease. The very high score of 99.99% is a knowledge-graph output and should not be read as evidence of efficacy.

The other top predictions show the same pattern. Most are rare skeletal or connective-tissue conditions (brachyolmia, pseudoachondroplasia, myosclerosis) or juvenile and rheumatoid arthritis variants. All are at evidence level L5, with no trials or literature. Where a link exists at all, it is indirect symptomatic pain relief. Paediatric use of tramadol is also restricted by safety concerns, including CYP2D6 ultra-rapid metabolism and respiratory depression.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

Tramadol has 9 SAHPRA registrations. The five main ones are listed below. Approved indication text and manufacturer details were not included in the data provided.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 32/2.9/0652 | Tramahexal | Capsule |
| Reg. No. 44/2.9/0496 | Tramazac SR | Sustained-release tablet (recorded as "Srt") |
| Reg. No. 36/2.9/0337 | Dolotram 50 | Injection |
| Reg. No. 37/2.9/0532 | Dolotram | Capsule |
| Reg. No. 54/2.9/0185 | Domadol Plus | Tablet |

Available routes are oral (capsule, tablet) and injectable.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note that the Evidence Pack flags paediatric restrictions for tramadol (CYP2D6 ultra-rapid metabolism and respiratory depression). This matters for any use in juvenile-onset conditions among the wider predictions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature, and no plausible disease-modifying mechanism links tramadol to this genetic skeletal dysplasia. Safety data from the SAHPRA package insert are also missing, so the candidate cannot progress to safety screening.

**To proceed, the following is needed:**
- SAHPRA package insert warnings and contraindications (download and parse the PI)
- Mechanism of action data from DrugBank
- Any published or registered clinical evidence for tramadol in this condition
- Approved indication text for the local registrations
- Route compatibility assessment against the needs of the target condition

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

