---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Atazanavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "congenital human immunodeficiency virus", "AIDS related complex"]
---

# Atazanavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Atazanavir: From HIV Infection and AIDS to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV protease inhibitor, originally used to treat HIV infectious disease and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome** (a veterinary condition), but there are **no clinical trials** and **no publications** directly supporting this prediction. This is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (from the knowledge graph, as the registration records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, atazanavir is an HIV-1 protease inhibitor. Its efficacy in HIV infection and AIDS is established, and mechanistically it may be applicable to related lentiviral infections.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, so a high score is plausible through shared biology. However, FIV protease differs structurally from HIV-1 protease, and atazanavir's activity against it has not been established.

This is a veterinary indication, not a human clinical one. The high score should be treated as a hypothesis from the knowledge graph only.

**Other predictions reviewed (lower priority):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Simian immunodeficiency virus infection | 99.98% | L4 | Animal model only (one macaque HAART study, PMID 20497048); does not isolate atazanavir's effect; not a human indication |
| Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.98% | L5 | No mechanistic link identified; likely a network-proximity artefact |
| Obsolete familial combined hyperlipidaemia | 99.82% | L5 | Protease inhibitors are associated with dyslipidaemia rather than treating it; likely spurious |
| Congenital HIV | 99.71% | L3 | Observational data only, mostly safety of in utero exposure; neonatal efficacy not demonstrated |
| AIDS related complex | 99.71% | L3 | Essentially an older term for an existing indication, so not true repurposing |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (feline acquired immunodeficiency syndrome).

For reference, the closest supporting publications for the other predictions are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Cohort | Antiviral Therapy | Atazanavir exposure in pregnancy was effective regardless of tenofovir use (relevant to congenital HIV prevention) |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort | JAMA Pediatrics | Congenital anomalies and in utero antiretroviral exposure in HIV-exposed uninfected infants |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohort | Frontiers in Immunology | PHACS SMARTT study: safety of in utero antiretroviral exposure |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/non-case study | Eur J Clin Pharmacol | Antiretroviral exposure in pregnancy and congenital anomaly risk in Europe |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohort | J Acquir Immune Defic Syndr | Commonly prescribed ART regimens and incidence of AIDS-defining neurological conditions |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Risk factors for gastrointestinal adverse events in HIV-treated and untreated patients |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study | J Infect Dis | SIV-infected macaques on HAART had reduced CNS viral replication and inflammation, but viral DNA persisted |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In vitro / rat | Reprod Toxicol | Atazanavir and ritonavir interact with placental efflux transporters (ABCB1, ABCG2, ABCC2) |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 45/20.2.8/0925 | Zatonav | Film-coated tablet (Fct) | Not available in the data compiled |
| 50/20.2.8/0242 | Emcovir | Tablet | Not available in the data compiled |

Both registrations are valid single-ingredient products. Essential Medicines List (EML) inclusion status could not be confirmed from the data compiled for this report.

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease contraindication links, not label text; verify against the SAHPRA-approved Professional Information):
- Hepatic: liver failure, liver disease, gallbladder disease, chronic hepatitis B and C virus infection
- Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, lactic acidosis
- Bilirubin-related: hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome
- Renal: nephrolithiasis, acute urate nephropathy
- Cardiac conduction: atrioventricular block
- Haematological: haemophilia

**Drug interactions** (100 interactions recorded; examples below):
- **Major:** famotidine, ranitidine, rabeprazole, omeprazole (acid-suppressing agents, which reduce atazanavir absorption), loperamide, triamcinolone, budesonide
- **Moderate:** acarbose, metformin, pioglitazone, alogliptin, albiglutide, hydrocortisone, betamethasone, aprepitant, alosetron, aluminium hydroxide, calcium carbonate

Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions are a veterinary disease (feline AIDS) and an animal model infection (SIV), both with no human trials and no atazanavir-specific evidence. The more clinically relevant predictions (congenital HIV, AIDS related complex) largely overlap with the existing HIV indication or rest on observational safety data only.

**To proceed, the following is needed:**
- Mechanism of action data for atazanavir (currently unavailable)
- SAHPRA package insert warnings and contraindications, and approved indication text for both registrations
- For congenital HIV: paediatric and neonatal efficacy and dosing evidence, and registered trials
- For veterinary or animal-model indications: in vitro evidence of atazanavir activity against FIV or SIV protease, and confirmation that a human-health pathway exists
- Confirmation of EML status in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

