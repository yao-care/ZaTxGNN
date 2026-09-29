---
layout: default
title: Itraconazole
parent: Moderate Evidence (L3-L4)
nav_order: 278
evidence_level: L4
indication_count: 1
---

# Itraconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Itraconazole: From Antifungal Therapy to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal that blocks fungal ergosterol synthesis. The TxGNN model predicts it may be effective for **pneumocystosis**, but no clinical trials are registered for this use and no supplied publication shows itraconazole activity against *Pneumocystis*. The very high model score most likely reflects the drug's proximity to other fungal infections in the knowledge graph rather than a validated mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| South Africa Market Status | Marketed |
| Number of SAHPRA Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not recorded in the DrugBank entry supplied. The mechanism described in the evidence review is that itraconazole inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which blocks ergosterol synthesis. This is the standard action of azole antifungals.

That mechanism fits pneumocystosis poorly. *Pneumocystis jirovecii* has cholesterol-based membranes with little or no ergosterol, so the drug's target is largely absent. Azoles are not established therapy or prophylaxis for this infection. Standard care is trimethoprim-sulfamethoxazole (TMP-SMX), with pentamidine, atovaquone and dapsone as alternatives.

A 2003 study of the *Pneumocystis carinii* Erg11 enzyme supports this caution. It reports that the organism is intrinsically resistant to azole antifungals, even though it carries the target enzyme. Beyond that, the data contains no independent mechanistic support and nothing showing itraconazole activity against *Pneumocystis*.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 18 retrieved publications are all still unreviewed for relevance. Most are general infection reviews, opportunistic-infection cohorts or HIV case reports. The 10 most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled phase III trial of itraconazole capsules to prevent deep fungal infections in HIV patients. The abstract does not report *Pneumocystis* outcomes. |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism study | Am J Respir Cell Mol Biol | Cloned and characterised *Pneumocystis carinii* Erg11, the azole target. Reports the organism is intrinsically resistant to azoles. |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *P. carinii*. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Penetration of antifungal, antitubercular and other anti-infective agents into pulmonary epithelial lining fluid. |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clin Evid | Primary and secondary prophylaxis of opportunistic infections in HIV. |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infection after lung transplantation, including prevention and treatment. |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Prophylaxis and treatment of infection in bone marrow transplant recipients. |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian J Med Microbiol | Respiratory fungal pathogens in immunocompetent versus immunocompromised hosts, related to CD4+ counts. |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplant Proc | Single-centre experience of invasive fungal infections after kidney transplantation. |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Front Immunol | *Talaromyces marneffei* and *P. jirovecii* coinfection in a child with a STAT1 mutation. |

## South Africa Market Information

| Registration Number | Product Name | Dosage Form |
|---------|------|------|
| Reg. No. 37/20.2.2/0559 | Adco-sporozole | Capsule (oral) |

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

The drug-interaction query returned no records, so this should not be read as an absence of interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any registered trial or by a plausible mechanism. *Pneumocystis* lacks the ergosterol target and is described as intrinsically azole-resistant, and effective standard alternatives already exist.

**To proceed, the following is needed:**
- The SAHPRA package insert, to obtain warnings, contraindications and the approved indication (blocking for safety screening)
- Mechanism-of-action data from DrugBank
- Direct evidence of itraconazole activity against *Pneumocystis*, such as in vitro susceptibility or animal-model data
- A relevance review of the retrieved publications, which are all still unreviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

