---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atazanavir: From HIV-1 Infection to Congenital HIV Prevention

> **Editorial note:** Among the six TxGNN-predicted indications for atazanavir, predictions ranked 1–4 target animal diseases (feline AIDS, simian immunodeficiency virus) or obsolete/artefactual ontology terms unsuitable for clinical action. This report focuses on **Rank 5 — Congenital Human Immunodeficiency Virus** — which carries the highest evidence grade (L1) and is directly actionable within South Africa's national PMTCT programme.

---

## One-Sentence Summary

Atazanavir (Reyataz®, BMS-232632) is an HIV-1 protease inhibitor used globally as part of combination antiretroviral therapy for adults and children with HIV infection, but currently not registered with SAHPRA in South Africa.
The TxGNN model predicts it may be effective for **congenital human immunodeficiency virus** (prevention of mother-to-child HIV transmission), with **25 clinical trials** and **7 publications** currently supporting this direction.
This is the highest-evidence prediction across all TxGNN outputs for this drug and is directly relevant to South Africa's national PMTCT programme.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection in adults and paediatric patients (based on international regulatory approvals; not currently SAHPRA-registered) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus (Perinatal HIV Prevention / PMTCT) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| South Africa Market Status | Not marketed |
| Number of SAHPRA Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, atazanavir is an **azapeptide HIV-1 protease inhibitor** that competitively binds the active site of the HIV-1 protease enzyme, blocking cleavage of the gag-pol polyprotein into functional structural and replication proteins. This prevents viral maturation and halts the production of new infectious HIV-1 virions. When pharmacokinetically boosted with low-dose ritonavir (ATV/r), atazanavir achieves sustained therapeutic plasma concentrations with once-daily dosing, making it suitable for long-term regimens including pregnancy.

The mechanistic link between HIV-1 treatment and prevention of congenital HIV is direct: preventing mother-to-child transmission (MTCT) requires achieving undetectable maternal viral load (<50 copies/mL) through effective HAART during pregnancy, delivery, and the breastfeeding period. ATV/r suppresses HIV-1 replication through the same mechanism as in standard adult treatment, and its pharmacokinetics during pregnancy have been prospectively validated — PMID 24992294 confirms that adequate ATV exposure is maintained throughout pregnancy irrespective of concomitant tenofovir use. Both WHO and DHHS guidelines list ATV/r as an acceptable alternative PMTCT regimen, particularly for women who were virologically stabilised on ATV/r prior to conception.

