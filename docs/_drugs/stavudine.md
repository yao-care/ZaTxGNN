---
layout: default
title: Stavudine
parent: Model Prediction Only (L5)
nav_order: 428
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Stavudine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "STAVUDINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Stavudine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Stavudine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Stavudine is a nucleoside reverse transcriptase inhibitor (NRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** directly support this prediction.
The prediction is a computational signal only, and the condition is a veterinary disease rather than a human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (taken from the TxGNN knowledge graph, as the SAHPRA registration entries contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Based on known pharmacology, stavudine is a thymidine analogue NRTI. After phosphorylation inside cells to stavudine triphosphate, it terminates viral DNA chain elongation. Its efficacy in HIV-1 is established.

Feline immunodeficiency virus (FIV) is a lentivirus, and its reverse transcriptase is related to that of HIV. A mechanistic rationale therefore exists. However, the high score reflects a network-based prediction only, and no direct evidence was found for this condition.

Stavudine is also being phased out of human use because of mitochondrial toxicity (lipodystrophy, peripheral neuropathy, pancreatitis, lactic acidosis). This limits its appeal for veterinary repurposing. Feline AIDS is also not a human clinical indication, so the relevance to South African human healthcare is limited.

*Other predictions in the data (lower priority):*
- **Simian immunodeficiency virus (SIV) infection** (score 99.55%, evidence level L4): only preclinical or in vitro studies are available (see below).
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.51%, evidence level L5): no clear mechanistic link was identified. Stavudine's known neurotoxicity argues against use in a neurological condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

There is no literature for the top-ranked prediction (feline AIDS). The table below lists the publications compiled for the second-ranked prediction, SIV infection, as indirect supporting evidence. All are non-human or in vitro studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22013040](https://pubmed.ncbi.nlm.nih.gov/22013040/) | 2012 | Animal study (macaque) | J Virol | Fatal pancreatitis in SIVmac251-infected macaques treated with didanosine and stavudine after CTLA-4 and IDO blockade. This is a safety signal. |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility study | Antivir Ther | Antiviral activity of 16 approved drugs was evaluated against HIV-2, SIV and SHIV strains, to guide treatment and post-exposure prophylaxis. |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | In vitro study (related retrovirus) | J Virol | Susceptibility of human foamy virus to dideoxynucleosides. Only zidovudine was as effective as against HIV-1. |
| [9021177](https://pubmed.ncbi.nlm.nih.gov/9021177/) | 1997 | In vitro study (different compound) | Antimicrob Agents Chemother | Concerns the macrolide SRR-SB3, not stavudine. Limited relevance. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| A40/20.2.8/0659 | Sonke-Laminevstav 30 | Tablet | Indication text not available in the registration data |
| 44/20.2.8/0212 | Tri-Nestlam 150/30/200 | Tablet | Indication text not available in the registration data |

Both registrations are currently valid, and both are oral tablets. The data compiled for this report do not state Essential Medicines List (EML) status.

## Safety Considerations

**Knowledge-graph contraindications.** These come from drug-disease contraindication links in the TxGNN knowledge graph, not from label text. They include:
- Liver and metabolic: liver disease, fatty liver disease, non-alcoholic steatohepatitis, lactic acidosis
- Pancreas, gallbladder and kidney: pancreatitis, gallbladder disease, kidney disease, pyoureter
- Glucose and weight: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, obesity disorder, monogenic obesity
- Nervous system and other: peripheral nervous system disease, peripheral neuropathy, substance abuse/dependence

**Drug interactions.** A screen returned 100 interacting drugs in total. Those with a Moderate level are:
- Metronidazole
- Naltrexone
- Orlistat
- Rosuvastatin
- Simvastatin
- Tinidazole

Other listed interactions have an unknown severity level, including metformin, omeprazole, pantoprazole, lansoprazole, prednisone, morphine, vancomycin, doxycycline and sulfasalazine.

**Animal safety signal.** Fatal pancreatitis was reported in SIV-infected macaques given a dideoxynucleoside regimen that included stavudine.

Warnings and contraindications from the SAHPRA-approved Professional Information (PI) were not available for this report. Please refer to the PI for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5). No clinical trials or publications support feline AIDS. The related SIV literature is preclinical and includes a pancreatitis safety signal. Stavudine's mitochondrial toxicity profile and its phase-out from human use further weaken the case. Feline AIDS is a veterinary condition, so it falls outside human drug repurposing.

**To proceed, the following is needed:**
- Mechanism of action data for stavudine
- The SAHPRA Professional Information (PI) warnings and contraindications, which are currently missing and block safety screening
- Direct evidence for the predicted indication, such as veterinary studies of FIV antiviral activity
- A decision on whether a veterinary indication is within the scope of this programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

