---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Original Indication (Not Specified in Evidence Pack) to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF, DB00688) is an immunosuppressant whose original indication is not documented in this evidence pack. The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **10 clinical trials** and **20 publications** currently identified, though only a small subset directly test MMF as an HIV therapy and results are largely inconclusive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| South Africa Market Status | Not Marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this drug is not available in the current evidence pack (data gap DG002). Based on the mechanistic rationale in the underlying prediction, MMF inhibits proliferation of activated T lymphocytes. Theoretically, this could reduce the pool of activated CD4+ T cells — the primary cellular target of HIV infection — and MMF has previously been explored as an adjunct to HAART to modulate the chronic immune hyperactivation seen in HIV disease.

However, this is an immunomodulatory mechanism rather than a direct antiviral one, and the original indication for this drug is not recorded here, so the relationship between the original indication and this new predicted indication cannot be assessed from the evidence pack alone.

Clinical evidence for MMF specifically in HIV is mixed: the MAN2 study (NCT00120419, Phase 4) directly tested MMF in untreated chronically HIV-1-infected patients but remains listed as UNKNOWN status with no confirmed outcome. Several smaller pharmacokinetic/cohort studies (e.g., PMID 12352149, 15213566) suggest MMF combined with certain antiretrovirals (notably abacavir) can transiently reduce plasma HIV-1 RNA via depletion of intracellular deoxyguanosine triphosphate, but sample sizes are small and findings have not been confirmed in a definitive controlled trial. Most of the higher-enrollment trials in the evidence set (transplant/GVHD studies) use MMF for its established immunosuppressive purpose in HIV-positive patients rather than as HIV therapy itself, and are only indirectly relevant.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT in HIV-positive patients; MMF used as GVHD prophylaxis, not as HIV treatment |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 Study: tests whether MMF reduces chronic immune hyperactivation and slows CD4+ T-cell decline in ART-naive HIV patients; no confirmed result on record |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | DAPD vs. DAPD+MMF in treatment-experienced HIV patients; direct antiviral combination study |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide, sirolimus and MMF for GVHD prophylaxis in hematologic malignancies |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | MMF as adjunct to abacavir in treatment-failure HIV patients; withdrawn before enrollment, no data generated |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy evaluating MMF's effect on cardiovascular surrogate markers in HIV-1 infection |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation in HIV-infected patients with end-stage renal disease; MMF used for rejection prophylaxis |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Clinical/immunological follow-up after renal transplantation in HIV-1-infected patients; immunosuppressive regimen includes MMF |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Thiotepa/busulfan/fludarabine conditioning for haplo-HSCT in elderly AML patients; MMF used for GVHD prophylaxis, not HIV-specific |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine+MMF vs. cyclophosphamide+prednisolone for anti-EPO-associated PRCA; not related to HIV indication |

No South African National Clinical Trials Register (SANCTR) or Pan African Clinical Trials Registry (PACTR) entries were identified in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF's effect on immune response and plasma/lymphatic viral load during and after HAART interruption in chronic HIV infection |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical study | AIDS | HAART with or without MMF in treatment-naive HIV-1 patients; effect on plasma RNA decay and latent reservoir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | No detrimental immunological effects observed with MMF added to HAART in treatment-naive acute/chronic HIV-1 patients |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort/PK | Clin Pharmacokinet | Pharmacokinetics/pharmacodynamics of low-dose MMF in HIV patients treated with abacavir, efavirenz and nelfinavir |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK/PD study | Clin Pharmacokinet | Effect of MMF on pharmacokinetics of antiretrovirals and intracellular nucleoside triphosphate pools |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort | J Acquir Immune Defic Syndr | Addition of MMF to abacavir-containing ART associated with dGTP depletion and decreased plasma HIV-1 RNA |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | MMF as a component of multidrug-resistant HIV-1 salvage therapy in 7 heavily pre-treated AIDS patients |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study | AIDS | Amdoxovir (DAPD) with or without MMF in drug-resistant HIV infection |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Review of immunosuppressive drugs, including MMF, in HIV disease and immune activation |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Mechanistic/translational | J Clin Invest | Selective targeting of HIV-infected clonal CD4+ T cells by antiproliferative drugs (mechanistic rationale for antiproliferative approaches, including MMF-class agents) |

---

## South Africa Market Information

Mycophenolate mofetil currently has no SAHPRA registrations on record in this evidence pack; market status is **Not Marketed** (0 registered products).

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. Report adverse drug reactions to SAHPRA.

*Note: A Blocking data gap (DG001) was identified — TFDA/SAHPRA-equivalent product labelling (warnings and contraindications) is not currently available, which prevents completion of the initial safety screening (Stage S1) for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a plausible but indirect immunomodulatory mechanism, and the most directly relevant trial (MAN2, NCT00120419) has no confirmed outcome (status: Unknown). Combined with a Blocking data gap on safety labelling and the drug's absence from the South African market (0 SAHPRA registrations), the evidence is not yet sufficient to proceed even with guardrails.

**To proceed, the following is needed:**
- SAHPRA-equivalent Professional Information (warnings, contraindications) to close the Blocking safety gap (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Outcome data from the MAN2 study (NCT00120419) and its cardiovascular substudy (NCT00247494)
- Assessment of a South African market-entry pathway, since the product is not currently registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

