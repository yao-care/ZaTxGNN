---
layout: default
title: Atazanavir
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 4
monitor_inn: "ATAZANAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-29
description: "Atazanavir: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infection and AIDS"
---

# Atazanavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Atazanavir: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Atazanavir is an HIV-1 protease inhibitor, recorded in the knowledge graph for HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and only **1 publication** (a 2010 macaque study of combination antiretroviral therapy). This is an animal-model finding, not a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection and AIDS (relation recorded in the knowledge graph; SAHPRA licence indication text is not available) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| South Africa Market Status | Marketed (valid licences: 2 of 2) |
| Number of SAHPRA Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atazanavir is an HIV-1 protease inhibitor. Detailed mechanism of action data is not available in the data compiled for this report, but the drug class is well known. Protease inhibitors block cleavage of viral polyproteins, which prevents the production of mature, infectious virus particles.

SIV is a lentivirus closely related to HIV and has a homologous protease, so antiretroviral activity is biologically plausible. SIV infection in macaques is a standard animal model of HIV. The prediction therefore largely reflects the drug's existing HIV use rather than a genuinely new human indication.

The only cited study (PMID 20497048) tested combination antiretroviral therapy (HAART) in SIV-infected macaques. Atazanavir was likely one component, and its independent contribution cannot be separated. The study does not directly establish atazanavir's effect on SIV, so the evidence level is capped at L5 under the rules (a study that directly tests the drug against the predicted disease is required for L4 or above).

Other predictions in the list are weaker:
- **Feline acquired immunodeficiency syndrome** (score 0.9998): a veterinary indication with no trials or literature. HIV and FIV proteases differ in substrate specificity and respond differently to HIV protease inhibitors.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9998): no mechanistic link and no evidence. Likely a TxGNN model (deep learning) artifact.
- **Obsolete familial combined hyperlipidemia** (score 0.9982): the ontology term is obsolete, and atazanavir is not known to treat hyperlipidemia. It should be treated as a computational artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study (non-human primate) | The Journal of Infectious Diseases | In SIV-infected macaques given HAART, central nervous system viral replication and inflammation were reduced, but viral DNA persisted. The drug's individual contribution is not separable. |

---

## South Africa Market Information

Both registrations are single-ingredient products. Essential Medicines List status is not available in the data compiled for this report. Approved indication text is not available for either registration.

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 45/20.2.8/0925 | Zatonav | Film-coated tablet (Fct) | Not available in the compiled data |
| 50/20.2.8/0242 | Emcovir | Tablet | Not available in the compiled data |

---

## Safety Considerations

SAHPRA package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

**Contraindication-related relations recorded in the knowledge graph** (not label text, and to be verified against the PI): liver failure, liver disease, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C virus infection, haemophilia, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), nephrolithiasis, acute urate nephropathy, atrioventricular block and lactic acidosis.

**Drug interactions** (100 interactions found; examples below, from the DDInter database):

| Level | Interacting Drugs |
|------|------|
| Major | Famotidine, ranitidine, rabeprazole, omeprazole (acid-suppressing agents), loperamide, triamcinolone, budesonide |
| Moderate | Acarbose, metformin, pioglitazone, alogliptin, albiglutide, acetohexamide, hydrocortisone, betamethasone, alosetron, aprepitant, aluminium hydroxide, calcium carbonate |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a single macaque study of combination therapy, with no clinical trials. SIV infection is an animal model of HIV, not a human indication, so the finding mostly restates atazanavir's existing HIV use. It is not true repurposing, and the evidence level is L5.

**To proceed, the following is needed:**
- Review of the SAHPRA Professional Information for atazanavir (approved indications, warnings and contraindications), which is currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Evidence that tests atazanavir alone against the predicted disease, if any is pursued
- Human-relevant candidate indications beyond HIV, as the other predictions (feline AIDS, rare neurodevelopmental disorder, obsolete hyperlipidaemia term) have no supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

