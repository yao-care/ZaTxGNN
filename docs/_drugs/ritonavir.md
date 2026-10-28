---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 3
monitor_inn: "RITONAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS, and hepatitis C virus infection"
---

# Ritonavir
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

## Ritonavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor, with hepatitis C virus infection, HIV infectious disease and AIDS listed as its original uses.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS, and hepatitis C virus infection (relations recorded in the knowledge graph; no approved-indication text is available from the local licences) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 9 of 9) |
| Number of SAHPRA Registrations | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ritonavir is known as an HIV protease inhibitor, and HIV infection and AIDS are among its listed uses.

Feline immunodeficiency virus (FIV) is a lentivirus whose aspartyl protease is related to HIV-1 protease, so a mechanistic rationale exists. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so activity cannot be assumed. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is a prediction only.

Note that this is a veterinary disease. It is not a human treatment indication, so its value for human repurposing is limited.

Two other predictions were also generated:
- **Simian immunodeficiency virus (SIV) infection** (score 0.9992): this has preclinical support (see below), but it is an animal model, not a human indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9992): no mechanistic link could be established, and no trials or literature were found.

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome. No trials were found for the other two predicted indications either.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For context, the closely related SIV prediction (rank 2) has preclinical publications, none of which study the feline disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by ritonavir (EC50 about 13 nM), comparable to HIV-1 (about 25 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Antiviral activity of approved anti-HIV-1 drugs tested against HIV-2, SIV and SHIV strains |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | J Virol Methods | Oral HAART including lopinavir/ritonavir in two SHIV-infected macaques; effect on the CD8 subset |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study | PLoS Pathog | Intensified multidrug ART gave long-term viral suppression in SIV-infected macaques; ritonavir's role not confirmed |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Rapid viral decay in SIV-infected macaques on quadruple ART; ritonavir's role not confirmed |

## South Africa Market Information

All 9 registrations are valid single-ingredient licences. No approved-indication text is available in the data compiled for this report. Essential Medicines List status is not stated in the data.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 51/20.2.8/0687.686 | Hetrovir 100 | Tablet | Not available |
| 51/20.2.8/0154 | Norvir Oral Powder | Sachet | Not available |
| 56/20.2.8/0838 | Ronivid 400/50 Mg | Film-coated tablet | Not available |
| 45/20.2.8/0925 | Zatonav | Film-coated tablet | Not available |
| 43/20.2.8/0356 | Aluvia 100/25 | Tablet | Not available |

Four further registrations (Emcovir, Paxlovid, Quadrimune, Lopimune 40/10 Oral Pellets) are also valid.

## Safety Considerations

**Contraindications recorded in the knowledge graph (not label text):** long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy, coronary artery disease, myocardial ischemia, pancreatitis, liver disease, cirrhosis, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridaemia, hyperbilirubinaemia, Gilbert syndrome, chronic hepatitis B, gout, potassium deficiency, haemophilia and others.

**Drug Interactions:** 100 interactions were identified. Examples of those graded Major: loperamide, triamcinolone and budesonide. Moderate examples include metformin, acarbose, dexamethasone, hydrocortisone, clarithromycin, metronidazole, bupropion and aprepitant. Ritonavir is a strong CYP3A4 inhibitor, which drives many of these.

Please refer to the SAHPRA-approved Professional Information (PI) for label warnings and contraindications. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for feline acquired immunodeficiency syndrome rests on model score alone, with no trials or literature, so the evidence level is L5. It is also a veterinary disease, not a human indication.

**To proceed, the following is needed:**
- Studies of ritonavir against FIV protease (in vitro and in cats), if a veterinary direction is of interest
- Mechanism of action data
- Extraction of warnings and contraindications from the SAHPRA package insert
- If SIV is pursued, treat it as a preclinical HIV model rather than a repurposing target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

