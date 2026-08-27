---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

> Itraconazole is a triazole antifungal internationally indicated for systemic and invasive fungal infections such as aspergillosis, candidiasis, and histoplasmosis.
> The TxGNN model predicts it may be effective for **Pneumocystosis (Pneumocystis jirovecii infection)**,
> with **no dedicated clinical trials** and **20 publications** currently offering only indirect supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the available regulatory data; internationally itraconazole is indicated for systemic/invasive fungal infections (aspergillosis, candidiasis, histoplasmosis, blastomycosis) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (mechanism/indirect evidence only) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for itraconazole was not available in this evidence pack. Based on known pharmacology, itraconazole is a triazole antifungal that inhibits fungal CYP450 lanosterol 14α-demethylase, blocking ergosterol synthesis in the fungal cell membrane — its efficacy against classical fungi (Aspergillus, Candida, Histoplasma) is well established.

However, *Pneumocystis jirovecii* is an atypical fungus whose membrane relies primarily on host-derived cholesterol rather than self-synthesized ergosterol. A mechanistic study in the evidence pool (PMID 12606318) found that *Pneumocystis carinii*'s lanosterol 14α-demethylase differs from azole-susceptible organisms, consistent with the organism's known intrinsic resistance to azole antifungals. This means the standard triazole mechanism is unlikely to translate directly into anti-Pneumocystis activity.

Most of the supporting literature places itraconazole in the context of broad-spectrum antifungal **prophylaxis** for immunocompromised patients (HIV, transplant recipients), where it is co-administered or co-discussed alongside pneumocystosis prevention rather than used as direct treatment for *P. jirovecii*. The TxGNN score of 99.34% likely reflects a strong **co-occurrence pathway** in the knowledge graph (itraconazole – immunocompromised host – opportunistic infection) rather than a validated pharmacological mechanism against *P. jirovecii* specifically. This distinction is important: the prediction is biologically plausible as a research signal but does not currently indicate direct causal efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled Phase 3 trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients; did not specifically isolate pneumocystosis outcomes |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Reviews primary/secondary prophylaxis for opportunistic infections in HIV, including Pneumocystis, in the context of antifungal/antimicrobial strategies |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Summarizes therapy and prophylaxis for Pneumocystis carinii and other protozoan/opportunistic infections, including mode of action and dosing of available agents |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Discusses prophylaxis and treatment strategies for infections, including fungal, in bone marrow transplant recipients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Reviews infection risk and management, including fungal pneumonia, after lung transplantation |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian J Medical Microbiology | Compares respiratory fungal pathogen profiles and susceptibility between immunocompetent and immunocompromised hosts by CD4 count |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Single-center experience of invasive fungal infections after kidney transplantation |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanistic study | Am J Respir Cell Mol Biol | Characterizes lanosterol 14α-demethylase from *Pneumocystis carinii*; notes intrinsic resistance of Pneumocystis to azole antifungals — directly relevant to mechanistic plausibility |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | Reports unusual *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with STAT1 mutation |
| [7877856](https://pubmed.ncbi.nlm.nih.gov/7877856/) | 1994 | Case report/Review | Pathologie-Biologie | Reviews aspergillosis in AIDS patients, noting prior pneumocystosis as a predisposing clinical context |

---

## South Africa Market Information

Itraconazole currently has **no SAHPRA product registrations** and is classified as **not marketed** in South Africa (0 licenses on record). No product name, dosage form, or approved indication text is available from the regulatory data source.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence linking itraconazole to pneumocystosis is indirect — it consists of co-occurrence in prophylaxis literature rather than direct treatment/prevention trials, and a mechanistic study suggests *P. jirovecii* is intrinsically less susceptible to azole action than classical fungi. Combined with the absence of dedicated clinical trials, unknown MOA/safety data, and the drug's unregistered status in South Africa, the evidence does not yet support progression beyond a research hold.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data from DrugBank/PI to validate or refute applicability to *P. jirovecii*
- SAHPRA Professional Information (warnings, contraindications, DDI) once/if a registration application is filed
- Direct clinical or preclinical evidence testing itraconazole specifically against *Pneumocystis jirovecii* (treatment or prophylaxis), compared with standard-of-care (e.g., TMP-SMX)
- Clarification of South Africa market entry pathway, given the current "not marketed" / 0-registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

