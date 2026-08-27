---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

Using the report as specified by the Evidence Pack schema. This pack is a **multi-indication** candidate file (`TW-DB00643-multi`) — TxGNN returned 10 predicted indications for Mebendazole, but only 2 of them (both in the *Echinococcus* family) carry real literature/trial support; the other 8 are flagged in the pack's own `repurposing_rationale` as mechanistically implausible or likely noise. I've built the report around the credible signal and surfaced the rest transparently rather than mechanically headlining the single highest TxGNN score (which is "acne," explicitly annotated in the pack as a probable database mis-association).

# Mebendazole: From Antiparasitic Therapy to Echinococcosis

## One-Sentence Summary

> Mebendazole is a benzimidazole anthelmintic; the evidence pack in front of it returns 10 TxGNN-predicted indications, but only **Echinococcus granulosus infection (cystic echinococcosis)** and **alveolar echinococcosis (E. multilocularis)** are backed by real literature and trial data — the other 8 candidates (including the highest-scoring "acne" prediction) are flagged by the model's own rationale as mechanistically implausible or likely noise.
> For the two credible indications, **7–20 publications** and **1 completed observational trial** support mebendazole's established (not truly novel) role as an alternative to albendazole in echinococcosis chemotherapy.
> Mebendazole is currently **not marketed in South Africa**, and safety/PI data are missing, so no SAHPRA safety pathway can yet be assessed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (MOA and original indication are flagged as Data Gaps — see below) |
| Predicted New Indication | Echinococcosis — cystic (*Echinococcus granulosus*) and alveolar (*E. multilocularis*) |
| TxGNN Prediction Score | 95.61% (cystic echinococcosis) / 94.20% (alveolar echinococcosis) |
| Evidence Level | L3 (observational studies / reviews) for both |
| South Africa Market Status | Not marketed (0 SAHPRA registrations) |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails *(contingent on resolving the blocking safety data gap below)* |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Mebendazole is not available in this evidence pack (Data Gap DG002). Based on established pharmacology, Mebendazole is a **benzimidazole anthelmintic** that inhibits β-tubulin polymerization in helminth (worm) cells, blocking microtubule assembly and glucose uptake in the parasite — this is the same mechanistic class as albendazole.

*Echinococcus granulosus* and *E. multilocularis* are cestode (tapeworm) parasites, and their larval stages cause cystic and alveolar echinococcosis (hydatid disease), respectively. Because Mebendazole's target (parasitic β-tubulin) is directly present in these organisms, the mechanistic link is strong and direct — considerably stronger than a typical "novel" repurposing hypothesis. In fact, multiple reviews in the evidence set (e.g., PMID 25526545, PMID 19254162) confirm that benzimidazoles (albendazole and mebendazole) are **already the WHO-recommended chemotherapy backbone** for both cystic and alveolar echinococcosis. This means the TxGNN prediction largely reconfirms known, guideline-level pharmacology rather than surfacing an unexpected new use — which is itself a useful validation signal for the model, but tempers the "repurposing novelty" framing.

By contrast, the model's 8 other predictions (acne, diffuse cutaneous leishmaniasis, hordeolum, inhalational/toxin-mediated botulism, impetigo, Sorsby's fundus dystrophy, and demodicidosis) have no plausible mechanistic connection to an antihelminthic microtubule inhibitor, and the pack's own rationale text flags the top-ranked "acne" association as most likely a **database/ontology labeling error** (the only supporting literature hit is an unrelated sparganosis case report), and the Sorsby's fundus dystrophy hit as **likely model noise**. These are detailed in "Other Predicted Indications" below rather than omitted, but should not be acted on.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Phase NA | Completed | 50 | Observational follow-up study of hepatic alveolar echinococcosis patients treated with benzimidazole therapy (albendazole), evaluating parasite viability biomarkers and imaging for guiding treatment withdrawal decisions. Graded "B" relevance — it monitors benzimidazole-treated patients rather than directly testing mebendazole efficacy. |

