---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 280
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis…"
monitor_inn: "ITRACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal, originally used for systemic fungal infections such as candidiasis, histoplasmosis, aspergillosis and blastomycosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are **no registered clinical trials** and the **20 publications** retrieved are mostly reviews, case reports and general infection studies, none of which directly demonstrate efficacy against Pneumocystis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis, blastomycosis and other fungal infections (from the knowledge graph; the SAHPRA registration lists no indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (see the note on the evidence level in the Conclusion) |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Itraconazole inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. Detailed mechanism of action data is not available in the data compiled for this report, so this description reflects the generally known class mechanism.

The prediction is **mechanistically weak**. *Pneumocystis jirovecii* is classified as a fungus, but its cell membrane contains mainly cholesterol rather than ergosterol, so the azole target is only weakly relevant. Azoles are not established as effective anti-Pneumocystis agents. Standard prophylaxis and treatment rely on other agents, such as trimethoprim-sulfamethoxazole, as the retrieved reviews also mention.

The high TxGNN score most likely reflects itraconazole's broad antifungal profile and its frequent co-occurrence with other opportunistic infections in immunocompromised patients (for example, histoplasmosis in AIDS). It does not reflect a validated mechanism against Pneumocystis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below tests itraconazole against pneumocystosis. They are mostly reviews on infections in immunocompromised hosts, or reports of other fungal infections.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Randomised, double-blind, placebo-controlled phase III trial | HIV Medicine | Itraconazole capsules for prevention of deep fungal infections in HIV-infected patients; focus is fungal infections in general, not specifically Pneumocystis |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against Pneumocystis pneumonia |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including Pneumocystis |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Invasive fungal infections after kidney transplantation (single centre) |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series | Medicine | Disseminated histoplasmosis in AIDS: clinical findings, diagnosis and treatment |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and review | Frontiers in Immunology | *Talaromyces marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 37/20.2.2/0559 | Adco-sporozole | Capsule (oral) | Not available in the data compiled for this report |

## Safety Considerations

**Contraindications and conditions of concern (from the knowledge graph, not label text):** the drug-disease contraindication links include:
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, congestive heart failure, heart failure, cardiomyopathy (including hypertrophic), myocardial ischaemia, coronary artery disease, heart valve disease
- **Hepatic and renal:** liver disease, drug-induced liver injury, kidney disease, impaired renal function
- **Respiratory:** chronic obstructive pulmonary disease
- **Neurological and sensory:** peripheral neuropathy, vision disorder, hearing loss
- **Metabolic:** potassium deficiency, hypercalcaemia

**Drug interactions:** 100 interactions were identified, and the main ones in the retrieved list include:
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, alosetron
- **Minor:** metformin, pioglitazone, chlorpropamide, amphotericin B

Acid-suppressing agents (H2 blockers and proton pump inhibitors) are of particular relevance because they can reduce absorption of itraconazole capsules.

The SAHPRA-approved Professional Information (PI) warnings and contraindications were not available for this report and must be reviewed. Report adverse drug reactions to SAHPRA.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring alone. There are no registered clinical trials, the literature does not test itraconazole against *Pneumocystis*, and the biological rationale is weak because the organism lacks ergosterol as its main membrane sterol. Established, effective alternatives already exist. The evidence level is shown as L4 in the scoring data; the available evidence is closer to model prediction with only indirect literature, so it should be regarded as very low confidence.

**To proceed, the following is needed:**
- Laboratory or in vivo data on itraconazole activity against *Pneumocystis jirovecii*
- Mechanism of action data and a clear mechanistic link to the new indication
- The SAHPRA package insert (warnings, contraindications, approved indications) for safety screening
- A comparison with standard therapy (trimethoprim-sulfamethoxazole) to define any clinical niche, for example in patients who cannot tolerate it
- A review of cardiac, hepatic and interaction risks in the immunocompromised target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

