---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamivudine: From Original Indication (Not on File) to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

The original indication and mechanism of action for lamivudine are not present in this evidence pack (flagged as data gaps DG001/DG002), so the usual "original vs. new indication" comparison cannot be made with confidence. The TxGNN model's top-ranked signal, **feline acquired immunodeficiency syndrome (FIV)**, is a **veterinary indication**, not a human one, and none of the five predicted indications in this pack currently constitute an actionable human drug-repurposing candidate — every candidate is scored **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no SAHPRA/regulatory licence records or indication text in this evidence pack (data gap) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — a veterinary, non-human indication |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lamivudine is currently unavailable in this pack (DG002, High severity), and no original indication is recorded in the South African regulatory extract. Without these two anchors, mechanistic plausibility cannot be assessed in the standard way, and this itself is a material limitation of the current data cut.

The pack's own rationale for the top-ranked candidate is instructive: lamivudine (3TC) is a nucleoside reverse transcriptase inhibitor, and FIV — like HIV — is a lentivirus, so in vitro and small-cohort veterinary studies do show cross-species antiretroviral activity. However, the evidence pack explicitly notes this is a **veterinary indication that falls outside the scope of human drug repurposing**, which is the platform's intended use case.

The remaining candidates are similarly non-actionable. Simian immunodeficiency virus infection (rank 2) is likewise a non-human primate indication with zero supporting trials or literature (L5, pure model inference). The rare neurodevelopmental disorder (rank 3) has no known biological link to reverse-transcriptase inhibition and is judged a likely embedding-space false positive. "Obsolete familial combined hyperlipidemia" (rank 4) is flagged in the disease ontology itself as an obsolete term with no mechanistic rationale. Chronic hepatitis C virus infection (rank 5) has the largest evidence volume (16 trials, 20 publications) but the pack's own mechanistic analysis concludes lamivudine has **no known direct antiviral activity against HCV**, an RNA virus that replicates via RNA-dependent RNA polymerase rather than reverse transcriptase — the high score is attributed to semantic clustering around "viral hepatitis" (HBV and HCV are frequently discussed together) rather than a genuine pharmacological signal.

## Clinical Trial Evidence

The trials retrieved against the top-ranked candidate (FIV) are shown below. **Important caveat**: all five were matched purely on the drug name "lamivudine" — every one is a human HIV trial; none is an actual feline/FIV trial. They should not be read as clinical support for the FIV indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir + NRTI backbone in ART-naïve HIV-1 adults. **Not relevant** — human HIV trial, species/indication mismatch (relevance grade C). |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. other regimens in HIV-1-naïve adults. **Not relevant** — human HIV trial (relevance grade C). |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dolutegravir dose-selection with abacavir/lamivudine or tenofovir/emtricitabine in ART-naïve HIV-1 adults. Human HIV trial; relevance not yet assessed. |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Dolutegravir + abacavir/lamivudine, CNS and plasma PK, in ART-naïve HIV-1 adults. Human HIV trial; relevance not yet assessed. |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs. Atripla in ART-naïve HIV-1 adults. Human HIV trial; relevance not yet assessed. |

## Literature Evidence

Unlike the clinical trials above, the literature retrieved for FIV is genuinely on-topic (veterinary studies of lamivudine/3TC in cats).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort | Journal of Feline Medicine and Surgery | Long-term antiretroviral therapy follow-up in FIV-infected cats treated initially with zidovudine (AZT). |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort | Viruses | Evaluated zidovudine, zidovudine+lamivudine, and other antiretroviral protocols in naturally FIV-infected cats in late asymptomatic stage; assessed viral load and CD4+/CD8+ ratios over one year. |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Review | Veterinary Immunology and Immunopathology | In vitro/in vivo evaluation of AZT/3TC (lamivudine) combination against FIV; additive-to-synergistic anti-FIV activity in primary PBMCs. |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Cohort | Antiviral Research | Combined zidovudine, lamivudine and abacavir suppress FIV replication in vitro; supports the cat/FIV model as an analogue for HIV research. |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | American Journal of Veterinary Research | Characterized FIV-pPPR molecular clone and two 3TC-resistant pol gene mutants; in vitro replication and nucleoside analogue susceptibility. |

## Other TxGNN-Predicted Indications (Screened, Not Prioritized)

| Rank | Disease | TxGNN Score | Evidence Level | Trials / Literature | Key Note |
|------|---------|------|------|------|------|
| 2 | Simian immunodeficiency virus infection | 99.93% | L5 | 0 / 0 | Non-human primate indication; no supporting evidence; pure model inference. |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, decreased cortical white matter | 99.93% | L5 | 0 / 0 | Rare genetic disorder with no known mechanistic link to reverse-transcriptase inhibition; likely a false positive. |
| 4 | Obsolete familial combined hyperlipidemia | 99.63% | L5 | 0 / 0 | Disease ontology term itself is flagged obsolete; no mechanistic rationale. Recommend exclusion from further review. |
| 5 | Chronic hepatitis C virus infection | 99.11% | L4 | 16 / 20 | Largest evidence volume of all candidates, but pack's own analysis finds no plausible mechanism (HCV is an RNA virus, not reverse-transcriptase dependent); several matched trials are actually about hepatitis B, not C. Likely a semantic-clustering artifact. |

## South Africa Market Information

Lamivudine is currently **not marketed** in South Africa according to this evidence pack, with **0 registrations** on file. No SAHPRA registration records, product names, or approved-indication text are available to populate a registration table.

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

Note: warnings, contraindications, and drug-drug interaction data are recorded as an unresolved, **Blocking**-severity data gap (DG001) in this pack, meaning safety review (S1 stage) cannot proceed until the TFDA/SAHPRA PI is retrieved and parsed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this pack is independently scored "Hold" at decision stage S0. The top four candidates are not viable human repurposing signals — one is a genuine but veterinary-only mechanism (FIV), one is a non-human primate indication with no evidence, one is a rare genetic disorder with no mechanistic link, and one is built on an obsolete ontology term. The fifth (hepatitis C), despite having the most trial/literature volume, is mechanistically implausible by the pack's own analysis. Compounding this, the drug's original indication, MOA, and safety data are all missing, and it is not currently marketed in South Africa.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the TFDA/SAHPRA Professional Information for warnings/contraindications before any safety review can begin
- Resolve DG002: query DrugBank for confirmed mechanism of action
- Establish the drug's confirmed original indication(s) from an authoritative regulatory source
- If pursuing the hepatitis C signal further, obtain independent mechanistic or pharmacology review to confirm or refute the TxGNN association before any evidence-collection investment
- Re-run TxGNN scoring/triage once MOA and original-indication data are populated, since current L5-level candidates were generated without that context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