For cystic echinococcosis (*Echinococcus granulosus*), no registered clinical trials were found in ClinicalTrials.gov or ICTRP for this drug-disease pair.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2585032](https://pubmed.ncbi.nlm.nih.gov/2585032/) | 1989 | Cohort/Clinical case series | J Chemother | 70 patients with hydatid cysts (150 cysts, 13 disseminated cases) treated with mebendazole per WHO protocol; morphological/volumetric improvement in 64.3% over 6mo–5yr follow-up |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | Parasite | Reviews albendazole and mebendazole as the established chemotherapy for alveolar and cystic echinococcosis; surveys candidate next-generation compounds |
| [19254162](https://pubmed.ncbi.nlm.nih.gov/19254162/) | 2009 | Review/Consensus | Expert Rev Anti Infect Ther | Consensus statement on benzimidazole use for cystic and alveolar echinococcosis |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Comparative study/Review | J Antimicrob Chemother | 35 alveolar echinococcosis patients on mebendazole or albendazole followed ~39 months; compares treatment regimens and outcomes |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Case report | J Hepatol | 13-year continuous mebendazole therapy (45–48 mg/kg/day) in non-resectable hepatic alveolar echinococcosis, suggesting parasitocidal (not just parasitostatic) potential with long-term dosing |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | Animal pharmacokinetic study | Eur J Clin Pharmacol | Plasma mebendazole concentrations >0.25 µmol/L correlated with reduced parasite weight in infected jirds; informs human dosing rationale |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Current management of liver echinococcosis; surgery as cornerstone, benzimidazoles as adjunct/alternative therapy |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | Acta Tropica | Status of novel treatment options for alveolar and cystic echinococcosis; notes albendazole/mebendazole remain the only licensed non-surgical options |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite | Notes benzimidazoles (albendazole/mebendazole) are parasitostatic, not curative, and can cause liver dysfunction — supports need for monitoring |
| [19296876](https://pubmed.ncbi.nlm.nih.gov/19296876/) | 2009 | Review | J Helminthol | Benzimidazoles used alone or peri-surgically for AE/CE; notes in vivo efficacy limitations against alveolar disease specifically |

---

## South Africa Market Information

Mebendazole currently has **no SAHPRA registrations** and is not marketed in South Africa (`market_status: 未上市`, `total_licenses: 0`). No product, dosage form, or approved-indication data is available to summarize.

---

## Other Predicted Indications (Low Confidence — Not Recommended)

For transparency, the remaining 8 TxGNN predictions in this evidence pack scored high but have no supporting evidence and were judged Hold/L5 by the model's own rationale:

| Disease | TxGNN Score | Evidence | Rationale Summary |
|---|---|---|---|
| Acne (disease) | 99.20% | 1 unrelated literature hit (sparganosis case report) | Likely database/ontology mislabeling; no mechanistic link to anthelmintic action |
| Leishmaniasis, diffuse cutaneous | 98.38% | None | Protozoan (not helminth) target; no evidence |
| Hordeolum | 94.88% | None | Bacterial eyelid infection; no mechanistic link |
| Inhalational botulism | 93.82% | None | Neurotoxin-mediated disease; no mechanistic link |
| Toxin-mediated infectious botulism | 93.52% | None | Same as above |
| Impetigo | 93.22% | None | Bacterial skin infection; no mechanistic link |
| Sorsby's fundus dystrophy | 93.13% | None | Genetic retinal disease; flagged as likely model noise |
| Demodicidosis of sebaceous gland | 92.99% | None | Theoretically plausible (ectoparasite), but zero supporting evidence — preclinical validation needed before any further action |

None of these should be pursued without new supporting data.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

**Note:** Local (SAHPRA) product warnings, contraindications, and drug-interaction data are currently a **blocking data gap (DG001)** — the evidence pack cannot proceed to initial safety assessment (S1) without this information. This must be resolved before any further decision-making on this candidate.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Echinococcosis indications only; blocked pending resolution of DG001)*

**Rationale:**
- The mechanistic link between Mebendazole and echinococcosis is strong and already reflected in international treatment guidelines (this is a re-confirmation of known pharmacology rather than a novel discovery), supported by observational cohort data (PMID 2585032) and consistent review-level consensus.
- However, Mebendazole has zero SAHPRA registrations and no local safety/PI data, and the evidence pack itself marks the missing TFDA/SAHPRA warning and contraindication data (DG001) as a **Blocking** severity gap — meaning this candidate cannot legitimately clear even a preliminary safety screen (S1) yet, despite the two credible indications reaching decision stage S2 on efficacy grounds.
- The other 8 predicted indications should be disregarded; they lack any supporting mechanism or evidence and are likely model artifacts.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, precautions, and contraindications (DG001, Blocking)
- Formal mechanism-of-action documentation from DrugBank or equivalent source (DG002, High)
- A defined regulatory pathway for a currently unregistered drug in South Africa (import/registration route)
- If pursued clinically for echinococcosis: baseline and monitoring plan for hepatotoxicity, given benzimidazole-class hepatic dysfunction signals noted in the literature (e.g., PMID 39311470)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

