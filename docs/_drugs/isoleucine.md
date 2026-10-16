---
layout: default
title: Isoleucine
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Isoleucine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the SAHPRA registration data"
---

# Isoleucine
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

# Isoleucine: From Parenteral Nutrition Component to Gastroparesis

## One-Sentence Summary

Isoleucine is an essential branched-chain amino acid. In South Africa it is registered only as a component of parenteral nutrition and peritoneal dialysis products. The TxGNN model predicts it may be useful for **gastroparesis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the SAHPRA registration data (all registrations are for amino acid-containing infusion products) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isoleucine is an essential amino acid that is mainly given as a nutritional component within multi-ingredient infusion products. No original indication or mechanism is recorded for it, so no verifiable mechanistic pathway to gastroparesis can be established from the data compiled for this report.

Two indirect links can be proposed, but both are speculative and unsupported by the data:
- Nutritional support may help with the malnutrition that often accompanies gastroparesis.
- Amino acids may influence gastric emptying and gut hormone signalling (for example CCK and GLP-1).

The score of 0.993 is a knowledge-graph model output, not clinical evidence, and should not be treated as validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## South Africa Market Information

All 10 registrations are valid single-ingredient-category licences. The data compiled for this report does not include approved indication text or Essential Medicines List (EML) status. The five main registrations are listed below.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/34/0243 | Nutrineal PD4 with 1.1% amino acids 2.5L | Infusion | Not stated |
| Reg. No. 37/25.2/0503 | Oliclinomel N6 900E 2000ml | Infusion | Not stated |
| Reg. No. 41/25/0757 | Nutriflex Lipid Peri | Infusion | Not stated |
| Reg. No. 52/25/0739 | Numeta G13E | Infusion | Not stated |
| Reg. No. 46/32.2/0518 | Smofkabiven | Infusion | Not stated |

Five further registrations exist: Numeta G16E, Smofkabiven Peripheral, Nutriflex Omega Specialized, Nutriflex Lipid Special 625ml, and Adco-ipratropium (ni201), the last of which is listed as a vial. Its link to isoleucine is unclear and should be verified against the SAHPRA record.

## Safety Considerations

No label-based warnings, contraindications or drug interaction data were available. The drug interaction query returned no results.

**Contraindication associations from the knowledge graph (not label text):** The TxGNN knowledge graph (PrimeKG) links isoleucine to contraindication with the following conditions. These are model-derived associations and need verification against the approved Professional Information.
- **Renal:** kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
- **Cardiovascular:** heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
- **Metabolic and calcium:** phenylketonuria, disorder of phenylalanine metabolism, phosphorus metabolism disease, hypercalcemia disease, humoral hypercalcemia of malignancy, sarcoidosis

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). There are no clinical trials, no literature, no recorded mechanism and no label-based safety data. The knowledge graph also flags several renal and cardiac contraindication associations, which warrant caution in a population that may have comorbidities.

**To proceed, the following is needed:**
- The SAHPRA Professional Information (warnings, contraindications, approved indications) for the registered products
- Mechanism of action data, for example from DrugBank
- A literature search for amino acid or isoleucine effects on gastric emptying and nutritional outcomes in gastroparesis
- Assessment of route compatibility, since current registrations are infusion-based and the route needed for gastroparesis is undetermined
- If preclinical or mechanistic support emerges, a safety review for patients with renal or cardiac disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

