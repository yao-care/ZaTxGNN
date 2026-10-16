---
layout: default
title: Linezolid
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Linezolid: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Streptococcal and staphylococcal infections…"
---

# Linezolid
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

# Linezolid: From Staphylococcal and Streptococcal Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Linezolid is an oxazolidinone antibacterial, originally used to treat staphylococcal and streptococcal infections, including staphylococcal and streptococcal pneumonia.
The TxGNN model's top-ranked prediction is **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support it, so it rests on the model prediction alone.
The best-supported alternative direction is **pyelonephritis** (limited to Gram-positive pathogens such as VRE and MRSA), with **no registered trials** and **14 publications**, mostly case reports and reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Streptococcal and staphylococcal infections, including streptococcal and staphylococcal pneumonia (the SAHPRA licence records provided contain no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 92.45% |
| Evidence Level | L5 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Linezolid is known to be an oxazolidinone antibacterial that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Its efficacy in Gram-positive infections is established, including resistant organisms such as MRSA and VRE.

For the top-ranked prediction, **polyclonal hyperviscosity syndrome**, no mechanistic link could be identified. The high score is a graph-based prediction only. A bacterial protein synthesis inhibitor has no recognised role in a condition of raised blood viscosity.

Other top predictions (hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, and haematological disease with peripheral neuropathy) also lack a plausible mechanism. In several cases, linezolid's known adverse effects (myelosuppression, peripheral and optic neuropathy, pancreatitis, lactic acidosis) argue against benefit.

The only prediction with a plausible rationale is **pyelonephritis** (rank 10, score 82.67%). Linezolid is active against resistant Gram-positive uropathogens such as VRE and MRSA. It lacks activity against common Gram-negative uropathogens such as *E. coli*, so it would be a niche option, not a general one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome, and none were found for pyelonephritis either.

---

## Literature Evidence

For the top-ranked prediction (polyclonal hyperviscosity syndrome), currently no related literature available.

For the most plausible prediction, **pyelonephritis**, the most relevant items retrieved were:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14520141](https://pubmed.ncbi.nlm.nih.gov/14520141/) | 2003 | RCT (mixed resistant Gram-positive infections; not pyelonephritis-specific) | Pediatr Infect Dis J | Linezolid versus vancomycin in neonates with known or suspected resistant Gram-positive infections |
| [21308555](https://pubmed.ncbi.nlm.nih.gov/21308555/) | 2010 | Review | Curr Infect Dis Rep | Management of resistant enterococcal urinary tract infections, including MDR and vancomycin-resistant strains |
| [38161637](https://pubmed.ncbi.nlm.nih.gov/38161637/) | 2024 | Case report | Clin Case Rep | VRE urinary tract infection with bacteraemia after continent urinary diversion |
| [34556047](https://pubmed.ncbi.nlm.nih.gov/34556047/) | 2021 | Case report | BMC Infect Dis | *Enterococcus hirae* bacteraemia with acute pyelonephritis in a patient with alcoholic cirrhosis |
| [19918525](https://pubmed.ncbi.nlm.nih.gov/19918525/) | 2009 | Case report | Cases J | Xanthogranulomatous pyelonephritis due to community-associated MRSA |
| [18349306](https://pubmed.ncbi.nlm.nih.gov/18349306/) | 2008 | Case report | Ann Pharmacother | VRE *E. faecium* pyelonephritis treated with daptomycin during pregnancy |

Note: Several retrieved items concern other agents (omadacycline, eravacycline, RBx 11760) or general infection topics, and are not direct evidence for linezolid in pyelonephritis. Only abstract fragments were available, so study designs should be verified against the full texts.

For other lower-ranked predictions, the literature consists of case reports only. These describe linezolid treating bacterial infections in patients who happen to have a haematological condition (e.g. macroglobulinaemia, myeloma, Job's syndrome). They do not show treatment of the haematological disorder itself.

---

## South Africa Market Information

| Registration Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Reg. No. 35/20.1.1/0312 | Zyvoxid 200Mg/100Ml | Injection | Not available in the data compiled |
| Reg. No. 48/20.1.1/0223 | Linezolid specpharm | Tablet | Not available in the data compiled |
| Reg. No. 50/20.1.1/0184 | Zenilid Iv 600 Mg/300 Ml | Infusion | Not available in the data compiled |

All three registrations are valid single-ingredient products (none cancelled). Both oral (tablet) and injectable (injection, infusion) forms are available. Essential Medicines List (EML) status is not available in the data compiled.

---

## Safety Considerations

**Contraindications / conditions flagged in the knowledge graph** (these come from graph relationships, not from the label text):
- Haematological: thrombocytopenia, anaemia (including macrocytic), leukopenia, pancytopenia
- Neurological and ocular: peripheral neuropathy, peripheral nervous system disease, optic nerve disease, vision disorder, blindness, epilepsy
- Metabolic and endocrine: lactic acidosis, thyrotoxicosis, hyperthyroidism, Graves disease
- Serotonergic and catecholamine-related: serotonin syndrome, carcinoid syndrome, phaeochromocytoma, sympathetic paraganglioma, hypertension and hypertensive disorder
- Gastrointestinal: *Clostridium difficile* colitis, perinatal necrotising enterocolitis
- Cancers also listed: duodenal, small intestine, heart and adrenal gland cancers

**Drug Interactions:** 100 interactions were identified. The main ones are:
- **Major:** isometheptene, epinephrine, bupropion, morphine, lorcaserin, diethylpropion, dolasetron, palonosetron, phentermine. These largely reflect serotonergic or pressor risk, as linezolid is a monoamine oxidase inhibitor.
- **Moderate:** metronidazole, chlorpropamide, picosulfuric acid, glimepiride, and several insulins (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular). Hypoglycaemia is the relevant concern with antidiabetic agents.

Key warnings and contraindications from the SAHPRA package insert were not available. Please refer to the SAHPRA-approved Professional Information (PI) for full safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (polyclonal hyperviscosity syndrome) is supported only by a graph-based score, with no trials, no literature, and no plausible mechanism (Evidence Level L5). Linezolid's known toxicities (myelosuppression, neuropathy, lactic acidosis) also argue against use in the haematological conditions predicted. Pyelonephritis is a reasonable research question for resistant Gram-positive pathogens only, but evidence is limited to case reports, reviews, and one mixed-infection comparative trial (Level L4).

**To proceed, the following is needed:**
- The SAHPRA package insert (warnings, contraindications, approved indications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- For pyelonephritis: a focused review of linezolid use in VRE/MRSA urinary tract infection, plus a check of registries (ClinicalTrials.gov, SANCTR, PACTR) for relevant trials
- A safety plan covering myelosuppression, neuropathy, lactic acidosis, and serotonergic interactions
- Clarification of EML status and local resistance patterns in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

