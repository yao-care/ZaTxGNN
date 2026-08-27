---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

Using **txgnn-pipeline** context (Evidence Pack → drug repurposing report) is not applicable here — this is a direct report-writing task per the given prompt, so I'll proceed to draft it directly.

Note before the report: this Evidence Pack has an unusual profile — the top-ranked predicted indication is *simian immunodeficiency virus infection* (an animal-model disease, not a human clinical indication), original indication/MOA fields are data gaps, and the drug is unregistered in South Africa. I've flagged this transparently in the report rather than glossing over it.

---

# Emtricitabine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) internationally approved for HIV-1 infection as part of antiretroviral therapy; this specific Evidence Pack does not contain original-indication or SAHPRA licensing data for it. The TxGNN model predicts a link to **Simian Immunodeficiency Virus (SIV) Infection**, but this is a non-human primate disease model rather than a human clinical target, supported only by **2 clinical trials** (neither testing emtricitabine directly) and **20 publications** (mostly macaque pre-exposure prophylaxis studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (no SAHPRA license text); internationally approved for HIV-1 infection as part of combination antiretroviral therapy |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, emtricitabine is an NRTI that inhibits the reverse transcriptase of lentiviruses; its efficacy in HIV-1 infection (including pre-exposure prophylaxis, PrEP) is well established internationally.

SIV is the macaque-model analogue of HIV, and its reverse transcriptase shares high homology with HIV's — this is almost certainly why the TxGNN knowledge graph placed the two nodes close together, producing a very high similarity score (0.999). However, SIV infection itself is an animal-model disease, not a human clinical indication that SAHPRA (or any regulator) could approve a product for. The supporting literature consistently reflects this: nearly all cited studies are macaque PrEP/chemoprophylaxis experiments using emtricitabine (usually combined with tenofovir) to prevent SHIV/SIV acquisition — i.e., evidence reinforcing emtricitabine's *existing* human HIV-PrEP role, not evidence of a new "SIV treatment" indication.

Given this, the prediction is best read as the model correctly recognizing HIV/SIV mechanistic proximity, rather than surfacing a genuinely novel, actionable human indication.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Studied raltegravir (not emtricitabine) HIV/SIV decay kinetics; withdrawn with zero enrollment — low relevance, likely a knowledge-graph adjacency artifact |
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Studied vedolizumab + antiretroviral therapy for HIV virological remission; does not test emtricitabine specifically, very small cohort |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT/Review | Pharmacotherapy | Reviews systemic HIV pre-exposure prophylaxis evidence (incl. iPrEx-related human data); supports established FTC/TDF PrEP use, not SIV treatment specifically |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal Study | Nature Communications | Oral FTC/TAF plus long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques with early treatment initiation |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal Study | J Infect Dis | Oral TAF/FTC combination prevented vaginal SHIV infection in macaques (PrEP model) |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Animal Study | J Infect Dis | Vaginally administered FTC/tenofovir gel protected macaques against repeated rectal SHIV exposure (cross-compartment protection) |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Study | J Infect Dis | Oral FTC + tenofovir alafenamide chemoprophylaxis protected macaques from rectal SHIV infection |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal Study | J Infect Dis | Combination FTC/TDF prevented vaginal SHIV infection in macaques even with Chlamydia/Trichomonas coinfection |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal Study | AIDS Res Hum Retroviruses | HIV vaccine combined with partial oral FTC/TDF PrEP prevented SHIV infection in macaques and primed immunity |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal Study | J Infect Dis | Oral FTC/TDF prevented transmission of a tenofovir-resistant SHIV strain (K65R mutation) in macaques |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Basic Virology | J Virology | Examined SIVagm dynamics in African green monkeys under tenofovir/emtricitabine ART; natural-host model without disease progression |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Basic Virology | J Virology | M184V resistance mutation reduced SIV fitness/virulence in macaques treated with lamivudine or emtricitabine |

## South Africa Market Information

Emtricitabine is currently **not registered with SAHPRA** (0 licenses on record in this Evidence Pack).

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA. (Key warnings, contraindications, and drug-interaction data were not available in this Evidence Pack — flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication — SIV infection — is a non-human primate disease model, not a valid human clinical target, and evidence level is L4 (mechanistic/preclinical only). No trial or publication directly tests emtricitabine's efficacy against SIV as a treatment indication; all relevant literature instead supports emtricitabine's existing human HIV-PrEP role.

**To proceed, the following is needed:**
- SAHPRA-approved Professional Information (PI) — warnings, contraindications, DDI (currently Blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Reassessment of whether the intended repurposing target should instead be a human-equivalent indication (e.g., HIV-1 PrEP or treatment), since "SIV infection" itself is not a regulatable human indication
- SAHPRA registration/import pathway assessment, since the drug is currently not marketed in South Africa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

