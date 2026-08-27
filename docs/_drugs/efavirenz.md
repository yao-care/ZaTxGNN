---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for HIV-1 infection.
> The TxGNN model predicts a **99.80% score** for "Simian Immunodeficiency Virus (SIV) Infection" as a new indication,
> but the supporting evidence — **1 clinical trial** (unrelated drug, withdrawn) and **16 publications** — consists entirely of preclinical animal-model research, not evidence of treating a distinct human disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (established antiretroviral use; not extractable from South African regulatory data below, see Market Status) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical/animal-model studies only; no relevant completed human RCT) |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently not available in the evidence pack (Data Gap DG002). Based on known pharmacology, efavirenz is an NNRTI that binds an allosteric pocket on HIV-1 reverse transcriptase (RT), a mechanism specific to the HIV-1 enzyme structure.

Critically, the predicted "new indication" here is not a distinct human disease — it is simian immunodeficiency virus (SIV) infection, the primate counterpart of HIV. Wild-type SIV RT is naturally **not** sensitive to NNRTIs like efavirenz because its binding pocket differs structurally from HIV-1 RT. The literature evidence base consists of studies using an artificially engineered "RT-SHIV" chimeric virus, in which researchers replaced SIV's own RT with HIV-1 RT specifically so that NNRTI-based regimens (including efavirenz) could be tested in a macaque model of HIV/AIDS. This is a research-tool model built to study human HIV pathophysiology and drug resistance in animals — it is not evidence that efavirenz treats naturally occurring SIV infection in its own right.

In other words, the TxGNN model has likely picked up on efavirenz's known antiretroviral mechanism and associated it with a taxonomically adjacent viral disease label, rather than identifying a genuinely novel indication outside the drug's existing pharmacological class.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Studied decay kinetics of HIV/SIV using the integrase inhibitor **raltegravir**, not efavirenz; trial withdrawn with zero enrollment. Relevance graded C — different drug class, no usable data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Imaging/pharmacology study | Antimicrob Agents Chemother | Mass spectrometry imaging of antiretroviral distribution and viral RNA in spleens of ART-treated nonhuman primates |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal model study | Antimicrob Agents Chemother | Enhanced 4/5-drug HAART regimens improved RT-SHIV viral decay kinetics in rhesus macaques |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Animal model/virology | J Virol | Allele-specific PCR detection of pre-existing drug-resistant RT-SHIV variants in macaques |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Virology/sequence analysis | J Virol | Genetic diversity of RT-SHIV persists in macaques despite antiretroviral therapy, including short-course efavirenz monotherapy |
| [21289110](https://pubmed.ncbi.nlm.nih.gov/21289110/) | 2011 | Basic virology | J Virol | Mechanistic study of HIV-1/SIV Gag-Pol interaction with clathrin; not a treatment study |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal model study | Retrovirology | RT-SHIV subpopulation dynamics in macaques during short-course efavirenz monotherapy followed by combination ART |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model study | Virology | Vaginal transmission characterization of RT-SHIV in Chinese rhesus macaques |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal model study | J Virol | HAART regimen (efavirenz + lamivudine + tenofovir) suppressed viral load in RT-SHIV-infected rhesus macaques |
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal model study | Antimicrob Agents Chemother | Evaluated efavirenz antiviral activity specifically in the RT-SHIV chimeric macaque model (engineered for NNRTI susceptibility) |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro virology | J Virol | In vitro characterization of the RT-SHIV chimera used to study antiviral resistance in pigtail macaques |

*Note: all listed studies are preclinical (tier 3, animal/in vitro models). None constitute clinical evidence in humans or naturally SIV-infected animals.*

---

## South Africa Market Information

Efavirenz currently has **no SAHPRA registration records** in this evidence pack (0 registrations; market status: not marketed). No product-level licence data is available to summarise.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*(Key warnings, contraindications, and drug interaction data are marked as data gaps in the evidence pack — DG001, severity Blocking — and could not be summarised here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only clinical trial identified is for a different drug (raltegravir) and was withdrawn with zero enrollment; it provides no support for this indication.
- All 16 literature references are preclinical animal studies using an engineered RT-SHIV chimeric virus — a research tool designed to make SIV artificially susceptible to NNRTIs like efavirenz, not evidence that efavirenz treats naturally occurring SIV infection.
- SAHPRA safety data (PI warnings, contraindications, drug interactions) is entirely unavailable (DG001, Blocking severity) and mechanism-of-action documentation is missing (DG002), so this candidate cannot pass an initial safety screen (S1).
- Efavirenz is not currently marketed in South Africa (0 SAHPRA registrations).

**To proceed, the following is needed:**
- SAHPRA-approved PI (warnings, contraindications, drug interactions) to clear the Blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source
- Evidence of clinical relevance to an actual human/veterinary disease population, since the current "new indication" largely reflects a taxonomic variant of efavirenz's existing approved use rather than a distinct disease
- SAHPRA market authorisation status confirmation if commercial availability in South Africa is being considered

*Note: two additional TxGNN-predicted indications for efavirenz (feline immunodeficiency virus infection, and a rare genetic neurodevelopmental disorder) were also reviewed and carry even weaker evidence (Evidence Level L5 — model prediction only, with no or minimally relevant supporting studies); both are also recommended Hold.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

