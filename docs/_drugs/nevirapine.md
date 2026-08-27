---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 3
---

# Nevirapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the drug-repurposing evaluation report format from the task prompt (no specialized skill applies — this is a direct content-generation task from a supplied template and JSON evidence pack).

# Nevirapine: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

> Nevirapine is a first-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) established for HIV-1 antiretroviral therapy (this evidence pack contains no SAHPRA regulatory record confirming a local original indication).
> The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
> with **no clinical trials** and **17 preclinical/mechanistic publications** currently associated with this direction — and several of those publications actually report NNRTI resistance in SIV.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI antiretroviral) — general pharmacological knowledge; not confirmed by any SAHPRA registration record in this evidence pack |
| Predicted New Indication | Simian immunodeficiency virus (SIV) infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (data gap DG002). Based on known pharmacology, nevirapine is a first-generation NNRTI that binds a hydrophobic pocket specific to HIV-1 reverse transcriptase (RT), blocking viral replication; its efficacy in HIV-1 infection is well established.

SIV and HIV-1 belong to the same "immunodeficiency virus" family and share substantial sequence and structural homology, which plausibly explains why the TxGNN knowledge-graph embedding clustered them together and produced a high similarity score. However, the underlying literature evidence undermines this prediction mechanistically: two in vitro resistance-profiling studies (PMID 7541200, PMID 15040537) specifically report that native SIV and HIV-2 RT are largely **resistant** to first-generation NNRTIs such as nevirapine, because the NNRTI binding pocket is not well conserved outside HIV-1 RT. The chimeric/humanized SIV models that do respond to nevirapine (e.g., RT-SHIV constructs, PMID 15564466, 19195672, 11375059) do so only because they carry an engineered HIV-1 RT gene, not native SIV RT.

Taken together, this prediction is best read as a knowledge-graph clustering artifact driven by disease-entity similarity rather than genuine pharmacological plausibility against wild-type SIV. SIV infection is also primarily a non-human primate research/veterinary model used to study HIV pathogenesis and drug resistance, not a recognized human clinical indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro resistance profiling | Biochem Biophys Res Commun | Chimeric SIV carrying HIV-1 RT is sensitive to NNRTIs, but native SIV RT is not — indicates NNRTI specificity for HIV-1 RT |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility comparison | Antiviral Therapy | Evaluated 16 approved anti-HIV-1 drugs against HIV-2, SIV and SHIV strains; informs treatment/PEP applicability across strains |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro chimeric virus characterization | Journal of Virology | Characterized SIV-HIV chimera expressing HIV-1 RT to study NNRTI antiviral resistance in pigtail macaques |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model (macaque) transmission study | Virology | RT-SHIV (HIV-1 RT in SIV backbone) transmits efficiently via vaginal route in rhesus macaques, supporting its use as a resistance-study model |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model resistance development | AIDS Research and Human Retroviruses | RT-SHIV-infected cynomolgus monkeys used to study emergence/reversal of RT-inhibitor drug resistance in vivo |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro combination study | Antimicrob Agents Chemother | Diketo integrase-inhibitor derivative tested in combination with zidovudine, **nevirapine**, or nelfinavir against SIV(MAC251); combinations were subsynergistic |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review/clinical commentary (non-SIV) | Annals of Emergency Medicine | Reviews nonoccupational HIV post-exposure prophylaxis; cites animal SIV studies as indirect support, not direct nevirapine-SIV data |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | In vitro antiviral screening | Chemical Biology & Drug Design | Novel small molecule 3G11 blocks HIV-1 RT but does **not** inhibit SIV(mac), HIV-2, or other lentiviruses — illustrates HIV-1 RT specificity |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro antiviral screening | Antiviral Chemistry & Chemotherapy | Fluoroquinolone derivative K-12 shows broad-spectrum activity against HIV-1, HIV-2 and SIV strains at the transcriptional level |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | In vitro virion pretreatment study | Virology | HIV-1 and SIV virions pretreated with NRTIs/NNRTIs to test inhibition of endogenous reverse transcription as a potential microbicide strategy |

---

## South Africa Market Information

No SAHPRA-registered products for nevirapine are recorded in this evidence pack (0 registrations; market status: **Not marketed**). Regulatory/product-level data (registration numbers, brand names, approved indication text) is a data gap (DG001, Blocking) and must be sourced from the SAHPRA register/PI directly before any repurposing pathway can proceed.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence is limited to preclinical/mechanistic studies (L4) with no clinical trials, and the strongest mechanistic evidence (PMID 7541200, 15040537) indicates that wild-type SIV reverse transcriptase is naturally **resistant** to first-generation NNRTIs like nevirapine — the high TxGNN score likely reflects disease-entity clustering ("immunodeficiency virus" family) rather than true pharmacological plausibility. SIV is also not a human clinical indication. The two lower-ranked candidates in this pack (feline immunodeficiency syndrome — a veterinary indication with a single structural-comparison paper; and a rare neurodevelopmental white-matter disorder — L5, no supporting evidence at all) are equally unsupported and also recommended Hold.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI (blocking data gap DG001)
- Confirmed mechanism of action detail from DrugBank/primary literature (DG002)
- A validated human-relevant target indication, since SIV infection itself has no human clinical application
- If pursuing a genuine HIV/AIDS-adjacent repurposing hypothesis, re-run prediction/evidence review against clinically relevant disease terms (e.g., specific opportunistic infections or HIV treatment-adjacent conditions) rather than the animal-model entity "SIV infection"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

