---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Fungal Infections (Candidiasis) to Vulvovaginitis

## One-Sentence Summary

> Nystatin is a polyene antifungal originally used to treat *Candida* (yeast) infections of the skin and mucous membranes.
> The TxGNN model predicts it may be effective for **Vulvovaginitis**,
> with **0 registered clinical trials** but **20 publications** currently supporting this direction.
> Note: the evidence pack contains no SAHPRA-specific indication text or product information for Nystatin, as it is currently **not marketed** in South Africa.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (candidiasis) — based on established pharmacological knowledge; no SAHPRA-specific indication text is available (drug not marketed in South Africa) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% (rank 729) |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap DG002). Based on well-established pharmacological knowledge, Nystatin is a **polyene antifungal** that binds directly to ergosterol in the fungal cell membrane, forming pores that cause leakage of intracellular contents and fungal cell death. Its efficacy against *Candida* species in fungal infections has been proven for decades.

Vulvovaginitis — and vulvovaginal candidiasis specifically — is estimated to be the second most common cause of vaginitis after bacterial vaginosis, with *Candida albicans* accounting for 85–90% of cases (PMID 25775428, 19454049). Because the causative organism of most vulvovaginitis cases is the same fungal genus Nystatin was developed against, the mechanistic link here is direct rather than speculative: this is closer to a well-established off-label/legacy use than a novel biological hypothesis.

Historically, Nystatin was in fact a first-line topical treatment for vulvovaginal candidiasis before being largely superseded by imidazole and triazole antifungals due to convenience of dosing (PMID 1436934). Contemporary literature also positions Nystatin as a relevant alternative in **fluconazole-resistant** vulvovaginal candidiasis (PMID 39771534, 32104010), suggesting renewed clinical interest where azole resistance is a concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | In vitro fluconazole and nystatin susceptibility correlated with clinical outcome in 283 patients with complicated VVC (287 *Candida* isolates) |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In vitro study | Infection and Drug Resistance | Nystatin (and ZnO nanoparticles) downregulated SAP1-3 virulence gene expression in fluconazole-resistant *C. albicans* isolates from VVC |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Animal study | BMC Microbiology | Nystatin enhanced mucosal immune response and protected vaginal epithelial ultrastructure in a rat model of VVC |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | Vaginal combination therapy with nystatin and nifuratel evaluated for mixed/miscellaneous vulvovaginitis |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | Comparative study | J Infect Dev Ctries | Compared tea tree oil (5%, 10%) and nystatin inhibition zones against vaginal *Candida* isolates in pregnancy |
| [1436934](https://pubmed.ncbi.nlm.nih.gov/1436934/) | 1992 | Review | Obstet Gynecol Clin North Am | Reviews topical antifungals; notes nystatin was the original 1950s treatment for VVC, later surpassed by imidazoles/triazoles |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Update on fluconazole-resistant VVC management; nystatin discussed among alternative antifungal therapies |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Womens Health | Reviews boric acid for recurrent VVC, with nystatin as comparator context in azole-resistant disease |
| [4919155](https://pubmed.ncbi.nlm.nih.gov/4919155/) | 1970 | Review | Med Clin North Am | General clinical review of nystatin pharmacology and use |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | Epidemiology of vulvovaginal candidiasis; *C. albicans* causes 85-90% of cases |

---

## South Africa Market Information

Nystatin currently has **0 SAHPRA registrations** and is **not marketed** in South Africa. No product listings, registration numbers, or approved indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: This evidence pack flags a blocking data gap (DG001) — no regulatory warnings/contraindications data was available for review — meaning a formal safety assessment (S1 stage) has not yet been completed for this candidate.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and long-established — *Candida* species cause the majority of vulvovaginitis cases, and Nystatin's antifungal action against *Candida* is well documented in 20 supporting publications, including data on efficacy against fluconazole-resistant strains. However, no clinical trials specifically test Nystatin in vulvovaginitis, and the drug is not currently registered in South Africa, so this remains guarded rather than a clear "Go."

**To proceed, the following is needed:**
- Regulatory PI (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- A SAHPRA registration/importation pathway assessment, since the product is not currently marketed in South Africa
- Ideally, a prospective clinical trial or comparative study against standard-of-care azole antifungals for vulvovaginitis in a South African population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

