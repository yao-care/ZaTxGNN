---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Fluconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Fluconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Fluconazole is a triazole antifungal agent, established for treating systemic and mucosal fungal infections. The TxGNN model's top-ranked prediction (punctate epithelial keratoconjunctivitis, 99.2%) has **no supporting clinical trial or literature evidence** and is explicitly flagged in the evidence pack as mechanistically implausible, so this report instead focuses on the only candidate with substantive evidence: **Pneumocystosis (Pneumocystis jirovecii pneumonia)**, supported by **7 clinical trials** and **20 publications**, though the mechanistic rationale for efficacy remains contested.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic/mucosal fungal infections (antifungal, azole class) — Taiwan/SA-specific approved indication text not available (drug not registered locally) |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 97.82% |
| Evidence Level | L3 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this specific product is not available in the current dataset (data gap). Based on known pharmacology, fluconazole inhibits fungal 14α-demethylase (CYP51), blocking ergosterol synthesis in the fungal cell membrane — a mechanism effective against *Candida* and other classical yeasts.

*Pneumocystis jirovecii*, however, has an atypical cell membrane that largely lacks the conventional ergosterol pathway targeted by azoles, and it is intrinsically considered non-susceptible to fluconazole. Standard prophylaxis/treatment for pneumocystosis relies on trimethoprim-sulfamethoxazole, dapsone, atovaquone, or pentamidine — not azole antifungals.

The TxGNN high score most likely reflects a knowledge-graph clustering effect around "opportunistic/immunocompromised fungal infection" rather than a direct pharmacological rationale. The one directly relevant completed Phase 3 trial (NCT00000676) evaluated fluconazole for general fungal infection prophylaxis in AIDS patients — not specifically for Pneumocystis treatment or prevention — so the mechanistic case for this indication remains weak despite the volume of loosely related literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000676](https://clinicaltrials.gov/study/NCT00000676) | Phase 3 | Completed | 500 | Randomized comparison of fluconazole vs. clotrimazole troches for prevention of serious fungal infection in AIDS/ARC patients (nested in ACTG 081); the only trial directly involving fluconazole, but targets broad fungal prophylaxis, not Pneumocystis specifically (Relevance: A) |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Randomized trial of three anti-Pneumocystis regimens plus zidovudine for primary PCP prevention in advanced HIV; regimens traditionally exclude fluconazole (Relevance: B) |
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Rezafungin vs. standard antimicrobial regimen for invasive fungal disease prevention post-transplant; different drug/mechanism (echinocandin) (Relevance: C) |
| [NCT00892359](https://clinicaltrials.gov/study/NCT00892359) | Phase 2 | Unknown | 10 | Pharmacokinetics of anidulafungin during CVVH; different drug, echinocandin class active against fluconazole-resistant strains (Relevance: C) |
| [NCT02651038](https://clinicaltrials.gov/study/NCT02651038) | Phase 4 | Completed | 10 | Pharmacokinetics of micafungin during CVVHDF; different drug (Relevance: C) |
| [NCT01042704](https://clinicaltrials.gov/study/NCT01042704) | Phase 1 | Completed | 29 | Bendamustine + lenalidomide + dexamethasone in relapsed multiple myeloma; unrelated to antifungal therapy, likely linked via opportunistic-infection risk in the study population (Relevance: C) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | GVHD prophylaxis platform trial post-transplant; not targeted at pneumocystosis (Relevance: C) |

**Note:** Only NCT00000676 directly involves fluconazole, and it does not specifically test efficacy against *Pneumocystis*.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and Pneumocystis pneumonia; notes fluconazole prophylaxis reduces invasive candidiasis in high-risk haemato-oncology patients (most directly relevant) |
| [8818831](https://pubmed.ncbi.nlm.nih.gov/8818831/) | 1996 | Review | J Antimicrob Chemother | Treatment of fungal infections in AIDS, including fluconazole use for mucosal candidiasis |
| [30508854](https://pubmed.ncbi.nlm.nih.gov/30508854/) | 2018 | Review | Dtsch Med Wochenschr | Update on opportunistic infection management; TMP-SMX remains standard for PCP prophylaxis/treatment |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clin Evid | Primary/secondary prophylaxis for HIV-related opportunistic infections |
| [16288352](https://pubmed.ncbi.nlm.nih.gov/16288352/) | 2005 | Review | Klin Padiatr | Diagnosis/management of fungal infections and PCP in pediatric cancer patients |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infection after lung transplantation, including antifungal strategies |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | Prophylaxis/treatment of infection in bone marrow transplant recipients |
| [15826284](https://pubmed.ncbi.nlm.nih.gov/15826284/) | 2005 | Review | Mycoses | Invasive fungal infections after liver transplantation |
| [11418871](https://pubmed.ncbi.nlm.nih.gov/11418871/) | 2001 | Review | Clin Infect Dis | CDC/IDSA/ASBMT guidelines summary for preventing opportunistic infections after HSCT |
| [29514232](https://pubmed.ncbi.nlm.nih.gov/29514232/) | 2018 | Review | Clin Infect Dis | WHO guidelines for managing advanced HIV disease in a public health approach |

None of the above are RCTs specifically testing fluconazole against pneumocystosis; all are reviews providing contextual/background support only.

---

## South Africa Market Information

Fluconazole has **0 SAHPRA registrations** in this dataset and is recorded as **not marketed** in South Africa. No product-level registration data is available for review.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Note: TFDA/local warning and contraindication data, and DDI data, are flagged as a blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Despite L3 evidence (7 trials, 20 publications), only one trial directly involves fluconazole, and it does not specifically address Pneumocystis efficacy; the mechanistic rationale is weak because *P. jirovecii* is intrinsically non-susceptible to azole antifungals, and the TxGNN score likely reflects an "opportunistic infection" knowledge-graph clustering artifact rather than true pharmacological plausibility.
- The model's top-ranked candidate (punctate epithelial keratoconjunctivitis) was excluded from this report due to zero supporting evidence and an explicit contraindicating rationale in the source data.

**To proceed, the following is needed:**
- Resolution of the blocking data gap: TFDA/SAHPRA-equivalent PI warnings and contraindications (currently unavailable, prevents S1 safety assessment)
- Confirmed mechanism-of-action data for fluconazole (currently a data gap)
- A dedicated in vitro/preclinical study confirming (or refuting) fluconazole activity against *Pneumocystis jirovecii*, given standard-of-care already exists (TMP-SMX, dapsone, pentamidine, atovaquone)
- Re-evaluation of lower-ranked candidates only if new trial or literature evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

