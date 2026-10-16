---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "conjunctivitis (disease)", "exposure keratitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "otitis externa", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome"]
---

# Trimethoprim
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

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial originally used for urinary tract infection, ear and eye infections, pneumocystosis and shigellosis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** were retrieved for this prediction, so the evidence rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (SAHPRA indication text not available; taken from the knowledge-graph indication list) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trimethoprim is an antibacterial whose efficacy in bacterial infections is established, and it has been used in ophthalmic combinations (with polymyxin B) for bacterial conjunctivitis and blepharoconjunctivitis. These are already listed among its original indications.

The prediction is therefore a graph-based extension to a closely related ocular surface disease. The main limitation is that punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or non-infectious, and an antibacterial would be unlikely to help in those cases. The prediction is plausible only for a bacterial subset, and this has not been tested.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

Currently no related literature available for punctate epithelial keratoconjunctivitis.

For context, the second-ranked prediction, conjunctivitis, already falls within the original indications. It has supporting literature, including a multicentre comparison of polymyxin B/trimethoprim with moxifloxacin ([19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/), 2008), a paediatric survey ([8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/), 1995) and a clinical evaluation of trimethoprim-containing ophthalmic solutions ([6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/), 1984). It is not a true repurposing candidate. The other eight predicted indications are weakly supported or unsupported. Several are indirect (exposure keratitis, infective urethral stricture, otitis externa), and for post-bacterial disorder the trials tested trimethoprim-sulfamethoxazole rather than trimethoprim alone.

## South Africa Market Information

All nine registrations are valid single-ingredient products. Approved indication text was not available in the data compiled for this report. Essential Medicines List (EML) status could not be confirmed from the data provided.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 27/20.2/0335 | Dynazole | Suspension | Not available |
| Z/20.2/209 | Trixazole | Tablet | Not available |
| K/20.2.1/335 | Spectrim | Capsule | Not available |
| W/20.2/376 | Novatrim | Suspension | Not available |
| R/20.1.1/47 | Rocephin | Injection | Not available |

The remaining four registrations are Purbac injection 5ml (L/20.2/336), Xerazole Suspension (28/20.2/0389), Co-Trimoxazole 960 Biotech (W/20.2.1/88) and Cotrizid (52/20.2/0208). No ophthalmic formulation appears among the registrations listed, which matters for the predicted ocular indication.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** inherited porphyria and other porphyrias, kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, *Clostridium difficile* colitis, G6PD deficiency, folic acid deficiency anaemia, and several others (glycogen storage disease, cystinuria, galactosaemia, perinatal necrotizing enterocolitis, pyoureter).

**Drug Interactions:** 100 interactions were identified. Major-level interactions are with potassium salts (potassium chloride, potassium citrate, potassium bicarbonate, potassium gluconate), reflecting a risk of raised potassium. Moderate-level interactions include metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid and sapropterin.

Please refer to the SAHPRA-approved Professional Information (PI) for full warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials or publications for punctate epithelial keratoconjunctivitis (Evidence Level L5). Many cases are viral or non-infectious, and no ophthalmic trimethoprim product was identified among the South African registrations.

**To proceed, the following is needed:**
- Clinical or literature evidence of trimethoprim (or polymyxin B/trimethoprim) in punctate epithelial keratoconjunctivitis, ideally stratified by bacterial versus viral cause
- Confirmation of whether an ophthalmic formulation is registered or obtainable in South Africa
- SAHPRA Professional Information warnings and contraindications
- Mechanism of action data to support the mechanistic link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

