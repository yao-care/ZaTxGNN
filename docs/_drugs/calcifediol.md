---
layout: default
title: Calcifediol
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 2
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis"]
last_modified_at: 2026-10-27
description: "Calcifediol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcifediol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Calcifediol: Vitamin D metabolite (25-hydroxyvitamin D3) → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcifediol (25-hydroxyvitamin D3) is the main circulating form of vitamin D and the direct precursor of calcitriol. The TxGNN model predicts it may be relevant to **obsolete vitamin D deficiency**, a term flagged as obsolete in the disease ontology. No clinical trials or publications were found for this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From known pharmacology, calcifediol is the direct circulating precursor of calcitriol, the active hormone, and is the main marker of vitamin D status. Repletion in vitamin D deficiency is therefore mechanistically plausible.

The disease term, however, is flagged as obsolete in the ontology. The very high score (0.9999) most likely reflects the term's closeness to the drug's existing associations, not independent clinical evidence. No trials or literature were supplied, so the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| H2466 | Complenatal Ff | Capsule | Not recorded |
| H2062 (ACT 101) | Filibon | Capsule | Not recorded |

Both registrations are currently valid single-ingredient records, and the available dosage form is oral capsule.

---

## Safety Considerations

**Drug Interactions** (57 interactions recorded; selected examples by severity):
- **Major**: Cholecalciferol, Calcitriol, Burosumab
- **Moderate**: Fosphenytoin, carbamazepine and barbiturates (amobarbital, butalbital, butabarbital), thiazide diuretics (hydrochlorothiazide, bendroflumethiazide, chlorothiazide, chlorthalidone), aluminium hydroxide, bile-acid sequestrants (cholestyramine, colesevelam, colestipol), digitoxin, topical calcipotriol and calcitriol

Combining calcifediol with other vitamin D products carries a risk of excess vitamin D effect and hypercalcaemia. Thiazides can also raise calcium levels.

Conditions in which calcifediol is flagged as potentially problematic, from drug-disease relation data rather than label text: hypercalcaemia, nephrocalcinosis, nephrolithiasis, sarcoidosis, hyperphosphataemia, hypervitaminosis, kidney disease. Please confirm against the SAHPRA-approved Professional Information (PI). Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no trials or publications. The disease term is also obsolete in the ontology, so the score probably reflects ontology proximity and not new clinical insight. The evidence level is L5.

**To proceed, the following is needed:**
- Mapping of the obsolete term to a current vitamin D deficiency concept, then a focused literature and trial search
- SAHPRA Professional Information (warnings, contraindications, approved indications) for the registered products
- Detailed mechanism of action data
- Review of the major interactions and the calcium and renal risk profile before considering any new-use plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

