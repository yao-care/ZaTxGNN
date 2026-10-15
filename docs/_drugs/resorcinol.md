---
layout: default
title: Resorcinol
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Resorcinol
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

# Resorcinol: From Acne and Dermatitis to Acne Keloid

## One-Sentence Summary

Resorcinol is a topical keratolytic agent, originally associated with acne, dermatitis and acneiform dermatitis.
The TxGNN model predicts it may be useful for **acne keloid** (acne keloidalis), but **no clinical trials and no publications** were found to support this prediction. It is a model-based hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, dermatitis, acneiform dermatitis (from the TxGNN knowledge graph; the South African registration lists no approved indication text) |
| Predicted New Indication | Acne keloid |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only; no trials or literature) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, resorcinol is a keratolytic agent already used in acne, and mechanistically it may be applicable to acne keloid.

Acne keloidalis is a chronic follicular inflammatory condition of the neck and scalp, so it shares general biological features with acne (follicular involvement and inflammation). Among the ten predictions generated, it is the closest to the original indications and therefore the most credible candidate. This overlap is indirect and plausible only. The high TxGNN score is a computational output and is not clinical evidence.

Other predictions (for example dermatomyositis, juvenile arthritis, ankylosing spondylitis, rheumatoid vasculitis and childhood interstitial lung disease) have no identifiable mechanistic link to a topical keratolytic. They are most likely artefacts of the model's graph propagation and are not recommended for further pursuit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| E512 | Anugesic | Suppository | Not stated in the data compiled for this report |

Only one registration (single-ingredient, valid) was identified. The registered product is a suppository, not a topical skin formulation. Its route is therefore not directly aligned with the topical use expected for dermatological indications. Essential Medicines List (EML) inclusion status could not be determined from the data compiled for this report.

## Safety Considerations

The following are contraindication associations drawn from the knowledge graph. They are not taken from the product label and need verification against the Professional Information (PI):

- **Haematological and metabolic:** methemoglobinemia (including due to methemoglobin reductase deficiency), sulfhemoglobinemia, G6PD deficiency, diabetes mellitus, diabetic ketoacidosis, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency
- **Cardiovascular and respiratory:** sudden cardiac arrest, heart conduction disease, peripheral vascular disease, intermittent claudication, peripheral arterial disease, respiratory failure
- **Renal and neurological:** kidney disease, pyoureter, epilepsy
- **Skin and infection-related:** folliculitis, seborrheic dermatitis, dermatitis, exanthem, common wart, anogenital human papillomavirus infection

Of particular concern is percutaneous absorption leading to methemoglobinemia, especially in neonates and children, in people with G6PD deficiency, and on broken or extensive skin areas.

No drug interaction data were found.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne keloid prediction rests only on a model score and indirect biological similarity to acne. There are no registered trials, no publications, no mechanism data, and no label-based safety information. The only local product is a suppository, which does not match a topical dermatological use.

**To proceed, the following is needed:**
- Mechanism of action data for resorcinol
- The SAHPRA package insert (warnings, contraindications and approved indication) for the registered product
- A literature and trial search specific to resorcinol in acne keloidalis
- Confirmation of whether a topical resorcinol product is registered or available in South Africa
- A safety assessment covering percutaneous absorption and methemoglobinemia risk, especially in children and in G6PD deficiency
- Clinical evidence (at least a small controlled study) before any change in the decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

