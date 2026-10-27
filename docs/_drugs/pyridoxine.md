---
layout: default
title: Pyridoxine
parent: Model Prediction Only (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pyridoxine: predicted new indication Gonococcal urethritis (evidence level L5). Approved use: Pyridoxine deficiency anaemia"
monitor_inn: "Pyridoxine"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "urinary tract infection (disease)", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "congenital prothrombin deficiency", "toxocariasis", "toxascariasis", "anisakiasis", "vitamin deficiency disorder"]
---

# Pyridoxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Pyridoxine: From Pyridoxine Deficiency Anaemia to Gonococcal Urethritis
{: .text-alpha }

## One-Sentence Summary

Pyridoxine (vitamin B6) is originally used to treat pyridoxine deficiency anaemia.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, but **0 clinical trials** and **0 publications** currently support this prediction.
It is a computational signal only and has no supporting evidence or plausible biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pyridoxine deficiency anaemia |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 93.87% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on known pharmacology, pyridoxine is the precursor of pyridoxal 5'-phosphate (PLP), a cofactor in amino acid metabolism. Its efficacy in correcting vitamin B6 deficiency is established.

**This prediction is not mechanistically supported.** Pyridoxine has no known antibacterial activity against *Neisseria gonorrhoeae*. The high TxGNN score appears to be a network-based artefact, probably driven by graph proximity to other urethritis-related nodes. No trials or publications back it.

The same applies to the other high-scoring predictions for this drug, such as Ureaplasma urethritis, xanthogranulomatous pyelonephritis, toxocariasis and congenital prothrombin deficiency. Their evidence is likewise absent or unrelated.

The best-supported prediction in the compiled data is **vitamin deficiency disorder**. It is rated L2, with one completed Phase 2/3 study (NCT01128244, n=13) and reviews on B6 deficiency. However, it is essentially a restatement of the original indication, not true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for gonococcal urethritis.

## Literature Evidence

Currently no related literature available for gonococcal urethritis.

## South Africa Market Information

Pyridoxine is registered in South Africa in 13 valid single-ingredient registrations, with no cancelled registrations. The table shows five of them.

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| H2611 (ACT 101/1965) | Becoplex ido vial 10ml | Injection |
| T1012 (ACT 101/1965) | Beespan | Capsule |
| H2412 (ACT 101/1965) | A-lennon vitamin b co ampoule 2ml | Injection |
| A/21.8.1/743 | Menoflush | Tablet |
| 36/22.1/0508 | Cernevit | Infusion |

The remaining registrations are capsules, injections, infusions and TPN products, including multivitamin products.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** These come from drug-disease contraindication links in the TxGNN knowledge graph. They are not taken from SAHPRA-approved labelling and should be verified against the Professional Information (PI). They include liver failure and liver disease, kidney disease and impaired renal function, peptic ulcer disease, diabetes mellitus and diabetic ketoacidosis, gout, systemic lupus erythematosus, peripheral neuropathy and peripheral nervous system disease, Wilson disease, hereditary haemochromatosis, rhabdomyolysis, and substance abuse/dependence.
- **Drug interactions (13 recorded):**
  - Moderate: altretamine, phenobarbital, levodopa (when given without a decarboxylase inhibitor) and phenytoin.
  - Minor: amobarbital, butabarbital, butalbital, methohexital, pentobarbital, secobarbital, thiopental, methylphenobarbital and primidone.
- **High-dose caution:** The vitamin neurotoxicity literature documents sensory neuropathy with chronic high-dose pyridoxine.

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score of 93.87%. It has no clinical trials, no literature and no plausible antibacterial mechanism. Standard antimicrobial therapy is the appropriate treatment for gonococcal urethritis, and there is no basis for repurposing pyridoxine for it.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence of activity against *N. gonorrhoeae*, which is currently absent.
- Mechanism of action data, together with the SAHPRA PI warnings and contraindications.
- A shift in evaluation focus to better-supported directions, such as vitamin B6 deficiency states and B6-dependent conditions (including hyperoxaluria), assessed as separate indications. Any such use needs dose and duration guardrails for neuropathy risk and interaction checks, notably with levodopa, phenytoin and phenobarbital.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

