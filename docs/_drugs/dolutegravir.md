---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir is an integrase strand transfer inhibitor (INSTI) used in combination antiretroviral therapy for HIV-1 infection in humans. The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**, with **5 clinical trials** (conducted in human HIV-1 subjects, providing indirect mechanistic support) and **1 direct animal study publication** currently identified. Evidence remains at the preclinical stage, with no dedicated feline clinical trials registered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection — combination antiretroviral therapy (inferred from drug class; no SAHPRA registration data available in this Evidence Pack) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

FIV (Feline Immunodeficiency Virus) is a lentivirus that causes progressive immune dysfunction in domestic cats, clinically paralleling HIV-1 infection in humans. Both viruses belong to the lentivirus genus, and their integrase enzymes share the conserved DDE catalytic triad — the active site where INSTI drugs like dolutegravir bind to block viral integration into the host genome. This structural conservation forms the primary mechanistic basis for the TxGNN model's prediction, and is biologically plausible.

One direct animal study (Kim et al., *Viruses*, 2023) demonstrated that a combination ART regimen including dolutegravir (2.5 mg/kg) alongside tenofovir and emtricitabine could be administered to FIV-infected domestic cats, providing initial proof-of-concept for pharmacokinetic feasibility in the target species. However, comprehensive efficacy and safety data in cats remain unavailable, and no formal Phase 1+ feline clinical trial has been registered.

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, dolutegravir inhibits lentiviral integrase via its conserved DDE motif. This mechanism is present in FIV integrase, but species-specific susceptibility data (in vitro EC₅₀ against FIV integrase) and formal feline pharmacokinetic studies are still required before any clinical translation can be recommended. This prediction should be treated as a well-grounded research hypothesis rather than a ready-to-implement repurposing candidate.

---

## Clinical Trial Evidence

No clinical trials specifically targeting FIV in cats were identified. The following trials were conducted in human HIV-1 subjects and provide indirect mechanistic support for dolutegravir's integrase inhibitory activity.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir 50 mg QD non-inferior to raltegravir 400 mg BID in ART-experienced, INSTI-naïve HIV-1 adults over 48 weeks; demonstrates potent integrase inhibitory activity |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir 50 mg QD non-inferior to raltegravir in ART-naïve adults over 96 weeks; confirms high genetic barrier to resistance, relevant to FIV given similar INSTI resistance pathways |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Optimal once-daily dose selection (50 mg QD) established; provides human PK/PD reference parameters for inter-species dose modelling |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Dolutegravir demonstrates high CNS penetration (high CPE score) in HIV-1 adults — directly relevant as FIV causes neurological disease similar to HIV-associated neurocognitive disorders |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine superior to Atripla over 96 weeks in ART-naïve adults; confirms sustained virological suppression with once-daily dosing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Animal/Observational Study | *Viruses* | The only identified study directly evaluating dolutegravir in FIV-infected cats: combination ART (dolutegravir 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) administered to specific pathogen-free FIV-infected domestic cats; assessed pharmacokinetics and immunophenotypic clinical outcomes — proof-of-concept for feasibility in the target species |

---

## South Africa Market Information

No SAHPRA registrations for dolutegravir were identified in this Evidence Pack.

> **Important note for healthcare professionals:** This finding is inconsistent with dolutegravir's global regulatory profile, where it holds approvals in over 100 countries including major African markets, and is widely used in national HIV programmes. Healthcare professionals should verify current SAHPRA registration status directly via the [SAHPRA online medicines database](https://www.sahpra.org.za) before drawing any conclusions from this data. The zero-registration finding may reflect a data retrieval gap rather than an actual absence of registration.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA via the MedSafety app or the [SAHPRA ADR reporting portal](https://www.sahpra.org.za).

> **Additional safety note specific to the predicted feline indication:** Feline dosing for dolutegravir has not been established through formal veterinary clinical trials. The single available animal study used 2.5 mg/kg in cats, but comprehensive tolerability data are absent. Known human safety concerns — including hypersensitivity reactions, hepatotoxicity, and neural tube defects with periconceptional exposure — require independent evaluation in feline species before veterinary use can be considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is at L4 (preclinical/mechanistic level) — the mechanistic basis for INSTI activity against FIV integrase is biologically sound, but only one small pharmacokinetic/observational animal study involving dolutegravir in FIV-infected cats has been published. No registered Phase 1+ feline clinical trials exist, and comprehensive species-specific safety and efficacy data are unavailable.

**To proceed, the following is needed:**

- **In vitro susceptibility data**: EC₅₀ and CC₅₀ of dolutegravir specifically against FIV integrase (not HIV-1 surrogate)
- **Feline pharmacokinetic study**: Species-specific PK profiling in healthy cats to establish an appropriate dose range and confirm adequate plasma exposure
- **Pilot safety/efficacy study**: Structured study in FIV-infected cats (Phase 1 equivalent), with defined endpoints for virological suppression and immune recovery (CD4+ T-cell count)
- **Regulatory pathway clarification**: Determine whether this falls under SAHPRA veterinary medicine regulations (Act 36 of 1947) or off-label use provisions for veterinary practitioners
- **MOA data retrieval**: Obtain mechanism of action details from DrugBank (DB08930) to formally document integrase inhibitory pharmacology in the Evidence Pack
- **Safety gap remediation**: Retrieve SAHPRA/TFDA Professional Information (PI) to complete safety assessment (currently blocking items DG001 and DG002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

