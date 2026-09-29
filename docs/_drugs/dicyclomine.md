---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 2
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Gastrointestinal Antispasmodic Use to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antimuscarinic antispasmodic that relaxes smooth muscle. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (general pharmacology: antispasmodic) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, dicyclomine is an antimuscarinic and antispasmodic that relaxes smooth muscle. At most, it could ease secondary bladder-muscle (detrusor) or bowel spasm in cauda equina syndrome.

The link is weak. Cauda equina syndrome is caused by nerve root compression and is a surgical emergency. Dicyclomine does not treat that cause. Its anticholinergic effect could also cause urinary retention and worsen bladder dysfunction in this setting. The high score (99.66%) is a model output only, with no trial or literature record behind it.

The second-ranked prediction is "obsolete neurogenic bladder (disease)" (score 99.50%). Antimuscarinic drugs are a recognised class for neurogenic detrusor overactivity, so that link is biologically more plausible. It also has no supporting trials or publications. The disease label is an obsolete ontology term, which points to a mapping-quality problem. It should be remapped to a current neurogenic bladder or neurogenic lower urinary tract dysfunction concept before further review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 33/20.2.2/0267 | Pinaspor V | Vcr |
| Reg. No. 32/11.4.2/0211 | Co-gel | Suspension |
| Reg. No. 41/1.2/0373 | Voxra Xl 150 | Tablet |
| Reg. No. 46/11.4.2/008 | Meddev | Syrup |

The registry entries carry no approved indication text. The product-to-ingredient matching should be verified against the SAHPRA Professional Information (PI) before any use of these registrations.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or publications. The proposed mechanism does not address the cause of cauda equina syndrome, and anticholinergic effects could worsen bladder function. The registry also lacks indication and safety data.

**To proceed, the following is needed:**
- SAHPRA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Remapping of the second prediction to a current neurogenic bladder or neurogenic lower urinary tract dysfunction concept, then a literature and trial search
- Verification that the four registered products actually contain dicyclomine
- A literature and trial search specific to cauda equina syndrome, with clinical review of the urinary retention risk

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