In South Africa, where antenatal HIV prevalence exceeds 30% in several provinces and PMTCT is a national health priority, the availability of alternative PI-based regimens is clinically important — especially for pregnant women with NNRTI resistance or intolerance to standard first-line regimens. The PRINCE I and PRINCE II Phase 3 trials established safety and pharmacokinetic data for ATV/r in children as young as 3 months, reinforcing the overall perinatal safety profile. The primary safety concern specific to neonates is hyperbilirubinaemia, as atazanavir inhibits UGT1A1 (the main enzyme for neonatal bilirubin conjugation), necessitating bilirubin monitoring in newborns whose mothers received ATV/r during pregnancy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | **PRINCE II:** Safety, efficacy and PK of ATV powder + ritonavir in HIV-infected children aged 3 months to <11 years; established weight-based paediatric dosing guidelines |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | **PRINCE I:** ATV powder + ritonavir safety, efficacy and PK in children aged ≥3 months to <6 years; confirmed adequate drug exposure in infants and young children |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | Long-term safety of ATV capsule + ritonavir in HIV-infected paediatric patients aged 6 to <18 years; real-world safety dataset |
| [NCT00326716](https://clinicaltrials.gov/study/NCT00326716) | Phase 1 | Completed | 69 | PK of ATV/ritonavir in HIV-1 infected pregnant women; determined adequate dosing regimen during pregnancy compared to historical non-pregnant data |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1578 | **IMPAACT P1026s:** Largest prospective PK study of ARV drugs (including ATV) in pregnant women and infants; also evaluated PK in postpartum women starting hormonal contraceptives |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Completed | 205 | Updated PK data for ARV drugs including ATV during pregnancy and postpartum (2021–2025) |
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Completed | 571 | Phase 3 trial of ATV/r or ATV/SQV versus LPV/r, each with TDF + NRTI, in treatment-experienced HIV patients; established ATV/r efficacy in boosted PI-based HAART |
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1057 | **CASTLE:** 96-week head-to-head comparison of ATV/r versus LPV/r + TDF/FTC in treatment-naïve HIV subjects; ATV/r demonstrated non-inferior antiviral efficacy with better lipid profile |
| [NCT00207142](https://clinicaltrials.gov/study/NCT00207142) | Phase 4 | Completed | 252 | **INDUMA:** ATV/r induction followed by unboosted ATV maintenance; supports long-term ATV virological durability |
| [NCT01232127](https://clinicaltrials.gov/study/NCT01232127) | Phase 4 | Completed | 25 | Effect of famotidine (H2-receptor antagonist) on ATV/r + TDF pharmacokinetics in HIV-infected patients; directly relevant for managing acid-suppression drug interactions during antenatal care |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Prospective PK Study | *Antiviral Therapy* | ATV exposure remains pharmacologically adequate throughout pregnancy irrespective of concomitant tenofovir; supports continuation of standard ATV/r dosing (300/100 mg once daily) during pregnancy |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Retrospective Cohort | *JAMA Pediatrics* | Congenital anomaly rates in HIV-exposed uninfected infants with various in utero ARV exposures; provides comparative safety signal data for ATV-containing regimens |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort (SMARTT) | *Frontiers in Immunology* | PHACS SMARTT multicentre study (n>3,500 HIV-exposed infants): comprehensive assessment of in utero ARV toxicities across metabolic, cardiac, neurological, neurodevelopmental, and hearing domains |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Cross-Sectional | *Journal of AIDS and Immune Research* | Newborn hearing screening referral rates in HIV-exposed uninfected infants enrolled in SMARTT; evaluates association between specific ARV exposures (including ATV) and hearing risk |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In Vitro Mechanistic | *Reproductive Toxicology* | First study characterising ATV and ritonavir interactions with placental ABC efflux transporters (P-gp/ABCB1, BCRP/ABCG2, MRP2/ABCC2); higher congenital anomaly risk associated with impaired placental efflux |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance Analysis | *Clinical Infectious Diseases* | Multi-database pharmacovigilance review of ARV safety in pregnancy; provides comparative safety context for PI-based versus INSTI-based regimens and informs signal interpretation |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Case/Non-case Study | *European Journal of Clinical Pharmacology* | European congenital anomaly registry analysis (most recent data): congenital anomaly risk following fetal exposure to ARV drugs including protease inhibitors; case/non-case design strengthens causal inference |

---

## South Africa Market Information

Atazanavir is **not currently registered with SAHPRA**. There are no active product licences in South Africa.

> **Note for clinicians:** Atazanavir is approved internationally under the brand name **Reyataz®** (Bristol-Myers Squibb) and is **WHO-prequalified in generic form** by manufacturers including Aurobindo, Mylan/Viatris, and others. In South Africa, clinical use would currently require one of the following pathways:
>
> 1. **SAHPRA Section 21 authorisation** — unregistered medicines access for individual patients or named-patient/compassionate-use programmes
> 2. **Full product registration** by an originator or WHO-prequalified generic manufacturer
> 3. **Procurement via PEPFAR or Global Fund channels** using WHO-prequalified generic formulations
>
> The South African Essential Medicines List (EML) does not currently include atazanavir. South Africa's national ART guidelines use dolutegravir-based regimens as preferred first-line therapy; ATV/r would primarily serve as an alternative for women with documented NNRTI resistance or intolerance.

---

## Safety Considerations

Please refer to the SAHPRA-approved Professional Information (PI) for safety information. As atazanavir is not currently SAHPRA-registered, consult the **FDA or EMA prescribing information** (Reyataz®) and the **WHO Model Formulary** for complete prescribing guidance. Report adverse drug reactions to SAHPRA via the MedSafety reporting portal.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 clinical trials, a large prospective pregnancy pharmacokinetics dataset (IMPAACT P1026s, n=1,578), and paediatric safety data from the PRINCE I and PRINCE II Phase 3 trials collectively provide L1 evidence for the use of atazanavir/ritonavir in the context of perinatal HIV management. The drug is mechanistically well-suited to PMTCT and is recognised in international guidelines. The primary barrier to clinical use in South Africa is the absence of SAHPRA registration, which must be resolved before ATV/r can be routinely prescribed.

**To proceed, the following is needed:**

- **Regulatory pathway:** Initiate a SAHPRA Section 21 application for compassionate use, or support a WHO-prequalified generic manufacturer to apply for full SAHPRA registration
- **Procurement assessment:** Evaluate availability and cost of WHO-prequalified generic ATV/r through PEPFAR, the Global Fund, or the National Department of Health's revolving drug fund
- **Safety documentation:** Retrieve the complete FDA/EMA prescribing information for ATV/r, including full boxed warnings, contraindications, pregnancy and lactation sections, and drug interaction tables
- **MOA data:** Obtain the complete DrugBank pharmacological and mechanistic profile (DB01072) to formalise the mechanistic justification for regulatory submission
- **Neonatal monitoring protocol:** Develop local guidance for bilirubin monitoring in neonates born to mothers on ATV/r (UGT1A1 inhibition risk), aligned with South African neonatal jaundice management pathways
- **EML submission:** Prepare a dossier for the National Essential Medicines Committee (NEMLC) to evaluate ATV/r as an alternative PMTCT option for women with NNRTI resistance or intolerance
- **National guideline alignment:** Engage with the National Department of Health to assess whether ATV/r should be incorporated into the South African ART and PMTCT guidelines as a preferred second-line or alternative agent

---

*This report is intended for research and clinical decision-support purposes only. It does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data current as of 4 April 2026.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

