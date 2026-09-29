---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From Amino Acid Nutritional Supplementation to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid. In South Africa it is registered as an ingredient in parenteral nutrition and peritoneal dialysis products, and no single approved indication is recorded for it.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Amino acid nutritional supplementation (inferred from product types; registration records give no indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tyrosine is a building block for proteins and the precursor of catecholamines (dopamine, noradrenaline and adrenaline) and thyroid hormones. Its established role is nutritional.

The relationship between the original use and the predicted indication is weak. Cauda equina syndrome is a compressive neurosurgical emergency, usually caused by a herniated disc, tumour or trauma. It is treated by urgent decompression, not by medicines. No plausible therapeutic mechanism for tyrosine is evident. The high score most likely reflects a knowledge-graph artifact, such as tyrosine's neurotransmitter-pathway links to nervous system terms, and not a real treatment signal.

Other top-ranked predictions show the same pattern. Trials and papers retrieved for hyperthyroidism, neovascular glaucoma and postural orthostatic tachycardia syndrome were mostly keyword matches on "tyrosine kinase inhibitors", a different drug class. None tested L-tyrosine as an intervention. For hyperthyroidism, tyrosine is the substrate for thyroid hormone synthesis, so supplementation could theoretically worsen the condition. That needs a safety review before any further work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

Tyrosine appears as an ingredient in combination products, mainly parenteral nutrition and peritoneal dialysis solutions. The registration data lists 8 registrations and provides no approved indication text. Essential Medicines List (EML) inclusion status is not available. Five registrations are shown below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated in registration data |
| Reg. No. 33/10.2.1/0271 | Adco-ipratropium (ni201) | Vial | Not stated in registration data |
| Reg. No. 38/34/0172 | Extraneal 2L single bag | Infusion | Not stated in registration data |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated in registration data |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not stated in registration data |

The Adco-ipratropium entry does not look like a tyrosine-containing product and may be a mapping error. It should be verified against the SAHPRA record.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and there is no plausible mechanism linking tyrosine to cauda equina syndrome. The score is most likely a knowledge-graph artifact. No further resources are justified on this indication.

**To proceed, the following is needed:**
- Obtain the SAHPRA Professional Information for tyrosine-containing products (warnings and contraindications), which is currently missing.
- Retrieve mechanism of action data from DrugBank.
- Confirm the approved indication of each registered product, and verify the Adco-ipratropium mapping.
- Re-review other predicted indications with more relevant evidence. Hyperthyroidism needs a safety assessment, and postural orthostatic tachycardia syndrome needs a check of the direction of effect. Both require manual verification, because the retrieved trials are largely tyrosine kinase inhibitor keyword matches.
- Map "obsolete neurogenic bladder (disease)" to a current ontology term before any evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

